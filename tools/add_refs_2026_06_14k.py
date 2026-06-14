#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch K (named-plant priority).

User-requested priority enrichment of well-known but under-cited records, batch 1
of 2 for the named set:

    Zingiber officinale (Ginger)      -> REF-0634..REF-0639
    Hericium erinaceus (Lion's mane)  -> REF-0640..REF-0645
    Allium sativum (Garlic)           -> REF-0646..REF-0651

All sources are from PubMed (metadata via the PubMed MCP server: authors, title,
journal, year, DOI, findings drawn from the abstract). New BibTeX entries are
inserted at the correct alphabetical position by citation key; the YAML citations
are added by hand alongside this script and logged in each record's internal_notes.

Additive and idempotent: an entry whose REF id or citation key already exists is
skipped, so re-running changes nothing.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    # ---- Zingiber officinale (Ginger) -------------------------------------
    "crichton2023gingercinv": """@article{crichton2023gingercinv,
  author  = {Crichton, M., Marshall, S., Isenring, E., Lohning, A., McCarthy, A.L., Molassiotis, A. and others},
  title   = {Effect of a Standardized Ginger Root Powder Regimen on Chemotherapy-Induced Nausea and Vomiting: A Multicenter, Double-Blind, Placebo-Controlled Randomized Trial},
  journal = {Journal of the Academy of Nutrition and Dietetics},
  note    = {REF-0634},
  year    = {2023},
  doi     = {10.1016/j.jand.2023.09.003},
  annote  = {Crichton, M., Marshall, S., Isenring, E., Lohning, A., McCarthy, A.L., Molassiotis, A., et al. (2023) 'Effect of a Standardized Ginger Root Powder Regimen on Chemotherapy-Induced Nausea and Vomiting: A Multicenter, Double-Blind, Placebo-Controlled Randomized Trial', Journal of the Academy of Nutrition and Dietetics, 124(3), pp. 313-330. doi:10.1016/j.jand.2023.09.003. [RCT, n=103: 84 mg/day standardized gingerols/shogaols alongside antiemetics improved chemotherapy-induced nausea-related quality of life and reduced delayed nausea, vomiting and fatigue, with no serious adverse events.]}
}

""",
    "hu2020gingerpregnancy": """@article{hu2020gingerpregnancy,
  author  = {Hu, Y., Amoah, A.N., Zhang, H., Fu, R., Qiu, Y., Cao, Y. and others},
  title   = {Effect of ginger in the treatment of nausea and vomiting compared with vitamin B6 and placebo during pregnancy: a meta-analysis},
  journal = {Journal of Maternal-Fetal and Neonatal Medicine},
  note    = {REF-0635},
  year    = {2020},
  doi     = {10.1080/14767058.2020.1712714},
  annote  = {Hu, Y., Amoah, A.N., Zhang, H., Fu, R., Qiu, Y., Cao, Y., et al. (2020) 'Effect of ginger in the treatment of nausea and vomiting compared with vitamin B6 and placebo during pregnancy: a meta-analysis', Journal of Maternal-Fetal and Neonatal Medicine, 35(1), pp. 187-196. doi:10.1080/14767058.2020.1712714. [Meta-analysis of 13 RCTs (1174 women): ginger significantly relieved general symptoms and nausea severity of pregnancy versus placebo, and was at least as effective as vitamin B6.]}
}

""",
    "xu2020cinnamonfennelginger": """@article{xu2020cinnamonfennelginger,
  author  = {Xu, Y., Yang, Q. and Wang, X.},
  title   = {Efficacy of herbal medicine (cinnamon/fennel/ginger) for primary dysmenorrhea: a systematic review and meta-analysis of randomized controlled trials},
  journal = {Journal of International Medical Research},
  note    = {REF-0636},
  year    = {2020},
  doi     = {10.1177/0300060520936179},
  annote  = {Xu, Y., Yang, Q. and Wang, X. (2020) 'Efficacy of herbal medicine (cinnamon/fennel/ginger) for primary dysmenorrhea: a systematic review and meta-analysis of randomized controlled trials', Journal of International Medical Research, 48(6). doi:10.1177/0300060520936179. [Meta-analysis (9 RCTs, 647 patients): ginger, cinnamon and fennel each significantly reduced primary dysmenorrhoea pain intensity versus placebo, and cinnamon shortened pain duration.]}
}

""",
    "mathieu2022osteoarthritis": """@article{mathieu2022osteoarthritis,
  author  = {Mathieu, S., Soubrier, M., Peirs, C., Monfoulet, L.E., Boirie, Y. and Tournadre, A.},
  title   = {A Meta-Analysis of the Impact of Nutritional Supplementation on Osteoarthritis Symptoms},
  journal = {Nutrients},
  note    = {REF-0637},
  year    = {2022},
  doi     = {10.3390/nu14081607},
  annote  = {Mathieu, S., Soubrier, M., Peirs, C., Monfoulet, L.E., Boirie, Y. and Tournadre, A. (2022) 'A Meta-Analysis of the Impact of Nutritional Supplementation on Osteoarthritis Symptoms', Nutrients, 14(8), 1607. doi:10.3390/nu14081607. [Meta-analysis: across three trials (166 vs 164 controls) ginger significantly decreased osteoarthritis pain, with a significant reduction in inflammatory markers.]}
}

""",
    "zhang2025kneeosteoarthritis": """@article{zhang2025kneeosteoarthritis,
  author  = {Zhang, Y., Gui, Y., Adams, R., Farragher, J., Itsiopoulos, C., Bow, K. and others},
  title   = {Comparative Effectiveness of Nutritional Supplements in the Treatment of Knee Osteoarthritis: A Network Meta-Analysis},
  journal = {Nutrients},
  note    = {REF-0638},
  year    = {2025},
  doi     = {10.3390/nu17152547},
  annote  = {Zhang, Y., Gui, Y., Adams, R., Farragher, J., Itsiopoulos, C., Bow, K., et al. (2025) 'Comparative Effectiveness of Nutritional Supplements in the Treatment of Knee Osteoarthritis: A Network Meta-Analysis', Nutrients, 17(15), 2547. doi:10.3390/nu17152547. [Network meta-analysis of 39 RCTs (4599 patients): ginger, alongside Boswellia, curcumin, collagen and krill oil, showed benefit for knee osteoarthritis symptoms without increased adverse events.]}
}

""",
    "huang2019gingerdiabetes": """@article{huang2019gingerdiabetes,
  author  = {Huang, F.Y., Deng, T., Meng, L.X. and Ma, X.L.},
  title   = {Dietary ginger as a traditional therapy for blood sugar control in patients with type 2 diabetes mellitus: A systematic review and meta-analysis},
  journal = {Medicine (Baltimore)},
  note    = {REF-0639},
  year    = {2019},
  doi     = {10.1097/MD.0000000000015054},
  annote  = {Huang, F.Y., Deng, T., Meng, L.X. and Ma, X.L. (2019) 'Dietary ginger as a traditional therapy for blood sugar control in patients with type 2 diabetes mellitus: A systematic review and meta-analysis', Medicine (Baltimore), 98(13), e15054. doi:10.1097/MD.0000000000015054. [Meta-analysis of 8 RCTs (454 patients with type 2 diabetes): ginger (1.6-4 g/day) significantly improved HbA1c, indicating benefit for longer-term glycaemic control.]}
}

""",
    # ---- Hericium erinaceus (Lion's mane) --------------------------------
    "docherty2023lionsmane": """@article{docherty2023lionsmane,
  author  = {Docherty, S., Doughty, F.L. and Smith, E.F.},
  title   = {The Acute and Chronic Effects of Lion's Mane Mushroom Supplementation on Cognitive Function, Stress and Mood in Young Adults: A Double-Blind, Parallel Groups, Pilot Study},
  journal = {Nutrients},
  note    = {REF-0640},
  year    = {2023},
  doi     = {10.3390/nu15224842},
  annote  = {Docherty, S., Doughty, F.L. and Smith, E.F. (2023) 'The Acute and Chronic Effects of Lions Mane Mushroom Supplementation on Cognitive Function, Stress and Mood in Young Adults: A Double-Blind, Parallel Groups, Pilot Study', Nutrients, 15(22), 4842. doi:10.3390/nu15224842. [Randomized controlled pilot (n=41): a single 1.8 g dose of Hericium erinaceus sped Stroop-task performance at 60 min, with a trend toward reduced subjective stress after 28 days.]}
}

""",
    "surendran2025lionsmane": """@article{surendran2025lionsmane,
  author  = {Surendran, G., Saye, J., Binti Mohd Jalil, S., Spreadborough, J., Duong, K., Shatwan, I.M. and others},
  title   = {Acute effects of a standardised extract of Hericium erinaceus (Lion's Mane mushroom) on cognition and mood in healthy younger adults: a double-blind randomised placebo-controlled study},
  journal = {Frontiers in Nutrition},
  note    = {REF-0641},
  year    = {2025},
  doi     = {10.3389/fnut.2025.1405796},
  annote  = {Surendran, G., Saye, J., Binti Mohd Jalil, S., Spreadborough, J., Duong, K., Shatwan, I.M., et al. (2025) 'Acute effects of a standardised extract of Hericium erinaceus (Lions Mane mushroom) on cognition and mood in healthy younger adults: a double-blind randomised placebo-controlled study', Frontiers in Nutrition, 12, 1405796. doi:10.3389/fnut.2025.1405796. [Acute crossover RCT (n=18): a single 3 g dose of fruiting-body extract improved psychomotor (pegboard) performance 90 min post-dose, while global cognition and mood were unchanged.]}
}

""",
    "szucko2023hericium": """@article{szucko2023hericium,
  author  = {Szucko-Kociuba, I., Trzeciak-Ryczek, A., Kupnicka, P. and Chlubek, D.},
  title   = {Neurotrophic and Neuroprotective Effects of Hericium erinaceus},
  journal = {International Journal of Molecular Sciences},
  note    = {REF-0642},
  year    = {2023},
  doi     = {10.3390/ijms242115960},
  annote  = {Szucko-Kociuba, I., Trzeciak-Ryczek, A., Kupnicka, P. and Chlubek, D. (2023) 'Neurotrophic and Neuroprotective Effects of Hericium erinaceus', International Journal of Molecular Sciences, 24(21), 15960. doi:10.3390/ijms242115960. [Review: the mushroom's erinacines and hericenones stimulate nerve growth factor release, regulate inflammation, reduce oxidative stress and protect neurons from apoptosis.]}
}

""",
    "li2024hericiumcolitis": """@article{li2024hericiumcolitis,
  author  = {Li, H., Feng, J., Liu, C., Hou, S., Meng, J., Liu, J.Y. and others},
  title   = {Polysaccharides from an edible mushroom, Hericium erinaceus, alleviate ulcerative colitis in mice by inhibiting the NLRP3 inflammasomes and reestablish intestinal homeostasis},
  journal = {International Journal of Biological Macromolecules},
  note    = {REF-0643},
  year    = {2024},
  doi     = {10.1016/j.ijbiomac.2024.131251},
  annote  = {Li, H., Feng, J., Liu, C., Hou, S., Meng, J., Liu, J.Y., et al. (2024) 'Polysaccharides from an edible mushroom, Hericium erinaceus, alleviate ulcerative colitis in mice by inhibiting the NLRP3 inflammasomes and reestablish intestinal homeostasis', International Journal of Biological Macromolecules, 267(Pt 1), 131251. doi:10.1016/j.ijbiomac.2024.131251. [Fruiting-body polysaccharides reduced colonic IL-6, IL-1-beta and TNF-alpha and oxidative damage, suppressed the NLRP3 inflammasome/caspase-1 pathway, and restored gut microbiota in a mouse ulcerative-colitis model.]}
}

""",
    "shi2024hericiummacrophage": """@article{shi2024hericiummacrophage,
  author  = {Shi, X.Z., Zhang, X.Y., Wang, Y.Y., Zhao, Y.M. and Wang, J.},
  title   = {Polysaccharides from Hericium erinaceus and its immunomodulatory effects on RAW 264.7 macrophages},
  journal = {International Journal of Biological Macromolecules},
  note    = {REF-0644},
  year    = {2024},
  doi     = {10.1016/j.ijbiomac.2024.134947},
  annote  = {Shi, X.Z., Zhang, X.Y., Wang, Y.Y., Zhao, Y.M. and Wang, J. (2024) 'Polysaccharides from Hericium erinaceus and its immunomodulatory effects on RAW 264.7 macrophages', International Journal of Biological Macromolecules, 278(Pt 3), 134947. doi:10.1016/j.ijbiomac.2024.134947. [Optimised-extraction H. erinaceus polysaccharides enhanced macrophage immune activity, increasing production of IL-6 and TNF-alpha.]}
}

""",
    "pellegrino2025hericiumgastritis": """@article{pellegrino2025hericiumgastritis,
  author  = {Pellegrino, R. and Gravina, A.G.},
  title   = {Potential of traditional Chinese medicine in gastrointestinal disorders: Hericium erinaceus in chronic atrophic gastritis},
  journal = {World Journal of Gastroenterology},
  note    = {REF-0645},
  year    = {2025},
  doi     = {10.3748/wjg.v31.i20.106615},
  annote  = {Pellegrino, R. and Gravina, A.G. (2025) 'Potential of traditional Chinese medicine in gastrointestinal disorders: Hericium erinaceus in chronic atrophic gastritis', World Journal of Gastroenterology, 31(20), 106615. doi:10.3748/wjg.v31.i20.106615. [Commentary: early clinical data suggest H. erinaceus induces clinical and histological improvement in chronic atrophic gastritis with antimicrobial activity against Helicobacter pylori; erinacine A and S show antineoplastic activity in gastric carcinogenesis.]}
}

""",
    # ---- Allium sativum (Garlic) -----------------------------------------
    "ried2016garlicbloodpressure": """@article{ried2016garlicbloodpressure,
  author  = {Ried, K.},
  title   = {Garlic Lowers Blood Pressure in Hypertensive Individuals, Regulates Serum Cholesterol, and Stimulates Immunity: An Updated Meta-analysis and Review},
  journal = {Journal of Nutrition},
  note    = {REF-0646},
  year    = {2016},
  doi     = {10.3945/jn.114.202192},
  annote  = {Ried, K. (2016) 'Garlic Lowers Blood Pressure in Hypertensive Individuals, Regulates Serum Cholesterol, and Stimulates Immunity: An Updated Meta-analysis and Review', Journal of Nutrition, 146(2), pp. 389S-396S. doi:10.3945/jn.114.202192. [Meta-analysis of 20 trials (970 participants): garlic lowered systolic blood pressure by ~8.7 mmHg in hypertensive subjects, reduced total/LDL cholesterol by ~10%, and stimulated immune function (fewer, shorter upper-respiratory infections).]}
}

""",
    "sleiman2024garlichypertension": """@article{sleiman2024garlichypertension,
  author  = {Sleiman, C., Daou, R.M., Al Hazzouri, A., Hamdan, Z., Ghadieh, H.E., Harbieh, B. and Romani, M.},
  title   = {Garlic and Hypertension: Efficacy, Mechanism of Action, and Clinical Implications},
  journal = {Nutrients},
  note    = {REF-0647},
  year    = {2024},
  doi     = {10.3390/nu16172895},
  annote  = {Sleiman, C., Daou, R.M., Al Hazzouri, A., Hamdan, Z., Ghadieh, H.E., Harbieh, B. and Romani, M. (2024) 'Garlic and Hypertension: Efficacy, Mechanism of Action, and Clinical Implications', Nutrients, 16(17), 2895. doi:10.3390/nu16172895. [Review: garlic modestly lowers blood pressure, especially in mild hypertension, via allicin- and ajoene-driven increases in nitric oxide, improved endothelial function and antioxidant effects; not a substitute for antihypertensive drugs.]}
}

""",
    "imaizumi2022garliccardiovascular": """@article{imaizumi2022garliccardiovascular,
  author  = {Imaizumi, V.M., Laurindo, L.F., Manzan, B., Guiguer, E.L., Oshiiwa, M., Otoboni, A.M.M.B. and others},
  title   = {Garlic: A systematic review of the effects on cardiovascular diseases},
  journal = {Critical Reviews in Food Science and Nutrition},
  note    = {REF-0648},
  year    = {2022},
  doi     = {10.1080/10408398.2022.2043821},
  annote  = {Imaizumi, V.M., Laurindo, L.F., Manzan, B., Guiguer, E.L., Oshiiwa, M., Otoboni, A.M.M.B., et al. (2022) 'Garlic: A systematic review of the effects on cardiovascular diseases', Critical Reviews in Food Science and Nutrition, 63(24), pp. 6797-6819. doi:10.1080/10408398.2022.2043821. [Systematic review: garlic reduced blood pressure, waist circumference, BMI, LDL/total cholesterol, triglycerides and inflammatory markers and raised HDL, improving multiple cardiovascular risk factors.]}
}

""",
    "serrano2023agedgarlic": """@article{serrano2023agedgarlic,
  author  = {Serrano, J.C.E., Castro-Boque, E., Garcia-Carrasco, A., Moran-Valero, M.I., Gonzalez-Hedstrom, D., Bermudez-Lopez, M. and others},
  title   = {Antihypertensive Effects of an Optimized Aged Garlic Extract in Subjects with Grade I Hypertension and Antihypertensive Drug Therapy: A Randomized, Triple-Blind Controlled Trial},
  journal = {Nutrients},
  note    = {REF-0649},
  year    = {2023},
  doi     = {10.3390/nu15173691},
  annote  = {Serrano, J.C.E., Castro-Boque, E., Garcia-Carrasco, A., Moran-Valero, M.I., Gonzalez-Hedstrom, D., Bermudez-Lopez, M., et al. (2023) 'Antihypertensive Effects of an Optimized Aged Garlic Extract in Subjects with Grade I Hypertension and Antihypertensive Drug Therapy: A Randomized, Triple-Blind Controlled Trial', Nutrients, 15(17), 3691. doi:10.3390/nu15173691. [12-week RCT: aged black garlic extract (0.25 mg/day S-allyl-cysteine) gave an additional reduction in systolic and diastolic blood pressure, raised blood nitric oxide and antioxidant capacity, and lowered ACE activity in treated Grade I hypertensives.]}
}

""",
    "choo2020allicin": """@article{choo2020allicin,
  author  = {Choo, S., Chin, V.K., Wong, E.H., Madhavan, P., Tay, S.T., Yong, P.V.C. and Chong, P.P.},
  title   = {Review: antimicrobial properties of allicin used alone or in combination with other medications},
  journal = {Folia Microbiologica},
  note    = {REF-0650},
  year    = {2020},
  doi     = {10.1007/s12223-020-00786-5},
  annote  = {Choo, S., Chin, V.K., Wong, E.H., Madhavan, P., Tay, S.T., Yong, P.V.C. and Chong, P.P. (2020) 'Review: antimicrobial properties of allicin used alone or in combination with other medications', Folia Microbiologica, 65(3), pp. 451-465. doi:10.1007/s12223-020-00786-5. [Review: allicin from raw garlic inhibits a broad range of bacteria and fungi by targeting thiol-containing enzymes, and enhances the activity of conventional antibiotics and antifungals when combined.]}
}

""",
    "reiter2017allicin": """@article{reiter2017allicin,
  author  = {Reiter, J., Levina, N., van der Linden, M., Gruhlke, M., Martin, C. and Slusarenko, A.J.},
  title   = {Diallylthiosulfinate (Allicin), a Volatile Antimicrobial from Garlic (Allium sativum), Kills Human Lung Pathogenic Bacteria, Including MDR Strains, as a Vapor},
  journal = {Molecules},
  note    = {REF-0651},
  year    = {2017},
  doi     = {10.3390/molecules22101711},
  annote  = {Reiter, J., Levina, N., van der Linden, M., Gruhlke, M., Martin, C. and Slusarenko, A.J. (2017) 'Diallylthiosulfinate (Allicin), a Volatile Antimicrobial from Garlic (Allium sativum), Kills Human Lung Pathogenic Bacteria, Including MDR Strains, as a Vapor', Molecules, 22(10), 1711. doi:10.3390/molecules22101711. [Allicin inhibited clinical lung pathogens, including multidrug-resistant strains, both in solution and as a vapour; cytotoxicity to human cells was ameliorated by glutathione, supporting potential inhalational use.]}
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
