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

# Floor for indications written to symptoms.json (the Symptom-tool feed). 1 keeps
# every link (mechanism-inferred ones flagged "inferred"); raise to e.g. 3 for a
# high-confidence-only tool. plants.json always keeps the full set.
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


# Evidence tier of a single source, derived heuristically from its bibtex type and
# title/abstract wording. Used by the website to label + order source cards by
# strength (strongest first). Coarse and automatic — an editor can always refine.
# Ordered strongest -> weakest: review > rct > clinical > preclinical > traditional.
TIER_RANK = {"review": 0, "rct": 1, "clinical": 2, "preclinical": 3, "traditional": 4}


def classify_tier(f, etype):
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
    sym_plants = []
    for p in plants:
        keep = [i for i in p.get("indications", []) if i.get("evidence", 0) >= SYM_MIN_EVIDENCE]
        if not keep:
            continue
        keep.sort(key=lambda i: (-i.get("evidence", 0),
                                 conditions.get(i["condition"], {}).get("label", i["condition"]).lower()))
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
                            "evidence": i["evidence"], "status": i.get("status", ""),
                            "inferred": i.get("status") == "needs-review",
                            "references": list(i.get("reference_ids", []))}
                           for i in keep],
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
