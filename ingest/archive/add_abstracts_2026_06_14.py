#!/usr/bin/env python3
"""
add_abstracts_2026_06_14.py - populate `abstract` fields for scientific articles.

For every @article entry in bibliography.bibtex that does not yet carry an
`abstract` field, this script retrieves the official abstract and inserts it as a
standard BibTeX `abstract = {...}` field, immediately after the `note` line.

Retrieval order (first hit wins):
  1. Europe PMC  by DOI    (exact match on the DOI; safest)
  2. Europe PMC  by title  (only accepted if the returned title is highly
                            similar to ours -> guards against wrong matches)
  3. Crossref    by DOI    (JATS abstract, tags stripped)

DESIGN
------
* IDEMPOTENT: entries that already have a non-empty `abstract` field are skipped,
  and every network lookup is cached in tools/_abstract_cache.json, so re-running
  costs (almost) no requests and never double-inserts.
* SAFE FOR THE REGEX PARSERS (build_citations_json.py / os-knowledge-finder.php):
  abstracts are stored on a single line with all braces removed and whitespace
  collapsed, so brace-depth parsing and the non-greedy `\\n}` entry terminator
  are never disturbed.
* ADDITIVE: only the new `abstract` field is inserted; no existing field, value,
  ordering or formatting is touched.
* Only @article entries are processed (the database's "scientific publication"
  type). @book and @misc (websites/blogs/fact-sheets) are reported but skipped.

Stdlib only. Run from anywhere:  python tools/add_abstracts_2026_06_14.py
Add --dry-run to fetch + report without writing the bibliography.
"""

import difflib
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")
CACHE = os.path.join(ROOT, "tools", "_abstract_cache.json")
LOG = os.path.join(ROOT, "tools", "abstracts_log_2026_06_14.txt")

UA = "OmniaSana-AbstractFetcher/1.0 (mailto:r.serafimovics@gmail.com)"
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", re.S)
FIELD_START_RE = re.compile(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*")
TITLE_SIM_THRESHOLD = 0.85
MAX_ABSTRACT = 8000          # hard cap to avoid pathological payloads
SLEEP = 0.20                 # polite delay between network calls (seconds)
DRY_RUN = "--dry-run" in sys.argv


# --------------------------------------------------------------------- parsing
def extract_fields(body):
    """Brace-balanced `field = {value}` / `"value"` / bareword parser (mirrors
    the builder so we read exactly what the tool reads)."""
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
        fields[key] = val.strip()
    return fields


def title_from_annote(annote):
    """First quoted segment of an annote reads as the title."""
    if not annote:
        return ""
    norm = (annote.replace("‘", "'").replace("’", "'")
                  .replace("“", '"').replace("”", '"'))
    for pat in (r"'([^']{12,220})'", r'"([^"]{12,220})"'):
        m = re.search(pat, norm)
        if m:
            return m.group(1).strip().strip(".,")
    return ""


def is_good_title(t):
    """A usable title has real words and is not a stray volume/issue fragment
    (e.g. ';6(1):20.') or a bare URL -- mirrors the builder's check."""
    t = (t or "").strip()
    if not t or t[0] == ";" or re.match(r"https?://", t, re.I):
        return False
    return sum(c.isalpha() for c in t) >= 6 and len(t) >= 8


def display_title(fields):
    """Prefer a real `title` field; otherwise recover the title from the annote
    (book-ingested entries park a volume/issue fragment in `title`)."""
    t = re.sub(r"[{}]", "", fields.get("title", "")).strip()
    if is_good_title(t):
        return t
    alt = re.sub(r"[{}]", "", title_from_annote(fields.get("annote", ""))).strip()
    return alt if is_good_title(alt) else (t or alt)


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def titles_match(a, b):
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    ratio = difflib.SequenceMatcher(None, na, nb).ratio()
    if ratio >= TITLE_SIM_THRESHOLD:
        return True
    short, lng = sorted((na, nb), key=len)
    return short in lng and len(short) >= 0.65 * len(lng)


def clean_abstract(s):
    """Make an abstract safe to embed in a single-line BibTeX brace value and
    pleasant to read: drop markup, unescape entities, remove braces/backslashes,
    collapse whitespace."""
    if not s:
        return ""
    s = re.sub(r"(?is)<\s*(script|style)[^>]*>.*?<\s*/\s*\1\s*>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)            # HTML / JATS tags
    s = html.unescape(s)
    s = s.replace("{", "(").replace("}", ")")  # keep brace depth intact
    s = s.replace("\\", " ")                   # neutralise stray TeX escapes
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"^abstract[:\.\s-]+", "", s, flags=re.I).strip()
    if len(s) > MAX_ABSTRACT:
        s = s[:MAX_ABSTRACT].rsplit(" ", 1)[0].rstrip(" .,;") + " …"
    return s


# ------------------------------------------------------------------ networking
def _get(url, timeout=30, tries=3):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - retry on any transport error
            last = e
            time.sleep(0.8 * (attempt + 1))
    raise last


def epmc_by_doi(doi):
    q = urllib.parse.quote('DOI:"%s"' % doi)
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s"
           "&resultType=core&format=json&pageSize=1" % q)
    res = json.loads(_get(url)).get("resultList", {}).get("result", [])
    if res and res[0].get("abstractText"):
        return res[0]["abstractText"], "europepmc:doi"
    return "", ""


