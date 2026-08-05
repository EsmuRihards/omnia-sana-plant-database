#!/usr/bin/env python3
"""
scripts/audit_species.py — wrong-species citation audit (the #1 unmechanized failure).

`validate.py` proves a cited REF *resolves*; it never checks the reference is about the
right *species*. Wrong-species citations — a congener returned by a genus-level search —
are the most common failure mode in this database (invariant 2). This script moves that
check from a hope into a signal, WITHOUT wiring a noisy heuristic into the hard gate.

It is **precision-first and non-blocking**. For every claim-bearing citation on a plant,
it reads the reference's title+abstract and classifies the species evidence:

  * OK            — the plant's own binomial (full or abbreviated) is present.
  * OK (common)   — a common name of the plant is present (softer, still fine).
  * ⚑ CONGENER    — a DIFFERENT species of the SAME genus is named and the plant's own
                    species is NOT — the wrong-species smoking gun. This is the headline.
  * genus-only    — the genus is named but not the species and no congener — usually fine
                    (papers say "the genus" / "the plant"); reported only as a count.
  * no-mention    — no matching binomial or common name — often legitimate (a compound,
                    mechanism or methods paper). Reported as a count; --show-no-mention
                    lists them. NOT treated as wrong-species.
  * unassessable  — the reference has no abstract and no usable title.

Only CONGENER is surfaced as actionable by default. Everything else is a count you can
drill into. Exit 0 always, unless --strict (then a CONGENER flag exits 1, for CI).

Usage:
  python scripts/audit_species.py                 # summary + congener flags
  python scripts/audit_species.py --plant salvia-officinalis
  python scripts/audit_species.py --show-no-mention --show-genus-only
  python scripts/audit_species.py --strict        # nonzero exit if any congener flag
"""
import os, re, sys, glob, yaml

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS = os.path.join(ROOT, "plants")
BIB = os.path.join(ROOT, "bibliography.bibtex")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from build import parse_bibtex
except Exception as exc:                                    # pragma: no cover
    print("could not import parse_bibtex from build.py:", exc)
    sys.exit(2)

REF_RE = re.compile(r"REF-\d{4,}")
# Common English words that happen to look like a lowercase species epithet, so a bare
# "Genus <word>" match doesn't invent a congener out of ordinary prose.
STOP_EPITHETS = {
    "and", "the", "was", "were", "are", "for", "with", "from", "have", "has", "not",
    "also", "may", "can", "which", "that", "this", "these", "those", "used", "using",
    "such", "species", "extract", "extracts", "leaf", "leaves", "root", "roots", "plant",
    "plants", "oil", "flower", "flowers", "seed", "seeds", "linn", "family", "genus",
    "var", "subsp", "spp", "sp", "cv", "aqueous", "methanol", "ethanol", "vulgaris",
    "vegetables", "supplements", "products", "derivatives", "preparations", "containing",
    "related", "emodin", "aloin",  # compounds that begin with a genus-like token
}


def _lev(a, b):
    """Levenshtein distance, capped early — used only to treat spelling/OCR variants of an
    epithet (citriodora≈citrodora, paniculate≈paniculata) as the same species, not a congener."""
    if abs(len(a) - len(b)) > 2:
        return 3
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[-1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]

# Fields whose reference_ids are claim-bearing (species must match). Deliberately EXCLUDES
# `dangerous_lookalikes` — that field's sources are *about the other species* by design, so a
# congener mention there is correct, not an error. Also excludes plant-level `references[]`
# (identification/foraging overviews where a species mention isn't guaranteed).
CLAIM_KEYS = ("indications", "actions", "constituents", "contraindications",
              "drug_class_interactions", "preparations", "dosage",
              "botanical_description", "habitat", "harvesting", "traditional_uses")


def binomial_parts(name):
    """('Salvia officinalis') -> ('salvia', 'officinalis'); tolerant of extra author text."""
    toks = re.findall(r"[A-Za-z-]+", str(name or ""))
    if len(toks) < 2:
        return None
    return toks[0].lower(), toks[1].lower()


