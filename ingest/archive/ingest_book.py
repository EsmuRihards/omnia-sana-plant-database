#!/usr/bin/env python3
"""
ingest_book.py — one-shot ingestion of the Omnia Sana book manuscript into the
plant database.

It reads the .docx manuscript, parses the "References & Citations" section into
BibTeX entries (each tagged with a REF-XXXX id), maps every reference to the
plant(s) it is "[Cited in:]", and emits one YAML record per plant in plants/.

This is provenance: re-running it regenerates the book-derived records. The
Dandelion record (taraxacum_officinale.yaml) is curated separately from the
omniasana.bio Materia Medica post and is NOT overwritten by this script.

Usage:
    python tools/ingest_book.py [path-to-docx]
"""

import os
import re
import sys
import unicodedata

import docx
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PLANTS_DIR = os.path.join(ROOT, "plants")
BIBLIO = os.path.join(ROOT, "bibliography.bibtex")

DEFAULT_DOCX = os.path.join(
    os.path.dirname(ROOT), "book", "Koffetablbok_with_additions.docx"
)

LAST_UPDATED = "2026-06-12"

# Plants curated from other sources — do not generate/overwrite from the book.
SKIP_PLANTS = {"Dandelion"}

# Genus -> botanical family. Covers every genus in the manuscript. Families use
# modern (APG) circumscription; fungi use their mycological family.
GENUS_FAMILY = {
    "Trachyspermum": "Apiaceae", "Aloe": "Asphodelaceae", "Pimpinella": "Apiaceae",
    "Withania": "Solanaceae", "Laurus": "Lauraceae", "Betula": "Betulaceae",
    "Nigella": "Ranunculaceae", "Ribes": "Grossulariaceae", "Eucalyptus": "Myrtaceae",
    "Borago": "Boraginaceae", "Thymus": "Lamiaceae", "Theobroma": "Malvaceae",
    "Carum": "Apiaceae", "Elettaria": "Zingiberaceae", "Nepeta": "Lamiaceae",
    "Inonotus": "Hymenochaetaceae", "Matricaria": "Asteraceae", "Salvia": "Lamiaceae",
    "Stellaria": "Caryophyllaceae", "Capsicum": "Solanaceae", "Galium": "Rubiaceae",
    "Syzygium": "Myrtaceae", "Coffea": "Rubiaceae", "Tussilago": "Asteraceae",
    "Symphytum": "Boraginaceae", "Juniperus": "Cupressaceae", "Rumex": "Polygonaceae",
    "Cordyceps": "Cordycipitaceae", "Coriandrum": "Apiaceae", "Primula": "Primulaceae",
    "Oxycoccus": "Ericaceae", "Vaccinium": "Ericaceae", "Cuminum": "Apiaceae",
    "Taraxacum": "Asteraceae", "Anethum": "Apiaceae", "Rosa": "Rosaceae",
    "Sambucus": "Adoxaceae", "Foeniculum": "Apiaceae", "Trigonella": "Fabaceae",
    "Equisetum": "Equisetaceae", "Chamerion": "Onagraceae", "Epilobium": "Onagraceae",
    "Linum": "Linaceae", "Allium": "Amaryllidaceae", "Zingiber": "Zingiberaceae",
    "Ginkgo": "Ginkgoaceae", "Solidago": "Asteraceae", "Verbascum": "Scrophulariaceae",
    "Arctium": "Asteraceae", "Plantago": "Plantaginaceae", "Aegopodium": "Apiaceae",
    "Paullinia": "Sapindaceae", "Crataegus": "Rosaceae", "Cannabis": "Cannabaceae",
    "Humulus": "Cannabaceae", "Hyssopus": "Lamiaceae", "Reynoutria": "Polygonaceae",
    "Rhododendron": "Ericaceae", "Alchemilla": "Rosaceae", "Lavandula": "Lamiaceae",
    "Melissa": "Lamiaceae", "Glycyrrhiza": "Fabaceae", "Ganoderma": "Ganodermataceae",
    "Hericium": "Hericiaceae", "Origanum": "Lamiaceae", "Filipendula": "Rosaceae",
    "Leonurus": "Lamiaceae", "Artemisia": "Asteraceae", "Morinda": "Rubiaceae",
    "Olea": "Oleaceae", "Pleurotus": "Pleurotaceae", "Panax": "Araliaceae",
    "Mentha": "Lamiaceae", "Hypericum": "Hypericaceae", "Calendula": "Asteraceae",
    "Psilocybe": "Hymenogastraceae", "Echinacea": "Asteraceae", "Trifolium": "Fabaceae",
    "Rhodiola": "Crassulaceae", "Crocus": "Iridaceae", "Pinus": "Pinaceae",
    "Hippophae": "Elaeagnaceae", "Prunella": "Lamiaceae", "Lentinula": "Omphalotaceae",
    "Urtica": "Urticaceae", "Tanacetum": "Asteraceae", "Camellia": "Theaceae",
    "Cinnamomum": "Lauraceae", "Curcuma": "Zingiberaceae", "Trametes": "Polyporaceae",
    "Valeriana": "Caprifoliaceae", "Bacopa": "Plantaginaceae",
}

