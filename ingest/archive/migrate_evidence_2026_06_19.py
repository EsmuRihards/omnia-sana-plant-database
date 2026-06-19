#!/usr/bin/env python3
"""
ingest/archive/migrate_evidence_2026_06_19.py — one-shot migration.

Removes the legacy per-indication `evidence: N` field (the old hand-assigned 1-5
score) from every plants/*.yaml. The evidence score is now COMPUTED at build time
from the study types of the cited references (scripts/build.py, Option B, 1-10),
so the stored value is redundant and would otherwise drift out of sync.

Editors who need to force a value can add `evidence_override: N` (1-10) to an
indication; the build honours it verbatim.

Line-based and minimal-diff: deletes only lines that are exactly a 2-space-indented
`evidence: <int>` (the indentation every indication uses), leaving all other
formatting, comments and key order untouched. Idempotent.
Run:  python ingest/archive/migrate_evidence_2026_06_19.py
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLANTS = os.path.join(ROOT, "plants")
EVID_RE = re.compile(r"(?m)^  evidence: *\d+\n")


def main():
    files = sorted(glob.glob(os.path.join(PLANTS, "*.yaml")))
    changed, removed = 0, 0
    for path in files:
        text = open(path, encoding="utf-8").read()
        new, n = EVID_RE.subn("", text)
        if n:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
            removed += n
    print(f"Stripped {removed} legacy evidence lines from {changed}/{len(files)} plant files.")


if __name__ == "__main__":
    main()
