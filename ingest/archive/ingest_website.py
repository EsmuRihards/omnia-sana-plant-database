#!/usr/bin/env python3
"""
ingest_website.py — fold omniasana.bio content into the local plant database.

Additive only; it does NOT change the schema/architecture. It:
  1. Adds every source cited on the site's Materia Medica plant pages plus the
     Symptom-to-Plant Lookup tool to bibliography.bibtex (continuing REF ids).
  2. Creates new plant records that are on the site but not in the DB:
       - White Dead Nettle (Lamium album) — full, part-mapped, well cited.
       - 77 plants from the Symptom-to-Plant Lookup tool — skeletal records
         (symptom associations + the tool's evidence score), status needs-review.
         (Holy Basil merges the tool data with its Materia Medica stub.)
  3. Enriches existing records that have a richer site page (Plantago major,
     Achillea millefolium) with site-sourced constituents, actions and cautions.

Data sources (saved provenance):
  tools/sources/symptom_lookup.json     — the tool's PLANTS array
  tools/sources/website_references.json — verbatim reference lists per page

Run AFTER ingest_book.py and add_dandelion.py. Idempotent: reference entries
dedupe by citation text, plant files overwrite, enrichment dedupes by name/text.
"""

import os
import re
import json
import unicodedata

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PLANTS_DIR = os.path.join(ROOT, "plants")
BIBLIO = os.path.join(ROOT, "bibliography.bibtex")
SRC = os.path.join(HERE, "sources")
LAST_UPDATED = "2026-06-12"

# --------------------------------------------------------------------------- #
# Genus -> family (modern circumscription) for every genus added here.
# --------------------------------------------------------------------------- #
GENUS_FAMILY = {
    "Lamium": "Lamiaceae", "Ocimum": "Lamiaceae",
    "Agrimonia": "Rosaceae", "Vaccinium": "Ericaceae", "Andrographis": "Acanthaceae",
    "Angelica": "Apiaceae", "Arnica": "Asteraceae", "Cynara": "Asteraceae",
    "Astragalus": "Fabaceae", "Epilobium": "Onagraceae", "Arctostaphylos": "Ericaceae",
    "Bistorta": "Polygonaceae", "Momordica": "Cucurbitaceae", "Actaea": "Ranunculaceae",
    "Rubus": "Rosaceae", "Cnicus": "Asteraceae", "Boswellia": "Burseraceae",
    "Ruscus": "Asparagaceae", "Petasites": "Asteraceae", "Eschscholzia": "Papaveraceae",
    "Cinnamomum": "Lauraceae", "Centaurium": "Gentianaceae", "Vitex": "Lamiaceae",
    "Zea": "Poaceae", "Elymus": "Poaceae", "Viburnum": "Adoxaceae",
    "Verbascum": "Scrophulariaceae", "Harpagophytum": "Pedaliaceae", "Inula": "Asteraceae",
    "Oenothera": "Onagraceae", "Euphrasia": "Orobanchaceae", "Tanacetum": "Asteraceae",
    "Scrophularia": "Scrophulariaceae", "Gentiana": "Gentianaceae", "Hydrastis": "Ranunculaceae",
    "Centella": "Apiaceae", "Chelidonium": "Papaveraceae", "Viola": "Violaceae",
    "Hibiscus": "Malvaceae", "Marrubium": "Lamiaceae", "Aesculus": "Sapindaceae",
    "Hedera": "Araliaceae", "Aloysia": "Verbenaceae", "Arctium": "Asteraceae",
    "Tilia": "Malvaceae", "Pulmonaria": "Boraginaceae", "Malva": "Malvaceae",
    "Althaea": "Malvaceae", "Silybum": "Asteraceae", "Origanum": "Lamiaceae",
    "Mahonia": "Berberidaceae", "Petroselinum": "Apiaceae", "Passiflora": "Passifloraceae",
    "Pelargonium": "Geraniaceae", "Asclepias": "Apocynaceae", "Prunus": "Rosaceae",
    "Plantago": "Plantaginaceae", "Salvia": "Lamiaceae", "Serenoa": "Arecaceae",
    "Schisandra": "Schisandraceae", "Capsella": "Brassicaceae", "Eleutherococcus": "Araliaceae",
    "Scutellaria": "Lamiaceae", "Saponaria": "Caryophyllaceae", "Veronica": "Plantaginaceae",
    "Acorus": "Acoraceae", "Thymus": "Lamiaceae", "Potentilla": "Rosaceae",
    "Verbena": "Verbenaceae", "Lactuca": "Asteraceae", "Dioscorea": "Dioscoreaceae",
    "Salix": "Salicaceae", "Hamamelis": "Hamamelidaceae", "Stachys": "Lamiaceae",
    "Achillea": "Asteraceae",
}

