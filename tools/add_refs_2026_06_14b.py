#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 2.

Targets six more records that carried only two references each:

    Boswellia serrata, Hedera helix (Ivy Leaf), Pelargonium sidoides,
    Althaea officinalis (Marshmallow), Gentiana lutea (Gentian),
    Schisandra chinensis.

New sources from PubMed/PMC are added as REF-0573..REF-0583 and cited from
the relevant actions / constituents / contraindications in the plant YAML
files (edited alongside this script, provenance in each record's
internal_notes).

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "majeed2019boswellia": """@article{majeed2019boswellia,
  author  = {Majeed, M., Majeed, S., Narayanan, N.K. and Nagabhushanam, K.},
  title   = {A pilot, randomized, double-blind, placebo-controlled trial to assess the safety and efficacy of a novel Boswellia serrata extract in the management of osteoarthritis of the knee},
  journal = {Phytotherapy Research},
  note    = {REF-0573},
  year    = {2019},
  doi     = {10.1002/ptr.6338},
  annote  = {Majeed, M., Majeed, S., Narayanan, N.K. and Nagabhushanam, K. (2019) 'A pilot, randomized, double-blind, placebo-controlled trial to assess the safety and efficacy of a novel Boswellia serrata extract in the management of osteoarthritis of the knee', Phytotherapy Research, 33(5), pp. 1457-1468. doi:10.1002/ptr.6338.}
}

""",
    "liu2018supplements": """@article{liu2018supplements,
  author  = {Liu, X., Machado, G.C., Eyles, J.P., Ravi, V. and Hunter, D.J.},
  title   = {Dietary supplements for treating osteoarthritis: a systematic review and meta-analysis},
  journal = {British Journal of Sports Medicine},
  note    = {REF-0574},
  year    = {2018},
  doi     = {10.1136/bjsports-2016-097333},
  annote  = {Liu, X., Machado, G.C., Eyles, J.P., Ravi, V. and Hunter, D.J. (2018) 'Dietary supplements for treating osteoarthritis: a systematic review and meta-analysis', British Journal of Sports Medicine, 52(3), pp. 167-175. doi:10.1136/bjsports-2016-097333.}
}

""",
    "schaefer2016ivy": """@article{schaefer2016ivy,
  author  = {Schaefer, A., Kehr, M.S., Giannetti, B.M., Bulitta, M. and Staiger, C.},
  title   = {A randomized, controlled, double-blind, multi-center trial to evaluate the efficacy and safety of a liquid containing ivy leaves dry extract (EA 575) vs. placebo in the treatment of adults with acute cough},
  journal = {Die Pharmazie},
  note    = {REF-0575},
  year    = {2016},
  doi     = {10.1691/ph.2016.6712},
  annote  = {Schaefer, A., Kehr, M.S., Giannetti, B.M., Bulitta, M. and Staiger, C. (2016) 'A randomized, controlled, double-blind, multi-center trial to evaluate the efficacy and safety of a liquid containing ivy leaves dry extract (EA 575) vs. placebo in the treatment of adults with acute cough', Die Pharmazie, 71(9), pp. 504-509. doi:10.1691/ph.2016.6712.}
}

""",
    "agbabiaka2008pelargonium": """@article{agbabiaka2008pelargonium,
  author  = {Agbabiaka, T.B., Guo, R. and Ernst, E.},
  title   = {Pelargonium sidoides for acute bronchitis: a systematic review and meta-analysis},
  journal = {Phytomedicine},
  note    = {REF-0576},
  year    = {2008},
  doi     = {10.1016/j.phymed.2007.11.023},
  annote  = {Agbabiaka, T.B., Guo, R. and Ernst, E. (2008) 'Pelargonium sidoides for acute bronchitis: a systematic review and meta-analysis', Phytomedicine, 15(5), pp. 378-385. doi:10.1016/j.phymed.2007.11.023.}
}

""",
    "koch2016rhinosinusitis": """@article{koch2016rhinosinusitis,
  author  = {Koch, A.K., Klose, P., Lauche, R., Cramer, H., Baasch, J., Dobos, G.J. and Langhorst, J.},
  title   = {A Systematic Review of Phytotherapy for Acute Rhinosinusitis},
  journal = {Forschende Komplementarmedizin},
  note    = {REF-0577},
  year    = {2016},
  doi     = {10.1159/000447467},
  annote  = {Koch, A.K., Klose, P., Lauche, R., Cramer, H., Baasch, J., Dobos, G.J. and Langhorst, J. (2016) 'A Systematic Review of Phytotherapy for Acute Rhinosinusitis', Forschende Komplementarmedizin, 23(3), pp. 165-169. doi:10.1159/000447467.}
}

""",
    "sutovska2009althaea": """@article{sutovska2009althaea,
  author  = {Sutovska, M., Nosalova, G., Sutovsky, J., Franova, S., Prisenznakova, L. and Capek, P.},
  title   = {Possible mechanisms of dose-dependent cough suppressive effect of Althaea officinalis rhamnogalacturonan in guinea pigs test system},
  journal = {International Journal of Biological Macromolecules},
  note    = {REF-0578},
  year    = {2009},
  doi     = {10.1016/j.ijbiomac.2009.03.008},
  annote  = {Sutovska, M., Nosalova, G., Sutovsky, J., Franova, S., Prisenznakova, L. and Capek, P. (2009) 'Possible mechanisms of dose-dependent cough suppressive effect of Althaea officinalis rhamnogalacturonan in guinea pigs test system', International Journal of Biological Macromolecules, 45(1), pp. 27-32. doi:10.1016/j.ijbiomac.2009.03.008.}
}

""",
    "sutovska2011althaea": """@article{sutovska2011althaea,
  author  = {Sutovska, M., Capek, P., Franova, S., Joskova, M., Sutovsky, J., Marcinek, J. and Kalman, M.},
  title   = {Antitussive activity of Althaea officinalis L. polysaccharide rhamnogalacturonan and its changes in guinea pigs with ovalbumine-induced airways inflammation},
  journal = {Bratislavske Lekarske Listy},
  note    = {REF-0579},
  year    = {2011},
  annote  = {Sutovska, M., Capek, P., Franova, S., Joskova, M., Sutovsky, J., Marcinek, J. and Kalman, M. (2011) 'Antitussive activity of Althaea officinalis L. polysaccharide rhamnogalacturonan and its changes in guinea pigs with ovalbumine-induced airways inflammation', Bratislavske Lekarske Listy, 112(12), pp. 670-675.}
}

""",
    "jiang2020gentiana": """@article{jiang2020gentiana,
  author  = {Jiang, M., Cui, B.W., Wu, Y.L., Nan, J.X. and Lian, L.H.},
  title   = {Genus Gentiana: A review on phytochemistry, pharmacology and molecular mechanism},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0580},
  year    = {2020},
  doi     = {10.1016/j.jep.2020.113391},
  annote  = {Jiang, M., Cui, B.W., Wu, Y.L., Nan, J.X. and Lian, L.H. (2020) 'Genus Gentiana: A review on phytochemistry, pharmacology and molecular mechanism', Journal of Ethnopharmacology, 264, 113391. doi:10.1016/j.jep.2020.113391.}
}

""",
    "pan2016gentiana": """@article{pan2016gentiana,
  author  = {Pan, Y., Zhao, Y.L., Zhang, J., Li, W.Y. and Wang, Y.Z.},
  title   = {Phytochemistry and Pharmacological Activities of the Genus Gentiana (Gentianaceae)},
  journal = {Chemistry & Biodiversity},
  note    = {REF-0581},
  year    = {2016},
  doi     = {10.1002/cbdv.201500333},
  annote  = {Pan, Y., Zhao, Y.L., Zhang, J., Li, W.Y. and Wang, Y.Z. (2016) 'Phytochemistry and Pharmacological Activities of the Genus Gentiana (Gentianaceae)', Chemistry & Biodiversity, 13(2), pp. 107-150. doi:10.1002/cbdv.201500333.}
}

""",
    "park2016schisandra": """@article{park2016schisandra,
  author  = {Park, J.Y. and Kim, K.H.},
  title   = {A randomized, double-blind, placebo-controlled trial of Schisandra chinensis for menopausal symptoms},
  journal = {Climacteric},
  note    = {REF-0582},
  year    = {2016},
  doi     = {10.1080/13697137.2016.1238453},
  annote  = {Park, J.Y. and Kim, K.H. (2016) 'A randomized, double-blind, placebo-controlled trial of Schisandra chinensis for menopausal symptoms', Climacteric, 19(6), pp. 574-580. doi:10.1080/13697137.2016.1238453.}
}

""",
    "yang2021schisandra": """@article{yang2021schisandra,
  author  = {Yang, K., Qiu, J., Huang, Z., Yu, Z., Wang, W., Hu, H. and You, Y.},
  title   = {A comprehensive review of ethnopharmacology, phytochemistry, pharmacology, and pharmacokinetics of Schisandra chinensis (Turcz.) Baill. and Schisandra sphenanthera Rehd. et Wils.},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0583},
  year    = {2021},
  doi     = {10.1016/j.jep.2021.114759},
  annote  = {Yang, K., Qiu, J., Huang, Z., Yu, Z., Wang, W., Hu, H. and You, Y. (2021) 'A comprehensive review of ethnopharmacology, phytochemistry, pharmacology, and pharmacokinetics of Schisandra chinensis (Turcz.) Baill. and Schisandra sphenanthera Rehd. et Wils.', Journal of Ethnopharmacology, 284, 114759. doi:10.1016/j.jep.2021.114759.}
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
