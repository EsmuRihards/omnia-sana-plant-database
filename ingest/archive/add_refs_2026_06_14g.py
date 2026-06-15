#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 7.

Targets six more records that carried only two references each:

    Verbascum densiflorum (Mullein), Euphrasia officinalis (Eyebright),
    Dioscorea villosa (Wild Yam), Verbena officinalis (Vervain),
    Angelica archangelica (Angelica), Viola tricolor (Heartsease).

New sources from PubMed/PMC are added as REF-0611..REF-0617 and cited from the
relevant actions / constituents in the plant YAML files (edited alongside this
script, provenance in each record's internal_notes).

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "sarrell2001otikon": """@article{sarrell2001otikon,
  author  = {Sarrell, E.M., Mandelberg, A. and Cohen, H.A.},
  title   = {Efficacy of naturopathic extracts in the management of ear pain associated with acute otitis media},
  journal = {Archives of Pediatrics & Adolescent Medicine},
  note    = {REF-0611},
  year    = {2001},
  doi     = {10.1001/archpedi.155.7.796},
  annote  = {Sarrell, E.M., Mandelberg, A. and Cohen, H.A. (2001) 'Efficacy of naturopathic extracts in the management of ear pain associated with acute otitis media', Archives of Pediatrics & Adolescent Medicine, 155(7), pp. 796-799. doi:10.1001/archpedi.155.7.796. [Otikon ear drops contain Verbascum thapsus among other herbs.]}
}

""",
    "sarrell2003naturopathic": """@article{sarrell2003naturopathic,
  author  = {Sarrell, E.M., Cohen, H.A. and Kahan, E.},
  title   = {Naturopathic treatment for ear pain in children},
  journal = {Pediatrics},
  note    = {REF-0612},
  year    = {2003},
  doi     = {10.1542/peds.111.5.e574},
  annote  = {Sarrell, E.M., Cohen, H.A. and Kahan, E. (2003) 'Naturopathic treatment for ear pain in children', Pediatrics, 111(5 Pt 1), pp. e574-e579. doi:10.1542/peds.111.5.e574. [Naturopathic Herbal Extract Ear Drops contain Verbascum thapsus among other herbs.]}
}

""",
    "stoss2000euphrasia": """@article{stoss2000euphrasia,
  author  = {Stoss, M., Michels, C., Peter, E., Beutke, R. and Gorter, R.W.},
  title   = {Prospective cohort trial of Euphrasia single-dose eye drops in conjunctivitis},
  journal = {Journal of Alternative and Complementary Medicine},
  note    = {REF-0613},
  year    = {2000},
  doi     = {10.1089/acm.2000.6.499},
  annote  = {Stoss, M., Michels, C., Peter, E., Beutke, R. and Gorter, R.W. (2000) 'Prospective cohort trial of Euphrasia single-dose eye drops in conjunctivitis', Journal of Alternative and Complementary Medicine, 6(6), pp. 499-508. doi:10.1089/acm.2000.6.499.}
}

""",
    "komesaroff2001wildyam": """@article{komesaroff2001wildyam,
  author  = {Komesaroff, P.A., Black, C.V., Cable, V. and Sudhir, K.},
  title   = {Effects of wild yam extract on menopausal symptoms, lipids and sex hormones in healthy menopausal women},
  journal = {Climacteric},
  note    = {REF-0614},
  year    = {2001},
  annote  = {Komesaroff, P.A., Black, C.V., Cable, V. and Sudhir, K. (2001) 'Effects of wild yam extract on menopausal symptoms, lipids and sex hormones in healthy menopausal women', Climacteric, 4(2), pp. 144-150. [Double-blind, placebo-controlled crossover RCT; topical wild yam cream had little effect on menopausal symptoms or hormones.]}
}

""",
    "lopezseoane2025angelica": """@article{lopezseoane2025angelica,
  author  = {Lopez-Seoane, J., Gesteiro, E., Castro-Alija, M.J., Quesada-Gonzalez, C., Perez-Ruiz, M. and Gonzalez-Gross, M.},
  title   = {Effects of Angelica archangelica Extract on Overactive Bladder: A Pilot Randomized Controlled Trial},
  journal = {Food Science & Nutrition},
  note    = {REF-0615},
  year    = {2025},
  doi     = {10.1002/fsn3.71258},
  annote  = {Lopez-Seoane, J., Gesteiro, E., Castro-Alija, M.J., Quesada-Gonzalez, C., Perez-Ruiz, M. and Gonzalez-Gross, M. (2025) 'Effects of Angelica archangelica Extract on Overactive Bladder: A Pilot Randomized Controlled Trial', Food Science & Nutrition, 13(12), e71258. doi:10.1002/fsn3.71258.}
}

""",
    "khan2016verbena": """@article{khan2016verbena,
  author  = {Khan, A.W., Khan, A.U. and Ahmed, T.},
  title   = {Anticonvulsant, Anxiolytic, and Sedative Activities of Verbena officinalis},
  journal = {Frontiers in Pharmacology},
  note    = {REF-0616},
  year    = {2016},
  doi     = {10.3389/fphar.2016.00499},
  annote  = {Khan, A.W., Khan, A.U. and Ahmed, T. (2016) 'Anticonvulsant, Anxiolytic, and Sedative Activities of Verbena officinalis', Frontiers in Pharmacology, 7, 499. doi:10.3389/fphar.2016.00499.}
}

""",
    "retzl2023viola": """@article{retzl2023viola,
  author  = {Retzl, B., Zimmermann-Klemd, A.M., Winker, M., Nicolay, S., Grundemann, C. and Gruber, C.W.},
  title   = {Exploring Immune Modulatory Effects of Cyclotide-Enriched Viola tricolor Preparations},
  journal = {Planta Medica},
  note    = {REF-0617},
  year    = {2023},
  doi     = {10.1055/a-2173-8627},
  annote  = {Retzl, B., Zimmermann-Klemd, A.M., Winker, M., Nicolay, S., Grundemann, C. and Gruber, C.W. (2023) 'Exploring Immune Modulatory Effects of Cyclotide-Enriched Viola tricolor Preparations', Planta Medica, 89(15), pp. 1493-1504. doi:10.1055/a-2173-8627.}
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
