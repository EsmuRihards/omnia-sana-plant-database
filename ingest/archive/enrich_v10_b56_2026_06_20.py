#!/usr/bin/env python3
"""Batch 56 of the ">=10 scientific publications" enrichment (2026-06-20).
Plants:
  angelica_archangelica  (garden angelica)  8 -> ~13,
  cinnamomum_verum       (Ceylon cinnamon)  9 -> ~14,
  hericium_erinaceus     (lion's mane)       9 -> ~14.
Verified via PubMed MCP; DOIs where available; REAL authors per PMID from persisted metadata.

Species-care / exclusions:
  * garden angelica: kept Angelica archangelica-specific pharmacology (phytochem/pharmacology review,
    fibromyalgia anti-inflammatory/cognition, anti-anxiety part-comparison, EO anti-inflammatory, root
    EO composition/antimicrobial constituents). EXCLUDED terpene-synthase genetics (37283614), breast-
    cancer anticancer off-vocab (30799248), Ginkgo-combo high-altitude hemoglobin (34792008), and a
    multi-species anticonvulsant screen where A. archangelica was non-significant (40650201).
  * Ceylon cinnamon: C. verum == C. zeylanicum (J. Presl) synonym; prefer verum/Ceylon-specific over
    pooled cassia. Kept Ceylon-cinnamon RCT (lipid/glucose/safety), C. verum phytochem/pharmacol review,
    C. verum anti-inflammatory NF-kB THP-1, bark antioxidant/anti-inflammatory post-digestion, bark anti-
    inflammatory/antidiabetic/hypolipidemic. EXCLUDED NMN-content anti-aging biochem (36296647), chitosan-
    nano EO (37570651), EO-sertraline synergy (36421261), leaf antibacterial (33749459), proanthocyanidin
    dentin-biomodification materials (35107279), multi-plant T2D integrative review (36424773).
  * lion's mane: kept Hericium erinaceus neurotrophic/neuroprotective review, neuroprotective/anti-inflam/
    antimicrobial narrative review, erinacine-A Alzheimer's pilot RCT, chemistry/health-promoting review,
    secondary-metabolite anti-inflammatory. (Existing refs already cover 2 cognition RCTs + colitis/macrophage
    polysaccharides; no off-target hits needed excluding this batch.)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v10_2026_06_20 import apply

SOURCES = [
    # ==================================== angelica_archangelica (garden angelica) ====================================
    {"citekey": "kaur2021angelica", "plant": "angelica_archangelica", "study_type": "systematic-review",
     "fields": {"author": "Kaur, A. and Bhatti, R.",
                "title": "Understanding the phytochemistry and molecular insights to the pharmacology of Angelica archangelica L. (garden angelica) and its bioactive components",
                "journal": "Phytotherapy Research", "year": "2021", "volume": "35", "number": "11", "pages": "5961-5979",
                "doi": "10.1002/ptr.7206"},
     "abstract": "This review of Angelica archangelica (garden angelica) summarises its phytochemistry and pharmacology, including anti-anxiety, anticonvulsant, cognition-enhancing, anti-inflammatory and gastroprotective activities attributed to its coumarins and volatile oils.",
     "actions": ["anti-inflammatory", "anxiolytic", "gastroprotective"], "constituents": ["Coumarins and furanocoumarins"]},
    {"citekey": "kaur2020angelica", "plant": "angelica_archangelica", "study_type": "preclinical",
     "fields": {"author": "Kaur, A. and Singh, N. and Bhatti, M.S. and Bhatti, R.",
                "title": "Optimization of extraction conditions of Angelica archangelica extract and activity evaluation in experimental fibromyalgia",
                "journal": "Journal of Food Science", "year": "2020", "volume": "85", "number": "11", "pages": "3700-3710",
                "doi": "10.1111/1750-3841.15476"},
     "abstract": "A coumarin-containing Angelica archangelica root extract attenuated pain, improved cognition and reduced serum cytokines and brain oxidative stress in a reserpine model of fibromyalgia.",
     "actions": ["anti-inflammatory", "neuroprotective"], "constituents": ["Coumarins and furanocoumarins"]},
    {"citekey": "kumar2012angelica", "plant": "angelica_archangelica", "study_type": "preclinical",
     "fields": {"author": "Kumar, D. and Bhat, Z.A.",
                "title": "Anti-anxiety Activity of Methanolic Extracts of Different Parts of Angelica archangelica Linn.",
                "journal": "Journal of Traditional and Complementary Medicine", "year": "2012", "volume": "2", "number": "3", "pages": "235-241",
                "doi": "10.1016/s2225-4110(16)30105-5"},
     "abstract": "Methanol extracts of Angelica archangelica parts showed anxiolytic activity in the elevated plus maze in rats, with the whole plant and root most active.",
     "actions": ["anxiolytic", "sedative"]},
    {"citekey": "fraternale2018angelica", "plant": "angelica_archangelica", "study_type": "preclinical",
     "fields": {"author": "Fraternale, D. and Teodori, L. and Rudov, A. and Prattichizzo, F. and Olivieri, F. and Guidarelli, A. and Albertini, M.C.",
                "title": "The In Vitro Activity of Angelica archangelica L. Essential Oil on Inflammation",
                "journal": "Journal of Medicinal Food", "year": "2018", "volume": "21", "number": "12", "pages": "1238-1243",
                "doi": "10.1089/jmf.2018.0017"},
     "abstract": "Angelica archangelica essential oil showed anti-inflammatory activity in vitro, decreasing the pro-inflammatory cytokine interleukin-6 and reverting LPS-induced inflammatory microRNA expression in endothelial cells.",
     "actions": ["anti-inflammatory"], "constituents": ["Essential (volatile) oil"]},
    {"citekey": "fraternale2014angelica", "plant": "angelica_archangelica", "study_type": "preclinical",
     "fields": {"author": "Fraternale, D. and Flamini, G. and Ricci, D.",
                "title": "Essential oil composition and antimicrobial activity of Angelica archangelica L. (Apiaceae) roots",
                "journal": "Journal of Medicinal Food", "year": "2014", "volume": "17", "number": "9", "pages": "1043-1047",
                "doi": "10.1089/jmf.2013.0012"},
     "abstract": "The alpha-pinene- and phellandrene-rich essential oil of Angelica archangelica roots showed antimicrobial activity against Clostridium difficile, Clostridium perfringens, Enterococcus faecalis and Candida albicans.",
     "constituents": ["Essential (volatile) oil"]},

    # ==================================== cinnamomum_verum (Ceylon cinnamon) ====================================
    {"citekey": "muthukuda2025cinnamomum", "plant": "cinnamomum_verum", "study_type": "clinical",
     "fields": {"author": "Muthukuda, D. and de Silva, C.K. and Ajanthan, S. and Wijesinghe, N. and Dahanayaka, A. and Pathmeswaran, A.",
                "title": "Effects of Cinnamomum zeylanicum (Ceylon cinnamon) extract on lipid profile, glucose levels and its safety in adults: A randomized, double-blind, controlled trial",
                "journal": "PLoS One", "year": "2025", "volume": "20", "number": "1", "pages": "e0317904",
                "doi": "10.1371/journal.pone.0317904"},
     "abstract": "In a randomized, double-blind, placebo-controlled trial, a standardized Cinnamomum zeylanicum (Ceylon cinnamon, C. verum) extract significantly reduced fasting blood sugar and was well tolerated in adults.",
     "actions": ["antidiabetic"], "indications": ["cardiovascular-support", "blood-sugar"]},
    {"citekey": "singh2020cinnamomum", "plant": "cinnamomum_verum", "study_type": "systematic-review",
     "fields": {"author": "Singh, N. and Rao, A.S. and Nandal, A. and Kumar, S. and Yadav, S.S. and Ganaie, S.A. and Narasimhan, B.",
                "title": "Phytochemical and pharmacological review of Cinnamomum verum J. Presl - a versatile spice used in food and nutrition",
                "journal": "Food Chemistry", "year": "2020", "volume": "338", "pages": "127773",
                "doi": "10.1016/j.foodchem.2020.127773"},
     "abstract": "This review of Cinnamomum verum (true Ceylon cinnamon) summarises its phytochemistry, dominated by cinnamaldehyde, and its antimicrobial, anti-inflammatory, antidiabetic and antioxidant pharmacology.",
     "actions": ["anti-inflammatory", "antimicrobial"], "constituents": ["Cinnamaldehyde"]},
    {"citekey": "kim2023cinnamomum", "plant": "cinnamomum_verum", "study_type": "preclinical",
     "fields": {"author": "Kim, N.Y. and Kim, S. and Park, H.M. and Lim, C.M. and Kim, J. and Park, J.Y. and Jeon, K.B. and Poudel, A.",
                "title": "Cinnamomum verum extract inhibits NOX2/ROS and PKCdelta/JNK/AP-1/NF-kB pathway-mediated inflammatory response in PMA-stimulated THP-1 monocytes",
                "journal": "Phytomedicine", "year": "2023", "volume": "112", "pages": "154685",
                "doi": "10.1016/j.phymed.2023.154685"},
     "abstract": "A Cinnamomum verum extract inhibited NOX2/ROS generation and the PKCdelta/JNK/AP-1/NF-kB pathway, suppressing the inflammatory response in PMA-stimulated THP-1 monocytes.",
     "actions": ["anti-inflammatory"]},
    {"citekey": "pagliari2023cinnamomum", "plant": "cinnamomum_verum", "study_type": "preclinical",
     "fields": {"author": "Pagliari, S. and Forcella, M. and Lonati, E. and Sacco, G. and Romaniello, F. and Rovellini, P. and Fusi, P. and Palestini, P.",
                "title": "Antioxidant and Anti-Inflammatory Effect of Cinnamon (Cinnamomum verum J. Presl) Bark Extract after In Vitro Digestion Simulation",
                "journal": "Foods", "year": "2023", "volume": "12", "number": "3", "pages": "452",
                "doi": "10.3390/foods12030452"},
     "abstract": "A Cinnamomum verum bark extract retained antioxidant and anti-inflammatory activity after in vitro digestion simulation, supporting its beneficial effects when consumed.",
     "actions": ["antioxidant", "anti-inflammatory"]},
    {"citekey": "ulhasnain2024cinnamomum", "plant": "cinnamomum_verum", "study_type": "preclinical",
     "fields": {"author": "Ul Hasnain, S.Z. and Ahmed, M. and Manzoor, R. and Amin, A. and Mudassir, J. and Jafar Rana, S. and Abbas, K.",
                "title": "Anti-inflammatory, antidiabetic and hypolipidemic potential of Cinnamomum verum J. Presl bark coupled with FT-IR and HPLC analysis",
                "journal": "Pakistan Journal of Pharmaceutical Sciences", "year": "2024", "volume": "37", "number": "6", "pages": "1529-1544"},
     "abstract": "A Cinnamomum verum bark extract demonstrated anti-inflammatory, antidiabetic and hypolipidemic potential, with its phytochemistry characterised by FT-IR and HPLC analysis.",
     "actions": ["anti-inflammatory", "antidiabetic"]},

    # ==================================== hericium_erinaceus (lion's mane) ====================================
    {"citekey": "szucko2023hericium", "plant": "hericium_erinaceus", "study_type": "systematic-review",
     "fields": {"author": "Szucko-Kociuba, I. and Trzeciak-Ryczek, A. and Kupnicka, P. and Chlubek, D.",
                "title": "Neurotrophic and Neuroprotective Effects of Hericium erinaceus",
                "journal": "International Journal of Molecular Sciences", "year": "2023", "volume": "24", "number": "21", "pages": "15960",
                "doi": "10.3390/ijms242115960"},
     "abstract": "This review analyses the neurotrophic and neuroprotective effects of Hericium erinaceus, whose erinacines and hericenones stimulate nerve growth factor release, reduce oxidative stress and protect nerve cells.",
     "actions": ["neuroprotective"], "constituents": ["Erinacines and hericenones"]},
    {"citekey": "contato2025hericium", "plant": "hericium_erinaceus", "study_type": "systematic-review",
     "fields": {"author": "Contato, A.G. and Conte-Junior, C.A.",
                "title": "Lion's Mane Mushroom (Hericium erinaceus): A Neuroprotective Fungus with Antioxidant, Anti-Inflammatory, and Antimicrobial Potential - A Narrative Review",
                "journal": "Nutrients", "year": "2025", "volume": "17", "number": "8", "pages": "1307",
                "doi": "10.3390/nu17081307"},
     "abstract": "This narrative review summarises the anti-inflammatory, antioxidant, antimicrobial and neuroprotective activities of Hericium erinaceus (lion's mane), attributed to its polysaccharides, terpenoids and phenolics.",
     "actions": ["anti-inflammatory", "neuroprotective"]},
    {"citekey": "li2020hericium", "plant": "hericium_erinaceus", "study_type": "clinical",
     "fields": {"author": "Li, I.C. and Chang, H.H. and Lin, C.H. and Chen, W.P. and Lu, T.H. and Lee, L.Y. and Chen, Y.W. and Chen, Y.P. and Chen, C.C. and Lin, D.P.",
                "title": "Prevention of Early Alzheimer's Disease by Erinacine A-Enriched Hericium erinaceus Mycelia Pilot Double-Blind Placebo-Controlled Study",
                "journal": "Frontiers in Aging Neuroscience", "year": "2020", "volume": "12", "pages": "155",
                "doi": "10.3389/fnagi.2020.00155"},
     "abstract": "In a pilot double-blind placebo-controlled trial, erinacine A-enriched Hericium erinaceus mycelia improved cognitive scores and contrast sensitivity in patients with mild Alzheimer's disease.",
     "actions": ["neuroprotective"], "constituents": ["Erinacines and hericenones"]},
    {"citekey": "friedman2015hericium", "plant": "hericium_erinaceus", "study_type": "systematic-review",
     "fields": {"author": "Friedman, M.",
                "title": "Chemistry, Nutrition, and Health-Promoting Properties of Hericium erinaceus (Lion's Mane) Mushroom Fruiting Bodies and Mycelia and Their Bioactive Compounds",
                "journal": "Journal of Agricultural and Food Chemistry", "year": "2015", "volume": "63", "number": "32", "pages": "7108-7123",
                "doi": "10.1021/acs.jafc.5b02914"},
     "abstract": "This overview consolidates the chemistry of Hericium erinaceus polysaccharides and secondary metabolites and their anti-inflammatory, antioxidant, immunostimulating and neuroprotective health-promoting properties.",
     "actions": ["immunomodulator"], "constituents": ["Polysaccharides (beta-glucans)"]},
    {"citekey": "xie2022hericium", "plant": "hericium_erinaceus", "study_type": "preclinical",
     "fields": {"author": "Xie, G. and Tang, L. and Xie, Y. and Xie, L.",
                "title": "Secondary Metabolites from Hericium erinaceus and Their Anti-Inflammatory Activities",
                "journal": "Molecules", "year": "2022", "volume": "27", "number": "7", "pages": "2157",
                "doi": "10.3390/molecules27072157"},
     "abstract": "Secondary metabolites isolated from the fruiting bodies of Hericium erinaceus, including a new sterol ester and hericenones, showed anti-inflammatory activity by inhibiting TNF-alpha, IL-6 and NO production in LPS-stimulated macrophages.",
     "actions": ["anti-inflammatory"], "constituents": ["Erinacines and hericenones"]},
]

if __name__ == "__main__":
    apply(SOURCES)
