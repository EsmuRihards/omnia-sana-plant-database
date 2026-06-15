#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 9.

Targets the harder, sparsely-studied tail of the two-reference records:

    Actaea racemosa (Black Cohosh), Acorus calamus (Sweet Flag),
    Arctium minus (Lesser Burdock), Asclepias tuberosa (Pleurisy Root),
    Bistorta officinalis (Bistort), Prunus serotina (Wild Cherry Bark).

New sources from PubMed/PMC are added as REF-0623..REF-0628 and cited from the
relevant actions / constituents / contraindications in the plant YAML files
(edited alongside this script, provenance in each record's internal_notes).

Elymus repens (Couch Grass) was also in this group but is genuinely not indexed
in PubMed under findable terms; its EMA HMPC + ESCOP monograph baseline is
retained unchanged.

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "borrelli2008cohosh": """@article{borrelli2008cohosh,
  author  = {Borrelli, F. and Ernst, E.},
  title   = {Black cohosh (Cimicifuga racemosa) for menopausal symptoms: a systematic review of its efficacy},
  journal = {Pharmacological Research},
  note    = {REF-0623},
  year    = {2008},
  doi     = {10.1016/j.phrs.2008.05.008},
  annote  = {Borrelli, F. and Ernst, E. (2008) 'Black cohosh (Cimicifuga racemosa) for menopausal symptoms: a systematic review of its efficacy', Pharmacological Research, 58(1), pp. 8-14. doi:10.1016/j.phrs.2008.05.008. [Concluded the efficacy of black cohosh for menopausal symptoms is uncertain and inconsistent across RCTs.]}
}

""",
    "sharma2020acorus": """@article{sharma2020acorus,
  author  = {Sharma, V., Sharma, R., Gautam, D.S., Kuca, K., Nepovimova, E. and Martins, N.},
  title   = {Role of Vacha (Acorus calamus Linn.) in Neurological and Metabolic Disorders: Evidence from Ethnopharmacology, Phytochemistry, Pharmacology and Clinical Study},
  journal = {Journal of Clinical Medicine},
  note    = {REF-0624},
  year    = {2020},
  doi     = {10.3390/jcm9041176},
  annote  = {Sharma, V., Sharma, R., Gautam, D.S., Kuca, K., Nepovimova, E. and Martins, N. (2020) 'Role of Vacha (Acorus calamus Linn.) in Neurological and Metabolic Disorders: Evidence from Ethnopharmacology, Phytochemistry, Pharmacology and Clinical Study', Journal of Clinical Medicine, 9(4), 1176. doi:10.3390/jcm9041176.}
}

""",
    "chan2011burdock": """@article{chan2011burdock,
  author  = {Chan, Y.S., Cheng, L.N., Wu, J.H., Chan, E., Kwan, Y.W., Lee, S.M.Y., Leung, G.P.H., Yu, P.H.F. and Chan, S.W.},
  title   = {A review of the pharmacological effects of Arctium lappa (burdock)},
  journal = {Inflammopharmacology},
  note    = {REF-0625},
  year    = {2011},
  doi     = {10.1007/s10787-010-0062-4},
  annote  = {Chan, Y.S., Cheng, L.N., Wu, J.H., Chan, E., Kwan, Y.W., Lee, S.M.Y., Leung, G.P.H., Yu, P.H.F. and Chan, S.W. (2011) 'A review of the pharmacological effects of Arctium lappa (burdock)', Inflammopharmacology, 19(5), pp. 245-254. doi:10.1007/s10787-010-0062-4. [Reviews the better-studied congener A. lappa; the root is used to "detoxify" blood and treat skin disease such as eczema, with antioxidant and antidiabetic constituents.]}
}

""",
    "mikkelsen2017asclepias": """@article{mikkelsen2017asclepias,
  author  = {Mikkelsen, L.H., Hamoudi, H., Gul, C.A. and Heegaard, S.},
  title   = {Corneal Toxicity Following Exposure to Asclepias Tuberosa},
  journal = {The Open Ophthalmology Journal},
  note    = {REF-0626},
  year    = {2017},
  doi     = {10.2174/1874364101711010001},
  annote  = {Mikkelsen, L.H., Hamoudi, H., Gul, C.A. and Heegaard, S. (2017) 'Corneal Toxicity Following Exposure to Asclepias Tuberosa', The Open Ophthalmology Journal, 11, pp. 1-4. doi:10.2174/1874364101711010001. [Case of corneal oedema after exposure to A. tuberosa latex, whose cardenolides inhibit Na/K-ATPase - documents the plant's cardiac-glycoside toxicity.]}
}

""",
    "khan2023bistorta": """@article{khan2023bistorta,
  author  = {Khan, S., Arshad, S., Masood, I., Arif, A., Abbas, S., Qureshi, A.W., Parveen, A. and Seemab Ameen, Z.},
  title   = {GC-MS Analysis of Persicaria bistorta: Uncovering the Molecular Basis of Its Traditional Medicinal Use},
  journal = {Applied Biochemistry and Biotechnology},
  note    = {REF-0627},
  year    = {2023},
  doi     = {10.1007/s12010-023-04580-0},
  annote  = {Khan, S., Arshad, S., Masood, I., Arif, A., Abbas, S., Qureshi, A.W., Parveen, A. and Seemab Ameen, Z. (2023) 'GC-MS Analysis of Persicaria bistorta: Uncovering the Molecular Basis of Its Traditional Medicinal Use', Applied Biochemistry and Biotechnology, 196(4), pp. 2270-2288. doi:10.1007/s12010-023-04580-0. [Persicaria bistorta = Bistorta officinalis; GC-MS characterised constituents and confirmed antibacterial activity of the extracts.]}
}

""",
    "palomares2017prunus": """@article{palomares2017prunus,
  author  = {Palomares-Alonso, F., Rojas-Tome, I.S., Palencia Hernandez, G., Jimenez-Arellanes, M.A., Macias-Rubalcava, M.L. and others},
  title   = {In vitro and in vivo cysticidal activity of extracts and isolated flavanone from the bark of Prunus serotina: A bio-guided study},
  journal = {Acta Tropica},
  note    = {REF-0628},
  year    = {2017},
  doi     = {10.1016/j.actatropica.2017.02.023},
  annote  = {Palomares-Alonso, F., Rojas-Tome, I.S., Palencia Hernandez, G., Jimenez-Arellanes, M.A., Macias-Rubalcava, M.L., et al. (2017) 'In vitro and in vivo cysticidal activity of extracts and isolated flavanone from the bark of Prunus serotina: A bio-guided study', Acta Tropica, 170, pp. 1-7. doi:10.1016/j.actatropica.2017.02.023. [Identified naringenin and methoxylated benzene derivatives in P. serotina bark and showed antiparasitic (cysticidal) activity.]}
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
