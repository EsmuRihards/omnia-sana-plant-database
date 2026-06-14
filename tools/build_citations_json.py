#!/usr/bin/env python3
"""
build_citations_json.py - Omnia Sana "Knowledge Finder" data builder.

Reads the canonical citation database (bibliography.bibtex) and the per-species
plant YAML files in plants/, and emits a single public-safe citations.json that
the website's Knowledge Finder tool consumes (WordPress pulls it on a WP-cron
schedule, caches it, and serves it from /wp-json/omniasana/v1/citations).

PUBLIC-SAFE BY DESIGN: only bibliographic metadata + plant/action linkage is
emitted. internal_notes, contraindication prose, and draft-only fields are
intentionally NOT included, so this file is safe to publish even if the rest of
the database stays private.

No timestamp is embedded, so the file only changes in git when the underlying
data changes (clean diffs / idempotent CI). WordPress records its own sync time.

Stdlib only - no third-party dependencies. Run from anywhere:
    python tools/build_citations_json.py
"""

import json
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")
PLANTS_DIR = os.path.join(ROOT, "plants")
OUT = os.path.join(ROOT, "citations.json")

REF_RE = re.compile(r"REF-\d{3,}")
FIELD_START_RE = re.compile(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*")


def _clean(s):
    """Light cleanup of common BibTeX/LaTeX artifacts for display/search."""
    if not s:
        return ""
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_")
    s = s.replace("``", '"').replace("''", '"')
    s = re.sub(r"[{}]", "", s)          # leftover grouping braces
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_fields(body):
    """Parse `field = {value}` / `field = "value"` pairs from an entry body,
    brace-balanced so values may span multiple lines."""
    fields, i, n = {}, 0, len(body)
    while i < n:
        m = FIELD_START_RE.match(body, i)
        if not m:
            i += 1
            continue
        key, j = m.group(1).lower(), m.end()
        if j >= n:
            break
        ch = body[j]
        if ch == "{":
            depth, k = 0, j
            while k < n:
                if body[k] == "{":
                    depth += 1
                elif body[k] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                k += 1
            val, i = body[j + 1:k], k + 1
        elif ch == '"':
            k = j + 1
            while k < n and body[k] != '"':
                k += 1
            val, i = body[j + 1:k], k + 1
        else:
            k = j
            while k < n and body[k] not in ",\n":
                k += 1
            val, i = body[j:k], k
        fields[key] = _clean(val)
    return fields


def parse_bibtex(text):
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
        etype, key, body = m.group(1).lower(), m.group(2).strip(), m.group(3)
        f = extract_fields(body)
        mref = REF_RE.search(f.get("note", ""))
        entries.append({
            "type": etype,
            "key": key,
            "ref_id": mref.group(0) if mref else "",
            "fields": f,
        })
    return entries


def load_plant_index():
    """REF id -> {plants, scientific, actions} (reference_ids are plant-level)."""
    inv = {}
    if not os.path.isdir(PLANTS_DIR):
        sys.stderr.write("WARNING: plants/ dir not found at %s\n" % PLANTS_DIR)
        return inv
    for fn in sorted(os.listdir(PLANTS_DIR)):
        if not fn.endswith((".yaml", ".yml")):
            continue
        txt = open(os.path.join(PLANTS_DIR, fn), encoding="utf-8").read()
        msci = re.search(r"^scientific_name:\s*(.+)$", txt, re.M)
        sci = _clean(msci.group(1)) if msci else ""
        commons = []
        mcn = re.search(r"^common_names:\s*\n((?:[ \t]*-\s*.+\n?)+)", txt, re.M)
        if mcn:
            commons = [_clean(re.sub(r"^[ \t]*-\s*", "", l))
                       for l in mcn.group(1).splitlines() if l.strip().startswith("-")]
        actions = sorted({_clean(a) for a in re.findall(r"^\s*-\s*action:\s*(.+)$", txt, re.M)})
        for r in REF_RE.findall(txt):
            d = inv.setdefault(r, {"plants": set(), "scientific": set(), "actions": set()})
            for c in commons:
                if c:
                    d["plants"].add(c)
            if sci:
                d["scientific"].add(sci)
            for a in actions:
                if a:
                    d["actions"].add(a)
    return inv


def _is_good_title(t):
    """A usable title has real words and doesn't look like a stray volume/issue
    fragment (e.g. ';6(1):20.' or ';10:1043034')."""
    if not t:
        return False
    t = t.strip()
    if t.startswith(";"):
        return False
    if re.match(r"https?://", t, re.I):
        return False
    letters = sum(c.isalpha() for c in t)
    return letters >= 6 and len(t) >= 8


def _label_from_url(u):
    """Readable label for an entry that is nothing but a URL, e.g.
    'ods.od.nih.gov - Ashwagandha HealthProfessional'."""
    m = re.match(r"https?://([^/]+)(/.*)?$", (u or "").strip(), re.I)
    if not m:
        return ""
    host = re.sub(r"^www\.", "", m.group(1))
    seg = (m.group(2) or "").rstrip("/").split("/")[-1]
    seg = re.sub(r"\.[a-z]{2,5}$", "", seg)
    seg = re.sub(r"[-_+%0-9]+", " ", seg).strip()
    return host + (" - " + seg if seg else "")


def _title_from_annote(annote):
    """Most annote strings read: Author (year) 'Title', Journal... — pull the
    first quoted segment out as the title."""
    if not annote:
        return ""
    norm = (annote.replace("‘", "'").replace("’", "'")
                  .replace("“", '"').replace("”", '"'))
    for pat in (r"'([^']{12,220})'", r'"([^"]{12,220})"'):
        m = re.search(pat, norm)
        if m:
            return m.group(1).strip().strip(".,")
    return ""


def derive_display(title, annote, authors, key, url=""):
    """Best human-readable label for a citation card. Never a bare URL."""
    if _is_good_title(title):
        return title
    alt = _title_from_annote(annote)
    if alt and not alt.lower().startswith("http"):
        return alt
    if authors and len(authors) >= 6 and not authors.lower().startswith("http"):
        return authors
    if annote:
        first = re.split(r"(?<=[.])\s", annote.strip(), 1)[0]
        if len(first) > 12 and not first.lower().startswith("http"):
            return first[:140].rstrip(" .,") + ("…" if len(first) > 140 else "")
    for cand in (url, title, annote):
        if cand and cand.lower().startswith("http"):
            lab = _label_from_url(cand)
            if lab:
                return lab
    return title if (title and not title.lower().startswith("http")) else key


def best_link(f):
    """Return (url, type) - the most resolvable source link available.
    type in {doi, url, search, none}. 'search' is a Google Scholar title query
    fallback for book-derived refs that carry no DOI/URL."""
    doi = f.get("doi", "").strip()
    url = f.get("url", "").strip()
    if doi:
        d = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi).strip()
        return "https://doi.org/" + d, "doi"
    if url:
        return url, "url"
    q = f.get("title", "").strip() or f.get("author", "").strip()
    if q:
        return "https://scholar.google.com/scholar?q=" + urllib.parse.quote(q), "search"
    return "", "none"


