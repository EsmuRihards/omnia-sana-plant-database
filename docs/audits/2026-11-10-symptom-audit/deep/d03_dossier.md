# Deep dossier batch 3

## asclepias-tuberosa - Asclepias tuberosa - Pleurisy Root, Butterfly weed, Butterfly milkweed
actions: anti-inflammatory=['REF-0495']; diaphoretic=['REF-0494', 'REF-0495', 'REF-1948']; expectorant=['REF-0494', 'REF-0495', 'REF-1948']
- **bronchitis** [needs-review,ev1] note="Traditional expectorant - helps clear phlegm in chest conditions, bronchitis and pleurisy"
    D=['REF-0494'] N=[] X=['REF-0495', 'REF-1948'] M=[]
- **cold** [needs-review,ev1] !INF note="inferred from diaphoretic action"
    D=['REF-0494'] N=[] X=['REF-0495', 'REF-1948'] M=[]
- **respiratory-support** [needs-review,ev1] !INF note="inferred from expectorant action"
    D=['REF-0494'] N=[] X=['REF-0495', 'REF-1948'] M=[]
  REF-0494 [traditional] n.d.  | Asclepias tuberosa | NO-ID 
     used: A:diaphoretic, A:expectorant, D:bronchitis, D:cold, D:respiratory-support
     (no abstract)
  REF-0495 [traditional] n.d.  | Pleurisy Root (Asclepias tuberosa) | NO-ID 
     used: A:anti-inflammatory, A:diaphoretic, A:expectorant
     (no abstract)
  REF-1948 [traditional] 1848 Medical Examiner (Philadelphia) | Asclepias Tuberosa, Butterfly-Weed, Milk-Weed, Pleurisy Root, White Root | NO-ID 
     used: A:diaphoretic, A:expectorant
     (no abstract)

## astragalus-membranaceus - Astragalus membranaceus - Astragalus, Huang qi, Milkvetch root
actions: adaptogen=['REF-0402', 'REF-2261']; anti-inflammatory=['REF-0402', 'REF-0736', 'REF-2258']; anticancer=['REF-0736', 'REF-0402', 'REF-2868', 'REF-2869', 'REF-2870', 'REF-0401']; antioxidant=['REF-0402', 'REF-2256', 'REF-2260']; immunomodulator=['REF-0401', 'REF-0402', 'REF-0736', 'REF-2256', 'REF-2257', 'REF-2262', 'REF-2263']; nephroprotective=['REF-0402', 'REF-0586']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0402'] M=['REF-0736<anti-inflammatory', 'REF-2258<anti-inflammatory']
- **cancer** [needs-review,ev2] note="Astragalus membranaceus protects against gastrointestinal cancers; astragaloside IV inhibits lung cancer metastasis via macrophage repolarization, cycloastragenol boosts CD8+ T-cell antitumour immunity (with anti-PD-1 synergy), and Astragalus polysaccharide suppresses inflammation-induced colorectal cancer (preclinical)."
    D=['REF-0736', 'REF-0402', 'REF-2868', 'REF-2869', 'REF-2870', 'REF-0401'] N=[] X=[] M=[]
- **cold** [needs-review,ev1] note="Supports resistance to colds and respiratory infection (immune)"
    D=[] N=[] X=['REF-2263', 'REF-0401'] M=['REF-0402<immunomodulator', 'REF-0736<immunomodulator', 'REF-2256<immunomodulator', 'REF-2257<immunomodulator', 'REF-2262<immunomodulator']
- **fatigue** [verified,ev7] note="Adaptogenic tonic for fatigue and low vitality (traditional 'Qi' tonic)"
    D=['REF-2261'] N=[] X=['REF-0402'] M=[]
- **immune-support** [verified,ev2] note="Immune support / immunomodulation (activates macrophages, NK cells, T and B lymphocytes); Supports resistance to colds and respiratory infection (immune)"
    D=['REF-0401', 'REF-0402'] N=[] X=[] M=['REF-0736<immunomodulator', 'REF-2256<immunomodulator', 'REF-2257<immunomodulator', 'REF-2262<immunomodulator', 'REF-2263<immunomodulator']
- **infection** [verified,ev2] note="Supports resistance to colds and respiratory infection (immune)"
    D=['REF-0401'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0402'] N=[] X=[] M=['REF-0736<anti-inflammatory', 'REF-2258<anti-inflammatory']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0402'] M=['REF-0736<anti-inflammatory', 'REF-2258<anti-inflammatory']
  REF-0401 [narrative-review] 2022 Archives of Pharmacal Research | Astragalus polysaccharide: a review of its immunomodulatory effect | doi:10.1007/s12272-022-01393-3 
     used: A:anticancer, A:immunomodulator, D:cancer, D:immune-support, D:infection
     C: Among them, the anticancer effect is the most prominent. In short, Astragalus polysaccharide is a valuable immunomodulatory medicine, but further high-quality studies are warranted to corroborate its clinical efficacy.
  REF-0402 [narrative-review] 2019 Advances in Pharmacology | Astragaloside IV derived from Astragalus membranaceus: A research review on the pharmacological effects | doi:10.1016/bs.apha.2019.08.002 
     used: A:adaptogen, A:anti-inflammatory, A:anticancer, A:antioxidant, A:immunomodulator, A:nephroprotective, D:cancer, D:immune-support, D:inflammation, M:cold
     C: This review will provide an overall understanding of the pharmacological functions of astragaloside IV on neuroprotection, liver protection, anti-cancer and anti-diabetes. In light of this, AS-IV will be a potent alternative therapeutic agent for treatment of the above mentioned diseases.
  REF-0586 [systematic-review] 2014 Cochrane Database of Systematic Reviews | Astragalus (a traditional Chinese medicine) for treating chronic kidney disease | doi:10.1002/14651858.CD008369.pub2 
     used: A:nephroprotective
     C: Astragalus significantly decreased systolic blood pressure (2 studies, 77 participants: MD -16.65 mm Hg, 95% CI -28.83 to -4.47; I² = 50%), and diastolic blood pressure (2 studies, 77 participants: MD -6.02 mm Hg, 95% CI -10.59 to -1.46; I² = 0%).Six of 22 included studies reported no adverse effects were observed; while the remaining 16 studies did not report adverse effects. Authors' conclusions Although Astragalus
  REF-0736 [narrative-review] 2016 The American Journal of Chinese Medicine | Astragalus membranaceus: A Review of its Protection Against Inflammation and Gastrointestinal Cancers | doi:10.1142/S0192415X16500014 
     used: A:anti-inflammatory, A:anticancer, A:immunomodulator, D:cancer, M:arthritis, M:cold, M:immune-support, M:inflammation, M:skin-irritation
     C: We discuss in detail how the Astragalus herb and AST influence the immune system, modulate various cancer signaling pathways, and interact with specific transcription molecules during protection against gastrointestinal inflammation and cancers. This information could help clinicians and scientists develop novel target-specific and effective therapeutic agents that are deprived of major systemic side effects, so as t
  REF-2256 [narrative-review] 2014 Phytotherapy Research | Review of the botanical characteristics, phytochemistry, and pharmacology of Astragalus membranaceus (Huangqi) | doi:10.1002/ptr.5188 
     used: A:antioxidant, A:immunomodulator, M:cold, M:immune-support
     C: As an important traditional Chinese medicine, further studies on Astragali Radix can lead to the development of new drugs and therapies for various diseases. The improvement of its utilization should be studied further.
  REF-2257 [narrative-review] 2023 Molecules | Biosynthesis and pharmacological activities of flavonoids, triterpene saponins and polysaccharides derived from Astragalus membranaceus | doi:10.3390/molecules28135018 
     used: A:immunomodulator, M:cold, M:immune-support
     C: We further systematically summarized the pharmacological effects of bioactive ingredients in A. membranaceus , which laid the foundation for the development of clinical candidate agents. Finally, we proposed potential strategies of heterologous biosynthesis to improve the industrialized production and sustainable supply of natural products with pharmacological activities from A. membranaceus , thereby providing an im
  REF-2258 [preclinical] 2023 International Journal of Biological Macr | Structural characterization and anti-inflammatory activity of polysaccharides from Astragalus membranaceus | doi:10.1016/j.ijbiomac.2023.124386 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: They could inhibit the production of inflammatory factors (TNF-α, IL-6, and MCP-1) in LPS-stimulated RAW264.7 macrophages via NF-κB and MAPK (ERK, JNK) pathways. These results suggested that the two polysaccharides could be potential anti-inflammatory supplements.
  REF-2260 [preclinical] 2024 FASEB Journal | The protective effect and bioactive compounds of Astragalus membranaceus against neurodegenerative disorders via alleviating oxidative stress in Droso | doi:10.1096/fj.202400390R 
     used: A:antioxidant
     C: Daidzein ameliorated neurobehavioral defect of Aβ-induced AD mode. Taken together, AM plays a protective role in oxidative damage, thereby as a potential natural drug to treat neurodegenerative disorders.
  REF-2261 [systematic-review] 2019 Metabolic Brain Disease | Adjuvant therapy with Astragalus membranaceus for post-stroke fatigue: a systematic review | doi:10.1007/s11011-019-00483-4 
     used: A:adaptogen, D:fatigue
     C: In conclusions, adjuvant therapy with CHM-HQ may benefit in managing fatigue and quality of life in stroke patients. However, stronger evidence is needed for a promising conclusion and more rigorous designs of RCTs are merited in the future.
  REF-2262 [preclinical] 2014 International Journal of Biological Macr | Structural features and biological activities of the polysaccharides from Astragalus membranaceus | doi:10.1016/j.ijbiomac.2013.12.002 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Modern phytochemistry and pharmacological experiments have proved that polysaccharide is one of the major active ingredients in the root of A. membranaceus with various important bioactivities, such as immunomodulation, antioxidant, antitumor, anti-diabetes, antiviral, hepatoprotection, anti-inflammation, anti-atherosclerosis, hematopoiesis and neuroprotection. The aim of the present review is to summarize previous a
  REF-2263 [narrative-review] 2019 Chinese Journal of Integrative Medicine | Research progress in Astragalus membranaceus and its active components on immune responses in liver fibrosis | doi:10.1007/s11655-019-3039-1 
     used: A:immunomodulator, M:immune-support
     C: This article reviews the action mechanism of immune cells on liver fibrosis and the effect of Astragalus membranaeus and its active components on immune cells. In-depth study of interaction between immune cells and HSCs on the pathogenesis of liver fibrosis, and the regulatory effect of Astragalus membranaeus and its active components on immune mechanism will provide new insights in the treatment of liver fibrosis.
  REF-2868 [preclinical] 2018 Journal of Experimental & Clinical Cance | Astragaloside IV inhibits lung cancer progression and metastasis by modulating macrophage polarization through AMPK signaling | pmid:30157903 doi:10.1186/s13046-018-0878-0 !SP
     used: A:anticancer, D:cancer
     C: AS-IV reduced the growth, invasion, migration, and angiogenesis of lung cancer by blocking the M2 polarization of macrophages partially through the AMPK signaling pathway, which appears to play an important role in AS-IV's ability to inhibit the metastasis of lung cancer.
  REF-2869 [preclinical] 2022 Journal for ImmunoTherapy of Cancer | Targeting cathepsin B by cycloastragenol enhances antitumor immunity of CD8 T cells via inhibiting MHC-I degradation | pmid:36307151 doi:10.1136/jitc-2022-004874 
     used: A:anticancer, D:cancer
     C: Our data reported for the first time that cathepsin B downregulation confers antitumor immunity and explicates the antitumor mechanism of natural product CAG.
  REF-2870 [preclinical] 2024 Biomedicine & Pharmacotherapy | Astragalus polysaccharide ameliorates CD8 T cell dysfunction through STAT3/Gal-3/LAG3 pathway in inflammation-induced colorectal cancer | pmid:38278025 doi:10.1016/j.biopha.2024.116172 
     used: A:anticancer, D:cancer
     C: Co-culture experiments with MC38 and CD8 + T cells demonstrated that APS decreased the expression of co-inhibitory receptor LAG3 in CD8 + T cells by targeting STAT3/Gal-3 in MC38 cells. Mechanism investigations revealed that APS specifically improved CD8 + T cell function through modulation of the STAT3/Gal-3/LAG3 pathway to inhibit CRC development, providing insights for future clinical development of natural anti-t

