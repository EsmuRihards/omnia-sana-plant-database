#!/usr/bin/env python3
"""
scripts/build.py — the single builder for all website-facing JSON outputs.

Reads the canonical data (bibliography.bibtex, plants/, vocabularies/, compounds/)
and writes build/:
  * citations.json — Knowledge Finder (bib metadata + generated citation + plant/
    action/condition linkage). Citation is GENERATED from structured fields
    (Harvard), falling back to the legacy `annote` only for thin entries.
  * symptoms.json  — Symptom-to-Plant Lookup (plant <-> condition with evidence).
  * plants.json    — full public-safe plant index (plant pages + future tools).
  * vocab.json     — actions + conditions + compounds for UI filters / labels.

PUBLIC-SAFE: internal_notes are NEVER emitted. No timestamp embedded (clean diffs).
Stdlib + PyYAML. Run: python scripts/build.py
"""
import json, os, re, glob, urllib.parse, hashlib, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
COMPDIR = os.path.join(ROOT, "compounds")
PRACTICE = os.path.join(ROOT, "practice")
OUT = os.path.join(ROOT, "build")

# Floor for indications written to symptoms.json (the Symptom-tool feed), on the
# 1-10 evidence scale. 1 keeps every link (mechanism-inferred ones flagged
# "inferred"); raise to e.g. 5 for a high-confidence-only tool. plants.json always
# keeps the full set.
SYM_MIN_EVIDENCE = 1

REF_RE = re.compile(r"REF-\d{3,}")
FIELD_START_RE = re.compile(r"([A-Za-z][A-Za-z0-9_-]*)\s*=\s*")