# Nicely formatted labels for symptom slugs (default: de-slug + capitalise).
SYMPTOM_LABELS = {
    "uti": "Urinary tract infection (UTI)", "ibs": "Irritable bowel syndrome (IBS)",
    "ibd": "Inflammatory bowel disease (IBD)", "pms": "Premenstrual syndrome (PMS)",
    "hot-flashes": "Hot flashes", "high-cholesterol": "High cholesterol",
    "high-blood-pressure": "High blood pressure", "blood-sugar": "Blood-sugar support",
    "liver-support": "Liver support", "immune-support": "Immune support",
    "kidney-support": "Kidney support", "prostate-support": "Prostate support",
    "lactation-support": "Lactation support", "pregnancy-support": "Pregnancy support",
    "nervous-tension": "Nervous tension", "muscle-soreness": "Muscle soreness",
    "muscle-spasm": "Muscle spasm", "cognitive-function": "Cognitive function",
    "eye-strain": "Eye strain", "acid-reflux": "Acid reflux", "bad-breath": "Bad breath",
    "heavy-bleeding": "Heavy menstrual bleeding", "appetite-loss": "Appetite loss",
    "varicose-veins": "Varicose veins", "back-pain": "Back pain",
    "skin-irritation": "Skin irritation", "menstrual-cramps": "Menstrual cramps",
    "sore-throat": "Sore throat",
}


def sym_label(slug):
    if slug in SYMPTOM_LABELS:
        return SYMPTOM_LABELS[slug]
    s = slug.replace("-", " ")
    return s[0].upper() + s[1:]