def epmc_by_title(title):
    q = urllib.parse.quote('TITLE:"%s"' % title.replace('"', ""))
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s"
           "&resultType=core&format=json&pageSize=5" % q)
    for r in json.loads(_get(url)).get("resultList", {}).get("result", []):
        if r.get("abstractText") and titles_match(title, r.get("title", "")):
            return r["abstractText"], "europepmc:title"
    return "", ""


def crossref_by_doi(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    msg = json.loads(_get(url)).get("message", {})
    if msg.get("abstract"):
        return msg["abstract"], "crossref:doi"
    return "", ""


def fetch_abstract(doi, title):
    """Return (clean_abstract, source) or ('', '') if nothing reliable found."""
    if doi:
        for fn in (epmc_by_doi, crossref_by_doi):
            try:
                raw, src = fn(doi)
                if raw:
                    return clean_abstract(raw), src
            except Exception as e:  # noqa: BLE001
                sys.stderr.write("  ! %s(%s): %s\n" % (fn.__name__, doi, e))
            time.sleep(SLEEP)
    if title:
        try:
            raw, src = epmc_by_title(title)
            if raw:
                return clean_abstract(raw), src
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("  ! epmc_by_title(%.40s): %s\n" % (title, e))
        time.sleep(SLEEP)
    return "", ""


# ----------------------------------------------------------------------- main
def load_cache():
    if os.path.isfile(CACHE):
        try:
            return json.load(open(CACHE, encoding="utf-8"))
        except Exception:  # noqa: BLE001
            return {}
    return {}


def save_cache(c):
    with open(CACHE, "w", encoding="utf-8") as fh:
        json.dump(c, fh, ensure_ascii=False, indent=1, sort_keys=True)


def insert_abstract(entry_text, abstract):
    """Insert `abstract = {...}` as the last field, before the closing brace."""
    head = entry_text[:-1].rstrip()        # drop final '}' and trailing newline/space
    if head.endswith(","):
        head = head[:-1]
    return head + ",\n  abstract = {" + abstract + "}\n}"


def main():
    text = open(BIB, encoding="utf-8").read()
    cache = load_cache()
    log_lines = []

    matches = list(ENTRY_RE.finditer(text))
    articles = [m for m in matches if m.group(1).lower() == "article"]
    n_book = sum(1 for m in matches if m.group(1).lower() == "book")
    n_misc = sum(1 for m in matches if m.group(1).lower() == "misc")

    edits = []          # (start, end, new_text)
    added = already = notfound = 0
    fetched_since_save = 0

    print("Scientific publications (@article): %d  |  skipped non-articles: "
          "@book=%d @misc=%d" % (len(articles), n_book, n_misc))

    for idx, m in enumerate(articles, 1):
        key, body, full = m.group(2).strip(), m.group(3), m.group(0)
        fields = extract_fields(body)
        ref = fields.get("note", "")
        if fields.get("abstract", "").strip():
            already += 1
            continue

        doi = re.sub(r"[{}]", "", fields.get("doi", "")).strip()
        doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I).strip()
        doi = re.sub(r"/(full|abstract|pdf|html|meta|epdf)/?$", "", doi, flags=re.I).strip()
        title = display_title(fields)

        # Cache successes permanently; retry past misses (cheap, lets fixes land).
        cached = cache.get(key)
        if cached and cached.get("abstract", "").strip():
            abstract, src = cached["abstract"], cached.get("source", "cache")
        else:
            sys.stdout.write("[%3d/%3d] %-26s " % (idx, len(articles), key))
            sys.stdout.flush()
            abstract, src = fetch_abstract(doi, title)
            cache[key] = {"abstract": abstract, "source": src,
                          "doi": doi, "title": title}
            fetched_since_save += 1
            print("OK (%s, %d chars)" % (src, len(abstract)) if abstract else "-- not found")
            if fetched_since_save >= 20:
                save_cache(cache)
                fetched_since_save = 0

        if abstract:
            added += 1
            if not DRY_RUN:
                edits.append((m.start(), m.end(), insert_abstract(full, abstract)))
            log_lines.append("OK    %-26s %-7s %s | %s" % (key, ref, src, title[:80]))
        else:
            notfound += 1
            log_lines.append("MISS  %-26s %-7s doi=%s | %s"
                             % (key, ref, doi or "-", title[:80]))

    save_cache(cache)

    if edits and not DRY_RUN:
        for start, end, new in sorted(edits, key=lambda x: x[0], reverse=True):
            text = text[:start] + new + text[end:]
        with open(BIB, "w", encoding="utf-8") as fh:
            fh.write(text)

    summary = [
        "",
        "==================== ABSTRACT POPULATION SUMMARY ====================",
        "Scientific publications processed (@article): %d" % len(articles),
        "  abstracts added this run:                   %d" % added,
        "  already had an abstract:                    %d" % already,
        "  no abstract found (logged below):           %d" % notfound,
        "Non-article sources skipped: @book=%d  @misc=%d" % (n_book, n_misc),
        "Mode: %s" % ("DRY RUN (no file written)" if DRY_RUN else "wrote bibliography.bibtex"),
        "=====================================================================",
    ]
    print("\n".join(summary))

    with open(LOG, "w", encoding="utf-8") as fh:
        fh.write("\n".join(summary) + "\n\n--- per-entry ---\n")
        fh.write("\n".join(sorted(log_lines)) + "\n")
    print("Per-entry log: %s" % LOG)


if __name__ == "__main__":
    main()