## bacopa-monnieri - Bacopa monnieri - Water Hyssop, Bacopa, brahmi
actions: anti-inflammatory=['REF-0309', 'REF-2112']; anticancer=['REF-0742', 'REF-2871', 'REF-2872']; antioxidant=['REF-0309', 'REF-2109', 'REF-2111', 'REF-2112']; neuroprotective=['REF-0740', 'REF-0283', 'REF-0309', 'REF-0742', 'REF-2107', 'REF-2108', 'REF-2109', 'REF-2110', 'REF-2113']; sedative=['REF-0309', 'REF-0740']
- **cancer** [needs-review,ev2] note="Bacopaside II from Bacopa monnieri inhibits colon cancer cell growth via cell-cycle arrest and apoptosis (aquaporin-1 blockade), and its bacopasaponins are cytotoxic to lung (PC9) and colon (SW620) cancer cells (preclinical)."
    D=['REF-0742', 'REF-2871', 'REF-2872'] N=[] X=[] M=[]
- **cognitive-function** [needs-review,ev6] !INF note="inferred from neuroprotective action"
    D=['REF-0740', 'REF-0283'] N=[] X=['REF-0309'] M=['REF-0742<neuroprotective', 'REF-2107<neuroprotective', 'REF-2108<neuroprotective', 'REF-2109<neuroprotective', 'REF-2110<neuroprotective', 'REF-2113<neuroprotective']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0309'] M=['REF-2112<anti-inflammatory']