# --------------------------------------------------------------------------- #
# Text + reference helpers
# --------------------------------------------------------------------------- #
def norm_ws(s):
    s = s.replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def ascii_fold(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def clean_text(s):
    for k, v in {"u2018": "'", "u2019": "'", "u201c": '"', "u201d": '"',
                 "u2013": "-", "u2014": "-", "‘": "'", "’": "'",
                 "“": '"', "”": '"', "–": "-", "—": "-"}.items():
        s = s.replace(k, v)
    return s


def filename_for(sci):
    s = ascii_fold(sci).lower().replace("×", " ").replace("&", " ")
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_") + ".yaml"


STOPWORDS = {"the", "and", "for", "with", "from", "review", "study", "https", "http",
             "www", "available", "benefits", "uses", "safety", "plant", "plants",
             "identification", "guide", "complete", "common", "their", "modern"}
URL_RE = re.compile(r"https?://[^\s\]]+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s,;]+", re.IGNORECASE)
YEAR_RE = re.compile(r"\((\d{4})[a-z]?\)")
ND_RE = re.compile(r"\(n\.?\s*d\.?\)", re.IGNORECASE)


def parse_ref(raw):
    text = clean_text(norm_ws(raw))
    m = YEAR_RE.search(text)
    if m:
        year = m.group(1)
        after = text[m.end():]
    elif ND_RE.search(text):
        year = "nd"
        after = text[ND_RE.search(text).end():]
    else:
        year = "0000"
        after = text
    sm = re.match(r"[A-Za-z'][\w'-]*", text)
    surname = re.sub(r"[^a-z]", "", ascii_fold(sm.group(0)).lower()) if sm else "anon"
    pool = DOI_RE.sub(" ", URL_RE.sub(" ", after))
    kw = ""
    for w in re.findall(r"[A-Za-z]{4,}", pool):
        lw = ascii_fold(w).lower()
        if lw not in STOPWORDS:
            kw = re.sub(r"[^a-z]", "", lw)
            break
    doi = DOI_RE.search(text)
    url = URL_RE.search(text)
    typ = "misc"
    if doi or re.search(r"\b\d+\(\d+\)", text):
        typ = "article"
    elif re.search(r"\b(Press|Cape|Bloomsbury|thesis|Handbook|Modern Herbal|Routledge|Springer)\b", text):
        typ = "book"
    base = re.sub(r"[^a-z0-9]", "", surname + (year if year != "nd" else "nd") + kw) or surname
    return {"author": text.split("(")[0].strip(" .,"), "year": year, "doi": doi.group(0).rstrip(".") if doi else "",
            "url": url.group(0).rstrip(".") if url else "", "annote": text, "key": base, "type": typ}


def esc(s):
    return s.replace("{", "(").replace("}", ")").replace("\\", "/")


def render(r):
    lines = []
    if r["author"]:
        lines.append(f'  author  = {{{esc(r["author"])}}}')
    lines.append(f'  note    = {{{r["ref_id"]}}}')
    if r["year"] not in ("0000",):
        lines.append(f'  year    = {{{r["year"] if r["year"] != "nd" else "n.d."}}}')
    if r["doi"]:
        lines.append(f'  doi     = {{{r["doi"]}}}')
    if r["url"]:
        lines.append(f'  url     = {{{r["url"]}}}')
    lines.append(f'  annote  = {{{esc(r["annote"])}}}')
    return f'@{r["type"]}{{{r["key"]},\n' + ",\n".join(lines) + "\n}"


# --------------------------------------------------------------------------- #
# Bibliography state
# --------------------------------------------------------------------------- #
def load_bib():
    text = open(BIBLIO, encoding="utf-8").read()
    cut = text.find("@")
    header, body = (text[:cut], text[cut:]) if cut != -1 else (text, "")
    entries = {}
    annotes = {}
    maxid = 0
    for blk in re.split(r"(?m)^(?=@)", body):
        blk = blk.strip()
        if not blk:
            continue
        km = re.match(r"@\w+\s*\{\s*([^,\s]+)", blk)
        key = km.group(1) if km else f"~u{len(entries)}"
        entries[key] = blk
        am = re.search(r"annote\s*=\s*\{(.+?)\}\s*\n\}", blk, re.DOTALL)
        if am:
            annotes[re.sub(r"\s+", " ", am.group(1)).strip().lower()] = re.search(r"REF-(\d+)", blk).group(0) if re.search(r"REF-(\d+)", blk) else None
        for mid in re.findall(r"REF-(\d+)", blk):
            maxid = max(maxid, int(mid))
    return header, entries, annotes, maxid


def write_bib(header, entries):
    ordered = [entries[k] for k in sorted(entries, key=str.lower)]
    with open(BIBLIO, "w", encoding="utf-8") as fh:
        fh.write(header.rstrip() + "\n\n" + "\n\n".join(ordered) + "\n")


def dump_plant(rec, fname):
    with open(os.path.join(PLANTS_DIR, fname), "w", encoding="utf-8") as fh:
        yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True,
                       default_flow_style=False, width=100)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    header, entries, annotes, nextid = load_bib()
    nextid += 1
    used_keys = set(entries)

    def add_ref(raw):
        """Add a reference (dedupe by annote text); return its REF id."""
        nonlocal nextid
        r = parse_ref(raw)
        sig = re.sub(r"\s+", " ", r["annote"]).strip().lower()
        if sig in annotes and annotes[sig]:
            return annotes[sig]
        # unique key
        key = r["key"]
        n = 2
        while key in used_keys:
            key = f'{r["key"]}{n}'
            n += 1
        used_keys.add(key)
        r["key"] = key
        r["ref_id"] = f"REF-{nextid:04d}"
        nextid += 1
        entries[key] = render(r)
        annotes[sig] = r["ref_id"]
        return r["ref_id"]

    web = json.load(open(os.path.join(SRC, "website_references.json"), encoding="utf-8"))

    # Parse each page's reference list -> id map keyed for substring lookup.
    def build(page):
        ids = []
        for raw in web[page]:
            rid = add_ref(raw)
            ids.append({"annote": clean_text(raw).lower(), "id": rid})
        def ref_for(substr):
            for x in ids:
                if substr.lower() in x["annote"]:
                    return x["id"]
            raise KeyError(f"{page}: no ref matching {substr!r}")
        return ref_for, [x["id"] for x in ids]

    wn, wn_all = build("white_dead_nettle")
    pl, pl_all = build("broadleaf_plantain")
    ya, ya_all = build("yarrow")

    # Provenance refs for stub/skeletal data.
    TOOL = add_ref("Omnia Sana (n.d.) 'Symptom-to-Plant Lookup'. Interactive Tools. "
                   "Available at: https://omniasana.bio/symptom-plant-lookup/ (Accessed: 12 June 2026).")
    HB_PAGE = add_ref("Omnia Sana (n.d.) 'Holy Basil'. Materia Medica. "
                      "Available at: https://omniasana.bio/holy-basil/ (Accessed: 12 June 2026).")

    created, enriched, skipped = [], [], []

    # ----- New plant: White Dead Nettle (Lamium album) ----------------------
    rec = {
        "common_names": ["White Dead Nettle", "White dead-nettle", "Bee nettle", "Dumb nettle"],
        "scientific_name": "Lamium album",
        "family": "Lamiaceae",
        "parts_used": [
            {"name": "Flower", "medicinal_actions": [
                {"action": "Astringent (catarrh, excessive menstrual or vaginal discharge)",
                 "reference_ids": [wn("Grieve"), wn("Herbal Reality")], "status": "verified"},
                {"action": "Expectorant",
                 "reference_ids": [wn("Grieve"), wn("Ask-Ayurveda")], "status": "verified"},
                {"action": "Anti-inflammatory",
                 "reference_ids": [wn("Damtoft"), wn("Pietrzak")], "status": "verified"},
                {"action": "Antioxidant",
                 "reference_ids": [wn("Budzianowski"), wn("Damtoft")], "status": "verified"},
            ]},
            {"name": "Leaf", "medicinal_actions": [
                {"action": "Vulnerary (minor wounds), applied topically",
                 "reference_ids": [wn("Grieve"), wn("Herbal Reality")], "status": "verified"},
                {"action": "Edible spring potherb (young leaves and shoots, cooked)",
                 "reference_ids": [wn("Francis-Baker"), wn("Wildlife Trusts")], "status": "verified"},
            ]},
            {"name": "Aerial parts", "medicinal_actions": [
                {"action": "Astringent and anti-inflammatory infusion or tincture (flowering tops)",
                 "reference_ids": [wn("Grieve"), wn("Pietrzak"), wn("Herbal Reality")], "status": "verified"},
            ]},
        ],
        "constituents": [
            {"name": "Phenylpropanoid and flavonoid glycosides",
             "note": "Verbascoside, tiliroside and quercetin/kaempferol 3-O-glucosides in the flowers.",
             "reference_ids": [wn("Budzianowski")]},
            {"name": "Iridoid glycosides",
             "note": "Lamalbid, alboside A and B and caryoptoside; linked to antioxidant and anti-inflammatory activity.",
             "reference_ids": [wn("Damtoft")]},
            {"name": "Standardisation markers (Lamii albi flos)",
             "note": "Lamalbid, chlorogenic acid, verbascoside, rutin and tiliroside, richest in the flowering tops.",
             "reference_ids": [wn("Pietrzak")]},
        ],
        "contraindications": [
            {"note": "Generally regarded as safe in culinary amounts and at normal medicinal doses; unlike the stinging nettle it has no stinging hairs.",
             "reference_ids": [wn("Wildlife Trusts")], "status": "verified"},
            {"note": "Medicinal use during pregnancy or breastfeeding should be approached cautiously, as for any traditional astringent.",
             "reference_ids": [wn("Grieve"), wn("Francis-Baker")], "status": "verified"},
            {"note": "Identify correctly before foraging (resembles stinging nettle before flowering and red dead-nettle); clinical evidence is limited, so it should not replace conventional treatment.",
             "reference_ids": [wn("First Nature"), wn("Herbal Reality")], "status": "verified"},
        ],
        "internal_notes": ("Ingested from the omniasana.bio Materia Medica page "
                           "(https://omniasana.bio/white-dead-nettle-lamium-album/). New species not in the "
                           "book manuscript. Identification, distribution and collection notes from the source "
                           "are retained in the bibliography (some references are cited at plant level)."),
        "last_updated": LAST_UPDATED,
        "status": "verified",
    }
    # ensure every WN reference is represented (attach leftovers to a cultural note)
    used = {rid for part in rec["parts_used"] for a in part["medicinal_actions"] for rid in a["reference_ids"]}
    used |= {rid for c in rec["constituents"] for rid in c["reference_ids"]}
    used |= {rid for c in rec["contraindications"] for rid in c["reference_ids"]}
    leftover = [r for r in wn_all if r not in used]
    if leftover:
        rec["contraindications"].append(
            {"note": "Identification, distribution and horticultural references for Lamium album.",
             "reference_ids": leftover, "status": "verified"})
    dump_plant(rec, "lamium_album.yaml")
    created.append("lamium_album.yaml")

    # ----- Enrich existing: Plantago major & Achillea millefolium -----------
    enrich_plantain(pl, pl_all)
    enrich_yarrow(ya, ya_all)
    enriched += ["plantago_major.yaml", "achillea_millefolium.yaml"]

    # ----- Symptom-to-Plant Lookup tool: 77 skeletal records ----------------
    data = json.load(open(os.path.join(SRC, "symptom_lookup.json"), encoding="utf-8"))
    # filenames already present in the DB (do not overwrite book/enriched plants)
    existing_files = set(os.listdir(PLANTS_DIR))
    for p in data:
        sci = norm_ws(p["l"])
        fname = filename_for(sci)
        genus = sci.split()[0]
        family = GENUS_FAMILY.get(genus, "Unknown (needs-review)")
        # common names: split parentheticals
        names = []
        base = re.sub(r"\(([^)]*)\)", r" \1 ", p["n"])
        for token in re.split(r"\s*\(|\)\s*", p["n"]):
            t = token.strip(" ()")
            if t:
                names.append(t)
        if not names:
            names = [p["n"]]
        # symptom-derived actions, highest evidence first
        acts = []
        for slug, score in sorted(p["s"].items(), key=lambda kv: (-kv[1], kv[0])):
            acts.append({
                "action": f"{sym_label(slug)} (symptom-lookup evidence {score}/4)",
                "reference_ids": [TOOL],
                "status": "draft" if score >= 3 else "needs-review",
            })
        rec = {
            "common_names": names,
            "scientific_name": sci,
            "family": family,
            "parts_used": [{"name": "Whole plant", "medicinal_actions": acts}],
            "constituents": [],
            "contraindications": [],
            "internal_notes": ("Imported from the omniasana.bio Symptom-to-Plant Lookup tool "
                               "(https://omniasana.bio/symptom-plant-lookup/). Symptom associations only; the "
                               "evidence score (1-4) is the tool's indicative strength-of-evidence rating, not an "
                               "independent verification. No parts, constituents or contraindications were given by "
                               "the source - manual enrichment pending."),
            "last_updated": LAST_UPDATED,
            "status": "needs-review",
        }
        # Holy Basil also has a Materia Medica stub -> fold in its note + source.
        if sci.lower().startswith("ocimum"):
            rec["common_names"] = ["Holy Basil", "Tulsi"]
            rec["parts_used"][0]["name"] = "Leaf"
            rec["parts_used"][0]["medicinal_actions"].append(
                {"action": "Adaptogen (calm, clear mind; balanced response to everyday stress) - traditional use",
                 "reference_ids": [HB_PAGE, TOOL], "status": "needs-review"})
            rec["contraindications"].append(
                {"note": "Most often taken as a daily tea; speak with a practitioner if pregnant or managing blood sugar.",
                 "reference_ids": [HB_PAGE], "status": "needs-review"})
            rec["internal_notes"] = ("Combined from the omniasana.bio Symptom-to-Plant Lookup tool and the Holy "
                                     "Basil Materia Medica page (https://omniasana.bio/holy-basil/). Ocimum "
                                     "tenuiflorum (accepted) = Ocimum sanctum (synonym). Skeletal record - manual "
                                     "enrichment pending.")
        if fname in existing_files and fname not in created:
            # Should not happen (all 77 are new species), but never clobber.
            skipped.append(fname)
            continue
        dump_plant(rec, fname)
        created.append(fname)

    write_bib(header, entries)

    print(f"New bibliography size : {len([k for k in entries])} entries")
    print(f"Highest REF id now    : REF-{nextid-1:04d}")
    print(f"Plant files created   : {len(created)}")
    print(f"Plant files enriched  : {len(set(enriched))} ({', '.join(sorted(set(enriched)))})")
    if skipped:
        print(f"Skipped (would clobber): {skipped}")


