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
import json, os, re, glob, urllib.parse, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB = os.path.join(ROOT, "bibliography.bibtex")
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
COMPDIR = os.path.join(ROOT, "compounds")
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


def load_plants():
    out = []
    for fn in sorted(glob.glob(os.path.join(PLANTS, "*.yaml"))):
        out.append(yaml.safe_load(open(fn, encoding="utf-8")))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    actions = {a["id"]: a for a in yaml.safe_load(open(os.path.join(VOCAB, "actions.yaml"), encoding="utf-8"))}
    conditions = {c["id"]: c for c in yaml.safe_load(open(os.path.join(VOCAB, "conditions.yaml"), encoding="utf-8"))}
    compounds = {}
    for fn in sorted(glob.glob(os.path.join(COMPDIR, "*.yaml"))):
        c = yaml.safe_load(open(fn, encoding="utf-8"))
        compounds[c["id"]] = c
    plants = load_plants()

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

    # ---- plants.json (public-safe: drop internal_notes) ----
    pub = []
    for p in plants:
        q = {k: v for k, v in p.items() if k != "internal_notes"}
        pub.append(q)
    write(os.path.join(OUT, "plants.json"), {"schema": "omnia-sana/plants@1", "count": len(pub), "plants": pub})

    # ---- vocab.json ----
    write(os.path.join(OUT, "vocab.json"), {
        "schema": "omnia-sana/vocab@1",
        "actions": [{"id": a["id"], "label": a["label"], "category": a.get("category", "")} for a in actions.values()],
        "conditions": sym_conditions,
        "compounds": [{"id": c["id"], "name": c["name"], "class": c.get("class", "")} for c in compounds.values()],
    })

    linked = sum(1 for c in cites if c["plants"])
    print("build/ written:")
    print("  citations.json : %d citations (%d linked to >=1 plant)" % (len(cites), linked))
    print("  symptoms.json  : %d plants, %d conditions" % (len(sym_plants), len(sym_conditions)))
    print("  plants.json    : %d plants" % len(pub))
    print("  vocab.json     : %d actions, %d conditions, %d compounds" % (len(actions), len(conditions), len(compounds)))


def write(path, obj):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write("\n")


if __name__ == "__main__":
    main()
