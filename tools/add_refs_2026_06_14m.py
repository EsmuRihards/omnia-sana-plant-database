#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch M (least-cited records, 1).

First batch of the least-referenced (three-reference) records, enriching three
well-documented species by five new PubMed sources each:

    Actaea racemosa (Black cohosh)       -> REF-0670..REF-0674
    Aesculus hippocastanum (Horse chestnut) -> REF-0675..REF-0679
    Agrimonia eupatoria (Agrimony)       -> REF-0680..REF-0684

All sources from PubMed. New BibTeX entries inserted alphabetically by citation
key; YAML citations added by hand per action and logged in internal_notes.
Additive and idempotent.

Honest scope: Acorus calamus was held back from this batch - most retrievable
primary literature is on the related species Acorus tatarinowii (and one hit was
Agrimonia pilosa, not A. eupatoria); both were excluded to keep records
species-accurate. Black cohosh keeps a balanced evidence base (positive
meta-analysis REF-0670 alongside two null RCTs REF-0672/REF-0673).
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    # ---- Actaea racemosa (Black cohosh) ----------------------------------
    "castelobranco2020blackcohosh": """@article{castelobranco2020blackcohosh,
  author  = {Castelo-Branco, C., Gambacciani, M., Cano, A., Minkin, M.J., Rachon, D., Ruan, X., Beer, A.M., Schnitker, J., Henneicke-von Zepelin, H.H. and Pickartz, S.},
  title   = {Review and meta-analysis: isopropanolic black cohosh extract iCR for menopausal symptoms - an update on the evidence},
  journal = {Climacteric},
  note    = {REF-0670},
  year    = {2020},
  doi     = {10.1080/13697137.2020.1820477},
  annote  = {Castelo-Branco, C., Gambacciani, M., Cano, A., Minkin, M.J., Rachon, D., Ruan, X., Beer, A.M., Schnitker, J., Henneicke-von Zepelin, H.H. and Pickartz, S. (2020) 'Review and meta-analysis: isopropanolic black cohosh extract iCR for menopausal symptoms - an update on the evidence', Climacteric, 24(2), pp. 109-119. doi:10.1080/13697137.2020.1820477. [Meta-analysis (35 studies, 43,759 women): isopropanolic black cohosh extract was significantly superior to placebo for neurovegetative and psychological menopausal symptoms, dose-dependently and comparably to low-dose estradiol, with no evidence of hepatotoxicity and no effect on estrogen-sensitive tissues.]}
}

""",
    "pokushalov2025blackcohosh": """@article{pokushalov2025blackcohosh,
  author  = {Pokushalov, E., Ponomarenko, A., Garcia, C., Kasimova, L., Pak, I., Shrainer, E., Romanova, A., Kudlay, D., Johnson, M. and Miller, R.},
  title   = {Assessing the combined effects of Black Cohosh, Soy Isoflavones, and SDG Lignans on menopausal symptoms: a randomized, double-blind, placebo-controlled clinical trial},
  journal = {European Journal of Nutrition},
  note    = {REF-0671},
  year    = {2025},
  doi     = {10.1007/s00394-025-03588-y},
  annote  = {Pokushalov, E., Ponomarenko, A., Garcia, C., Kasimova, L., Pak, I., Shrainer, E., Romanova, A., Kudlay, D., Johnson, M. and Miller, R. (2025) 'Assessing the combined effects of Black Cohosh, Soy Isoflavones, and SDG Lignans on menopausal symptoms: a randomized, double-blind, placebo-controlled clinical trial', European Journal of Nutrition, 64(3), 138. doi:10.1007/s00394-025-03588-y. [90-day RCT (96 postmenopausal women): a black cohosh, soy isoflavone and SDG lignan combination significantly reduced all Menopause Rating Scale domains versus placebo, with a favourable safety profile.]}
}

""",
    "tanmahasamut2014blackcohosh": """@article{tanmahasamut2014blackcohosh,
  author  = {Tanmahasamut, P., Vichinsartvichai, P., Rattanachaiyanont, M., Techatraisak, K., Dangrat, C. and Sardod, P.},
  title   = {Cimicifuga racemosa extract for relieving menopausal symptoms: a randomized controlled trial},
  journal = {Climacteric},
  note    = {REF-0672},
  year    = {2014},
  doi     = {10.3109/13697137.2014.933410},
  annote  = {Tanmahasamut, P., Vichinsartvichai, P., Rattanachaiyanont, M., Techatraisak, K., Dangrat, C. and Sardod, P. (2014) 'Cimicifuga racemosa extract for relieving menopausal symptoms: a randomized controlled trial', Climacteric, 18(1), pp. 79-85. doi:10.3109/13697137.2014.933410. [RCT (54 Thai women): black cohosh 40 mg/day was not superior to placebo for relieving moderate-to-severe menopausal symptoms or improving quality of life, with no significant change in liver function.]}
}

""",
    "pockaj2006blackcohosh": """@article{pockaj2006blackcohosh,
  author  = {Pockaj, B.A., Gallagher, J.G., Loprinzi, C.L., Stella, P.J., Barton, D.L., Sloan, J.A. and others},
  title   = {Phase III double-blind, randomized, placebo-controlled crossover trial of black cohosh in the management of hot flashes: NCCTG Trial N01CC1},
  journal = {Journal of Clinical Oncology},
  note    = {REF-0673},
  year    = {2006},
  doi     = {10.1200/JCO.2005.05.4296},
  annote  = {Pockaj, B.A., Gallagher, J.G., Loprinzi, C.L., Stella, P.J., Barton, D.L., Sloan, J.A., et al. (2006) 'Phase III double-blind, randomized, placebo-controlled crossover trial of black cohosh in the management of hot flashes: NCCTG Trial N01CC1', Journal of Clinical Oncology, 24(18), pp. 2836-2841. doi:10.1200/JCO.2005.05.4296. [Phase III crossover RCT (132 women, mostly breast cancer survivors): black cohosh did not reduce hot flashes more than placebo.]}
}

""",
    "shahmohammadi2019menopause": """@article{shahmohammadi2019menopause,
  author  = {Shahmohammadi, A., Ramezanpour, N., Mahdavi Siuki, M., Dizavandi, F., Ghazanfarpour, M., Rahmani, Y., Tahajjodi, R. and Babakhanian, M.},
  title   = {The efficacy of herbal medicines on anxiety and depression in peri- and postmenopausal women: A systematic review and meta-analysis},
  journal = {Post Reproductive Health},
  note    = {REF-0674},
  year    = {2019},
  doi     = {10.1177/2053369119841166},
  annote  = {Shahmohammadi, A., Ramezanpour, N., Mahdavi Siuki, M., Dizavandi, F., Ghazanfarpour, M., Rahmani, Y., Tahajjodi, R. and Babakhanian, M. (2019) 'The efficacy of herbal medicines on anxiety and depression in peri- and postmenopausal women: A systematic review and meta-analysis', Post Reproductive Health, 25(3), pp. 131-141. doi:10.1177/2053369119841166. [Systematic review and meta-analysis of herbal medicines, including black cohosh, for relief of anxiety and depression in peri- and postmenopausal women.]}
}

""",
    # ---- Aesculus hippocastanum (Horse chestnut) -------------------------
    "cheong2018escin": """@article{cheong2018escin,
  author  = {Cheong, D.H.J., Arfuso, F., Sethi, G., Wang, L., Hui, K.M., Kumar, A.P. and Tran, T.},
  title   = {Molecular targets and anti-cancer potential of escin},
  journal = {Cancer Letters},
  note    = {REF-0675},
  year    = {2018},
  doi     = {10.1016/j.canlet.2018.02.027},
  annote  = {Cheong, D.H.J., Arfuso, F., Sethi, G., Wang, L., Hui, K.M., Kumar, A.P. and Tran, T. (2018) 'Molecular targets and anti-cancer potential of escin', Cancer Letters, 422, pp. 1-8. doi:10.1016/j.canlet.2018.02.027. [Review: escin, the triterpene-saponin mixture from horse chestnut, has potent anti-inflammatory and anti-oedematous properties used against chronic venous insufficiency and oedema, and additionally shows broad preclinical anti-cancer activity.]}
}

""",
    "domanski2016escin": """@article{domanski2016escin,
  author  = {Domanski, D., Zegrocka-Stendel, O., Perzanowska, A., Dutkiewicz, M., Kowalewska, M., Grabowska, I., Maciejko, D., Fogtman, A., Dadlez, M. and Koziak, K.},
  title   = {Molecular Mechanism for Cellular Response to beta-Escin and Its Therapeutic Implications},
  journal = {PLoS One},
  note    = {REF-0676},
  year    = {2016},
  doi     = {10.1371/journal.pone.0164365},
  annote  = {Domanski, D., Zegrocka-Stendel, O., Perzanowska, A., Dutkiewicz, M., Kowalewska, M., Grabowska, I., Maciejko, D., Fogtman, A., Dadlez, M. and Koziak, K. (2016) 'Molecular Mechanism for Cellular Response to beta-Escin and Its Therapeutic Implications', PLoS One, 11(10), e0164365. doi:10.1371/journal.pone.0164365. [In human endothelial cells beta-escin induced cholesterol synthesis, reduced monolayer permeability and migration, and inhibited NF-kB signalling and TNF-alpha-induced effector proteins, explaining its anti-oedematous, anti-inflammatory and venotonic effects.]}
}

""",
    "wu2011escin": """@article{wu2011escin,
  author  = {Wu, X.J., Zhang, M.L., Cui, X.Y., Gao, F., He, Q., Li, X.J., Zhang, J.W., Fawcett, J.P. and Gu, J.K.},
  title   = {Comparative pharmacokinetics and bioavailability of escin Ia and isoescin Ia after administration of escin and of pure escin Ia and isoescin Ia in rat},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0677},
  year    = {2011},
  doi     = {10.1016/j.jep.2011.11.003},
  annote  = {Wu, X.J., Zhang, M.L., Cui, X.Y., Gao, F., He, Q., Li, X.J., Zhang, J.W., Fawcett, J.P. and Gu, J.K. (2011) 'Comparative pharmacokinetics and bioavailability of escin Ia and isoescin Ia after administration of escin and of pure escin Ia and isoescin Ia in rat', Journal of Ethnopharmacology, 139(1), pp. 201-206. doi:10.1016/j.jep.2011.11.003. [Pharmacokinetic study: escin Ia and isoescin Ia, the chief active saponins of horse chestnut, have low oral bioavailability and interconvert in vivo, so whole-herb escin preparations give a longer duration of action than single isomers.]}
}

""",
    "gloviczki2025venoactive": """@article{gloviczki2025venoactive,
  author  = {Gloviczki, M.L., Kakkos, S.K., Urbanek, T., Chuback, J. and Nicolaides, A.},
  title   = {The role of venoactive compounds in the treatment of chronic venous disease},
  journal = {Journal of Vascular Surgery: Venous and Lymphatic Disorders},
  note    = {REF-0678},
  year    = {2025},
  doi     = {10.1016/j.jvsv.2025.102258},
  annote  = {Gloviczki, M.L., Kakkos, S.K., Urbanek, T., Chuback, J. and Nicolaides, A. (2025) 'The role of venoactive compounds in the treatment of chronic venous disease', Journal of Vascular Surgery: Venous and Lymphatic Disorders, 13(5), 102258. doi:10.1016/j.jvsv.2025.102258. [GRADE review: venoactive compounds, including horse chestnut seed extract, seal the endothelial barrier, enhance lymphatic drainage, reduce venous oedema and improve venous tone as part of chronic venous disease management.]}
}

""",
    "santiago2026venoactive": """@article{santiago2026venoactive,
  author  = {Santiago, F.R., Grillo, L., Amore, M., Carmelino, C., Trejo, J.M.R. and Ulloa, J.H.},
  title   = {Venoactive drugs in the management of chronic venous disease: A critical appraisal of the evidence and comparison with international guidelines},
  journal = {Vascular Pharmacology},
  note    = {REF-0679},
  year    = {2026},
  doi     = {10.1016/j.vph.2026.107614},
  annote  = {Santiago, F.R., Grillo, L., Amore, M., Carmelino, C., Trejo, J.M.R. and Ulloa, J.H. (2026) 'Venoactive drugs in the management of chronic venous disease: A critical appraisal of the evidence and comparison with international guidelines', Vascular Pharmacology, 163, 107614. doi:10.1016/j.vph.2026.107614. [Critical appraisal: venoactive drugs including horse chestnut seed extract reduce chronic-venous-disease symptoms such as pain, heaviness and oedema and improve quality of life by improving venous tone, reducing inflammation and enhancing microcirculation.]}
}

""",
    # ---- Agrimonia eupatoria (Agrimony) ----------------------------------
    "lee2016agrimonia": """@article{lee2016agrimonia,
  author  = {Lee, K.H. and Rhee, K.H.},
  title   = {Anti-nociceptive effect of Agrimonia eupatoria extract on a cisplatin-induced neuropathic model},
  journal = {African Journal of Traditional, Complementary and Alternative Medicines},
  note    = {REF-0680},
  year    = {2016},
  doi     = {10.21010/ajtcam.v13i5.18},
  annote  = {Lee, K.H. and Rhee, K.H. (2016) 'Anti-nociceptive effect of Agrimonia eupatoria extract on a cisplatin-induced neuropathic model', African Journal of Traditional, Complementary and Alternative Medicines, 13(5), pp. 139-144. doi:10.21010/ajtcam.v13i5.18. [In a cisplatin-induced neuropathy rat model, oral Agrimonia eupatoria extract (200 mg/kg) reduced mechanical and cold hypersensitivity, outperforming gabapentin across the pain tests used.]}
}

""",
    "malheiros2022agrimonia": """@article{malheiros2022agrimonia,
  author  = {Malheiros, J., Simoes, D.M., Figueirinha, A., Cotrim, M.D. and Fonseca, D.A.},
  title   = {Agrimonia eupatoria L.: An integrative perspective on ethnomedicinal use, phenolic composition and pharmacological activity},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0681},
  year    = {2022},
  doi     = {10.1016/j.jep.2022.115498},
  annote  = {Malheiros, J., Simoes, D.M., Figueirinha, A., Cotrim, M.D. and Fonseca, D.A. (2022) 'Agrimonia eupatoria L.: An integrative perspective on ethnomedicinal use, phenolic composition and pharmacological activity', Journal of Ethnopharmacology, 296, 115498. doi:10.1016/j.jep.2022.115498. [Review: A. eupatoria is rich in phenolic acids, flavonoids and tannins (e.g. agrimoniin, rutin, hyperoside) with antioxidant, antimicrobial, antidiabetic, antinociceptive and anti-inflammatory activity; two clinical studies of the infusion showed hepatoprotective and cardiovascular/metabolic benefits.]}
}

""",
    "vasilenko2022agrimonia": """@article{vasilenko2022agrimonia,
  author  = {Vasilenko, T., Kovac, I., Slezak, M., Durkac, J., Perzelova, V., Coma, M. and others},
  title   = {Agrimonia eupatoria L. aqueous extract improves skin wound healing: an in vitro study in fibroblasts and keratinocytes and in vivo study in rats},
  journal = {In Vivo},
  note    = {REF-0682},
  year    = {2022},
  doi     = {10.21873/invivo.12822},
  annote  = {Vasilenko, T., Kovac, I., Slezak, M., Durkac, J., Perzelova, V., Coma, M., et al. (2022) 'Agrimonia eupatoria L. aqueous extract improves skin wound healing: an in vitro study in fibroblasts and keratinocytes and in vivo study in rats', In Vivo, 36(3), pp. 1236-1244. doi:10.21873/invivo.12822. [The aqueous extract promoted fibroblast-to-myofibroblast conversion, extracellular-matrix deposition and keratinocyte activity in vitro, and significantly increased wound tensile strength and contraction of skin wounds in rats.]}
}

""",
    "paluch2020agrimonia": """@article{paluch2020agrimonia,
  author  = {Paluch, Z., Biriczova, L., Pallag, G., Carvalheiro Marques, E., Vargova, N. and Kmonickova, E.},
  title   = {The therapeutic effects of Agrimonia eupatoria L.},
  journal = {Physiological Research},
  note    = {REF-0683},
  year    = {2020},
  doi     = {10.33549/physiolres.934641},
  annote  = {Paluch, Z., Biriczova, L., Pallag, G., Carvalheiro Marques, E., Vargova, N. and Kmonickova, E. (2020) 'The therapeutic effects of Agrimonia eupatoria L.', Physiological Research, 69(Suppl 4), pp. S555-S571. doi:10.33549/physiolres.934641. [Review: A. eupatoria infusions and decoctions are used for airway, urinary and digestive complaints and chronic wounds; its tannins, flavonoids, phenolic acids and triterpenoids confer antioxidant, immunomodulatory and antimicrobial activity.]}
}

""",
    "shareef2025agrimonia": """@article{shareef2025agrimonia,
  author  = {Shareef, S.H., Asaad, N.K., Gheni, N.A., Fisal, D.N., Shakir Agha, N.F., Ali, R.T. and Abdulla, M.A.},
  title   = {Agrimonia eupatoria leaf extract attenuates alcohol-induced oxidative stress, ulcer and alleviates stomach damage in rats},
  journal = {Food Science and Nutrition},
  note    = {REF-0684},
  year    = {2025},
  doi     = {10.1002/fsn3.71203},
  annote  = {Shareef, S.H., Asaad, N.K., Gheni, N.A., Fisal, D.N., Shakir Agha, N.F., Ali, R.T. and Abdulla, M.A. (2025) 'Agrimonia eupatoria leaf extract attenuates alcohol-induced oxidative stress, ulcer and alleviates stomach damage in rats', Food Science and Nutrition, 13(11), e71203. doi:10.1002/fsn3.71203. [In a rat model of ethanol-induced gastric ulcer, A. eupatoria leaf extract reduced ulcer area, raised gastric mucus and pH, increased superoxide dismutase and catalase, and lowered malondialdehyde, showing gastroprotective and antioxidant activity.]}
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