- **memory** [needs-review,ev6] !INF note="inferred from neuroprotective action"
    D=['REF-0740', 'REF-0283'] N=[] X=['REF-0309'] M=['REF-0742<neuroprotective', 'REF-2107<neuroprotective', 'REF-2108<neuroprotective', 'REF-2109<neuroprotective', 'REF-2110<neuroprotective', 'REF-2113<neuroprotective']
  REF-0283 [rct] 2001  | The chronic effects of an extract of Bacopa monniera (Brahmi) on cognitive function in healthy human subjects | doi:10.1007/s002130100815 
     used: A:neuroprotective, D:cognitive-function, D:memory
     C: These findings suggest that B. monniera may improve higher order cognitive processes that are critically dependent on the input of information from our environment such as learning and memory.
     !NULL: However, the effects on human cognition are inconclusive.
  REF-0309 [traditional] 2002  | WHO Monographs on Selected Medicinal Plants | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:neuroprotective, A:sedative
     (no abstract)
  REF-0740 [rct] 2008 Journal of Alternative and Complementary | Effects of a standardized Bacopa monnieri extract on cognitive performance, anxiety, and depression in the elderly: a randomized, double-blind, placeb | doi:10.1089/acm.2008.0018 
     used: A:neuroprotective, A:sedative, D:cognitive-function, D:memory
     C: This study provides further evidence that B. monnieri has potential for safely enhancing cognitive performance in the aging.
     !NULL: No effects were found on the DAT, WAIS digit task, mood, or blood pressure.
  REF-0742 [narrative-review] 2022 Frontiers in Nutrition | Pharmacological attributes of Bacopa monnieri extract: Current updates and clinical manifestation | doi:10.3389/fnut.2022.972379 
     used: A:anticancer, A:neuroprotective, D:cancer, M:cognitive-function, M:memory
     C: In addition, we investigated the underlying molecular mechanism in therapeutic interventions, toxicities, safety concerns and synergistic potential in cognition and neuroprotection. Overall, this review provides deeper insights into the therapeutic implications of Brahmi as a lead formulation for treating neurological disorders and exerting cognitive-enhancing effects.
  REF-2107 [meta-analysis] 2014 Journal of Ethnopharmacology | Meta-analysis of randomized controlled trials on cognitive effects of Bacopa monnieri extract | doi:10.1016/j.jep.2013.11.008 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: This meta-analysis suggests that Bacopa monnieri has the potential to improve cognition, particularly speed of attention but only a large well designed 'head-to-head' trial against an existing medication will provide definitive data on its efficacy on healthy or dementia patients using a standardized preparation.
  REF-2108 [narrative-review] 2022 Current Topics in Medicinal Chemistry | Bacopa monnieri for disorders affecting brain: current perspectives | doi:10.2174/1568026622666220119111538 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: We have also discussed CDRI-08, clinical trials, safety, emerging formulation technologies, as well as BM combinations, and dietary supplements. To propel the clinical translation of BM in disorders affecting the brain, strategies to improve brain delivery via novel formulations and integration of the preclinical findings into large and well-defined clinical trials, in appropriate age groups and sex, specifically in 
  REF-2109 [preclinical] 2023 International Journal of Biological Macr | Bacopa monnieri reduces Tau aggregation and Tau-mediated toxicity in cells | doi:10.1016/j.ijbiomac.2023.123171 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: On the contrary, Bacopa monnieri treatment restored the NUP358 arrangement in cells. The overall results of the present study suggested that Bacopa monnieri could be considered a potent herb against Tau phosphorylation and Tau aggregation, which projects it as a promising formulation for Alzheimer's disease.
  REF-2110 [narrative-review] 2021 Molecular Biology Reports | Neuroprotection with Bacopa monnieri - a review of experimental evidence | doi:10.1007/s11033-021-06236-w 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: English language articles from databases PubMed, Scopus and Google scholar were searched using appropriate free keywords and MeSH terms related to the topic. The review demonstrates the neuroprotective potential of the Ayurveda herb Brahmi in several disorders including Alzheimer's disease, epilepsy, Parkinson's disease, Huntington's disease, cerebral ischemia and infarct and neoplasms.
  REF-2111 [narrative-review] 2015 Evidence-Based Complementary and Alterna | Bacopa monnieri as an antioxidant therapy to reduce oxidative stress in the aging brain | doi:10.1155/2015/615384 
     used: A:antioxidant
     C: In this review we discuss the animal studies and in vivo evidence for Bacopa monnieri as a potential therapeutic antioxidant to reduce oxidative stress and improve cognitive function. We suggest that future studies incorporate neuroimaging particularly magnetic resonance spectroscopy into their randomized controlled trials to better understand whether changes in antioxidant status in vivo cause improvements in cognit
  REF-2112 [preclinical] 2019 Metabolic Brain Disease | Bacopa monnieri prevents colchicine-induced dementia by anti-inflammatory action | doi:10.1007/s11011-018-0332-1 
     used: A:anti-inflammatory, A:antioxidant, M:inflammation
     C: Inflammatory and oxidative stress markers were attenuated in the brain regions of BM supplemented animals. Taken together, the findings reveal that BM reverses colchicine-induced dementia by its anti-inflammatory and anti-oxidant action suggesting that it may be an effective therapeutic intervention to ameliorate progression of AD.
  REF-2113 [narrative-review] 2019 Archives of Biochemistry and Biophysics | Brahmi (Bacopa monnieri): an ayurvedic herb against the Alzheimer's disease | doi:10.1016/j.abb.2019.108153 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: Here on basis of earlier studies we hypothesize the inhibitory role of Brahmi against Tau-mediated toxicity. The overall studies have concluded that Brahmi can be used as a lead formulation for treatment of Alzheimer's disease and other neurological disorders.
  REF-2871 [preclinical] 2018 Cells | The Purified Extract from the Medicinal Plant Bacopa monnieri, Bacopaside II, Inhibits Growth of Colon Cancer Cells In Vitro by Inducing Cell Cycle Ar | pmid:30037060 doi:10.3390/cells7070081 
     used: A:anticancer, D:cancer
     C: Inhibition of SW480, SW620 and HCT116 at ≥15 µM was mediated by G2/M arrest and apoptosis. These results are the first to show that bacopaside II inhibits colon cancer cell growth by inducing cell cycle arrest and apoptosis.
  REF-2872 [preclinical] 2022 Natural Product Research | Two new triterpenoid glycosides from Bacopa monnieri and their cytotoxic activity | pmid:36239487 doi:10.1080/14786419.2022.2132498 
     used: A:anticancer, D:cancer
     C: All these compounds were evaluated for their cytotoxic activity using the cell counting kit-8 (CCK-8) assay. Compounds 4 , 6 , 8 , and 10 exhibited potential cytotoxic effects against human lung cancer cells (PC9) and human colon cancer cells (SW620).

## betula-pendula - Betula pendula - Birch, Silver Birch, Warty Birch
actions: anti-inflammatory=['REF-0080', 'REF-0743', 'REF-1692', 'REF-1695', 'REF-1697']; anti-rheumatic=['REF-0080', 'REF-1692']; anticancer=['REF-0080', 'REF-1695', 'REF-1696', 'REF-1697']; antidiabetic=['REF-0080', 'REF-1694']; antimicrobial=['REF-0080', 'REF-0743']; antioxidant=['REF-0080', 'REF-0743', 'REF-0744', 'REF-1693', 'REF-1694', 'REF-1695']; antiviral=['REF-0080']; diuretic=['REF-0080']; emollient=['REF-0080']; gastroprotective=['REF-0080']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0080', 'REF-1697'] M=['REF-0743<anti-inflammatory', 'REF-1692<anti-inflammatory', 'REF-1695<anti-inflammatory']
- **back-pain** [needs-review,ev1] note="inferred from anti-rheumatic action"
    D=[] N=[] X=['REF-0080'] M=['REF-1692<anti-rheumatic']
- **blood-sugar** [needs-review,ev1] note="inferred from antidiabetic action"
    D=[] N=[] X=['REF-0080'] M=['REF-1694<antidiabetic']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1696'] N=[] X=['REF-0080'] M=['REF-1695<anticancer', 'REF-1697<anticancer']
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0080'] M=['REF-0743<antimicrobial']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0080', 'REF-1697'] M=['REF-0743<anti-inflammatory', 'REF-1692<anti-inflammatory', 'REF-1695<anti-inflammatory']
- **metabolic-support** [needs-review,ev1] note="inferred from antidiabetic action"
    D=[] N=[] X=['REF-0080'] M=['REF-1694<antidiabetic']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0080', 'REF-1697'] M=['REF-0743<anti-inflammatory', 'REF-1692<anti-inflammatory', 'REF-1695<anti-inflammatory']
- **urinary-support** [needs-review,ev1] !INF note="inferred from diuretic action"
    D=['REF-0080'] N=[] X=[] M=[]
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0080'] M=['REF-0743<antimicrobial']
  REF-0080 [traditional] 2015  | Birch leaf (Betulae folium): summary for the public | NO-ID 
     used: A:anti-inflammatory, A:anti-rheumatic, A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:antiviral, A:diuretic, A:emollient, A:gastroprotective, D:urinary-support
     (no abstract)
  REF-0743 [narrative-review] 2014 Journal of Ethnopharmacology | Medicinal plants of the genus Betula — traditional uses and a phytochemical-pharmacological review | doi:10.1016/j.jep.2014.11.010 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, M:arthritis, M:infection, M:inflammation, M:skin-irritation, M:wounds
     C: Several species belonging to the genus Betula are widely used in traditional medicine. Betula platyphylla and Betula pendula have specifically been found to be potentially useful in the treatment of degenerative joint disease. There is convincing evidence in experimental animal models in support of their anti-carcinogenic effects. However, it would be worthwhile to investigate the biochemical and physiological mechan
  REF-0744 [preclinical] 2018 Folia Medica | Antioxidant Activity of Dry Birch (Betula pendula) Leaves Extract | doi:10.2478/folmed-2018-0035 
     used: A:antioxidant
     C: Dried birch leaf extract has a relatively high antioxidant potential and could be used as a natural source of antioxidants.
  REF-1692 [preclinical] 2011 Journal of Ethnopharmacology | An aqueous birch leaf extract of Betula pendula inhibits the growth and cell division of inflammatory lymphocytes | doi:10.1016/j.jep.2011.05.018 
     used: A:anti-inflammatory, A:anti-rheumatic, M:arthritis, M:back-pain, M:inflammation, M:skin-irritation
     C: Our results give a rational basis for the use of Betula pendula leaf extract for the treatment of immune disorders, like rheumatoid arthritis, by diminishing proliferating inflammatory lymphocytes.
  REF-1693 [preclinical] 2017 Pharmaceutical Biology | Evaluation of the antioxidant activity of Betula pendula leaves extract and its effects on model foods | doi:10.1080/13880209.2017.1282528 
     used: A:antioxidant
     C: The present results indicated that the BP extracts can be used as natural food antioxidants.
  REF-1694 [preclinical] 2016 Evidence-Based Complementary and Alterna | Effect of Betula pendula Leaf Extract on alpha-Glucosidase and Glutathione Level in Glucose-Induced Oxidative Stress | doi:10.1155/2016/8429398 
     used: A:antidiabetic, A:antioxidant, M:blood-sugar, M:metabolic-support
     C: In addition, ethanolic extract effectively increased cellular glutathione levels caused by hyperglycemia and inhibited α-glucosidase with the activity comparable to that of acarbose. Therefore, in vitro research using B. pendula plant extracts has confirmed their antidiabetic properties.
  REF-1695 [preclinical] 2023 Journal of Ethnopharmacology | Novel compounds discovery approach based on UPLC-QTOF-MS/MS chemical profile reveals birch bark extract anti-inflammatory, -oxidative, and -proliferat | doi:10.1016/j.jep.2023.116148 
     used: A:anti-inflammatory, A:anticancer, A:antioxidant, M:arthritis, M:cancer, M:inflammation, M:skin-irritation
     C: This study provided a predictable chemical profile and demonstrated the pharmacological effects of birch bark extract, elucidated the mechanism of this traditional Chinese medicine and suggested it as a novel anti-cancer candidate.
  REF-1696 [preclinical] 2021 Journal of Cellular and Molecular Medici | Santin and cirsimaritin from Betula pubescens and Betula pendula buds induce apoptosis in human digestive system cancer cells | doi:10.1111/jcmm.17031 
     used: A:anticancer, D:cancer
     C: Moreover, upregulation of p53 was detected only in wild-type p53 harbouring cells. Together, our results suggest that santin and cirsimaritin exhibit promising anti-cancer activity in cultures of digestive system cancer cells.
  REF-1697 [preclinical] 2018 PLoS One | Cytotoxicity of white birch bud extracts: Perspectives for therapy of tumours | doi:10.1371/journal.pone.0201949 
     used: A:anti-inflammatory, A:anticancer, M:cancer
     C: The rich chemical composition of birch buds suggests the possibility of a wider spectrum of biological activity than previously thought. Birch bud extracts could be a promising source of compounds with cytotoxic activity against various cancers.

