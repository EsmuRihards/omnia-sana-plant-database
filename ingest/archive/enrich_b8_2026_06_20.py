#!/usr/bin/env python3
"""Batch 8 of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: filipendula_ulmaria, galium_aparine, ganoderma_lingzhi, ginkgo_biloba,
glycyrrhiza_glabra. Sources verified via the PubMed MCP; DOIs pre-checked.
Some galium refs are genus/congener-level (G. verum, G. odoratum)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- filipendula_ulmaria (meadowsweet) ----
    {"citekey": "samardzic2017filipendula", "plant": "filipendula_ulmaria", "study_type": "preclinical",
     "fields": {"author": "Samardžić, S., Arsenijević, J., Božić, D., Milenković, M. et al.",
                "title": "Antioxidant, anti-inflammatory and gastroprotective activity of Filipendula ulmaria (L.) Maxim. and Filipendula vulgaris Moench",
                "journal": "Journal of Ethnopharmacology", "year": "2017", "volume": "213", "pages": "132-137",
                "doi": "10.1016/j.jep.2017.11.013"},
     "abstract": "Meadowsweet (Filipendula ulmaria) is used in folk medicine for antirheumatic, antipyretic and anti-ulcer properties. Lyophilised flower infusions and isolated flavonoids (spiraeoside) and the tannin tellimagrandin II showed antioxidant (DPPH, FRAP) and anti-inflammatory activity (inhibition of eicosanoid biosynthesis in human platelets), and the infusions preserved gastric mucosal integrity in an ethanol-induced gastric injury model in rats, supporting the traditional use."},
    {"citekey": "andonova2024meadowsweet", "plant": "filipendula_ulmaria", "study_type": "preclinical",
     "fields": {"author": "Andonova, T., Muhovski, Y., Apostolova, E., Naimov, S. et al.",
                "title": "DNA-Protective, Antioxidant and Anti-Carcinogenic Potential of Meadowsweet (Filipendula ulmaria) Dry Tincture",
                "journal": "Antioxidants (Basel)", "year": "2024", "volume": "13", "number": "10", "pages": "1200",
                "doi": "10.3390/antiox13101200"},
     "abstract": "A dry tincture of meadowsweet (Filipendula ulmaria) was analysed by HPLC (major phenolics: salicylic acid 18.84 mg/g, rutin, p-coumaric acid, quercetin, rosmarinic acid) and bioassayed. The high antioxidant potential was confirmed by four assays, and the study reported for the first time highly protective activity against oxidative DNA damage and an antiproliferative effect against hepatocellular carcinoma (HepG2) cells."},
    {"citekey": "vanderauwera2023filipendula", "plant": "filipendula_ulmaria", "study_type": "preclinical",
     "fields": {"author": "Van der Auwera, A., Peeters, L., Foubert, K., Piazza, S. et al.",
                "title": "In Vitro Biotransformation and Anti-Inflammatory Activity of Constituents and Metabolites of Filipendula ulmaria",
                "journal": "Pharmaceutics", "year": "2023", "volume": "15", "number": "4", "pages": "1291",
                "doi": "10.3390/pharmaceutics15041291"},
     "abstract": "Filipendula ulmaria (meadowsweet) is widely used in phytotherapy against inflammatory diseases. An in vitro gastrointestinal biotransformation model showed glycosylated flavonoids (rutin, spiraeoside) decrease while aglycones (quercetin, apigenin, naringenin, kaempferol) increase in the colon; both the genuine and metabolised extracts inhibited COX-1 more than COX-2, indicating the anti-inflammatory activity arises from an additive/synergistic effect of constituents and gut-microbiota metabolites."},

    # ---- galium_aparine (cleavers; some genus/congener-level refs) ----
    {"citekey": "laanet2023galium", "plant": "galium_aparine", "study_type": "preclinical",
     "fields": {"author": "Laanet, P.R., Saar-Reismaa, P., Jõul, P., Bragina, O. and Vaher, M.",
                "title": "Phytochemical Screening and Antioxidant Activity of Selected Estonian Galium Species",
                "journal": "Molecules", "year": "2023", "volume": "28", "number": "6", "pages": "2867",
                "doi": "10.3390/molecules28062867"},
     "abstract": "Three Galium species from Estonia, including Galium aparine (cleavers), were characterised for non-volatile and volatile phytochemicals and antioxidant activity. High concentrations of polyphenols, flavonoids and iridoids were quantified (asperuloside, asperulosidic acid, chlorogenic acid as key compounds), and all Galium species exhibited strong antioxidant capacity (ORAC), supporting the antioxidant potential of cleavers."},
    {"citekey": "antoniak2023galium", "plant": "galium_aparine", "study_type": "preclinical",
     "fields": {"author": "Antoniak, K., Studzińska-Sroka, E., Szymański, M., Dudek-Makuch, M. et al.",
                "title": "Antiangiogenic, Anti-Inflammatory and Antioxidant Properties of Bidens tripartita Herb, Galium verum Herb and Rumex hydrolapathum Root",
                "journal": "Molecules", "year": "2023", "volume": "28", "number": "13", "pages": "4966",
                "doi": "10.3390/molecules28134966"},
     "abstract": "Ethanolic extracts of three plants including Galium verum herb (a cleavers congener) were tested on endothelial cells. The Galium verum extract showed anti-inflammatory activity (reducing pro-inflammatory IL-8 and IL-6) and antioxidant activity (DPPH, FRAP) related to its polyphenol content, with effects on angiogenesis-related factors, indicating potential in disorders linked to inflammation and free-radical formation."},
    {"citekey": "razzivina2024galium", "plant": "galium_aparine", "study_type": "preclinical",
     "fields": {"author": "Razzivina, V., Vasiljeva, A., Kronberga, A., Skudrins, G. et al.",
                "title": "Phenolic Content and Anti-Inflammatory Activity of Cultivated and Wild-Type Galium odoratum Extracts in Murine Bone Marrow-Derived Macrophages",
                "journal": "Antioxidants (Basel)", "year": "2024", "volume": "13", "number": "12", "pages": "1447",
                "doi": "10.3390/antiox13121447"},
     "abstract": "Galium odoratum (sweet woodruff, a cleavers congener) extracts from cultivated and wild plants were analysed. Phenolic content and antioxidant activity increased under sun-grown conditions (chlorogenic acid and rutin major contributors), and the extracts exhibited anti-inflammatory activity, reducing the M1 macrophage population, highlighting the antioxidant and anti-inflammatory potential of Galium species."},

    # ---- ganoderma_lingzhi (reishi) ----
    {"citekey": "li2024ganoderma", "plant": "ganoderma_lingzhi", "study_type": "preclinical",
     "fields": {"author": "Li, W., Zhou, Q., Lv, B., Li, N. et al.",
                "title": "Ganoderma lucidum Polysaccharide Supplementation Significantly Activates T-Cell-Mediated Antitumor Immunity and Enhances Anti-PD-1 Immunotherapy Efficacy in Colorectal Cancer",
                "journal": "Journal of Agricultural and Food Chemistry", "year": "2024", "volume": "72", "number": "21", "pages": "12072-12082",
                "doi": "10.1021/acs.jafc.3c08385"},
     "abstract": "Ganoderma lucidum (reishi) polysaccharide (GLP) significantly inhibited tumor growth and activated antitumor immunity in colorectal cancer: it increased cytotoxic CD8 T cells and Th1 helper cells while decreasing immunosuppressive Tregs, alleviated gut microbiota dysbiosis, increased short-chain fatty acid production, and enhanced the efficacy of anti-PD-1 immunotherapy, supporting reishi as an immunomodulatory prebiotic."},
    {"citekey": "cai2017ganoderma", "plant": "ganoderma_lingzhi", "study_type": "preclinical",
     "fields": {"author": "Cai, Q., Li, Y. and Pei, G.",
                "title": "Polysaccharides from Ganoderma lucidum attenuate microglia-mediated neuroinflammation and modulate microglial phagocytosis and behavioural response",
                "journal": "Journal of Neuroinflammation", "year": "2017", "volume": "14", "number": "1", "pages": "63",
                "doi": "10.1186/s12974-017-0839-0"},
     "abstract": "Ganoderma lucidum polysaccharides (GLP) down-regulated LPS- or amyloid-beta-induced pro-inflammatory cytokines and promoted anti-inflammatory cytokine expression in microglia, and attenuated inflammation-related microglial migration, morphological alterations and phagocytosis, suggesting the neuroprotective function of reishi polysaccharides is achieved through modulation of microglial inflammatory and behavioural responses."},
    {"citekey": "zheng2023ganoderma", "plant": "ganoderma_lingzhi", "study_type": "preclinical",
     "fields": {"author": "Zheng, G., Zhao, Y., Li, Z., Hua, Y. et al.",
                "title": "Ganoderma lucidum spore powder and derived triterpenes attenuate atherosclerosis and aortic calcification by stimulating ABCA1/G1-mediated macrophage cholesterol efflux and inactivating RUNX2-mediated VSMC osteogenesis",
                "journal": "Theranostics", "year": "2023", "volume": "13", "number": "4", "pages": "1325-1341",
                "doi": "10.7150/thno.80250"},
     "abstract": "Ganoderma lucidum spore powder (GLSP) and its triterpenes (ganoderic acids A, B, C6, G and ganodermanontriol) attenuated plaque area and aortic calcification in atherosclerotic mice by improving ABCA1/G1-mediated macrophage cholesterol efflux, reducing foam cells and inflammation, and inactivating RUNX2-mediated osteogenesis in vascular smooth muscle cells, suggesting reishi as a candidate against atherosclerosis and vascular calcification."},

    # ---- ginkgo_biloba ----
    {"citekey": "tan2015ginkgo", "plant": "ginkgo_biloba", "study_type": "systematic-review",
     "fields": {"author": "Tan, M.S., Yu, J.T., Tan, C.C., Wang, H.F. et al.",
                "title": "Efficacy and adverse effects of Ginkgo biloba for cognitive impairment and dementia: a systematic review and meta-analysis",
                "journal": "Journal of Alzheimer's Disease", "year": "2015", "volume": "43", "number": "2", "pages": "589-603",
                "doi": "10.3233/JAD-140837"},
     "abstract": "A systematic review and meta-analysis of nine randomized controlled trials (2561 patients, 22-26 weeks) of standardised Ginkgo biloba extract EGb761 for cognitive impairment and dementia. EGb761 at 240 mg/day was able to stabilise or slow decline in cognition, activities of daily living, behaviour and global clinical impression, especially in patients with neuropsychiatric symptoms, with no important safety concerns. (Note: the large negative GEM prevention RCT, DeKosky 2008, is already in the database.)"},
    {"citekey": "singh2019ginkgo", "plant": "ginkgo_biloba", "study_type": "traditional",
     "fields": {"author": "Singh, S.K., Srivastav, S., Castellani, R.J., Plascencia-Villa, G. and Perry, G.",
                "title": "Neuroprotective and Antioxidant Effect of Ginkgo biloba Extract Against AD and Other Neurological Disorders",
                "journal": "Neurotherapeutics", "year": "2019", "volume": "16", "number": "3", "pages": "666-674",
                "doi": "10.1007/s13311-019-00767-8"},
     "abstract": "Ginkgo biloba extract (GBE) is one of the most investigated herbal remedies for cognitive disorders and Alzheimer's disease, taken as a dietary supplement to improve memory and age-related cognitive decline, although its efficacy remains controversial. This review summarises the potential use and antioxidant mechanisms of GBE in the prevention of Alzheimer's disease and other neurodegenerative disorders."},
    {"citekey": "diamond2013ginkgo", "plant": "ginkgo_biloba", "study_type": "traditional",
     "fields": {"author": "Diamond, B.J. and Bailey, M.R.",
                "title": "Ginkgo biloba: indications, mechanisms, and safety",
                "journal": "Psychiatric Clinics of North America", "year": "2013", "volume": "36", "number": "1", "pages": "73-83",
                "doi": "10.1016/j.psc.2012.12.006"},
     "abstract": "Ginkgo biloba special extract (EGb761) is used in most randomized controlled trials, with indications including cognition and memory in Alzheimer disease, age-associated dementia, cerebral insufficiency and intermittent claudication. Mechanisms include increasing cerebral blood flow and antioxidant, anti-inflammatory and antiplatelet effects. Possible interactions with warfarin, MAO inhibitors and other drugs are reviewed for safety."},

    # ---- glycyrrhiza_glabra (licorice) ----
    {"citekey": "pastorino2018liquorice", "plant": "glycyrrhiza_glabra", "study_type": "traditional",
     "fields": {"author": "Pastorino, G., Cornara, L., Soares, S., Rodrigues, F. and Oliveira, M.B.P.P.",
                "title": "Liquorice (Glycyrrhiza glabra): A phytochemical and pharmacological review",
                "journal": "Phytotherapy Research", "year": "2018", "volume": "32", "number": "12", "pages": "2323-2339",
                "doi": "10.1002/ptr.6178"},
     "abstract": "Glycyrrhiza glabra (liquorice) contains phytocompounds such as glycyrrhizin, 18-beta-glycyrrhetinic acid, glabrin A and B and isoflavones. Pharmacological experiments show extracts and pure compounds exhibit a broad range of biological properties including antibacterial, anti-inflammatory, antiviral, antioxidant and antidiabetic activities. The review provides a critical, updated overview of liquorice composition and biological activities and its therapeutic potential."},
    {"citekey": "nazari2017licorice", "plant": "glycyrrhiza_glabra", "study_type": "traditional",
     "fields": {"author": "Nazari, S., Rameshrad, M. and Hosseinzadeh, H.",
                "title": "Toxicological Effects of Glycyrrhiza glabra (Licorice): A Review",
                "journal": "Phytotherapy Research", "year": "2017", "volume": "31", "number": "11", "pages": "1635-1650",
                "doi": "10.1002/ptr.5893"},
     "abstract": "This review gathers research on the toxicity of licorice (Glycyrrhiza glabra) and glycyrrhizin. G. glabra and glycyrrhizin salts are moderately toxic and need to be used with caution, especially in pregnancy. The most important side effects are hypertension and hypokalemia-induced secondary disorders, increased by prolonged use, decreased 11-beta-hydroxysteroid dehydrogenase activity, old age and female sex — key safety considerations for licorice use."},
    {"citekey": "batiha2020licorice", "plant": "glycyrrhiza_glabra", "study_type": "traditional",
     "fields": {"author": "El-Saber Batiha, G., Magdy Beshbishy, A., El-Mleeh, A., Abdel-Daim, M.M. and Prasad Devkota, H.",
                "title": "Traditional Uses, Bioactive Chemical Constituents, and Pharmacological and Toxicological Activities of Glycyrrhiza glabra L. (Fabaceae)",
                "journal": "Biomolecules", "year": "2020", "volume": "10", "number": "3", "pages": "352",
                "doi": "10.3390/biom10030352"},
     "abstract": "Glycyrrhiza glabra (licorice) has been traditionally used to treat respiratory disorders, fever, stomach ulcers, rheumatism, skin diseases and jaundice. Chemical analysis revealed liquiritin, liquiritigenin, glycyrrhizin, isoangustone A and many other constituents. Pharmacological activities include antimicrobial, antiviral, antiparasitic, antioxidant, antifungal, anticarcinogenic, anti-inflammatory and cytotoxic effects. The review covers its phytochemistry, pharmacology, pharmacokinetics and toxicity."},
]

if __name__ == "__main__":
    apply(SOURCES)
