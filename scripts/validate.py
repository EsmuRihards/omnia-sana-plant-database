#!/usr/bin/env python3
"""
scripts/validate.py — integrity checker for the Omnia Sana plant database.

Checks:
  1. Every REF-id cited anywhere in plants/*.yaml resolves to a BibTeX entry.
  2. Every action / condition / compound id used in a plant resolves to its
     controlled vocabulary (vocabularies/) or compound entity (compounds/).
  3. Required fields, id slug format, id uniqueness, status enum, evidence_override range.
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
NAMESDIR = os.path.join(ROOT, "names")
BIB = os.path.join(ROOT, "bibliography.bibtex")

REF_RE = re.compile(r"REF-\d{4,}")
SLUG = re.compile(r"^[a-z0-9-]+$")
STATUSES = {"verified", "draft", "needs-review"}
SAFETY_STATUSES = {"draft", "approved"}
SEVERITIES = {"avoid", "caution", "likely-safe", "insufficient"}
PAIR_TYPES = {"synergy", "neutral", "caution", "avoid"}
LOOKALIKE_SEVERITIES = {"fatal", "dangerous", "irritant", "caution"}
LOOKALIKE_OUTCOMES = {"none-known", "has-lookalikes"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


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
    D = vocab_ids(os.path.join(VOCAB, "drug_classes.yaml"))
    X = vocab_ids(os.path.join(VOCAB, "dangerous_plants.yaml"))
    LANGS = yaml.safe_load(open(os.path.join(VOCAB, "languages.yaml"), encoding="utf-8"))
    LANG_CODES = {x["code"] for x in LANGS}
    LANG_ENABLED = {x["code"] for x in LANGS if x.get("enabled")}

    cited, seen_ids, pair_refs = set(), {}, []
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
            ov = i.get("evidence_override")
            if ov is not None and not (isinstance(ov, int) and 1 <= ov <= 10):
                errors.append(f"{name}: indication '{i.get('condition')}' bad evidence_override {ov} (want int 1-10)")
        for c in d.get("constituents", []):
            for cm in c.get("compounds", []):
                if cm not in K:
                    errors.append(f"{name}: compound '{cm}' has no entity in compounds/")
        if "common_slug" in d and not SLUG.match(str(d.get("common_slug", ""))):
            errors.append(f"{name}: bad common_slug '{d.get('common_slug')}'")
        for it in d.get("drug_class_interactions", []):
            if it.get("drug_class") not in D:
                errors.append(f"{name}: drug_class '{it.get('drug_class')}' not in drug_classes vocab")
            if it.get("severity") not in SEVERITIES:
                errors.append(f"{name}: interaction severity '{it.get('severity')}' invalid (want {sorted(SEVERITIES)})")
            if it.get("status") not in SAFETY_STATUSES:
                errors.append(f"{name}: interaction status '{it.get('status')}' invalid (want draft|approved)")
        for pr in d.get("pairings", []):
            if pr.get("type") not in PAIR_TYPES:
                errors.append(f"{name}: pairing type '{pr.get('type')}' invalid (want {sorted(PAIR_TYPES)})")
            if pr.get("status") not in SAFETY_STATUSES:
                errors.append(f"{name}: pairing status '{pr.get('status')}' invalid (want draft|approved)")
            if pr.get("partner_id") == d.get("id"):
                errors.append(f"{name}: pairing partner_id points at itself")
            pair_refs.append((name, pr.get("partner_id")))
        for la in d.get("dangerous_lookalikes", []):
            if la.get("dangerous_plant") not in X:
                errors.append(f"{name}: dangerous_plant '{la.get('dangerous_plant')}' not in dangerous_plants vocab")
            if la.get("severity") not in LOOKALIKE_SEVERITIES:
                errors.append(f"{name}: lookalike severity '{la.get('severity')}' invalid (want {sorted(LOOKALIKE_SEVERITIES)})")
            if la.get("status") not in SAFETY_STATUSES:
                errors.append(f"{name}: lookalike status '{la.get('status')}' invalid (want draft|approved)")
            df = la.get("distinguishing_features")
            if not (isinstance(df, list) and df):
                errors.append(f"{name}: lookalike '{la.get('dangerous_plant')}' needs >=1 distinguishing_features")
            if la.get("status") == "approved":
                if not la.get("reviewed_by"):
                    errors.append(f"{name}: approved lookalike '{la.get('dangerous_plant')}' missing reviewed_by")
                if not DATE_RE.match(str(la.get("reviewed_date", ""))):
                    errors.append(f"{name}: approved lookalike '{la.get('dangerous_plant')}' bad reviewed_date '{la.get('reviewed_date')}'")
        lr = d.get("lookalikes_review")
        if lr is not None:
            if lr.get("outcome") not in LOOKALIKE_OUTCOMES:
                errors.append(f"{name}: lookalikes_review outcome '{lr.get('outcome')}' invalid (want {sorted(LOOKALIKE_OUTCOMES)})")
            if lr.get("outcome") == "has-lookalikes" and not d.get("dangerous_lookalikes"):
                errors.append(f"{name}: lookalikes_review outcome 'has-lookalikes' but no dangerous_lookalikes[]")
        cited.update(find_refs(d))

    for (nm, pid) in pair_refs:
        if pid not in seen_ids:
            errors.append(f"{nm}: pairing partner_id '{pid}' has no plant record")

    # ---- vernacular names (names/*.yaml) — the Multilingual Plant-Name Dictionary ----
    # Strict data-quality backstop: a published (verified) name must be attested by either
    # >=1 curated authority (EPPO / POWO / Catalogue of Life) OR >=2 independent sources.
    # No name may exist without >=1 source. This mirrors the pipeline's accept rule so a
    # hand edit or a pipeline regression can never ship an unverified translation.
    CURATED_PREFIXES = ("eppo:", "powo:", "col:")
    name_files = sorted(glob.glob(os.path.join(NAMESDIR, "*.yaml")))
    for path in name_files:
        nm = "names/" + os.path.basename(path)
        d = yaml.safe_load(open(path, encoding="utf-8"))
        if not isinstance(d, dict):
            errors.append(f"{nm}: not a mapping")
            continue
        for k in ("id", "scientific_name", "names"):
            if k not in d:
                errors.append(f"{nm}: missing required field '{k}'")
        nid = d.get("id")
        if nid and nid not in seen_ids:
            errors.append(f"{nm}: id '{nid}' has no plant record in plants/")
        names = d.get("names") or {}
        if not isinstance(names, dict):
            errors.append(f"{nm}: 'names' must be a mapping of lang -> list")
            names = {}
        for lang, arr in names.items():
            if lang not in LANG_CODES:
                errors.append(f"{nm}: language '{lang}' not in languages.yaml")
            elif lang not in LANG_ENABLED:
                warnings.append(f"{nm}: language '{lang}' present but not enabled")
            if not isinstance(arr, list) or not arr:
                errors.append(f"{nm}: language '{lang}' must be a non-empty list")
                continue
            pref = 0
            for e in arr:
                if not isinstance(e, dict) or not str(e.get("name", "")).strip():
                    errors.append(f"{nm}: {lang} has an entry with no name")
                    continue
                srcs = e.get("sources") or []
                if not isinstance(srcs, list) or not srcs:
                    errors.append(f"{nm}: {lang} '{e.get('name')}' has no sources")
                    srcs = []
                st = e.get("status", "verified")
                if st not in ("verified", "needs-review"):
                    errors.append(f"{nm}: {lang} '{e.get('name')}' bad status '{st}'")
                if e.get("preferred"):
                    pref += 1
                if st == "verified":
                    curated = any(str(s).startswith(CURATED_PREFIXES) for s in srcs)
                    if not curated and len(set(map(str, srcs))) < 2:
                        errors.append(f"{nm}: {lang} '{e.get('name')}' is verified but fails the "
                                      f"multi-source rule (need >=1 curated source or >=2 independent)")
            if pref > 1:
                errors.append(f"{nm}: {lang} has {pref} names flagged preferred (want <=1)")
        v = d.get("verification") or {}
        for lc in v.get("checked_languages", []):
            if lc not in LANG_CODES:
                warnings.append(f"{nm}: checked_languages has unknown code '{lc}'")

    missing = sorted(cited - declared)
    orphan = sorted(declared - cited)
    for r in missing:
        errors.append(f"cited REF not in bibliography: {r}")
    for r in orphan:
        warnings.append(f"orphan reference (never cited): {r}")

    print(f"Scanned {len(files)} plants | {len(name_files)} names files | "
          f"refs cited {len(cited)} / declared {len(declared)} | "
          f"actions {len(A)} conditions {len(C)} drug-classes {len(D)} dangerous-plants {len(X)} "
          f"compounds {len(K)} languages {len(LANG_ENABLED)}")
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
