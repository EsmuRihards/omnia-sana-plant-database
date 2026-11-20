#!/usr/bin/env python3
"""Read-only audit: citations nobody can open.

A bibliography entry with no abstract, url, doi or pmid gives a reader nothing to
check: the public source card falls back to a title search, and the Knowledge
Finder shows a bare title. That is fine for a genuine printed book (the British
Herbal Pharmacopoeia exists on paper), but it also hides modern papers that lost
their locator and papers whose study_type was never checked against the source.

The 2026-11-19 monograph-source audit missed these because it only looked at ref
sets that were all clinical or all preclinical; an unreadable 1978 study tagged
`traditional` sat as the sole source for field restharrow's habitat and harvest.

This script lists:
  1. every locatorless ref (no abstract, url, doi, pmid), with how often it is cited;
  2. every plant entry (any field except internal_notes, at any depth) whose
     reference_ids are ALL locatorless refs.

It never edits data. A flag is a lead to read, not a verdict: a locatorless print
monograph can be a perfectly good source.

    python scripts/audit_locatorless_refs.py [out.tsv]
"""
import os
import re
import sys
from collections import Counter

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCATORS = ("abstract", "url", "doi", "pmid")


def field_value(block, name):
    """Return the raw value of a bibtex field, or '' if absent or empty."""
    m = re.search(r"^\s*%s\s*=\s*\{(.*?)\}\s*,?\s*$" % name, block, re.M | re.S)
    return m.group(1).strip() if m else ""


def load_bib():
    """REF id -> {key, type, study_type, title, year, locatorless}."""
    text = open(os.path.join(ROOT, "bibliography.bibtex"), encoding="utf-8").read()
    out = {}
    for block in re.split(r"\n(?=@)", text):
        m = re.search(r"note\s*=\s*\{(REF-\d+)\}", block)
        head = re.match(r"@(\w+)\{([^,]+),", block)
        if not m or not head:
            continue
        has = {f: bool(field_value(block, f)) for f in LOCATORS}
        out[m.group(1)] = {
            "key": head.group(2),
            "type": head.group(1).lower(),
            "study_type": field_value(block, "study_type").lower(),
            "title": re.sub(r"[{}\s]+", " ", field_value(block, "title")).strip(),
            "author": re.sub(r"\s+", " ", field_value(block, "author"))[:60],
            "year": field_value(block, "year"),
            "venue": re.sub(r"\s+", " ", field_value(block, "journal")
                            or field_value(block, "publisher")
                            or field_value(block, "booktitle"))[:60],
            "locatorless": not any(has.values()),
        }
    return out


def walk(node, path):
    """Yield (path, entry) for every dict carrying reference_ids, skipping internal_notes."""
    if isinstance(node, dict):
        if "reference_ids" in node:
            yield path, node
        for k, v in node.items():
            if k == "internal_notes":
                continue
            yield from walk(v, "%s.%s" % (path, k) if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, "%s[%d]" % (path, i))


def label(entry):
    for k in ("condition", "action", "name", "drug_class", "compound", "partner",
              "plant", "form", "part", "id"):
        v = entry.get(k)
        if isinstance(v, str) and v:
            return v
    return ""


def main(out_path):
    bib = load_bib()
    dead = {r for r, b in bib.items() if b["locatorless"]}
    cites = Counter()
    rows = []
    for fn in sorted(os.listdir(os.path.join(ROOT, "plants"))):
        if not fn.endswith(".yaml"):
            continue
        rec = yaml.safe_load(open(os.path.join(ROOT, "plants", fn), encoding="utf-8"))
        pid = rec.get("id", fn[:-5])
        for path, e in walk(rec, ""):
            refs = e.get("reference_ids") or []
            for r in refs:
                if r in dead:
                    cites[r] += 1
            if refs and all(r in dead for r in refs):
                text = e.get("text") or e.get("note") or e.get("description") or ""
                rows.append({
                    "plant": pid,
                    "field": path.split("[")[0].split(".")[0],
                    "path": path,
                    "label": label(e),
                    "status": e.get("status", ""),
                    "refs": ",".join(refs),
                    "study_types": ",".join(bib[r]["study_type"] or "?" for r in refs),
                    "snippet": re.sub(r"\s+", " ", str(text))[:160],
                    "ref_titles": " | ".join(bib[r]["title"][:90] for r in refs),
                })
    # Section 1: the locatorless refs themselves.
    ref_cols = ["ref", "key", "type", "study_type", "year", "author", "venue",
                "cited_entries", "title"]
    # Section 2: entries cited only to them.
    cols = ["plant", "field", "path", "label", "status", "refs", "study_types",
            "snippet", "ref_titles"]
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("# section 1: refs with no abstract/url/doi/pmid\n")
        f.write("\t".join(ref_cols) + "\n")
        for r in sorted(dead, key=lambda x: int(x[4:])):
            b = bib[r]
            row = dict(b, ref=r, cited_entries=cites[r])
            f.write("\t".join(str(row[c]).replace("\t", " ") for c in ref_cols) + "\n")
        f.write("\n# section 2: plant entries whose reference_ids are ALL locatorless\n")
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]).replace("\t", " ") for c in cols) + "\n")
    print("locatorless refs: %d (%d cited somewhere)" % (len(dead), sum(1 for r in dead if cites[r])))
    print("entries cited ONLY to them: %d across %d plants"
          % (len(rows), len({r["plant"] for r in rows})))
    for k, n in Counter(r["field"] for r in rows).most_common():
        print("  %-24s %d" % (k, n))
    print("  by study_type of the refs:", dict(Counter(
        bib[r]["study_type"] or "?" for r in dead)))
    print("  wrote", out_path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "locatorless_refs_audit.tsv")