## bistorta-officinalis - Bistorta officinalis - Bistort, Common bistort, Snakeroot
actions: anti-inflammatory=['REF-0746', 'REF-0411', 'REF-2116']; anticancer=['REF-2122', 'REF-2123']; antidiarrheal=['REF-0746', 'REF-0411', 'REF-2116']; antimicrobial=['REF-0746', 'REF-0627', 'REF-0747']; astringent=['REF-0746', 'REF-0411']; styptic=['REF-0746', 'REF-0411']; vulnerary=['REF-0746', 'REF-0411']
- **cancer** [needs-review,ev2] note="Polygonum bistorta (Bistorta officinalis) methanol-water and aqueous extracts inhibit hepatocellular carcinoma cells via ROS-induced ER stress and apoptosis (delaying xenograft tumour growth), with phenolic constituents driving the cytotoxicity (preclinical)."
    D=['REF-2122', 'REF-2123'] N=[] X=[] M=[]
- **diarrhea** [verified,ev2] note="Astringent for mild diarrhoea (tannins tighten the gut lining and reduce excess secretion)"
    D=['REF-0746'] N=[] X=['REF-0411'] M=[]
- **infection** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0746'] N=[] X=['REF-0627'] M=['REF-0747<antimicrobial']
- **inflammation** [verified,ev2] note="Anti-inflammatory gargle / mouthwash for inflammation of the mouth and throat (sore throat)"
    D=['REF-0746'] N=[] X=['REF-0411'] M=['REF-2116<anti-inflammatory']
- **skin-irritation** [needs-review,ev2] !INF note="inferred from astringent action"
    D=['REF-0746'] N=[] X=['REF-2116', 'REF-0411'] M=[]
- **wounds** [needs-review,ev1] note="Vulnerary and styptic for minor wounds (topical)"
    D=[] N=[] X=['REF-0411', 'REF-0746'] M=['REF-0627<antimicrobial', 'REF-0747<antimicrobial']
  REF-0411 [traditional] n.d.  | Bistort: Overview, Uses, Side Effects, Precautions, Interactions, Dosing and Reviews | NO-ID !TAG review-title/traditional
     used: A:anti-inflammatory, A:antidiarrheal, A:astringent, A:styptic, A:vulnerary
     (no abstract)
  REF-0627 [preclinical] 2023 Applied Biochemistry and Biotechnology | GC-MS Analysis of Persicaria bistorta: Uncovering the Molecular Basis of Its Traditional Medicinal Use | doi:10.1007/s12010-023-04580-0 
     used: A:antimicrobial, M:wounds
     C: Overall, results suggest that Persicaria bistorta may have therapeutic potential and warrant further investigation. Further research is needed to confirm the efficacy and safety of Persicaria bistorta as a natural medicine and determine its active compounds' mechanisms of action.
  REF-0746 [preclinical] 2020 Journal of Ethnopharmacology | Antibacterial and anti-inflammatory activity of bistort (Bistorta officinalis) aqueous extract and its major components: justification of the usage of | doi:10.1016/j.jep.2020.113077 
     used: A:anti-inflammatory, A:antidiarrheal, A:antimicrobial, A:astringent, A:styptic, A:vulnerary, D:diarrhea, D:infection, D:inflammation, D:skin-irritation
     C: The results obtained in the present study support that the infusions from common bistort influence key biological processes are crucial for skin conditions with the inflammatory background. The study justifies the traditional topical application of common bistort.
  REF-0747 [preclinical] 2020 Molecules | Anti-Virulence Potential and In Vivo Toxicity of Persicaria maculosa and Bistorta officinalis Extracts | doi:10.3390/molecules25081811 
     used: A:antimicrobial, M:infection, M:wounds
     C: The bioactive concentrations of the extracts were not toxic in the zebrafish model system. This study represents an initial step towards the integration of P. maculosa and B. officinalis for use in the treatment of Pseudomonas infections.
  REF-2116 [preclinical] 2024 Inflammopharmacology | Protective effect of freeze-dried extract of Persicaria bistorta Samp. on acetic acid-induced colitis model in rats: involvement of nitric oxide and o | doi:10.1007/s10787-024-01518-8 
     used: A:anti-inflammatory, A:antidiarrheal, M:inflammation
     C: Additionally, while blocking NO and opioid pathways, the therapeutic effect of the extract was not significant, compared to the negative control, suggesting that PB 700 has exerted its therapeutic effect via these two pathways. However, further mechanistic and clinical studies are recommended to confirm PB as a natural treatment for colitis.
     !NULL: Additionally, while blocking NO and opioid pathways, the therapeutic effect of the extract was not significant, compared to the negative control, suggesting that PB 700 has exerted its therapeutic effect via these two pathways.
  REF-2122 [preclinical] 2012 African Journal of Traditional, Compleme | Anticancer constituents and cytotoxic activity of methanol-water extract of Polygonum bistorta L. | doi:10.4314/ajtcam.v10i1.9 
     used: A:anticancer, D:cancer
     C: Fractions were evaluated for their cytotoxic activity on a rarely studied human hepatocellular carcinoma cell line (HCCLM3). 11 fractions showed good to strong cytotoxicity in a range of 200 µg/mL-800 µg/mL, whereas 2 fractions did not show any activity even at 800 µg/mL and no anticancer constituent was detected from them. 50 percent growth inhibition (GI50) values for five most active fractions were calculated and 
     !NULL: 11 fractions showed good to strong cytotoxicity in a range of 200 µg/mL-800 µg/mL, whereas 2 fractions did not show any activity even at 800 µg/mL and no anticancer constituent was detected from them.
  REF-2123 [preclinical] 2017 Scientific Reports | Aqueous extract of Polygonum bistorta modulates proteostasis by ROS-induced ER stress in human hepatoma cells | doi:10.1038/srep41437 
     used: A:anticancer, D:cancer
     C: Oral administration of PB delayed tumour growth in a xenograft model without significant body weight loss. These findings indicate that PB may be a potential new alternative or complementary medicine for HCC.

