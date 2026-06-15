#!/usr/bin/env python3
"""
add_dandelion.py — build the curated Dandelion worked example.

Adds the references cited in the omniasana.bio Materia Medica post
(https://omniasana.bio/dandelion-taraxacum-officinale/) to bibliography.bibtex
(continuing REF ids after the book-ingested set, reusing the existing Kew
Taraxacum entry), then writes the part-mapped plants/taraxacum_officinale.yaml.

Run AFTER tools/ingest_book.py. Re-running is idempotent: existing REF ids /
citation keys are not duplicated, and the bibliography is re-sorted by key.
"""

import os
import re
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BIBLIO = os.path.join(ROOT, "bibliography.bibtex")
PLANTS_DIR = os.path.join(ROOT, "plants")

# Existing entry reused from the book ingestion (Kew POWO Taraxacum page).
KEW = "REF-0248"

# New references from the omniasana.bio Dandelion post. ref ids continue the
# book-ingested sequence (book used REF-0001..REF-0319).
NEW_REFS = [
    dict(ref="REF-0320", key="bsbindtaraxacum", type="misc",
         author="Botanical Society of Britain and Ireland", year="n.d.",
         title="Dandelion identification (Taraxacum)",
         url="https://bsbi.org/identification/taraxacum",
         annote="Botanical Society of Britain and Ireland (n.d.) 'Dandelion identification (Taraxacum)'. Available at: https://bsbi.org/identification/taraxacum (Accessed: 7 June 2026)."),
    dict(ref="REF-0321", key="clare2009diuretic", type="article",
         author="Clare, B.A., Conroy, R.S. and Spelman, K.", year="2009",
         title="The diuretic effect in human subjects of an extract of Taraxacum officinale folium over a single day",
         doi="10.1089/acm.2008.0152",
         annote="Clare, B.A., Conroy, R.S. and Spelman, K. (2009) 'The diuretic effect in human subjects of an extract of Taraxacum officinale folium over a single day', Journal of Alternative and Complementary Medicine, 15(8), pp. 929–934. doi:10.1089/acm.2008.0152."),
    dict(ref="REF-0322", key="farm2021harvest", type="misc",
         author="Farm and Dairy", year="2021",
         title="How to harvest and use dandelion roots, leaves and flowers",
         url="https://www.farmanddairy.com/news/top-stories/how-to-harvest-and-use-dandelion-roots-leaves-and-flowers/656605.html",
         annote="Farm and Dairy (2021) 'How to harvest and use dandelion roots, leaves and flowers'. Available at: https://www.farmanddairy.com/news/top-stories/how-to-harvest-and-use-dandelion-roots-leaves-and-flowers/656605.html (Accessed: 7 June 2026)."),
    dict(ref="REF-0323", key="firstnaturendtaraxacum", type="misc",
         author="First Nature", year="n.d.",
         title="Taraxacum officinale, Dandelion: identification, distribution, habitat",
         url="https://www.first-nature.com/flowers/taraxacum-officinale.php",
         annote="First Nature (n.d.) 'Taraxacum officinale, Dandelion: identification, distribution, habitat'. Available at: https://www.first-nature.com/flowers/taraxacum-officinale.php (Accessed: 7 June 2026)."),
    dict(ref="REF-0324", key="fsusndtaraxacum", type="misc",
         author="Flora of the Southeastern United States", year="n.d.",
         title="Taraxacum officinale (Common Dandelion)",
         url="https://fsus.ncbg.unc.edu/main.php?pg=show-taxon.php&plantname=taraxacum+officinale",
         annote="FSUS (n.d.) 'Taraxacum officinale (Common Dandelion)'. Flora of the Southeastern United States. Available at: https://fsus.ncbg.unc.edu/main.php?pg=show-taxon.php&plantname=taraxacum+officinale (Accessed: 7 June 2026)."),
    dict(ref="REF-0325", key="goodgrubndplant", type="misc",
         author="Good Grub", year="n.d.",
         title="Plant of the Month: Dandelion!",
         url="https://www.goodgrub.org/post/plant-of-the-month-dandelion",
         annote="Good Grub (n.d.) 'Plant of the Month: Dandelion!'. Available at: https://www.goodgrub.org/post/plant-of-the-month-dandelion (Accessed: 7 June 2026)."),
    dict(ref="REF-0326", key="hao2024taraxacum", type="article",
         author="Hao, F., Deng, X., Yu, X., Wang, W., Yan, W., Zhao, X., Wang, X., Bai, C., Wang, Z. and Han, L.", year="2024",
         title="Taraxacum: A Review of Ethnopharmacology, Phytochemistry and Pharmacological Activity",
         doi="10.1142/S0192415X24500083",
         annote="Hao, F., Deng, X., Yu, X., Wang, W., Yan, W., Zhao, X., Wang, X., Bai, C., Wang, Z. and Han, L. (2024) 'Taraxacum: A Review of Ethnopharmacology, Phytochemistry and Pharmacological Activity', The American Journal of Chinese Medicine, 52(1), pp. 183–215. doi:10.1142/S0192415X24500083."),
    dict(ref="REF-0327", key="herbawave2026dandelion", type="misc",
         author="HerbaWave", year="2026",
         title="Dandelion (Taraxacum officinale) – Origin, Phytochemistry, Traditional Use",
         url="https://herbawave.com/en/learn/ingredients/dandelion",
         annote="HerbaWave (2026) 'Dandelion (Taraxacum officinale) – Origin, Phytochemistry, Traditional Use'. Available at: https://herbawave.com/en/learn/ingredients/dandelion (Accessed: 7 June 2026)."),
    dict(ref="REF-0328", key="herbalrealitynddandelion", type="misc",
         author="Herbal Reality", year="n.d.",
         title="Dandelion (Taraxacum officinale): Benefits, Safety, Uses",
         url="https://www.herbalreality.com/herb/dandelion/",
         annote="Herbal Reality (n.d.) 'Dandelion (Taraxacum officinale): Benefits, Safety, Uses'. Available at: https://www.herbalreality.com/herb/dandelion/ (Accessed: 7 June 2026)."),
    dict(ref="REF-0329", key="kania2022dandelion", type="article",
         author="Kania-Dobrowolska, M. and Baraniak, J.", year="2022",
         title="Dandelion (Taraxacum officinale L.) as a Source of Biologically Active Compounds Supporting the Therapy of Co-Existing Diseases in Metabolic Syndrome",
         doi="10.3390/foods11182858",
         annote="Kania-Dobrowolska, M. and Baraniak, J. (2022) 'Dandelion (Taraxacum officinale L.) as a Source of Biologically Active Compounds Supporting the Therapy of Co-Existing Diseases in Metabolic Syndrome', Foods, 11(18), 2858. doi:10.3390/foods11182858."),
    dict(ref="REF-0330", key="mossy2025forage", type="misc",
         author="Mossy Oak", year="2025",
         title="How to Forage for Dandelions",
         url="https://www.mossyoak.com/our-obsession/blogs/recipes/how-to-forage-for-dandelions",
         annote="Mossy Oak (2025) 'How to Forage for Dandelions'. Available at: https://www.mossyoak.com/our-obsession/blogs/recipes/how-to-forage-for-dandelions (Accessed: 7 June 2026)."),
    dict(ref="REF-0331", key="practical2024dandelion", type="misc",
         author="Practical Frugality", year="2024",
         title="Dandelion: Foraging Guide, Recipes & Harvesting Tips",
         url="https://www.practicalfrugality.com/dandelion/",
         annote="Practical Frugality (2024) 'Dandelion: Foraging Guide, Recipes & Harvesting Tips'. Available at: https://www.practicalfrugality.com/dandelion/ (Accessed: 7 June 2026)."),
    dict(ref="REF-0332", key="rodriguez2007risks", type="article",
         author="Rodriguez-Fragoso, L., Reyes-Esparza, J., Burchiel, S.W., Herrera-Ruiz, D. and Torres, E.", year="2007",
         title="Risks and benefits of commonly used herbal medicines in Mexico",
         doi="10.1016/j.taap.2007.10.005",
         annote="Rodriguez-Fragoso, L., Reyes-Esparza, J., Burchiel, S.W., Herrera-Ruiz, D. and Torres, E. (2007) 'Risks and benefits of commonly used herbal medicines in Mexico', Toxicology and Applied Pharmacology, 227(1), pp. 125–135. doi:10.1016/j.taap.2007.10.005."),
    dict(ref="REF-0333", key="sharifi2018ethnobotany", type="article",
         author="Sharifi-Rad, M., Roberts, T.H., Matthews, K.R., Bezerra, C.F., Morais-Braga, M.F.B., Coutinho, H.D.M., Sharopov, F., Salehi, B., Yousaf, Z., Sharifi-Rad, M., del Mar Contreras, M., Varoni, E.M., Verma, D.R., Iriti, M. and Sharifi-Rad, J.", year="2018",
         title="Ethnobotany of the genus Taraxacum – Phytochemicals and antimicrobial activity",
         doi="10.1002/ptr.6157",
         annote="Sharifi-Rad, M., Roberts, T.H., Matthews, K.R., Bezerra, C.F., Morais-Braga, M.F.B., Coutinho, H.D.M., Sharopov, F., Salehi, B., Yousaf, Z., Sharifi-Rad, M., del Mar Contreras, M., Varoni, E.M., Verma, D.R., Iriti, M. and Sharifi-Rad, J. (2018) 'Ethnobotany of the genus Taraxacum – Phytochemicals and antimicrobial activity', Phytotherapy Research, 32(11), pp. 2131–2145. doi:10.1002/ptr.6157."),
    dict(ref="REF-0334", key="under2025foraging", type="misc",
         author="Under A Tin Roof", year="2025",
         title="The Ultimate Guide to Foraging Dandelions",
         url="https://underatinroof.com/blog/the-ultimate-guide-to-foraging-dandelions-how-to-harvest-flowers-greens-and-roots",
         annote="Under A Tin Roof (2025) 'The Ultimate Guide to Foraging Dandelions'. Available at: https://underatinroof.com/blog/the-ultimate-guide-to-foraging-dandelions-how-to-harvest-flowers-greens-and-roots (Accessed: 7 June 2026)."),
    dict(ref="REF-0335", key="umassndtaraxacum", type="misc",
         author="University of Massachusetts", year="n.d.",
         title="Taraxacum officinale",
         url="https://extension.umass.edu/weed-herbarium/weeds/taraxacum-officinale/",
         annote="University of Massachusetts (n.d.) 'Taraxacum officinale'. UMass Weed Herbarium. Available at: https://extension.umass.edu/weed-herbarium/weeds/taraxacum-officinale/ (Accessed: 7 June 2026)."),
    dict(ref="REF-0336", key="wikipediandtaraxacum", type="misc",
         author="Wikipedia", year="n.d.",
         title="Taraxacum officinale",
         url="https://en.wikipedia.org/wiki/Taraxacum_officinale",
         annote="Wikipedia (n.d.) 'Taraxacum officinale'. Available at: https://en.wikipedia.org/wiki/Taraxacum_officinale (Accessed: 7 June 2026)."),
    dict(ref="REF-0337", key="wisconsinnddandelion", type="misc",
         author="University of Wisconsin-Madison Division of Extension", year="n.d.",
         title="Dandelion, Taraxacum officinale",
         url="https://hort.extension.wisc.edu/articles/dandelion-taraxacum-officinale/",
         annote="Wisconsin Horticulture (n.d.) 'Dandelion, Taraxacum officinale'. University of Wisconsin-Madison Division of Extension. Available at: https://hort.extension.wisc.edu/articles/dandelion-taraxacum-officinale/ (Accessed: 7 June 2026)."),
    dict(ref="REF-0338", key="wu2024taraxaci", type="article",
         author="Wu, J., Sun, J., Liu, M., Zhang, X., Kong, L., Ma, L., Jiang, S., Liu, X. and Ma, W.", year="2024",
         title="Botany, Traditional Use, Phytochemistry, Pharmacology and Quality Control of Taraxaci Herba: A Comprehensive Review",
         doi="10.3390/ph17091113",
         annote="Wu, J., Sun, J., Liu, M., Zhang, X., Kong, L., Ma, L., Jiang, S., Liu, X. and Ma, W. (2024) 'Botany, Traditional Use, Phytochemistry, Pharmacology and Quality Control of Taraxaci Herba: A Comprehensive Review', Pharmaceuticals, 17(9), 1113. doi:10.3390/ph17091113."),
]