# --------------------------------------------------------------------------- #
# Enrichment of existing records (additive, idempotent)
# --------------------------------------------------------------------------- #
def _load(fname):
    return yaml.safe_load(open(os.path.join(PLANTS_DIR, fname), encoding="utf-8"))


def _add_actions(rec, new_actions):
    """Append actions whose name is not already present (case-insensitive)."""
    group = rec["parts_used"][0]
    have = {a["action"].split(" (")[0].strip().lower() for a in group["medicinal_actions"]}
    for a in new_actions:
        if a["action"].split(" (")[0].strip().lower() not in have:
            group["medicinal_actions"].append(a)
            have.add(a["action"].split(" (")[0].strip().lower())


def _add_constituents(rec, cons):
    have = {c["name"].strip().lower() for c in rec.get("constituents", [])}
    rec.setdefault("constituents", [])
    for c in cons:
        if c["name"].strip().lower() not in have:
            rec["constituents"].append(c)
            have.add(c["name"].strip().lower())


def _add_contra(rec, contra):
    have = {c["note"].strip().lower()[:50] for c in rec.get("contraindications", [])}
    rec.setdefault("contraindications", [])
    for c in contra:
        if c["note"].strip().lower()[:50] not in have:
            rec["contraindications"].append(c)
            have.add(c["note"].strip().lower()[:50])