## borago-officinalis - Borago officinalis - Borage, Starflower, Common borage
SERIOUS: Pyrrolizidine alkaloids (PAs): Many Boraginaceae can produce PAs; unsaturated PAs are hepatotoxic and genotoxic (risk increases with cumulative exposure). Borag
actions: analgesic=['REF-0309']; anti-inflammatory=['REF-0309', 'REF-0749', 'REF-1952', 'REF-1958']; anticancer=['REF-1953']; antioxidant=['REF-0309', 'REF-0749', 'REF-1951', 'REF-1953', 'REF-1956']; digestive=['REF-0309', 'REF-1950']; emollient=['REF-0309', 'REF-1951']; immunomodulator=['REF-0309', 'REF-1958']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-1952', 'REF-1958', 'REF-0309'] M=['REF-0749<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1953'] N=[] X=[] M=[]
- **cold** [needs-review,ev2] !INF note="inferred from immunomodulator action"
    D=['REF-0749'] N=[] X=['REF-1958', 'REF-0309'] M=[]
- **eczema** [needs-review,ev1] note="inferred from emollient action"
    D=[] N=[] X=['REF-0309'] M=['REF-1951<emollient']
- **immune-support** [needs-review,ev1] note=""
    D=[] N=[] X=['REF-0309'] M=['REF-1958<immunomodulator']
- **indigestion** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0309'] M=['REF-1950<digestive']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0749'] N=[] X=['REF-0309'] M=['REF-1952<anti-inflammatory', 'REF-1958<anti-inflammatory']
- **respiratory-support** [verified,ev2] note=""
    D=['REF-0749'] N=[] X=[] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-1952', 'REF-1958', 'REF-0309'] M=['REF-0749<anti-inflammatory', 'REF-1951<emollient']
  REF-0309 [traditional] 2002  | WHO Monographs on Selected Medicinal Plants | NO-ID 
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:digestive, A:emollient, A:immunomodulator
     (no abstract)
  REF-0749 [narrative-review] 2024 Chemistry & Biodiversity | Borago officinalis L.: A Review on Extraction, Phytochemical, and Pharmacological Activities | doi:10.1002/cbdv.202301822 
     used: A:anti-inflammatory, A:antioxidant, D:cold, D:inflammation, D:respiratory-support, M:arthritis, M:skin-irritation
     C: Its pharmacological properties and biological activities - among them antioxidant, antimicrobial, anticancer, anti-inflammatory, insecticidal, antigenotoxic, and anti-obesity activity - were demonstrated in vitro and in vivo and are related to its rich content of bioactive compounds (mainly phenolic acids, flavonoids, anthocyanins, alkaloids, and terpenes) extracted from various parts of B. officinalis including leav
  REF-1950 [preclinical] 2020 Frontiers in Veterinary Science | Protective Effects of Borago officinalis (Borago) on Cold Restraint Stress-Induced Gastric Ulcers in Rats: A Pilot Study | doi:10.3389/fvets.2020.00427 
     used: A:digestive, M:indigestion
     C: Organic extract showed also a significant cytotoxic effect at 500 and 1,000 mg/kg with a 3T3 cell viability reduction of 43.6% ( ** p < 0.01) and 92.1% ( *** p < 0.001), respectively. Borago aqueous extract at 10 mg/kg could be considered as a potential protective agent against stress-induced ulcers, and it is reasonable to possibly ascribe such protective activity to a modulation of the NR2A and NR2B subunit express
  REF-1951 [preclinical] 2018 Experimental Gerontology | Borago officinalis L. attenuates UVB-induced skin photodamage via regulation of AP-1 and Nrf2/ARE pathway in normal human dermal fibroblasts and promo | doi:10.1016/j.exger.2018.02.017 
     used: A:antioxidant, A:emollient, M:eczema, M:skin-irritation
     C: Moreover, skin hydration and collagen synthesis were improved by dietary BO treatment. Our results demonstrate that BO can be used in functional foods, cosmetic products, and medicines for prevention and treatment of UVB-induced skin photodamage.
  REF-1952 [rct] 2016 Tanaffos | Effect of Borago Officinalis Extract on Moderate Persistent Asthma: A Phase two Randomized, Double Blind, Placebo-Controlled Clinical Trial | doi:10.1183/13993003.congress-2016.pa4116 
     used: A:anti-inflammatory, M:inflammation
     C: Borago improved the clinical findings of asthma, but it was not able to suppress the inflammation involved in asthma.
     !NULL: Physiological parameters including spirometry, FENO, and sputum cytology including eosinophil and neutrophil did not change significantly.
  REF-1953 [preclinical] 2016 Nutrients | Cancer Prevention and Health Benefices of Traditionally Consumed Borago officinalis Plants | doi:10.3390/nu8010048 
     used: A:anticancer, A:antioxidant, D:cancer
     C: B. officinalis exerts DNA protection and anticarcinogenic effects as do its component rosmarinic acid and the mixture of the main phenolics presented in the plant. In conclusion, the results showed that B. officinalis may represent a high value plant for pleiotropic uses and support its consumption as a nutraceutical plant.
  REF-1956 [preclinical] 2022 Antioxidants | Neuroprotective Profile of Edible Flowers of Borage (Borago officinalis L.) in Two Different Models: Caenorhabditis elegans and Neuro-2a Cells | doi:10.3390/antiox11071244 
     used: A:antioxidant
     C: B. officinalis flower extract showed promising antioxidant activity in the selected models, without causing toxicity. Hence, the results obtained support the antioxidant properties of borage flowers in different bioassays using living organisms.
  REF-1958 [clinical] 2021 Cellular and Molecular Biology | The effect of Borago officinalis on the signaling pathway of the NLRP3 inflammasome complex, TLR4 and some inflammatory cytokines in type II diabetic  | doi:10.14715/cmb/2021.67.3.28 
     used: A:anti-inflammatory, A:immunomodulator, M:immune-support, M:inflammation
     C: Thus, in the early and middle stages of ARDS, borage oil can be effective in reducing the inflammasome pathway of inflammation and also reduce blood sugar levels in these diabetic patients. But in the severe stage of ARDS, it not only does not help to treat the ARDS; it also increases systolic and diastolic blood pressure in diabetic patients.

## boswellia-serrata - Boswellia serrata - Boswellia, Indian frankincense, Salai guggul
actions: analgesic=['REF-0422', 'REF-0573', 'REF-1810', 'REF-1816']; anti-inflammatory=['REF-0573', 'REF-1809', 'REF-1810', 'REF-1811', 'REF-1812', 'REF-1813', 'REF-1815', 'REF-1816', 'REF-1818']; anticancer=['REF-1814', 'REF-2873', 'REF-2876']
- **arthritis** [verified,ev9] note="Osteoarthritis: reduces joint pain and stiffness and improves function (over at least 4 weeks); Supports inflammatory arthritis including rheumatoid arthritis"
    D=['REF-0422', 'REF-0573', 'REF-0574'] N=[] X=['REF-1811', 'REF-1813'] M=['REF-1809<anti-inflammatory', 'REF-1810<anti-inflammatory', 'REF-1812<anti-inflammatory', 'REF-1815<anti-inflammatory', 'REF-1816<anti-inflammatory', 'REF-1818<anti-inflammatory']
- **cancer** [needs-review,ev2] note="Boswellia serrata resin and its triterpenoid AKBA arrest the cell cycle and induce apoptosis in non-small-cell lung cancer, suppress colitis-associated colorectal cancer (NF-kB, gut microbiota) and inhibit prostate cancer (IL-17 pathway) in vitro and in vivo (preclinical)."
    D=['REF-1814', 'REF-2873', 'REF-2876'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev5] !INF note="inferred from anti-inflammatory action"
    D=['REF-0573'] N=[] X=[] M=['REF-1809<anti-inflammatory', 'REF-1810<anti-inflammatory', 'REF-1811<anti-inflammatory', 'REF-1812<anti-inflammatory', 'REF-1813<anti-inflammatory', 'REF-1815<anti-inflammatory', 'REF-1816<anti-inflammatory', 'REF-1818<anti-inflammatory']
