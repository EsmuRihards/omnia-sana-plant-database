#!/usr/bin/env python3
"""
migrate_phase3_bibliography.py — architecture migration, Phase 3 (additive).

Makes the BibTeX structured fields complete and authoritative by backfilling the
`title` field for entries that currently carry their title ONLY inside the
free-text `annote` string (the inconsistency the builders work around with
title-from-annote heuristics).

SAFE BY DESIGN:
  * Additive only — inserts a `title = {...}` field; never edits or removes any
    existing field (annote is retained for now; its removal + build-time citation
    generation happens in Phase 6, after the generator is verified against it).
  * Surgical — leaves every other byte of each entry untouched (clean diff).
  * Idempotent — entries that already have a title are skipped.

Usage:  python ingest/migrate_phase3_bibliography.py [--apply]
        (without --apply it just reports; with --apply it writes the file)
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")

ENTRY_RE = re.compile(r"@\w+\s*\{\s*[^,\s]+\s*,.*?\n\}", re.S)
HAS_TITLE_RE = re.compile(r"(?mi)^\s*title\s*=")
ANNOTE_RE = re.compile(r"(?is)annote\s*=\s*\{")


def title_from_annote(annote):
    """First quoted segment of a Harvard annote string is the title."""
    norm = (annote.replace("‘", "'").replace("’", "'")
                  .replace("“", '"').replace("”", '"'))
    for pat in (r"'([^']{12,220})'", r'"([^"]{12,220})"'):
        m = re.search(pat, norm)
        if m:
            return m.group(1).strip().strip(".,")
    return ""


def brace_value(text, brace_open_idx):
    depth, i = 0, brace_open_idx
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[brace_open_idx + 1:i]
        i += 1
    return ""


def process_entry(entry, stats):
    stats["entries"] += 1
    if HAS_TITLE_RE.search(entry):
        stats["had_title"] += 1
        return entry
    ma = ANNOTE_RE.search(entry)
    if not ma:
        stats["no_title_no_annote"] += 1
        return entry
    open_idx = entry.index("{", ma.start())
    title = title_from_annote(brace_value(entry, open_idx))
    if not title:
        stats["unparseable"] += 1
        return entry
    nl = entry.index("\n")          # insert right after the "@type{key," line
    stats["backfilled"] += 1
    return entry[:nl] + "\n  title    = {%s}," % title + entry[nl:]


def main():
    apply = "--apply" in sys.argv
    raw = open(BIB, encoding="utf-8").read()
    stats = dict(entries=0, had_title=0, backfilled=0, no_title_no_annote=0, unparseable=0)
    new = ENTRY_RE.sub(lambda m: process_entry(m.group(0), stats), raw)

    print("BibTeX title backfill —", "APPLY" if apply else "DRY RUN")
    for k in ("entries", "had_title", "backfilled", "unparseable", "no_title_no_annote"):
        print(f"  {k:20s}: {stats[k]}")

    if apply:
        with open(BIB, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("  -> wrote", BIB)
    else:
        print("  (re-run with --apply to write)")


if __name__ == "__main__":
    main()