def enrich_plantain(ref_for, all_ids):
    rec = _load("plantago_major.yaml")
    _add_constituents(rec, [
        {"name": "Iridoid glycosides (aucubin, catalpol)",
         "note": "Characteristic iridoids of Plantago major.",
         "reference_ids": [ref_for("Samuelsen"), ref_for("Adom")]},
        {"name": "Caffeic acid esters (plantamajoside, acteoside/verbascoside)",
         "note": "Polyphenolic esters contributing to antioxidant and anti-inflammatory activity.",
         "reference_ids": [ref_for("Samuelsen"), ref_for("Adom")]},
        {"name": "Flavonoids (baicalein, luteolin, hispidulin)",
         "note": "Flavonoid constituents of the leaf.", "reference_ids": [ref_for("Adom")]},
        {"name": "Allantoin", "note": "Cell-proliferative compound supporting wound healing.",
         "reference_ids": [ref_for("Samuelsen")]},
        {"name": "Mucilage and triterpenes (ursolic and oleanolic acid)",
         "note": "Demulcent mucilage plus anti-inflammatory triterpenes.",
         "reference_ids": [ref_for("Samuelsen"), ref_for("Adom")]},
    ])
    _add_actions(rec, [
        {"action": "Vulnerary (wound healing) - fresh leaf poultice",
         "reference_ids": [ref_for("scratch assay"), ref_for("Samuelsen"), ref_for("Herbal Reality")], "status": "verified"},
        {"action": "Demulcent / expectorant (coughs, catarrh, irritated airways)",
         "reference_ids": [ref_for("Herbal Reality"), ref_for("Grieve")], "status": "verified"},
        {"action": "Astringent (diarrhoea)",
         "reference_ids": [ref_for("Herbal Reality"), ref_for("Grieve")], "status": "verified"},
        {"action": "Antimicrobial",
         "reference_ids": [ref_for("Adom")], "status": "verified"},
        {"action": "Antioxidant",
         "reference_ids": [ref_for("Adom")], "status": "verified"},
        {"action": "Anti-inflammatory",
         "reference_ids": [ref_for("Doctoral thesis"), ref_for("Samuelsen")], "status": "verified"},
        {"action": "Bulk laxative (mucilaginous seeds)",
         "reference_ids": [ref_for("Herbal Reality")], "status": "verified"},
    ])
    _add_contra(rec, [
        {"note": "Generally regarded as safe as food and in customary medicinal use; allergic reactions are uncommon, though the abundant wind-borne pollen can aggravate hay fever in sensitive people.",
         "reference_ids": [ref_for("Samuelsen"), ref_for("Herbal Reality")], "status": "verified"},
        {"note": "Correct identification is essential and material should be gathered away from roadsides, sprayed lawns and other contaminated ground; deep or infected wounds warrant proper medical care.",
         "reference_ids": [ref_for("Herbal Medic"), ref_for("Samuelsen")], "status": "verified"},
    ])
    leftover = [r for r in all_ids if r not in _used_ids(rec)]
    if leftover:
        rec["contraindications"].append(
            {"note": "Additional omniasana.bio sources cited for Plantago major (identification, distribution, foraging, traditional use and supporting evidence; see bibliography).",
             "reference_ids": leftover, "status": "verified"})
    rec["internal_notes"] = (rec.get("internal_notes", "").rstrip() +
        " | Enriched 2026-06-12 from the omniasana.bio 'Broadleaf Plantain' Materia Medica page "
        "(https://omniasana.bio/broadleaf-plantain-plantago-major/): added constituents, web-sourced actions "
        "and cautions.").strip(" |")
    rec["last_updated"] = LAST_UPDATED
    dump_plant(rec, "plantago_major.yaml")