- **pain** [verified,ev9] note="Analgesic (pain relief); Osteoarthritis: reduces joint pain and stiffness and improves function (over at least 4 weeks)"
    D=['REF-0422', 'REF-0573', 'REF-0574'] N=[] X=[] M=['REF-1810<analgesic', 'REF-1816<analgesic']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0573', 'REF-1810', 'REF-1811', 'REF-1813', 'REF-1816'] M=['REF-1809<anti-inflammatory', 'REF-1812<anti-inflammatory', 'REF-1815<anti-inflammatory', 'REF-1818<anti-inflammatory']
  REF-0422 [systematic-review] 2020 BMC Complementary Medicine and Therapies | Effectiveness of Boswellia and Boswellia extract for osteoarthritis patients: a systematic review and meta-analysis | doi:10.1186/s12906-020-02985-6 
     used: A:analgesic, D:arthritis, D:pain
     C: Based on current evidence, Boswellia and its extract may be an effective and safe treatment option for patient with OA, and the recommended duration of treatment with Boswellia and its extract is at least 4 weeks.
  REF-0573 [rct] 2019 Phytotherapy Research | A pilot, randomized, double-blind, placebo-controlled trial to assess the safety and efficacy of a novel Boswellia serrata extract in the management o | doi:10.1002/ptr.6338 
     used: A:analgesic, A:anti-inflammatory, D:arthritis, D:inflammation, D:pain
     C: This is the first study with BSE conducted for a period of 120 days, longer than any other previous clinical trial on patients with OA of the knee. The findings provide evidence that biologically active constituents of BSE, namely, AKBBA and BBA, act synergistically to exert anti-inflammatory/anti-arthritic activity showing improvement in physical and functional ability and reducing the pain and stiffness.
  REF-0574 [systematic-review] 2018 British Journal of Sports Medicine | Dietary supplements for treating osteoarthritis: a systematic review and meta-analysis | doi:10.1136/bjsports-2016-097333 
     used: D:arthritis, D:pain
     C: The overall analysis including all trials showed that supplements provided moderate and clinically meaningful treatment effects on pain and function in patients with hand, hip or knee osteoarthritis at short term, although the quality of evidence was very low. Some supplements with a limited number of studies and participants suggested large treatment effects, while widely used supplements such as glucosamine and cho
     !NULL: There were no differences between supplements and placebo for safety outcomes, except for diacerein.
     !NULL: The Grading of Recommendations Assessment, Development and Evaluation suggested a wide range of quality evidence from very low to high.
     !NULL: Conclusions The overall analysis including all trials showed that supplements provided moderate and clinically meaningful treatment effects on pain and function in patients with hand, hip or knee osteoarthritis at short term, although the quality of evidence was very low.
  REF-1809 [narrative-review] 2011 Indian Journal of Pharmaceutical Science | Boswellia serrata, a potential antiinflammatory agent: an overview | doi:10.4103/0250-474X.93507 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The resinous part of Boswellia serrata possesses monoterpenes, diterpenes, triterpenes, tetracyclic triterpenic acids and four major pentacyclic triterpenic acids i.e. β-boswellic acid, acetyl-β-boswellic acid, 11-keto-β-boswellic acid and acetyl-11-keto-β-boswellic acid, responsible for inhibition of pro-inflammatory enzymes. Out of these four boswellic acids, acetyl-11-keto-β-boswellic acid is the most potent inhib
  REF-1810 [rct] 2022 Journal of the American Nutrition Associ | Efficacy and Safety of Aflapin, a Novel Boswellia serrata Extract, in the Treatment of Osteoarthritis of the Knee: A Short-Term 30-Day Randomized, Dou | doi:10.1080/07315724.2021.2014370 
     used: A:analgesic, A:anti-inflammatory, M:arthritis, M:inflammation, M:pain
     C: This investigation affirms that Aflapin is clinically efficacious, fast-acting, and safe in the management of osteoarthritis. No significant adverse effects were observed.
     !NULL: No significant adverse effects were observed.
  REF-1811 [rct] 2011 Cancer | Boswellia serrata acts on cerebral edema in patients irradiated for brain tumors: a prospective, randomized, placebo-controlled, double-blind pilot tr | doi:10.1002/cncr.25945 
     used: A:anti-inflammatory, M:inflammation
     C: BS significantly reduced cerebral edema measured by MRI in the study population. BS could potentially be steroid-sparing for patients receiving brain irradiation. Our findings will need to be further validated in larger studies.
  REF-1812 [narrative-review] 2011 Clinical Pharmacokinetics | Boswellia serrata: an overall assessment of in vitro, preclinical, pharmacokinetic and clinical data | doi:10.2165/11586800-000000000-00000 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: In view of the results of clinical trials and the experimental data from in vitro studies of BSE, and the available pharmacokinetic and metabolic data on boswellic acids, this review presents different perspectives and gives a differentiated insight into the possible mechanisms of action of BSE in humans. It underlines BSE as a promising alternative to NSAIDs, which warrants investigation in further pharmacological s
     !NULL: However, boswellic acids failed to inhibit leukotriene formation in human whole blood, and pharmacokinetic data revealed very low concentrations of AKBA and KBA in plasma, being far below the effective concentrations for bioactivity in vitro.
  REF-1813 [narrative-review] 2021 Inflammopharmacology | Boswellic acids/Boswellia serrata extract as a potential COVID-19 therapeutic agent in the elderly | doi:10.1007/s10787-021-00841-8 
     used: A:anti-inflammatory, M:inflammation
     C: However, large doses of BA may be beneficial in suppressing uncontrolled activation of the innate immune response. More clinical results are required to determine with certainty whether there is sufficient evidence of the benefits against COVID-19.
  REF-1814 [narrative-review] 2016 Journal of Ethnopharmacology | Pharmacological evidences for cytotoxic and antitumor properties of Boswellic acids from Boswellia serrata | doi:10.1016/j.jep.2016.06.053 
     used: A:anticancer, D:cancer
     C: Boswellic acids appear to be promising candidates for anticancer drug development in future. However, further in vivo studies are needed. Studies in combination with clinically used anticancer drugs and QSAR studies on individual boswellic acid also need to be carried out.
  REF-1815 [narrative-review] 2010 Phytomedicine | Modulation of the immune system by Boswellia serrata extracts and boswellic acids | doi:10.1016/j.phymed.2010.03.003 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Here, BEs as well as BAs have been found to be inhibitory. From the pharmacological properties of BEs and BAs it is not surprising that positive effects of BEs in some chronic inflammatory diseases including rheumatoid arthritis, bronchial asthma, osteoarthritis, ulcerative colitis and Crohn's disease have been reported.
  REF-1816 [preclinical] 2020 Evidence-Based Complementary and Alterna | An Anti-Inflammatory Composition of Boswellia serrata Resin Extracts Alleviates Pain and Protects Cartilage in Monoiodoacetate-Induced Osteoarthritis  | doi:10.1155/2020/7381625 
     used: A:analgesic, A:anti-inflammatory, M:arthritis, M:inflammation, M:pain
     C: Besides, the histological observations on Safranin-O green stained articular cartilage revealed that LI13019F1 also prevented the MIA-induced structural damage of the cartilage and reduced the loss of the extracellular matrix (ECM) components in the experimental rats. In conclusion, the present observations suggest that LI13019F1, a new composition of B. serrata gum resin extracts, reduces pain and protects articular
  REF-1818 [narrative-review] 2023 Doklady Biological Sciences | Component Composition and Biological Activity of Oleo-Gum Resin from Boswellia serrata (Burseraceae) | doi:10.1134/S0012496623700643 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Boswellic acids (BAs), which belong to the tetra- and pentacyclic triterpenoid classes, showed the highest anti-inflammatory activity. The frankincense resin is traditionally used in Ayurvedic and Unani medicine and can provide a promising source to design drugs effective in treating musculoskeletal disorders.
  REF-2873 [preclinical] 2020 OncoTargets and Therapy | Acetyl-11-Keto-beta-Boswellic Acid Exerts the Anti-Cancer Effects via Cell Cycle Arrest, Apoptosis Induction and Autophagy Suppression in Non-Small Ce | pmid:32158225 doi:10.2147/OTT.S236346 
     used: A:anticancer, D:cancer
     C: AKBA exerts the anti-cancer effects via cell cycle arrest, apoptosis induction, and autophagy suppression in NSCLC cells. This body of evidence supports the potential of AKBA as a promising drug in the treatment of NSCLC.
  REF-2876 [narrative-review] 2023 Naunyn-Schmiedeberg's Archives of Pharma | The journey of boswellic acids from synthesis to pharmacological activities | pmid:37740772 doi:10.1007/s00210-023-02725-w 
     used: A:anticancer, D:cancer
     C: Activation of caspases, upregulation of Bax expression, downregulation of nuclear factor-kappa B (NF-kB), and stimulation of poly (ADP)-ribose polymerase (PARP) cleavage are the primary mechanisms responsible for cytotoxic and antitumor effects. Evidence suggests that BAs have shown promise in combating a wide range of debilitating disease conditions, including cancer, hepatic, inflammatory, and neurological disorder

