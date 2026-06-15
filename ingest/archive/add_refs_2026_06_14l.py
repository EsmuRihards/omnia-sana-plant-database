#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch L (named-plant priority, 2/2).

Second half of the user-requested named set:

    Cuminum cyminum (Cumin)        -> REF-0652..REF-0657
    Prunella vulgaris (Selfheal)   -> REF-0658..REF-0663
    Cinnamomum verum (Cinnamon)    -> REF-0664..REF-0669

All sources from PubMed (metadata via the PubMed MCP server). New BibTeX entries
are inserted alphabetically by citation key; YAML citations are added by hand and
logged in each record's internal_notes. Additive and idempotent.

Notes on honest scope:
- Cumin's glycaemic evidence is mixed: a positive meta-analysis (REF-0653) and a
  null meta-analysis (REF-0654) are both cited so the record reflects the conflict.
- Some cinnamon sources pool species or study C. cassia (REF-0668); the record is
  C. verum (Ceylon). Cinnamaldehyde is shared across the genus; coumarin content,
  the key safety difference, is far lower in C. verum than C. cassia.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    # ---- Cuminum cyminum (Cumin) -----------------------------------------
    "hadi2018cuminlipid": """@article{hadi2018cuminlipid,
  author  = {Hadi, A., Mohammadi, H., Hadi, Z., Roshanravan, N. and Kafeshani, M.},
  title   = {Cumin (Cuminum cyminum L.) is a safe approach for management of lipid parameters: A systematic review and meta-analysis of randomized controlled trials},
  journal = {Phytotherapy Research},
  note    = {REF-0652},
  year    = {2018},
  doi     = {10.1002/ptr.6162},
  annote  = {Hadi, A., Mohammadi, H., Hadi, Z., Roshanravan, N. and Kafeshani, M. (2018) 'Cumin (Cuminum cyminum L.) is a safe approach for management of lipid parameters: A systematic review and meta-analysis of randomized controlled trials', Phytotherapy Research, 32(11), pp. 2146-2154. doi:10.1002/ptr.6162. [Meta-analysis of 6 RCTs (376 adults): cumin supplementation significantly lowered total and LDL cholesterol and raised HDL cholesterol.]}
}

""",
    "tavakoli2021cuminglycemic": """@article{tavakoli2021cuminglycemic,
  author  = {Tavakoli-Rouzbehani, O.M., Faghfouri, A.H., Anbari, M., Papi, S., Shojaei, F.S., Ghaffari, M. and Alizadeh, M.},
  title   = {The effects of Cuminum cyminum on glycemic parameters: A systematic review and meta-analysis of controlled clinical trials},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0653},
  year    = {2021},
  doi     = {10.1016/j.jep.2021.114510},
  annote  = {Tavakoli-Rouzbehani, O.M., Faghfouri, A.H., Anbari, M., Papi, S., Shojaei, F.S., Ghaffari, M. and Alizadeh, M. (2021) 'The effects of Cuminum cyminum on glycemic parameters: A systematic review and meta-analysis of controlled clinical trials', Journal of Ethnopharmacology, 281, 114510. doi:10.1016/j.jep.2021.114510. [Meta-analysis of 8 trials: cumin significantly reduced fasting blood sugar and HbA1c and improved insulin sensitivity (QUICKI).]}
}

""",
    "karimian2021cuminglycemic": """@article{karimian2021cuminglycemic,
  author  = {Karimian, J., Farrokhzad, A. and Jalili, C.},
  title   = {The effect of cumin (Cuminum cyminum L.) supplementation on glycemic indices: A systematic review and meta-analysis of randomized controlled trials},
  journal = {Phytotherapy Research},
  note    = {REF-0654},
  year    = {2021},
  doi     = {10.1002/ptr.7075},
  annote  = {Karimian, J., Farrokhzad, A. and Jalili, C. (2021) 'The effect of cumin (Cuminum cyminum L.) supplementation on glycemic indices: A systematic review and meta-analysis of randomized controlled trials', Phytotherapy Research, 35(8), pp. 4127-4135. doi:10.1002/ptr.7075. [Meta-analysis of 8 RCTs (552 adults): cumin did not significantly change fasting blood sugar, insulin or HOMA-IR - evidence on glycaemic benefit is mixed.]}
}

""",
    "morovati2019cuminmetabolic": """@article{morovati2019cuminmetabolic,
  author  = {Morovati, A., Pourghassem Gargari, B. and Sarbakhsh, P.},
  title   = {Effects of cumin (Cuminum cyminum L.) essential oil supplementation on metabolic syndrome components: A randomized, triple-blind, placebo-controlled clinical trial},
  journal = {Phytotherapy Research},
  note    = {REF-0655},
  year    = {2019},
  doi     = {10.1002/ptr.6500},
  annote  = {Morovati, A., Pourghassem Gargari, B. and Sarbakhsh, P. (2019) 'Effects of cumin (Cuminum cyminum L.) essential oil supplementation on metabolic syndrome components: A randomized, triple-blind, placebo-controlled clinical trial', Phytotherapy Research, 33(12), pp. 3261-3269. doi:10.1002/ptr.6500. [8-week RCT in metabolic-syndrome patients: cumin essential oil (225 mg/day) significantly lowered diastolic blood pressure versus placebo, with no significant change in the other components.]}
}

""",
    "amin2024cuminbowel": """@article{amin2024cuminbowel,
  author  = {Amin, E.A., Ismail, E., Mahboobeh, R. and Tabandeh, S.},
  title   = {The effect of Cuminum cyminum on the return of bowel motility after abdominal surgery: a triple-blind randomized clinical trial},
  journal = {BMC Complementary Medicine and Therapies},
  note    = {REF-0656},
  year    = {2024},
  doi     = {10.1186/s12906-024-04530-1},
  annote  = {Amin, E.A., Ismail, E., Mahboobeh, R. and Tabandeh, S. (2024) 'The effect of Cuminum cyminum on the return of bowel motility after abdominal surgery: a triple-blind randomized clinical trial', BMC Complementary Medicine and Therapies, 24(1), 254. doi:10.1186/s12906-024-04530-1. [Triple-blind RCT (74 patients): Cuminum cyminum extract after abdominal surgery shortened the time to first flatus and defecation and significantly reduced abdominal pain, bloating, nausea and vomiting.]}
}

""",
    "benmiri2018cuminaflatoxin": """@article{benmiri2018cuminaflatoxin,
  author  = {Ben Miri, Y. and Djenane, D.},
  title   = {Evaluation of Protective Impact of Algerian Cuminum cyminum L. and Coriandrum sativum L. Essential Oils on Aspergillus flavus Growth and Aflatoxin B1 Production},
  journal = {Pakistan Journal of Biological Sciences},
  note    = {REF-0657},
  year    = {2018},
  doi     = {10.3923/pjbs.2018.67.77},
  annote  = {Ben Miri, Y. and Djenane, D. (2018) 'Evaluation of Protective Impact of Algerian Cuminum cyminum L. and Coriandrum sativum L. Essential Oils on Aspergillus flavus Growth and Aflatoxin B1 Production', Pakistan Journal of Biological Sciences, 21(2), pp. 67-77. doi:10.3923/pjbs.2018.67.77. [C. cyminum essential oil - dominated by cuminaldehyde (about 66 percent of the oil) - inhibited Aspergillus flavus growth and completely suppressed aflatoxin B1 production at 1.25 mg/mL, and showed DPPH radical-scavenging antioxidant activity.]}
}

""",
    # ---- Prunella vulgaris (Selfheal) ------------------------------------
    "haarberg2015prunellacolitis": """@article{haarberg2015prunellacolitis,
  author  = {Haarberg, K.M.K., Wymore Brand, M.J., Overstreet, A.M.C., Hauck, C.C., Murphy, P.A., Hostetter, J.M., Ramer-Tait, A.E. and Wannemuehler, M.J.},
  title   = {Orally administered extract from Prunella vulgaris attenuates spontaneous colitis in mdr1a(-/-) mice},
  journal = {World Journal of Gastrointestinal Pharmacology and Therapeutics},
  note    = {REF-0658},
  year    = {2015},
  doi     = {10.4292/wjgpt.v6.i4.223},
  annote  = {Haarberg, K.M.K., Wymore Brand, M.J., Overstreet, A.M.C., Hauck, C.C., Murphy, P.A., Hostetter, J.M., Ramer-Tait, A.E. and Wannemuehler, M.J. (2015) 'Orally administered extract from Prunella vulgaris attenuates spontaneous colitis in mdr1a(-/-) mice', World Journal of Gastrointestinal Pharmacology and Therapeutics, 6(4), pp. 223-237. doi:10.4292/wjgpt.v6.i4.223. [A P. vulgaris ethanolic extract delayed onset and reduced severity of spontaneous colitis in mice, lowering serum TNF-alpha and CXCL9, colonic myeloperoxidase and mucosal inflammation.]}
}

""",
    "mir2022prunellareview": """@article{mir2022prunellareview,
  author  = {Mir, R.H., Bhat, M.F., Sawhney, G., Kumar, P., Andrabi, N.I., Shaikh, M., Mohi-Ud-Din, R. and Masoodi, M.H.},
  title   = {Prunella vulgaris L.: Critical Pharmacological, Expository Traditional Uses and Extensive Phytochemistry: A Review},
  journal = {Current Drug Discovery Technologies},
  note    = {REF-0659},
  year    = {2022},
  doi     = {10.2174/1570163818666210203181542},
  annote  = {Mir, R.H., Bhat, M.F., Sawhney, G., Kumar, P., Andrabi, N.I., Shaikh, M., Mohi-Ud-Din, R. and Masoodi, M.H. (2022) 'Prunella vulgaris L.: Critical Pharmacological, Expository Traditional Uses and Extensive Phytochemistry: A Review', Current Drug Discovery Technologies, 19(1), e140122191102. doi:10.2174/1570163818666210203181542. [Review: self-heal contains triterpenoids (ursolic, oleanolic and betulinic acids), phenolic acids (rosmarinic acid), coumarins (umbelliferone, scopoletin, esculetin), sterols and flavonoids (luteolin), underpinning antimicrobial, immunomodulatory, anti-cancer, cardioprotective and anti-inflammatory activity.]}
}

""",
    "zhong2024prunellahsv": """@article{zhong2024prunellahsv,
  author  = {Zhong, X., Zhang, Y., Yuan, M., Xu, L., Luo, X., Wu, R., Xi, Z., Li, Y. and Xu, H.},
  title   = {Prunella vulgaris polysaccharide inhibits herpes simplex virus infection by blocking TLR-mediated NF-kB activation},
  journal = {Chinese Medicine},
  note    = {REF-0660},
  year    = {2024},
  doi     = {10.1186/s13020-023-00865-y},
  annote  = {Zhong, X., Zhang, Y., Yuan, M., Xu, L., Luo, X., Wu, R., Xi, Z., Li, Y. and Xu, H. (2024) 'Prunella vulgaris polysaccharide inhibits herpes simplex virus infection by blocking TLR-mediated NF-kB activation', Chinese Medicine, 19(1), 6. doi:10.1186/s13020-023-00865-y. [The polysaccharide PVE30 competed with heparan sulfate for HSV glycoproteins gB and gC to block viral attachment, downregulated viral genes, and suppressed TLR2/TLR3-NF-kB signalling with reduced IL-6 and TNF-alpha.]}
}

""",
    "zhang2021prunellahsv": """@article{zhang2021prunellahsv,
  author  = {Zhang, Q., Li, Y., Zhong, X., Fu, W., Luo, X., Feng, J., Yuan, M., Xiao, L. and Xu, H.},
  title   = {Polyphenolic-protein-polysaccharide conjugates from Spica of Prunella vulgaris: Chemical profile and anti-herpes simplex virus activities},
  journal = {International Journal of Biological Macromolecules},
  note    = {REF-0661},
  year    = {2021},
  doi     = {10.1016/j.ijbiomac.2021.11.200},
  annote  = {Zhang, Q., Li, Y., Zhong, X., Fu, W., Luo, X., Feng, J., Yuan, M., Xiao, L. and Xu, H. (2021) 'Polyphenolic-protein-polysaccharide conjugates from Spica of Prunella vulgaris: Chemical profile and anti-herpes simplex virus activities', International Journal of Biological Macromolecules. doi:10.1016/j.ijbiomac.2021.11.200. [Polyphenolic-protein-polysaccharide conjugates (PVG, about 41.7 kDa) inhibited HSV, including acyclovir-resistant strains, more potently than acyclovir in vitro.]}
}

""",
    "ma2016prunellapolysaccharide": """@article{ma2016prunellapolysaccharide,
  author  = {Ma, F.W., Kong, S.Y., Tan, H.S., Wu, R., Xia, B., Zhou, Y. and Xu, H.X.},
  title   = {Structural characterization and antiviral effect of a novel polysaccharide PSP-2B from Prunellae Spica},
  journal = {Carbohydrate Polymers},
  note    = {REF-0662},
  year    = {2016},
  doi     = {10.1016/j.carbpol.2016.07.062},
  annote  = {Ma, F.W., Kong, S.Y., Tan, H.S., Wu, R., Xia, B., Zhou, Y. and Xu, H.X. (2016) 'Structural characterization and antiviral effect of a novel polysaccharide PSP-2B from Prunellae Spica', Carbohydrate Polymers, 152, pp. 699-709. doi:10.1016/j.carbpol.2016.07.062. [PSP-2B, a partially sulphated arabinogalactomannan (about 32 kDa), inhibited HSV-1 (IC50 about 69 ug/mL) and HSV-2 (about 49 ug/mL) with no cytotoxicity up to 1600 ug/mL.]}
}

""",
    "zhang2025prunellasting": """@article{zhang2025prunellasting,
  author  = {Zhang, Y.B., Xu, L., Yuan, M., Liu, M.F., Li, Y., Zhong, X.L., Lin, Z.X., Xian, Y.F., Lu, P., Xi, Z.C. and Xu, H.X.},
  title   = {Protective effects of Prunella vulgaris polysaccharides against herpes simplex virus type 1 infection through the STING-TBK1-IRF3 pathway},
  journal = {Journal of Integrative Medicine},
  note    = {REF-0663},
  year    = {2025},
  doi     = {10.1016/j.joim.2025.12.008},
  annote  = {Zhang, Y.B., Xu, L., Yuan, M., Liu, M.F., Li, Y., Zhong, X.L., Lin, Z.X., Xian, Y.F., Lu, P., Xi, Z.C. and Xu, H.X. (2025) 'Protective effects of Prunella vulgaris polysaccharides against herpes simplex virus type 1 infection through the STING-TBK1-IRF3 pathway', Journal of Integrative Medicine, 24(3), pp. 454-465. doi:10.1016/j.joim.2025.12.008. [PVE30 pre-treatment protected human keratinocytes from HSV-1 by enhancing STING-TBK1-IRF3-mediated innate immunity, raising IFN-beta and interferon-stimulated genes and reducing viral load.]}
}

""",
    # ---- Cinnamomum verum (Cinnamon) -------------------------------------
    "moridpour2023cinnamonglycemic": """@article{moridpour2023cinnamonglycemic,
  author  = {Moridpour, A.H., Kavyani, Z., Khosravi, S., Farmani, E., Daneshvar, M., Musazadeh, V. and Faghfouri, A.H.},
  title   = {The effect of cinnamon supplementation on glycemic control in patients with type 2 diabetes mellitus: An updated systematic review and dose-response meta-analysis of randomized controlled trials},
  journal = {Phytotherapy Research},
  note    = {REF-0664},
  year    = {2023},
  doi     = {10.1002/ptr.8026},
  annote  = {Moridpour, A.H., Kavyani, Z., Khosravi, S., Farmani, E., Daneshvar, M., Musazadeh, V. and Faghfouri, A.H. (2023) 'The effect of cinnamon supplementation on glycemic control in patients with type 2 diabetes mellitus: An updated systematic review and dose-response meta-analysis of randomized controlled trials', Phytotherapy Research, 38(1), pp. 117-130. doi:10.1002/ptr.8026. [Meta-analysis of 24 RCTs: cinnamon significantly reduced fasting blood sugar, HOMA-IR and HbA1c in patients with type 2 diabetes.]}
}

""",
    "demoura2025cinnamonmetabolic": """@article{demoura2025cinnamonmetabolic,
  author  = {de Moura, S.L., Gomes, B.G.R., Guilarducci, M.J., Coelho, O.G.L., Guimaraes, N.S. and Gomes, J.M.G.},
  title   = {Effects of cinnamon supplementation on metabolic biomarkers in individuals with type 2 diabetes: a systematic review and meta-analysis},
  journal = {Nutrition Reviews},
  note    = {REF-0665},
  year    = {2025},
  doi     = {10.1093/nutrit/nuae058},
  annote  = {de Moura, S.L., Gomes, B.G.R., Guilarducci, M.J., Coelho, O.G.L., Guimaraes, N.S. and Gomes, J.M.G. (2025) 'Effects of cinnamon supplementation on metabolic biomarkers in individuals with type 2 diabetes: a systematic review and meta-analysis', Nutrition Reviews, 83(2), pp. 249-279. doi:10.1093/nutrit/nuae058. [Meta-analysis of 28 RCTs (3054 patients): cinnamon reduced fasting and postprandial glucose, HbA1c and HOMA-IR; in capsule form it also lowered total cholesterol, LDL and triglycerides.]}
}

""",
    "maierean2017cinnamonlipid": """@article{maierean2017cinnamonlipid,
  author  = {Maierean, S.M., Serban, M.C., Sahebkar, A., Ursoniu, S., Serban, A., Penson, P. and Banach, M.},
  title   = {The effects of cinnamon supplementation on blood lipid concentrations: A systematic review and meta-analysis},
  journal = {Journal of Clinical Lipidology},
  note    = {REF-0666},
  year    = {2017},
  doi     = {10.1016/j.jacl.2017.08.004},
  annote  = {Maierean, S.M., Serban, M.C., Sahebkar, A., Ursoniu, S., Serban, A., Penson, P. and Banach, M. (2017) 'The effects of cinnamon supplementation on blood lipid concentrations: A systematic review and meta-analysis', Journal of Clinical Lipidology, 11(6), pp. 1393-1406. doi:10.1016/j.jacl.2017.08.004. [Meta-analysis of 13 RCTs (750 participants): cinnamon significantly reduced blood triglycerides and total cholesterol, with no significant change in LDL or HDL.]}
}

""",
    "jafari2025cinnamoncardiovascular": """@article{jafari2025cinnamoncardiovascular,
  author  = {Jafari, A., Mardani, H., Faghfouri, A.H., AhmadianMoghaddam, M., Musazadeh, V. and Alaghi, A.},
  title   = {The effect of cinnamon supplementation on cardiovascular risk factors in adults: a GRADE assessed systematic review, dose-response and meta-analysis of randomized controlled trials},
  journal = {Journal of Health, Population and Nutrition},
  note    = {REF-0667},
  year    = {2025},
  doi     = {10.1186/s41043-025-00967-3},
  annote  = {Jafari, A., Mardani, H., Faghfouri, A.H., AhmadianMoghaddam, M., Musazadeh, V. and Alaghi, A. (2025) 'The effect of cinnamon supplementation on cardiovascular risk factors in adults: a GRADE assessed systematic review, dose-response and meta-analysis of randomized controlled trials', Journal of Health, Population and Nutrition, 44(1), 233. doi:10.1186/s41043-025-00967-3. [Meta-analysis of 49 RCTs: cinnamon improved waist circumference, systolic and diastolic blood pressure, glucose, HbA1c, HOMA-IR, CRP, MDA and the lipid profile, and raised HDL cholesterol.]}
}

""",
    "gu2023cinnamoncandida": """@article{gu2023cinnamoncandida,
  author  = {Gu, K., Feng, S., Zhang, X., Peng, Y., Sun, P., Liu, W., Wu, Y., Yu, Y., Liu, X., Deng, G., Zheng, J., Li, B. and Zhao, L.},
  title   = {Deciphering the antifungal mechanism and functional components of Cinnamomum cassia essential oil against Candida albicans},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0668},
  year    = {2023},
  doi     = {10.1016/j.jep.2023.117156},
  annote  = {Gu, K., Feng, S., Zhang, X., Peng, Y., Sun, P., Liu, W., Wu, Y., Yu, Y., Liu, X., Deng, G., Zheng, J., Li, B. and Zhao, L. (2023) 'Deciphering the antifungal mechanism and functional components of Cinnamomum cassia essential oil against Candida albicans through integration of network-based metabolomics and pharmacology', Journal of Ethnopharmacology, 319(Pt 2), 117156. doi:10.1016/j.jep.2023.117156. [Cinnamon (C. cassia) essential oil showed strong, concentration-dependent antifungal activity against Candida albicans by damaging the fungal cell membrane; trans-cinnamaldehyde was the principal active component.]}
}

""",
    "aggarwal2022cinnamaldehyde": """@article{aggarwal2022cinnamaldehyde,
  author  = {Aggarwal, S., Bhadana, K., Singh, B., Rawat, M., Mohammad, T., Al-Keridis, L.A., Alshammari, N., Hassan, M.I. and Das, S.N.},
  title   = {Cinnamomum zeylanicum extract and its bioactive component cinnamaldehyde show anti-tumor effects via inhibition of multiple cellular pathways},
  journal = {Frontiers in Pharmacology},
  note    = {REF-0669},
  year    = {2022},
  doi     = {10.3389/fphar.2022.918479},
  annote  = {Aggarwal, S., Bhadana, K., Singh, B., Rawat, M., Mohammad, T., Al-Keridis, L.A., Alshammari, N., Hassan, M.I. and Das, S.N. (2022) 'Cinnamomum zeylanicum extract and its bioactive component cinnamaldehyde show anti-tumor effects via inhibition of multiple cellular pathways', Frontiers in Pharmacology, 13, 918479. doi:10.3389/fphar.2022.918479. [Ceylon cinnamon (C. zeylanicum) extract and cinnamaldehyde inhibited oral cancer cell growth, inducing apoptosis and autophagy and suppressing NF-kB and PI3K-AKT-mTOR signalling.]}
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