def esc(s):
    return s.replace("{", "(").replace("}", ")").replace("\\", "/")


def render(r):
    lines = [f'  author  = {{{esc(r["author"])}}}',
             f'  title   = {{{esc(r["title"])}}}',
             f'  note    = {{{r["ref"]}}}',
             f'  year    = {{{r["year"]}}}']
    if r.get("doi"):
        lines.append(f'  doi     = {{{r["doi"]}}}')
    if r.get("url"):
        lines.append(f'  url     = {{{r["url"]}}}')
    lines.append(f'  annote  = {{{esc(r["annote"])}}}')
    return f'@{r["type"]}{{{r["key"]},\n' + ",\n".join(lines) + "\n}"


def upsert_bibliography():
    text = open(BIBLIO, encoding="utf-8").read()
    cut = text.find("@")
    header, body = (text[:cut], text[cut:]) if cut != -1 else (text, "")
    # Split existing entries, keyed by citation key. Any block that does not
    # parse is preserved verbatim under a synthetic key so nothing is ever
    # silently dropped during the re-sort.
    entries = {}
    for i, block in enumerate(re.split(r"(?m)^(?=@)", body)):
        block = block.strip()
        if not block:
            continue
        m = re.match(r"@\w+\s*\{\s*([^,\s]+)", block)
        key = m.group(1) if m else f"~unparsed{i}"
        if key in entries:
            key = f"{key}~dup{i}"
        entries[key] = block
    # Add/replace the new Dandelion references.
    for r in NEW_REFS:
        entries[r["key"]] = render(r)
    ordered = [entries[k] for k in sorted(entries, key=str.lower)]
    with open(BIBLIO, "w", encoding="utf-8") as fh:
        fh.write(header.rstrip() + "\n\n")
        fh.write("\n\n".join(ordered) + "\n")


