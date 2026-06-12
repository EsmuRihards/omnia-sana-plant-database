#!/usr/bin/env python3
"""
validate_references.py — integrity checker for the Omnia Sana plant database.

Checks the link between plant YAML records and the BibTeX bibliography:

  1. Every REF-XXXX id used in any plants/*.yaml has a matching BibTeX entry
     (an entry whose `note` field contains that REF id).
  2. Reports orphaned references (BibTeX entries never cited by any plant).
  3. Reports malformed reference ids (not matching REF-#### with >=4 digits).

Usage:
    python validate_references.py            # validate
    python validate_references.py --quiet     # only print on problems

Exit code 0 = all good. Exit code 1 = missing references (a hard error).
Orphaned references are reported as warnings and do NOT fail the build.
"""

import os
import re
import sys
import glob

# Make stdout robust on consoles with a non-UTF-8 default codec (e.g. Windows
# cp1252) so printing a unicode citation key never crashes the validator.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML is required. Install with: pip install pyyaml\n")
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
PLANTS_DIR = os.path.join(HERE, "plants")
BIBLIO = os.path.join(HERE, "bibliography.bibtex")

REF_RE = re.compile(r"REF-\d{4,}")


def find_ref_ids(node):
    """Recursively yield every REF-XXXX string found anywhere in a YAML node."""
    if isinstance(node, dict):
        for v in node.values():
            yield from find_ref_ids(v)
    elif isinstance(node, list):
        for v in node:
            yield from find_ref_ids(v)
    elif isinstance(node, str):
        for m in REF_RE.findall(node):
            yield m


def load_yaml_refs():
    """Map each REF id -> set of plant files that use it. Also collect malformed ids."""
    used = {}            # ref_id -> set(files)
    malformed = {}       # bad_string -> set(files)
    files = sorted(glob.glob(os.path.join(PLANTS_DIR, "*.yaml")) +
                   glob.glob(os.path.join(PLANTS_DIR, "*.yml")))
    for path in files:
        name = os.path.basename(path)
        with open(path, "r", encoding="utf-8") as fh:
            try:
                data = yaml.safe_load(fh)
            except yaml.YAMLError as e:
                sys.stderr.write(f"  ! YAML parse error in {name}: {e}\n")
                continue
        if data is None:
            continue
        # Structured reference_ids fields (the canonical place ids live).
        for ref in find_ref_ids(data):
            used.setdefault(ref, set()).add(name)
        # Catch reference-looking ids that are malformed (e.g. REF-1, REF-12).
        raw = open(path, "r", encoding="utf-8").read()
        for m in re.findall(r"REF-\d+", raw):
            if not REF_RE.fullmatch(m):
                malformed.setdefault(m, set()).add(name)
    return used, malformed, files


def load_bibtex_refs():
    """Map each REF id declared in bibliography.bibtex -> citation key."""
    declared = {}        # ref_id -> citation_key
    if not os.path.exists(BIBLIO):
        return declared
    raw = open(BIBLIO, "r", encoding="utf-8").read()
    # Drop % comment lines (header/examples) so they are never parsed as entries.
    text = "\n".join(ln for ln in raw.splitlines() if not ln.lstrip().startswith("%"))
    # Split into entries on @type{key,
    entry_re = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", re.DOTALL)
    for m in entry_re.finditer(text):
        key = m.group(1).strip()
        body = m.group(2)
        for ref in REF_RE.findall(body):
            declared[ref] = key
    return declared


def main():
    quiet = "--quiet" in sys.argv

    used, malformed, files = load_yaml_refs()
    declared = load_bibtex_refs()

    used_ids = set(used)
    declared_ids = set(declared)

    missing = sorted(used_ids - declared_ids)      # cited but not in bibliography
    orphaned = sorted(declared_ids - used_ids)     # in bibliography but never cited

    if not quiet:
        print(f"Scanned {len(files)} plant file(s).")
        print(f"  reference ids used in YAML : {len(used_ids)}")
        print(f"  reference ids in BibTeX    : {len(declared_ids)}")
        print()

    ok = True

    if malformed:
        ok = False
        print("MALFORMED reference ids (must be REF-#### with >= 4 digits):")
        for bad, where in sorted(malformed.items()):
            print(f"  {bad}  in {', '.join(sorted(where))}")
        print()

    if missing:
        ok = False
        print("MISSING references (cited in YAML, absent from bibliography.bibtex):")
        for ref in missing:
            print(f"  {ref}  used in: {', '.join(sorted(used[ref]))}")
        print()

    if orphaned:
        print("WARNING — orphaned references (in bibliography.bibtex, never cited):")
        for ref in orphaned:
            print(f"  {ref}  -> {declared[ref]}")
        print()

    if ok and not missing and not malformed:
        if not quiet:
            print("OK — every cited reference resolves to a BibTeX entry.")
        # Orphans are warnings only; do not fail.
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