## calendula-officinalis - Calendula officinalis - Pot marigold, Calendula, common marigold
actions: anti-inflammatory=['REF-0112', 'REF-0199', 'REF-0753', 'REF-2126', 'REF-2128']; anticancer=['REF-2124', 'REF-0753', 'REF-2877']; antifungal=['REF-0112', 'REF-0199']; antimicrobial=['REF-0112', 'REF-0199', 'REF-2127']; antioxidant=['REF-0112', 'REF-0199', 'REF-2124', 'REF-2130']; emollient=['REF-0112', 'REF-0199']; vulnerary=['REF-0112', 'REF-0199', 'REF-0752', 'REF-2125', 'REF-2129']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0199', 'REF-2128', 'REF-0112'] M=['REF-0753<anti-inflammatory', 'REF-2126<anti-inflammatory']
- **cancer** [needs-review,ev7] note="A Calendula officinalis (LACE) aqueous extract inhibits proliferation (70-100%) of leukemia, melanoma, breast, prostate, lung and colon cancer cell lines via G0/G1 arrest and caspase-3 apoptosis and inhibits melanoma growth in nude mice; a systematic review documents its cytotoxic and antimetastatic antitumour activity (preclinical)."
    D=['REF-2124', 'REF-0753', 'REF-2877'] N=[] X=[] M=[]
- **infection** [needs-review,ev1] note="inferred from antifungal action"
    D=[] N=[] X=['REF-0199', 'REF-0112'] M=['REF-2127<antimicrobial']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0112', 'REF-0199'] M=['REF-0753<anti-inflammatory', 'REF-2126<anti-inflammatory', 'REF-2128<anti-inflammatory']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-2128', 'REF-0112', 'REF-0199'] M=['REF-0753<anti-inflammatory', 'REF-2126<anti-inflammatory']
- **wounds** [needs-review,ev8] !INF note="inferred from antimicrobial action"
    D=['REF-0199', 'REF-0752', 'REF-2125'] N=[] X=['REF-2127', 'REF-0112'] M=['REF-2129<vulnerary']
  REF-0112 [traditional] 2003  | Medical Herbalism | NO-ID 
     used: A:anti-inflammatory, A:antifungal, A:antimicrobial, A:antioxidant, A:emollient, A:vulnerary
     (no abstract)
  REF-0199 [preclinical] 2009  | Wound healing activity of flower extract of Calendula officinalis | doi:10.1515/jbcpp.2009.20.1.73 
     used: A:anti-inflammatory, A:antifungal, A:antimicrobial, A:antioxidant, A:emollient, A:vulnerary, D:wounds
     C: A significant increase was observed in the hydroxy proline and hexosamine content in the extract-treated group compared with the untreated animals. The data indicate potent wound healing activity ofC. officinalis extract.
  REF-0752 [systematic-review] 2019 Wound Repair and Regeneration | A systematic review of Calendula officinalis extract for wound healing | doi:10.1111/wrr.12737 
     used: A:vulnerary, D:wounds
     C: This review identified some evidence for the beneficial effects of C. officinalis extract for wound healing, consistent with its role in traditional medicine. There is a need for larger, well-designed randomized control trials to assess the effect of calendula on wound healing including complications.
     !NULL: Another randomized clinical trial demonstrated no improvement for the calendula group in diabetic leg ulcer healing.
     !NULL: A randomized clinical trial of patients suffering from partial to full thickness burns demonstrated no benefit for topical application of calendula extract compared to controls.
     !NULL: Two randomized clinical trials assessed the potential for extract to prevent acute post radiation dermatitis, with one study showing improvements compared to trolamine, while the other found no improvement compared to aqua gel cream.
  REF-0753 [narrative-review] 2023 Pharmaceuticals (Basel) | An Updated Review on the Multifaceted Therapeutic Potential of Calendula officinalis L. | doi:10.3390/ph16040611 
     used: A:anti-inflammatory, A:anticancer, D:cancer, M:arthritis, M:inflammation, M:skin-irritation
     C: We have also elucidated CO's molecular mechanisms and recent clinical studies. Overall, this review intends to summarize, fill in the gaps in the existing research, and provide a wealth of possibilities for researchers working to validate traditional claims and advance the safe and effective use of CO in treating various ailments.
  REF-2124 [systematic-review] 2018 Integrative Cancer Therapies | Calendula officinalis: potential roles in cancer treatment and palliative care | doi:10.1177/1534735418803766 
     used: A:anticancer, A:antioxidant, D:cancer
     C: Nevertheless, its cytotoxic activity is related to a few bioactive compounds, presenting multiple roles in both activation of proapoptotic proteins and decreasing the expression of the proteins that inhibit cell death. Moreover, due to its anti-genotoxic/protective as well as antitumor and antimetastatic effects proven in animal models, C officinalis could have important future implications in developing novel cancer
  REF-2125 [rct] 2023 Scars, Burns & Healing | Effect of oral Calendula officinalis on second-degree burn wound healing | doi:10.1177/20595131221134053 
     used: A:vulnerary, D:wounds
     C: Based on the results of this study, C. officinalis may have beneficial healing properties and be effective in accelerating the healing of second-degree burn wounds and can be used as a supplement to treat wounds.
  REF-2126 [preclinical] 2023 Bioscience, Biotechnology, and Biochemis | Prenylated acetophenones from the roots of Calendula officinalis and their anti-inflammatory activity | doi:10.1093/bbb/zbad042 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Both compounds decreased lipopolysaccharide-stimulated NO production in J774.1 cells. This study could lead to the use of the Calendula roots as a natural source of inflammatory mediators.
  REF-2127 [preclinical] 2022 Natural Product Research | A new antiprotozoal compound from Calendula officinalis | doi:10.1080/14786419.2021.2023868 
     used: A:antimicrobial, M:infection
     C: Compound 1 showed leishmanicidal activity against L. donovani amastigote with an IC 50 of 16.4394 µM and IC 90 of 28.9015 µM and a weak antitrypanosomal activity with an IC 50 of 37.6136 µM. The cytotoxicity of 1 was evaluated using standard experimental procedures against THP1 cells and no cytotoxicity was observed indicating its selectivity and safety.Supplemental data for this article can be accessed here.
  REF-2128 [preclinical] 2016 Pharmaceutical Biology | Calendula officinalis ameliorates l-arginine-induced acute necrotizing pancreatitis in rats | doi:10.1080/13880209.2016.1195848 
     used: A:anti-inflammatory, M:inflammation
     C: Discussion and conclusion The beneficial effect of COE may be attributed to its antioxidant, antinitrosative and antifibrotic actions. Hence, the study concludes that COE promotes spontaneous repair and regeneration of the pancreas.
  REF-2129 [preclinical] 2014 Anatomical Record | Effect of Calendula officinalis cream on achilles tendon healing | doi:10.1002/ar.23057 
     used: A:vulnerary, M:wounds
     C: Immunocytochemistry analysis for chondroitin-6-sulfate showed no difference between the C and Cal groups. In conclusion, the topical application of C. officinalis after tendon transection increases the concentrations of collagen and non-collagenous proteins, as well as the collagen organization in the initial phase of healing.
     !NULL: Zymography showed no difference in the amount of the isoforms of metalloproteinase-2 and of metalloproteinase-9, between C and Cal groups.
     !NULL: Immunocytochemistry analysis for chondroitin-6-sulfate showed no difference between the C and Cal groups.
  REF-2130 [preclinical] 2023 Food Science & Nutrition | Active compounds from Calendula officinalis flowers act via PI3K and ERK signaling pathways to offer neuroprotective effects against Parkinson's disea | doi:10.1002/fsn3.3792 
     used: A:antioxidant
     C: These compounds from C. officinalis could be potent nutraceutical agents with protective properties that may shield dopaminergic neurons against the damage caused by PD. Our findings provide a basis for utilizing the C. officinalis flowers in functional foods.
  REF-2877 [preclinical] 2006 BMC Cancer | A new extract of the plant Calendula officinalis produces a dual in vitro effect: cytotoxic anti-tumor activity and lymphocyte activation | pmid:16677386 doi:10.1186/1471-2407-6-119 
     used: A:anticancer, D:cancer
     C: These results indicate that LACE aqueous extract has two complementary activities in vitro with potential anti-tumor therapeutic effect: cytotoxic tumor cell activity and lymphocyte activation. The LACE extract presented in vivo anti-tumoral activity in nude mice against tumor growth of Ando-2 melanoma cells.

