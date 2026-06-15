#!/usr/bin/env python3
"""Add new references for the 2026-06-15 enrichment batch N (least-cited records, 2).

Second batch of the least-referenced (three-reference) records; five new PubMed
sources each:

    Alchemilla vulgaris (Lady's mantle)     -> REF-0685..REF-0689
    Aloysia citrodora (Lemon verbena)       -> REF-0690..REF-0694
    Angelica archangelica (Garden angelica) -> REF-0695..REF-0699
    Arctostaphylos uva-ursi (Bearberry)     -> REF-0700..REF-0704
    Arctium lappa (Burdock)                 -> REF-0705..REF-0709

All sources from PubMed. New BibTeX entries inserted alphabetically by citation
key; YAML citations added by hand per action and logged in internal_notes.
Additive and idempotent.

Honest scope: the two bearberry UTI randomized trials (REF-0700 Gagyor, REF-0701
ATAFUTI/Moore) showed weak or null symptomatic benefit and are added as a
cautionary counterpoint to the traditional-use monographs already cited; the
record's UTI action is left verified (monograph basis) but the limitation is
documented in internal_notes. Some lady's-mantle and bearberry sources are
compound-level (arbutin) or antitumour studies cited mainly in internal_notes.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    # ---- Alchemilla vulgaris (Lady's mantle) -----------------------------
    "anajirih2024alchemilla": """@article{anajirih2024alchemilla,
  author  = {Anajirih, N., Abdeen, A., Taher, E.S., Abdelkader, A., Abd-Ellatieff, H.A., Gewaily, M.S. and others},
  title   = {Alchemilla vulgaris modulates isoproterenol-induced cardiotoxicity: interplay of oxidative stress, inflammation, autophagy, and apoptosis},
  journal = {Frontiers in Pharmacology},
  note    = {REF-0685},
  year    = {2024},
  doi     = {10.3389/fphar.2024.1394557},
  annote  = {Anajirih, N., Abdeen, A., Taher, E.S., Abdelkader, A., Abd-Ellatieff, H.A., Gewaily, M.S., et al. (2024) 'Alchemilla vulgaris modulates isoproterenol-induced cardiotoxicity: interplay of oxidative stress, inflammation, autophagy, and apoptosis', Frontiers in Pharmacology, 15, 1394557. doi:10.3389/fphar.2024.1394557. [In a mouse model of isoproterenol cardiac injury, A. vulgaris extract raised SOD, catalase and glutathione, lowered malondialdehyde, and downregulated IL-1-beta, TNF-alpha and NF-kB, confirming antioxidant and anti-inflammatory activity.]}
}

""",
    "jelaca2022alchemilla": """@article{jelaca2022alchemilla,
  author  = {Jelaca, S., Dajic-Stevanovic, Z., Vukovic, N., Kolasinac, S., Trendafilova, A., Nedialkov, P. and others},
  title   = {Beyond Traditional Use of Alchemilla vulgaris: Genoprotective and Antitumor Activity In Vitro},
  journal = {Molecules},
  note    = {REF-0686},
  year    = {2022},
  doi     = {10.3390/molecules27238113},
  annote  = {Jelaca, S., Dajic-Stevanovic, Z., Vukovic, N., Kolasinac, S., Trendafilova, A., Nedialkov, P., et al. (2022) 'Beyond Traditional Use of Alchemilla vulgaris: Genoprotective and Antitumor Activity In Vitro', Molecules, 27(23), 8113. doi:10.3390/molecules27238113. [UHPLC-HRMS identified 45 compounds in the ethanolic extract, which showed strong free-radical scavenging, protected human lymphocytes from chromosome damage, and suppressed several tumour cell lines via apoptosis and autophagy.]}
}