def collect_refs(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "internal_notes":
                continue
            collect_refs(v, out)
    elif isinstance(node, list):
        for v in node:
            collect_refs(v, out)
    elif isinstance(node, str):
        out.update(REF_RE.findall(node))


def claim_refs(plant):
    """The set of REF ids reachable from claim-bearing fields only."""
    out = set()
    for k in CLAIM_KEYS:
        if k in plant:
            collect_refs(plant[k], out)
    return out


def _norm(s):
    """Lowercase; collapse hyphens, dots and whitespace to single spaces. This unifies
    'agnus-castus' / 'agnus castus' and 'V. officinalis' / 'V officinalis' so the writer's
    orthography doesn't create phantom mismatches."""
    return re.sub(r"[.\-\s]+", " ", str(s or "").lower()).strip()

# English prose words wearing a Latin-epithet costume end in these; real epithets don't.
_ENGLISH_SUFFIX = re.compile(r"(ed|ing|ly|ion|ness|ment|ology|ical)$")


def classify(plant, text):
    """Return (verdict, detail)."""
    if not text.strip():
        return "unassessable", ""
    genus, sp = plant["_gsp"]
    gen = genus.lower()
    ep = _norm(sp)                                     # full epithet, may be multi-word
    ep_tokens = set(ep.split())
    ntext = _norm(text)
    # 1. own species present? normalized full binomial, abbreviated genus, or a synonym
    own = (gen + " " + ep) in ntext or (gen[0] + " " + ep) in ntext
    syn_hit = any((_norm(sg) + " " + _norm(se)) in ntext for (sg, se) in plant["_syn_binomials"])
    if own or syn_hit:
        return "ok", ""
    # 2. same-genus congeners: words following the FULL genus that aren't part of our own
    #    epithet, a synonym epithet, a stop-word, or obvious English prose. Detected on a
    #    hyphen-PRESERVING copy and requiring whitespace, so hyphenated compounds
    #    ("Aloe-emodin") and hyphenated epithets never masquerade as a congener.
    low = re.sub(r"\.", " ", text.lower())
    cong = set()
    for m in re.finditer(r"\b" + re.escape(gen) + r"\s+([a-z]{3,})", low):
        w = m.group(1)
        if (w in ep_tokens or w in plant["_syn_epithets"] or w in STOP_EPITHETS
                or _ENGLISH_SUFFIX.search(w)):
            continue
        # spelling / OCR variant of our own (or a synonym's) epithet -> same species, not a congener
        if any(_lev(w, e) <= 1 for e in ep_tokens | plant["_syn_epithets"]):
            continue
        cong.add(w)
    if len(cong) >= 3:
        return "genus_review", genus.capitalize() + " ×" + str(len(cong))  # a genus-wide survey
    if cong:
        return "congener", genus.capitalize() + " " + ", ".join(sorted(cong))
    # 3. genus named at all?
    if re.search(r"\b" + re.escape(gen) + r"\b", ntext):
        return "genus_only", ""
    # 4. a common name present?
    for cn in plant["_commons"]:
        if re.search(r"\b" + re.escape(_norm(cn)) + r"\b", ntext):
            return "ok_common", cn
    return "no_mention", ""


def main():
    args = sys.argv[1:]
    only = None
    if "--plant" in args:
        only = args[args.index("--plant") + 1]
    show_nomention = "--show-no-mention" in args
    show_genus = "--show-genus-only" in args
    strict = "--strict" in args

    bib = {e["ref_id"]: e["fields"] for e in parse_bibtex(open(BIB, encoding="utf-8").read()) if e["ref_id"]}

    counts = {"ok": 0, "ok_common": 0, "congener": 0, "genus_review": 0,
              "genus_only": 0, "no_mention": 0, "unassessable": 0}
    congener_flags, nomention_list, genus_list = [], [], []

    files = sorted(glob.glob(os.path.join(PLANTS, "*.yaml")))
    for path in files:
        p = yaml.safe_load(open(path, encoding="utf-8"))
        if not isinstance(p, dict):
            continue
        pid = p.get("id") or os.path.splitext(os.path.basename(path))[0]
        if only and pid != only:
            continue
        gsp = binomial_parts(p.get("scientific_name"))
        if not gsp:
            continue
        genus, sp = gsp
        syn_binos = [b for b in (binomial_parts(s) for s in p.get("synonyms", []) or []) if b]
        p["_gsp"] = gsp
        p["_syn_binomials"] = syn_binos
        p["_syn_epithets"] = {e for (_g, e) in syn_binos}
        p["_commons"] = [c.lower() for c in (p.get("common_names") or []) if len(c) >= 4]

        for rid in sorted(claim_refs(p)):
            f = bib.get(rid)
            if not f:
                continue  # validate.py owns "resolves or not"; skip here
            text = ((f.get("title") or "") + "  " + (f.get("abstract") or "")).lower()
            verdict, detail = classify(p, text)
            counts[verdict] += 1
            if verdict == "congener":
                congener_flags.append((pid, p.get("scientific_name"), rid, detail,
                                       (f.get("title") or "")[:90]))
            elif verdict == "no_mention":
                nomention_list.append((pid, rid, (f.get("title") or "")[:80]))
            elif verdict == "genus_only":
                genus_list.append((pid, rid, (f.get("title") or "")[:80]))

    total = sum(counts.values())
    print("=" * 70)
    print("SPECIES-DIFF CITATION AUDIT" + (f"  ({only})" if only else ""))
    print("=" * 70)
    print(f"Claim citations assessed: {total}")
    print(f"  ok (species named)   : {counts['ok']}")
    print(f"  ok (common name)     : {counts['ok_common']}")
    print(f"  genus-wide review    : {counts['genus_review']}  (surveys naming 3+ species; usually ok)")
    print(f"  genus-only (likely ok): {counts['genus_only']}")
    print(f"  no species mention   : {counts['no_mention']}  (often compound/mechanism papers)")
    print(f"  unassessable (no text): {counts['unassessable']}")
    print(f"  ⛑ CONGENER (wrong-species suspects): {counts['congener']}")

    if congener_flags:
        print("\n" + "-" * 70)
        print("⛑ CONGENER FLAGS — a same-genus congener is named and the record's own")
        print("   species is not. Open each and confirm the binomial (invariant 2).")
        print("-" * 70)
        for (pid, sci, rid, detail, title) in congener_flags:
            print(f"  {pid}  ({sci})")
            print(f"      {rid}  found: {detail}")
            print(f"      title: {title}")
    else:
        print("\nNo congener (wrong-species) suspects found in claim citations.")

    if show_genus and genus_list:
        print("\n" + "-" * 70 + "\ngenus-only citations (genus named, species not — usually fine):")
        for (pid, rid, title) in genus_list[:200]:
            print(f"  {pid}  {rid}  {title}")
    if show_nomention and nomention_list:
        print("\n" + "-" * 70 + "\nno-species-mention citations (review manually; many are legitimate):")
        for (pid, rid, title) in nomention_list[:400]:
            print(f"  {pid}  {rid}  {title}")

    print("\n" + "=" * 70)
    print("Heuristic, non-blocking: a flag is a prompt to check the source, not a verdict.")
    if strict and counts["congener"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