# Scientific-name overrides for messy / multi-species headers.
SCINAME_OVERRIDE = {
    "Coffee (Arabica & Robusta)": "Coffea arabica",
    "Purple coneflower": "Echinacea purpurea",
    "Peppermint": "Mentha × piperita",
    "Chili Pepper": "Capsicum annuum",
}


# --------------------------------------------------------------------------- #
# Text helpers
# --------------------------------------------------------------------------- #
def norm_ws(s):
    """Normalise unicode whitespace and odd control chars to plain spaces."""
    s = s.replace("\xa0", " ").replace("​", "")
    s = "".join(" " if unicodedata.category(c) == "Zs" else c for c in s)
    return re.sub(r"\s+", " ", s).strip()


def ascii_fold(s):
    return "".join(
        c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)
    )


def clean_binomial(heading, raw_sci):
    """Return a clean 'Genus species' (keeping a hybrid x marker if present)."""
    if heading in SCINAME_OVERRIDE:
        return SCINAME_OVERRIDE[heading]
    s = norm_ws(raw_sci)
    # Take the leading binomial, dropping trailing authorship.
    toks = s.split()
    if not toks:
        return s
    genus = toks[0]
    genus = genus[0].upper() + genus[1:]
    rest = toks[1:]
    # hybrid marker
    hybrid = ""
    if rest and rest[0] in ("×", "x", "X"):
        hybrid = "× "
        rest = rest[1:]
    species = ""
    for t in rest:
        if re.fullmatch(r"[A-Za-z][A-Za-z-]+", t):
            species = t.lower()
            break
    return f"{genus} {hybrid}{species}".strip()


def filename_for(sciname):
    s = ascii_fold(sciname).lower()
    s = s.replace("×", " ").replace("&", " ")
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_") + ".yaml"


def genus_of(sciname):
    return sciname.split()[0] if sciname else ""


# --------------------------------------------------------------------------- #
# Reference parsing
# --------------------------------------------------------------------------- #
CITED_RE = re.compile(r"\[Cited in:\s*([^\]]+)\]", re.IGNORECASE)
YEAR_PAREN_RE = re.compile(r"\((\d{4})[a-z]?\)")
YEAR_ND_RE = re.compile(r"\(n\.?\s*d\.?\)", re.IGNORECASE)
YEAR_BARE_RE = re.compile(r"\b(1[89]\d{2}|20\d{2})\b")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s,;]+", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s\]]+")
STOPWORDS = {
    "the", "and", "for", "with", "from", "review", "study", "effects", "effect",
    "potential", "health", "benefits", "analysis", "their", "into", "some", "new",
    "evaluation", "comparison", "randomized", "clinical", "trial", "trials",
    "https", "http", "www", "available", "org", "com", "html", "ncbi", "pmc",
    "doi", "article", "articles", "journal",
}


def parse_year(text):
    m = YEAR_PAREN_RE.search(text)
    if m:
        return m.group(1)
    if YEAR_ND_RE.search(text):
        return "nd"
    m = YEAR_BARE_RE.search(text)
    if m:
        return m.group(1)
    return "0000"


def first_surname(text):
    m = re.search(r"[A-Za-zÀ-ɏ]+", text)
    word = ascii_fold(m.group(0)).lower() if m else "anon"
    return re.sub(r"[^a-z]", "", word) or "anon"


