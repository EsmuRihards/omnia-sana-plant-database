#!/usr/bin/env python3
"""2026-06-27 — new records equisetum_pratense (shady horsetail, 3 sources) and
equisetum_sylvaticum (wood horsetail, 5 sources). Both are extremely sparse-literature
species (4 and 7 total PubMed records); SETTLED-INCOMPLETE. Genuine species-specific only,
no E. arvense padding. Verified via PubMed MCP. The two Batir-Marin 2021 multi-species papers
are shared (reused) across both records."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v15_2026_06_27 import apply

NEURO = {"citekey": "batirmarin2021equisetumneuro", "study_type": "preclinical",
         "fields": {"author": "Batir-Marin, D., Boev, M., Cioanca, O., Mircea, C., Burlec, A.F., Beppe, G.J., Spac, A., Corciova, A., Hritcu, L. and Hancianu, M.",
                    "title": "Neuroprotective and antioxidant enhancing properties of selective Equisetum extracts",
                    "journal": "Molecules", "year": "2021", "volume": "26", "number": "9", "pages": "2565",
                    "doi": "10.3390/molecules26092565"},
         "abstract": "Ethanolic extracts of Equisetum pratense, E. sylvaticum and E. telmateia, rich in polyphenolic derivatives, showed significant antioxidant activity in vitro and neuroprotective (with anxiolytic/antidepressant) effects in zebrafish."}
AGNP = {"citekey": "batirmarin2021equisetumagnp", "study_type": "preclinical",
        "fields": {"author": "Batir-Marin, D., Mircea, C., Boev, M., Burlec, A.F., Corciova, A., Fifere, A., Iacobescu, A., Cioanca, O., Verestiuc, L. and Hancianu, M.",
                   "title": "In vitro antioxidant, antitumor and photocatalytic activities of silver nanoparticles synthesized using Equisetum species: a green approach",
                   "journal": "Molecules", "year": "2021", "volume": "26", "number": "23", "pages": "7325",
                   "doi": "10.3390/molecules26237325"},
        "abstract": "Ethanolic extracts of Equisetum pratense, E. sylvaticum and E. telmateia were characterized for antioxidant capacity and used to green-synthesize silver nanoparticles with antioxidant and cytotoxic activity against the MG63 cancer cell line."}

SOURCES = [
    # ---- equisetum_pratense ----
    {**NEURO, "plant": "equisetum_pratense", "actions": ["antioxidant", "neuroprotective"],
     "constituents": ["Phenolic"]},
    {**AGNP, "plant": "equisetum_pratense", "actions": ["antioxidant"]},
    {"citekey": "chang1985equisetum", "plant": "equisetum_pratense", "study_type": "preclinical",
     "fields": {"author": "Chang, F.J. and Su, Y.M.",
                "title": "Pharmacological studies of the extract of Equisetum pratense on the tolerance to myocardial hypoxia in animals",
                "journal": "Zhong Xi Yi Jie He Za Zhi", "year": "1985", "volume": "5", "number": "12", "pages": "744-746"},
     "abstract": "An animal pharmacology study reported that an Equisetum pratense extract improved tolerance to myocardial hypoxia, with effects on myocardial cyclic AMP and cyclic GMP.",
     "indications": ["cardiovascular-support"]},

    # ---- equisetum_sylvaticum ----
    {"citekey": "wang2022equisetum", "plant": "equisetum_sylvaticum", "study_type": "preclinical",
     "fields": {"author": "Wang, Z., Tian, Y., Sugimoto, S., Yamano, Y., Kawakami, S., Otsuka, H. and Matsunami, K.",
                "title": "Four new glucosides from the aerial parts of Equisetum sylvaticum",
                "journal": "Journal of Natural Medicines", "year": "2022", "volume": "76", "number": "4", "pages": "832-841",
                "doi": "10.1007/s11418-022-01643-0"},
     "abstract": "Two new megastigmane glucosides, an apocarotenoid glucoside (equiseoside A) and an aromatic glucoside (equiseoside B), together with 35 known compounds, were isolated and characterized from the aerial parts of Equisetum sylvaticum.",
     "constituents": ["Megastigmane"]},
    {**NEURO, "plant": "equisetum_sylvaticum", "actions": ["antioxidant"], "constituents": ["Phenolic"]},
    {**AGNP, "plant": "equisetum_sylvaticum", "actions": ["antioxidant"]},
    {"citekey": "patova2019equisetum", "plant": "equisetum_sylvaticum", "study_type": "preclinical",
     "fields": {"author": "Patova, O.A., Smirnov, V.V., Golovchenko, V.V., Vityazev, F.V., Shashkov, A.S. and Popov, S.V.",
                "title": "Structural, rheological and antioxidant properties of pectins from Equisetum arvense L. and Equisetum sylvaticum L.",
                "journal": "Carbohydrate Polymers", "year": "2019", "volume": "209", "pages": "239-249",
                "doi": "10.1016/j.carbpol.2018.12.098"},
     "abstract": "Pectins isolated from the sterile stems of Equisetum sylvaticum were structurally characterized and scavenged DPPH and hydroxyl radicals, supporting their potential as components of wound-healing remedies.",
     "actions": ["antioxidant"], "constituents": ["Pectic"]},
    {"citekey": "fry2008equisetum", "plant": "equisetum_sylvaticum", "study_type": "preclinical",
     "fields": {"author": "Fry, S.C., Nesselrode, B.H.W.A., Miller, J.G. and Mewburn, B.R.",
                "title": "Mixed-linkage (1->3,1->4)-beta-D-glucan is a major hemicellulose of Equisetum (horsetail) cell walls",
                "journal": "New Phytologist", "year": "2008", "volume": "179", "number": "1", "pages": "104-115",
                "doi": "10.1111/j.1469-8137.2008.02435.x"},
     "abstract": "Mixed-linkage (1->3,1->4)-beta-D-glucan was identified as a major wall hemicellulose in Equisetum species including E. sylvaticum, an independently evolved trait shared with grasses.",
     "constituents": ["Mixed-linkage"]},
]

if __name__ == "__main__":
    apply(SOURCES)
