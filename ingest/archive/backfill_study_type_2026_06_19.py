#!/usr/bin/env python3
"""
ingest/archive/backfill_study_type_2026_06_19.py — one-shot hardening migration.

Adds an explicit `study_type = {...}` field to every entry in bibliography.bibtex
so the build's tier classification (scripts/build.py: classify_tier) stops
depending on title/abstract KEYWORDS. After this runs, study_type is the single,
deterministic signal; the keyword heuristic survives only as a fallback for any
future un-annotated entry.

The initial values are SEEDED by running the legacy keyword heuristic once
(build.classify_tier, which falls back to keywords when no study_type is present).
They are a starting point — an editor can correct any entry by hand afterwards and
the build will honour the explicit value verbatim.

Canonical study_type vocabulary (strongest -> weakest):
  systematic-review | rct | clinical | preclinical | traditional

Idempotent: aborts if any study_type already exists. Minimal diff: inserts one
line directly after each entry's `note = {REF-XXXX}` line, touching nothing else.
Run:  python ingest/archive/backfill_study_type_2026_06_19.py
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BIB = os.path.join(ROOT, "bibliography.bibtex")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import build  # noqa: E402  (parse_bibtex + classify_tier)

# tier (from classify_tier) -> canonical study_type written to bibtex.
TIER_STUDY_TYPE = {
    "review": "systematic-review",
    "rct": "rct",
    "clinical": "clinical",
    "preclinical": "preclinical",
    "traditional": "traditional",
}

NOTE_RE = re.compile(r"^(\s*note\s*=\s*\{(REF-\d+)\})(,?)[ \t]*$", re.M)


def main():
    raw = open(BIB, encoding="utf-8").read()
    if "study_type" in raw:
        print("study_type already present — nothing to do (idempotent).")
        return

    entries = build.parse_bibtex(raw)
    st_for = {}
    for e in entries:
        if not e["ref_id"]:
            continue
        tier = build.classify_tier(e["fields"], e["type"])  # keyword fallback (no study_type yet)
        st_for[e["ref_id"]] = TIER_STUDY_TYPE[tier]

    def repl(m):
        st = st_for.get(m.group(2))
        if not st:
            return m.group(0)
        # note line keeps a trailing comma; study_type inherits the original
        # terminator (comma if a field followed note, empty if note was last).
        return m.group(1) + "," + "\n  study_type = {" + st + "}" + m.group(3)

    new, n = NOTE_RE.subn(repl, raw)
    if n == 0:
        print("ERROR: no note lines matched — aborting.")
        sys.exit(1)
    open(BIB, "w", encoding="utf-8").write(new)

    dist = {}
    for v in st_for.values():
        dist[v] = dist.get(v, 0) + 1
    print(f"Annotated {n} entries with study_type.")
    for k in ("systematic-review", "rct", "clinical", "preclinical", "traditional"):
        print(f"  {k:18} {dist.get(k, 0)}")


if __name__ == "__main__":
    main()
