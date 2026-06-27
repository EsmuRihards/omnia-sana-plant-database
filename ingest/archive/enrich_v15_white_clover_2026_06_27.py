#!/usr/bin/env python3
"""2026-06-27 — trifolium_repens (white clover) was SETTLED-INCOMPLETE at 7. A fresh genuine-only
search found additional species-specific T. repens medicinal/phytochemical articles, so the record
is brought up honestly (no wrong-species padding). Verified via PubMed MCP."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v15_2026_06_27 import apply, add_facts

add_facts("trifolium_repens",
          actions=["nephroprotective", "anticancer", "hepatoprotective"],
          indications=["kidney-support", "liver-support"])

SOURCES = [
    {"citekey": "ahmad2020trifoliumreview", "plant": "trifolium_repens", "study_type": "systematic-review",
     "fields": {"author": "Ahmad, S. and Zeb, A.",
                "title": "Phytochemical profile and pharmacological properties of Trifolium repens",
                "journal": "Journal of Basic and Clinical Physiology and Pharmacology", "year": "2020",
                "doi": "10.1515/jbcpp-2020-0015"},
     "abstract": "This review summarises the phytochemistry and pharmacology of Trifolium repens, which is used for antioxidant, anti-inflammatory, antiseptic, analgesic, antirheumatic and antimicrobial purposes and contains phenols, flavonoids, isoflavones, pterocarpans, cyanogenic glucosides, saponins and condensed tannins.",
     "actions": ["antioxidant", "anti-inflammatory"]},
    {"citekey": "ngangom2024trifolium", "plant": "trifolium_repens", "study_type": "systematic-review",
     "fields": {"author": "Ngangom, L., Venugopal, D. and Pandey, N.",
                "title": "Investigation of Trifolium repens L. from the Indian Himalayan region as a phyto-therapeutic agent",
                "journal": "Natural Product Research", "year": "2024", "volume": "38", "number": "24", "pages": "4468-4478",
                "doi": "10.1080/14786419.2023.2299319"},
     "abstract": "This review of Trifolium repens describes its traditional use for skin problems, wound healing, fever and as an analgesic and expectorant, and the antibacterial, antifungal, anti-inflammatory, antiaging and anti-hepatotoxic activities of bioactive compounds such as quercetin, kaempferol, myricetin and linamarin.",
     "actions": ["vulnerary", "anti-inflammatory"], "indications": ["wounds"]},
    {"citekey": "chen2019trifolium", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Chen, Y.H., Chen, P., Wang, Y., Yang, C.H., Wu, X., Wu, C.J., Luo, L., Wang, Q., Niu, C. and Yao, J.Y.",
                "title": "Structural characterization and anti-inflammatory activity evaluation of chemical constituents in the extract of Trifolium repens L.",
                "journal": "Journal of Food Biochemistry", "year": "2019", "volume": "43", "number": "9", "pages": "e12981",
                "doi": "10.1111/jfbc.12981"},
     "abstract": "Constituents of Trifolium repens were characterized by UPLC-HRMS, and three isolated compounds suppressed iNOS and COX-2 expression in LPS-induced RAW 264.7 cells, indicating anti-inflammatory activity.",
     "actions": ["anti-inflammatory"], "indications": ["inflammation"]},
    {"citekey": "ahmad2020trifoliumnephro", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Ahmad, S. and Zeb, A.",
                "title": "Nephroprotective property of Trifolium repens leaf extract against paracetamol-induced kidney damage in mice",
                "journal": "3 Biotech", "year": "2020", "volume": "10", "number": "12", "pages": "541",
                "doi": "10.1007/s13205-020-02539-0"},
     "abstract": "A phenolic-rich Trifolium repens leaf extract normalised renal function, electrolytes, glutathione and lipid peroxidation and protected kidney histology against paracetamol-induced nephrotoxicity in mice.",
     "actions": ["nephroprotective", "antioxidant"], "indications": ["kidney-support"]},
    {"citekey": "sarno2020trifolium", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Sarno, F., Pepe, G., Termolino, P., Carafa, V., Massaro, C., Merciai, F., Campiglia, P., Nebbioso, A. and Altucci, L.",
                "title": "Trifolium repens blocks proliferation in chronic myelogenous leukemia via the BCR-ABL/STAT5 pathway",
                "journal": "Cells", "year": "2020", "volume": "9", "number": "2", "pages": "379",
                "doi": "10.3390/cells9020379"},
     "abstract": "A Trifolium repens extract and its isoflavonoid-rich fraction were cytotoxic to chronic myelogenous leukemia K562 cells via inhibition of BCR-ABL/STAT5 and activation of p38, without harming normal cells.",
     "actions": ["anticancer"]},
    {"citekey": "habibizadeh2020trifolium", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Habibi Zadeh, S.K., Farahpour, M.R. and Kar, H.H.",
                "title": "The effect of topical administration of an ointment prepared from Trifolium repens hydroethanolic extract on the acceleration of excisional cutaneous wound healing",
                "journal": "Wounds", "year": "2020", "volume": "32", "number": "9", "pages": "253-261",
                "doi": "10.25270/wnds/2020.253261"},
     "abstract": "Topical Trifolium repens extract ointment accelerated excisional wound healing in rats, increasing wound contraction, angiogenesis and fibroblast distribution and modulating apoptosis genes, with strong antioxidant activity.",
     "actions": ["vulnerary", "antioxidant"], "indications": ["wounds"]},
    {"citekey": "kicel2011trifolium", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Kicel, A. and Wolbis, M.",
                "title": "Study on the phenolic constituents of the flowers and leaves of Trifolium repens L.",
                "journal": "Natural Product Research", "year": "2012", "volume": "26", "number": "21", "pages": "2050-2054",
                "doi": "10.1080/14786419.2011.637217"},
     "abstract": "Fourteen phenolic compounds, mainly flavonol glycosides of quercetin, kaempferol and myricetin plus a pterocarpan and methyl caffeate, were isolated from the flowers and leaves of Trifolium repens and showed potent DPPH antioxidant activity.",
     "actions": ["antioxidant"]},
    {"citekey": "ahmad2019trifoliumhepato", "plant": "trifolium_repens", "study_type": "preclinical",
     "fields": {"author": "Ahmad, S. and Zeb, A.",
                "title": "Effects of phenolic compounds from aqueous extract of Trifolium repens against acetaminophen-induced hepatotoxicity in mice",
                "journal": "Journal of Food Biochemistry", "year": "2019", "volume": "43", "number": "9", "pages": "e12963",
                "doi": "10.1111/jfbc.12963"},
     "abstract": "A phenolic-rich aqueous extract of Trifolium repens leaves protected against acetaminophen-induced hepatotoxicity in mice, normalising serum biochemistry, liver histology, lipid peroxidation and glutathione.",
     "actions": ["hepatoprotective", "antioxidant"], "indications": ["liver-support"]},
]

if __name__ == "__main__":
    apply(SOURCES)
