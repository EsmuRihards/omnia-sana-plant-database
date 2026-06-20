#!/usr/bin/env python3
"""Batch 10 (final) of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: hyssopus_officinalis, inonotus_obliquus, juniperus_communis, lactuca_virosa,
lavandula_angustifolia. Sources verified via the PubMed MCP; DOIs pre-checked.
Lactuca refs are genus/congener-level (L. serriola, L. sativa, Lactuca contact allergy)
as wild-lettuce-specific literature is thin; the L. virosa lactucin study was already
in the database."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- hyssopus_officinalis (hyssop) ----
    {"citekey": "atazhanova2024hyssopus", "plant": "hyssopus_officinalis", "study_type": "traditional",
     "fields": {"author": "Atazhanova, G., Ishmuratova, M., Levaya, Y., Smagulov, M. and Lakomkina, Y.",
                "title": "The Genus Hyssopus: Traditional Use, Phytochemicals and Pharmacological Properties",
                "journal": "Plants (Basel)", "year": "2024", "volume": "13", "number": "12", "pages": "1683",
                "doi": "10.3390/plants13121683"},
     "abstract": "The genus Hyssopus includes seven plant species rich in various groups of biologically active substances with a wide spectrum of pharmacological action. This review provides a comprehensive overview of the botanical research, extraction methods, chemical composition (mono- and sesquiterpenoids, flavonoids, alkaloids) and pharmacological activity of Hyssopus plants, including Hyssopus officinalis, noting that composition depends on growth location, weather, chemotype and extraction method."},
    {"citekey": "sharifirad2022hyssopus", "plant": "hyssopus_officinalis", "study_type": "traditional",
     "fields": {"author": "Sharifi-Rad, J., Quispe, C., Kumar, M., Akram, M. et al.",
                "title": "Hyssopus Essential Oil: An Update of Its Phytochemistry, Biological Activities, and Safety Profile",
                "journal": "Oxidative Medicine and Cellular Longevity", "year": "2022", "volume": "2022", "pages": "8442734",
                "doi": "10.1155/2022/8442734"},
     "abstract": "Hyssopus species are used as herbal remedies for cold, cough, loss of appetite, fungal infection and spasmodic conditions. The important active constituents of the essential oils are pinene, pinocamphone, isopinocamphone and other terpenoids, alongside flavonoids and phenolic acids. Extracts show antiviral and antifungal activities in vitro and plasma-membrane-relaxant, cytotoxic and sedative effects in vivo; the plant is considered relatively safe at culinary levels, though more safety studies are needed."},
    {"citekey": "gharakhanibeni2022hyssop", "plant": "hyssopus_officinalis", "study_type": "preclinical",
     "fields": {"author": "Gharakhani-Beni, A., Ghasemi Pirbalouti, A., Javanmard, H., Soleymani, A. and Golparvar, A.",
                "title": "Chemical compositions, yield and antioxidant activity of the essential oil of hyssop (Hyssopus officinalis L.) under intercropping with fenugreek",
                "journal": "Natural Product Research", "year": "2022", "volume": "37", "number": "4", "pages": "675-680",
                "doi": "10.1080/14786419.2022.2078971"},
     "abstract": "The effect of intercropping hyssop (Hyssopus officinalis) with fenugreek on the hyssop essential oil was studied. Sole cropping gave the highest essential-oil yield and the highest contents of major constituents (cis- and trans-pinocamphone and beta-pinene), while intercropping with fenugreek increased the antioxidant activity of the hyssop essential oil, illustrating how cultivation conditions modulate hyssop's volatile composition and antioxidant capacity."},

    # ---- inonotus_obliquus (chaga) ----
    {"citekey": "camilleri2024chaga", "plant": "inonotus_obliquus", "study_type": "traditional",
     "fields": {"author": "Camilleri, E., Blundell, R., Baral, B., Karpinski, T.M. et al.",
                "title": "A brief overview of the medicinal and nutraceutical importance of Inonotus obliquus (chaga) mushrooms",
                "journal": "Heliyon", "year": "2024", "volume": "10", "number": "15", "pages": "e35638",
                "doi": "10.1016/j.heliyon.2024.e35638"},
     "abstract": "This review explores chaga mushrooms (Inonotus obliquus), focusing on their phytochemical composition, health-promoting attributes and mechanisms of action. It highlights chaga's anticancer, antioxidant, anti-diabetic, anti-inflammatory, antimicrobial and immunomodulating properties, underscoring its importance in the medicinal sector and its pharmacological potential."},
    {"citekey": "lu2021chagapoly", "plant": "inonotus_obliquus", "study_type": "traditional",
     "fields": {"author": "Lu, Y., Jia, Y., Xue, Z., Li, N. et al.",
                "title": "Recent Developments in Inonotus obliquus (Chaga mushroom) Polysaccharides: Isolation, Structural Characteristics, Biological Activities and Application",
                "journal": "Polymers (Basel)", "year": "2021", "volume": "13", "number": "9", "pages": "1441",
                "doi": "10.3390/polym13091441"},
     "abstract": "Inonotus obliquus (chaga) polysaccharide (IOPS) is one of the major bioactive components of chaga, possessing antitumor, antioxidant, anti-virus, hypoglycemic and hypolipidemic activities. This review summarises advances in the extraction, purification, structural characteristics and biological activities of IOPS and its possible mechanisms, suggesting IOPS as a potential candidate for the treatment of cancers and type 2 diabetes."},
    {"citekey": "kobus2024chaga", "plant": "inonotus_obliquus", "study_type": "preclinical",
     "fields": {"author": "Kobus, Z., Krzywicka, M., Blicharz-Kania, A., Bosacka, A. et al.",
                "title": "Impact of Incorporating Dried Chaga Mushroom (Inonotus obliquus) into Gluten-Free Bread on Its Antioxidant and Sensory Characteristics",
                "journal": "Molecules", "year": "2024", "volume": "29", "number": "16", "pages": "3801",
                "doi": "10.3390/molecules29163801"},
     "abstract": "Gluten-free bread enriched with chaga (Inonotus obliquus) mushroom flour showed increased polyphenol and flavonoid content and enhanced antioxidant activity (DPPH, FRAP), with the highest levels at 20% chaga, demonstrating the antioxidant value of chaga; however sensory acceptability limited practical addition to about 10%."},

    # ---- juniperus_communis (juniper) ----
    {"citekey": "pepeljnjak2005juniper", "plant": "juniperus_communis", "study_type": "preclinical",
     "fields": {"author": "Pepeljnjak, S., Kosalec, I., Kalodera, Z. and Blazević, N.",
                "title": "Antimicrobial activity of juniper berry essential oil (Juniperus communis L., Cupressaceae)",
                "journal": "Acta Pharmaceutica", "year": "2005", "volume": "55", "number": "4", "pages": "417-422",
                "url": "https://pubmed.ncbi.nlm.nih.gov/16375831/"},
     "abstract": "Juniper berry essential oil (main compounds alpha-pinene, beta-pinene, sabinene, limonene) was evaluated against sixteen bacterial species, seven yeast-like fungi, three yeasts and four dermatophytes. The oil showed similar bactericidal activity against Gram-positive and Gram-negative bacteria and strong fungicidal activity against yeasts and dermatophytes, with the strongest activity against Candida spp. and dermatophytes, supporting the antimicrobial use of juniper."},
    {"citekey": "peruc2020juniper", "plant": "juniperus_communis", "study_type": "preclinical",
     "fields": {"author": "Peruč, D., Tićac, B., Broznić, D., Maglica, Ž. et al.",
                "title": "Juniperus communis essential oil limits the biofilm formation of Mycobacterium avium and Mycobacterium intracellulare on polystyrene in a temperature-dependent manner",
                "journal": "International Journal of Environmental Health Research", "year": "2020", "volume": "32", "number": "1", "pages": "141-154",
                "doi": "10.1080/09603123.2020.1741519"},
     "abstract": "Juniperus communis essential oil was investigated against nontuberculous mycobacteria and their biofilm formation. The combination of the essential oil and increasing temperature synergistically reduced biofilm formation on a polystyrene surface, and a significant antibiofilm effect was found at subinhibitory concentrations, suggesting a potential role for juniper essential oil as an alternative disinfectant."},
    {"citekey": "markovic2024juniper", "plant": "juniperus_communis", "study_type": "preclinical",
     "fields": {"author": "Marković, T., Popović, S., Matić, S., Mitrović, M. et al.",
                "title": "Insights into Molecular Mechanisms of Anticancer Activity of Juniperus communis Essential Oil in HeLa and HCT 116 Cells",
                "journal": "Plants (Basel)", "year": "2024", "volume": "13", "number": "17", "pages": "2351",
                "doi": "10.3390/plants13172351"},
     "abstract": "Juniperus communis berry essential oil was studied for antitumor potential in cervical cancer HeLa and colorectal HCT 116 cells. It produced concentration-dependent reductions in cell viability and long-term cytotoxic effects, induced the intrinsic apoptosis pathway (cleaved caspase-3, increased Bax/Bcl-2, cytochrome C release) and arrested HeLa cells in the S phase, highlighting juniper berry essential oil as a natural agent with anticancer potential."},

    # ---- lactuca_virosa (wild lettuce; genus/congener-level refs) ----
    {"citekey": "ullah2022lactuca", "plant": "lactuca_virosa", "study_type": "preclinical",
     "fields": {"author": "Ullah, M.I., Anwar, R., Kamran, S., Gul, B. et al.",
                "title": "Evaluation of the Anxiolytic and Anti-Epileptogenic Potential of Lactuca serriola Seed Using Pentylenetetrazol-Induced Kindling in Mice and Metabolic Profiling of Its Bioactive Extract",
                "journal": "Antioxidants (Basel)", "year": "2022", "volume": "11", "number": "11", "pages": "2232",
                "doi": "10.3390/antiox11112232"},
     "abstract": "Seed extracts of Lactuca serriola (prickly lettuce, a wild-lettuce congener) showed anxiolytic potential (increased open-arm time in the elevated plus maze, reduced head-dipping), sedative effects (reduced sleep latency and prolonged barbiturate sleep) and anti-epileptogenic activity (reduced seizure score in PTZ-kindling), with antioxidant effects in brain tissue, supporting the ethnopharmacological sedative use of wild lettuce."},
    {"citekey": "lee2024lactuca", "plant": "lactuca_virosa", "study_type": "preclinical",
     "fields": {"author": "Lee, M., Park, J., Cho, W., Jun, Y. et al.",
                "title": "Lactuca L. Extract Enhances Sleep Duration Through Upregulation of Adenosine A1 Receptor and GABA-A Receptor Subunits in Pentobarbital-Injected Mice",
                "journal": "Journal of Medicinal Food", "year": "2024", "volume": "27", "number": "7", "pages": "661-668",
                "doi": "10.1089/jmf.2023.K.0250"},
     "abstract": "A Lactuca (lettuce) extract was investigated in pentobarbital-induced sleep in mice. The extract significantly reduced sleep latency and increased sleep duration, and increased the expression of the adenosine A1 receptor and several GABA-A receptor subunits in the brain, indicating it could be used to develop natural products that improve sleep quality and duration — a mechanism relevant to wild lettuce's traditional sedative use."},
    {"citekey": "paulsen2015lettuce", "plant": "lactuca_virosa", "study_type": "traditional",
     "fields": {"author": "Paulsen, E. and Andersen, K.E.",
                "title": "Lettuce contact allergy",
                "journal": "Contact Dermatitis", "year": "2015", "volume": "74", "number": "2", "pages": "67-75",
                "doi": "10.1111/cod.12458"},
     "abstract": "Lettuce (Lactuca) and its varieties are a well-known, rarely reported cause of contact allergy, mostly occupational, with sesquiterpene lactones implicated. The review presents data on lettuce contact allergy and recommends patch testing with freshly cut lettuce supplemented with Compositae mix — a relevant safety/contraindication consideration for Compositae-sensitised individuals using wild lettuce preparations."},

    # ---- lavandula_angustifolia (lavender) ----
    {"citekey": "tan2023essentialoils", "plant": "lavandula_angustifolia", "study_type": "systematic-review",
     "fields": {"author": "Tan, L., Liao, F.F., Long, L.Z., Ma, X.C. et al.",
                "title": "Essential oils for treating anxiety: a systematic review of randomized controlled trials and network meta-analysis",
                "journal": "Frontiers in Public Health", "year": "2023", "volume": "11", "pages": "1144404",
                "doi": "10.3389/fpubh.2023.1144404"},
     "abstract": "A systematic review and network meta-analysis of 44 randomized controlled trials (3419 patients, 10 essential oils) for anxiety. Essential oils significantly reduced State and Trait Anxiety Inventory scores and lowered systolic blood pressure and heart rate; in the network analysis lavender (Lavandula angustifolia) was among the most effective and most recommended essential oils for treating anxiety."},
    {"citekey": "doslucena2021lavender", "plant": "lavandula_angustifolia", "study_type": "rct",
     "fields": {"author": "Dos Reis Lucena, L., Dos Santos-Junior, J.G., Tufik, S. and Hachul, H.",
                "title": "Lavender essential oil on postmenopausal women with insomnia: Double-blind randomized trial",
                "journal": "Complementary Therapies in Medicine", "year": "2021", "volume": "59", "pages": "102726",
                "doi": "10.1016/j.ctim.2021.102726"},
     "abstract": "A double-blind randomized controlled trial of Lavandula angustifolia essential oil inhalation versus placebo for 29 days in 35 postmenopausal women with insomnia. Although no significant between-group difference was seen in the primary sleep-quality outcome, the lavender group showed a significant decrease in sleep-onset latency and depression levels, reduced hot flashes and increased sleep efficiency on polysomnography compared to baseline."},
    {"citekey": "moss2003lavender", "plant": "lavandula_angustifolia", "study_type": "rct",
     "fields": {"author": "Moss, M., Cook, J., Wesnes, K. and Duckett, P.",
                "title": "Aromas of rosemary and lavender essential oils differentially affect cognition and mood in healthy adults",
                "journal": "International Journal of Neuroscience", "year": "2003", "volume": "113", "number": "1", "pages": "15-38",
                "doi": "10.1080/00207450390161903"},
     "abstract": "A randomized controlled trial assessed the olfactory impact of lavender (Lavandula angustifolia) and rosemary essential oils on cognition and mood in 144 healthy volunteers. Lavender produced a decrement in working-memory performance and slower reaction times compared with controls, but the lavender group was significantly more content than controls, indicating lavender aroma produces objective cognitive and subjective mood effects consistent with a calming/sedative action."},
]

if __name__ == "__main__":
    apply(SOURCES)
