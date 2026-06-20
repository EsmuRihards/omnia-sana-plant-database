#!/usr/bin/env python3
"""
enrich_lib_2026_06_20.py — shared, idempotent helper for the 2026-06-20
"least-cited plants" enrichment (add 3 PubMed sources to each of the 50 plants
with the fewest references).

Each batch script (enrich_bN_2026_06_20.py) defines a SOURCES list and calls
apply(SOURCES). Re-running is safe:
  * a source whose citekey already exists in bibliography.bibtex reuses its
    REF-id (no duplicate entry, no new id burned);
  * new sources get the next sequential REF-id and a formatted @article block
    appended to bibliography.bibtex;
  * each plant's new REF-ids are union-added to a plant-level `references:`
    bucket (inserted just before `provenance:`), provenance gains `+pubmed`,
    last_updated -> 2026-06-20, and a one-line provenance note is appended to
    internal_notes (guarded by a marker so re-runs don't duplicate it).

Plant YAML is dumped with the SAME config the entity-migration used
(sort_keys=False, allow_unicode=True, default_flow_style=False, width=100),
which round-trips the existing files byte-for-byte, so diffs show only changes.

Source dict shape:
  {"citekey": str, "plant": "<plant_file_stem>", "study_type": str,
   "fields": {"author","title","journal","year","volume","number","pages","doi","url"},
   "abstract": str (optional)}
study_type in {systematic-review, meta-analysis, rct, clinical, preclinical, traditional}
"""
import os, re, glob, html, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIB = os.path.join(ROOT, "bibliography.bibtex")
PLANTS = os.path.join(ROOT, "plants")

FIELD_ORDER = ["author", "title", "journal", "year", "volume", "number", "pages", "doi", "url"]
NOTE_MARKER = "2026-06-20: added 3 PubMed-sourced references"


def clean_text(s):
    """Decode HTML entities, strip braces (would break the bibtex brace parser),
    collapse whitespace."""
    if not s:
        return ""
    s = html.unescape(s)
    s = s.replace("{", "(").replace("}", ")")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fmt_entry(citekey, ref_id, study_type, fields, abstract):
    lines = ["@article{%s," % citekey]
    body = []
    for k in FIELD_ORDER:
        v = clean_text(fields.get(k, ""))
        if v:
            body.append("  %s = {%s}" % (k.ljust(8), v))
    body.append("  %s = {%s}" % ("note".ljust(8), ref_id))
    body.append("  %s = {%s}" % ("study_type".ljust(8), study_type))
    ab = clean_text(abstract)
    if ab:
        body.append("  %s = {%s}" % ("abstract".ljust(8), ab))
    return lines[0] + "\n" + ",\n".join(body) + "\n}\n"


def existing_citekeys(text):
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def citekey_to_ref(text):
    out = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", text, re.S):
        r = re.search(r"REF-\d{4,}", m.group(2))
        if r:
            out[m.group(1)] = r.group(0)
    return out


def max_ref(text):
    ids = [int(x) for x in re.findall(r"REF-(\d{4,})", text)]
    return max(ids) if ids else 0


def insert_before(d, newkey, newval, beforekey):
    """Return a new dict with newkey inserted immediately before beforekey."""
    if newkey in d and beforekey in d:
        # already present; just update value handled by caller
        pass
    out = {}
    inserted = False
    for k, v in d.items():
        if k == newkey:
            continue  # we'll place it at the desired spot
        if k == beforekey and not inserted:
            out[newkey] = newval
            inserted = True
        out[k] = v
    if not inserted:
        out[newkey] = newval
    return out


def apply(sources):
    bib = open(BIB, encoding="utf-8").read()
    have = existing_citekeys(bib)
    c2r = citekey_to_ref(bib)
    nextid = max_ref(bib) + 1

    appended = []
    plant_refs = {}   # plant stem -> [ref_id,...] in source order
    for s in sources:
        ck = s["citekey"]
        if ck in have:
            ref_id = c2r.get(ck)
        else:
            ref_id = "REF-%04d" % nextid
            nextid += 1
            appended.append(fmt_entry(ck, ref_id, s["study_type"], s["fields"], s.get("abstract", "")))
            have.add(ck)
            c2r[ck] = ref_id
        plant_refs.setdefault(s["plant"], [])
        if ref_id not in plant_refs[s["plant"]]:
            plant_refs[s["plant"]].append(ref_id)

    if appended:
        if not bib.endswith("\n"):
            bib += "\n"
        bib = bib.rstrip("\n") + "\n\n" + "\n".join(appended)
        open(BIB, "w", encoding="utf-8").write(bib)

    changed_plants = []
    for stem, refs in plant_refs.items():
        path = os.path.join(PLANTS, stem + ".yaml")
        d = yaml.safe_load(open(path, encoding="utf-8"))
        bucket = list(d.get("references", []))
        added = [r for r in refs if r not in bucket]
        bucket.extend(added)
        d = insert_before(d, "references", bucket, "provenance")
        prov = str(d.get("provenance", "")).strip()
        if "pubmed" not in prov:
            d["provenance"] = (prov + "+pubmed") if prov else "pubmed"
        d["last_updated"] = "2026-06-20"
        notes = d.get("internal_notes", "") or ""
        if NOTE_MARKER not in notes:
            sentence = (" | %s to the plant-level references bucket (least-cited "
                        "enrichment): %s." % (NOTE_MARKER, ", ".join(refs)))
            d["internal_notes"] = (notes.rstrip() + sentence) if notes else sentence.lstrip(" |").strip()
        out = yaml.safe_dump(d, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
        open(path, "w", encoding="utf-8").write(out)
        changed_plants.append((stem, refs))

    print("bibliography: %d new entries appended (next id now REF-%04d)" % (len(appended), nextid))
    for stem, refs in changed_plants:
        print("  %-32s + %s" % (stem, ", ".join(refs)))
    return changed_plants