def main():
    if not os.path.isfile(BIB):
        sys.exit("ERROR: bibliography not found at %s" % BIB)
    entries = parse_bibtex(open(BIB, encoding="utf-8").read())
    pindex = load_plant_index()

    out = []
    for e in entries:
        f = e["fields"]
        link, link_type = best_link(f)
        pi = pindex.get(e["ref_id"], {"plants": set(), "scientific": set(), "actions": set()})
        title = f.get("title", "")
        annote = f.get("annote", "")
        out.append({
            "ref_id": e["ref_id"],
            "key": e["key"],
            "type": e["type"],
            "title": title,
            "authors": f.get("author", ""),
            "journal": f.get("journal", ""),
            "year": f.get("year", ""),
            "doi": f.get("doi", ""),
            "url": f.get("url", ""),
            "link": link,
            "link_type": link_type,
            "citation": annote,
            "abstract": f.get("abstract", ""),
            "display": derive_display(title, annote, f.get("author", ""), e["key"], f.get("url", "")),
            "plants": sorted(pi["plants"]),
            "scientific": sorted(pi["scientific"]),
            "actions": sorted(pi["actions"]),
        })

    # Newest first, then title A->Z within a year. Undated refs sink to the
    # bottom. Two stable passes: title asc, then year desc.
    def _year_key(c):
        m = re.search(r"\b(\d{4})\b", c["year"] or "")
        return int(m.group(1)) if m else 0

    out.sort(key=lambda c: c["display"].lower())
    out.sort(key=_year_key, reverse=True)

    payload = {
        "schema": "omnia-sana/knowledge-finder@1",
        "count": len(out),
        "citations": out,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
        fh.write("\n")

    linked = sum(1 for c in out if c["link_type"] in ("doi", "url"))
    withplants = sum(1 for c in out if c["plants"])
    print("Wrote %s" % OUT)
    print("  citations:           %d" % len(out))
    print("  direct source link:  %d (doi/url)" % linked)
    print("  scholar fallback:    %d" % sum(1 for c in out if c["link_type"] == "search"))
    print("  no link at all:      %d" % sum(1 for c in out if c["link_type"] == "none"))
    print("  linked to >=1 plant: %d" % withplants)


if __name__ == "__main__":
    main()
