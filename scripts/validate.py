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
PRACTICEDIR = os.path.join(ROOT, "practice")

# REF_RE above is UNANCHORED and is used with .findall() on prose. Do not reuse it
# with .match() — "REF-0481-typo" would pass. This is the anchored twin.
REF_EXACT_RE = re.compile(r"^REF-\d{4,}$")

# ---- practice corpus (practice/**/*.yaml) -----------------------------------
# The record-shape enums. The SOLVENT and METHOD vocabularies are NOT here: they
# are loaded from vocabularies/solvents.yaml and vocabularies/extraction_methods.yaml
# so that consumer_safe / consumer_reproducible travel with the id. A second
# hardcoded copy is how the safety flags get silently lost.
PRACTICE_RECORD_TYPES = {"extraction", "stability", "dose-form-conversion", "harvest-timing",
                         "identification", "cultivation", "post-harvest"}
PRACTICE_TYPES_LIVE = {"extraction", "stability", "dose-form-conversion"}
PARAMETER_KINDS = {"empirical", "normative"}
SPECIES_SCOPES = {"class-general", "species-specific"}
GENERALISATION_BASES = {"physicochemical", "matrix-analogous"}
LOCATOR_SECTIONS = {"methods", "results", "table", "figure", "supplementary", "monograph"}
MATERIAL_STATES = {"fresh", "dried", "freeze-dried", "frozen", "unspecified"}
VARIED_FACTORS = {"solvent_pct", "temperature_c", "time_min", "solid_liquid_ratio",
                  "ph", "particle_size_mm", "cycles", "method", "none"}
DOE_DESIGNS = {"rsm-ccd", "rsm-bbd", "factorial", "taguchi", "mixture", "multi-level-sweep"}
QUANTIFICATION = {"hplc-dad", "hplc-uv", "hplc-ms", "uplc-ms", "gc-ms", "gc-fid", "lc-nmr",
                  "uv-vis", "gravimetric", "titrimetric", "folin-ciocalteu",
                  "aluminium-chloride", "vanillin-hcl", "dpph", "frap",
                  "volumetric-distillation"}
UNIT_BASES = {"dry-weight", "fresh-weight", "extract", "volume", "unspecified"}
FULLTEXT_SOURCES = {"doi-pdf", "pmc", "publisher-html", "institutional", "author-copy",
                    "print", "pharmacopoeia-subscription"}
AUTHORITIES = {"ph-eur", "usp-nf", "bhp", "ahp", "bp", "who-monographs", "escop"}
TOXICITY_FLAGS = {"none", "dose-limited", "topical-only", "avoid-internal"}
ROUTES = {"internal", "topical"}
EQUIV_UNIT_RE = re.compile(r"\b(RE|GE|QE|GAE|equivalents?)\b")
# 'N:M' as the paper prints it, the literal 'unspecified' (which CAPS the finding),
# or 'n-a' where requires_menstruum is false. A '1:N'-only rule rejects every 20:1
# concentrate and every paper that omits the ratio — and rejecting the paper is
# exactly what makes a tired editor invent 1:10.
RATIO_RE = re.compile(r"^(\d+(\.\d+)?:\d+(\.\d+)?|unspecified|n-a)$")
BINOMIAL_RE = re.compile(r"^[A-Z][a-z]+ [a-z][a-z-]+$")
# NO OUTCOME_UNITS / UNIT_RANGE. outcome.unit is OPEN TEXT (R1-9): a closed slug
# set rejects 'mg RE/g', 'mL/100 g' and '% v/w', the units papers actually print,
# and a closed enum is what destroyed reference_standard the first time.
# NO NO_MENSTRUUM_METHODS either. requires_menstruum travels with the id in
# extraction_methods.yaml, where SEVEN ids declare it false (expression,
# crush-and-rest, steam-distillation, hydrodistillation, spray-drying, sfe, none).
# A second hardcoded copy naming four is how the flags drift — and it makes
# dose-form-conversion, one of the three LIVE record types, unauthorable.


# Keys whose free text is editorial prose, not citation data. They routinely
# discuss REF-ids that are deliberately no longer cited — e.g. the notes
# recording why a phantom reference was removed — so scanning them would
# resurrect those ids as "cited" and break the missing/orphan accounting.
PROSE_KEYS = {"internal_notes"}


