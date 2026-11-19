#!/usr/bin/env python3
"""Read-only audit: monograph fields whose only citations cannot support them.

The 2026-07-12 "monograph-base fields" campaign filled botanical_description,
habitat, harvesting, traditional_uses, preparations, dosage and constituents
"from the existing references bucket". Where that bucket held only clinical
papers, a plant's morphology, range, history or dose ended up cited to a trial
that never describes them (ginger's botanical description cited a
chemotherapy-nausea RCT until 2026-11-19).

This script flags every such entry whose reference_ids are ALL clinical-tier
(rct / clinical / meta-analysis / systematic-review / review), plus descriptive
blocks (botanical, habitat, harvesting, traditional use) cited ONLY to
preclinical lab/animal papers, and writes a ranked TSV. It never edits data. A flag is a lead to read, not a verdict: a
dosage line that says "trials used 1 g" can legitimately cite the trial.

    python scripts/audit_monograph_sources.py [out.tsv]
"""
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLINICAL = {"rct", "clinical", "meta-analysis", "systematic-review", "review"}
# Fields whose claims are about the plant itself, not about a product or a dose.
DESCRIPTIVE = {"botanical", "habitat", "harvest", "history"}

# field -> (kind, base severity). Kind is what the field asserts.
FIELDS = {
    "botanical_description": ("botanical", 3),
    "habitat": ("habitat", 3),
    "harvesting": ("harvest", 3),
    "traditional_uses": ("history", 2),
    "constituents": ("chemistry", 2),
    "preparations": ("preparation", 2),
    "dosage": ("dose", 2),
}

# Text that openly reports trial material ("capsules used in trials", "a meta-
# analysis found") can be backed by the trial itself, so it ranks lower.
TRIAL_WORDS = re.compile(
    r"\b(trial|trials|randomi[sz]ed|placebo|meta-analys[ie]s|participants|patients|"
    r"clinical stud|study used|studies used|was effective|were effective)\b", re.I)


def load_bib():
    """REF id -> {study_type, title}. Plain parser: one @entry per block."""
    text = open(os.path.join(ROOT, "bibliography.bibtex"), encoding="utf-8").read()
    out = {}
    for block in re.split(r"\n(?=@)", text):
        m = re.search(r"note\s*=\s*\{(REF-\d+)\}", block)
        if not m:
            continue
        st = re.search(r"study_type\s*=\s*\{([^}]*)\}", block)
        ti = re.search(r"title\s*=\s*\{(.*?)\},?\s*\n", block, re.S)
        out[m.group(1)] = {
            "study_type": (st.group(1).strip().lower() if st else ""),
            "title": re.sub(r"[{}\s]+", " ", ti.group(1)).strip() if ti else "",
        }
    return out


def entries(rec, field):
    """Yield (label, text, refs, status) for a dict field or a list field."""
    v = rec.get(field)
    if isinstance(v, dict):
        yield field, v.get("text", ""), v.get("reference_ids") or [], v.get("status", "")
    elif isinstance(v, list):
        for i, e in enumerate(v):
            if not isinstance(e, dict):
                continue
            label = "%s[%d] %s" % (field, i, e.get("name", ""))
            text = e.get("text") or e.get("note") or ""
            yield label.strip(), text, e.get("reference_ids") or [], e.get("status", "")


def main(out_path):
    bib = load_bib()
    rows = []
    for fn in sorted(os.listdir(os.path.join(ROOT, "plants"))):
        if not fn.endswith(".yaml"):
            continue
        rec = yaml.safe_load(open(os.path.join(ROOT, "plants", fn), encoding="utf-8"))
        sci = rec.get("scientific_name", "")
        genus = sci.split()[0].lower() if sci else ""
        for field, (kind, base) in FIELDS.items():
            for label, text, refs, status in entries(rec, field):
                if not refs:
                    continue  # unsourced is the D8 gate's job, not this audit's
                types = [bib.get(r, {}).get("study_type", "?") for r in refs]
                if all(t in CLINICAL for t in types):
                    issue, sev = "clinical-only", base
                elif kind in DESCRIPTIVE and all(t == "preclinical" for t in types):
                    # A lab or animal paper rarely describes the plant, its range
                    # or its folk history either - same bulk-ingest pattern, one
                    # step less certain (a pharmacognosy paper may), so ranked lower.
                    issue, sev = "preclinical-only", base - 1
                else:
                    continue
                if kind in ("preparation", "dose", "history") and TRIAL_WORDS.search(text or ""):
                    sev -= 1  # text openly reports trial material
                if status == "verified":
                    sev += 0.5  # shown publicly as verified: worse if wrong
                off_plant = [r for r in refs if genus and genus not in bib.get(r, {}).get("title", "").lower()]
                rows.append({
                    "severity": sev,
                    "issue": issue,
                    "plant": rec.get("id", fn[:-5]),
                    "field": label,
                    "kind": kind,
                    "status": status,
                    "refs": ",".join("%s:%s" % (r, t) for r, t in zip(refs, types)),
                    "refs_title_lacks_genus": ",".join(off_plant),
                    "snippet": re.sub(r"\s+", " ", text or "")[:160],
                    "ref_titles": " | ".join(bib.get(r, {}).get("title", "")[:90] for r in refs),
                })
    rows.sort(key=lambda r: (-r["severity"], r["issue"], r["plant"], r["field"]))
    cols = ["severity", "issue", "plant", "field", "kind", "status", "refs",
            "refs_title_lacks_genus", "snippet", "ref_titles"]
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r[c]).replace("\t", " ") for c in cols) + "\n")
    # Summary to stdout.
    from collections import Counter
    print("flagged entries: %d across %d plants" % (len(rows), len({r["plant"] for r in rows})))
    for k, n in sorted(Counter((r["issue"], r["kind"]) for r in rows).items()):
        print("  %-16s %-12s %d" % (k[0], k[1], n))
    print("  by status:", dict(Counter(r["status"] or "(none)" for r in rows)))
    print("  wrote", out_path)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "monograph_source_audit.tsv")