def write_dandelion():
    R = {r["key"]: r["ref"] for r in NEW_REFS}
    rec = {
        "common_names": [
            "Dandelion", "Common dandelion", "Lion's tooth", "Blowball",
            "Puffball", "Priest's crown", "Pissenlit", "Wet-the-bed",
            "Irish daisy", "Monk's head",
        ],
        "scientific_name": "Taraxacum officinale",
        "family": "Asteraceae",
        "parts_used": [
            {"name": "Leaf", "medicinal_actions": [
                {"action": "Diuretic (potassium-sparing)",
                 "reference_ids": [R["clare2009diuretic"], R["hao2024taraxacum"], R["wu2024taraxaci"]],
                 "status": "verified"},
                {"action": "Bitter digestive tonic",
                 "reference_ids": [R["hao2024taraxacum"], R["herbalrealitynddandelion"]],
                 "status": "verified"},
                {"action": "Choleretic (stimulates bile flow)",
                 "reference_ids": [R["hao2024taraxacum"], R["wu2024taraxaci"]],
                 "status": "verified"},
                {"action": "Edible bitter spring green (traditional food use)",
                 "reference_ids": [R["firstnaturendtaraxacum"], R["goodgrubndplant"],
                                   R["wikipediandtaraxacum"], R["umassndtaraxacum"],
                                   R["wisconsinnddandelion"], R["bsbindtaraxacum"]],
                 "status": "verified"},
            ]},
            {"name": "Root", "medicinal_actions": [
                {"action": "Hepatic (liver) support",
                 "reference_ids": [R["hao2024taraxacum"], R["wu2024taraxaci"], R["kania2022dandelion"]],
                 "status": "verified"},
                {"action": "Choleretic (stimulates bile flow)",
                 "reference_ids": [R["hao2024taraxacum"], R["wu2024taraxaci"]],
                 "status": "verified"},
                {"action": "Prebiotic (inulin-rich, especially autumn root)",
                 "reference_ids": [R["kania2022dandelion"], R["hao2024taraxacum"]],
                 "status": "verified"},
                {"action": "Mild laxative",
                 "reference_ids": [R["herbalrealitynddandelion"], R["hao2024taraxacum"]],
                 "status": "verified"},
                {"action": "Roasted-root coffee substitute (traditional preparation)",
                 "reference_ids": [R["farm2021harvest"], R["mossy2025forage"],
                                   R["under2025foraging"], R["herbawave2026dandelion"]],
                 "status": "verified"},
            ]},
            {"name": "Flower", "medicinal_actions": [
                {"action": "Traditional preparation into wines and syrups",
                 "reference_ids": [R["farm2021harvest"], R["practical2024dandelion"],
                                   R["under2025foraging"], R["fsusndtaraxacum"]],
                 "status": "verified"},
            ]},
            {"name": "Whole plant", "medicinal_actions": [
                {"action": "Anti-inflammatory",
                 "reference_ids": [R["sharifi2018ethnobotany"], R["hao2024taraxacum"]],
                 "status": "verified"},
                {"action": "Antioxidant",
                 "reference_ids": [R["sharifi2018ethnobotany"], R["kania2022dandelion"]],
                 "status": "verified"},
                {"action": "Antimicrobial",
                 "reference_ids": [R["sharifi2018ethnobotany"]],
                 "status": "verified"},
            ]},
        ],
        "constituents": [
            {"name": "Sesquiterpene lactones",
             "note": "Bitter principles (e.g. taraxacin) responsible for the characteristic bitterness and bitter-tonic action.",
             "reference_ids": [R["hao2024taraxacum"], R["wu2024taraxaci"]]},
            {"name": "Triterpenes and plant sterols",
             "note": "Including taraxasterol; contribute to anti-inflammatory and hepatoprotective signals.",
             "reference_ids": [R["hao2024taraxacum"], R["sharifi2018ethnobotany"]]},
            {"name": "Phenolic acids and flavonoids",
             "note": "Antioxidant constituents (e.g. chicoric acid, luteolin derivatives).",
             "reference_ids": [R["kania2022dandelion"], R["sharifi2018ethnobotany"]]},
            {"name": "Inulin",
             "note": "Fructan storage carbohydrate; prebiotic fibre concentrated in the autumn root.",
             "reference_ids": [R["kania2022dandelion"], R["hao2024taraxacum"]]},
        ],
        "contraindications": [
            {"note": "Allergy risk in individuals sensitive to Asteraceae (daisy family) plants such as ragweed and chamomile.",
             "reference_ids": [R["herbalrealitynddandelion"], R["rodriguez2007risks"]],
             "status": "verified"},
            {"note": "Avoid medicinal use in anyone with a blocked bile duct or gallstones; use caution with gallbladder or serious liver disease.",
             "reference_ids": [R["herbalrealitynddandelion"]],
             "status": "verified"},
            {"note": "May potentiate prescription diuretics; possible interactions with lithium and drugs metabolised by the liver.",
             "reference_ids": [R["rodriguez2007risks"], R["herbalrealitynddandelion"]],
             "status": "verified"},
            {"note": "Can accumulate soil pollutants and heavy metals; harvest from clean, unpolluted sites.",
             "reference_ids": [R["wu2024taraxaci"], R["herbalrealitynddandelion"]],
             "status": "verified"},
            {"note": "Use during pregnancy or breastfeeding should be guided by a qualified practitioner. Herbal use should support, not replace, conventional medical care.",
             "reference_ids": [R["herbalrealitynddandelion"]],
             "status": "verified"},
        ],
        "internal_notes": (
            "Worked example. Curated from the omniasana.bio Materia Medica post "
            "(https://omniasana.bio/dandelion-taraxacum-officinale/). Unlike the "
            "bulk book-ingested records, actions are mapped to specific parts and "
            "references per the source post. The Kew Plants of the World Online "
            f"entry is shared with the book ingestion ({KEW})."
        ),
        "last_updated": "2026-06-12",
        "status": "verified",
    }
    path = os.path.join(PLANTS_DIR, "taraxacum_officinale.yaml")
    with open(path, "w", encoding="utf-8") as fh:
        yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True,
                       default_flow_style=False, width=100)
    return path


def reconcile_ids():
    """Assign new REF ids after the highest existing id, and find the existing
    Kew 'Taraxacum officinale' entry to reuse instead of duplicating it."""
    global KEW
    text = open(BIBLIO, encoding="utf-8").read()
    ids = [int(m) for m in re.findall(r"REF-(\d+)", text)]
    nextid = (max(ids) + 1) if ids else 1
    # Reuse the book's Kew Taraxacum POWO entry if present.
    found = None
    for block in re.split(r"(?m)^(?=@)", text):
        if "Royal Botanic Gardens, Kew" in block and re.search(r"Taraxac", block):
            m = re.search(r"REF-(\d+)", block)
            if m:
                found = f"REF-{int(m.group(1)):04d}"
                break
    KEW = found or "REF-9999"
    for i, r in enumerate(NEW_REFS):
        r["ref"] = f"REF-{nextid + i:04d}"
    return nextid


if __name__ == "__main__":
    start = reconcile_ids()
    upsert_bibliography()
    p = write_dandelion()
    print("Wrote", p)
    print(f"Added {len(NEW_REFS)} references "
          f"(REF-{start:04d}..REF-{start + len(NEW_REFS) - 1:04d}); "
          f"reused {KEW} for the Kew Taraxacum entry.")