def find_refs(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in PROSE_KEYS:
                continue
            yield from find_refs(v)
    elif isinstance(node, list):
        for v in node:
            yield from find_refs(v)
    elif isinstance(node, str):
        yield from REF_RE.findall(node)


def declared_refs():
    """REF-ids declared by the bibliography.

    Only the canonical `note = {REF-XXXX}` field counts. Scanning whole entry
    bodies would also pick up REF-ids mentioned inside `summary`/`abstract`/
    `integrity_note` prose (e.g. a note explaining that some other entry was a
    phantom), which would silently mask a genuine missing-reference error.
    """
    raw = open(BIB, encoding="utf-8").read()
    text = "\n".join(l for l in raw.splitlines() if not l.lstrip().startswith("%"))
    out = set()
    for m in re.finditer(r"@\w+\s*\{\s*[^,\s]+\s*,(.*?)(?=\n@|\Z)", text, re.S):
        for note in re.finditer(r"note\s*=\s*\{\s*(REF-\d{4,})\s*\}", m.group(1)):
            out.add(note.group(1))
    return out


def vocab_ids(path):
    return {x["id"] for x in yaml.safe_load(open(path, encoding="utf-8"))}


def vocab_map(path):
    """id -> whole record. vocab_ids() discards every field but the id, which is
    fine for actions/conditions but not for solvents and methods, where the
    consumer_safe / consumer_reproducible flags ARE the gate."""
    return {x["id"]: x for x in yaml.safe_load(open(path, encoding="utf-8"))}


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _s(v):
    """Text of a possibly-null field. EVERY text gate in this file goes through this.

    `str(None)` is the four-character string 'None', which is truthy and survives
    .strip() — so wrapping a bare .get() in str() and stripping it accepts an
    explicit YAML `null` as if it were content. (That idiom is deliberately not
    written out here: pre-flight step 1 greps the code blocks for it, and a
    docstring quoting it would match its own check.) It silently defeats the
    copyright gate, the equivalence-unit gate, verified_by, jurisdiction and
    discordance_note, and the spec TELLS authors to write nulls. yaml.safe_load
    returns None for `key:` with no value, so this is the common case, not an edge
    one. Note `.get(k, "")` does not help: the default only applies when the key is
    ABSENT, never when it is present and null."""
    return "" if v is None else str(v).strip()


def check_practice_record(nm, rec, plant_ids, K, COMPRECS, SOLV, METH, XCLS,
                          bib_fields, plant_refs, errors, warnings):
    """Every rule the JSON Schema *documents* but cannot enforce.

    schema/*.json is loaded by NOTHING — there is no `import jsonschema` anywhere
    in scripts/. Every "required", "minItems", "false" and "const" in
    practice.schema.json is inert documentation. This function is the enforcement.
    """
    for k in ("id", "record_type", "parameter_kind", "species_scope", "key",
              "status", "last_updated"):
        if k not in rec:
            errors.append(f"{nm}: missing required field '{k}'")
    rt = rec.get("record_type")
    if rt not in PRACTICE_RECORD_TYPES:
        errors.append(f"{nm}: record_type '{rt}' invalid (want {sorted(PRACTICE_RECORD_TYPES)})")
    elif rt not in PRACTICE_TYPES_LIVE:
        errors.append(f"{nm}: record_type '{rt}' is RESERVED — no record may be authored "
                      f"under it until its schema branch and rules exist")
    kind = rec.get("parameter_kind")
    if kind not in PARAMETER_KINDS:
        errors.append(f"{nm}: parameter_kind '{kind}' invalid (want {sorted(PARAMETER_KINDS)})")
    if not DATE_RE.match(str(rec.get("last_updated", ""))):
        errors.append(f"{nm}: bad last_updated '{rec.get('last_updated')}'")
    if rec.get("status") not in SAFETY_STATUSES:
        errors.append(f"{nm}: status '{rec.get('status')}' invalid (want draft|approved)")

    key = rec.get("key")
    if rt == "extraction":
        if not isinstance(key, dict):
            errors.append(f"{nm}: extraction record needs a key{{}} block")
            key = {}
        xc = key.get("extraction_class")
        if xc is not None and xc not in XCLS:
            errors.append(f"{nm}: key.extraction_class '{xc}' not in "
                          f"vocabularies/extraction_classes.yaml (null is valid — it is an "
                          f"OPTIONAL disambiguator, used only where one compound id spans "
                          f"classes with opposite optima)")
        if key.get("part") is not None:
            errors.append(f"{nm}: key.part is FROZEN to null in v1 (got {key.get('part')!r}). "
                          f"plants[].parts_used is 58 dirty free-text strings and constituents[] "
                          f"carries no part attribution, so the part axis cannot be joined from "
                          f"plant data. Unfreezing it is gated on the parts cleanup (D7).")
        cid = key.get("compound_id")
        if not cid:
            errors.append(f"{nm}: key.compound_id is required — it IS the join key")
        elif cid not in K:
            errors.append(f"{nm}: key.compound_id '{cid}' has no entity in compounds/ — "
                          f"a record that cannot join is a record no calculator will read")
        if key.get("solvent") not in SOLV:
            errors.append(f"{nm}: key.solvent '{key.get('solvent')}' not in vocabularies/solvents.yaml")
        if key.get("method") not in METH:
            errors.append(f"{nm}: key.method '{key.get('method')}' not in vocabularies/extraction_methods.yaml")

    findings = rec.get("findings")
    if findings is None:
        findings = []
    if not isinstance(findings, list):
        errors.append(f"{nm}: findings must be a list")
        findings = []
    for i, fi in enumerate(findings):
        if isinstance(fi, dict):
            _check_finding(nm, fi, i, SOLV, METH, errors, warnings)
        else:
            errors.append(f"{nm}: findings[{i}] is not a mapping")
    for ov in (rec.get("species_overrides") or []):
        if isinstance(ov, dict):
            plant_refs.append((nm, ov.get("plant_id")))

    _check_recommendation(nm, rec, findings, SOLV, METH, errors, warnings)
    _check_scope(nm, rec, findings, plant_ids, errors, warnings)
    _check_copyright(nm, rec, errors)
    _check_toxicity(nm, rec, COMPRECS, errors)
    if rec.get("status") == "approved":
        _check_approval(nm, rec, findings, errors)


def _check_finding(nm, fi, i, SOLV, METH, errors, warnings):
    tag = f"{nm}: findings[{i}] ({fi.get('ref_id', 'no-ref')})"
    if not REF_EXACT_RE.match(str(fi.get("ref_id", ""))):
        errors.append(f"{tag}: bad or missing ref_id")
    if fi.get("fulltext_source") not in FULLTEXT_SOURCES:
        errors.append(f"{tag}: fulltext_source '{fi.get('fulltext_source')}' invalid (want "
                      f"{sorted(FULLTEXT_SOURCES)}). There is no value meaning 'abstract only' "
                      f"— an abstract cannot produce a finding.")
    mt = (fi.get("method_type") or "").strip().lower()
    if mt not in PRACTICE_METHOD_TYPES:
        errors.append(f"{tag}: method_type '{mt}' invalid (want {sorted(PRACTICE_METHOD_TYPES)}). "
                      f"It lives on the FINDING, not on the bibtex entry: the same paper is "
                      f"'optimisation' for the solvent axis and 'characterisation' for temperature.")
        return
    tier = PRACTICE_METHOD_TYPES[mt]
    if tier not in PRACTICE_FINDING_TIERS:
        errors.append(f"{tag}: tier '{tier}' may not carry a finding — a review or textbook "
                      f"reports no single (solvent, temperature, time, ratio, yield) tuple. "
                      f"Move it to context_reference_ids[].")
        return

    loc = fi.get("locator") or {}
    if loc.get("section") not in LOCATOR_SECTIONS:
        errors.append(f"{tag}: locator.section '{loc.get('section')}' invalid")
    if tier == "pharmacopoeial":
        for k in ("monograph", "edition"):
            if not _s(loc.get(k)):
                errors.append(f"{tag}: pharmacopoeial finding needs locator.{k} "
                              f"(cite the coordinates; NEVER reproduce the text)")
        if fi.get("authority") not in AUTHORITIES:
            errors.append(f"{tag}: pharmacopoeial finding needs authority (want {sorted(AUTHORITIES)})")
    else:
        if not (_s(loc.get("table")) or _s(loc.get("figure"))):
            errors.append(f"{tag}: needs locator.table or locator.figure — an abstract has no "
                          f"tables, so this is the field a second reader can check in 30 seconds")
        if loc.get("section") not in ("results", "table", "figure", "supplementary"):
            errors.append(f"{tag}: a measured value must be located in results/table/figure/supplementary")
        if not isinstance(loc.get("page"), int):
            warnings.append(f"{tag}: no locator.page — makes audit slower")

    mat = fi.get("material") or {}
    sp = _s(mat.get("species"))
    if not BINOMIAL_RE.match(sp):
        errors.append(f"{tag}: material.species '{sp}' is not 'Genus species' — record the "
                      f"binomial the paper actually printed, not the one you wanted")
    if not _s(mat.get("part")):
        errors.append(f"{tag}: material.part is required — free text exactly as the paper "
                      f"reports it ('aerial parts', 'root bark'). NOT a controlled id: the "
                      f"part vocabulary is frozen in v1 and no parts.yaml exists.")
    if mat.get("state") not in MATERIAL_STATES:
        errors.append(f"{tag}: material.state '{mat.get('state')}' invalid")
    if tier == "pharmacopoeial":
        return                                     # a norm has no experimental conditions

    co = fi.get("conditions") or {}
    meth = co.get("method")
    if meth not in METH:
        errors.append(f"{tag}: conditions.method '{meth}' not in vocabularies/extraction_methods.yaml")
    solv = co.get("solvent")
    # Derived from the vocabulary, never hardcoded. An unknown method already
    # errored above; treat it as menstruum-requiring so the strict path still runs.
    needs_menstruum = METH.get(meth, {}).get("requires_menstruum", True) is not False
    # Membership is checked ALWAYS: solvents.yaml carries `none` precisely so that
    # expression and the distillations have a valid id to record.
    if solv not in SOLV:
        errors.append(f"{tag}: conditions.solvent '{solv}' not in vocabularies/solvents.yaml "
                      f"(use 'none' for methods with requires_menstruum false)")
    else:
        takes = SOLV[solv].get("takes_concentration") is True
        pct = co.get("solvent_pct")
        if takes and not _num(pct):
            errors.append(f"{tag}: solvent '{solv}' has takes_concentration: true and requires "
                          f"a numeric conditions.solvent_pct — the number the paper printed "
                          f"(63), never a band")
        if not takes and pct is not None:
            errors.append(f"{tag}: solvent '{solv}' has takes_concentration: false; "
                          f"conditions.solvent_pct must be null (got {pct!r})")
        if _num(pct) and not (0 <= pct <= 100):
            errors.append(f"{tag}: solvent_pct {pct} out of range 0-100")
    required_conds = ("temperature_c", "time_min", "solid_liquid_ratio") if needs_menstruum \
                     else ("temperature_c", "time_min")
    for k in required_conds:
        v = co.get(k, "__absent__")
        if v == "__absent__":
            errors.append(f"{tag}: conditions.{k} is required (use null and accept the grade cap "
                          f"if the paper genuinely omits it) — silent absence is the signature "
                          f"of an abstract-only read")
        elif v is None or (isinstance(v, str) and v.strip().lower() == "unspecified"):
            warnings.append(f"{tag}: conditions.{k} is null — this finding cannot be the sole "
                            f"support for an approved recommendation")
    t, tm = co.get("temperature_c"), co.get("time_min")
    if _num(t) and not (-80 <= t <= 250):
        errors.append(f"{tag}: temperature_c {t} out of range -80..250")
    if _num(tm) and not (0.5 <= tm <= 20160):
        errors.append(f"{tag}: time_min {tm} out of range 0.5-20160")
    slr = co.get("solid_liquid_ratio")
    if slr is not None and needs_menstruum:
        if not RATIO_RE.match(str(slr)):
            # THE QUOTING TRAP. PyYAML applies the YAML 1.1 sexagesimal rule, so an
            # unquoted `1:10` loads as the integer 70 (1*60+10) and `1:20` as 80.
            # Only ratios whose second term is <=59 are affected — `1:100` stays a
            # string — so it fails inconsistently and the naive error message ("'70'
            # must be 'N:M'") points nowhere near the cause. Name the cause instead.
            if isinstance(slr, int) and not isinstance(slr, bool):
                errors.append(f"{tag}: solid_liquid_ratio loaded as the integer {slr} — you wrote "
                              f"it unquoted and YAML read 'N:M' as minutes:seconds "
                              f"({slr // 60}:{slr % 60:02d} -> {slr}). Quote it: '1:{slr % 60}'. "
                              f"ALWAYS quote ratios.")
            else:
                errors.append(f"{tag}: solid_liquid_ratio '{slr}' must be 'N:M' (g:mL), or the literal 'unspecified', or 'n-a'")
        elif ":" in str(slr):
            a, b = (float(x) for x in str(slr).split(":"))
            n = (b / a) if a else 0
            if not (2 <= n <= 200):
                errors.append(f"{tag}: solid:liquid 1:{n:g} outside the plausible 1:2-1:200 band")
        else:
            warnings.append(f"{tag}: solid_liquid_ratio '{slr}' — condition-incomplete; this "
                            f"finding cannot be the sole support for an approved recommendation")
    ph = co.get("ph")
    if ph is not None and not (_num(ph) and 0 <= ph <= 14):
        errors.append(f"{tag}: conditions.ph {ph} out of range 0-14")

    out = fi.get("outcome") or {}
    if len(_s(out.get("analyte"))) < 3:
        errors.append(f"{tag}: outcome.analyte is required — 'significantly higher' is an "
                      f"abstract; a named analyte is a Results table")
    q = out.get("quantification")
    if q not in QUANTIFICATION:
        errors.append(f"{tag}: outcome.quantification '{q}' invalid")
    v, u = out.get("value"), str(out.get("unit") or "").strip()
    if not (_num(v) and v > 0):
        errors.append(f"{tag}: outcome.value must be a positive number (got {v!r})")
    if not u:
        errors.append(f"{tag}: outcome.unit is required — open text, exactly as printed "
                      f"('mg/g', 'mL/100 g', '% v/w', 'mg RE/g')")
    if out.get("unit_basis") not in UNIT_BASES:
        errors.append(f"{tag}: outcome.unit_basis '{out.get('unit_basis')}' invalid (want "
                      f"{sorted(UNIT_BASES)}) — a mg/g with no dry/fresh basis is not a number")
    if EQUIV_UNIT_RE.search(u) and not _s(out.get("reference_standard")):
        errors.append(f"{tag}: unit '{u}' is an equivalence unit and requires "
                      f"reference_standard (rutin, gallic acid, quercetin)")

    vf = fi.get("varied_factor")
    if vf not in VARIED_FACTORS:
        errors.append(f"{tag}: varied_factor '{vf}' invalid")
    # TWO views of the level set, and the distinction is load-bearing.
    # `all_levels` counts what the paper tested — a categorical sweep is a real sweep.
    # `levels` is the numeric subset, used ONLY for arithmetic (membership, envelope).
    # Filtering to numerics BEFORE counting made `varied_factor: method` unauthorable at
    # every tier: its levels are words ('maceration', 'uae', 'soxhlet'), so the count was
    # always 0 and comparative-bench hard-errored, while downgrading to characterisation
    # tripped 'cannot report an optimum'. A method-comparison paper is the ONLY evidence
    # there is for recommendation.method, which is a required field.
    all_levels = [x for x in (out.get("comparator_levels") or [])
                  if _num(x) or _s(x)]
    levels = [x for x in all_levels if _num(x)]
    need = 3 if tier == "optimisation" else 2 if tier == "comparative-bench" else 0
    if tier == "optimisation" and fi.get("design") not in DOE_DESIGNS:
        errors.append(f"{tag}: method_type 'optimisation' requires design in {sorted(DOE_DESIGNS)}")
    opt = out.get("optimum_level")
    if need:
        if vf == "none":
            errors.append(f"{tag}: tier '{tier}' asserts a factor was varied but varied_factor is 'none'")
        if len(all_levels) < need:
            errors.append(f"{tag}: tier '{tier}' requires >={need} comparator_levels (the FULL set "
                          f"the Methods say was tested); got {len(all_levels)}")
        if opt is None and not _s(out.get("optimum_value")):
            errors.append(f"{tag}: a comparative finding must record which level won")
        if _num(opt) and levels and opt not in levels:
            errors.append(f"{tag}: optimum_level {opt} is not a member of comparator_levels "
                          f"{levels} — that is what a guessed level set looks like")
        # Same membership rule for a categorical winner: naming a winner that was never
        # among the tested levels is the same defect whether it is a number or a word.
        ov = _s(out.get("optimum_value"))
        if ov and not _num(opt):
            cats = [_s(x) for x in all_levels if not _num(x)]
            if cats and ov.casefold() not in {c.casefold() for c in cats}:
                errors.append(f"{tag}: optimum_value '{ov}' is not a member of comparator_levels "
                              f"{cats} — that is what a guessed level set looks like")
        if _num(opt) and vf in ("solvent_pct", "temperature_c", "time_min", "ph"):
            here = co.get(vf)
            if _num(here) and here != opt:
                errors.append(f"{tag}: varied_factor '{vf}' optimum is {opt} but conditions "
                              f"record {here} — best condition and run condition disagree")
    elif tier == "characterisation" and (opt is not None or out.get("optimum_value")):
        errors.append(f"{tag}: a single-condition characterisation cannot report an optimum")


def _check_recommendation(nm, rec, findings, SOLV, METH, errors, warnings):
    """Two things the drafts left out and that are the difference between
    'use 60-70% ethanol' and 'use 80% methanol'.

    1. recommendation.solvent is REQUIRED and gated on consumer_safe. A bare band
       {parameter: solvent_pct, range: [60,75]} derived entirely from methanol
       sweeps renders in an ethanol calculator as 'use 60-75% ethanol'.
    2. The swept envelope is partitioned BY SOLVENT and BY PARAMETER. Pooling all
       comparator_levels lets a temperature sweep of 40-80 C legitimise a solvent
       band of 60-75%, which defeats the one check advertised as stopping
       extrapolation.
    """
    r = rec.get("recommendation")
    if not isinstance(r, dict) or not r:
        # An avoid-only record is legitimate and deliberately cheap: the cost of a
        # wrong precaution is a suboptimal extract; the cost of a wrong instruction
        # is somebody drinking it for two years.
        if not (rec.get("avoid") or []):
            errors.append(f"{nm}: needs a recommendation{{}} or a non-empty avoid[] — "
                          f"a record that asserts neither says nothing")
        return
    param = r.get("parameter")
    if not param:
        errors.append(f"{nm}: recommendation.parameter is required")

    if r.get("route") not in ROUTES:
        errors.append(f"{nm}: recommendation.route '{r.get('route')}' invalid — required, "
                      f"want internal|topical. A band with no route renders in the tincture "
                      f"calculator as something to drink.")
    if len(_s(r.get("statement"))) < 20:
        errors.append(f"{nm}: recommendation.statement is required — the sentence a reader "
                      f"actually sees, not just the numbers behind it")
    handles = [str(fi.get("id", "")) for fi in findings if isinstance(fi, dict)]
    for h in handles:
        if not re.match(r"^F\d+$", h):
            errors.append(f"{nm}: findings[] entry has bad or missing id '{h}' (want F1, F2, …) "
                          f"— derived_from[] points at these handles")
    dupes = sorted({h for h in handles if h and handles.count(h) > 1})
    if dupes:
        errors.append(f"{nm}: duplicate findings[].id handles {dupes}")
    df = r.get("derived_from") or []
    if not df:
        errors.append(f"{nm}: recommendation.derived_from must name the finding ids the band "
                      f"came from")
    for src in df:
        if src not in handles:
            errors.append(f"{nm}: recommendation.derived_from '{src}' resolves to no finding")
    for i, av in enumerate(rec.get("avoid") or []):
        for src in ((av or {}).get("derived_from") or []):
            if src not in handles:
                errors.append(f"{nm}: avoid[{i}].derived_from '{src}' resolves to no finding")

    if rec.get("record_type") == "extraction":
        rs, rm = r.get("solvent"), r.get("method")
        if rs not in SOLV:
            errors.append(f"{nm}: recommendation.solvent '{rs}' missing or not in "
                          f"vocabularies/solvents.yaml — a band with no named solvent is "
                          f"rendered by the calculator as an ETHANOL band whatever was tested")
        elif SOLV[rs].get("consumer_safe") is not True:
            errors.append(f"{nm}: recommendation.solvent '{rs}' is consumer_safe: false. "
                          f"Findings may cite methanol/acetone/scCO2 freely; a recommendation "
                          f"may not. A bench optimum is a fact about chemistry, not something "
                          f"a person should put in a jar.")
        if rm not in METH:
            errors.append(f"{nm}: recommendation.method '{rm}' missing or not in "
                          f"vocabularies/extraction_methods.yaml")
        elif METH[rm].get("consumer_reproducible") is not True:
            errors.append(f"{nm}: recommendation.method '{rm}' is consumer_reproducible: false "
                          f"— telling a reader 20 min of 40 kHz sonication is optimal is true "
                          f"and useless")

    rng = r.get("range")
    if rng is None and r.get("value") is None:
        errors.append(f"{nm}: recommendation needs range[lo,hi] or a categorical value")
        return
    if rng is None:
        return
    # SHAPE FIRST, then arithmetic. range: ['a','b'] or [60] must be one error line,
    # not a TypeError/ValueError that kills the gate for the whole repo.
    if not (isinstance(rng, list) and len(rng) == 2 and all(_num(x) for x in rng)):
        errors.append(f"{nm}: recommendation.range must be [lo, hi], two numbers (got {rng!r})")
        return
    lo, hi = rng
    if lo > hi:
        errors.append(f"{nm}: recommendation.range {rng} has lo > hi")
        return
    if param == "solvent_pct" and not (0 <= lo and hi <= 100):
        errors.append(f"{nm}: recommendation.range {rng} outside 0-100 for solvent_pct")

    # Normative records and non-swept parameters have no envelope. Ph. Eur. does not
    # report that 1:5 is optimal; it defines what may be CALLED a tincture, and
    # shelf_life_months / drug_extract_ratio are not factors anyone varies in a run.
    if rec.get("parameter_kind") == "normative" or param in ("shelf_life_months",
                                                             "drug_extract_ratio"):
        return
    rs = r.get("solvent")
    swept, optima = [], []
    for fi in findings:
        if not isinstance(fi, dict) or fi.get("varied_factor") != param:
            continue                            # a temperature sweep says nothing about a % band
        if (fi.get("conditions") or {}).get("solvent") != rs:
            continue    # Partition by solvent on EVERY axis, not just solvent_pct. Solvent
                        # boiling point, viscosity and analyte solubility all move the
                        # optimum: a methanol temperature curve is not an ethanol one.
        out = fi.get("outcome") or {}
        swept += [x for x in (out.get("comparator_levels") or []) if _num(x)]
        if _num(out.get("optimum_level")):
            optima.append(out["optimum_level"])
    if not swept:
        errors.append(f"{nm}: no finding varies '{param}' in solvent '{rs}' — nothing was swept "
                      f"on the recommended axis, so nothing supports a band")
        return
    if not (min(swept) <= lo and hi <= max(swept)):
        errors.append(f"{nm}: recommendation.range {rng} extrapolates beyond the tested envelope "
                      f"[{min(swept)}, {max(swept)}] on this axis and solvent")
    if optima and not any(lo <= x <= hi for x in optima):
        errors.append(f"{nm}: no cited optimum falls inside {rng}. Widen the band in a visible "
                      f"one-line diff or fix the band — there is no tolerance parameter")


def _check_scope(nm, rec, findings, plant_ids, errors, warnings):
    scope = rec.get("species_scope")
    if scope not in SPECIES_SCOPES:
        errors.append(f"{nm}: species_scope '{scope}' invalid (want {sorted(SPECIES_SCOPES)})")
        return
    found = sorted({_s((fi.get("material") or {}).get("species"))
                    for fi in findings if isinstance(fi, dict)
                    and _s((fi.get("material") or {}).get("species"))})
    if scope == "species-specific":
        sp = _s(rec.get("species"))
        if not BINOMIAL_RE.match(sp):
            errors.append(f"{nm}: species-specific record needs a valid `species` binomial")
            return
        if rec.get("generalisation"):
            errors.append(f"{nm}: species-specific record must not carry a generalisation block")
        wrong = [s for s in found if s != sp]
        if wrong:
            errors.append(f"{nm}: species-specific record for '{sp}' cites findings on {wrong} "
                          f"— invariant 2. Drop them or re-scope to class-general and DECLARE it.")
        pid = sp.lower().replace(" ", "-")
        if pid not in plant_ids and not rec.get("off_corpus"):
            warnings.append(f"{nm}: species '{sp}' has no plant record; set off_corpus: true "
                            f"if deliberate")
        return
    g = rec.get("generalisation") or {}
    if not g:
        errors.append(f"{nm}: class-general record requires a generalisation block — "
                      f"generalising must be explicit and reviewable, never silent")
        return
    if g.get("basis") not in GENERALISATION_BASES:
        errors.append(f"{nm}: generalisation.basis '{g.get('basis')}' invalid")
    if len(_s(g.get("rationale"))) < 80:
        errors.append(f"{nm}: generalisation.rationale must say WHY the physicochemistry carries "
                      f"across species, in >=80 chars. 'Similar compounds' is not a rationale.")
    for s in (g.get("excluded_taxa") or []):
        if not BINOMIAL_RE.match(str(s).strip()):
            errors.append(f"{nm}: excluded_taxa '{s}' is not a valid binomial")
        if str(s).strip() in found:
            errors.append(f"{nm}: '{s}' is both an excluded taxon and a source taxon")
    if len({s.split()[0] for s in found}) < 2:
        warnings.append(f"{nm}: draft class-general record rests on a single genus — it is a species "
                        f"result wearing a class label and cannot be approved")


def _check_copyright(nm, rec, errors):
    """Pharmacopoeias are paywalled, copyrighted normative texts. The schema's
    maxLength:300 and `abstract: false` are inert (nothing loads schema/*.json).
    This function is the only thing that runs."""
    # statement_summary lives on the FINDING (schema $defs.finding).
    # `normative_citations[]` is a field name from the losing draft: it is not in
    # practice.schema.json at all, so keying this gate on it means it never fires.
    for i, fi in enumerate(rec.get("findings") or []):
        if not isinstance(fi, dict):
            continue
        s = _s(fi.get("statement_summary"))
        if len(s) > 300:
            errors.append(f"{nm}: findings[{i}].statement_summary is {len(s)} chars (max 300). "
                          f"Paraphrase the requirement in ONE sentence in your own words. A "
                          f"summary long enough to substitute for buying the monograph is too "
                          f"long, and a transcription is a reproduction.")
        for k in ("monograph_text", "quote", "verbatim", "abstract"):
            if fi.get(k):
                errors.append(f"{nm}: findings[{i}] carries reproduced monograph text in '{k}' "
                              f"— cite locator.edition + locator.monograph only")
        if (fi.get("method_type") or "") == "pharmacopoeial" and not s.strip():
            errors.append(f"{nm}: findings[{i}] is pharmacopoeial and needs a statement_summary")


def _check_toxicity(nm, rec, COMPRECS, errors):
    """FAIL CLOSED, here or nowhere. compound.schema.json's `default: avoid-internal`
    is inert — nothing in scripts/ loads JSON Schema — so an absent flag is
    unconstrained unless this function treats it as avoid-internal."""
    if rec.get("record_type") != "extraction":
        return
    cid = (rec.get("key") or {}).get("compound_id")
    flag = (COMPRECS.get(cid) or {}).get("toxicity_flag", "avoid-internal")
    if flag not in TOXICITY_FLAGS:
        errors.append(f"{nm}: compounds/{cid}.yaml toxicity_flag '{flag}' invalid "
                      f"(want {sorted(TOXICITY_FLAGS)})")
        flag = "avoid-internal"
    r = rec.get("recommendation") or {}
    if flag == "none" or not r:
        return
    if len(_s(rec.get("limit_rationale"))) < 120:
        errors.append(f"{nm}: key.compound_id '{cid}' carries toxicity_flag '{flag}' (ABSENT "
                      f"counts as avoid-internal — fail closed). A recommendation keyed on it "
                      f"requires limit_rationale >=120 chars stating the dose or route limit "
                      f"and why the band is not the argmax of a yield table.")
    if flag == "topical-only" and r.get("route") != "topical":
        errors.append(f"{nm}: compound '{cid}' is topical-only; recommendation.route must be "
                      f"'topical' (got {r.get('route')!r})")
    if flag == "avoid-internal" and r.get("route") == "internal":
        errors.append(f"{nm}: compound '{cid}' is avoid-internal; no internal recommendation "
                      f"may be authored on it")
    if rec.get("status") == "approved" and not (rec.get("reviewed_by") and rec.get("verified_by")):
        errors.append(f"{nm}: approved record keyed on toxicity-flagged '{cid}' needs both "
                      f"reviewed_by and verified_by")


def _check_approval(nm, rec, findings, errors):
    rows = practice_finding_rows(rec, findings)
    idx = practice_score_from_rows(rows)
    adm = [r for r in rows if r["admissible"]]
    if idx < 5:
        errors.append(f"{nm}: approved but method-confidence index is {idx} "
                      f"(band '{practice_band(idx)}'); approval requires >=5")
    n_ind = practice_n_independent(adm)
    if rec.get("parameter_kind") == "normative":
        # R1-13: the >=2-independent-source rule was designed for empirical
        # concordance and does not apply to definitions. Disagreement between
        # bodies is TWO jurisdiction-scoped records, not one contested record.
        if not _s((rec.get("recommendation") or {}).get("jurisdiction")):
            errors.append(f"{nm}: approved normative record needs recommendation.jurisdiction "
                          f"and a jurisdiction-scoped statement ('Ph. Eur. defines a tincture "
                          f"as 1:5 in 70% ethanol') — one authority suffices only when scoped")
    elif n_ind < 2:
        errors.append(f"{nm}: approved on {n_ind} independent source(s); approval requires >=2 "
                      f"independent research groups")
    if rec.get("parameter_kind") == "empirical" and not any(
            r["tier"] in ("optimisation", "comparative-bench") for r in adm):
        errors.append(f"{nm}: approved with no optimisation or comparative-bench finding — no "
                      f"cited paper actually varied the factor being recommended")
    vb, rb = _s(rec.get("verified_by")), _s(rec.get("reviewed_by"))
    if not vb or not DATE_RE.match(str(rec.get("verified_date", ""))):
        errors.append(f"{nm}: approved record needs verified_by + verified_date — a second "
                      f"person opened the cited PDFs and checked the locators")
    elif vb.casefold() == rb.casefold():
        errors.append(f"{nm}: verified_by must DIFFER from reviewed_by. The entire content of "
                      f"the check is that it was a different person.")
    if not rec.get("reviewed_by"):
        errors.append(f"{nm}: approved record missing reviewed_by")
    if not DATE_RE.match(str(rec.get("reviewed_date", ""))):
        errors.append(f"{nm}: approved record bad reviewed_date '{rec.get('reviewed_date')}'")
    if rec.get("species_scope") == "class-general":
        gen = {s.split()[0] for s in
               {_s((fi.get("material") or {}).get("species"))
                for fi in findings if isinstance(fi, dict)} if s}
        if len(gen) < 2:
            errors.append(f"{nm}: approved class-general record rests on {len(gen)} genus/genera "
                          f"— that is a species result wearing a class label")
    disc = practice_n_independent([r for r in adm if r["in_band"] is False])
    if disc and not _s(rec.get("discordance_note")):
        errors.append(f"{nm}: {disc} independent finding(s) fall outside the band; an approved "
                      f"record must carry a discordance_note. Deleting the inconvenient finding "
                      f"to lift the score is falsifying the grade.")


# The practice evidence ladder is DEFINED ONCE, in scripts/build.py, and imported
# here so the gate and the published score can never drift. build.py guards main()
# behind __main__, so this import has no side effects.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import (PRACTICE_METHOD_TYPES, PRACTICE_FINDING_TIERS, PRACTICE_TIER_BASE,
                   ADMISSIBLE_TIERS, practice_finding_rows, practice_score_from_rows,
                   practice_band, practice_n_independent)  # noqa: E402