def title_keyword(text, year):
    """A short distinguishing word for the citation key (usually a title word)."""
    # Prefer a quoted title (Harvard style: 'Title ...').
    qm = re.search(r"[‘'“\"]([^’'”\"]{4,})[’'”\"]", text)
    if qm:
        pool = qm.group(1)
    else:
        # The title normally follows the (year) / (n.d.) marker — look there so
        # org-authored refs key on the topic, not the organisation name.
        m = re.search(r"\((?:\d{4}[a-z]?|n\.?\s*d\.?)\)", text, re.IGNORECASE)
        pool = text[m.end():] if m else text
    # Never pull a keyword out of a URL or DOI fragment.
    pool = URL_RE.sub(" ", pool)
    pool = DOI_RE.sub(" ", pool)
    for w in re.findall(r"[A-Za-zÀ-ɏ]{4,}", pool):
        lw = ascii_fold(w).lower()
        if lw not in STOPWORDS:
            return re.sub(r"[^a-z]", "", lw)
    return ""


def entry_type(text):
    if DOI_RE.search(text) or re.search(r"\b\d+\(\d+\)", text):
        return "article"
    if re.search(r"\b(Press|edn\b|\bed\.\)|Handbook|Encyclop|Pharmacopoeia|"
                 r"Publishing|Routledge|Springer|CRC|Wiley)\b", text):
        return "book"
    return "misc"


def bibtex_escape(s):
    return s.replace("{", "(").replace("}", ")").replace("\\", "/")


def parse_references(ref_paras):
    """Return list of dicts with parsed reference data (no REF ids yet)."""
    refs = []
    for raw in ref_paras:
        text = norm_ws(raw)
        plants = []
        cm = CITED_RE.search(text)
        if cm:
            plants = [p.strip() for p in cm.group(1).split(",") if p.strip()]
            text = CITED_RE.sub("", text).strip()
        # strip leading Vancouver number "12. "
        text = re.sub(r"^\d+\.\s+", "", text).strip()
        if not text:
            continue
        year = parse_year(text)
        surname = first_surname(text)
        kw = title_keyword(text, year)
        key = surname + (year if year != "nd" else "nd") + kw
        doi = DOI_RE.search(text)
        url = URL_RE.search(text)
        refs.append({
            "raw": text,
            "plants": plants,
            "year": year,
            "key": re.sub(r"[^A-Za-z0-9]", "", key) or surname,
            "type": entry_type(text),
            "doi": doi.group(0).rstrip(".") if doi else "",
            "url": url.group(0).rstrip(".") if url else "",
        })
    return refs


def assign_keys_and_ids(refs):
    """Sanitise + dedupe citation keys, sort alphabetically, assign REF ids."""
    # Keys must be alphanumeric only (BibTeX-safe); never let braces etc. in.
    for r in refs:
        r["key"] = re.sub(r"[^A-Za-z0-9]", "", r["key"]) or "ref"
    # Dedupe with numeric suffixes (base, base2, base3, ...), guaranteed unique.
    used = set()
    counts = {}
    for r in refs:
        base = r["key"]
        n = counts.get(base, 0) + 1
        counts[base] = n
        key = base if n == 1 else f"{base}{n}"
        while key in used:
            key += "x"
        used.add(key)
        r["key"] = key
    refs.sort(key=lambda r: r["key"].lower())
    for i, r in enumerate(refs, start=1):
        r["ref_id"] = f"REF-{i:04d}"
    assert len({r["key"] for r in refs}) == len(refs), "duplicate citation keys"
    return refs


def render_bibtex(refs):
    out = []
    for r in refs:
        author = r["raw"].split("(")[0].strip(" .,")
        if r["year"] not in ("0000", "nd"):
            # crude title: text right after the year marker, first sentence
            after = r["raw"].split(r["year"], 1)
            title = ""
            if len(after) == 2:
                t = after[1].lstrip(") '‘’“”.,")
                title = re.split(r"['’”\"]|\.\s", t)[0].strip()
            else:
                title = ""
        else:
            title = ""
        fields = [f'  note    = {{{r["ref_id"]}}}']
        if author:
            fields.insert(0, f'  author  = {{{bibtex_escape(author)}}}')
        if title:
            fields.insert(1, f'  title   = {{{bibtex_escape(title)}}}')
        yr = r["year"]
        if yr not in ("0000",):
            fields.append(f'  year    = {{{yr if yr != "nd" else "n.d."}}}')
        if r["doi"]:
            fields.append(f'  doi     = {{{r["doi"]}}}')
        if r["url"]:
            fields.append(f'  url     = {{{r["url"]}}}')
        # Always preserve the full original citation verbatim.
        fields.append(f'  annote  = {{{bibtex_escape(r["raw"])}}}')
        body = ",\n".join(fields)
        out.append(f'@{r["type"]}{{{r["key"]},\n{body}\n}}')
    return out


