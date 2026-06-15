#!/usr/bin/env python3
"""
migrate_followup_drop_annote.py — follow-up: normalize the bibliography.

Backfills structured volume/number/pages from the legacy `annote` Harvard string
(where missing), then DROPS the `annote` field entirely and re-serialises every
entry in a canonical field order. After this, scripts/build.py generates the
display citation from structured fields via harvard() — annote is no longer the
source of truth, removing the last denormalised/duplicated field.

Preserves: citation key, REF-id (note), all field values (raw, brace-balanced),
abstract. Entry count and REF ids are unchanged (verify with scripts/validate.py).

Usage:  python ingest/migrate_followup_drop_annote.py [--apply]
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")

FIELD_START_RE = re.compile(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*")
ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", re.S)
ORDER = ["author", "title", "booktitle", "journal", "year", "volume", "number",
         "pages", "publisher", "address", "edition", "doi", "url", "note", "abstract"]


def extract_fields(body):
    """field -> RAW value (inner braces preserved); ordered dict."""
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


def backfill_from_annote(f):
    """Fill volume/number/pages from the annote Harvard string if missing. Returns
    (n_backfilled)."""
    an = f.get("annote", "")
    if not an:
        return 0
    n = 0
    # volume(number) e.g. "79(1)" or "25(12)"
    if not f.get("volume"):
        m = re.search(r"(?<![\w.])(\d{1,4})\((\d{1,4}|[A-Za-z]{1,8})\)", an)
        if m:
            f["volume"] = m.group(1)
            if not f.get("number"):
                f["number"] = m.group(2)
            n += 1
    # pages e.g. "pp. 929-938" / "pp. e64-e74"
    if not f.get("pages"):
        m = re.search(r"pp?\.\s*([0-9A-Za-z]+(?:\s*[–—-]\s*[0-9A-Za-z]+)?)", an)
        if m:
            pg = re.sub(r"\s*[–—-]\s*", "--", m.group(1).strip())
            f["pages"] = pg
            n += 1
    return n


def serialize(etype, key, f):
    lines = ["@%s{%s," % (etype, key)]
    keys = [k for k in ORDER if k in f] + [k for k in f if k not in ORDER]
    for k in keys:
        if k == "annote":
            continue
        v = f[k]
        if v == "":
            continue
        lines.append("  %-8s = {%s}," % (k, v))
    # drop trailing comma on last field
    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return "\n".join(lines)


def main():
    apply = "--apply" in sys.argv
    raw = open(BIB, encoding="utf-8").read()
    header = raw[:raw.find("@")] if "@" in raw else ""
    entries = []
    stats = dict(entries=0, annote_dropped=0, backfilled=0, has_vol=0, has_pages=0)
    for m in ENTRY_RE.finditer(raw):
        etype, key, body = m.group(1).lower(), m.group(2).strip(), m.group(3)
        f = extract_fields(body)
        stats["entries"] += 1
        stats["backfilled"] += 1 if backfill_from_annote(f) else 0
        if "annote" in f:
            stats["annote_dropped"] += 1
        if f.get("volume"):
            stats["has_vol"] += 1
        if f.get("pages"):
            stats["has_pages"] += 1
        entries.append((key, serialize(etype, key, f)))

    entries.sort(key=lambda x: x[0].lower())
    out = header.rstrip() + "\n\n" + "\n\n".join(e[1] for e in entries) + "\n"

    print(("APPLY" if apply else "DRY RUN") + " — drop annote / normalize bibliography")
    for k, v in stats.items():
        print(f"  {k:16s}: {v}")
    if apply:
        open(BIB, "w", encoding="utf-8").write(out)
        print("  -> wrote", BIB)
    else:
        print("  (re-run with --apply to write)")


if __name__ == "__main__":
    main()
