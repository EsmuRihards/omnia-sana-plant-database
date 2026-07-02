#!/usr/bin/env python3
"""Batch 57 of the ">=10 scientific publications" enrichment (2026-06-20).
The FINAL workable batch (remaining <10 plants are sparse/settled-incomplete).
Plants:
  prunella_vulgaris  (selfheal)  8 -> ~13,
  allium_sativum     (garlic)    9 -> ~14.
NOTE galium_album (9) is intentionally NOT enriched: it is already SETTLED-INCOMPLETE
(sparse Rubiaceae; per its yaml every genuine species-specific article is included and
policy forbids padding with wrong-species Galium verum / G. aparine citations).
Verified via PubMed MCP; DOIs where available; REAL authors per PMID from persisted metadata.

Species-care / exclusions:
  * selfheal: kept Prunella vulgaris-specific pharmacology/phytochem (critical pharmacology review,
    ethnopharm/QC review, comprehensive constituents/clinical review, polysaccharide NASH/gut, luteolin
    Graves'-disease immunomodulation/antioxidant). Coherent literature; nothing off-target needed excluding.
  * garlic: DEEP literature -> kept Allium sativum-titled pharmacology (constituents/pharmacology review,
    bioactive-compounds/biological-functions review, immunomodulatory T2DM review, human-health facts/myths
    review, NAFLD prevention SR/meta-analysis). EXCLUDED fish-aquaculture feed-additive (34164770),
    silver-nanoparticle antibacterial (36545079), and anticancer/food-peptide reviews kept out for the
    on-vocab set (34749610, 37801762, 26721553)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v10_2026_06_20 import apply

SOURCES = [
    # ==================================== prunella_vulgaris (selfheal) ====================================
    {"citekey": "mir2022prunella", "plant": "prunella_vulgaris", "study_type": "systematic-review",
     "fields": {"author": "Mir, R.H. and Bhat, M.F. and Sawhney, G. and Kumar, P. and Andrabi, N.I. and Shaikh, M. and Mohi-Ud-Din, R. and Masoodi, M.H.",
                "title": "Prunella vulgaris L: Critical Pharmacological, Expository Traditional Uses and Extensive Phytochemistry: A Review",
                "journal": "Current Drug Discovery Technologies", "year": "2022", "volume": "19", "number": "1", "pages": "e140122191102",
                "doi": "10.2174/1570163818666210203181542"},
     "abstract": "This review of Prunella vulgaris (selfheal) covers its traditional anti-inflammatory, antipyretic and antirheumatic uses and its triterpenoid, phenolic-acid, coumarin and flavonoid phytochemistry underlying antimicrobial, immunosuppressive and anti-inflammatory activity.",
     "actions": ["anti-inflammatory", "antimicrobial"], "constituents": ["Triterpenoids and phenolic acids"]},
    {"citekey": "pan2022prunella", "plant": "prunella_vulgaris", "study_type": "systematic-review",
     "fields": {"author": "Pan, J. and Wang, H. and Chen, Y.",
                "title": "Prunella vulgaris L. - A Review of its Ethnopharmacology, Phytochemistry, Quality Control and Pharmacological Effects",
                "journal": "Frontiers in Pharmacology", "year": "2022", "volume": "13", "pages": "903171",
                "doi": "10.3389/fphar.2022.903171"},
     "abstract": "This review summarises the ethnopharmacology, phytochemistry and pharmacology of Prunella vulgaris, including its anti-inflammatory, anti-tumor, antibacterial, antiviral, immunoregulatory and antioxidant effects.",
     "actions": ["anti-inflammatory", "antiviral", "antioxidant"]},
    {"citekey": "wang2019prunella", "plant": "prunella_vulgaris", "study_type": "systematic-review",
     "fields": {"author": "Wang, S.J. and Wang, X.H. and Dai, Y.Y. and Ma, M.H. and Rahman, K. and Nian, H. and Zhang, H.",
                "title": "Prunella vulgaris: A Comprehensive Review of Chemical Constituents, Pharmacological Effects and Clinical Applications",
                "journal": "Current Pharmaceutical Design", "year": "2019", "volume": "25", "number": "3", "pages": "359-369",
                "doi": "10.2174/1381612825666190313121608"},
     "abstract": "This comprehensive review of Prunella vulgaris summarises its triterpenoid, sterol and flavonoid constituents and its antimicrobial, anti-cancer and anti-inflammatory pharmacological activities and clinical applications.",
     "actions": ["anti-inflammatory", "antimicrobial"], "constituents": ["Triterpenoids and phenolic acids"]},
    {"citekey": "zhu2025prunella", "plant": "prunella_vulgaris", "study_type": "preclinical",
     "fields": {"author": "Zhu, M.J. and Song, Y.J. and Rao, P.L. and Gu, W.Y. and Xu, Y. and Xu, H.X.",
                "title": "Therapeutic role of Prunella vulgaris L. polysaccharides in non-alcoholic steatohepatitis and gut dysbiosis",
                "journal": "Journal of Integrative Medicine", "year": "2025", "volume": "23", "number": "3", "pages": "297-308",
                "doi": "10.1016/j.joim.2025.03.002"},
     "abstract": "Prunella vulgaris polysaccharides reduced hepatic inflammation and fibrosis in a non-alcoholic steatohepatitis model and improved gut microbiota composition and intestinal barrier function.",
     "actions": ["anti-inflammatory", "immunomodulator"], "constituents": ["Sulphated and polyphenol-conjugated polysaccharides"]},
    {"citekey": "zhang2024prunella", "plant": "prunella_vulgaris", "study_type": "preclinical",
     "fields": {"author": "Zhang, Y. and Qu, X. and Xu, N. and He, H. and Li, Q. and Wei, X. and Chen, Y. and Xu, Y. and Li, X. and Zhang, R. and Zhong, R. and Liu, C. and Xiang, P. and Zhu, F.",
                "title": "Mechanism of Prunella vulgaris L. and luteolin in restoring Tfh/Tfr balance and alleviating oxidative stress in Graves' disease",
                "journal": "Phytomedicine", "year": "2024", "volume": "132", "pages": "155818",
                "doi": "10.1016/j.phymed.2024.155818"},
     "abstract": "Prunella vulgaris and its flavonoid luteolin rebalanced follicular helper/regulatory T cells and alleviated oxidative stress in a Graves' disease model, acting via the Nrf2/HO-1 and PI3K/Akt pathways.",
     "actions": ["immunomodulator", "antioxidant"]},

    # ==================================== allium_sativum (garlic) ====================================
    {"citekey": "batiha2020allium", "plant": "allium_sativum", "study_type": "systematic-review",
     "fields": {"author": "El-Saber Batiha, G. and Magdy Beshbishy, A. and G Wasef, L. and Elewa, Y.H.A. and A Al-Sagan, A. and Abd El-Hack, M.E. and Taha, A.E. and M Abd-Elhakim, Y. and Prasad Devkota, H.",
                "title": "Chemical Constituents and Pharmacological Activities of Garlic (Allium sativum L.): A Review",
                "journal": "Nutrients", "year": "2020", "volume": "12", "number": "3", "pages": "872",
                "doi": "10.3390/nu12030872"},
     "abstract": "This review of garlic (Allium sativum) summarises its sulfur-containing phytoconstituents (alliin, allicin, ajoenes, S-allyl-cysteine) and its antibacterial, antifungal, antioxidant, anti-inflammatory, antidiabetic and antihypertensive pharmacological activities.",
     "actions": ["antioxidant", "antimicrobial", "antidiabetic"], "constituents": ["Allicin and organosulfur compounds (ajoene, S-allyl-cysteine)"]},
    {"citekey": "shang2019allium", "plant": "allium_sativum", "study_type": "systematic-review",
     "fields": {"author": "Shang, A. and Cao, S.Y. and Xu, X.Y. and Gan, R.Y. and Tang, G.Y. and Corke, H. and Mavumengwana, V. and Li, H.B.",
                "title": "Bioactive Compounds and Biological Functions of Garlic (Allium sativum L.)",
                "journal": "Foods", "year": "2019", "volume": "8", "number": "7", "pages": "246",
                "doi": "10.3390/foods8070246"},
     "abstract": "This review summarises the bioactive organosulfur compounds of garlic (Allium sativum) and their antioxidant, anti-inflammatory, antibacterial, antifungal, immunomodulatory, cardiovascular-protective and anti-diabetic functions.",
     "actions": ["antioxidant", "anti-inflammatory", "antimicrobial", "immunomodulator"], "constituents": ["Allicin and organosulfur compounds (ajoene, S-allyl-cysteine)"]},
    {"citekey": "mejiadelgado2025allium", "plant": "allium_sativum", "study_type": "systematic-review",
     "fields": {"author": "Mejia Delgado, E.M. and Quiroz-Aldave, J.E. and Durand-Vasquez, M.D.C. and Aldave-Pita, L.N. and Fuentes-Mendoza, J.M. and Concepcion-Urteaga, L.A. and Paz-Ibarra, J. and Concepcion-Zavaleta, M.J.",
                "title": "Immunomodulatory effect of Allium sativum in type 2 diabetes mellitus",
                "journal": "World Journal of Experimental Medicine", "year": "2025", "volume": "15", "number": "2", "pages": "103481",
                "doi": "10.5493/wjem.v15.i2.103481"},
     "abstract": "This review describes how the bioactive compounds of Allium sativum (allicin, S-allyl-cysteine, diallyl disulfide) exert anti-inflammatory, antioxidant and hypoglycemic effects and improve glucose metabolism in type 2 diabetes mellitus.",
     "actions": ["immunomodulator", "antidiabetic"], "indications": ["blood-sugar"]},
    {"citekey": "majewski2014allium", "plant": "allium_sativum", "study_type": "systematic-review",
     "fields": {"author": "Majewski, M.",
                "title": "Allium sativum: facts and myths regarding human health",
                "journal": "Roczniki Panstwowego Zakladu Higieny", "year": "2014", "volume": "65", "number": "1", "pages": "1-8"},
     "abstract": "This review of garlic (Allium sativum) evaluates the clinical evidence for its antibacterial, antihypertensive and antithrombotic properties and its use in hypertension, hypercholesterolemia and the prevention of atherosclerosis.",
     "actions": ["antimicrobial"], "indications": ["cardiovascular-support"]},
    {"citekey": "mardi2023allium", "plant": "allium_sativum", "study_type": "systematic-review",
     "fields": {"author": "Mardi, P. and Kargar, R. and Fazeli, R. and Qorbani, M.",
                "title": "Allium sativum: A potential natural compound for NAFLD prevention and treatment",
                "journal": "Frontiers in Nutrition", "year": "2023", "volume": "10", "pages": "1059106",
                "doi": "10.3389/fnut.2023.1059106"},
     "abstract": "This systematic review and meta-analysis found that Allium sativum (garlic) consumption is associated with prevention of non-alcoholic fatty liver disease and significantly lowers alanine and aspartate aminotransferase levels in NAFLD patients."},
]

if __name__ == "__main__":
    apply(SOURCES)