# --------------------------------------------------------------------------- #
# Plant block parsing
# --------------------------------------------------------------------------- #
FIELD_RE = re.compile(r"^([A-Z][A-Za-z /']+?):\s*(.*)$")
SECTION_HEADERS = {
    "summary", "distribution", "notes", "cultural notes", "safety notes",
    "related entries", "preparation methods",
}


def split_list(value):
    parts = re.split(r"[;,]", value)
    return [norm_ws(p) for p in parts if norm_ws(p)]


def parse_plant_block(heading, block_paras):
    """block_paras: list of (style, text). Returns a record dict + plant key."""
    lines = [(s, norm_ws(t)) for s, t in block_paras if norm_ws(t)]
    sci_raw = lines[0][1] if lines else ""
    sciname = clean_binomial(heading, sci_raw)

    fields = {}     # field label (lower) -> value string
    # Collect simple "Label: value" header fields and section bodies.
    current_section = None
    sections = {}   # section name -> list of paragraph texts
    for idx, (style, text) in enumerate(lines):
        if idx == 0:
            continue  # scientific name line
        m = FIELD_RE.match(text)
        label = m.group(1).strip().lower() if m else None
        if label in SECTION_HEADERS or (label and label.endswith("notes")):
            current_section = label
            sections.setdefault(current_section, [])
            tail = m.group(2).strip()
            if tail:
                sections[current_section].append(tail)
            continue
        if m and m.group(2) is not None and current_section is None:
            fields[label] = m.group(2).strip()
            continue
        if current_section:
            sections.setdefault(current_section, []).append(text)

    common = []
    if "common names" in fields:
        for c in split_list(fields["common names"]):
            c = re.sub(r"\([^)]*\)", "", c).strip(" .;")
            if c:
                common.append(c)
    # Always include the chapter heading as a common name (first).
    heading_clean = norm_ws(heading)
    names = [heading_clean] + [c for c in common if c.lower() != heading_clean.lower()]
    # de-dup preserving order
    seen = set()
    common_names = []
    for n in names:
        if n.lower() not in seen:
            seen.add(n.lower())
            common_names.append(n)

    parts = split_list(fields.get("parts used", "")) or ["Whole plant"]
    actions = split_list(fields.get("medicinal actions", ""))

    family = GENUS_FAMILY.get(genus_of(sciname), "")

    return {
        "heading": heading_clean,
        "sciname": sciname,
        "family": family,
        "parts": parts,
        "actions": actions,
        "safety": sections.get("safety notes", []),
        "fields": fields,
    }