""",
    "vlaisavljevic2019alchemilla": """@article{vlaisavljevic2019alchemilla,
  author  = {Vlaisavljevic, S., Jelaca, S., Zengin, G., Mimica-Dukic, N., Berezni, S., Miljic, M. and Dajic Stevanovic, Z.},
  title   = {Alchemilla vulgaris agg. (Lady's mantle) from central Balkan: antioxidant, anticancer and enzyme inhibition properties},
  journal = {RSC Advances},
  note    = {REF-0687},
  year    = {2019},
  doi     = {10.1039/c9ra08231j},
  annote  = {Vlaisavljevic, S., Jelaca, S., Zengin, G., Mimica-Dukic, N., Berezni, S., Miljic, M. and Dajic Stevanovic, Z. (2019) 'Alchemilla vulgaris agg. (Lady's mantle) from central Balkan: antioxidant, anticancer and enzyme inhibition properties', RSC Advances, 9(64), pp. 37474-37483. doi:10.1039/c9ra08231j. [Twenty-six phenolics were quantified (gallic acid, caffeic acid, catechin, quercetin); the ethyl-acetate extract showed the greatest antioxidant, enzyme-inhibitory and cytotoxic activity.]}
}

""",
    "jelaca2024alchemillabreast": """@article{jelaca2024alchemillabreast,
  author  = {Jelaca, S., Jovanovic, I., Bovan, D., Jovanovic, M.Z., Jurisevic, M.M., Dundjerovic, D. and others},
  title   = {Dual Role of Alchemilla vulgaris L. Extract in Breast Cancer Regression: Reestablishment of Effective Immune Response},
  journal = {Pharmaceuticals},
  note    = {REF-0688},
  year    = {2024},
  doi     = {10.3390/ph17030286},
  annote  = {Jelaca, S., Jovanovic, I., Bovan, D., Jovanovic, M.Z., Jurisevic, M.M., Dundjerovic, D., et al. (2024) 'Dual Role of Alchemilla vulgaris L. Extract in Breast Cancer Regression: Reestablishment of Effective Immune Response', Pharmaceuticals, 17(3), 286. doi:10.3390/ph17030286. [The ethanolic extract reduced 4T1 breast-tumour growth in vitro and in vivo through apoptosis and autophagy while restoring antitumour immunity (dendritic-cell and effector T-cell activity).]}
}

""",
    "jelaca2024alchemillamelanoma": """@article{jelaca2024alchemillamelanoma,
  author  = {Jelaca, S., Jovanovic, I., Bovan, D., Pavlovic, S., Gajovic, N., Dundjerovic, D. and others},
  title   = {Antimelanoma Effects of Alchemilla vulgaris: A Comprehensive In Vitro and In Vivo Study},
  journal = {Diseases},
  note    = {REF-0689},
  year    = {2024},
  doi     = {10.3390/diseases12060125},
  annote  = {Jelaca, S., Jovanovic, I., Bovan, D., Pavlovic, S., Gajovic, N., Dundjerovic, D., et al. (2024) 'Antimelanoma Effects of Alchemilla vulgaris: A Comprehensive In Vitro and In Vivo Study', Diseases, 12(6), 125. doi:10.3390/diseases12060125. [The aerial-parts extract suppressed melanoma cell viability and reduced tumour growth in a syngeneic mouse model while enhancing antitumour immune responses, without systemic toxicity.]}
}

""",
    # ---- Aloysia citrodora (Lemon verbena) -------------------------------
    # Bahramsoltani 2018 review is already in the bibliography (REF-0474), so the
    # fifth lemon-verbena slot uses the Afrasiabian insomnia RCT instead.
    "afrasiabian2018aloysia": """@article{afrasiabian2018aloysia,
  author  = {Afrasiabian, F., Mirabzadeh Ardakani, M., Rahmani, K., Azadi, N.A., Alemohammad, Z.B., Bidaki, R., Karimi, M., Emtiazy, M. and Hashempur, M.H.},
  title   = {Aloysia citriodora Palau (lemon verbena) for insomnia patients: A randomized, double-blind, placebo-controlled clinical trial of efficacy and safety},
  journal = {Phytotherapy Research},
  note    = {REF-0690},
  year    = {2018},
  doi     = {10.1002/ptr.6228},
  annote  = {Afrasiabian, F., Mirabzadeh Ardakani, M., Rahmani, K., Azadi, N.A., Alemohammad, Z.B., Bidaki, R., Karimi, M., Emtiazy, M. and Hashempur, M.H. (2018) 'Aloysia citriodora Palau (lemon verbena) for insomnia patients: A randomized, double-blind, placebo-controlled clinical trial of efficacy and safety', Phytotherapy Research, 33(2), pp. 350-359. doi:10.1002/ptr.6228. [RCT (100 insomnia patients): a lemon verbena syrup taken before bedtime for 4 weeks significantly improved global Pittsburgh Sleep Quality Index and Insomnia Severity Index scores, including sleep latency and efficiency, versus placebo.]}
}

""",
    "perezpinero2024aloysia": """@article{perezpinero2024aloysia,
  author  = {Perez-Pinero, S., Munoz-Carrillo, J.C., Echepare-Taberna, J., Munoz-Camara, M., Herrera-Fernandez, C., Garcia-Guillen, A.I. and others},
  title   = {Dietary Supplementation with an Extract of Aloysia citrodora (Lemon verbena) Improves Sleep Quality in Healthy Subjects: A Randomized Double-Blind Controlled Study},
  journal = {Nutrients},
  note    = {REF-0691},
  year    = {2024},
  doi     = {10.3390/nu16101523},
  annote  = {Perez-Pinero, S., Munoz-Carrillo, J.C., Echepare-Taberna, J., Munoz-Camara, M., Herrera-Fernandez, C., Garcia-Guillen, A.I., et al. (2024) 'Dietary Supplementation with an Extract of Aloysia citrodora (Lemon verbena) Improves Sleep Quality in Healthy Subjects: A Randomized Double-Blind Controlled Study', Nutrients, 16(10), 1523. doi:10.3390/nu16101523. [90-day RCT (71 healthy adults with sleep disturbance): a lemon verbena extract significantly improved subjective and actigraphy sleep quality, latency and efficiency versus placebo, and raised nocturnal melatonin.]}
}

""",
    "tammar2021aloysia": """@article{tammar2021aloysia,
  author  = {Tammar, S., Salem, N., Aidi Wannes, W., Limam, H., Bourgou, S., Fares, N. and others},
  title   = {Chemometric Profiling and Bioactivity of Verbena (Aloysia citrodora) Methanolic Extract from Four Localities in Tunisia},
  journal = {Foods},
  note    = {REF-0692},
  year    = {2021},
  doi     = {10.3390/foods10122912},
  annote  = {Tammar, S., Salem, N., Aidi Wannes, W., Limam, H., Bourgou, S., Fares, N., et al. (2021) 'Chemometric Profiling and Bioactivity of Verbena (Aloysia citrodora) Methanolic Extract from Four Localities in Tunisia', Foods, 10(12), 2912. doi:10.3390/foods10122912. [Acteoside (verbascoside) made up about 80 percent of the methanolic fraction; the extract showed antioxidant, antibacterial, antifungal and anti-inflammatory activity varying with collection site.]}
}

""",
    "rashid2022aloysia": """@article{rashid2022aloysia,
  author  = {Rashid, H.M., Mahmod, A.I., Afifi, F.U. and Talib, W.H.},
  title   = {Antioxidant and Antiproliferation Activities of Lemon Verbena (Aloysia citrodora): An In Vitro and In Vivo Study},
  journal = {Plants},
  note    = {REF-0693},
  year    = {2022},
  doi     = {10.3390/plants11060785},
  annote  = {Rashid, H.M., Mahmod, A.I., Afifi, F.U. and Talib, W.H. (2022) 'Antioxidant and Antiproliferation Activities of Lemon Verbena (Aloysia citrodora): An In Vitro and In Vivo Study', Plants, 11(6), 785. doi:10.3390/plants11060785. [The ethanol extract showed potent DPPH radical-scavenging activity and the ethyl-acetate extract reduced tumour size and tumour incidence in tumour-bearing mice.]}
}

""",
    "hoseinifar2020aloysia": """@article{hoseinifar2020aloysia,
  author  = {Hoseinifar, S.H., Shakouri, M., Doan, H.V., Shafiei, S., Yousefi, M., Raeisi, M. and others},
  title   = {Dietary supplementation of lemon verbena (Aloysia citrodora) improved immunity, immune-related genes expression and antioxidant enzymes in rainbow trout (Oncorhynchus mykiss)},
  journal = {Fish and Shellfish Immunology},
  note    = {REF-0694},
  year    = {2020},
  doi     = {10.1016/j.fsi.2020.02.006},
  annote  = {Hoseinifar, S.H., Shakouri, M., Doan, H.V., Shafiei, S., Yousefi, M., Raeisi, M., et al. (2020) 'Dietary supplementation of lemon verbena (Aloysia citrodora) improved immunity, immune-related genes expression and antioxidant enzymes in rainbow trout (Oncorhynchus mykiss)', Fish and Shellfish Immunology, 99, pp. 379-385. doi:10.1016/j.fsi.2020.02.006. [Dietary lemon verbena raised serum lysozyme and immunoglobulin, upregulated IL-1-beta, IL-8 and TNF-alpha, and increased antioxidant enzymes (SOD, GST, GPx), indicating immunostimulant and antioxidant activity.]}
}

""",
    # ---- Angelica archangelica (Garden angelica) -------------------------
    "kaur2021angelica": """@article{kaur2021angelica,
  author  = {Kaur, A. and Bhatti, R.},
  title   = {Understanding the phytochemistry and molecular insights to the pharmacology of Angelica archangelica L. (garden angelica) and its bioactive components},
  journal = {Phytotherapy Research},
  note    = {REF-0695},
  year    = {2021},
  doi     = {10.1002/ptr.7206},
  annote  = {Kaur, A. and Bhatti, R. (2021) 'Understanding the phytochemistry and molecular insights to the pharmacology of Angelica archangelica L. (garden angelica) and its bioactive components', Phytotherapy Research, 35(11), pp. 5961-5979. doi:10.1002/ptr.7206. [Review: A. archangelica coumarins and volatile oils underlie validated anti-anxiety, anticonvulsant, cognition-enhancing, antiviral, cholinesterase-inhibitory, anti-inflammatory and gastroprotective activities.]}
}

""",
    "kaur2020angelicafibromyalgia": """@article{kaur2020angelicafibromyalgia,
  author  = {Kaur, A., Singh, N., Bhatti, M.S. and Bhatti, R.},
  title   = {Optimization of extraction conditions of Angelica archangelica extract and activity evaluation in experimental fibromyalgia},
  journal = {Journal of Food Science},
  note    = {REF-0696},
  year    = {2020},
  doi     = {10.1111/1750-3841.15476},
  annote  = {Kaur, A., Singh, N., Bhatti, M.S. and Bhatti, R. (2020) 'Optimization of extraction conditions of Angelica archangelica extract and activity evaluation in experimental fibromyalgia', Journal of Food Science, 85(11), pp. 3700-3710. doi:10.1111/1750-3841.15476. [In a reserpine-induced fibromyalgia model, the coumarin-rich root extract attenuated pain, improved motor ability and cognition, and lowered serum cytokines and brain oxidative stress.]}
}

""",
    "suciu2025angelica": """@article{suciu2025angelica,
  author  = {Suciu, F., Mihai, D.P., Ungurianu, A., Andrei, C., Puscasu, C., Chitescu, C.L. and others},
  title   = {Investigation of Anticonvulsant Potential of Morus, Angelica, Passiflora and Viola Extracts: In Vivo and In Silico Studies},
  journal = {International Journal of Molecular Sciences},
  note    = {REF-0697},
  year    = {2025},
  doi     = {10.3390/ijms26136426},
  annote  = {Suciu, F., Mihai, D.P., Ungurianu, A., Andrei, C., Puscasu, C., Chitescu, C.L., et al. (2025) 'Investigation of Anticonvulsant Potential of Morus, Angelica, Passiflora and Viola Extracts: In Vivo and In Silico Studies', International Journal of Molecular Sciences, 26(13), 6426. doi:10.3390/ijms26136426. [In an electroshock seizure model the Angelica archangelica extract showed moderate (non-significant) anticonvulsant activity while significantly reducing brain TNF-alpha and enhancing antioxidant defences.]}
}

""",
    "suenaga2022angelica": """@article{suenaga2022angelica,
  author  = {Suenaga-Hiromori, M., Mogi, D., Kikuchi, Y., Tong, J., Kurisu, N., Aoki, Y. and others},
  title   = {Comprehensive identification of terpene synthase genes and organ-dependent accumulation of terpenoid volatiles in a traditional medicinal plant Angelica archangelica L.},
  journal = {Plant Biotechnology},
  note    = {REF-0698},
  year    = {2022},
  doi     = {10.5511/plantbiotechnology.22.1006a},
  annote  = {Suenaga-Hiromori, M., Mogi, D., Kikuchi, Y., Tong, J., Kurisu, N., Aoki, Y., et al. (2022) 'Comprehensive identification of terpene synthase genes and organ-dependent accumulation of terpenoid volatiles in a traditional medicinal plant Angelica archangelica L.', Plant Biotechnology, 39(4), pp. 391-404. doi:10.5511/plantbiotechnology.22.1006a. [Characterised 11 terpene synthases and 27 terpenoid volatiles; mature seeds were richest in monoterpenoids, with beta-phellandrene most prominent and alpha-pinene and beta-myrcene abundant across organs, defining the aromatic oil.]}
}

""",
    "raafat2022angelica": """@article{raafat2022angelica,
  author  = {Raafat, B.M., Gamal-Eldeen, A.M., Almehmadi, M.M., El-Daly, S.M., Faizo, N.L. and Althobaiti, F.},
  title   = {Angelica archangelica and Ginkgo biloba Extracts Recover Functional Blood Hemoglobin Derivatives in Rabbits Exposed to High Altitude},
  journal = {Current Pharmaceutical Biotechnology},
  note    = {REF-0699},
  year    = {2022},
  doi     = {10.2174/1389201022666211118112356},
  annote  = {Raafat, B.M., Gamal-Eldeen, A.M., Almehmadi, M.M., El-Daly, S.M., Faizo, N.L. and Althobaiti, F. (2022) 'Angelica archangelica and Ginkgo biloba Extracts Recover Functional Blood Hemoglobin Derivatives in Rabbits Exposed to High Altitude', Current Pharmaceutical Biotechnology, 23(11), pp. 1377-1382. doi:10.2174/1389201022666211118112356. [Oral antioxidant-rich A. archangelica extract restored near-normal haemoglobin derivatives and antioxidant-enzyme activity in high-altitude rabbits, supporting its antioxidant action against oxidative stress.]}
}

""",
    # ---- Arctostaphylos uva-ursi (Bearberry) -----------------------------
    "gagyor2021uvaursi": """@article{gagyor2021uvaursi,
  author  = {Gagyor, I., Hummers, E., Schmiemann, G., Friede, T., Pfeiffer, S., Afshar, K. and Bleidorn, J.},
  title   = {Herbal treatment with uva ursi extract versus fosfomycin in women with uncomplicated urinary tract infection in primary care: a randomized controlled trial},
  journal = {Clinical Microbiology and Infection},
  note    = {REF-0700},
  year    = {2021},
  doi     = {10.1016/j.cmi.2021.05.032},
  annote  = {Gagyor, I., Hummers, E., Schmiemann, G., Friede, T., Pfeiffer, S., Afshar, K. and Bleidorn, J. (2021) 'Herbal treatment with uva ursi extract versus fosfomycin in women with uncomplicated urinary tract infection in primary care: a randomized controlled trial', Clinical Microbiology and Infection, 27(10), pp. 1441-1447. doi:10.1016/j.cmi.2021.05.032. [Double-blind RCT (398 women): initial uva-ursi cut antibiotic courses by about 64 percent versus fosfomycin, but produced a higher symptom burden and more pyelonephritis cases, failing the non-inferiority margin.]}
}

""",
    "moore2019uvaursi": """@article{moore2019uvaursi,
  author  = {Moore, M., Trill, J., Simpson, C., Webley, F., Radford, M., Stanton, L. and others},
  title   = {Uva-ursi extract and ibuprofen as alternative treatments for uncomplicated urinary tract infection in women (ATAFUTI): a factorial randomized trial},
  journal = {Clinical Microbiology and Infection},
  note    = {REF-0701},
  year    = {2019},
  doi     = {10.1016/j.cmi.2019.01.011},
  annote  = {Moore, M., Trill, J., Simpson, C., Webley, F., Radford, M., Stanton, L., et al. (2019) 'Uva-ursi extract and ibuprofen as alternative treatments for uncomplicated urinary tract infection in women (ATAFUTI): a factorial randomized trial', Clinical Microbiology and Infection, 25(8), pp. 973-980. doi:10.1016/j.cmi.2019.01.011. [Factorial RCT (382 women): uva-ursi extract showed no significant effect on urinary-frequency symptom severity or antibiotic consumption, whereas ibuprofen advice reduced antibiotic use.]}
}

""",
    "braga2020uvaursi": """@article{braga2020uvaursi,
  author  = {Braga, V.C.C., Pianetti, G.A. and Cesar, I.C.},
  title   = {Comparative stability of arbutin in Arctostaphylos uva-ursi by a new comprehensive stability-indicating HPLC method},
  journal = {Phytochemical Analysis},
  note    = {REF-0702},
  year    = {2020},
  doi     = {10.1002/pca.2953},
  annote  = {Braga, V.C.C., Pianetti, G.A. and Cesar, I.C. (2020) 'Comparative stability of arbutin in Arctostaphylos uva-ursi by a new comprehensive stability-indicating HPLC method', Phytochemical Analysis, 31(6), pp. 884-891. doi:10.1002/pca.2953. [Bearberry leaves contained 1.19 to 4.15 percent (w/w) arbutin and 0.022 to 0.604 percent hydroquinone with high variability; plant-matrix antioxidants reduced oxidative degradation of arbutin to hydroquinone, underscoring the need for standardisation.]}
}

""",
    "qin2024arbutin": """@article{qin2024arbutin,
  author  = {Qin, D., Liu, J., Guo, W., Ju, T., Fu, S., Liu, D. and Hu, G.},
  title   = {Arbutin alleviates intestinal colitis by regulating neutrophil extracellular traps formation and microbiota composition},
  journal = {Phytomedicine},
  note    = {REF-0703},
  year    = {2024},
  doi     = {10.1016/j.phymed.2024.155741},
  annote  = {Qin, D., Liu, J., Guo, W., Ju, T., Fu, S., Liu, D. and Hu, G. (2024) 'Arbutin alleviates intestinal colitis by regulating neutrophil extracellular traps formation and microbiota composition', Phytomedicine, 130, 155741. doi:10.1016/j.phymed.2024.155741. [Beta-arbutin, the glycoside extracted from Arctostaphylos uva-ursi leaves, protected mice from DSS colitis by inhibiting ERK-dependent neutrophil extracellular trap formation, preserving the mucosal barrier and reshaping gut microbiota.]}
}

""",
    "zhang2021arbutin": """@article{zhang2021arbutin,
  author  = {Zhang, B., Zeng, M., Li, B., Kan, Y., Wang, S., Cao, B. and others},
  title   = {Arbutin attenuates LPS-induced acute kidney injury by inhibiting inflammation and apoptosis via the PI3K/Akt/Nrf2 pathway},
  journal = {Phytomedicine},
  note    = {REF-0704},
  year    = {2021},
  doi     = {10.1016/j.phymed.2021.153466},
  annote  = {Zhang, B., Zeng, M., Li, B., Kan, Y., Wang, S., Cao, B., et al. (2021) 'Arbutin attenuates LPS-induced acute kidney injury by inhibiting inflammation and apoptosis via the PI3K/Akt/Nrf2 pathway', Phytomedicine, 82, 153466. doi:10.1016/j.phymed.2021.153466. [Arbutin, the principal bearberry glycoside, improved renal function and reduced inflammation, oxidative stress and apoptosis in LPS-induced acute kidney injury via TLR4/NF-kB suppression and PI3K/Akt/Nrf2 activation.]}
}

""",
    # ---- Arctium lappa (Burdock) -----------------------------------------
    "desouza2022arctium": """@article{desouza2022arctium,
  author  = {de Souza, A.R.C., de Oliveira, T.L., Fontana, P.D., Carneiro, M.C., Corazza, M.L., de Messias Reason, I.J. and Bavia, L.},
  title   = {Phytochemicals and Biological Activities of Burdock (Arctium lappa L.) Extracts: A Review},
  journal = {Chemistry and Biodiversity},
  note    = {REF-0705},
  year    = {2022},
  doi     = {10.1002/cbdv.202200615},
  annote  = {de Souza, A.R.C., de Oliveira, T.L., Fontana, P.D., Carneiro, M.C., Corazza, M.L., de Messias Reason, I.J. and Bavia, L. (2022) 'Phytochemicals and Biological Activities of Burdock (Arctium lappa L.) Extracts: A Review', Chemistry and Biodiversity, 19(11), e202200615. doi:10.1002/cbdv.202200615. [Review: burdock's phenolic compounds and terpenes give antioxidant, antimicrobial, antitumour and anti-inflammatory activity, with leaf extracts also inhibiting all complement pathways.]}
}

""",
    "moro2020arctium": """@article{moro2020arctium,
  author  = {Moro, T.M.A. and Clerici, M.T.P.S.},
  title   = {Burdock (Arctium lappa L) roots as a source of inulin-type fructans and other bioactive compounds: Current knowledge and future perspectives for food and non-food applications},
  journal = {Food Research International},
  note    = {REF-0706},
  year    = {2020},
  doi     = {10.1016/j.foodres.2020.109889},
  annote  = {Moro, T.M.A. and Clerici, M.T.P.S. (2020) 'Burdock (Arctium lappa L) roots as a source of inulin-type fructans and other bioactive compounds: Current knowledge and future perspectives for food and non-food applications', Food Research International, 141, 109889. doi:10.1016/j.foodres.2020.109889. [Review: burdock roots are rich in prebiotic inulin-type fructans plus chlorogenic acids, cynarine, lignans and quercetin, with antioxidant, anti-inflammatory, hypolipidemic and gastric-mucosal-protective activity.]}
}

""",
    "mondal2022arctium": """@article{mondal2022arctium,
  author  = {Mondal, S.C. and Eun, J.B.},
  title   = {Mechanistic insights on burdock (Arctium lappa L.) extract effects on diabetes mellitus},
  journal = {Food Science and Biotechnology},
  note    = {REF-0707},
  year    = {2022},
  doi     = {10.1007/s10068-022-01091-2},
  annote  = {Mondal, S.C. and Eun, J.B. (2022) 'Mechanistic insights on burdock (Arctium lappa L.) extract effects on diabetes mellitus', Food Science and Biotechnology, 31(8), pp. 999-1008. doi:10.1007/s10068-022-01091-2. [Review: burdock-root fructooligosaccharides and chlorogenic acid show antiviral, anti-inflammatory, hypolipidemic and antidiabetic effects, supporting burdock as an adjunct in type-2 diabetes management.]}
}

""",
    "romualdo2019arctium": """@article{romualdo2019arctium,
  author  = {Romualdo, G.R., Silva, E.D.A., Da Silva, T.C., Aloia, T.P.A., Nogueira, M.S., De Castro, I.A. and others},
  title   = {Burdock (Arctium lappa L.) root attenuates preneoplastic lesion development in a diet and thioacetamide-induced model of steatohepatitis-associated hepatocarcinogenesis},
  journal = {Environmental Toxicology},
  note    = {REF-0708},
  year    = {2019},
  doi     = {10.1002/tox.22887},
  annote  = {Romualdo, G.R., Silva, E.D.A., Da Silva, T.C., Aloia, T.P.A., Nogueira, M.S., De Castro, I.A., et al. (2019) 'Burdock (Arctium lappa L.) root attenuates preneoplastic lesion development in a diet and thioacetamide-induced model of steatohepatitis-associated hepatocarcinogenesis', Environmental Toxicology, 35(4), pp. 518-527. doi:10.1002/tox.22887. [Chlorogenic- and caffeic-acid-rich burdock root extract reduced hepatic fatty acids and lipid hydroperoxides, raised superoxide dismutase and catalase, and diminished preneoplastic liver lesions in a steatohepatitis model.]}
}

""",
    "chan2010arctium": """@article{chan2010arctium,
  author  = {Chan, Y.S., Cheng, L.N., Wu, J.H., Chan, E., Kwan, Y.W., Lee, S.M.Y., Leung, G.P.H., Yu, P.H.F. and Chan, S.W.},
  title   = {A review of the pharmacological effects of Arctium lappa (burdock)},
  journal = {Inflammopharmacology},
  note    = {REF-0709},
  year    = {2010},
  doi     = {10.1007/s10787-010-0062-4},
  annote  = {Chan, Y.S., Cheng, L.N., Wu, J.H., Chan, E., Kwan, Y.W., Lee, S.M.Y., Leung, G.P.H., Yu, P.H.F. and Chan, S.W. (2010) 'A review of the pharmacological effects of Arctium lappa (burdock)', Inflammopharmacology, 19(5), pp. 245-254. doi:10.1007/s10787-010-0062-4. [Review: burdock root improves skin quality and helps skin conditions such as eczema and carries antioxidant and antidiabetic compounds; seeds are anti-inflammatory and antitumour and leaf extract is antimicrobial, while contact dermatitis is a recognised side effect.]}
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