def enrich_yarrow(ref_for, all_ids):
    rec = _load("achillea_millefolium.yaml")
    _add_constituents(rec, [
        {"name": "Essential oil (mono- and sesquiterpenes)",
         "note": "Chamazulene (blue colour), sabinene, 1,8-cineole, camphor and alpha-bisabolol.",
         "reference_ids": [ref_for("Ali")]},
        {"name": "Flavonoids (apigenin, luteolin, rutin, quercetin)",
         "note": "Antioxidant and antispasmodic flavonoids.", "reference_ids": [ref_for("Ali")]},
        {"name": "Sesquiterpene lactones, phenolic acids, tannins and coumarins",
         "note": "Contribute to anti-inflammatory and astringent activity.", "reference_ids": [ref_for("Ali")]},
        {"name": "Betonicine and achilleine",
         "note": "Compounds traditionally linked to the haemostatic (styptic) effect.",
         "reference_ids": [ref_for("Ali")]},
    ])
    _add_actions(rec, [
        {"action": "Styptic / haemostatic (slows bleeding from minor cuts)",
         "reference_ids": [ref_for("Ali"), ref_for("Herbal Reality"), ref_for("Sacred Plant")], "status": "verified"},
        {"action": "Vulnerary (wound healing)",
         "reference_ids": [ref_for("Hemmati"), ref_for("Ali")], "status": "verified"},
        {"action": "Diaphoretic (supports the body during colds and fevers)",
         "reference_ids": [ref_for("Ali"), ref_for("Herbal Reality")], "status": "verified"},
        {"action": "Antispasmodic (primary dysmenorrhea / menstrual cramps)",
         "reference_ids": [ref_for("Jenabi"), ref_for("Ali")], "status": "verified"},
        {"action": "Bitter digestive tonic (stimulates appetite and bile flow)",
         "reference_ids": [ref_for("Ali"), ref_for("Herbal Reality")], "status": "verified"},
        {"action": "Astringent",
         "reference_ids": [ref_for("Ali"), ref_for("Herbal Reality")], "status": "verified"},
    ])
    _add_contra(rec, [
        {"note": "As a member of the daisy family (Asteraceae) it can cause allergic reactions or contact dermatitis in sensitive people, and handling the fresh plant in sunlight can occasionally cause photosensitivity.",
         "reference_ids": [ref_for("Ali")], "status": "verified"},
        {"note": "Medicinal use is traditionally avoided in pregnancy (can stimulate the uterus and influence menstruation); caution while breastfeeding.",
         "reference_ids": [ref_for("Herbal Reality")], "status": "verified"},
        {"note": "May interact with anticoagulant, sedative and blood-pressure medications and with drugs metabolised by the liver; seek professional advice if on regular medication.",
         "reference_ids": [ref_for("Ali")], "status": "verified"},
        {"note": "Correct identification is essential, as several poisonous white-flowered umbellifers can be confused with yarrow; clinical evidence in humans is limited.",
         "reference_ids": [ref_for("First Nature"), ref_for("Ali")], "status": "verified"},
    ])
    leftover = [r for r in all_ids if r not in _used_ids(rec)]
    if leftover:
        rec["contraindications"].append(
            {"note": "Additional omniasana.bio sources cited for Achillea millefolium (identification, distribution, foraging, traditional use and supporting evidence; see bibliography).",
             "reference_ids": leftover, "status": "verified"})
    rec["internal_notes"] = (rec.get("internal_notes", "").rstrip() +
        " | Enriched 2026-06-12 from the omniasana.bio 'Yarrow' Materia Medica page "
        "(https://omniasana.bio/yarrow-achillea-millefolium/): added constituents, web-sourced actions and "
        "cautions.").strip(" |")
    rec["last_updated"] = LAST_UPDATED
    dump_plant(rec, "achillea_millefolium.yaml")


def _used_ids(rec):
    ids = set()
    for part in rec["parts_used"]:
        for a in part["medicinal_actions"]:
            ids |= set(a.get("reference_ids", []))
    for c in rec.get("constituents", []):
        ids |= set(c.get("reference_ids", []))
    for c in rec.get("contraindications", []):
        ids |= set(c.get("reference_ids", []))
    return ids


if __name__ == "__main__":
    main()
