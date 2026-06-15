#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 5.

Targets five more records that carried only two references each:

    Cinnamomum cassia (Cassia Cinnamon), Oenothera biennis (Evening Primrose),
    Chelidonium majus (Greater Celandine), Potentilla erecta (Tormentil),
    Marrubium vulgare (White Horehound).

(Plantago lanceolata and Aloysia citrodora were also considered for this batch
but deferred: their EMA/ESCOP-monograph baseline already covers the species and
no clean species-specific NEW primary sources were found this round.)

New sources from PubMed/PMC are added as REF-0598..REF-0603 and cited from the
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
    "moridpour2023cinnamon": """@article{moridpour2023cinnamon,
  author  = {Moridpour, A.H., Kavyani, Z., Khosravi, S., Farmani, E., Daneshvar, M., Musazadeh, V. and Faghfouri, A.H.},
  title   = {The effect of cinnamon supplementation on glycemic control in patients with type 2 diabetes mellitus: An updated systematic review and dose-response meta-analysis of randomized controlled trials},
  journal = {Phytotherapy Research},
  note    = {REF-0598},
  year    = {2023},
  doi     = {10.1002/ptr.8026},
  annote  = {Moridpour, A.H., Kavyani, Z., Khosravi, S., Farmani, E., Daneshvar, M., Musazadeh, V. and Faghfouri, A.H. (2023) 'The effect of cinnamon supplementation on glycemic control in patients with type 2 diabetes mellitus: An updated systematic review and dose-response meta-analysis of randomized controlled trials', Phytotherapy Research, 38(1), pp. 117-130. doi:10.1002/ptr.8026.}
}

""",
    "demoura2025cinnamon": """@article{demoura2025cinnamon,
  author  = {de Moura, S.L., Gomes, B.G.R., Guilarducci, M.J., Coelho, O.G.L., Guimaraes, N.S. and Gomes, J.M.G.},
  title   = {Effects of cinnamon supplementation on metabolic biomarkers in individuals with type 2 diabetes: a systematic review and meta-analysis},
  journal = {Nutrition Reviews},
  note    = {REF-0599},
  year    = {2025},
  doi     = {10.1093/nutrit/nuae058},
  annote  = {de Moura, S.L., Gomes, B.G.R., Guilarducci, M.J., Coelho, O.G.L., Guimaraes, N.S. and Gomes, J.M.G. (2025) 'Effects of cinnamon supplementation on metabolic biomarkers in individuals with type 2 diabetes: a systematic review and meta-analysis', Nutrition Reviews, 83(2), pp. 249-279. doi:10.1093/nutrit/nuae058.}
}

""",
    "kumari2024evening": """@article{kumari2024evening,
  author  = {Kumari, J., Amrita, Sinha, A., Kumari, S., Biswas, P. and Poonam},
  title   = {Effectiveness of Evening Primrose and Vitamin E for Cyclical Mastalgia: A Prospective Study},
  journal = {Cureus},
  note    = {REF-0600},
  year    = {2024},
  doi     = {10.7759/cureus.58055},
  annote  = {Kumari, J., Amrita, Sinha, A., Kumari, S., Biswas, P. and Poonam (2024) 'Effectiveness of Evening Primrose and Vitamin E for Cyclical Mastalgia: A Prospective Study', Cureus, 16(4), e58055. doi:10.7759/cureus.58055.}
}

""",
    "ciornolutchii2024celandine": """@article{ciornolutchii2024celandine,
  author  = {Ciornolutchii, V., Ismaiel, A., Sabo, C.M., Al Hajjar, N., Seicean, A. and Dumitrascu, D.L.},
  title   = {A Hidden Cause of Hypertransaminasemia: Liver Toxicity Caused by Chelidonium Majus L. Report of Two Cases of Herb-Induced Liver Injury and Literature Review},
  journal = {American Journal of Therapeutics},
  note    = {REF-0601},
  year    = {2024},
  doi     = {10.1097/MJT.0000000000001708},
  annote  = {Ciornolutchii, V., Ismaiel, A., Sabo, C.M., Al Hajjar, N., Seicean, A. and Dumitrascu, D.L. (2024) 'A Hidden Cause of Hypertransaminasemia: Liver Toxicity Caused by Chelidonium Majus L. Report of Two Cases of Herb-Induced Liver Injury and Literature Review', American Journal of Therapeutics, 31(4), pp. e382-e387. doi:10.1097/MJT.0000000000001708.}
}

""",
    "subbotina2003tormentil": """@article{subbotina2003tormentil,
  author  = {Subbotina, M.D., Timchenko, V.N., Vorobyov, M.M., Konunova, Y.S., Aleksandrovih, Y.S. and Shushunov, S.},
  title   = {Effect of oral administration of tormentil root extract (Potentilla tormentilla) on rotavirus diarrhea in children: a randomized, double blind, controlled trial},
  journal = {The Pediatric Infectious Disease Journal},
  note    = {REF-0602},
  year    = {2003},
  doi     = {10.1097/01.inf.0000078355.29647.d0},
  annote  = {Subbotina, M.D., Timchenko, V.N., Vorobyov, M.M., Konunova, Y.S., Aleksandrovih, Y.S. and Shushunov, S. (2003) 'Effect of oral administration of tormentil root extract (Potentilla tormentilla) on rotavirus diarrhea in children: a randomized, double blind, controlled trial', The Pediatric Infectious Disease Journal, 22(8), pp. 706-711. doi:10.1097/01.inf.0000078355.29647.d0.}
}

""",
    "acimovic2020marrubium": """@article{acimovic2020marrubium,
  author  = {Acimovic, M., Jeremic, K., Salaj, N., Gavaric, N., Kiprovski, B., Sikora, V. and Zeremski, T.},
  title   = {Marrubium vulgare L.: A Phytochemical and Pharmacological Overview},
  journal = {Molecules},
  note    = {REF-0603},
  year    = {2020},
  doi     = {10.3390/molecules25122898},
  annote  = {Acimovic, M., Jeremic, K., Salaj, N., Gavaric, N., Kiprovski, B., Sikora, V. and Zeremski, T. (2020) 'Marrubium vulgare L.: A Phytochemical and Pharmacological Overview', Molecules, 25(12), 2898. doi:10.3390/molecules25122898.}
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
