#!/usr/bin/env python3
"""Batch 55 of the ">=10 scientific publications" enrichment (2026-06-20).
Plants:
  actaea_racemosa         (black cohosh)     8 -> ~13,
  aesculus_hippocastanum  (horse chestnut)   8 -> ~13,
  aloysia_citrodora       (lemon verbena)    8 -> ~13.
Verified via PubMed MCP; DOIs included; REAL authors per PMID from persisted metadata.

Species-care / exclusions:
  * black cohosh: Actaea racemosa == Cimicifuga racemosa (synonym) -> genus-Cimicifuga climacteric
    pharmacology is species-appropriate. Kept menopausal/climacteric efficacy-safety reviews,
    AMPK-metabolic mechanism, macrophage anti-inflammatory Ze 450, extract-specific evidence grading,
    ethnobotany/phytochem review. (No off-target hits excluded this batch - literature is coherent.)
  * horse chestnut: kept Aesculus hippocastanum seed/bark escin pharmacology (phytochem/ethnomedicinal
    review, anti-inflammatory/antiviral NF-kB, gastroprotective ulcer, anti-osteoarthritic escin combo,
    bark antioxidant vascular mechanism). EXCLUDED beta-aescin antibacterial-only (33850709), cyclophos-
    phamide-protection tox study (36337244), cancer-associated-fibroblast signalling (34962824), aescin
    HPLC quality-control method (36283324).
  * lemon verbena: Aloysia citrodora == Lippia citriodora/citrodora (synonym). Kept phytochem/pharmacology
    review, antioxidant/antiproliferation, neuroprotective EO, EO biological-activity (anti-inflam/anti-
    oxidant/antibacterial), antidiabetic/antihyperlipidemic. EXCLUDED aflatoxin-B1 food-safety inhibition
    (37446789), multi-species amoebicidal EO (39237458), multi-species hydrosol antimicrobial (38163838),
    strawberry shelf-life food-tech (33919369), melanoma EGFR anticancer (34360915, off-vocab)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v10_2026_06_20 import apply

SOURCES = [
    # ==================================== actaea_racemosa (black cohosh) ====================================
    {"citekey": "hedaoo2024actaea", "plant": "actaea_racemosa", "study_type": "systematic-review",
     "fields": {"author": "Hedaoo, K. and Badge, A.K. and Tiwade, Y.R. and Bankar, N.J. and Mishra, V.H.",
                "title": "Exploring the Efficacy and Safety of Black Cohosh (Actaea racemosa) in Menopausal Symptom Management",
                "journal": "Journal of Mid-life Health", "year": "2024", "volume": "15", "number": "1", "pages": "5-11",
                "doi": "10.4103/jmh.jmh_242_23"},
     "abstract": "This review explores the efficacy and safety of black cohosh (Actaea racemosa) in managing menopausal symptoms, noting its serotonergic rather than estrogenic mechanism and its potential to reduce hot flashes and night sweats.",
     "indications": ["menopause", "hot-flashes"]},
    {"citekey": "salari2021actaea", "plant": "actaea_racemosa", "study_type": "systematic-review",
     "fields": {"author": "Salari, S. and Amiri, M.S. and Ramezani, M. and Moghadam, A.T. and Elyasi, S. and Sahebkar, A. and Emami, S.A.",
                "title": "Ethnobotany, Phytochemistry, Traditional and Modern Uses of Actaea racemosa L. (Black cohosh): A Review",
                "journal": "Advances in Experimental Medicine and Biology", "year": "2021", "volume": "1308", "pages": "403-449",
                "doi": "10.1007/978-3-030-64872-5_24"},
     "abstract": "This review of Actaea racemosa (black cohosh) covers its ethnobotany and phytochemistry, focusing on the triterpene glycosides and phenolic constituents underlying its use for menopausal and post-menopausal symptoms.",
     "indications": ["menopause"], "constituents": ["Triterpene glycosides (actein, 23-epi-26-deoxyactein/cimicifugoside)"]},
    {"citekey": "drewe2022actaea", "plant": "actaea_racemosa", "study_type": "systematic-review",
     "fields": {"author": "Drewe, J. and Boonen, G. and Culmsee, C.",
                "title": "Treat more than heat - New therapeutic implications of Cimicifuga racemosa through AMPK-dependent metabolic effects",
                "journal": "Phytomedicine", "year": "2022", "volume": "100", "pages": "154060",
                "doi": "10.1016/j.phymed.2022.154060"},
     "abstract": "This review proposes that Cimicifuga racemosa (Actaea racemosa) extracts mitigate climacteric symptoms such as hot flushes partly through AMP-activated protein kinase (AMPK)-dependent metabolic effects.",
     "indications": ["menopause", "hot-flashes"]},
    {"citekey": "curtis2026actaea", "plant": "actaea_racemosa", "study_type": "systematic-review",
     "fields": {"author": "Curtis, S. and Moore, A. and Breakspear, I.",
                "title": "Efficacy and safety of Actaea racemosa for relieving climacteric complaints",
                "journal": "Menopause", "year": "2026", "volume": "33", "number": "5", "pages": "624-631",
                "doi": "10.1097/GME.0000000000002704"},
     "abstract": "This systematic review assessed the quality of clinical trial evidence for Actaea racemosa (black cohosh) in relieving climacteric complaints, finding a wide range of reporting quality and a need for further high-quality trials.",
     "indications": ["menopause", "hot-flashes"]},
    {"citekey": "beer2013actaea", "plant": "actaea_racemosa", "study_type": "systematic-review",
     "fields": {"author": "Beer, A.M. and Neff, A.",
                "title": "Differentiated Evaluation of Extract-Specific Evidence on Cimicifuga racemosa's Efficacy and Safety for Climacteric Complaints",
                "journal": "Evidence-Based Complementary and Alternative Medicine", "year": "2013", "volume": "2013", "pages": "860602",
                "doi": "10.1155/2013/860602"},
     "abstract": "This differentiated evaluation of Cimicifuga racemosa (Actaea racemosa) extracts found that registered medicinal products, particularly the isopropanolic extract, demonstrated consistent efficacy and a good safety profile for climacteric complaints.",
     "indications": ["menopause"]},

    # ==================================== aesculus_hippocastanum (horse chestnut) ====================================
    {"citekey": "idris2020aesculus", "plant": "aesculus_hippocastanum", "study_type": "systematic-review",
     "fields": {"author": "Idris, S. and Mishra, A. and Khushtar, M.",
                "title": "Phytochemical, ethnomedicinal and pharmacological applications of escin from Aesculus hippocastanum L. towards future medicine",
                "journal": "Journal of Basic and Clinical Physiology and Pharmacology", "year": "2020", "volume": "31", "number": "5",
                "doi": "10.1515/jbcpp-2019-0115"},
     "abstract": "This review summarises the phytochemistry, ethnomedicinal uses and pharmacology of escin from Aesculus hippocastanum (horse chestnut), including its use for venous congestion, bruises and inflammation.",
     "actions": ["venotonic", "anti-inflammatory"], "constituents": ["Triterpene saponins (escin / aescin)"]},
    {"citekey": "penaranda2024aesculus", "plant": "aesculus_hippocastanum", "study_type": "preclinical",
     "fields": {"author": "Penaranda Figueredo, F.A. and Vicente, J. and Barquero, A.A. and Bueno, C.A.",
                "title": "Aesculus hippocastanum extract and the main bioactive constituent beta-escin as antivirals agents against coronaviruses, including SARS-CoV-2",
                "journal": "Scientific Reports", "year": "2024", "volume": "14", "number": "1", "pages": "6418",
                "doi": "10.1038/s41598-024-56759-y"},
     "abstract": "Aesculus hippocastanum extract and beta-escin exhibited antiviral, virucidal and NF-kB-modulating anti-inflammatory activity against coronaviruses including SARS-CoV-2.",
     "actions": ["anti-inflammatory"]},
    {"citekey": "idris2023aesculus", "plant": "aesculus_hippocastanum", "study_type": "preclinical",
     "fields": {"author": "Idris, S. and Mishra, A. and Khushtar, M.",
                "title": "Phytochemical Estimation and Therapeutic Amelioration of Aesculus hippocastanum L. Seeds Ethanolic Extract in Gastric Ulcer in Rats Possibly by Inhibiting Prostaglandin Synthesis",
                "journal": "Chinese Journal of Integrative Medicine", "year": "2023", "volume": "29", "number": "9", "pages": "818-824",
                "doi": "10.1007/s11655-023-3734-9"},
     "abstract": "An ethanolic extract of Aesculus hippocastanum seeds, containing quercetin and rutin, protected against indomethacin-induced gastric ulcers in rats, improving mucosal integrity and antioxidant enzyme levels."},
    {"citekey": "quarta2022aesculus", "plant": "aesculus_hippocastanum", "study_type": "preclinical",
     "fields": {"author": "Quarta, S. and Santarpino, G. and Carluccio, M.A. and Calabriso, N. and Scoditti, E. and Siculella, L. and Damiano, F. and Maffia, M. and Verri, T. and De Caterina, R. and Massaro, M.",
                "title": "Analysis of the Anti-Inflammatory and Anti-Osteoarthritic Potential of Flonat Fast, a Combination of Plant Extracts, Bromelain and Escin (Aesculus hippocastanum), Evaluated in In Vitro Models of Inflammation Relevant to Osteoarthritis",
                "journal": "Pharmaceuticals", "year": "2022", "volume": "15", "number": "10", "pages": "1263",
                "doi": "10.3390/ph15101263"},
     "abstract": "Escin from Aesculus hippocastanum, alone and in a combination product, suppressed TNF-alpha-induced inflammation and angiogenesis in endothelial and monocyte models relevant to osteoarthritis.",
     "actions": ["anti-inflammatory"], "indications": ["arthritis"]},
    {"citekey": "owczarek2021aesculus", "plant": "aesculus_hippocastanum", "study_type": "preclinical",
     "fields": {"author": "Owczarek, A. and Kolodziejczyk-Czepas, J. and Wozniak-Serwata, J. and Magiera, A. and Kobiela, N. and Wasowicz, K. and Olszewska, M.A.",
                "title": "Potential Activity Mechanisms of Aesculus hippocastanum Bark: Antioxidant Effects in Chemical and Biological In Vitro Models",
                "journal": "Antioxidants", "year": "2021", "volume": "10", "number": "7", "pages": "995",
                "doi": "10.3390/antiox10070995"},
     "abstract": "Aesculus hippocastanum bark extract and its constituents esculin, fraxin and epicatechin showed strong antioxidant activity, protecting human plasma against oxidative damage and supporting its use in vascular disorders.",
     "constituents": ["Flavonoids and coumarins (aesculin)"], "indications": ["varicose-veins"]},

    # ==================================== aloysia_citrodora (lemon verbena) ====================================
    {"citekey": "bahramsoltani2018aloysia", "plant": "aloysia_citrodora", "study_type": "systematic-review",
     "fields": {"author": "Bahramsoltani, R. and Rostamiasrabadi, P. and Shahpiri, Z. and Marques, A.M. and Rahimi, R. and Farzaei, M.H.",
                "title": "Aloysia citrodora Palau (Lemon verbena): A review of phytochemistry and pharmacology",
                "journal": "Journal of Ethnopharmacology", "year": "2018", "volume": "222", "pages": "34-51",
                "doi": "10.1016/j.jep.2018.04.021"},
     "abstract": "This review of Aloysia citrodora (lemon verbena) summarises its phytochemistry (citral-rich essential oil and verbascoside) and pharmacology, including antioxidant, anxiolytic, neuroprotective and sedative activities.",
     "actions": ["antioxidant", "anxiolytic"], "constituents": ["Essential oil (neral and geranial, i.e. citral)", "Verbascoside (acteoside)"]},
    {"citekey": "rashid2022aloysia", "plant": "aloysia_citrodora", "study_type": "preclinical",
     "fields": {"author": "Rashid, H.M. and Mahmod, A.I. and Afifi, F.U. and Talib, W.H.",
                "title": "Antioxidant and Antiproliferation Activities of Lemon Verbena (Aloysia citrodora): An In Vitro and In Vivo Study",
                "journal": "Plants", "year": "2022", "volume": "11", "number": "6", "pages": "785",
                "doi": "10.3390/plants11060785"},
     "abstract": "Aloysia citrodora (lemon verbena) extracts showed potent radical-scavenging antioxidant activity and antiproliferative effects in vitro and reduced tumour size in vivo.",
     "actions": ["antioxidant"]},
    {"citekey": "abuhamdah2015aloysia", "plant": "aloysia_citrodora", "study_type": "preclinical",
     "fields": {"author": "Abuhamdah, S. and Abuhamdah, R. and Howes, M.J.R. and Al-Olimat, S. and Ennaceur, A. and Chazot, P.L.",
                "title": "Pharmacological and neuroprotective profile of an essential oil derived from leaves of Aloysia citrodora Palau",
                "journal": "The Journal of Pharmacy and Pharmacology", "year": "2015", "volume": "67", "number": "9", "pages": "1306-1315",
                "doi": "10.1111/jphp.12424"},
     "abstract": "The citral-rich essential oil of Aloysia citrodora leaves displayed antioxidant, iron-chelating and neuroprotective activity against hydrogen-peroxide- and beta-amyloid-induced neurotoxicity, and interacted with CNS receptors.",
     "actions": ["antioxidant", "sedative"], "constituents": ["Essential oil (neral and geranial, i.e. citral)"]},
    {"citekey": "sprea2023aloysia", "plant": "aloysia_citrodora", "study_type": "preclinical",
     "fields": {"author": "Sprea, R.M. and Fernandes, L.H.M. and Pires, T.C.S.P. and Calhelha, R.C. and Rodrigues, P.J. and Amaral, J.S.",
                "title": "Volatile Compounds and Biological Activity of the Essential Oil of Aloysia citrodora Palau: Comparison of Hydrodistillation and Microwave-Assisted Hydrodistillation",
                "journal": "Molecules", "year": "2023", "volume": "28", "number": "11", "pages": "4528",
                "doi": "10.3390/molecules28114528"},
     "abstract": "The geranial- and neral-rich essential oil of Aloysia citrodora showed antioxidant, anti-inflammatory and antibacterial activity, with the extraction method influencing composition and bioactivity.",
     "actions": ["anti-inflammatory", "antioxidant"]},
    {"citekey": "elouady2021aloysia", "plant": "aloysia_citrodora", "study_type": "preclinical",
     "fields": {"author": "El-Ouady, F. and Eddouks, M.",
                "title": "Antihyperglycemic and Antihyperlipidemic Effects of Lippia citriodora in Rats",
                "journal": "Endocrine, Metabolic & Immune Disorders Drug Targets", "year": "2021", "volume": "21", "number": "4", "pages": "711-719",
                "doi": "10.2174/1871530320666200610153532"},
     "abstract": "An aqueous leaf extract of Lippia citriodora (Aloysia citrodora) lowered blood glucose and lipid levels and exhibited antioxidant activity in diabetic rats."},
]

if __name__ == "__main__":
    apply(SOURCES)
