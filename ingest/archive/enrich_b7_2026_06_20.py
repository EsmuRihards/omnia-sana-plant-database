#!/usr/bin/env python3
"""Batch 7 of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: eleutherococcus_senticosus, epilobium_parviflorum, eschscholzia_californica,
eucalyptus_globulus, euphrasia_officinalis. Sources verified via the PubMed MCP; DOIs pre-checked.
Epilobium refs are at the genus/congener level (E. hirsutum, Epilobium spp.) as E. parviflorum
shares the willowherb phytochemistry/prostate use; noted for transparency."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- eleutherococcus_senticosus (Siberian ginseng) ----
    {"citekey": "li2022eleutherococcus", "plant": "eleutherococcus_senticosus", "study_type": "traditional",
     "fields": {"author": "Li, X.T., Zhou, J.C., Zhou, Y., Ren, Y.S. et al.",
                "title": "Pharmacological effects of Eleutherococcus senticosus on the neurological disorders",
                "journal": "Phytotherapy Research", "year": "2022", "volume": "36", "number": "9", "pages": "3490-3504",
                "doi": "10.1002/ptr.7555"},
     "abstract": "Eleutherococcus senticosus is widely used in traditional medicine with anti-fatigue, sleep-improving and memory-enhancing effects. This review summarises its therapeutic effects on fatigue, depression, Alzheimer's disease, Parkinson's disease and cerebral ischemia, and the underlying mechanisms (anti-oxidative damage, anti-inflammation, neurotransmitter modulation, improvement of neuronal growth and anti-apoptosis), supporting its development as a neuroprotective phytotherapy agent."},
    {"citekey": "li2021eleutherococcuspoly", "plant": "eleutherococcus_senticosus", "study_type": "traditional",
     "fields": {"author": "Li, X., Chen, C., Leng, A. and Qu, J.",
                "title": "Advances in the Extraction, Purification, Structural Characteristics and Biological Activities of Eleutherococcus senticosus Polysaccharides",
                "journal": "Frontiers in Pharmacology", "year": "2021", "volume": "12", "pages": "753007",
                "doi": "10.3389/fphar.2021.753007"},
     "abstract": "Eleutherococcus senticosus is a medicine-and-food plant with anti-tumor, anti-inflammatory, central-nervous-system and cardiovascular-protective, anti-radiation and anti-fatigue effects. This review focuses on its polysaccharides (ESPS), summarising progress in their extraction, separation, structural characterisation and biological activity as a basis for further development and utilisation of this medicinal and edible resource."},
    {"citekey": "wrobelbiedrawa2024adaptogens", "plant": "eleutherococcus_senticosus", "study_type": "traditional",
     "fields": {"author": "Wróbel-Biedrawa, D. and Podolak, I.",
                "title": "Anti-Neuroinflammatory Effects of Adaptogens: A Mini-Review",
                "journal": "Molecules", "year": "2024", "volume": "29", "number": "4", "pages": "866",
                "doi": "10.3390/molecules29040866"},
     "abstract": "Adaptogens, including Eleutherococcus senticosus, exhibit complex nonspecific effects that increase the body's ability to adapt and survive stress. This mini-review presents the anti-neuroinflammatory potential of the most important adaptogenic plants: they display anti-inflammatory effects, regulating the gene expression of pro- and anti-inflammatory cytokines and modulating signaling pathways such as NF-kB, relevant to central-nervous-system disorders."},

    # ---- epilobium_parviflorum (small-flowered willowherb; genus/congener-level refs) ----
    {"citekey": "vitalone2018epilobium", "plant": "epilobium_parviflorum", "study_type": "traditional",
     "fields": {"author": "Vitalone, A. and Allkanjari, O.",
                "title": "Epilobium spp: Pharmacology and Phytochemistry",
                "journal": "Phytotherapy Research", "year": "2018", "volume": "32", "number": "7", "pages": "1229-1240",
                "doi": "10.1002/ptr.6072"},
     "abstract": "Epilobium species and their extracts are popular in folk medicine for a wide range of applications. This review analyses the pharmacological properties of Epilobium spp (anti-inflammatory, antioxidant, antitumor, antimicrobial, analgesic and antiandrogenic) and whether they justify the traditional use of willowherb, particularly for prostate conditions, noting that randomized controlled trials are still needed."},
    {"citekey": "cicero2019nutraceutical", "plant": "epilobium_parviflorum", "study_type": "traditional",
     "fields": {"author": "Cicero, A.F.G., Allkanjari, O., Busetto, G.M., Cai, T. et al.",
                "title": "Nutraceutical treatment and prevention of benign prostatic hyperplasia and prostate cancer",
                "journal": "Archivio Italiano di Urologia e Andrologia", "year": "2019", "volume": "91", "number": "3", "pages": "139-152",
                "doi": "10.4081/aiua.2019.3.139"},
     "abstract": "This review covers medicinal plants used for prostate diseases such as benign prostatic hyperplasia, prostatitis and chronic pelvic pain syndrome, whose desired pharmacological properties are anti-androgenic, anti-estrogenic, antiproliferative, antioxidant and anti-inflammatory. Alongside Serenoa repens, Pygeum africanum and Urtica dioica, Epilobium spp is highlighted as a promising plant for prostatic disease, supporting the traditional use of willowherb for prostate health."},
    {"citekey": "vlase2024epilobium", "plant": "epilobium_parviflorum", "study_type": "preclinical",
     "fields": {"author": "Vlase, A.M., Toiu, A., Gligor, O., Muntean, D. et al.",
                "title": "Investigation of Epilobium hirsutum L. Optimized Extract's Anti-Inflammatory and Antitumor Potential",
                "journal": "Plants (Basel)", "year": "2024", "volume": "13", "number": "2", "pages": "198",
                "doi": "10.3390/plants13020198"},
     "abstract": "An optimized extract of Epilobium hirsutum (a willowherb congener) was tested in animal models. In carrageenan-induced paw inflammation it showed anti-inflammatory properties comparable to indomethacin, and in an Ehrlich ascites carcinoma model it reduced tumor-associated inflammation and oxidative stress, indicating potential as a natural adjuvant against inflammation and oxidative stress."},

    # ---- eschscholzia_californica (California poppy) ----
    {"citekey": "rolland1991eschscholzia", "plant": "eschscholzia_californica", "study_type": "preclinical",
     "fields": {"author": "Rolland, A., Fleurentin, J., Lanhers, M.C., Younos, C. et al.",
                "title": "Behavioural effects of the American traditional plant Eschscholzia californica: sedative and anxiolytic properties",
                "journal": "Planta Medica", "year": "1991", "volume": "57", "number": "3", "pages": "212-216",
                "doi": "10.1055/s-2006-960076"},
     "abstract": "An aqueous extract of Eschscholzia californica, traditionally used by Californian populations for its analgesic and sedative properties, reduced behavioural parameters in mice at doses above 100 mg/kg and induced sleep, validating its sedative properties; at 25 mg/kg it produced anxiolytic (anticonflict) effects without toxic effects, supporting the traditional sedative/anxiolytic use of California poppy."},
    {"citekey": "rolland2001eschscholzia", "plant": "eschscholzia_californica", "study_type": "preclinical",
     "fields": {"author": "Rolland, A., Fleurentin, J., Lanhers, M.C., Misslin, R. and Mortier, F.",
                "title": "Neurophysiological effects of an extract of Eschscholzia californica Cham. (Papaveraceae)",
                "journal": "Phytotherapy Research", "year": "2001", "volume": "15", "number": "5", "pages": "377-381",
                "doi": "10.1002/ptr.884"},
     "abstract": "An aqueous-alcohol extract of Eschscholzia californica was evaluated for its mechanism of sedative and anxiolytic action. The extract appeared to possess affinity for the benzodiazepine receptor (flumazenil, a benzodiazepine antagonist, suppressed its sedative and anxiolytic effects) and induced peripheral analgesic effects, but had no antidepressant, neuroleptic or antihistaminic effects, clarifying the basis of California poppy's calming action."},
    {"citekey": "kalyniukova2025eschscholzia", "plant": "eschscholzia_californica", "study_type": "preclinical",
     "fields": {"author": "Kalyniukova, A., Ahmed, S., Ak, G., Saka, E. et al.",
                "title": "Comprehensive Metabolomic Profiling and Biological Activity Analysis of Eschscholzia californica Extracts Using LC-ESI-QTOF-MS",
                "journal": "Food Science & Nutrition", "year": "2025", "volume": "13", "number": "9", "pages": "e70885",
                "doi": "10.1002/fsn3.70885"},
     "abstract": "LC-ESI-QTOF-MS profiling of Eschscholzia californica aerial-part extracts identified 70 compounds including rutin, quinoline alkaloids, morphine derivatives and scoulerine. Extracts showed antioxidant, anti-acetylcholinesterase, anti-tyrosinase and anti-glucosidase activity, and in silico studies showed protopine, rutin, eschscholtzidine, boldine and scoulerine inhibit insomnia-related DRD5, DRD4 and SERT proteins, supporting the plant's traditional use for sleep."},

    # ---- eucalyptus_globulus ----
    {"citekey": "cmikova2023eucalyptus", "plant": "eucalyptus_globulus", "study_type": "preclinical",
     "fields": {"author": "Čmiková, N., Galovičová, L., Schwarzová, M., Vukic, M.D. et al.",
                "title": "Chemical Composition and Biological Activities of Eucalyptus globulus Essential Oil",
                "journal": "Plants (Basel)", "year": "2023", "volume": "12", "number": "5", "pages": "1076",
                "doi": "10.3390/plants12051076"},
     "abstract": "Eucalyptus globulus essential oil (EGEO), dominated by 1,8-cineole (63.1%), p-cymene, alpha-pinene and limonene (over 99% monoterpenes), was analysed for antimicrobial, antibiofilm, antioxidant and insecticidal activity. EGEO showed antioxidant capacity, antimicrobial activity (strongest against Gram-positive bacteria and microscopic fungi, especially in the vapour phase), antibiofilm activity and insecticidal activity."},
    {"citekey": "elangovan2023eucalyptus", "plant": "eucalyptus_globulus", "study_type": "systematic-review",
     "fields": {"author": "Elangovan, S. and Mudgil, P.",
                "title": "Antibacterial Properties of Eucalyptus globulus Essential Oil against MRSA: A Systematic Review",
                "journal": "Antibiotics (Basel)", "year": "2023", "volume": "12", "number": "3", "pages": "474",
                "doi": "10.3390/antibiotics12030474"},
     "abstract": "A systematic review of 20 studies (2002-2022) on the antibacterial properties of Eucalyptus globulus essential oil against methicillin-resistant Staphylococcus aureus (MRSA). The findings suggest E. globulus essential oil has antibacterial properties against MRSA, which can be enhanced when used in combination with other essential oils and antibiotics, supporting its potential as an alternative antimicrobial agent."},
    {"citekey": "zonfrillo2022eucalyptus", "plant": "eucalyptus_globulus", "study_type": "preclinical",
     "fields": {"author": "Zonfrillo, M., Andreola, F., Krasnowska, E.K., Sferrazza, G. et al.",
                "title": "Essential Oil from Eucalyptus globulus (Labill.) Activates Complement Receptor-Mediated Phagocytosis and Stimulates Podosome Formation in Human Monocyte-Derived Macrophages",
                "journal": "Molecules", "year": "2022", "volume": "27", "number": "11", "pages": "3488",
                "doi": "10.3390/molecules27113488"},
     "abstract": "Essential oil from Eucalyptus globulus, and its major component eucalyptol, stimulated the phagocytic activity of human monocyte-derived macrophages by activating complement-receptor-mediated phagocytosis and stimulating podosome formation, confirming the essential oil as a potent activator of innate cell-mediated immunity in addition to its known antiseptic and anti-inflammatory properties."},

    # ---- euphrasia_officinalis (eyebright) ----
    {"citekey": "novy2015euphrasia", "plant": "euphrasia_officinalis", "study_type": "preclinical",
     "fields": {"author": "Novy, P., Davidova, H., Serrano-Rojero, C.S., Rondevaldova, J. et al.",
                "title": "Composition and Antimicrobial Activity of Euphrasia rostkoviana Hayne Essential Oil",
                "journal": "Evidence-Based Complementary and Alternative Medicine", "year": "2015", "volume": "2015", "pages": "734101",
                "doi": "10.1155/2015/734101"},
     "abstract": "Eyebright (Euphrasia rostkoviana, syn. E. officinalis) is traditionally used in Europe as an eyewash to treat eye ailments such as conjunctivitis and blepharitis associated with bacterial infections. This study characterised the essential oil (main constituents n-hexadecanoic acid, thymol, myristic acid, linalool and anethole) and showed antimicrobial activity against organisms associated with eye infections, especially Gram-positive bacteria, supporting the traditional ophthalmic use."},
    {"citekey": "dambrosio2018euphrasia", "plant": "euphrasia_officinalis", "study_type": "preclinical",
     "fields": {"author": "D'Ambrosio, M., Ciocarlan, A. and Aricu, A.",
                "title": "Minor acetylated metabolites from Euphrasia rostkoviana",
                "journal": "Natural Product Research", "year": "2020", "volume": "34", "number": "2", "pages": "290-295",
                "doi": "10.1080/14786419.2018.1530227"},
     "abstract": "The phenylethanoids rostkovianoside and 6'-O-acetylcrassifolioside and the flavonoid rutin 3'''-acetate were isolated from the methanolic extract of the aerial parts of Euphrasia rostkoviana (syn. E. officinalis), and their structures elucidated by spectroscopic methods, characterising the phenylethanoid glycoside and flavonoid constituents of eyebright."},
    {"citekey": "ververis2024euphrasia", "plant": "euphrasia_officinalis", "study_type": "preclinical",
     "fields": {"author": "Ververis, A., Kyriakou, S., Paraskeva, H., Panayiotidis, M.I. et al.",
                "title": "Chemical Characterization and Assessment of the Neuroprotective Potential of Euphrasia officinalis",
                "journal": "International Journal of Molecular Sciences", "year": "2024", "volume": "25", "number": "23", "pages": "12902",
                "doi": "10.3390/ijms252312902"},
     "abstract": "Eyebright (Euphrasia officinalis), used in folk medicine for eye disorders and memory loss, was extracted with solvents of different polarities. The extracts showed notable antioxidant capacity, and five extracts had significant anti-neurotoxic properties, enhancing cell viability by 17.5-22.6% in human neuroblastoma cells exposed to amyloid-beta peptides, highlighting the neuroprotective potential of eyebright."},
]

if __name__ == "__main__":
    apply(SOURCES)
