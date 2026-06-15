#!/usr/bin/env python3
"""
scripts/validate.py — integrity checker for the Omnia Sana plant database.

Checks:
  1. Every REF-id cited anywhere in plants/*.yaml resolves to a BibTeX entry.
  2. Every action / condition / compound id used in a plant resolves to its
     controlled vocabulary (vocabularies/) or compound entity (compounds/).
  3. Required fields, id slug format, id uniqueness, status enum, evidence range.
  4. Orphan references (in bibliography, never cited) are reported as warnings.

Exit 0 = clean. Exit 1 = hard error (missing ref/vocab id, malformed record).
Supersedes the old validate_references.py. Run: python scripts/validate.py
"""
import os, re, sys, glob, yaml

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
COMPDIR = os.path.join(ROOT, "compounds")
BIB = os.path.join(ROOT, "bibliography.bibtex")

REF_RE = re.compile(r"REF-\d{4,}")
SLUG = re.compile(r"^[a-z0-9-]+$")
STATUSES = {"verified", "draft", "needs-review"}


def find_refs(node):
    if isinstance(node, dict):
        for v in node.values():
            yield from find_refs(v)
    elif isinstance(node, list):
        for v in node:
            yield from find_refs(v)
    elif isinstance(node, str):
        yield from REF_RE.findall(node)


def declared_refs():
    raw = open(BIB, encoding="utf-8").read()
    text = "\n".join(l for l in raw.splitlines() if not l.lstrip().startswith("%"))
    out = set()
    for m in re.finditer(r"@\w+\s*\{\s*[^,\s]+\s*,(.*?)(?=\n@|\Z)", text, re.S):
        out.update(REF_RE.findall(m.group(1)))
    return out


def vocab_ids(path):
    return {x["id"] for x in yaml.safe_load(open(path, encoding="utf-8"))}


def main():
    errors, warnings = [], []
    declared = declared_refs()
    A = vocab_ids(os.path.join(VOCAB, "actions.yaml"))
    C = vocab_ids(os.path.join(VOCAB, "conditions.yaml"))
    K = {yaml.safe_load(open(f, encoding="utf-8"))["id"] for f in glob.glob(os.path.join(COMPDIR, "*.yaml"))}

    cited, seen_ids = set(), {}
    files = sorted(glob.glob(os.path.join(PLANTS, "*.yaml")))
    for path in files:
        name = os.path.basename(path)
        d = yaml.safe_load(open(path, encoding="utf-8"))
        for k in ("id", "scientific_name", "common_names", "family", "status", "last_updated"):
            if k not in d:
                errors.append(f"{name}: missing required field '{k}'")
        if d.get("status") not in STATUSES:
            errors.append(f"{name}: bad status '{d.get('status')}'")
        if "id" in d:
            if not SLUG.match(d["id"]):
                errors.append(f"{name}: bad id slug '{d['id']}'")
            if d["id"] in seen_ids:
                errors.append(f"{name}: duplicate id '{d['id']}' (also {seen_ids[d['id']]})")
            seen_ids[d["id"]] = name
        if "Unknown" in str(d.get("family", "")):
            warnings.append(f"{name}: family is '{d.get('family')}'")
        for a in d.get("actions", []):
            if a.get("action") not in A:
                errors.append(f"{name}: action '{a.get('action')}' not in actions vocab")
        for i in d.get("indications", []):
            if i.get("condition") not in C:
                errors.append(f"{name}: condition '{i.get('condition')}' not in conditions vocab")
            if not (isinstance(i.get("evidence"), int) and 1 <= i["evidence"] <= 5):
                errors.append(f"{name}: indication '{i.get('condition')}' bad evidence {i.get('evidence')}")
        for c in d.get("constituents", []):
            for cm in c.get("compounds", []):
                if cm not in K:
                    errors.append(f"{name}: compound '{cm}' has no entity in compounds/")
        cited.update(find_refs(d))

    missing = sorted(cited - declared)
    orphan = sorted(declared - cited)
    for r in missing:
        errors.append(f"cited REF not in bibliography: {r}")
    for r in orphan:
        warnings.append(f"orphan reference (never cited): {r}")

    print(f"Scanned {len(files)} plants | refs cited {len(cited)} / declared {len(declared)} | "
          f"actions {len(A)} conditions {len(C)} compounds {len(K)}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings[:40]:
            print("  -", w)
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors[:60]:
            print("  -", e)
        sys.exit(1)
    print("\nOK — all references and vocab ids resolve; records well-formed.")


if __name__ == "__main__":
    main()