def main():
    errors, warnings = [], []
    declared = declared_refs()
    A = vocab_ids(os.path.join(VOCAB, "actions.yaml"))
    C = vocab_ids(os.path.join(VOCAB, "conditions.yaml"))
    # The whole compound record is kept, not just the id: toxicity_flag is read off
    # it by _check_toxicity(). K stays exactly what it was, so every existing use
    # is unaffected.
    COMPRECS = {}
    for _f in glob.glob(os.path.join(COMPDIR, "*.yaml")):
        _c = yaml.safe_load(open(_f, encoding="utf-8"))
        COMPRECS[_c["id"]] = _c
    K = set(COMPRECS)
    D = vocab_ids(os.path.join(VOCAB, "drug_classes.yaml"))
    X = vocab_ids(os.path.join(VOCAB, "dangerous_plants.yaml"))
    # Practice-corpus vocabularies. Loaded unconditionally, exactly like the five
    # above — a missing file is an unhandled FileNotFoundError that kills the gate,
    # so these YAML files and this line must land in the SAME commit. There is NO
    # parts.yaml: the part axis is frozen null in v1 (R1-3), and loading a file
    # section 1 forbids creating would kill the gate for all 187 plants.
    SOLV = vocab_map(os.path.join(VOCAB, "solvents.yaml"))
    METH = vocab_map(os.path.join(VOCAB, "extraction_methods.yaml"))
    XCLS = vocab_ids(os.path.join(VOCAB, "extraction_classes.yaml"))
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

    # ---- practice corpus (practice/**/*.yaml) ----------------------------------
    # Must run AFTER the plants loop (needs seen_ids) and BEFORE the missing/orphan
    # arithmetic below.
    bib_fields = {}
    try:
        from build import parse_bibtex as _pb
        bib_fields = {e["ref_id"]: e["fields"] for e in _pb(open(BIB, encoding="utf-8").read()) if e["ref_id"]}
    except Exception as exc:
        errors.append(f"practice: could not parse the bibliography for the kind=standard "
                      f"copyright check ({exc}) — this gate must not be skipped silently")
    # The kind=standard copyright gate. This is what bib_fields is parsed FOR, and it
    # runs over the whole bibliography, not per record — a monograph carrying an
    # `abstract` is either invented or a reproduction, whether or not a practice
    # record cites it yet.
    for _rid, _f in bib_fields.items():
        if _s(_f.get("kind")).lower() == "standard" and _s(_f.get("abstract")):
            errors.append(f"bibliography: {_rid} is kind=standard and carries an abstract. The "
                          f"Knowledge Finder renders `abstract` AS the source's own words, so "
                          f"this is either invented or a reproduction of paywalled normative text.")

    practice_files = sorted(glob.glob(os.path.join(PRACTICEDIR, "**", "*.yaml"), recursive=True))
    seen_practice_ids, practice_plant_refs = {}, []
    for path in practice_files:
        nm = "practice/" + os.path.relpath(path, PRACTICEDIR).replace("\\", "/")
        try:
            rec = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{nm}: YAML parse failed: {exc}")
            continue
        if not isinstance(rec, dict):
            errors.append(f"{nm}: not a mapping")
            continue

        # THE ORPHAN FIX. cited.update(find_refs(d)) is called exactly once today,
        # inside the plants loop. Without the mirror below, every REF cited only by a
        # practice record reports as "orphan reference (never cited)" — a WARNING, so
        # the build stays green — and osdb-verify-integrity's documented remediation
        # is to delete the bibliography entry. find_refs() walks the whole record and
        # already skips internal_notes via PROSE_KEYS, so it catches findings[],
        # context_reference_ids[], references[], avoid[].context_reference_ids[] and
        # the whole species_overrides subtree. Do NOT hand-enumerate ref fields — hand
        # enumeration is what broke this in the first place.
        cited.update(find_refs(rec))

        rid = rec.get("id")
        if rid:
            if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*(--[a-z0-9]+(-[a-z0-9]+)*)*$", str(rid)):
                errors.append(f"{nm}: bad practice id '{rid}'")
            if rid in seen_practice_ids:
                errors.append(f"{nm}: duplicate practice id '{rid}' (also {seen_practice_ids[rid]})")
            seen_practice_ids[rid] = nm

        # CRASH GUARD. One malformed record must be one error line, not a dead gate.
        # A traceback here takes down the hard gate for the whole repo, and the
        # editor's fastest way out is to delete the record — which, for a DISCORDANT
        # finding, is exactly the deletion the corpus exists to prevent.
        try:
            check_practice_record(nm, rec, seen_ids, K, COMPRECS, SOLV, METH, XCLS,
                                  bib_fields, practice_plant_refs, errors, warnings)
        except Exception as exc:
            errors.append(f"{nm}: crashed during validation ({type(exc).__name__}: {exc}) "
                          f"— fix the record shape; do not delete findings to make it pass")

    for (nm, pid) in practice_plant_refs:
        if pid not in seen_ids:
            errors.append(f"{nm}: species override plant_id '{pid}' has no plant record")

    missing = sorted(cited - declared)
    orphan = sorted(declared - cited)
    for r in missing:
        errors.append(f"cited REF not in bibliography: {r}")
    for r in orphan:
        warnings.append(f"orphan reference (never cited): {r}")

    print(f"Scanned {len(files)} plants | {len(name_files)} names files | "
          f"{len(practice_files)} practice records | "
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
