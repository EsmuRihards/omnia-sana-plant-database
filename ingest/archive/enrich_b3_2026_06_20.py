#!/usr/bin/env python3
"""Batch 3 of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: bacopa_monnieri, betula_pendula, bistorta_officinalis, borago_officinalis,
calendula_officinalis. Sources verified via the PubMed MCP; DOIs pre-checked against
bibliography.bibtex."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- bacopa_monnieri (brahmi) ----
    {"citekey": "calabrese2008bacopa", "plant": "bacopa_monnieri", "study_type": "rct",
     "fields": {"author": "Calabrese, C., Gregory, W.L., Leo, M., Kraemer, D. et al.",
                "title": "Effects of a standardized Bacopa monnieri extract on cognitive performance, anxiety, and depression in the elderly: a randomized, double-blind, placebo-controlled trial",
                "journal": "Journal of Alternative and Complementary Medicine", "year": "2008", "volume": "14", "number": "6", "pages": "707-713",
                "doi": "10.1089/acm.2008.0018"},
     "abstract": "A randomized, double-blind, placebo-controlled trial evaluated a standardized Bacopa monnieri whole-plant dry extract on cognitive function, affect, safety and tolerability in healthy elderly participants. Bacopa improved measures of cognitive performance (e.g. delayed word recall and Stroop task) and reduced anxiety and depression scores relative to placebo, with good tolerability, supporting its traditional use as a memory and learning enhancer."},
    {"citekey": "lorca2022nootropics", "plant": "bacopa_monnieri", "study_type": "systematic-review",
     "fields": {"author": "Lorca, C., Mulet, M., Arévalo-Caro, C., Sanchez, M.Á. et al.",
                "title": "Plant-derived nootropics and human cognition: A systematic review",
                "journal": "Critical Reviews in Food Science and Nutrition", "year": "2022", "volume": "63", "number": "22", "pages": "5521-5545",
                "doi": "10.1080/10408398.2021.2021137"},
     "abstract": "Substances with modulatory capabilities on human cognition have been revered as nootropics, and the plant kingdom provides most of the currently available natural nootropics. This systematic review provides state-of-the-art information on plant-derived nootropics and their effects on human cognition, among them Bacopa monnieri, reviewing the clinical evidence for memory and cognitive enhancement."},
    {"citekey": "fatima2022bacopa", "plant": "bacopa_monnieri", "study_type": "traditional",
     "fields": {"author": "Fatima, U., Roy, S., Ahmad, S., Ali, S. et al.",
                "title": "Pharmacological attributes of Bacopa monnieri extract: Current updates and clinical manifestation",
                "journal": "Frontiers in Nutrition", "year": "2022", "volume": "9", "pages": "972379",
                "doi": "10.3389/fnut.2022.972379"},
     "abstract": "Bacopa monnieri has been used for centuries in Ayurvedic medicine as a memory and learning enhancer, sedative and anti-epileptic. This review highlights the health benefits of Bacopa monnieri extracts, focusing on anti-cancer and neurodegenerative diseases, and the molecular mechanisms underlying its cognition-enhancing, neuroprotective and therapeutic effects, as well as its toxicity, safety and synergistic potential."},

    # ---- betula_pendula (silver birch) ----
    {"citekey": "rastogi2014betula", "plant": "betula_pendula", "study_type": "traditional",
     "fields": {"author": "Rastogi, S., Pandey, M.M. and Kumar Singh Rawat, A.",
                "title": "Medicinal plants of the genus Betula — traditional uses and a phytochemical-pharmacological review",
                "journal": "Journal of Ethnopharmacology", "year": "2014", "volume": "159", "pages": "62-83",
                "doi": "10.1016/j.jep.2014.11.010"},
     "abstract": "Trees and shrubs of the genus Betula (Betulaceae) inhabit temperate and boreal zones of the northern hemisphere. The healing properties of Betula bark, leaves and bark extracts have long been known in traditional medicine for skin diseases, rheumatism, gout and as a diuretic. This review compiles the traditional uses, phytochemistry (triterpenes such as betulin and betulinic acid, flavonoids, phenolics) and pharmacological activities of Betula species."},
    {"citekey": "penkov2018betula", "plant": "betula_pendula", "study_type": "preclinical",
     "fields": {"author": "Penkov, D., Andonova, V., Delev, D. and Kostadinov, I.",
                "title": "Antioxidant Activity of Dry Birch (Betula pendula) Leaves Extract",
                "journal": "Folia Medica", "year": "2018", "volume": "60", "number": "4", "pages": "571-579",
                "doi": "10.2478/folmed-2018-0035"},
     "abstract": "Betula pendula has been used in traditional medicine since ancient times, and birch leaf extracts exhibit a number of pharmacological activities. This study evaluated the antioxidant activity of a dry birch leaf extract, which demonstrated significant free-radical-scavenging and antioxidant capacity attributable to its phenolic and flavonoid content."},
    {"citekey": "sevastreberghian2023betula", "plant": "betula_pendula", "study_type": "preclinical",
     "fields": {"author": "Sevastre-Berghian, A.C., Ielciu, I., Bab, T., Olah, N.K. et al.",
                "title": "Betula pendula Leaf Extract Targets the Interplay between Brain Oxidative Stress, Inflammation, and NF-kB Pathways in Amyloid Abeta-Treated Rats",
                "journal": "Antioxidants (Basel)", "year": "2023", "volume": "12", "number": "12", "pages": "2110",
                "doi": "10.3390/antiox12122110"},
     "abstract": "Chemical analyses of a Betula pendula leaf extract revealed high amounts of polyphenol carboxylic acids and flavonoids. In amyloid-beta-treated rats, the leaf extract reduced brain oxidative stress and inflammation and modulated the NF-kB pathway, improving behavioural and biochemical markers, suggesting neuroprotective potential of the birch leaf extract."},

    # ---- bistorta_officinalis (bistort) ----
    {"citekey": "pawlowska2020bistort", "plant": "bistorta_officinalis", "study_type": "preclinical",
     "fields": {"author": "Pawłowska, K.A., Hałasa, R., Dudek, M.K., Majdan, M. et al.",
                "title": "Antibacterial and anti-inflammatory activity of bistort (Bistorta officinalis) aqueous extract and its major components: justification of the usage of the medicinal plant material as a traditional topical agent",
                "journal": "Journal of Ethnopharmacology", "year": "2020", "volume": "260", "pages": "113077",
                "doi": "10.1016/j.jep.2020.113077"},
     "abstract": "Bistort rhizome (Bistorta officinalis) is traditionally used in Europe and Asia for diarrhea and as a topical agent for skin conditions; it contains mostly condensed flavan-3-ol-derived tannins. The aqueous extract and its major components showed antibacterial and anti-inflammatory activity, justifying the traditional use of the rhizome as an astringent topical agent."},
    {"citekey": "jovanovic2020bistort", "plant": "bistorta_officinalis", "study_type": "preclinical",
     "fields": {"author": "Jovanović, M., Morić, I., Nikolić, B., Pavić, A. et al.",
                "title": "Anti-Virulence Potential and In Vivo Toxicity of Persicaria maculosa and Bistorta officinalis Extracts",
                "journal": "Molecules", "year": "2020", "volume": "25", "number": "8", "pages": "1811",
                "doi": "10.3390/molecules25081811"},
     "abstract": "The anti-virulence potential and safety of ethanol extracts of two medicinal plants, Persicaria maculosa and Bistorta officinalis, were evaluated for the first time. The extracts showed anti-virulence activity against bacterial pathogens together with a favourable in vivo toxicity (safety) profile, supporting their potential use as antimicrobial/anti-virulence agents."},
    {"citekey": "duwiejua1994bistort", "plant": "bistorta_officinalis", "study_type": "preclinical",
     "fields": {"author": "Duwiejua, M., Zeitlin, I.J., Waterman, P.G. and Gray, A.I.",
                "title": "Anti-inflammatory activity of Polygonum bistorta, Guaiacum officinale and Hamamelis virginiana in rats",
                "journal": "Journal of Pharmacy and Pharmacology", "year": "1994", "volume": "46", "number": "4", "pages": "286-290",
                "doi": "10.1111/j.2042-7158.1994.tb03795.x"},
     "abstract": "Aqueous ethanolic extract of Polygonum bistorta (Bistorta officinalis) significantly suppressed carrageenan-induced rat paw oedema in a dose-dependent manner and inhibited both the acute and chronic phases of adjuvant-induced arthritis; given after the onset of inflammation it reversed the course of the swelling. The results confirm that bistort rhizome contains anti-inflammatory substances, supporting its traditional anti-inflammatory and astringent use."},

    # ---- borago_officinalis (borage) ----
    {"citekey": "slama2024borago", "plant": "borago_officinalis", "study_type": "traditional",
     "fields": {"author": "Slama, M., Slougui, N., Benaissa, A., Nekkaa, A. et al.",
                "title": "Borago officinalis L.: A Review on Extraction, Phytochemical, and Pharmacological Activities",
                "journal": "Chemistry & Biodiversity", "year": "2024", "volume": "21", "number": "5", "pages": "e202301822",
                "doi": "10.1002/cbdv.202301822"},
     "abstract": "Borago officinalis L. (Boraginaceae) is used in traditional medicine for respiratory disorders, colds, influenza, diarrhea, cramps, inflammation, palpitation, hypertension and menopausal symptoms. Its antioxidant, antimicrobial, anticancer, anti-inflammatory and anti-obesity activities relate to its rich content of phenolic acids, flavonoids, anthocyanins, alkaloids and terpenes from leaves, flowers, seeds and roots. The review summarizes extraction, phytochemistry, pharmacology and toxicity."},
    {"citekey": "michalak2023borago", "plant": "borago_officinalis", "study_type": "preclinical",
     "fields": {"author": "Michalak, M., Zagórska-Dziok, M., Klimek-Szczykutowicz, M. and Szopa, A.",
                "title": "Phenolic Profile and Comparison of the Antioxidant, Anti-Ageing, Anti-Inflammatory, and Protective Activities of Borago officinalis Extracts on Skin Cells",
                "journal": "Molecules", "year": "2023", "volume": "28", "number": "2", "pages": "868",
                "doi": "10.3390/molecules28020868"},
     "abstract": "Methanol and water-methanol extracts of borage (Borago officinalis) herb were analysed for phenolic profile and biological activity. Twelve flavonoids and phenolic acids were identified. In vitro tests on human keratinocytes and fibroblasts showed the extracts reduced intracellular reactive oxygen species, inhibited protein denaturation, lipoxygenase and proteinase (anti-inflammatory), and inhibited collagenase and elastase (anti-ageing), indicating borage extracts protect skin cells."},
    {"citekey": "ghasemian2016borago", "plant": "borago_officinalis", "study_type": "traditional",
     "fields": {"author": "Ghasemian, M., Owlia, S. and Owlia, M.B.",
                "title": "Review of Anti-Inflammatory Herbal Medicines",
                "journal": "Advances in Pharmacological Sciences", "year": "2016", "volume": "2016", "pages": "9130979",
                "doi": "10.1155/2016/9130979"},
     "abstract": "Inflammation underlies a wide range of diseases including rheumatic and immune-mediated conditions. This review introduces medicinal herbs whose anti-inflammatory effects have been evaluated in clinical and experimental studies, among them Borago officinalis (alongside Curcuma longa, Zingiber officinale, Rosmarinus officinalis, evening primrose and Devil's claw), supporting a multidimensional herbal approach to inflammation."},

    # ---- calendula_officinalis (marigold) ----
    {"citekey": "givol2019calendula", "plant": "calendula_officinalis", "study_type": "systematic-review",
     "fields": {"author": "Givol, O., Kornhaber, R., Visentin, D., Cleary, M. et al.",
                "title": "A systematic review of Calendula officinalis extract for wound healing",
                "journal": "Wound Repair and Regeneration", "year": "2019", "volume": "27", "number": "5", "pages": "548-561",
                "doi": "10.1111/wrr.12737"},
     "abstract": "This systematic review evaluated Calendula officinalis flower extract as monotherapy for wound healing in vivo, with 14 studies meeting inclusion criteria (7 animal experiments and 7 clinical trials). Acute wound healing showed faster resolution of the inflammation phase and increased granulation tissue with calendula. Clinical results for chronic wounds, burns and radiation dermatitis were mixed. The review identified evidence for beneficial effects of C. officinalis extract for wound healing, consistent with its traditional use."},
    {"citekey": "shahane2023calendula", "plant": "calendula_officinalis", "study_type": "traditional",
     "fields": {"author": "Shahane, K., Kshirsagar, M., Tambe, S., Jain, D. et al.",
                "title": "An Updated Review on the Multifaceted Therapeutic Potential of Calendula officinalis L.",
                "journal": "Pharmaceuticals (Basel)", "year": "2023", "volume": "16", "number": "4", "pages": "611",
                "doi": "10.3390/ph16040611"},
     "abstract": "Calendula officinalis contains flavonoids, triterpenoids, glycosides, saponins, carotenoids, volatile oil and sterols, conferring anti-inflammatory, anti-cancer, antihelminthic, antidiabetic, wound-healing, hepatoprotective and antioxidant activities, and it is used in burns and gastrointestinal, gynecological, ocular and skin conditions. The review summarizes recent research on its therapeutic applications, molecular mechanisms and clinical studies."},
    {"citekey": "saffari2016calendula", "plant": "calendula_officinalis", "study_type": "rct",
     "fields": {"author": "Saffari, E., Mohammad-Alizadeh-Charandabi, S., Adibpour, M., Mirghafourvand, M. et al.",
                "title": "Comparing the effects of Calendula officinalis and clotrimazole on vaginal Candidiasis: A randomized controlled trial",
                "journal": "Women & Health", "year": "2016", "volume": "57", "number": "10", "pages": "1145-1160",
                "doi": "10.1080/03630242.2016.1263272"},
     "abstract": "This triple-blind randomized controlled trial (n=150) compared Calendula officinalis vaginal cream with clotrimazole for vaginal Candidiasis. Calendula vaginal cream was effective in treating vaginal Candidiasis, with a delayed but greater long-term effect than clotrimazole at the second follow-up, and improved sexual function similarly in both groups, supporting the antifungal and anti-inflammatory use of calendula."},
]

if __name__ == "__main__":
    apply(SOURCES)
