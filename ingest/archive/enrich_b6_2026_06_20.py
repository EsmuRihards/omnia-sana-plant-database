#!/usr/bin/env python3
"""Batch 6 of the 2026-06-20 least-cited enrichment (5 plants x 3 PubMed sources).
Plants: crataegus_monogyna, crocus_sativus, curcuma_longa, dioscorea_villosa,
echinacea_purpurea. Sources verified via the PubMed MCP; DOIs pre-checked.
NB: crataegus_monogyna uses monogyna-specific studies, distinct from the
crataegus_laevigata set in batch 5."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_2026_06_20 import apply

SOURCES = [
    # ---- crataegus_monogyna (hawthorn; distinct from laevigata set) ----
    {"citekey": "amrati2024monogyna", "plant": "crataegus_monogyna", "study_type": "preclinical",
     "fields": {"author": "Ez-Zahra Amrati, F., Mssillou, I., Boukhira, S., Djiddi Bichara, M. et al.",
                "title": "Phenolic Composition of Crataegus monogyna Jacq. Extract and Its Anti-Inflammatory, Hepatoprotective, and Antileukemia Effects",
                "journal": "Pharmaceuticals (Basel)", "year": "2024", "volume": "17", "number": "6", "pages": "786",
                "doi": "10.3390/ph17060786"},
     "abstract": "A hydroethanolic extract of Crataegus monogyna leaves and stems was profiled by UHPLC (procyanidin, quercetin, catechin) and tested for anti-inflammatory, hepatoprotective and anticancer activity. The 1000 mg/kg dose inhibited carrageenan-induced paw edema by 99% after 6 h in rats, the extract displayed hepatoprotective properties against acetaminophen-induced hepatotoxicity, and it showed cytotoxic activity against K-562 and HL-60 myeloleukemia cells."},
    {"citekey": "lis2019monogyna", "plant": "crataegus_monogyna", "study_type": "preclinical",
     "fields": {"author": "Lis, M., Szczypka, M., Suszko-Pawłowska, A., Sokół-Łętowska, A. et al.",
                "title": "Hawthorn (Crataegus monogyna) Phenolic Extract Modulates Lymphocyte Subsets and Humoral Immune Response in Mice",
                "journal": "Planta Medica", "year": "2019", "volume": "86", "number": "2", "pages": "160-168",
                "doi": "10.1055/a-1045-5437"},
     "abstract": "Crataegus monogyna phenolic extract was administered orally to mice and its effect on lymphocyte subsets in lymphoid organs and on humoral immune response to sheep red blood cells was assessed. The extract modulated thymocyte and T/B splenocyte populations and, at ten doses, elevated plaque-forming cells and anti-SRBC hemagglutinin titer, indicating that hawthorn extract may act as an immunomodulator."},
    {"citekey": "paun2024monogyna", "plant": "crataegus_monogyna", "study_type": "preclinical",
     "fields": {"author": "Paun, G., Neagu, E., Albu, C., Alecu, A. et al.",
                "title": "Antioxidant and Antidiabetic Activity of Crataegus monogyna L. and Cornus mas Fruit Extracts",
                "journal": "Molecules", "year": "2024", "volume": "29", "number": "15", "pages": "3595",
                "doi": "10.3390/molecules29153595"},
     "abstract": "Polyphenol- and vitamin-C-rich fruit extracts of Crataegus monogyna and Cornus mas were prepared by green extraction methods. The extracts showed antioxidant activity (DPPH, reducing power) and antidiabetic activity by inhibiting alpha-amylase and alpha-glucosidase and by stimulating insulin secretion in beta-TC-6 cells under normal and hyperglycemic conditions, indicating hawthorn fruit as a source of antioxidant and antidiabetic bioactive molecules."},

    # ---- crocus_sativus (saffron) ----
    {"citekey": "shafiee2025saffron", "plant": "crocus_sativus", "study_type": "systematic-review",
     "fields": {"author": "Shafiee, A., Jafarabady, K., Seighali, N., Mohammadi, I. et al.",
                "title": "Effect of Saffron Versus Selective Serotonin Reuptake Inhibitors (SSRIs) in Treatment of Depression and Anxiety: A Meta-analysis of Randomized Controlled Trials",
                "journal": "Nutrition Reviews", "year": "2025", "volume": "83", "number": "3", "pages": "e751-e761",
                "doi": "10.1093/nutrit/nuae076"},
     "abstract": "This systematic review and meta-analysis of randomized controlled trials compared saffron (Crocus sativus) with SSRIs in adults with depression or anxiety. Meta-analysis of 8 depression trials and 4 anxiety trials found no significant difference between saffron and SSRIs in reducing depressive or anxiety symptoms, while participants receiving saffron had fewer adverse events, suggesting saffron is a potential SSRI alternative with a better tolerability profile."},
    {"citekey": "lopresti2014saffron", "plant": "crocus_sativus", "study_type": "systematic-review",
     "fields": {"author": "Lopresti, A.L. and Drummond, P.D.",
                "title": "Saffron (Crocus sativus) for depression: a systematic review of clinical studies and examination of underlying antidepressant mechanisms of action",
                "journal": "Human Psychopharmacology", "year": "2014", "volume": "29", "number": "6", "pages": "517-527",
                "doi": "10.1002/hup.2434"},
     "abstract": "A systematic review of six randomized, double-blind clinical trials of saffron for depression. In placebo-comparison trials saffron had large treatment effects, and compared with antidepressant medications it had similar antidepressant efficacy. Saffron's antidepressant effects are potentially due to its serotonergic, antioxidant, anti-inflammatory, neuro-endocrine and neuroprotective actions, providing initial support for its use in mild-to-moderate depression."},
    {"citekey": "chen2022saffron", "plant": "crocus_sativus", "study_type": "preclinical",
     "fields": {"author": "Chen, Z., Gu, J., Lin, S., Xu, Z. et al.",
                "title": "Saffron essential oil ameliorates CUMS-induced depression-like behavior in mice via the MAPK-CREB1-BDNF signaling pathway",
                "journal": "Journal of Ethnopharmacology", "year": "2022", "volume": "300", "pages": "115719",
                "doi": "10.1016/j.jep.2022.115719"},
     "abstract": "Saffron (Crocus sativus) has a long history in the treatment of depression. In mice exposed to chronic unpredictable mild stress, inhaled saffron essential oil improved depression-like behaviors, raised serum 5-HT, dopamine, BDNF and GABA, and ameliorated hippocampal neuronal damage, acting mainly through upregulation of the MAPK-CREB1-BDNF signaling pathway."},

    # ---- curcuma_longa (turmeric) ----
    {"citekey": "zeng2022curcumin", "plant": "curcuma_longa", "study_type": "systematic-review",
     "fields": {"author": "Zeng, L., Yang, T., Yang, K., Yu, G. et al.",
                "title": "Efficacy and Safety of Curcumin and Curcuma longa Extract in the Treatment of Arthritis: A Systematic Review and Meta-Analysis of Randomized Controlled Trials",
                "journal": "Frontiers in Immunology", "year": "2022", "volume": "13", "pages": "891822",
                "doi": "10.3389/fimmu.2022.891822"},
     "abstract": "A systematic review and meta-analysis of 29 randomized controlled trials (2396 participants) across five types of arthritis (ankylosing spondylitis, rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis and gout/hyperuricemia). Curcumin and Curcuma longa extract (120-1500 mg, 4-36 weeks) were safe and improved the severity of inflammation and pain in arthritis patients."},
    {"citekey": "zeng2021curcumin", "plant": "curcuma_longa", "study_type": "systematic-review",
     "fields": {"author": "Zeng, L., Yu, G., Hao, W., Yang, K. and Chen, H.",
                "title": "The efficacy and safety of Curcuma longa extract and curcumin supplements on osteoarthritis: a systematic review and meta-analysis",
                "journal": "Bioscience Reports", "year": "2021", "volume": "41", "number": "6", "pages": "BSR20210817",
                "doi": "10.1042/BSR20210817"},
     "abstract": "A systematic review and meta-analysis of 15 randomized controlled trials (1621 participants) of Curcuma longa extract and curcumin for osteoarthritis. Compared with placebo, they decreased the VAS and WOMAC pain, function and stiffness scores with adverse events comparable to placebo, and showed effects on joint pain, function and stiffness similar to NSAIDs but with fewer adverse events; use for more than 12 weeks is recommended."},
    {"citekey": "marton2021curcumin", "plant": "curcuma_longa", "study_type": "systematic-review",
     "fields": {"author": "Marton, L.T., Pescinini-E-Salzedas, L.M., Camargo, M.E.C., Barbalho, S.M. et al.",
                "title": "The Effects of Curcumin on Diabetes Mellitus: A Systematic Review",
                "journal": "Frontiers in Endocrinology", "year": "2021", "volume": "12", "pages": "669448",
                "doi": "10.3389/fendo.2021.669448"},
     "abstract": "A systematic review of sixteen studies on Curcuma longa / curcumin in diabetes mellitus. Curcumin's anti-diabetic activity may be due to its capacity to suppress oxidative stress and inflammation; it significantly reduced fasting blood glucose, glycated hemoglobin and body mass index, and nanocurcumin reduced triglycerides, total and LDL cholesterol, C-reactive protein and malondialdehyde, supporting its use in the management of diabetes."},

    # ---- dioscorea_villosa (wild yam) ----
    {"citekey": "depypere2013menopause", "plant": "dioscorea_villosa", "study_type": "traditional",
     "fields": {"author": "Depypere, H.T. and Comhaire, F.H.",
                "title": "Herbal preparations for the menopause: beyond isoflavones and black cohosh",
                "journal": "Maturitas", "year": "2013", "volume": "77", "number": "2", "pages": "191-194",
                "doi": "10.1016/j.maturitas.2013.11.001"},
     "abstract": "A minireview of the evidence for herbal preparations used for menopausal symptoms beyond isoflavones and black cohosh. Randomized controlled trials find that Mediterranean pine bark, linseed and Maca reduce vasomotor symptoms, while animal and human studies suggest Dioscorea villosa (wild yam) and others may protect against osteoporosis and breast and gynecological cancers, though further evidence is required."},
    {"citekey": "cai2020diosgenin", "plant": "dioscorea_villosa", "study_type": "traditional",
     "fields": {"author": "Cai, B., Zhang, Y., Wang, Z., Xu, D. et al.",
                "title": "Therapeutic Potential of Diosgenin and Its Major Derivatives against Neurological Diseases: Recent Advances",
                "journal": "Oxidative Medicine and Cellular Longevity", "year": "2020", "volume": "2020", "pages": "3153082",
                "doi": "10.1155/2020/3153082"},
     "abstract": "Diosgenin, a steroidal sapogenin abundant in medicinal herbs such as Dioscorea villosa (wild yam) and a major starting material for steroidal drugs, has wide-ranging pharmacological activities. This review summarises the therapeutic potential of diosgenin and its derivatives against neurological disorders including Parkinson's disease, Alzheimer's disease, brain injury, neuroinflammation and ischemia, mediated through multiple signaling pathways."},
    {"citekey": "raj2023dioscorea", "plant": "dioscorea_villosa", "study_type": "traditional",
     "fields": {"author": "Raj, P.S., Bergfeld, W.F., Belsito, D.V., Cohen, D.E. et al.",
                "title": "Safety Assessment of Dioscorea Villosa (Wild Yam) Root Extract as Used in Cosmetics",
                "journal": "International Journal of Toxicology", "year": "2023", "volume": "42", "number": "3_suppl", "pages": "29S-31S",
                "doi": "10.1177/10915818231204230"},
     "abstract": "The Expert Panel for Cosmetic Ingredient Safety reviewed updated information on Dioscorea villosa (wild yam) root extract and reaffirmed its original conclusion that the extract is safe as a cosmetic ingredient in the current practices of use and concentration, supporting the topical safety profile of wild yam preparations."},

    # ---- echinacea_purpurea (purple coneflower) ----
    {"citekey": "karschvolk2014echinacea", "plant": "echinacea_purpurea", "study_type": "systematic-review",
     "fields": {"author": "Karsch-Völk, M., Barrett, B., Kiefer, D., Bauer, R. et al.",
                "title": "Echinacea for preventing and treating the common cold",
                "journal": "Cochrane Database of Systematic Reviews", "year": "2014", "volume": "2", "number": "2", "pages": "CD000530",
                "doi": "10.1002/14651858.CD000530.pub3"},
     "abstract": "A Cochrane systematic review of 24 double-blind trials (4631 participants) comparing mono-preparations of Echinacea with placebo for the common cold, including seven trials of preparations based on the aerial parts of Echinacea purpurea. Individual prevention trials consistently showed positive (if non-significant) trends, with a post-hoc pooled relative risk reduction of 10-20%; adverse events did not differ significantly from placebo."},
    {"citekey": "kamin2025phytotherapy", "plant": "echinacea_purpurea", "study_type": "systematic-review",
     "fields": {"author": "Kamin, W., Seifert, G., Zwiauer, K., Bonhoeffer, J. et al.",
                "title": "Phytotherapy for acute respiratory tract infections in children: a systematically conducted, comprehensive review",
                "journal": "Frontiers in Pediatrics", "year": "2025", "volume": "13", "pages": "1423250",
                "doi": "10.3389/fped.2025.1423250"},
     "abstract": "A systematically conducted review (PRISMA) of 45 reports on phytopharmaceuticals for paediatric acute respiratory tract infections, including various purple coneflower (Echinacea purpurea) preparations alongside ivy leaf, African geranium and others. The review presents the available efficacy and tolerability evidence for these herbal medicines as alternatives to reduce inappropriate antibiotic use in children."},
    {"citekey": "fashner2012coldtreatment", "plant": "echinacea_purpurea", "study_type": "traditional",
     "fields": {"author": "Fashner, J., Ericson, K. and Werner, S.",
                "title": "Treatment of the common cold in children and adults",
                "journal": "American Family Physician", "year": "2012", "volume": "86", "number": "2", "pages": "153-159",
                "url": "https://pubmed.ncbi.nlm.nih.gov/22962927/"},
     "abstract": "A clinical review of treatments for the common cold. For adults, nonsteroidal anti-inflammatory drugs and some herbal preparations, including Echinacea purpurea, improve symptoms, whereas Echinacea angustifolia preparations are ineffective; the review summarises the evidence and safety of symptomatic cold treatments in children and adults."},
]

if __name__ == "__main__":
    apply(SOURCES)