def build_record(parsed, ref_ids, status="verified"):
    parts = parsed["parts"]
    part_name = parts[0] if len(parts) == 1 else " / ".join(parts)
    actions = parsed["actions"]

    med_actions = []
    for a in actions:
        med_actions.append({
            "action": a,
            "reference_ids": list(ref_ids),
            "status": status,
        })

    parts_used = [{"name": part_name, "medicinal_actions": med_actions}]

    contraindications = []
    for note in parsed["safety"]:
        note = note.strip()
        if not note:
            continue
        contraindications.append({
            "note": note,
            "reference_ids": list(ref_ids),
            "status": status,
        })

    rec = {
        "common_names": parsed["common_names"],
        "scientific_name": parsed["sciname"],
        "family": parsed["family"] or "Unknown (needs-review)",
        "parts_used": parts_used,
        "constituents": [],
        "contraindications": contraindications,
        "internal_notes": (
            "Bulk-ingested from the Omnia Sana book manuscript "
            "(Koffetablbok_with_additions.docx). reference_ids are plant-level: "
            "the book lists parts and actions as flat, unmapped lists, so the "
            "full set of references cited for this plant is attached to each "
            "action rather than split per action. constituents not yet "
            "extracted — manual enrichment pending."
        ),
        "last_updated": LAST_UPDATED,
        "status": status,
    }
    return rec


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    docx_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DOCX
    doc = docx.Document(docx_path)
    paras = [(p.style.name, p.text) for p in doc.paragraphs]
    h_idx = [i for i, (s, t) in enumerate(paras) if s == "Heading 1" and t.strip()]
    headings = [paras[i][1].strip() for i in h_idx]

    ref_start = next(i for i, n in zip(h_idx, headings) if n.startswith("References"))
    ref_paras = [t for s, t in paras[ref_start + 1:] if t.strip()]
    # drop the intro sentence under the References heading
    ref_paras = [r for r in ref_paras if not r.lower().startswith("the following is")]

    refs = parse_references(ref_paras)
    refs = assign_keys_and_ids(refs)

    # plant heading -> set of REF ids
    plant_refs = {}
    for r in refs:
        for pl in r["plants"]:
            plant_refs.setdefault(pl, set()).add(r["ref_id"])

    # Write bibliography (preserve existing header up to the first @entry / EOF).
    header = ""
    if os.path.exists(BIBLIO):
        existing = open(BIBLIO, encoding="utf-8").read()
        cut = existing.find("@")
        header = existing[:cut] if cut != -1 else existing
    entries = render_bibtex(sorted(refs, key=lambda r: r["key"].lower()))
    with open(BIBLIO, "w", encoding="utf-8") as fh:
        fh.write(header.rstrip() + "\n\n")
        fh.write("\n\n".join(entries) + "\n")

    # Parse all plant blocks, merging any that resolve to the same file
    # (the manuscript has separate chapters for the same species — e.g.
    # "Chamomile" and "Scented Mayweed" are both Matricaria chamomilla).
    records = {}     # filename -> parsed dict (with common_names + ref_ids)
    merged = 0
    for k, i in enumerate(h_idx):
        nm = headings[k]
        if nm == "Table of Contents" or nm.startswith("References") or nm in SKIP_PLANTS:
            continue
        nexti = h_idx[k + 1] if k + 1 < len(h_idx) else len(paras)
        parsed = parse_plant_block(nm, paras[i + 1:nexti])
        parsed["common_names"] = _common_names(nm, parsed)
        parsed["ref_ids"] = sorted(plant_refs.get(nm, set()))
        fname = filename_for(parsed["sciname"])
        if fname in records:
            merge_parsed(records[fname], parsed)
            merged += 1
        else:
            records[fname] = parsed

    skipped_refs = 0
    for fname, parsed in records.items():
        if not parsed["ref_ids"]:
            skipped_refs += 1
        rec = build_record(parsed, parsed["ref_ids"])
        with open(os.path.join(PLANTS_DIR, fname), "w", encoding="utf-8") as fh:
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True,
                           default_flow_style=False, width=100)

    print(f"References parsed : {len(refs)}")
    print(f"Plant chapters    : {len(records) + merged}")
    print(f"Plant files written: {len(records)} ({merged} same-species merge)")
    print(f"Plants w/o refs   : {skipped_refs}")
    print(f"Bibliography      : {BIBLIO}")


def merge_parsed(dst, src):
    """Merge a same-species chapter into an existing parsed record."""
    def uniq_extend(base, extra):
        seen = {x.lower() for x in base}
        for x in extra:
            if x.lower() not in seen:
                seen.add(x.lower())
                base.append(x)
    uniq_extend(dst["common_names"], src["common_names"])
    uniq_extend(dst["actions"], src["actions"])
    uniq_extend(dst["parts"], src["parts"])
    uniq_extend(dst["safety"], src["safety"])
    dst["ref_ids"] = sorted(set(dst["ref_ids"]) | set(src["ref_ids"]))


def _common_names(heading, parsed):
    fields = parsed["fields"]
    common = []
    if "common names" in fields:
        for c in split_list(fields["common names"]):
            c = re.sub(r"\([^)]*\)", "", c).strip(" .;")
            if c:
                common.append(c)
    heading_clean = norm_ws(heading)
    names = [heading_clean] + [c for c in common if c.lower() != heading_clean.lower()]
    seen, out = set(), []
    for n in names:
        if n.lower() not in seen:
            seen.add(n.lower())
            out.append(n)
    return out


if __name__ == "__main__":
    main()
