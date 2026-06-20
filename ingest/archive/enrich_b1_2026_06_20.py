#!/usr/bin/env python3
"""Batch 1 of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: elymus_repens, rubus_fruticosus, acorus_calamus, aegopodium_podagraria, arctium_minus.
Sources verified via the PubMed MCP (titles/authors/DOIs/abstracts from article metadata)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- elymus_repens (couch grass) ----
    {"citekey": "saparkhanovich2026elymus", "plant": "elymus_repens", "study_type": "traditional",
     "fields": {"author": "Zhakipbekov, K.S., Serikbayeva, E.A., Tleubayeva, M.I. et al.",
                "title": "Elymus repens (L.) Gould: Phytochemistry, Pharmacological Activities and Therapeutic Potential with Future Perspectives",
                "journal": "International Journal of Molecular Sciences", "year": "2026", "volume": "27", "number": "11", "pages": "4928",
                "doi": "10.3390/ijms27114928"},
     "abstract": "Elymus repens (L.) Gould, commonly known as couch grass, is mainly distributed as a medicinal herb of great ethnopharmacological importance. This review presents the significance of nomenclature clarity, current insights on distribution, traditional use, phytochemistry and their biological activities. The bioactive compound composition displayed a variety of compounds including carbohydrates, phenolic acids, flavonoids, benzoxazinoids and volatile compounds, all of which contribute to its medicinal properties. The biological potential of this plant underlines diuretic, antiurolithiatic, anti-inflammatory, antioxidant and antidiabetic qualities. The reported data notably confirmed its potential in lowering renal calculi and alleviating associated symptoms."},
    {"citekey": "bortolami2022elymus", "plant": "elymus_repens", "study_type": "preclinical",
     "fields": {"author": "Bortolami, M., Di Matteo, P., Rocco, D., Feroci, M. and Petrucci, R.",
                "title": "Metabolic Profile of Elymus repens (L.) P. Beauv. Rhizome Herbal Tea by HPLC-PDA-ESI-MS/MS Analysis",
                "journal": "Molecules", "year": "2022", "volume": "27", "number": "15", "pages": "4962",
                "doi": "10.3390/molecules27154962"},
     "abstract": "Elymus repens (couch grass) is a worldwide infesting rhizomatous plant with pharmacological applications. The aqueous extracts have been sparingly investigated, although the herbal tea is by far the most used formulation. The metabolic profile of the rhizome herbal tea was investigated by ESI-MS/MS and the phenolic profile by HPLC-PDA-ESI-MS/MS. The analysis evidenced at least 20 characteristic phenolic compounds, the most representative being caffeoyl and feruloyl quinic esters, followed by coumaric, caffeic and ferulic acids, and hesperidin among flavonoids."},
    {"citekey": "kasote2017herbal", "plant": "elymus_repens", "study_type": "traditional",
     "fields": {"author": "Kasote, D.M., Jagtap, S.D., Thapa, D., Khyade, M.S. and Russell, W.R.",
                "title": "Herbal remedies for urinary stones used in India and China: A review",
                "journal": "Journal of Ethnopharmacology", "year": "2017", "volume": "203", "pages": "55-68",
                "doi": "10.1016/j.jep.2017.03.038"},
     "abstract": "Urolithiasis is a longstanding health problem. A comprehensive review of the scientific literature about antiurolithiatic plants was undertaken. Plants such as Phyllanthus niruri L. and Elymus repens (L.) Gould, as well as herbal products, have proved their utility as promising antiurolithiatic medicines in different phases of clinical trials. The majority of antiurolithiatic plants were found to either dissolve the stones or inhibit the process of urinary stone formation."},

    # ---- rubus_fruticosus (blackberry leaf) ----
    {"citekey": "ziaulhaq2014rubus", "plant": "rubus_fruticosus", "study_type": "traditional",
     "fields": {"author": "Zia-Ul-Haq, M., Riaz, M., De Feo, V., Jaafar, H.Z.E. and Moga, M.",
                "title": "Rubus fruticosus L.: constituents, biological activities and health related uses",
                "journal": "Molecules", "year": "2014", "volume": "19", "number": "8", "pages": "10998-11029",
                "doi": "10.3390/molecules190810998"},
     "abstract": "Rubus fruticosus L. is a shrub famous for its fruit, the blackberry. R. fruticosus contains vitamins, steroids and lipids in seed oil, and minerals, flavonoids, glycosides, terpenes, acids and tannins in aerial parts that possess diverse pharmacological activities such as antioxidant, anti-carcinogenic, anti-inflammatory, antimicrobial, anti-diabetic, anti-diarrheal, and antiviral. This review focuses on the nutrients and chemical constituents as well as the medicinal properties of different parts of R. fruticosus."},
    {"citekey": "monforte2018rubus", "plant": "rubus_fruticosus", "study_type": "preclinical",
     "fields": {"author": "Monforte, M.T., Smeriglio, A., Germanò, M.P., Pergolizzi, S., Circosta, C. and Galati, E.M.",
                "title": "Evaluation of antioxidant, antiinflammatory, and gastroprotective properties of Rubus fruticosus L. fruit juice",
                "journal": "Phytotherapy Research", "year": "2018", "volume": "32", "number": "7", "pages": "1404-1414",
                "doi": "10.1002/ptr.6078"},
     "abstract": "The juice of R. fruticosus (RFJ) fruits, containing mainly anthocyanins such as cyanidin derivatives, phenolic acids and flavonoids, showed significant antioxidant activity in DPPH, TEAC, FRAP, ORAC and beta-carotene bleaching assays. In vivo studies showed that RFJ significantly inhibits carrageenan-induced paw oedema (63-71%) in rats and possesses anti-inflammatory effects, and RFJ pretreatment was able to prevent the ethanol-induced ulcerogenic (gastroprotective) effect in rats."},
    {"citekey": "barbieri2022rubus", "plant": "rubus_fruticosus", "study_type": "preclinical",
     "fields": {"author": "Barbieri, F., Montanari, C., Šimat, V., Skroza, D., Čagalj, M. et al.",
                "title": "Effects of Rubus fruticosus and Juniperus oxycedrus derivatives on culturability and viability of Listeria monocytogenes",
                "journal": "Scientific Reports", "year": "2022", "volume": "12", "number": "1", "pages": "13158",
                "doi": "10.1038/s41598-022-17408-4"},
     "abstract": "Phenolic extracts and essential oils obtained from Mediterranean Rubus fruticosus leaves and Juniperus oxycedrus needles were evaluated for antimicrobial effects against Listeria monocytogenes. These plant derivatives affected the growth of L. monocytogenes, increasing the lag phase and decreasing the final cell load; R. fruticosus essential oil was the most effective, determining an initial decrease of cell counts of about 6 log cycles. The work highlights blackberry leaves as underused raw materials for food and other industries."},

    # ---- acorus_calamus (sweet flag) ----
    {"citekey": "sharma2014acorus", "plant": "acorus_calamus", "study_type": "traditional",
     "fields": {"author": "Sharma, V., Singh, I. and Chaudhary, P.",
                "title": "Acorus calamus (The Healing Plant): a review on its medicinal potential, micropropagation and conservation",
                "journal": "Natural Product Research", "year": "2014", "volume": "28", "number": "18", "pages": "1454-1466",
                "doi": "10.1080/14786419.2014.915827"},
     "abstract": "Acorus calamus L. is a well-known plant in Indian traditional medicine, highly valued as a rejuvenator for the brain and nervous system and a main medhya (memory-improving) drug. Rhizomes are widely used in the treatment of epilepsy, mental ailments, chronic diarrhoea, dysentery, fever, kidney and liver troubles, and rheumatism. A. calamus leaves, rhizomes and essential oil possess antispasmodic and carminative activities. The review describes chemical constituents, toxicology, ethnobotany and pharmacological properties."},
    {"citekey": "khwairakpam2018acorus", "plant": "acorus_calamus", "study_type": "traditional",
     "fields": {"author": "Khwairakpam, A.D., Damayenti, Y.D., Deka, A., Monisha, J., Roy, N.K. et al.",
                "title": "Acorus calamus: a bio-reserve of medicinal values",
                "journal": "Journal of Basic and Clinical Physiology and Pharmacology", "year": "2018", "volume": "29", "number": "2", "pages": "107-122",
                "doi": "10.1515/jbcpp-2016-0132"},
     "abstract": "Acorus calamus, commonly known as sweet flag, is a rhizomatous plant whose leaves and rhizomes are used traditionally for arthritis, neuralgia, diarrhoea, dyspepsia, kidney and liver troubles, eczema, sinusitis, asthma, fevers and bronchitis. Biochemical analysis has revealed a large number of secondary metabolites responsible for its medicinal properties. The review summarises the ethno-medicinal uses, botanical description, phytochemical constituents, biological activity and molecular targets of the plant."},
    {"citekey": "ukkirapandian2022acorus", "plant": "acorus_calamus", "study_type": "preclinical",
     "fields": {"author": "Ukkirapandian, K., Kayalvizhi, E., Udaykumar, K.P., Kandhi, S. and Muthulakshmi, R.",
                "title": "The Neuroprotective Role of Acorus calamus in Developmental and Histopathological Changes in Autism-Induced Wistar Rats",
                "journal": "Cureus", "year": "2022", "volume": "14", "number": "9", "pages": "e29717",
                "doi": "10.7759/cureus.29717"},
     "abstract": "A rat model of autism was created by administering sodium valproate in pregnancy. Autism-induced pups treated with an ethanolic extract of Acorus calamus (200 mg/kg) were compared with untreated controls. Neurodegenerative changes were well appreciated in the untreated autism group, with significant reduction in frontal-cortex neurons and cerebellar Purkinje cells, whereas the A. calamus-treated group did not show significant alteration, suggesting A. calamus in the early postnatal period protects brain morphology against autism pathology."},

    # ---- aegopodium_podagraria (ground elder / goutweed) ----
    {"citekey": "debia2025goutweed", "plant": "aegopodium_podagraria", "study_type": "traditional",
     "fields": {"author": "Dębia, K., Dzięcioł, M., Wróblewska, A. and Janda-Milczarek, K.",
                "title": "Goutweed (Aegopodium podagraria L.): An Edible Weed with Health-Promoting Properties",
                "journal": "Molecules", "year": "2025", "volume": "30", "number": "7", "pages": "1603",
                "doi": "10.3390/molecules30071603"},
     "abstract": "Goutweed (Aegopodium podagraria L.) is a medicinal perennial in the celery family (Apiaceae), also an edible plant of high nutritional value. In traditional folk medicine it was known as a remedy for gout (arthritis) and used to relieve rheumatism or sciatica. Specific metabolites include organic acids, flavonoids, coumarins, polyacetylenes and terpene components of essential oil. Its valuable medicinal properties include anti-inflammatory, antirheumatic, antioxidant, antibacterial, antifungal, diuretic, sedative and protective effects on the kidneys and liver."},
    {"citekey": "engelhardt2022aegopodium", "plant": "aegopodium_podagraria", "study_type": "preclinical",
     "fields": {"author": "Engelhardt, L., Pöhnl, T. and Neugart, S.",
                "title": "Edible Wild Vegetables Urtica dioica L. and Aegopodium podagraria L.: Antioxidants Affected by Processing",
                "journal": "Plants (Basel)", "year": "2022", "volume": "11", "number": "20", "pages": "2710",
                "doi": "10.3390/plants11202710"},
     "abstract": "Urtica dioica L. and Aegopodium podagraria L. (stinging nettle and ground elder) are edible wild green vegetables rich in bioactive and antioxidant polyphenols, vitamins and minerals. Antioxidant activity assays (TEAC, DPPH, TPC) combined with HPLC were used to qualify and quantify their chemical compositions. Drying methods affected antioxidant activity, and cooking increased antioxidant activity due to higher concentrations of bioactive compounds released through rupture of cell structures."},
    {"citekey": "jakubczyk2021aegopodium", "plant": "aegopodium_podagraria", "study_type": "preclinical",
     "fields": {"author": "Jakubczyk, K., Łukomska, A., Czaplicki, S., Wajs-Bonikowska, A., Gutowska, I. et al.",
                "title": "Bioactive Compounds in Aegopodium podagraria Leaf Extracts and Their Effects against Fluoride-Modulated Oxidative Stress in the THP-1 Cell Line",
                "journal": "Pharmaceuticals (Basel)", "year": "2021", "volume": "14", "number": "12", "pages": "1334",
                "doi": "10.3390/ph14121334"},
     "abstract": "Goutweed (Aegopodium podagraria L.) leaves contain polyacetylenes, essential oils, mono- and sesquiterpenes, vitamins, macro- and microelements and phenolic compounds. This study investigated the antioxidant properties of different goutweed leaf extracts and their effects on the THP-1 cell line. Ethanol extracts had a high content of polyphenols, polyacetylenes and essential oil and high antioxidant potential, with positive effects on antioxidant enzyme activity in cells under fluoride-induced oxidative stress."},

    # ---- arctium_minus (lesser burdock; studied congener Arctium lappa) ----
    {"citekey": "ahangarpour2017arctium", "plant": "arctium_minus", "study_type": "preclinical",
     "fields": {"author": "Ahangarpour, A., Heidari, H., Oroojan, A.A., Mirzavandi, F., Nasr Esfehani, K. and Dehghan Mohammadi, Z.",
                "title": "Antidiabetic, hypolipidemic and hepatoprotective effects of Arctium lappa root's hydro-alcoholic extract on nicotinamide-streptozotocin induced type 2 model of diabetes in male mice",
                "journal": "Avicenna Journal of Phytomedicine", "year": "2017", "volume": "7", "number": "2", "pages": "169-179",
                "url": "https://pubmed.ncbi.nlm.nih.gov/28348972/"},
     "abstract": "Arctium lappa (burdock) root has hypoglycemic and antioxidative effects and has been used for treatment of diabetes in traditional medicine. This study evaluated the antidiabetic and hypolipidemic properties of the root's hydro-alcoholic extract on nicotinamide-streptozotocin-induced type 2 diabetes in male mice. Administration of the extract significantly decreased triglyceride, VLDL, glucose and alkaline phosphatase, and increased insulin, HDL and leptin levels, indicating an antidiabetic effect through hypolipidemic and insulinotropic properties, and a hepatoprotective effect."},
    {"citekey": "gao2018arctigenin", "plant": "arctium_minus", "study_type": "traditional",
     "fields": {"author": "Gao, Q., Yang, M. and Zuo, Z.",
                "title": "Overview of the anti-inflammatory effects, pharmacokinetic properties and clinical efficacies of arctigenin and arctiin from Arctium lappa L.",
                "journal": "Acta Pharmacologica Sinica", "year": "2018", "volume": "39", "number": "5", "pages": "787-801",
                "doi": "10.1038/aps.2018.32"},
     "abstract": "Arctigenin and its glycoside arctiin are two major active ingredients of Arctium lappa L., a popular medicinal herb and health supplement frequently used in Asia. This article reviews their anti-inflammatory effects, pharmacokinetics and clinical efficacies. Arctigenin exhibits potent anti-inflammatory activities by inhibiting iNOS via modulation of several cytokines and may serve as a potential therapeutic compound against acute inflammation and various chronic diseases."},
    {"citekey": "zeng2023arctium", "plant": "arctium_minus", "study_type": "preclinical",
     "fields": {"author": "Zeng, F., Li, Y., Zhang, X., Shen, L., Zhao, X. et al.",
                "title": "Immune regulation and inflammation inhibition of Arctium lappa L. polysaccharides by TLR4/NF-κB signaling pathway in cells",
                "journal": "International Journal of Biological Macromolecules", "year": "2023", "volume": "254", "pages": "127700",
                "doi": "10.1016/j.ijbiomac.2023.127700"},
     "abstract": "Arctium lappa L. polysaccharides (ALP) are important active ingredients of burdock roots. A crude polysaccharide was extracted and purified to 99% purity, and its immunomodulatory activity and intestinal anti-inflammatory effects were investigated in LPS-induced RAW264.7 macrophages and IL-1beta-induced Caco-2 colon cells. ALP possessed both antioxidant and anti-inflammatory effects, inhibiting pro-inflammatory cytokines (IL-8, IL-6, IL-1beta, TNF-alpha) by down-regulating the TLR4/NF-kappaB signaling pathway, indicating burdock as a source of bioactive polysaccharides for immune support."},
]

if __name__ == "__main__":
    apply(SOURCES)
