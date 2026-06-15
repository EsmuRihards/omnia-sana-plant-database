#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 3.

Targets six more records that carried only two references each:

    Cynara scolymus (Artichoke), Astragalus membranaceus, Eleutherococcus
    senticosus (Siberian Ginseng), Hydrastis canadensis (Goldenseal),
    Aesculus hippocastanum (Horse Chestnut), Mahonia aquifolium (Oregon Grape).

New sources from PubMed/PMC are added as REF-0584..REF-0591 and cited from the
relevant actions / constituents / contraindications in the plant YAML files
(edited alongside this script, provenance in each record's internal_notes).

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "wider2013artichoke": """@article{wider2013artichoke,
  author  = {Wider, B., Pittler, M.H., Thompson-Coon, J. and Ernst, E.},
  title   = {Artichoke leaf extract for treating hypercholesterolaemia},
  journal = {Cochrane Database of Systematic Reviews},
  note    = {REF-0584},
  year    = {2013},
  doi     = {10.1002/14651858.CD003335.pub3},
  annote  = {Wider, B., Pittler, M.H., Thompson-Coon, J. and Ernst, E. (2013) 'Artichoke leaf extract for treating hypercholesterolaemia', Cochrane Database of Systematic Reviews, (3), CD003335. doi:10.1002/14651858.CD003335.pub3.}
}

""",
    "rondanelli2012artichoke": """@article{rondanelli2012artichoke,
  author  = {Rondanelli, M., Giacosa, A., Opizzi, A., Faliva, M.A., Sala, P. and others},
  title   = {Beneficial effects of artichoke leaf extract supplementation on increasing HDL-cholesterol in subjects with primary mild hypercholesterolaemia: a double-blind, randomized, placebo-controlled trial},
  journal = {International Journal of Food Sciences and Nutrition},
  note    = {REF-0585},
  year    = {2012},
  doi     = {10.3109/09637486.2012.700920},
  annote  = {Rondanelli, M., Giacosa, A., Opizzi, A., Faliva, M.A., Sala, P., et al. (2012) 'Beneficial effects of artichoke leaf extract supplementation on increasing HDL-cholesterol in subjects with primary mild hypercholesterolaemia: a double-blind, randomized, placebo-controlled trial', International Journal of Food Sciences and Nutrition, 64(1), pp. 7-15. doi:10.3109/09637486.2012.700920.}
}

""",
    "zhang2014astragalus": """@article{zhang2014astragalus,
  author  = {Zhang, H.W., Lin, Z.X., Xu, C., Leung, C. and Chan, L.S.},
  title   = {Astragalus (a traditional Chinese medicine) for treating chronic kidney disease},
  journal = {Cochrane Database of Systematic Reviews},
  note    = {REF-0586},
  year    = {2014},
  doi     = {10.1002/14651858.CD008369.pub2},
  annote  = {Zhang, H.W., Lin, Z.X., Xu, C., Leung, C. and Chan, L.S. (2014) 'Astragalus (a traditional Chinese medicine) for treating chronic kidney disease', Cochrane Database of Systematic Reviews, (10), CD008369. doi:10.1002/14651858.CD008369.pub2.}
}

""",
    "kos2025eleutherococcus": """@article{kos2025eleutherococcus,
  author  = {Kos, G., Czarnek, K., Sadok, I., Krzyszczak-Turczyn, A., Kubica, P. and others},
  title   = {Eleutherococcus senticosus: An Important Adaptogenic Plant},
  journal = {Molecules},
  note    = {REF-0587},
  year    = {2025},
  doi     = {10.3390/molecules30122512},
  annote  = {Kos, G., Czarnek, K., Sadok, I., Krzyszczak-Turczyn, A., Kubica, P., et al. (2025) 'Eleutherococcus senticosus: An Important Adaptogenic Plant', Molecules, 30(12), 2512. doi:10.3390/molecules30122512.}
}

""",
    "cech2012goldenseal": """@article{cech2012goldenseal,
  author  = {Cech, N.B., Junio, H.A., Ackermann, L.W., Kavanaugh, J.S. and Horswill, A.R.},
  title   = {Quorum quenching and antimicrobial activity of goldenseal (Hydrastis canadensis) against methicillin-resistant Staphylococcus aureus (MRSA)},
  journal = {Planta Medica},
  note    = {REF-0588},
  year    = {2012},
  doi     = {10.1055/s-0032-1315042},
  annote  = {Cech, N.B., Junio, H.A., Ackermann, L.W., Kavanaugh, J.S. and Horswill, A.R. (2012) 'Quorum quenching and antimicrobial activity of goldenseal (Hydrastis canadensis) against methicillin-resistant Staphylococcus aureus (MRSA)', Planta Medica, 78(14), pp. 1556-1561. doi:10.1055/s-0032-1315042.}
}

""",
    "sevior2010cyp": """@article{sevior2010cyp,
  author  = {Sevior, D.K., Hokkanen, J., Tolonen, A., Abass, K., Tursas, L., Pelkonen, O. and Ahokas, J.T.},
  title   = {Rapid screening of commercially available herbal products for the inhibition of major human hepatic cytochrome P450 enzymes using the N-in-one cocktail},
  journal = {Xenobiotica},
  note    = {REF-0589},
  year    = {2010},
  doi     = {10.3109/00498251003592683},
  annote  = {Sevior, D.K., Hokkanen, J., Tolonen, A., Abass, K., Tursas, L., Pelkonen, O. and Ahokas, J.T. (2010) 'Rapid screening of commercially available herbal products for the inhibition of major human hepatic cytochrome P450 enzymes using the N-in-one cocktail', Xenobiotica, 40(4), pp. 245-254. doi:10.3109/00498251003592683.}
}

""",
    "gallelli2019escin": """@article{gallelli2019escin,
  author  = {Gallelli, L.},
  title   = {Escin: a review of its anti-edematous, anti-inflammatory, and venotonic properties},
  journal = {Drug Design, Development and Therapy},
  note    = {REF-0590},
  year    = {2019},
  doi     = {10.2147/DDDT.S207720},
  annote  = {Gallelli, L. (2019) 'Escin: a review of its anti-edematous, anti-inflammatory, and venotonic properties', Drug Design, Development and Therapy, 13, pp. 3425-3437. doi:10.2147/DDDT.S207720.}
}

""",
    "bernstein2006mahonia": """@article{bernstein2006mahonia,
  author  = {Bernstein, S., Donsky, H., Gulliver, W., Hamilton, D., Nobel, S. and Norman, R.},
  title   = {Treatment of mild to moderate psoriasis with Relieva, a Mahonia aquifolium extract - a double-blind, placebo-controlled study},
  journal = {American Journal of Therapeutics},
  note    = {REF-0591},
  year    = {2006},
  doi     = {10.1097/00045391-200603000-00007},
  annote  = {Bernstein, S., Donsky, H., Gulliver, W., Hamilton, D., Nobel, S. and Norman, R. (2006) 'Treatment of mild to moderate psoriasis with Relieva, a Mahonia aquifolium extract - a double-blind, placebo-controlled study', American Journal of Therapeutics, 13(2), pp. 121-126. doi:10.1097/00045391-200603000-00007.}
}

""",
}


def citation_key(entry_text):
    m = re.match(r"@\w+\{([^,]+),", entry_text)
    return m.group(1) if m else ""


def main():
    with open(BIB, encoding="utf-8") as fh:
        text = fh.read()

    parts = re.split(r"(?m)^(?=@)", text)
    preamble, entries = parts[0], parts[1:]
    keys = [citation_key(e) for e in entries]
    existing_notes = set(re.findall(r"REF-\d+", text))

    added = 0
    for key in sorted(NEW_ENTRIES):
        block = NEW_ENTRIES[key]
        ref_id = re.search(r"REF-\d+", block).group(0)
        if ref_id in existing_notes or key in keys:
            continue
        pos = len(entries)
        for i, k in enumerate(keys):
            if k > key:
                pos = i
                break
        entries.insert(pos, block)
        keys.insert(pos, key)
        existing_notes.add(ref_id)
        added += 1

    with open(BIB, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(preamble + "".join(entries))

    print(f"Added {added} new reference(s); bibliography now has {len(entries)} entries.")


if __name__ == "__main__":
    main()
