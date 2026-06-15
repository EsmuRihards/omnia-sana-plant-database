#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch.

This batch targets six plant records that previously carried only two
references each (the least-cited records after the 2026-06-13 pass):

    Silybum marianum (Milk Thistle), Harpagophytum procumbens (Devil's Claw),
    Passiflora incarnata (Passionflower), Hibiscus sabdariffa (Hibiscus),
    Centella asiatica (Gotu Kola), Serenoa repens (Saw Palmetto).

For each, additional primary trials, systematic reviews and meta-analyses were
sourced from PubMed/PMC and added as REF-0559..REF-0572 below. The new ids are
then cited from the relevant actions / constituents / contraindications in the
plant YAML files (edited alongside this script, with provenance recorded in each
record's internal_notes).

The script is additive and idempotent: it inserts each new BibTeX entry at the
correct alphabetical position by citation key without reordering existing
entries, so re-running it makes no further change once the ids are present.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

# REF-XXXX -> BibTeX entry text. Each block ends with "}\n\n" so spacing matches
# the surrounding file.
NEW_ENTRIES = {
    "voroneanu2016silymarin": """@article{voroneanu2016silymarin,
  author  = {Voroneanu, L., Nistor, I., Dumea, R., Apetrii, M. and Covic, A.},
  title   = {Silymarin in Type 2 Diabetes Mellitus: A Systematic Review and Meta-Analysis of Randomized Controlled Trials},
  journal = {Journal of Diabetes Research},
  note    = {REF-0559},
  year    = {2016},
  doi     = {10.1155/2016/5147468},
  annote  = {Voroneanu, L., Nistor, I., Dumea, R., Apetrii, M. and Covic, A. (2016) 'Silymarin in Type 2 Diabetes Mellitus: A Systematic Review and Meta-Analysis of Randomized Controlled Trials', Journal of Diabetes Research, 2016, 5147468. doi:10.1155/2016/5147468.}
}

""",
    "zhou2021nafld": """@article{zhou2021nafld,
  author  = {Zhou, J., Chen, Y., Yu, J., Li, T., Lu, Z., Chen, Y., Zhang, X. and Ye, F.},
  title   = {The efficacy of novel metabolic targeted agents and natural plant drugs for nonalcoholic fatty liver disease treatment: A PRISMA-compliant network meta-analysis of randomized controlled trials},
  journal = {Medicine (Baltimore)},
  note    = {REF-0560},
  year    = {2021},
  doi     = {10.1097/MD.0000000000024884},
  annote  = {Zhou, J., Chen, Y., Yu, J., Li, T., Lu, Z., Chen, Y., Zhang, X. and Ye, F. (2021) 'The efficacy of novel metabolic targeted agents and natural plant drugs for nonalcoholic fatty liver disease treatment: A PRISMA-compliant network meta-analysis of randomized controlled trials', Medicine (Baltimore), 100(12), e24884. doi:10.1097/MD.0000000000024884.}
}

""",
    "gagnier2004harpagophytum": """@article{gagnier2004harpagophytum,
  author  = {Gagnier, J.J., Chrubasik, S. and Manheimer, E.},
  title   = {Harpagophytum procumbens for osteoarthritis and low back pain: a systematic review},
  journal = {BMC Complementary and Alternative Medicine},
  note    = {REF-0561},
  year    = {2004},
  doi     = {10.1186/1472-6882-4-13},
  annote  = {Gagnier, J.J., Chrubasik, S. and Manheimer, E. (2004) 'Harpagophytum procumbens for osteoarthritis and low back pain: a systematic review', BMC Complementary and Alternative Medicine, 4, 13. doi:10.1186/1472-6882-4-13.}
}

""",
    "chrubasik2004effectiveness": """@article{chrubasik2004effectiveness,
  author  = {Chrubasik, S., Conradt, C. and Roufogalis, B.D.},
  title   = {Effectiveness of Harpagophytum extracts and clinical efficacy},
  journal = {Phytotherapy Research},
  note    = {REF-0562},
  year    = {2004},
  doi     = {10.1002/ptr.1416},
  annote  = {Chrubasik, S., Conradt, C. and Roufogalis, B.D. (2004) 'Effectiveness of Harpagophytum extracts and clinical efficacy', Phytotherapy Research, 18(2), pp. 187-189. doi:10.1002/ptr.1416.}
}

""",
    "movafegh2008passiflora": """@article{movafegh2008passiflora,
  author  = {Movafegh, A., Alizadeh, R., Hajimohamadi, F., Esfehani, F. and Nejatfar, M.},
  title   = {Preoperative oral Passiflora incarnata reduces anxiety in ambulatory surgery patients: a double-blind, placebo-controlled study},
  journal = {Anesthesia and Analgesia},
  note    = {REF-0563},
  year    = {2008},
  doi     = {10.1213/ane.0b013e318172c3f9},
  annote  = {Movafegh, A., Alizadeh, R., Hajimohamadi, F., Esfehani, F. and Nejatfar, M. (2008) 'Preoperative oral Passiflora incarnata reduces anxiety in ambulatory surgery patients: a double-blind, placebo-controlled study', Anesthesia and Analgesia, 106(6), pp. 1728-1732. doi:10.1213/ane.0b013e318172c3f9.}
}

""",
    "lee2020passiflora": """@article{lee2020passiflora,
  author  = {Lee, J., Jung, H.Y., Lee, S.I., Choi, J.H. and Kim, S.G.},
  title   = {Effects of Passiflora incarnata Linnaeus on polysomnographic sleep parameters in subjects with insomnia disorder: a double-blind randomized placebo-controlled study},
  journal = {International Clinical Psychopharmacology},
  note    = {REF-0564},
  year    = {2020},
  doi     = {10.1097/YIC.0000000000000291},
  annote  = {Lee, J., Jung, H.Y., Lee, S.I., Choi, J.H. and Kim, S.G. (2020) 'Effects of Passiflora incarnata Linnaeus on polysomnographic sleep parameters in subjects with insomnia disorder: a double-blind randomized placebo-controlled study', International Clinical Psychopharmacology, 35(1), pp. 29-35. doi:10.1097/YIC.0000000000000291.}
}

""",
    "ngan2011passiflora": """@article{ngan2011passiflora,
  author  = {Ngan, A. and Conduit, R.},
  title   = {A double-blind, placebo-controlled investigation of the effects of Passiflora incarnata (passionflower) herbal tea on subjective sleep quality},
  journal = {Phytotherapy Research},
  note    = {REF-0565},
  year    = {2011},
  doi     = {10.1002/ptr.3400},
  annote  = {Ngan, A. and Conduit, R. (2011) 'A double-blind, placebo-controlled investigation of the effects of Passiflora incarnata (passionflower) herbal tea on subjective sleep quality', Phytotherapy Research, 25(8), pp. 1153-1159. doi:10.1002/ptr.3400.}
}

""",
    "abdelmonem2022hibiscus": """@article{abdelmonem2022hibiscus,
  author  = {Abdelmonem, M., Ebada, M.A., Diab, S., Ahmed, M.M., Zaazouee, M.S. and others},
  title   = {Efficacy of Hibiscus sabdariffa on Reducing Blood Pressure in Patients With Mild-to-Moderate Hypertension: A Systematic Review and Meta-Analysis of Published Randomized Controlled Trials},
  journal = {Journal of Cardiovascular Pharmacology},
  note    = {REF-0566},
  year    = {2022},
  doi     = {10.1097/FJC.0000000000001161},
  annote  = {Abdelmonem, M., Ebada, M.A., Diab, S., Ahmed, M.M., Zaazouee, M.S., et al. (2022) 'Efficacy of Hibiscus sabdariffa on Reducing Blood Pressure in Patients With Mild-to-Moderate Hypertension: A Systematic Review and Meta-Analysis of Published Randomized Controlled Trials', Journal of Cardiovascular Pharmacology, 79(1), pp. e64-e74. doi:10.1097/FJC.0000000000001161.}
}

""",
    "najafpour2020hibiscus": """@article{najafpour2020hibiscus,
  author  = {Najafpour Boushehri, S., Karimbeiki, R., Ghasempour, S., Ghalishourani, S.S., Pourmasoumi, M. and others},
  title   = {The efficacy of sour tea (Hibiscus sabdariffa L.) on selected cardiovascular disease risk factors: A systematic review and meta-analysis of randomized clinical trials},
  journal = {Phytotherapy Research},
  note    = {REF-0567},
  year    = {2020},
  doi     = {10.1002/ptr.6541},
  annote  = {Najafpour Boushehri, S., Karimbeiki, R., Ghasempour, S., Ghalishourani, S.S., Pourmasoumi, M., et al. (2020) 'The efficacy of sour tea (Hibiscus sabdariffa L.) on selected cardiovascular disease risk factors: A systematic review and meta-analysis of randomized clinical trials', Phytotherapy Research, 34(2), pp. 329-339. doi:10.1002/ptr.6541.}
}

""",
    "puttarak2017centella": """@article{puttarak2017centella,
  author  = {Puttarak, P., Dilokthornsakul, P., Saokaew, S., Dhippayom, T., Kongkaew, C. and others},
  title   = {Effects of Centella asiatica (L.) Urb. on cognitive function and mood related outcomes: A Systematic Review and Meta-analysis},
  journal = {Scientific Reports},
  note    = {REF-0568},
  year    = {2017},
  doi     = {10.1038/s41598-017-09823-9},
  annote  = {Puttarak, P., Dilokthornsakul, P., Saokaew, S., Dhippayom, T., Kongkaew, C., et al. (2017) 'Effects of Centella asiatica (L.) Urb. on cognitive function and mood related outcomes: A Systematic Review and Meta-analysis', Scientific Reports, 7(1), 10646. doi:10.1038/s41598-017-09823-9.}
}

""",
    "chong2013centella": """@article{chong2013centella,
  author  = {Chong, N.J. and Aziz, Z.},
  title   = {A Systematic Review of the Efficacy of Centella asiatica for Improvement of the Signs and Symptoms of Chronic Venous Insufficiency},
  journal = {Evidence-Based Complementary and Alternative Medicine},
  note    = {REF-0569},
  year    = {2013},
  doi     = {10.1155/2013/627182},
  annote  = {Chong, N.J. and Aziz, Z. (2013) 'A Systematic Review of the Efficacy of Centella asiatica for Improvement of the Signs and Symptoms of Chronic Venous Insufficiency', Evidence-Based Complementary and Alternative Medicine, 2013, 627182. doi:10.1155/2013/627182.}
}

""",
    "martinezzapata2020phlebotonics": """@article{martinezzapata2020phlebotonics,
  author  = {Martinez-Zapata, M.J., Vernooij, R.W., Simancas-Racines, D., Uriona Tuma, S.M., Stein, A.T. and others},
  title   = {Phlebotonics for venous insufficiency},
  journal = {Cochrane Database of Systematic Reviews},
  note    = {REF-0570},
  year    = {2020},
  doi     = {10.1002/14651858.CD003229.pub4},
  annote  = {Martinez-Zapata, M.J., Vernooij, R.W., Simancas-Racines, D., Uriona Tuma, S.M., Stein, A.T., et al. (2020) 'Phlebotonics for venous insufficiency', Cochrane Database of Systematic Reviews, 11, CD003229. doi:10.1002/14651858.CD003229.pub4.}
}

""",
    "velanavarrete2018serenoa": """@article{velanavarrete2018serenoa,
  author  = {Vela-Navarrete, R., Alcaraz, A., Rodriguez-Antolin, A., Minana Lopez, B., Fernandez-Gomez, J.M. and others},
  title   = {Efficacy and safety of a hexanic extract of Serenoa repens (Permixon) for the treatment of lower urinary tract symptoms associated with benign prostatic hyperplasia (LUTS/BPH): systematic review and meta-analysis of randomised controlled trials and observational studies},
  journal = {BJU International},
  note    = {REF-0571},
  year    = {2018},
  doi     = {10.1111/bju.14362},
  annote  = {Vela-Navarrete, R., Alcaraz, A., Rodriguez-Antolin, A., Minana Lopez, B., Fernandez-Gomez, J.M., et al. (2018) 'Efficacy and safety of a hexanic extract of Serenoa repens (Permixon) for the treatment of lower urinary tract symptoms associated with benign prostatic hyperplasia (LUTS/BPH): systematic review and meta-analysis of randomised controlled trials and observational studies', BJU International, 122(6), pp. 1049-1065. doi:10.1111/bju.14362.}
}

""",
    "novara2016serenoa": """@article{novara2016serenoa,
  author  = {Novara, G., Giannarini, G., Alcaraz, A., Cozar-Olmo, J.M., Descazeaud, A., Montorsi, F. and Ficarra, V.},
  title   = {Efficacy and Safety of Hexanic Lipidosterolic Extract of Serenoa repens (Permixon) in the Treatment of Lower Urinary Tract Symptoms Due to Benign Prostatic Hyperplasia: Systematic Review and Meta-analysis of Randomized Controlled Trials},
  journal = {European Urology Focus},
  note    = {REF-0572},
  year    = {2016},
  doi     = {10.1016/j.euf.2016.04.002},
  annote  = {Novara, G., Giannarini, G., Alcaraz, A., Cozar-Olmo, J.M., Descazeaud, A., Montorsi, F. and Ficarra, V. (2016) 'Efficacy and Safety of Hexanic Lipidosterolic Extract of Serenoa repens (Permixon) in the Treatment of Lower Urinary Tract Symptoms Due to Benign Prostatic Hyperplasia: Systematic Review and Meta-analysis of Randomized Controlled Trials', European Urology Focus, 2(5), pp. 553-561. doi:10.1016/j.euf.2016.04.002.}
}

""",
}


def citation_key(entry_text):
    m = re.match(r"@\w+\{([^,]+),", entry_text)
    return m.group(1) if m else ""


def main():
    with open(BIB, encoding="utf-8") as fh:
        text = fh.read()

    # Split into preamble + one chunk per entry (each chunk starts at a line
    # beginning with '@' and includes its trailing blank line(s)).
    parts = re.split(r"(?m)^(?=@)", text)
    preamble, entries = parts[0], parts[1:]
    keys = [citation_key(e) for e in entries]

    existing_notes = set(re.findall(r"REF-\d+", text))

    added = 0
    for key in sorted(NEW_ENTRIES):
        block = NEW_ENTRIES[key]
        ref_id = re.search(r"REF-\d+", block).group(0)
        if ref_id in existing_notes or key in keys:
            continue  # idempotent: already present
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