## camellia-sinensis - Camellia sinensis - Tea, green tea, black tea
actions: anti-inflammatory=['REF-0045']; anticancer=['REF-0045', 'REF-1960', 'REF-1961', 'REF-1965']; antidiabetic=['REF-0045']; antimicrobial=['REF-0045', 'REF-1964', 'REF-1967', 'REF-1968']; antioxidant=['REF-0045', 'REF-1960', 'REF-1962', 'REF-1966']; neuroprotective=['REF-0045', 'REF-1962']
- **blood-sugar** [needs-review,ev2] !INF note="inferred from antidiabetic action"
    D=['REF-0045'] N=[] X=[] M=[]
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1965'] N=['REF-1961'] X=[] M=['REF-0045<anticancer', 'REF-1960<anticancer']
- **cardiovascular-support** [verified,ev2] note=""
    D=['REF-0045'] N=[] X=[] M=[]
- **cognitive-function** [needs-review,ev5] !INF note="inferred from neuroprotective action"
    D=['REF-0184'] N=[] X=['REF-0045'] M=['REF-1962<neuroprotective']
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0045'] M=['REF-1964<antimicrobial', 'REF-1967<antimicrobial', 'REF-1968<antimicrobial']
- **memory** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-0045'] M=['REF-1962<neuroprotective']
- **metabolic-support** [verified,ev2] note=""
    D=['REF-0045'] N=[] X=[] M=[]
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-1964', 'REF-1968', 'REF-0045'] M=['REF-1967<antimicrobial']
  REF-0045 [narrative-review] 2010  | Beneficial effects of green tea: a literature review | doi:10.1186/1749-8546-5-13 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:neuroprotective, D:blood-sugar, D:cardiovascular-support, D:metabolic-support, M:cancer
     C: There are also human studies on using green tea catechins to treat metabolic syndrome, such as obesity, type II diabetes, and cardiovascular risk factors.Long-term consumption of tea catechins could be beneficial against high-fat diet-induced obesity and type II diabetes and could reduce the risk of coronary disease. Further research that conforms to international standards should be performed to monitor the pharmaco
  REF-0184 [rct] 2008  | L-theanine, a natural constituent in tea, and its effect on mental state | NO-ID 
     used: D:cognitive-function
     C: These data indicate that L-theanine, at realistic dietary levels, has a significant effect on the general state of mental alertness or arousal. Furthermore, alpha activity is known to play an important role in critical aspects of attention, and further research is therefore focussed on understanding the effect of L-theanine on attentional processes.
  REF-1960 [narrative-review] 2022 Molecules | Green Tea (Camellia sinensis): A Review of Its Phytochemistry, Pharmacology, and Toxicology | doi:10.3390/molecules27123909 
     used: A:anticancer, A:antioxidant, M:cancer
     C: Summary Green tea can be used to assist the treatment of diabetes, Alzheimer's disease, oral cancer, and dermatitis. Consequently, green tea has shown promising practical prospects in health care and disease prevention.
  REF-1961 [meta-analysis] 2020 Cochrane Database of Systematic Reviews | Green tea (Camellia sinensis) for the prevention of cancer | doi:10.1002/14651858.CD005004.pub3 
     used: A:anticancer, N:cancer
     C: In addition, the majority of included studies were carried out in Asian populations characterised by a high intake of green tea, thus limiting the generalisability of the findings to other populations. Well conducted and adequately powered RCTs would be needed to draw conclusions on the possible beneficial effects of green tea consumption on cancer risk.
     !NULL: No evidence of effect of non-melanoma skin cancer emerged (summary RR 1.
     !NULL: After stratifying the analysis according to study design, we found strongly conflicting results for some cancer sites: oesophageal, prostate and urinary tract cancer, and leukaemia showed an increased RR in cohort studies and a decreased RR or no difference in case-control studies.
     !NULL: Authors' conclusions Overall, findings from experimental and nonexperimental epidemiological studies yielded inconsistent results, thus providing limited evidence for the beneficial effect of green tea consumption on the overall risk of cancer or on specific cancer sites.
  REF-1962 [narrative-review] 2019 Nutrients | A Review of the Role of Green Tea (Camellia sinensis) in Antiphotoaging, Stress Resistance, Neuroprotection, and Autophagy | doi:10.3390/nu11020474 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: Green tea was able to activate autophagy in HL-60 xenographs by increasing the activity of PI3 kinase and BECLIN-1. This manuscript describes the reported anti-photoaging, stress resistance, and neuroprotective and autophagy properties of one of the most widely known functional foods-green tea.
  REF-1964 [narrative-review] 2001 Journal of Medical Microbiology | Anti-cariogenic properties of tea (Camellia sinensis) | doi:10.1099/0022-1317-50-4-299 
     used: A:antimicrobial, M:infection
     C: A limited number of clinical trials in man suggest that regular tea drinking may reduce the incidence and severity of caries. If substantiated, this could offer a very economical public health intervention.
  REF-1965 [narrative-review] 2015 Anti-Cancer Agents in Medicinal Chemistr | Tea (Camellia sinensis (L.)): a putative anticancer agent in bladder carcinoma? | doi:10.2174/1566524014666141203143143 
     used: A:anticancer, D:cancer
     C: The mechanisms responsible for this protection include deregulation of cell cycle, induction of apoptosis while protecting the surrounding healthy bladder cells, inhibition of metastization processes, among others. Herein, we discuss the potential beneficial effects of tea and tea components in bladder cancer prevention and/or treatment, and how they can be helpful in finding new therapeutic strategies to treat this 
  REF-1966 [narrative-review] 2009 British Journal of Nutrition | Green tea (Camellia sinensis) catechins and vascular function | doi:10.1017/S0007114509991218 
     used: A:antioxidant
     C: In conclusion, a positive effect of green tea catechins on vascular function is becoming apparent. Further studies in animal and cell models using physiological concentrations of catechins and their metabolites are warranted in order to gain some insight into the physiology and molecular basis of the observed beneficial effects.
  REF-1967 [narrative-review] 2021 Current Topics in Medicinal Chemistry | Chemistry and Pharmacology of Natural Catechins from Camellia sinensis as Anti-MRSA Agents | doi:10.2174/1568026621666210524100632 
     used: A:antimicrobial, M:infection, M:wounds
     C: MRSA also exhibits resistance to cephalosporins, macrolides, fluoroquinolones, aminoglycosides, and glycopeptides (teicoplanine and vancomycin), leading to resistant strains-glycopeptide resistant strain (GRSA) and glycopeptide intermediate (GISA) S. aureus. In this review, chemical constituents responsible for the anti-MRSA activity of tea are explored.
  REF-1968 [systematic-review] 2020 Journal of Dentistry (Shiraz) | Camellia Sinensis Mouthwashes in Oral Care: a Systematic Review | doi:10.30476/DENTJODS.2020.83204.1045 
     used: A:antimicrobial, M:infection
     C: We explored three scientific databases with keywords including tea, dental care, Camellia sinensis, and mouthwashes and found 69 relevant studies including 41 randomized controlled trials (RCTs), which are generally proposing anti-microbial, anti-plaque, and analgesic indications for these tea formulations. Considering the main trend in clinical evidence and favorable safety profile, Camellia sinensis products are ab

## campanula-persicifolia - Campanula persicifolia - Peach-leaved bellflower, fairy bellflower, peach-leaf bellflower
actions: antioxidant=['REF-2816', 'REF-2817']; anti-inflammatory=['REF-2816']; antimicrobial=['REF-2816']; vulnerary=[]
  REF-2816 [narrative-review] 2025 Molecules | Bioactive Compounds Isolated from the Campanula Genus: A Review | doi:10.3390/molecules30234495 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant
     C: It also highlights underexplored species and compound classes with potential therapeutic significance. By integrating the phytochemical evidence with pharmacological insights, this work underscores the value of the Campanula species as promising natural resources for future drug discovery and development.
  REF-2817 [preclinical] 2008 Natural Product Research | Chemical composition and antioxidant activity of Campanula alliariifolia | doi:10.1080/14786410701640429 
     used: A:antioxidant
     C: The methanol extract has antioxidant capacity according to the mentioned methods. Lobetyol and lobetyolin showed significant antioxidant activity more than both methanol extract and other purified compounds.