def _clean(s):
    if not s:
        return ""
    s = s.replace("\\&", "&").replace("\\%", "%").replace("\\_", "_")
    s = s.replace("``", '"').replace("''", '"')
    s = re.sub(r"[{}]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def extract_fields(body):
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
        fields[key] = _clean(val)
    return fields


def parse_bibtex(text):
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
        f = extract_fields(m.group(3))
        mref = REF_RE.search(f.get("note", ""))
        entries.append({"type": m.group(1).lower(), "key": m.group(2).strip(),
                        "ref_id": mref.group(0) if mref else "", "fields": f})
    return entries


def best_link(f):
    doi = f.get("doi", "").strip()
    url = f.get("url", "").strip()
    if doi:
        return "https://doi.org/" + re.sub(r"^https?://(dx\.)?doi\.org/", "", doi), "doi"
    if url:
        return url, "url"
    q = f.get("title", "").strip() or f.get("author", "").strip()
    if q:
        return "https://scholar.google.com/scholar?q=" + urllib.parse.quote(q), "search"
    return "", "none"


def harvard(f):
    """Generate a Harvard-style citation string from structured fields."""
    au, yr, ti = f.get("author", "").rstrip(". "), f.get("year", ""), f.get("title", "").rstrip(". ")
    jo, vol, num = f.get("journal", ""), f.get("volume", ""), f.get("number", "")
    pg, doi, url = f.get("pages", ""), f.get("doi", ""), f.get("url", "")
    out = au
    if yr:
        out += " (%s)" % yr
    if ti:
        out += " '%s'" % ti
    if jo:
        out += ", %s" % jo
    loc = vol + ("(%s)" % num if num else "")
    if pg:
        loc = (loc + ", " if loc else "") + "pp. " + pg
    if loc:
        out += ", " + loc
    out = out.strip().rstrip(",. ")
    if out:
        out += "."
    if doi:
        out += " doi:" + re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    elif url:
        out += " Available at: " + url
    return out.strip()


def display_title(f, key):
    t = f.get("title", "").strip()
    if t and not t.startswith(";") and sum(c.isalpha() for c in t) >= 6:
        return t
    u = f.get("url", "")
    if u:
        m = re.match(r"https?://([^/]+)", u)
        if m:
            return re.sub(r"^www\.", "", m.group(1))
    return t or key


# Evidence tier of a single source. Driven by the explicit `study_type` field in
# the bibtex entry — the hardened, keyword-free signal. The legacy title/abstract
# keyword heuristic is kept ONLY as a fallback for entries not yet annotated, so an
# un-annotated entry can never crash the build (the backfill assigns study_type to
# every entry). Used by the website to label + order source cards by strength and
# by the evidence scorer below. Ordered strongest -> weakest:
#   review > rct > clinical > preclinical > traditional.
TIER_RANK = {"review": 0, "rct": 1, "clinical": 2, "preclinical": 3, "traditional": 4}

# Canonical study_type values stored in bibliography.bibtex -> tier.
STUDY_TYPE_TIER = {
    "systematic-review": "review",
    "meta-analysis": "review",
    "review": "review",
    "rct": "rct",
    "clinical": "clinical",
    "preclinical": "preclinical",
    "traditional": "traditional",
}


def classify_tier(f, etype):
    # 1) Explicit, keyword-free signal (preferred).
    st = (f.get("study_type", "") or "").strip().lower()
    if st in STUDY_TYPE_TIER:
        return STUDY_TYPE_TIER[st]

    # 2) Fallback heuristic for entries without a study_type.
    blob = (f.get("title", "") + " " + f.get("abstract", "")).lower()
    jour = f.get("journal", "").strip()

    def has(*kw):
        return any(k in blob for k in kw)

    if has("systematic review", "meta-analysis", "meta analysis", "metaanalysis", "cochrane"):
        return "review"
    if has("randomized", "randomised", "double-blind", "double blind", "placebo-controlled",
           "placebo controlled", "randomized controlled", "randomised controlled", "clinical trial"):
        return "rct"
    # books, monographs, materia medica and other non-journal references -> traditional
    if etype in ("book", "incollection", "inbook", "booklet") or (etype == "misc" and not jour) or \
       has("traditional", "ethnobotan", "ethnopharmacolog", "monograph", "materia medica", "folk medicine"):
        return "traditional"
    if has("patients", "human subjects", "participants", "volunteers", "in human", "humans", "open-label", "cohort", "case report"):
        return "clinical"
    if has("in vitro", "in-vitro", "animal", "mice", "mouse", " rats", " rat ", "rodent", "cell line",
           "cells", "cytotox", "molecular docking", "in silico", "antioxidant activity"):
        return "preclinical"
    return "preclinical" if jour else "traditional"


# ---- Option B evidence scoring (deterministic, 1-10) -------------------------
# An indication's score is a pure function of the study types of the references
# that back it — no AI, no opaque counts, fully reproducible:
#   base  = score of the STRONGEST single source (best tier cited)
#   bonus = reward for a BODY of HUMAN evidence (review/rct/clinical sources)
# Preclinical/traditional volume does NOT raise the score: ten in-vitro studies
# are still not clinical evidence. Result is clamped to 1..10. An editor may set
# `evidence_override` (1-10) on an indication to bypass the computation.
#
#   tier         base   |  human-source count -> bonus
#   review        7      |     >=5 -> +3
#   rct           5      |     3-4 -> +2
#   clinical      3      |       2 -> +1
#   preclinical   2      |      <2 -> +0
#   traditional   1      |
# e.g. 1 RCT = 5; 3 RCTs = 7; a meta-analysis backed by >=5 human trials = 10;
#      any number of preclinical-only sources = 2; traditional-only = 1.
TIER_BASE = {"review": 7, "rct": 5, "clinical": 3, "preclinical": 2, "traditional": 1}
HUMAN_TIERS = {"review", "rct", "clinical"}


def score_from_tiers(tiers):
    tiers = [t for t in tiers if t]
    if not tiers:
        return 1
    base = max(TIER_BASE[t] for t in tiers)
    human = sum(1 for t in tiers if t in HUMAN_TIERS)
    bonus = 3 if human >= 5 else 2 if human >= 3 else 1 if human >= 2 else 0
    return max(1, min(10, base + bonus))


# ---- PRACTICE CORPUS: the inverted evidence ladder ---------------------------
# TIER_BASE above answers "does this happen in a human body?". This one answers
# "does this number reproduce on a bench?". They INVERT and must never be
# interchanged. Do NOT touch TIER_BASE/score_from_tiers to accommodate practice:
# they feed indication_score -> plants.json and symptoms.json, and editing them
# silently moves every evidence number on the site.
#
#   * A REVIEW is the top clinical tier and scores ZERO here — it reports no
#     single (solvent, temperature, time, ratio, yield) tuple, so under the rule
#     that recommendations come from Methods and Results it cannot carry a record.
#   * A designed, quantified bench experiment is the BOTTOM clinical tier and the
#     TOP tier here.
#   * An RCT has no tier here at all. It is not evidence about extraction.
#
# method_type lives on the FINDING, not on the bibtex entry: one paper is
# 'optimisation' for the solvent axis and 'characterisation' for temperature, and
# a per-source grade would have to pick one and be wrong half the time. It also
# means reusing an existing clinical REF needs no bibliography edit.
PRACTICE_METHOD_TYPES = {
    "optimisation": "optimisation", "rsm": "optimisation", "factorial": "optimisation",
    "comparative-bench": "comparative-bench",
    "characterisation": "characterisation",
    "pharmacopoeial": "pharmacopoeial",
    "method-review": "method-review", "traditional-text": "traditional-text",
}
PRACTICE_TIER_BASE = {"optimisation": 7, "pharmacopoeial": 6, "comparative-bench": 5,
                      "characterisation": 3, "method-review": 0, "traditional-text": 0}
PRACTICE_FINDING_TIERS = {"optimisation", "comparative-bench", "characterisation",
                          "pharmacopoeial"}
# A normative standard is not a measurement of the world; it is a definition of it.
# Ph. Eur. 1559 does not report that 1:5 is optimal — it defines what may be CALLED
# a tincture. So it is authoritative for its own question and inadmissible for the
# other, in BOTH directions.
ADMISSIBLE_TIERS = {"empirical": {"optimisation", "comparative-bench", "characterisation"},
                    "normative": {"pharmacopoeial"}}
# Presentation. DELIBERATELY NOT the clinical 1-10 dots and NOT os-scoring.php: a
# user who has learned ten dots means "strong human evidence this plant works"
# will read ten dots on an extraction record as exactly that, when it means "three
# labs agree about a solvent percentage". The two can sit a few hundred pixels
# apart on one page. This artifact NEVER emits a key named `evidence`, so a
# renderer written against the clinical contract renders nothing rather than the
# wrong thing.
PRACTICE_BANDS = ((8, "established"), (5, "supported"), (2, "provisional"), (1, "insufficient"))


def practice_band(idx):
    for floor, name in PRACTICE_BANDS:
        if idx >= floor:
            return name
    return "insufficient"


def practice_independence_key(fi):
    """Identity of the RESEARCH GROUP. Concordance counts independent replication,
    not one lab's serial papers. Two editions of Ph. Eur. are one voice. Surname
    collisions merge two unrelated authors — a deliberate conservative bias: the
    error can only LOWER a score, never raise one."""
    auth = (fi.get("authority") or "").strip().lower()
    if auth:
        return "authority:" + auth
    grp = (fi.get("research_group") or "").strip().lower()
    if grp:
        return "group:" + re.sub(r"[^a-z]", "", grp)
    return "ref:" + str(fi.get("ref_id") or "")


def practice_in_band(fi, rec):
    """True / False / None. None = reports no optimum, so counts neither way.
    Compares ONLY on the recommended axis and (for solvent_pct) the recommended
    solvent: a temperature optimum of 70 C is not concordance with a 60-75%
    ethanol band. No tolerance — widening a band is a visible one-line diff."""
    r = rec.get("recommendation") or {}
    out = fi.get("outcome") or {}
    param = r.get("parameter")
    if fi.get("varied_factor") != param:
        return None
    if (fi.get("conditions") or {}).get("solvent") != r.get("solvent"):
        return None   # Same partition as validate.py's envelope, on every axis.
    rng = r.get("range")
    x = out.get("optimum_level")
    if isinstance(rng, list) and len(rng) == 2 and all(isinstance(y, (int, float)) for y in rng) \
       and isinstance(x, (int, float)) and not isinstance(x, bool):
        return rng[0] <= x <= rng[1]
    val, want = out.get("optimum_value"), r.get("value")
    if isinstance(val, str) and isinstance(want, str):
        return val.strip().casefold() == want.strip().casefold()
    return None


def practice_finding_rows(rec, findings=None):
    kind = rec.get("parameter_kind", "empirical")
    rows = []
    for fi in (findings if findings is not None else rec.get("findings") or []):
        if not isinstance(fi, dict):
            continue
        tier = PRACTICE_METHOD_TYPES.get((fi.get("method_type") or "").strip().lower(),
                                         "traditional-text")
        rows.append({"ref_id": fi.get("ref_id", ""), "tier": tier,
                     "indep": practice_independence_key(fi),
                     "admissible": tier in ADMISSIBLE_TIERS.get(kind, set()),
                     "in_band": practice_in_band(fi, rec)})
    return rows


def practice_n_independent(rows):
    return len({r["indep"] for r in rows if r["indep"]})


def practice_score_from_rows(rows):
    """base = strongest ADMISSIBLE tier; bonus = independent CONCORDANT findings;
    penalty = independent DISCORDANT ones. The penalty has no clinical analogue and
    is the point: a result outside your band is information ABOUT the band, not a
    null to be bucketed away, and a contested parameter must not score high."""
    adm = [r for r in rows if r["admissible"]]
    if not adm:
        return 1
    base = max(PRACTICE_TIER_BASE[r["tier"]] for r in adm)
    conc = practice_n_independent([r for r in adm if r["in_band"] is True])
    disc = practice_n_independent([r for r in adm if r["in_band"] is False])
    bonus = 3 if conc >= 4 else 2 if conc == 3 else 1 if conc == 2 else 0
    penalty = 2 if (disc and disc >= conc) else 1 if disc else 0
    return max(1, min(10, base + bonus - penalty))


def load_practice():
    """practice/**/*.yaml. A missing directory yields [] — glob on a nonexistent
    path returns [], so an empty or absent corpus builds green."""
    out = []
    for fn in sorted(glob.glob(os.path.join(PRACTICE, "**", "*.yaml"), recursive=True)):
        d = yaml.safe_load(open(fn, encoding="utf-8"))
        if isinstance(d, dict):
            out.append(d)
    return out


def load_plants():
    out = []
    for fn in sorted(glob.glob(os.path.join(PLANTS, "*.yaml"))):
        out.append(yaml.safe_load(open(fn, encoding="utf-8")))
    return out


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").strip().lower())
    return s.strip("-")


def resolve_common_slugs(plants):
    """Public URL slug per plant for /plants/<slug>/. An explicit `common_slug`
    override wins and reserves the slug; otherwise it is derived from the primary
    common name. Collisions resolve deterministically (plants ordered by permanent
    id): the first claimant keeps the derived slug, later ones fall back to their
    Latin id (which is globally unique). Returns {plant_id: slug}."""
    out, taken = {}, {}
    ordered = sorted(plants, key=lambda p: p.get("id", ""))
    for p in ordered:                      # explicit overrides first
        ov = p.get("common_slug")
        if ov:
            out[p["id"]], taken[ov] = ov, p["id"]
    for p in ordered:
        if p["id"] in out:
            continue
        base = slugify((p.get("common_names") or [p.get("scientific_name", "")])[0]) or p["id"]
        slug = base if (base not in taken) else p["id"]   # collision -> permanent Latin id
        out[p["id"]], taken[slug] = slug, p["id"]
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    actions = {a["id"]: a for a in yaml.safe_load(open(os.path.join(VOCAB, "actions.yaml"), encoding="utf-8"))}
    conditions = {c["id"]: c for c in yaml.safe_load(open(os.path.join(VOCAB, "conditions.yaml"), encoding="utf-8"))}
    drug_classes = {d["id"]: d for d in yaml.safe_load(open(os.path.join(VOCAB, "drug_classes.yaml"), encoding="utf-8"))}
    dangerous_plants = {d["id"]: d for d in yaml.safe_load(open(os.path.join(VOCAB, "dangerous_plants.yaml"), encoding="utf-8"))}
    compounds = {}
    for fn in sorted(glob.glob(os.path.join(COMPDIR, "*.yaml"))):
        c = yaml.safe_load(open(fn, encoding="utf-8"))
        compounds[c["id"]] = c
    plants = load_plants()
    slugs = resolve_common_slugs(plants)
    # Loaded here, before citations.json, because the corpus dimension and the
    # practice linkage both feed the citation rows below.
    practice = load_practice()
    # Whole-tree walk mirroring validate.py's find_refs(). The ref surface is
    # findings[], context_reference_ids[], references[], avoid[].context_reference_ids[]
    # and the whole species_overrides subtree. Hand-enumerating it is how a source
    # gets silently mislabelled `clinical` in the public library.
    #
    # Own pattern, NOT build.py's module-level REF_RE, which is r"REF-\d{3,}" while
    # validate.py's is r"REF-\d{4,}". No live id is 3-digit so the two agree today, but
    # "mirrors find_refs()" has to be true of the regex as well as the traversal, or the
    # corpus derivation and the orphan accounting drift apart the first time a 3-digit
    # id exists. Do not swap in REF_RE to save a line.
    _PRACTICE_REF_RE = re.compile(r"REF-\d{4,}")
    _PROSE = {"internal_notes"}

    def _walk_refs(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k not in _PROSE:
                    yield from _walk_refs(v)
        elif isinstance(node, list):
            for v in node:
                yield from _walk_refs(v)
        elif isinstance(node, str):
            yield from _PRACTICE_REF_RE.findall(node)

    practice_refs = set()
    for _pr in practice:
        practice_refs.update(_walk_refs(_pr))
    # Public-safe drug-class list (NO editor-facing `examples`), shared by vocab.json
    # and interactions.v1.json.
    dc_public = sorted(
        [{"id": d["id"], "label": d["label"], "consumer_description": d.get("consumer_description", ""),
          "category": d.get("category", "")} for d in drug_classes.values()],
        key=lambda d: d["label"].lower())
    # Public-safe dangerous-plant vocab (strip editor_notes; keep toxicology the tool
    # renders). Keyed by id for the lookalike emitter; embedded (as a sorted list) in
    # lookalikes.v1.json so the front-end can label every referenced toxic plant.
    def _dp_pub(d):
        return {k: v for k, v in d.items() if k != "editor_notes"}
    dp_public = {d["id"]: _dp_pub(d) for d in dangerous_plants.values()}
    name_of = lambda p: (p.get("common_names") or [p["scientific_name"]])[0]

    # ---- ref -> linkage inversion (claim-level) ----
    inv = {}

    def add(ref, plant, kind, label=None):
        d = inv.setdefault(ref, {"plants": set(), "scientific": set(), "actions": set(), "conditions": set()})
        for cn in plant.get("common_names", []):
            d["plants"].add(cn)
        if plant.get("scientific_name"):
            d["scientific"].add(plant["scientific_name"])
        if kind == "action" and label:
            d["actions"].add(label)
        if kind == "condition" and label:
            d["conditions"].add(label)

    for p in plants:
        for a in p.get("actions", []):
            lbl = actions.get(a["action"], {}).get("label", a["action"])
            for r in a.get("reference_ids", []):
                add(r, p, "action", lbl)
        for i in p.get("indications", []):
            lbl = conditions.get(i["condition"], {}).get("label", i["condition"])
            for r in i.get("reference_ids", []):
                add(r, p, "condition", lbl)
        for c in p.get("constituents", []):
            for r in c.get("reference_ids", []):
                add(r, p, "other")
        for c in p.get("contraindications", []):
            for r in c.get("reference_ids", []):
                add(r, p, "other")
        for it in p.get("drug_class_interactions", []):
            for r in it.get("reference_ids", []):
                add(r, p, "other")
        for pr in p.get("pairings", []):
            for r in pr.get("reference_ids", []):
                add(r, p, "other")
        for r in p.get("references", []):
            add(r, p, "other")

    # ---- citations.json ----
    entries = parse_bibtex(open(BIB, encoding="utf-8").read())
    # ref_id -> evidence tier (study_type-driven), reused by the symptom scorer below.
    tier_by_ref = {e["ref_id"]: classify_tier(e["fields"], e["type"]) for e in entries if e["ref_id"]}
    cites = []
    for e in entries:
        f = e["fields"]
        link, lt = best_link(f)
        # Citation is generated from structured fields (annote was dropped after its
        # volume/issue/pages were backfilled into structured fields).
        citation = harvard(f)
        pi = inv.get(e["ref_id"], {"plants": set(), "scientific": set(), "actions": set(), "conditions": set()})
        cites.append({
            "ref_id": e["ref_id"], "key": e["key"], "type": e["type"],
            "title": f.get("title", ""), "authors": f.get("author", ""),
            "journal": f.get("journal", ""), "year": f.get("year", ""),
            "doi": f.get("doi", ""), "url": f.get("url", ""), "link": link, "link_type": lt,
            "citation": citation, "abstract": f.get("abstract", ""),
            "tier": classify_tier(f, e["type"]),
            # DERIVED, never declared. A derived value cannot drift from reality,
            # and a paper measuring both extraction yield and bioactivity legitimately
            # belongs to both — which is why it is an ARRAY. Behaviour when a REF is
            # cited by neither: ["clinical"], so all 3110 existing entries are
            # correctly labelled with zero backfill.
            "corpus": (["clinical"] if e["ref_id"] not in practice_refs
                       else (["clinical", "practice"] if e["ref_id"] in inv else ["practice"])),
            "display": display_title(f, e["key"]),
            "plants": sorted(pi["plants"]), "scientific": sorted(pi["scientific"]),
            "actions": sorted(pi["actions"]), "conditions": sorted(pi["conditions"]),
        })
    def _year(c):
        m = re.search(r"\b(\d{4})\b", c["year"] or "")
        return int(m.group(1)) if m else 0
    cites.sort(key=lambda c: c["display"].lower())
    cites.sort(key=_year, reverse=True)
    write(os.path.join(OUT, "citations.json"), {"schema": "omnia-sana/knowledge-finder@2", "count": len(cites), "citations": cites})

    # ---- symptoms.json ----
    def indication_score(i):
        # Editorial override wins; otherwise compute from the cited study types.
        ov = i.get("evidence_override")
        if isinstance(ov, int):
            return max(1, min(10, ov))
        return score_from_tiers([tier_by_ref.get(r) for r in i.get("reference_ids", [])])

    sym_plants = []
    for p in plants:
        scored = [(i, indication_score(i)) for i in p.get("indications", [])]
        keep = [(i, sc) for (i, sc) in scored if sc >= SYM_MIN_EVIDENCE]
        if not keep:
            continue
        keep.sort(key=lambda t: (-t[1],
                                 conditions.get(t[0]["condition"], {}).get("label", t[0]["condition"]).lower()))
        sym_plants.append({
            "name": (p.get("common_names") or [p["scientific_name"]])[0],
            "scientific": p["scientific_name"],
            "id": p.get("id"),
            "common_slug": slugs[p["id"]],
            "wp_post_id": p.get("wp_post_id"),
            # `references` are the claim-level reference ids for this plant<->condition
            # association — they make symptoms.json self-contained for the Symptom-tool
            # "View Sources" pages (the WP handler can also read them from plants.json).
            "indications": [{"condition": i["condition"],
                            "label": conditions.get(i["condition"], {}).get("label", i["condition"]),
                            "evidence": sc, "status": i.get("status", ""),
                            "inferred": i.get("status") == "needs-review",
                            "references": list(i.get("reference_ids", []))}
                           for (i, sc) in keep],
        })
    sym_conditions = [{"id": c["id"], "label": c["label"], "body_system": c.get("body_system", ""),
                       "consumer_synonyms": c.get("consumer_synonyms", []),
                       "related_actions": c.get("related_actions", [])} for c in conditions.values()]
    write(os.path.join(OUT, "symptoms.json"),
          {"schema": "omnia-sana/symptom-lookup@1", "count": len(sym_plants),
           "conditions": sorted(sym_conditions, key=lambda c: c["label"].lower()),
           "plants": sorted(sym_plants, key=lambda p: p["name"].lower())})

    # ---- plants.json (public-safe: drop internal_notes; inject resolved common_slug;
    #      filter safety records to approved-only so /plants can never leak a draft) ----
    def approved_only(items):
        return [x for x in (items or []) if x.get("status") == "approved"]

    # D8 — NOTHING UNSOURCED PUBLISHES. Owner decision, 2026-07-20.
    #
    # approved_only() above covers the three SAFETY lists, which use the
    # draft/approved vocabulary. The editorial lists (preparations, dosage,
    # indications, actions, contraindications) use verified/needs-review/draft and
    # never carry the value "approved" at all, so approved_only() cannot gate them —
    # applied there it would empty them completely. What gates them is evidence:
    # an entry with no reference_ids is an unsourced public claim on a site whose
    # whole proposition is that it cites things.
    #
    # Measured at the time of writing: this withheld 244 of 549 preparations and
    # 53 of 220 dosages. The 53 were the sharp case — specific ingestible
    # quantities attributed to unnamed "traditional herbal references".
    #
    # Nothing is deleted. The YAML keeps every word; an entry reappears here the
    # moment it earns a citation. Any FUTURE statused list on a plant record
    # inherits this automatically by being named in SOURCED_ONLY_KEYS — which is
    # the point, because the old leak path was that new fields shipped by default.
    SOURCED_ONLY_KEYS = ("preparations", "dosage")

    def sourced_only(items):
        return [x for x in (items or [])
                if isinstance(x, dict) and (x.get("reference_ids") or [])]

    withheld = {k: 0 for k in SOURCED_ONLY_KEYS}
    pub = []
    for p in plants:
        q = {k: v for k, v in p.items() if k != "internal_notes"}
        q["common_slug"] = slugs[p["id"]]
        for _k in SOURCED_ONLY_KEYS:
            if _k in q:
                _before = len(q[_k] or [])
                q[_k] = sourced_only(q[_k])
                withheld[_k] += _before - len(q[_k])
        # Enrich indications with the computed 1-10 evidence score + condition label so
        # plants.json is a self-contained record for plant pages + the embed card (the
        # raw score lives only in symptoms.json otherwise).
        if "indications" in q:
            q["indications"] = [dict(i, evidence=indication_score(i),
                                     label=conditions.get(i["condition"], {}).get("label", i["condition"]))
                                for i in q["indications"]]
        if "drug_class_interactions" in q:
            q["drug_class_interactions"] = approved_only(q["drug_class_interactions"])
        if "pairings" in q:
            q["pairings"] = approved_only(q["pairings"])
        if "dangerous_lookalikes" in q:
            q["dangerous_lookalikes"] = approved_only(q["dangerous_lookalikes"])
        pub.append(q)
    write(os.path.join(OUT, "plants.json"), {"schema": "omnia-sana/plants@1", "count": len(pub), "plants": pub})
    # Report what was withheld. A silent filter reads as "there was nothing to hide";
    # this number is the honest coverage debt and should fall as entries get sourced.
    _w = ", ".join("%d %s" % (v, k) for k, v in sorted(withheld.items()) if v)
    print("  plants.json    : withheld unsourced %s" % _w if _w
          else "  plants.json    : no unsourced entries withheld")

    # ---- vocab.json ----
    write(os.path.join(OUT, "vocab.json"), {
        "schema": "omnia-sana/vocab@1",
        "actions": [{"id": a["id"], "label": a["label"], "category": a.get("category", "")} for a in actions.values()],
        "conditions": sym_conditions,
        "drug_classes": dc_public,
        "dangerous_plants": sorted(dp_public.values(), key=lambda d: d["label"].lower()),
        # Defaults applied HERE, not by JSON Schema (which nothing loads): absent
        # resolution is 'unresolvable' and absent toxicity_flag is 'avoid-internal',
        # so an untriaged compound reaches the front end as "no recommendation"
        # rather than as silence a renderer can misread as "safe".
        "compounds": [{"id": c["id"], "name": c["name"], "class": c.get("class", ""),
                       "extraction_class": c.get("extraction_class", []),
                       "resolution": c.get("resolution", "unresolvable"),
                       "toxicity_flag": c.get("toxicity_flag", "avoid-internal"),
                       "regulatory_limit": c.get("regulatory_limit", "")}
                      for c in compounds.values()],
    })

    # ---- names.json (Multilingual Plant-Name Dictionary feed) --------------------
    # Joins the verified vernacular-name records (names/*.yaml) to plant identity and
    # ships ONLY status: verified names (needs-review entries are dropped here — they are
    # never served publicly). Reusable by the dictionary tool AND any other tool that
    # wants to resolve/search a plant by a name in any European language.
    languages = yaml.safe_load(open(os.path.join(VOCAB, "languages.yaml"), encoding="utf-8"))
    lang_pub = [{"code": l["code"], "iso3": l.get("iso3", ""), "name_en": l["name_en"],
                 "endonym": l["endonym"], "script": l.get("script", "Latin"), "tier": l.get("tier", "")}
                for l in languages if l.get("enabled")]
    lang_order = [l["code"] for l in lang_pub]
    plant_by_id = {p["id"]: p for p in plants}
    name_rows, coverage = [], {c: 0 for c in lang_order}
    for fn in sorted(glob.glob(os.path.join(ROOT, "names", "*.yaml"))):
        rec = yaml.safe_load(open(fn, encoding="utf-8"))
        p = plant_by_id.get(rec.get("id"))
        if not p:
            continue
        pub_names = {}
        for lang in lang_order:
            keep = [{"name": e["name"], "preferred": bool(e.get("preferred")), "sources": e.get("sources", [])}
                    for e in (rec.get("names", {}).get(lang) or [])
                    if e.get("status", "verified") != "needs-review"]
            if keep:
                keep.sort(key=lambda e: (not e["preferred"], e["name"].casefold()))
                pub_names[lang] = keep
                coverage[lang] += 1
        if not pub_names:
            continue
        name_rows.append({
            "id": rec["id"],
            "scientific_name": rec.get("scientific_name", p.get("scientific_name", "")),
            "common_slug": slugs[p["id"]],
            "family": p.get("family", ""),
            "wp_post_id": p.get("wp_post_id"),
            "english": (p.get("common_names") or [""])[0],
            "external_ids": p.get("external_ids", {}),
            "names": pub_names,
        })
    write(os.path.join(OUT, "names.json"), {
        "schema": "omnia-sana/names@1",
        "count": len(name_rows),
        "languages": lang_pub,
        "coverage": coverage,
        "plants": sorted(name_rows, key=lambda r: r["scientific_name"].lower()),
    })

    # ---- interactions.v1.json (Herb-Drug Interaction Checker feed) ----------------
    # PUBLIC file carries approved records ONLY; the *.draft.json twin carries every
    # record (draft + approved) for the review workflow and is NOT deployed publicly.
    def interaction_rows(status):
        rows = []
        for p in plants:
            for it in p.get("drug_class_interactions", []):
                if status and it.get("status") != status:
                    continue
                dc = drug_classes.get(it["drug_class"], {})
                rows.append({
                    "plant_id": p["id"], "plant": name_of(p), "scientific": p["scientific_name"],
                    "common_slug": slugs[p["id"]], "wp_post_id": p.get("wp_post_id"),
                    "drug_class": it["drug_class"], "drug_class_label": dc.get("label", it["drug_class"]),
                    "severity": it["severity"], "mechanism": it.get("mechanism", ""),
                    "references": list(it.get("reference_ids", [])), "status": it.get("status", ""),
                })
        rows.sort(key=lambda r: (r["plant"].lower(), r["drug_class_label"].lower()))
        return rows

    approved_int, draft_int = interaction_rows("approved"), interaction_rows(None)
    write(os.path.join(OUT, "interactions.v1.json"),
          {"schema": "omnia-sana/interactions@1", "count": len(approved_int),
           "drug_classes": dc_public, "interactions": approved_int})
    write(os.path.join(OUT, "interactions.v1.draft.json"),
          {"schema": "omnia-sana/interactions@1", "count": len(draft_int),
           "drug_classes": dc_public, "interactions": draft_int})

    # ---- pairings.v1.json (Herb-Herb Combinations feed) --------------------------
    # Directionless: every pairing is emitted BOTH ways so a query by either herb id
    # resolves it. Approved-only public + full draft twin, same as interactions.
    by_id = {p["id"]: p for p in plants}

    def pairing_rows(status):
        seen, rows = set(), []
        for p in plants:
            for pr in p.get("pairings", []):
                if status and pr.get("status") != status:
                    continue
                partner = by_id.get(pr["partner_id"])
                if not partner:
                    continue
                for a, b in ((p, partner), (partner, p)):
                    k = (a["id"], b["id"], pr["type"])
                    if k in seen:
                        continue
                    seen.add(k)
                    rows.append({
                        "herb_id": a["id"], "herb": name_of(a), "herb_slug": slugs[a["id"]],
                        "partner_id": b["id"], "partner": name_of(b), "partner_slug": slugs[b["id"]],
                        "type": pr["type"], "note": pr.get("note", ""),
                        "references": list(pr.get("reference_ids", [])), "status": pr.get("status", ""),
                    })
        rows.sort(key=lambda r: (r["herb"].lower(), r["partner"].lower()))
        return rows

    approved_pair, draft_pair = pairing_rows("approved"), pairing_rows(None)
    write(os.path.join(OUT, "pairings.v1.json"),
          {"schema": "omnia-sana/pairings@1", "count": len(approved_pair), "pairings": approved_pair})
    write(os.path.join(OUT, "pairings.v1.draft.json"),
          {"schema": "omnia-sana/pairings@1", "count": len(draft_pair), "pairings": draft_pair})

    # ---- lookalikes.v1.json (Dangerous Lookalikes feed) --------------------------
    # ONE-DIRECTIONAL (NOT mirrored, unlike pairings): each medicinal plant lists the
    # toxic plants IT is mistaken for + how to tell them apart. Carries the three-state
    # review flag so the tool distinguishes "not researched" (plant ABSENT from feed)
    # from "researched, none known" from "has hazards". Public file = approved rows
    # ONLY; a reviewed has-lookalikes plant with no approved rows yet stays absent
    # (renders as 'not researched'), never as an empty/alarming hazard list. The
    # .draft twin carries every row and is NOT deployed.
    SEV_ORDER = {"fatal": 0, "dangerous": 1, "irritant": 2, "caution": 3}

    def lookalike_plants(status):
        out = []
        for p in plants:
            review = p.get("lookalikes_review")
            las = p.get("dangerous_lookalikes", [])
            if status:
                las = [x for x in las if x.get("status") == status]
            rows = []
            for la in las:
                dp = dangerous_plants.get(la["dangerous_plant"], {})
                rows.append({
                    "dangerous_plant": la["dangerous_plant"],
                    "dangerous_plant_label": dp.get("label", la["dangerous_plant"]),
                    "kingdom": dp.get("kingdom", "plant"),
                    "severity": la["severity"],
                    "confused_part": la.get("confused_part", ""),
                    "confusion_context": la.get("confusion_context", ""),
                    "distinguishing_features": list(la.get("distinguishing_features", [])),
                    "key_test": la.get("key_test", ""),
                    "references": list(la.get("reference_ids", [])),
                    "status": la.get("status", ""),
                })
            rows.sort(key=lambda r: (SEV_ORDER.get(r["severity"], 9), r["dangerous_plant_label"].lower()))
            outcome = (review or {}).get("outcome")
            include = bool(rows) or outcome == "none-known"
            if status is None:
                include = include or bool(review) or bool(las)
            if not include:
                continue
            rec = {
                "plant_id": p["id"], "plant": name_of(p), "scientific": p["scientific_name"],
                "common_slug": slugs[p["id"]], "wp_post_id": p.get("wp_post_id"),
                "review_outcome": "has-lookalikes" if rows else "none-known",
                "lookalikes": rows,
            }
            if review:
                if review.get("reference_ids"):
                    rec["review_reference_ids"] = list(review["reference_ids"])
                if review.get("reviewed_by"):
                    rec["reviewed_by"] = review["reviewed_by"]
                if review.get("reviewed_date"):
                    rec["reviewed_date"] = review["reviewed_date"]
            out.append(rec)
        out.sort(key=lambda r: r["plant"].lower())
        return out

    dp_list = sorted(dp_public.values(), key=lambda d: d["label"].lower())
    approved_la, draft_la = lookalike_plants("approved"), lookalike_plants(None)
    n_appr_rows = sum(len(r["lookalikes"]) for r in approved_la)
    n_draft_rows = sum(len(r["lookalikes"]) for r in draft_la)
    write(os.path.join(OUT, "lookalikes.v1.json"),
          {"schema": "omnia-sana/lookalikes@1", "count": n_appr_rows,
           "plants_covered": len(approved_la), "dangerous_plants": dp_list, "plants": approved_la})
    write(os.path.join(OUT, "lookalikes.v1.draft.json"),
          {"schema": "omnia-sana/lookalikes@1", "count": n_draft_rows,
           "plants_covered": len(draft_la), "dangerous_plants": dp_list, "plants": draft_la})

    # ---- practice.v1.json (tincture / formula calculator provenance feed) --------
    # PUBLIC file carries approved records ONLY. The twin MUST be named
    # practice.v1.draft.json: that inherits the existing `build/*.draft.json` line in
    # .gitignore, so it never reaches osdb/main and therefore never reaches the
    # WordPress sync. Any other name publishes unreviewed extraction recommendations
    # straight to the live site. This is the highest-consequence name in the change.
    def practice_rows(status):
        rows = []
        for pr in practice:
            if status and pr.get("status") != status:
                continue
            rws = practice_finding_rows(pr)
            idx = practice_score_from_rows(rws)
            adm = [r for r in rws if r["admissible"]]
            k = pr.get("key") or {}
            rows.append({
                "id": pr.get("id", ""), "record_type": pr.get("record_type", ""),
                "parameter_kind": pr.get("parameter_kind", ""),
                "species_scope": pr.get("species_scope", ""),
                "compound_id": k.get("compound_id"), "species": pr.get("species", ""),
                "extraction_class": k.get("extraction_class"), "part": k.get("part"),
                "solvent": k.get("solvent"), "method": k.get("method"),
                "recommendation": pr.get("recommendation") or {},
                "avoid": pr.get("avoid") or [],
                "source_taxa": sorted({str((f.get("material") or {}).get("species") or "").strip()
                                       for f in (pr.get("findings") or []) if isinstance(f, dict)
                                       and (f.get("material") or {}).get("species")}),
                "excluded_taxa": sorted((pr.get("generalisation") or {}).get("excluded_taxa") or []),
                "discordance_note": pr.get("discordance_note", ""),
                "references": sorted({f["ref_id"] for f in (pr.get("findings") or [])
                                      if isinstance(f, dict) and f.get("ref_id")}),
                # Method confidence. NOT the clinical evidence scale. `scale` is a hard
                # assertion a front end can test; there is deliberately no key named
                # `evidence` anywhere in this row.
                "confidence_band": practice_band(idx), "confidence_index": idx,
                "basis_tier": max(adm, key=lambda r: PRACTICE_TIER_BASE[r["tier"]])["tier"] if adm else "",
                "concordant_sources": practice_n_independent([r for r in adm if r["in_band"] is True]),
                "discordant_sources": practice_n_independent([r for r in adm if r["in_band"] is False]),
                "scale": "omnia-sana/method-confidence@1",
                "status": pr.get("status", ""),
            })
        rows.sort(key=lambda r: (str(r["compound_id"] or ""),
                                 str(r["extraction_class"] or ""), str(r["part"] or ""),
                                 str(r["solvent"] or ""), str(r["method"] or ""), r["id"]))
        return rows

    approved_pr, draft_pr = practice_rows("approved"), practice_rows(None)
    solvents_pub, methods_pub, xclasses_pub = [], [], []
    for _fn, _sink in ((os.path.join(VOCAB, "solvents.yaml"), solvents_pub),
                       (os.path.join(VOCAB, "extraction_methods.yaml"), methods_pub),
                       (os.path.join(VOCAB, "extraction_classes.yaml"), xclasses_pub)):
        for _v in yaml.safe_load(open(_fn, encoding="utf-8")):
            # `note` is editorial; `optimal_ethanol_pct` and `compounds` are EDITOR
            # ORIENTATION with no reference behind them. An unsourced band sitting in
            # the calculator's own data file is the number that gets used when a class
            # has no resolved record, so it must not exist in the public artifact.
            _sink.append({k: v for k, v in _v.items()
                          if k not in ("note", "optimal_ethanol_pct", "compounds")})
    write(os.path.join(OUT, "practice.v1.json"),
          {"schema": "omnia-sana/practice@1", "count": len(approved_pr),
           "solvents": solvents_pub, "methods": methods_pub, "classes": xclasses_pub,
           "records": approved_pr})
    write(os.path.join(OUT, "practice.v1.draft.json"),
          {"schema": "omnia-sana/practice@1", "count": len(draft_pr),
           "solvents": solvents_pub, "methods": methods_pub, "classes": xclasses_pub,
           "records": draft_pr})

    # ---- manifest.json (versioning + integrity; no timestamp -> clean diffs) ------
    artifacts = {}
    for fn in ["citations.json", "symptoms.json", "plants.json", "vocab.json", "names.json",
               "interactions.v1.json", "pairings.v1.json", "lookalikes.v1.json",
               "practice.v1.json"]:
        raw = open(os.path.join(OUT, fn), "rb").read()
        head = json.loads(raw.decode("utf-8"))
        artifacts[fn] = {"schema": head.get("schema", ""), "count": head.get("count"),
                         "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
    write(os.path.join(OUT, "manifest.json"), {"schema": "omnia-sana/manifest@1", "artifacts": artifacts})

    linked = sum(1 for c in cites if c["plants"])
    print("build/ written:")
    print("  citations.json : %d citations (%d linked to >=1 plant)" % (len(cites), linked))
    print("  symptoms.json  : %d plants, %d conditions" % (len(sym_plants), len(sym_conditions)))
    print("  plants.json    : %d plants" % len(pub))
    print("  names.json     : %d plants w/ verified names, %d languages" % (len(name_rows), len(lang_pub)))
    print("  vocab.json     : %d actions, %d conditions, %d drug-classes, %d compounds" % (len(actions), len(conditions), len(drug_classes), len(compounds)))
    print("  interactions   : %d approved (%d incl. draft) [.v1.json + .draft twin]" % (len(approved_int), len(draft_int)))
    print("  pairings       : %d approved (%d incl. draft) [.v1.json + .draft twin]" % (len(approved_pair), len(draft_pair)))
    print("  lookalikes     : %d approved rows / %d plants (%d rows incl. draft) [.v1.json + .draft twin]" % (n_appr_rows, len(approved_la), n_draft_rows))
    print("  practice       : %d approved (%d incl. draft) [.v1.json + .draft twin]" % (len(approved_pr), len(draft_pr)))
    print("  manifest.json  : %d artifacts hashed" % len(artifacts))


def write(path, obj):
    # newline="\n" forces LF on every platform so build outputs (and the manifest
    # sha256/bytes computed from them) are byte-identical on Windows and CI (Linux).
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


if __name__ == "__main__":
    main()
