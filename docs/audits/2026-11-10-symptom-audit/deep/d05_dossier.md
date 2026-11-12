# Deep dossier batch 5

## cnicus-benedictus - Cnicus benedictus - Blessed Thistle, Holy thistle, St Benedict's thistle
actions: anti-inflammatory=['REF-0419', 'REF-0773', 'REF-1997']; anticancer=['REF-1995']; antimicrobial=['REF-0419', 'REF-0773', 'REF-1996']; appetite-stimulant=['REF-0419', 'REF-0420']; bitter-tonic=['REF-0419', 'REF-0420']; digestive=['REF-0419', 'REF-0420']; galactagogue=['REF-0420', 'REF-0421']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0419'] M=['REF-0773<anti-inflammatory', 'REF-1997<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1995'] N=[] X=[] M=[]
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0419'] M=['REF-0773<antimicrobial', 'REF-1996<antimicrobial']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0419'] M=['REF-0773<anti-inflammatory', 'REF-1997<anti-inflammatory']
- **lactation-support** [needs-review,ev1] note="Galactagogue to support breast-milk supply (traditional; no valid clinical-trial evidence)"
    D=['REF-0421'] N=[] X=[] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0419'] M=['REF-0773<anti-inflammatory', 'REF-1997<anti-inflammatory']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0419'] M=['REF-0773<antimicrobial', 'REF-1996<antimicrobial']
  REF-0419 [narrative-review] 2024 Planta Medica | Cnicus benedictus: Folk Medicinal Uses, Biological Activities, and In Silico Screening of Main Phytochemical Constituents | doi:10.1055/a-2401-6049 
     used: A:anti-inflammatory, A:antimicrobial, A:appetite-stimulant, A:bitter-tonic, A:digestive
     C: The bioactive compounds that can be extracted from it, such as the sesquiterpene lactones arctigenin, arctiin, and cnicin, are very interesting to researchers.In this article, based on available data from pre-clinical in vitro and in vivo studies, we delve into the pharmacology of the active constituents of this plant to explore its potential therapeutic applications and underlying mechanisms of action. In addition, 
  REF-0420 [traditional] n.d.  | Blessed Thistle Uses, Benefits & Dosage | NO-ID 
     used: A:appetite-stimulant, A:bitter-tonic, A:digestive, A:galactagogue
     (no abstract)
  REF-0421 [traditional] 2021  | Blessed Thistle | NO-ID 
     used: A:galactagogue, D:lactation-support
     (no abstract)
  REF-0773 [preclinical] 2023 Chemistry & Biodiversity | HPLC/ESI-MS Characterization of Phenolic Compounds from Cnicus benedictus L. Roots: A Study of Antioxidant, Antibacterial, Anti-Inflammatory, and Anti | doi:10.1002/cbdv.202300724 
     used: A:anti-inflammatory, A:antimicrobial, M:arthritis, M:infection, M:inflammation, M:skin-irritation, M:wounds
     C: Likewise, anti-Alzheimer activity of extracts was confirmed by this last technique taking into account the major compounds identified. Antibacterial tests revealed interesting results compared to amoxicillin for the different regions studied with a high content in trans chalcone and 3-hydroxy Flavone.
  REF-1995 [preclinical] 2024 Asian Pacific Journal of Cancer Preventi | In Vitro Evaluate the Antiproliferative Impact of Cnicus Benedictus L. Leaves Methanolic Extract on Cervical Cancer | doi:10.31557/APJCP.2024.25.10.3643 
     used: A:anticancer, D:cancer
     C: The study shows that Cnicus Benedictus leaves methanolic extract has ability to inhibit the growth of human cervical cancer cells in vitro. The extract cytotoxic behavior was (cell cycle and cell non-cycle) specific. The research also found that the extract selectively kills cancer cells rather than normal cells, indicating its safety in their effectivity.
  REF-1996 [preclinical] 2017 Natural Product Research | Two new sesquiterpene lactone glycosides from Cnicus benedictus | doi:10.1080/14786419.2017.1295239 
     used: A:antimicrobial, M:infection, M:wounds
     C: Compounds 1-6 all possessed an α-methyl-γ-lactone moiety. Moreover, compound 5 exhibited moderate activity against the growth of Aspergillus fumigatus, with IC 50 values of 17.67 μg mL -1 .
  REF-1997 [preclinical] 2019 BioMed Research International | Chemical and Bioactivity Evaluation of Cnicus benedictus and Eryngium planum Polyphenolic-Rich Extracts | doi:10.1155/2019/3692605 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Both polyphenolic-rich extracts had a higher inhibitory effect on α -amylase and α -glucosidase than that of the acarbose. The synergistic effect of ursolic acid, rutin, chlorogenic acid, rosmarinic acid, genistin, and daidzein identified in polyphenolic-rich extracts could be mainly responsible for the pharmacological potentials of the studied extracts used in managing inflammation and diabetes.

## coffea-arabica - Coffea arabica - Coffee (Arabica & Robusta), Coffee
actions: antioxidant=['REF-0059', 'REF-0081', 'REF-0096', 'REF-0109', 'REF-0121', 'REF-0135', 'REF-0178', 'REF-0205', 'REF-2379', 'REF-2381', 'REF-2383', 'REF-2386']; neuroprotective=['REF-0059', 'REF-0081', 'REF-0096', 'REF-0109', 'REF-0121', 'REF-0135', 'REF-0178', 'REF-0205', 'REF-2380']
- **cardiovascular-support** [verified,ev7] note=""
    D=['REF-0059', 'REF-0109', 'REF-2384'] N=[] X=[] M=[]
- **cognitive-function** [needs-review,ev1] !INF note="inferred from neuroprotective action"
    D=['REF-0178'] N=[] X=['REF-0059', 'REF-0081', 'REF-0121', 'REF-0135', 'REF-0096', 'REF-0109', 'REF-0205'] M=['REF-2380<neuroprotective']
- **memory** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-0059', 'REF-0081', 'REF-0096', 'REF-0121', 'REF-0135', 'REF-0205', 'REF-0109', 'REF-0178'] M=['REF-2380<neuroprotective']
- **metabolic-support** [verified,ev2] note=""
    D=['REF-0109', 'REF-2379'] N=[] X=[] M=[]
  REF-0059 [systematic-review] 2014  | Long-term coffee consumption and risk of cardiovascular disease: a systematic review and a dose-response meta-analysis of prospective cohort studies | doi:10.1161/CIRCULATIONAHA.113.005925 
     used: A:antioxidant, A:neuroprotective, D:cardiovascular-support
     C: A nonlinear association between coffee consumption and CVD risk was observed in this meta-analysis. Moderate coffee consumption was inversely significantly associated with CVD risk, with the lowest CVD risk at 3 to 5 cups per day, and heavy coffee consumption was not associated with elevated CVD risk.
  REF-0081 [traditional] 2015  | Scientific Opinion on the safety of caffeine | doi:10.2903/j.efsa.2015.4102 
     used: A:antioxidant, A:neuroprotective
     (no abstract)
  REF-0096 [traditional] 2010  | International society of sports nutrition position stand: caffeine and performance | doi:10.1186/1550-2783-7-5 
     used: A:antioxidant, A:neuroprotective
     C: Position Statement: The position of The Society regarding caffeine supplementation and sport performance is summarized by the following seven points: 1.) Caffeine is effective for enhancing sport performance in trained athletes when consumed in low-to-moderate dosages (~3-6 mg/kg) and overall does not result in further enhancement in performance when consumed in higher dosages (>/= 9 mg/kg). 2.) Caffeine exerts a gre
     !NULL: ) The scientific literature does not support caffeine-induced diuresis during exercise, or any harmful change in fluid balance that would negatively affect performance.
  REF-0109 [narrative-review] 2006  | Coffee and health: a review of recent human research | doi:10.1080/10408390500400009 
     used: A:antioxidant, A:neuroprotective, D:cardiovascular-support, D:metabolic-support
     C: However, some groups, including people with hypertension, children, adolescents, and the elderly, may be more vulnerable to the adverse effects of caffeine. In addition, currently available evidence suggests that it may be prudent for pregnant women to limit coffee consumption to 3 cups/d providing no more than 300 mg/d of caffeine to exclude any increased probability of spontaneous abortion or impaired fetal growth.
  REF-0121 [traditional] 2023  | Coffee Report & Outlook 2023 | NO-ID 
     used: A:antioxidant, A:neuroprotective
     (no abstract)
  REF-0135 [systematic-review] 2016  | Systematic review with meta-analysis: coffee consumption and the risk of cirrhosis | doi:10.1111/apt.13523 
     used: A:antioxidant, A:neuroprotective
     C: This meta-analysis suggests that increasing coffee consumption may substantially reduce the risk of cirrhosis.
  REF-0178 [traditional] 2023  | Caffeine | NO-ID 
     used: A:antioxidant, A:neuroprotective, D:cognitive-function
     (no abstract)
  REF-0205 [clinical] 2000  | Association of coffee and caffeine intake with the risk of Parkinson disease | doi:10.1001/jama.283.20.2674 
     used: A:antioxidant, A:neuroprotective
     C: Our findings indicate that higher coffee and caffeine intake is associated with a significantly lower incidence of PD. This effect appears to be independent of smoking. The data suggest that the mechanism is related to caffeine intake and not to other nutrients contained in coffee. JAMA. 2000;283:2674-2679.
  REF-2379 [preclinical] 2023 Journal of Biomolecular Structure & Dyna | Hypoglycemic effect of Coffea arabica leaf extracts and major bioactive constituents | doi:10.1080/07391102.2023.2188421 
     used: A:antioxidant, D:metabolic-support
     C: Finally, these results suggest that C. arabica leaf extracts possess antidiabetic and anti-obesity properties that can be attributed to the main metabolites and the synergistic action between them.Communicated by Ramaswamy H. Sarma.
  REF-2380 [preclinical] 2025 Neurochemical Research | Targeting IDO1 in Huntington's Disease: Network Pharmacology and Preclinical Evidence from Coffea arabica | doi:10.1007/s11064-025-04509-5 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: STATEMENT: This study integrates network pharmacology, in silico modeling, and in vivo analysis to explore geraniol, a key metabolite of Coffea arabica, as a multi-target agent for Huntington's disease (HD). Geraniol showed strong binding to IDO1, restored cognitive and motor functions, balanced oxidative stress, and preserved striatal neurons in an HD rat model. Our findings suggest geraniol as a promising therapeut
  REF-2381 [narrative-review] 2025 Pharmaceuticals | Coffea arabica: An Emerging Active Ingredient in Dermato-Cosmetic Applications | doi:10.3390/ph18020171 
     used: A:antioxidant
     C: The findings of this review underscore the potential of Coffea arabica as a valuable active ingredient in dermato-cosmetic applications. Its multifaceted bioactivity suggests that it can contribute significantly to skin health and cosmetic efficacy. Future research should focus on clinical trials to further validate these benefits and explore optimal formulation strategies for enhanced delivery and stability in cosme
  REF-2383 [preclinical] 2023 International Journal of Molecular Scien | Coffea arabica Extract Attenuates Atopic Dermatitis-like Skin Lesions by Regulating NLRP3 Inflammasome Expression and Skin Barrier Functions | doi:10.3390/ijms241512367 
     used: A:antioxidant
     C: CAE also reduced transepidermal water loss (TEWL) and immune cell infiltration in DNCB-treated mice. Overall, CAE exerted anti-oxidation and anti-inflammation effects and ameliorated skin barrier dysfunction, suggesting its potential as an active ingredient for AD treatment.
  REF-2384 [preclinical] 2020 Molecules | Anti-Platelet Aggregation and Anti-Cyclooxygenase Activities for a Range of Coffee Extracts (Coffea arabica) | doi:10.3390/molecules26010010 
     used: D:cardiovascular-support
     C: Espresso, boiled and drip coffee extracts were also a more potent inhibitors of COX-1 and COX-2 than purified caffeine or CGA. We conclude that inhibition of platelet aggregation and COX-1 and COX-2 may contribute to anti-platelet and anti-inflammatory effects of espresso and drip coffee extracts.
  REF-2386 [preclinical] 2022 Foods | Characterization of Extracts of Coffee Leaves (Coffea arabica L.) by Spectroscopic and Chromatographic/Spectrometric Techniques | doi:10.3390/foods11162495 
     used: A:antioxidant
     C: In total, 39 compounds were identified. The presence of these bioactive compounds proved the strong potential of C. arabica leaves as functional food and as an alternative to classic infused beverages.

## cordyceps-militaris - Cordyceps militaris - Cordyceps, caterpillar fungus, Dong Chong Xia Cao (冬蟲夏草)
actions: anti-inflammatory=['REF-2161']; antioxidant=['REF-2153', 'REF-2156']; ergogenic=[]; immunomodulator=['REF-2153', 'REF-2155', 'REF-2156', 'REF-2157', 'REF-2160', 'REF-2163']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2161<anti-inflammatory']
- **cold** [needs-review,ev1] note="inferred from immunomodulator action"
    D=[] N=[] X=['REF-2153'] M=['REF-2155<immunomodulator', 'REF-2156<immunomodulator', 'REF-2157<immunomodulator', 'REF-2160<immunomodulator', 'REF-2163<immunomodulator']
- **immune-support** [needs-review,ev1] note=""
    D=[] N=[] X=['REF-2153'] M=['REF-2155<immunomodulator', 'REF-2156<immunomodulator', 'REF-2157<immunomodulator', 'REF-2160<immunomodulator', 'REF-2163<immunomodulator']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2161<anti-inflammatory']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2161<anti-inflammatory']
  REF-2153 [narrative-review] 2023 Fungal Biology and Biotechnology | Cordyceps militaris polysaccharides: preparation and topical product application | doi:10.1186/s40694-023-00150-5 
     used: A:antioxidant, A:immunomodulator
     C: Cordyceps militaris mycelium residue is a beneficial source for pharmaceutical products. The C. militaris polysaccharides extract was prepared and qualified in terms of active content and stability. The extract was shown to be compatible with the available cosmetic ingredients. The safe and preferred C. militaris polysaccharides skin care cosmetics was developed. Accordingly, C. militaris polysaccharides skin care co
  REF-2155 [narrative-review] 2022 Frontiers in Nutrition | Structural elucidation and activities of Cordyceps militaris-derived polysaccharides: a review | doi:10.3389/fnut.2022.898674 
     used: A:immunomodulator, M:cold, M:immune-support
     C: This review will discuss the methods used in the elucidation of the structure of polysaccharides and structural characteristics as well as the signaling pathways modulated by C. militaris -derived polysaccharides. This article provides information useful for the development of C. militaris -derived polysaccharides as well as for investigating other medicinal polysaccharides.
  REF-2156 [narrative-review] 2021 Foods | Cordyceps militaris: an overview of its chemical constituents in relation to biological activity | doi:10.3390/foods10112634 
     used: A:antioxidant, A:immunomodulator, M:cold, M:immune-support
     C: To summarize, based on the presence of several bioactive compounds that contribute to biological activity, C. militaris mushrooms definitely deserve to be considered as functional foods and also have great potential for medicinal use. Recent scientific reports indicate the potential of cordycepin in antiviral activity, particularly against COVID-19.
  REF-2157 [narrative-review] 2022 Ceska a Slovenska Farmacie | Medicinal mushrooms Ophiocordyceps sinensis and Cordyceps militaris | doi:10.5817/csf2022-5-259 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Polysaccharides were extracted from four samples: sample 1 (grown on the substrate Oryza sativa indica, strain Ophiocordyceps sinensis), sample 2 (grown on the substrate Oryza sativa japonica, strain Ophiocordyceps sinensis), sample 3 (grown on the substrate Oryza sativa indica, strain Cordyceps militaris), sample 4 (grown on Oryza sativa japonica substrate, strain Cordyceps militaris). Through NMR spectroscopy and s
  REF-2160 [narrative-review] 2019 International Journal of Biological Macr | Advance in Cordyceps militaris (Linn) Link polysaccharides: isolation, structure, and bioactivities: a review | doi:10.1016/j.ijbiomac.2019.04.020 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Therefore, this review detailed the recent advance in several aspects (i.e., extraction, isolation, structure, and bioactivities) of the polysaccharides from fruiting body of Cordyceps militaris. This information could provide theoretical basis for the research on related polysaccharides, and also have important reference value in the field of functional foods and medicine in the future.
  REF-2161 [preclinical] 2016 Journal of Agricultural and Food Chemist | Anti-inflammatory cerebrosides from cultivated Cordyceps militaris | doi:10.1021/acs.jafc.5b05931 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Cordycerebroside A (1), the new cerebroside, along with soyacerebroside I (2) and glucocerebroside (3) inhibited the accumulation of pro-inflammatory iNOS protein and reduced the expression of COX-2 protein in LPS-stimulated RAW264.7 macrophages. This is the first study on the isolation of cerebrosides with anti-inflammatory activity from this TCM.
  REF-2163 [narrative-review] 2015 Critical Reviews in Biotechnology | Biotechnological production and applications of Cordyceps militaris, a valued traditional Chinese medicine | doi:10.3109/07388551.2014.900604 
     used: A:immunomodulator, M:cold, M:immune-support
     C: This fungus has been the subject of many reviews, but few have focused on its biotechnological production of bioactive constituents. This mini-review focuses on the recent advances in the biotechnological production of bioactive compositions of C. militaris and the latest advances on novel applications from this laboratory and many others.

## coriandrum-sativum - Coriandrum sativum - Coriander, cilantro, Chinese parsley
actions: anti-inflammatory=['REF-0151', 'REF-0308', 'REF-1700', 'REF-1701', 'REF-1706', 'REF-1708']; antimicrobial=['REF-0151', 'REF-0308', 'REF-1701', 'REF-1705']; antioxidant=['REF-0151', 'REF-0308', 'REF-1701', 'REF-1702', 'REF-1704', 'REF-1706', 'REF-1707', 'REF-1708']; antispasmodic=['REF-0151', 'REF-0308']; digestive=['REF-0151', 'REF-0308', 'REF-1701']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-1706', 'REF-1708', 'REF-0308', 'REF-0151'] M=['REF-1700<anti-inflammatory', 'REF-1701<anti-inflammatory']
- **bloating** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0308', 'REF-0151'] M=['REF-1701<digestive']
- **indigestion** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0308', 'REF-0151'] M=['REF-1701<digestive']
- **infection** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0151'] N=[] X=['REF-0308'] M=['REF-1701<antimicrobial', 'REF-1705<antimicrobial']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0151'] N=[] X=['REF-0308'] M=['REF-1700<anti-inflammatory', 'REF-1701<anti-inflammatory', 'REF-1706<anti-inflammatory', 'REF-1708<anti-inflammatory']
- **metabolic-support** [verified,ev2] note=""
    D=['REF-0151'] N=[] X=[] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-1706', 'REF-1708', 'REF-0308', 'REF-0151'] M=['REF-1700<anti-inflammatory', 'REF-1701<anti-inflammatory']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0308', 'REF-0151'] M=['REF-1701<antimicrobial', 'REF-1705<antimicrobial']
  REF-0151 [narrative-review] 2015 Fitoterapia | Coriander (Coriandrum sativum L.) and its bioactive constituents | doi:10.1016/j.fitote.2015.03.012 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive, D:infection, D:inflammation, D:metabolic-support
     C: Although coriander has been reported to possess a wide range of traditional medicinal uses, no report is available in its effectiveness use in reactive airway diseases such as asthma and bronchiolitis. In brief, the information presented herein will be helpful to create more interest towards this medicinal species by defining novel pharmacological and clinical applications and hence, may be useful in developing new d
  REF-0308 [traditional] 1999  | WHO Monographs on Selected Medicinal Plants, Volume 1 | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-1700 [narrative-review] 2021 Molecules | Coriandrum sativum L.: A Review on Ethnopharmacology, Phytochemistry, and Cardiovascular Benefits | doi:10.3390/molecules27010209 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: As a result, most of the studies that cover cardiovascular benefits and fulfilled the eligibility criteria were in vivo, while only a few were in vitro and clinical studies. In conclusion, C. sativum can be deemed a functional food due to its wide range of cardiovascular benefits such as antihypertensive, anti-atherogenic, antiarrhythmic, hypolipidemic as well as cardioprotective effects.
  REF-1701 [narrative-review] 2017 Food Research International | Coriander (Coriandrum sativum): A promising functional food toward the well-being | doi:10.1016/j.foodres.2017.11.019 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:digestive, M:arthritis, M:bloating, M:indigestion, M:infection, M:inflammation, M:skin-irritation, M:wounds
     C: Apart from the modulating effects, the potent antioxidant property of the C. sativum provides a key mechanism behind its protective effects against neurodegenerative diseases, cancer, and metabolic syndrome. This review shed light on comprehensive aspects regarding the therapeutic values of the C. sativum, which indicate its significance of being a promising functional food for promoting the well-being in the era of 
  REF-1702 [narrative-review] 2015 Fitoterapia | Coriander (Coriandrum sativum L.) and its bioactive constituents | doi:10.1016/j.fitote.2015.03.012 
     used: A:antioxidant
     C: Although coriander has been reported to possess a wide range of traditional medicinal uses, no report is available in its effectiveness use in reactive airway diseases such as asthma and bronchiolitis. In brief, the information presented herein will be helpful to create more interest towards this medicinal species by defining novel pharmacological and clinical applications and hence, may be useful in developing new d
  REF-1704 [narrative-review] 2023 Molecules | Coriander (Coriandrum sativum) Polyphenols and Their Nutraceutical Value against Obesity and Metabolic Syndrome | doi:10.3390/molecules28104187 
     used: A:antioxidant
     C: After that, we focus on the evidence of coriander polyphenols as protective agents against some inflammation-related diseases. Due to the bioactivities of coriander extract, this herb can be considered a valuable functional food against obesity, metabolic syndrome and diabetes.
  REF-1705 [narrative-review] 2023 Molecules | Coriandrum sativum Essential Oil: A review on Its Phytochemistry and Biological Activity | doi:10.3390/molecules28020696 
     used: A:antimicrobial, M:infection, M:wounds
     C: The study also provides detailed information on various pharmacological properties of essential oils, such as antimicrobial, anthelmintic, insecticidal, allelopathic, antioxidant, antidiabetic, anticonvulsive, antidepressant, and hepatoprotective properties, as well as playing a major role in maintaining good digestive health. Coriander essential oil is one of the most promising alternatives in the food and pharmaceu
  REF-1706 [preclinical] 2020 Folia Morphologica | Protective effect of Coriandrum sativum extract against inflammation and apoptosis in liver ischaemia/reperfusion injury | doi:10.5603/FM.a2020.0060 
     used: A:anti-inflammatory, A:antioxidant, M:inflammation
     C: It was found that Coriandrum sativum extract decreased proinflammatory cytokine TNF-α and apoptotic cell death and liver enzymes in liver ischaemia/reperfusion injury.
     !NULL: There was no significant difference between the ALP levels of the IRI and IRI + Coriandrum sativum groups TNF-α, NF-κB and caspase-3 immune positive stained hepatocytes were numerous and widely observed in the injury group.
  REF-1707 [preclinical] 2016 American Journal of Chinese Medicine | Coriandrum sativum Suppresses Abeta42-Induced ROS Increases, Glial Cell Proliferation, and ERK Activation | doi:10.1142/S0192415X16500749 
     used: A:antioxidant
     C: The constitutively active form of ERK abolished the protective function of C. sativum extract against the [Formula: see text]-induced eye defect phenotype in Drosophila. Taken together, these results suggest that C. sativum leaves have antioxidant, anti-inflammatory, and ERK signaling inhibitory properties that are beneficial for patients with AD.
  REF-1708 [preclinical] 2021 EXCLI Journal | Coriandrum sativum attenuates microglia mediated neuroinflammation and MPTP-induced behavioral and oxidative changes in Parkinson's disease mouse mode | doi:10.17179/excli2021-3668 
     used: A:anti-inflammatory, A:antioxidant, M:inflammation
     C: High-performance thin-layer chromatography fingerprinting analysis of CSE exhibited several distinctive peaks with quercetin and kaempferol-3O-glucoside as identifiable compounds. In conclusion, our study indicated that CSE attenuated neuroinflammatory processes in LPS-stimulated microglia in vitro and restored the MPTP-induced behavioral deficits and brain oxidative enzyme status in vivo proving its therapeutic pote

## crataegus-laevigata - Crataegus laevigata - Midland Hawthorn, woodland hawthorn, may tree
actions: anti-inflammatory=['REF-0108', 'REF-2442', 'REF-1784']; antioxidant=['REF-0108', 'REF-2442', 'REF-0783', 'REF-1780', 'REF-1781', 'REF-1782', 'REF-1783', 'REF-1784']; antispasmodic=['REF-0108', 'REF-2442', 'REF-0783', 'REF-1785', 'REF-1786']; sedative=['REF-0108', 'REF-2442', 'REF-1787']
- **cardiovascular-support** [verified,ev7] note=""
    D=['REF-2442', 'REF-0082'] N=[] X=[] M=[]
- **insomnia** [needs-review,ev1] !INF note="inferred from sedative action"
    D=['REF-0082'] N=[] X=['REF-2442', 'REF-0108'] M=['REF-1787<sedative']
  REF-0082 [traditional] 2016  | European Union herbal monograph on Crataegus spp., folium cum flore | NO-ID 
     used: D:cardiovascular-support, D:insomnia
     (no abstract)
  REF-0108 [traditional] 2014  | Hedgerow Medicine | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:sedative
     (no abstract)
  REF-0783 [traditional] 2018 Current Medicinal Chemistry | Phytochemical and Pharmacological Activity Profile of Crataegus oxyacantha L. (Hawthorn) - A Cardiotonic Herb | doi:10.2174/0929867323666160919095519 
     used: A:antioxidant, A:antispasmodic
     C: Numerous experiments and clinical studies have underlined cardiovascular efficacy of the plant through various mechanisms including positive inotropic and negative chronotropic effects, escalation in coronary blood flow and exercise tolerance, inhibition of the enzymes such as angiotensinconverting enzyme (ACE) and phosphodiesterase, anti-inflammatory and antihyperlipidemic effects, improving status of antioxidant en
  REF-1780 [preclinical] 2018 Drug Research | Ethanol Extract of Crataegus Oxyacantha L. Ameliorate Dietary Non-Alcoholic Fatty Liver Disease in Rat | doi:10.1055/a-0579-7532 
     used: A:antioxidant
     C: The administration of C. oxyacantha caused increased antioxidant status (GSH and FRAP levels) and decreased lipid peroxidation in treated animals. Major conclusion Accordingly, C. oxyacantha have both therapeutic and protective effect for NAFLD and may be a potential candidate for further assessments in clinical studies.
  REF-1781 [preclinical] 2019 Recent Patents on Food, Nutrition & Agri | Hepatoprotective Effects of Algerian Crataegus oxyacantha Leaves | doi:10.2174/2212798410666180730095456 
     used: A:antioxidant
     C: The obtained results support the traditional use of C. oxyacantha to cure gastrointestinal ailments and highlighted its possible use in the food and pharmaceutical industries as a source of natural antioxidant.
  REF-1782 [preclinical] 2019 Natural Product Research | Polyphenolic content and bioactivities of Crataegus oxyacantha L. (Rosaceae) | doi:10.1080/14786419.2019.1582044 
     used: A:antioxidant
     C: These compounds were identified by 1D and 2D NMR combined analysis as well as by MS and UV.The antimicrobial activity of these extracts has also been tested, showing strong antibacterial activity-solvent dependent-against Gram positive bacteria. Additionally, bactericidal power was demonstrated in fruit extracts.
  REF-1783 [preclinical] 2017 Frontiers in Pharmacology | Neurologically Potent Molecules from Crataegus oxyacantha; Isolation, Anticholinesterase Inhibition, and Molecular Docking | doi:10.3389/fphar.2017.00327 
     used: A:antioxidant
     C: Mechanism of the inhibition of both the enzymes were further studied by docking procedures using Genetic Optimization for Ligand Docking suit v5.4.1. Furthermore, computational blood brain barrier prediction of the isolated compounds suggest that these are BBB+.
  REF-1784 [preclinical] 2017 International Journal of Molecular Scien | Extracts of Crataegus oxyacantha and Rosmarinus officinalis Attenuate Ischemic Myocardial Damage by Decreasing Oxidative Stress and Regulating the Pro | doi:10.3390/ijms18112412 
     used: A:anti-inflammatory, A:antioxidant
     C: Polyphenol treatment restored the left intraventricular pressure and cardiac mechanical work. We conclude that Ro and Co treatment attenuate morphological and functional ischemic-related changes by both an oxidant load reduction and improvement of the balance between vasoconstrictors and vasodilators.
  REF-1785 [preclinical] 2014 Anatolian Journal of Cardiology | Protective effects of Hawthorn (Crataegus oxyacantha) extract against digoxin-induced arrhythmias in rats | doi:10.5152/akd.2014.5869 
     used: A:antispasmodic
     C: Crataegus oxyacantha alcoholic extract produced an antiarrhythmic effect that was induced by digoxin in Wistar rats. However, in the clinical use of this extract, the hypotensive effect should be considered. Also, the alcoholic extract of Crataegus oxyacantha may be an alternative treatment medication for arrhythmias induced by digoxin toxicity in humans.
     !NULL: On the other hand, the time to beginning of QRS prolongation did not differ between the two groups (p=0.
  REF-1786 [preclinical] 2001 Arzneimittel-Forschung | Effect of long-term application of Crataegus oxyacantha on ischemia and reperfusion induced arrhythmias in rats | doi:10.1055/s-0031-1299998 
     used: A:antispasmodic
     C: Also the number and duration of ischemia and reperfusion induced arrhythmias tended to occur longer and more frequently in the Crataegus collectives, whilst coronary flow remained unchanged. The phenomenon that Crataegus rather aggravates than prevents arrhythmias may be reduced to a Crataegus induced increase in intracellular Ca(2+)-concentration proven true for the positive inotropic effects of Crataegus.
  REF-1787 [narrative-review] 2022 Current Pharmaceutical Biotechnology | Anti-anxiety Properties of Selected Medicinal Plants | doi:10.2174/1389201022666210122125131 
     used: A:sedative, M:insomnia
     C: More studies are needed for the exploration of the antianxiety of medicinal plants. In drugs derived from natural sources have explored many components that are playing an essential role in curing anxiety disorders and associated complications.
  REF-2442 [meta-analysis] 2008 Cochrane Database of Systematic Reviews | Hawthorn extract for treating chronic heart failure | doi:10.1002/14651858.CD005312.pub2 
     used: A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:sedative, D:cardiovascular-support
     C: Reported adverse events were infrequent, mild, and transient; they included nausea, dizziness, and cardiac and gastrointestinal complaints. Authors' conclusions These results suggest that there is a significant benefit in symptom control and physiologic outcomes from hawthorn extract as an adjunctive treatment for chronic heart failure.

## crataegus-monogyna - Crataegus monogyna - Hawthorn, common hawthorn, may tree
actions: anti-inflammatory=['REF-0082', 'REF-2442', 'REF-1709']; anticancer=['REF-0785']; antioxidant=['REF-0082', 'REF-2442', 'REF-1709', 'REF-1710', 'REF-1711', 'REF-1714', 'REF-1715', 'REF-1716', 'REF-1717']; sedative=['REF-0082', 'REF-2442']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0082', 'REF-2442'] M=['REF-1709<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-0785'] N=[] X=[] M=[]
- **cardiovascular-support** [verified,ev7] note=""
    D=['REF-0082', 'REF-2442'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0082', 'REF-2442'] M=['REF-1709<anti-inflammatory']
- **insomnia** [needs-review,ev1] !INF note="inferred from sedative action"
    D=['REF-0082'] N=[] X=['REF-2442'] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0082', 'REF-2442'] M=['REF-1709<anti-inflammatory']
  REF-0082 [traditional] 2016  | European Union herbal monograph on Crataegus spp., folium cum flore | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:sedative, D:cardiovascular-support, D:insomnia
     (no abstract)
  REF-0785 [preclinical] 2024 Pharmaceuticals (Basel) | Phenolic Composition of Crataegus monogyna Jacq. Extract and Its Anti-Inflammatory, Hepatoprotective, and Antileukemia Effects | doi:10.3390/ph17060786 
     used: A:anticancer, D:cancer
     C: Procyanidin (-7.27 kcal/mol), quercetin (-8.102 kcal/mol), and catechin (-9.037 kcal/mol) were identified as the most active molecules against lipoxygenase, cytochrome P450, and tyrosine kinase, respectively. These findings highlight the untapped potential of C. monogyna for further exploration in treating liver damage, inflammation, and leukemia.
  REF-1709 [narrative-review] 2015 Nutrients | Polyphenolic Composition of Crataegus monogyna Jacq.: From Chemistry to Medical Applications | doi:10.3390/nu7095361 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: In addition, scientific evidence suggests that the toxicity of hawthorn is negligible. Therefore, the aim of this paper is to provide a critical review of the available scientific literature about pharmacological activities as well as botanical aspects, phytochemistry and clinical impacts of C. monogyna.
  REF-1710 [preclinical] 2021 Natural Product Research | Chemical composition, antioxidant and antibacterial activity of Crataegus monogyna leaves' extracts | doi:10.1080/14786419.2021.1958215 
     used: A:antioxidant
     C: The ethanol extract represented the richest extract in polyphenol with 473.4 mg GAE g -1 and flavonoids 80.9 mg CE g -1 and showed considerable antioxidant potential IC 50 =22.50 µg/ml. The antibacterial susceptibility test against Staphylococcus aureus 0.512 mg/mL.
  REF-1711 [preclinical] 2012 Acta Medica Iranica | Crataegus monogyna aqueous extract ameliorates cyclophosphamide-induced toxicity in rat testis: stereological evidences | NO-ID 
     used: A:antioxidant
     C: Notably, Crataegus coadministration caused a partial recovery in above-mentined parameters. These findings indicate that Crataegus monogyna may be partially protective against CP-induced testicular toxicity.
  REF-1714 [narrative-review] 2012 Phytochemistry | A review of the chemistry of the genus Crataegus | doi:10.1016/j.phytochem.2012.04.006 
     used: A:antioxidant
     C: The main flavonoids found in Crataegus spp. are hyperoside, vitexin, and additional glycosylated derivatives of these compounds. Reviewed herein are the botany, ethnobotany, and traditional use of hawthorn while focusing on the phytochemicals that have been reported in Crataegus species, and the variation in the described chemistry between individual species.
  REF-1715 [preclinical] 2013 Journal of Photochemistry and Photobiolo | Assessment of extracts of Helichrysum arenarium, Crataegus monogyna, Sambucus nigra in photoprotective UVA and UVB; photostability in cosmetic emulsio | doi:10.1016/j.jphotobiol.2013.07.029 
     used: A:antioxidant
     C: The results obtained show that the formulations containing polyphenols fulfill the official requirements for sunscreen products due to their broad spectrum of UV protection combined with their high photostability and remarkable antioxidant properties. Therefore H. arenarium, S. nigra, C. monogyna extracts represent useful additives for cosmetic formulation.
  REF-1716 [preclinical] 2013 Pharmaceutical Development and Technolog | Formulation of microspheres containing Crataegus monogyna Jacq. extract with free radical scavenging activity | doi:10.3109/10837450.2012.752387 
     used: A:antioxidant
     C: Antioxidant activity was evaluated before and after gastrointestinal transit in vitro simulation. Results indicate that the microparticulate systems maintained the antioxidant activity of hawthorn also after gastrointestinal transit in vitro simulation, exhibiting properties suitable for oral administration.
  REF-1717 [narrative-review] 2017 Journal of Physiology and Pharmacology | Crataegus special extract WS 1442: up-to-date review of experimental and clinical experiences | NO-ID 
     used: A:antioxidant
     C: Actions of WS 1442 special extract were investigated in in vitro as well as in vivo studies including large clinical trials. In this review authors present current state of knowledge about possible beneficial effects of WS 1442 special extract on cardiovascular system.
  REF-2442 [meta-analysis] 2008 Cochrane Database of Systematic Reviews | Hawthorn extract for treating chronic heart failure | doi:10.1002/14651858.CD005312.pub2 
     used: A:anti-inflammatory, A:antioxidant, A:sedative, D:cardiovascular-support
     C: Reported adverse events were infrequent, mild, and transient; they included nausea, dizziness, and cardiac and gastrointestinal complaints. Authors' conclusions These results suggest that there is a significant benefit in symptom control and physiologic outcomes from hawthorn extract as an adjunctive treatment for chronic heart failure.

## crocus-sativus - Crocus sativus - Saffron, true saffron, autumn crocus
actions: anti-inflammatory=['REF-0005', 'REF-0115', 'REF-0172', 'REF-2004', 'REF-2006']; anticancer=['REF-0005', 'REF-0115', 'REF-0172', 'REF-2007', 'REF-2008']; antidiabetic=['REF-0005', 'REF-0115', 'REF-0172']; antioxidant=['REF-0005', 'REF-0115', 'REF-0172', 'REF-2005', 'REF-2006']; neuroprotective=['REF-0005', 'REF-0115', 'REF-0172', 'REF-2005', 'REF-2009']; sedative=['REF-0005', 'REF-0115', 'REF-0172', 'REF-0789', 'REF-2001', 'REF-2002', 'REF-2003', 'REF-2010']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0005', 'REF-0172', 'REF-0115'] M=['REF-2004<anti-inflammatory', 'REF-2006<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2007', 'REF-2008'] N=[] X=['REF-0005', 'REF-0172'] M=['REF-0115<anticancer']
- **cognitive-function** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-0005', 'REF-0172', 'REF-0115'] M=['REF-2005<neuroprotective', 'REF-2009<neuroprotective']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0115'] N=[] X=['REF-0005', 'REF-0172'] M=['REF-2004<anti-inflammatory', 'REF-2006<anti-inflammatory']
- **insomnia** [needs-review,ev2] !INF note="inferred from sedative action"
    D=['REF-0115'] N=[] X=['REF-0005', 'REF-0172', 'REF-0789', 'REF-2001', 'REF-2002', 'REF-2003', 'REF-2010'] M=[]
- **memory** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-0005', 'REF-0172', 'REF-0115'] M=['REF-2005<neuroprotective', 'REF-2009<neuroprotective']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0005', 'REF-0172', 'REF-0115'] M=['REF-2004<anti-inflammatory', 'REF-2006<anti-inflammatory']
- **depression** [verified,ev10] note="RCTs and a meta-analysis report that saffron (stigma, and petal in one trial) improves symptoms of mild-to-moderate depression compared with placebo, and performed similarly to imipramine in a pilot trial. Trials are small and mostly from Iran."
    D=['REF-0005', 'REF-0172', 'REF-0789', 'REF-2001', 'REF-2002'] N=[] X=[] M=[]
  REF-0005 [rct] 2004 BMC Complementary and Alternative Medici | Comparison of Crocus sativus L. and imipramine in the treatment of mild to moderate depression: a pilot double-blind randomized trial [ISRCTN45683816] | doi:10.1186/1472-6882-4-12 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antioxidant, A:neuroprotective, A:sedative, D:depression
     C: To the best of our knowledge this is the first clinical trial that supports this indication for saffron. A large-scale trial with placebo control is warranted.
     !NULL: Many medicinal plants textbooks refer to this indication whereas there is no evidence-based document.
  REF-0115 [narrative-review] 2013 Phytotherapy Research | Avicenna's (Ibn Sina) the Canon of Medicine and saffron (Crocus sativus): a review | doi:10.1002/ptr.4784 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antioxidant, A:neuroprotective, A:sedative, D:inflammation, D:insomnia, M:cancer
     C: The pharmacological data on saffron and its constituents, including crocin, crocetin and safranal, are similar to those found in Avicenna's monograph. This review indicates that the evaluation of plants based on ethnobotanical information and ancient books may be a valuable approach to finding new biological activities and compounds.
  REF-0172 [rct] 2006 Phytomedicine | Crocus sativus L. (petal) in the treatment of mild-to-moderate depression: a double-blind, randomized and placebo-controlled trial | doi:10.1016/j.phymed.2006.08.006 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antioxidant, A:neuroprotective, A:sedative, D:depression
     C: The results of this study indicate the efficacy of petal of C. sativus in the treatment of mild-to-moderate depression. A large-scale trial is justified.
     !NULL: There were no significant differences in the two groups in terms of observed side effects.
  REF-0789 [systematic-review] 2014 Human Psychopharmacology | Saffron (Crocus sativus) for depression: a systematic review of clinical studies and examination of underlying antidepressant mechanisms of action | doi:10.1002/hup.2434 
     used: A:sedative, D:depression
     C: Research conducted so far provides initial support for the use of saffron for the treatment of mild-to-moderate depression. Further research is required to expand our understanding of the role and actions of saffron in major depression.
  REF-2001 [meta-analysis] 2013 Journal of Integrative Medicine | Saffron (Crocus sativus L.) and major depressive disorder: a meta-analysis of randomized clinical trials | doi:10.3736/jintegrmed2013056 
     used: A:sedative, D:depression
     C: Findings from clinical trials conducted to date indicate that saffron supplementation can improve symptoms of depression in adults with MDD. Larger clinical trials, conducted by research teams outside of Iran, with long-term follow-ups are needed before firm conclusions can be made regarding saffron's efficacy and safety for treating depressive symptoms.
  REF-2002 [rct] 2017 Complementary Therapies in Medicine | affron a novel saffron extract (Crocus sativus L.) improves mood in healthy adults over 4 weeks in a double-blind, parallel, randomized, placebo-contr | doi:10.1016/j.ctim.2017.06.001 
     used: A:sedative, D:depression
     C: affron ® increased mood, reduced anxiety and managed stress without side effects, offering a natural alternative to standard treatments.
  REF-2003 [rct] 2019 Journal of Child and Adolescent Psychoph | Crocus sativus L. Versus Methylphenidate in Treatment of Children with Attention-Deficit/Hyperactivity Disorder: A Randomized, Double-Blind Pilot Stud | doi:10.1089/cap.2018.0146 
     used: A:sedative
     C: Short-term therapy with saffron capsule showed the same efficacy compared with methylphenidate. Nevertheless, larger controlled studies with longer treatment periods are necessary for future studies.
     !NULL: General linear model repeated measures showed no significant difference between the two groups on Parent and Teacher Rating Scale scores (F = 0.
     !NULL: Changes in Teacher and Parent ADHD Rating Scale scores from baseline to the study end were not significantly different between the saffron group and the MPH group (p = 0.
  REF-2004 [narrative-review] 2014 Drug Research | Clinical Applications of Saffron (Crocus sativus) and its Constituents: A Review | doi:10.1055/s-0034-1375681 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: In another clinical trial, it was proved that in addition to the weight loss treatment, saffron could reduce snacking frequency. Clinical trials conducted on women with premenstrual syndrome showed that saffron could reduce suffering symptoms more than the placebo and similar to standard treatments.Furthermore, additional clinical trials on effects of saffron on erection dysfunction, allergies, cardiovascular and imm
  REF-2005 [narrative-review] 2017 Journal of Agricultural and Food Chemist | A Perspective on Crocus sativus L. (Saffron) Constituent Crocin: A Potent Water-Soluble Antioxidant and Potential Therapy for Alzheimer's Disease | doi:10.1021/acs.jafc.6b04398 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: A search of the studies on saffron and crocin that have been published in recent years for their impact on AD as well as crocin's effects on Aβ and tau protein has been conducted. This review demonstrates that crocin exhibits multifunctional protective activities in the brain and could be a promising agent applied as a supplement or drug for prevention or treatment of AD.
  REF-2006 [narrative-review] 2016 Phytotherapy Research | Antiinflammatory, Antioxidant, and Immunomodulatory Effects of Crocus sativus L. and its Main Constituents | doi:10.1002/ptr.5622 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: Present review found that the C. sativus and its main constituents such as safranal, crocins, and crocetin could be effective against various diseases because of their antioxidant, anti-inflammation, and immunomodulatory effects. Copyright © 2016 John Wiley & Sons, Ltd.
  REF-2007 [narrative-review] 2015 Journal of Traditional and Complementary | Crocus sativus L. (saffron) for cancer chemoprevention: A mini review | doi:10.1016/j.jtcme.2014.10.009 
     used: A:anticancer, D:cancer
     C: Studies in animal models and with cultured human malignant cell lines have demonstrated antitumor and cancer preventive activities of saffron and its main ingredients. This review provides a brief insight into the anticancer properties of saffron and its components.
  REF-2008 [narrative-review] 2018 Phytomedicine | Crocus sativus a natural food coloring and flavoring has potent anti-tumor properties | doi:10.1016/j.phymed.2018.03.041 
     used: A:anticancer, D:cancer
     C: Saffron possesses potent anti-tumor properties and represents an efficacious and safe treatment.
  REF-2009 [narrative-review] 2022 Nutrients | Saffron (Crocus sativus L.): A Source of Nutrients for Health and for the Treatment of Neuropsychiatric and Age-Related Diseases | doi:10.3390/nu14030597 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: The goal of this review is to present the beneficial effects of saffron and its main constituent molecules on neuropsychiatric diseases (depression, anxiety and schizophrenia) as well as on the most frequent age-related diseases (cardiovascular, ocular and neurodegenerative diseases, as well as sarcopenia). Overall, the phytochemical profile of saffron confers many beneficial virtues on human health and, in particula
  REF-2010 [narrative-review] 2021 Molecules | Crocus sativus L. Extracts and Its Constituents Crocins and Safranal; Potential Candidates for Schizophrenia Treatment? | doi:10.3390/molecules26051237 
     used: A:sedative
     C: Up to our days, few preclinical studies have been conducted to this end. In spite of it, results are encouraging and strongly corroborate that additional research is mandatory aiming to definitively establish a role for saffron and its bioactive components for the treatment of schizophrenia.

## cuminum-cyminum - Cuminum cyminum - Cumin, Roman cumin, jeera
actions: anti-inflammatory=['REF-0008', 'REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0654', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307']; antimicrobial=['REF-0008', 'REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0654', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0657']; antioxidant=['REF-0008', 'REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0654', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0657']; antispasmodic=['REF-0008', 'REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0654', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0656']; digestive=['REF-0008', 'REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0654', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0656']
- **bloating** [needs-review,ev2] !INF note="inferred from digestive action"
    D=['REF-0008'] N=[] X=['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0654', 'REF-0656'] M=[]
- **indigestion** [needs-review,ev2] !INF note="inferred from digestive action"
    D=['REF-0008'] N=[] X=['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0654', 'REF-0656'] M=[]
- **infection** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0008'] N=[] X=['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0654', 'REF-0657'] M=[]
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0008'] N=[] X=['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0654'] M=[]
- **metabolic-support** [verified,ev8] note=""
    D=['REF-0008', 'REF-0158', 'REF-0653'] N=['REF-0654', 'REF-0655'] X=[] M=[]
- **muscle-spasm** [needs-review,ev2] !INF note="inferred from antispasmodic action"
    D=['REF-0008'] N=[] X=['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0158', 'REF-0171', 'REF-0175', 'REF-0267', 'REF-0286', 'REF-0307', 'REF-0654', 'REF-0656'] M=[]
  REF-0008 [narrative-review] 2020  | Cumin (Cuminum cyminum L.): A review of its ethnopharmacology, phytochemistry and biological activities | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive, D:bloating, D:indigestion, D:infection, D:inflammation, D:metabolic-support, D:muscle-spasm
     (no abstract)
  REF-0026 [clinical] 2025  | Spices, herbs and allergic reactions in children: myth or reality? | doi:10.3389/falgy.2025.1698559/full 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     C: Management relies on strict allergen avoidance and emergency preparedness. Improved clinical awareness, diagnostic tools, and clearer labeling-especially regarding hidden allergens-are crucial for effective care.
  REF-0066 [traditional] 2015  | Official Journal of the European Union C 76/2015 (Latvian text; includes “Romiešu ķimenes (cumin) | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0067 [traditional] 2020  | Official Journal of the European Union C 108/2020 (Latvian text; includes “kumins (romiešu ķimenes) | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0116 [traditional] 2021  | Latviešu—angļu vārdnīca: ķimenes (includes “Romiešu ķimenes = cumin | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0147 [traditional] 2015  | Cumin: The Ancient Spice That | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0156 [traditional] 2025  | Allergic reactions to spices: a review of sensitivities to pepper, cumin, oregano, anise, mustard and other spices | NO-ID !TAG review-title/traditional
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0158 [systematic-review] 2025  | Potential benefits of Cuminum cyminum L | doi:10.3389/fnut.2025.1618108/full 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive, D:metabolic-support
     C: This meta-analysis suggests that cumin supplementation may have beneficial effects on several components of MetS, including FBS, lipid profile (TG and HDL-C), and WC, in adults with metabolic disorders. However, further high-quality, large-scale trials are needed to strengthen the evidence and confirm these findings.
     !NULL: However, previous studies have reported inconclusive and sometimes conflicting results.
  REF-0171 [preclinical] 2015  | Cuminaldehyde as the Major Component of Cuminum cyminum… | doi:10.1111/1750-3841.13016 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     C: Taken together, these results show for the first time that the small abundant natural compound, cuminaldehyde, can modulate α-SN fibrillation. Hence, suggesting that such natural active aldehyde could have potential therapeutic applications.
  REF-0175 [traditional] 2014  | Cumin, Camels, and Caravans: A Spice Odyssey | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0267 [traditional] n.d.  | Kumīns, ķimenes un citi līdzinieki! | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0286 [systematic-review] 2022  | The effects of cumin supplementation on lipid parameters: a systematic review and meta-analysis of RCTs | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0307 [traditional] 2018  | 1911 Encyclopædia Britannica: Cumin | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive
     (no abstract)
  REF-0653 [systematic-review] 2021 Journal of Ethnopharmacology | The effects of Cuminum cyminum on glycemic parameters: A systematic review and meta-analysis of controlled clinical trials | doi:10.1016/j.jep.2021.114510 
     used: D:metabolic-support
     C: CC had an improving effect on FBS, HbA1C, HOMA-B, and QUICKI. The effect of CC on amending HOMA-IR was significant after sensitivity analysis. However, the insulin level was not changed significantly.
     !NULL: However, no significant effect of CC was observed on insulin (SMD = -0.
  REF-0654 [systematic-review] 2021 Phytotherapy Research | The effect of cumin (Cuminum cyminum L.) supplementation on glycemic indices: A systematic review and meta-analysis of randomized controlled trials | doi:10.1002/ptr.7075 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:digestive, N:metabolic-support
     C: These results do not support the use of cumin supplementation for improving glycemic markers in adults. However, further high-quality trials are still needed to confirm these results.
     !NULL: The results of the meta-analysis suggest that cumin supplementation did not significantly alter serum FBS (WMD: -17.
  REF-0655 [rct] 2019 Phytotherapy Research | Effects of cumin (Cuminum cyminum L.) essential oil supplementation on metabolic syndrome components: A randomized, triple-blind, placebo-controlled c | doi:10.1002/ptr.6500 
     used: N:metabolic-support
     C: However, DBP was significantly lower in CuEO compared with the placebo group at the end of study (81.41 ± 5.88 vs. 84.09 ± 5.54 mmHg, MD with 95% CI: -3.98 [-7.60, -0.35] mmHg, p < .05). The results indicated that CuEO does not have any effect on MetS components, except for DBP in patients with MetS.
     !NULL: At the end of study, except for diastolic blood pressure (DBP), the other assessed variables were not significantly different between two groups.
     !NULL: In intra group analysis, placebo and CuEO groups both had nonsignificant decrements in DBP (mean difference [MD] with 95% CI: -3.
  REF-0656 [rct] 2024 BMC Complementary Medicine and Therapies | The effect of Cuminum cyminum on the return of bowel motility after abdominal surgery: a triple-blind randomized clinical trial | doi:10.1186/s12906-024-04530-1 
     used: A:antispasmodic, A:digestive
     C: According to the results, the consumption of Cuminum cyminum after abdominal surgery helps to reduce the time of gas passing, defecation, and the return of bowel motility. However, additional studies need to address the effectiveness of Cuminum cyminum by changing the time and duration of its use.
  REF-0657 [preclinical] 2018 Pakistan Journal of Biological Sciences | Evaluation of Protective Impact of Algerian Cuminum cyminum L. and Coriandrum sativum L. Essential Oils on Aspergillus flavus Growth and Aflatoxin B1  | doi:10.3923/pjbs.2018.67.77 
     used: A:antimicrobial, A:antioxidant
     C: The C. cyminum L. and C. sativum L EOs could be good alternative to protect foods.

## curcuma-longa - Curcuma longa - Turmeric, Tumeric, common turmeric
actions: anti-inflammatory=['REF-0002', 'REF-0273', 'REF-0308', 'REF-0791', 'REF-2164', 'REF-0792', 'REF-2165', 'REF-2167', 'REF-2168', 'REF-2169', 'REF-2170']; anticancer=['REF-0002', 'REF-0273', 'REF-0308']; antidiabetic=['REF-0002', 'REF-0273', 'REF-0308']; antimicrobial=['REF-0002', 'REF-0273', 'REF-0308', 'REF-2172']; antioxidant=['REF-0002', 'REF-0273', 'REF-0308', 'REF-2169', 'REF-2171']; gastroprotective=['REF-0002', 'REF-0273', 'REF-0308']
- **acid-reflux** [needs-review,ev1] !INF note="inferred from gastroprotective action"
    D=['REF-0308'] N=[] X=['REF-0002', 'REF-0273'] M=[]
- **arthritis** [verified,ev8] note=""
    D=['REF-0308', 'REF-0791', 'REF-0792'] N=[] X=['REF-0273', 'REF-2165', 'REF-0002'] M=['REF-2164<anti-inflammatory', 'REF-2167<anti-inflammatory', 'REF-2168<anti-inflammatory', 'REF-2169<anti-inflammatory', 'REF-2170<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-0002'] N=[] X=['REF-0273'] M=['REF-0308<anticancer']
- **cardiovascular-support** [verified,ev2] note=""
    D=['REF-0002'] N=[] X=[] M=[]
- **indigestion** [needs-review,ev1] !INF note="inferred from gastroprotective action"
    D=['REF-0308'] N=[] X=['REF-0002', 'REF-0273'] M=[]
- **infection** [needs-review,ev1] !INF note="inferred from antimicrobial action"
    D=['REF-0308'] N=[] X=['REF-0273', 'REF-0002'] M=['REF-2172<antimicrobial']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0002', 'REF-0308'] N=[] X=['REF-0273'] M=['REF-0791<anti-inflammatory', 'REF-2164<anti-inflammatory', 'REF-0792<anti-inflammatory', 'REF-2165<anti-inflammatory', 'REF-2167<anti-inflammatory', 'REF-2168<anti-inflammatory', 'REF-2169<anti-inflammatory', 'REF-2170<anti-inflammatory']
- **metabolic-support** [needs-review,ev2] !INF note="inferred from antidiabetic action"
    D=['REF-0002'] N=[] X=['REF-0273', 'REF-0308'] M=[]
- **skin-irritation** [needs-review,ev7] !INF note="inferred from anti-inflammatory action"
    D=['REF-0308', 'REF-2165'] N=[] X=['REF-0273', 'REF-0791', 'REF-0792', 'REF-0002'] M=['REF-2164<anti-inflammatory', 'REF-2167<anti-inflammatory', 'REF-2168<anti-inflammatory', 'REF-2169<anti-inflammatory', 'REF-2170<anti-inflammatory']
- **wounds** [needs-review,ev1] !INF note="inferred from antimicrobial action"
    D=['REF-0308'] N=[] X=['REF-0273', 'REF-0002'] M=['REF-2172<antimicrobial']
  REF-0002 [narrative-review] 2009  | Potential therapeutic effects of curcumin, the anti-inflammatory agent, against neurodegenerative, cardiovascular, pulmonary, metabolic, autoimmune an | doi:10.1016/j.biocel.2008.06.010 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:gastroprotective, D:cancer, D:cardiovascular-support, D:inflammation, D:metabolic-support
     C: In the current review, we provide evidence for the potential role of curcumin in the prevention and treatment of various proinflammatory chronic diseases. These features, combined with the pharmacological safety and negligible cost, render curcumin an attractive agent to explore further.
  REF-0273 [clinical] 1998  | Influence of piperine on the pharmacokinetics of curcumin in animals and human volunteers | doi:10.1055/s-2006-957450 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:gastroprotective
     C: Concomitant administration of piperine 20 mg produced much higher concentrations from 0.25 to 1 h post drug (P < 0.01 at 0.25 and 0.5 h; P < 0.001 at 1 h), the increase in bioavailability was 2000%. The study shows that in the dosages used, piperine enhances the serum concentration, extent of absorption and bioavailability of curcumin in both rats and humans with no adverse effects.
     !NULL: On the other hand in humans after a dose of 2 g curcumin alone, serum levels were either undetectable or very low.
  REF-0308 [traditional] 1999  | WHO Monographs on Selected Medicinal Plants, Volume 1 | NO-ID 
     used: A:anti-inflammatory, A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:gastroprotective, D:acid-reflux, D:arthritis, D:indigestion, D:infection, D:inflammation, D:skin-irritation, D:wounds, M:cancer
     (no abstract)
  REF-0791 [systematic-review] 2022 Frontiers in Immunology | Efficacy and Safety of Curcumin and Curcuma longa Extract in the Treatment of Arthritis: A Systematic Review and Meta-Analysis of Randomized Controlle | doi:10.3389/fimmu.2022.891822 
     used: A:anti-inflammatory, D:arthritis, M:inflammation
     C: Curcumin and Curcuma longa Extract may improve symptoms and inflammation levels in people with arthritis. However, due to the low quality and small quantity of RCTs, the conclusions need to be interpreted carefully.
  REF-0792 [systematic-review] 2021 Bioscience Reports | The efficacy and safety of Curcuma longa extract and curcumin supplements on osteoarthritis: a systematic review and meta-analysis | doi:10.1042/BSR20210817 
     used: A:anti-inflammatory, D:arthritis, M:inflammation
     C: Curcuma longa extract and curcumin may be a safer and effective supplement for OA patients. It is recommended to use Curcuma longa extract and curcumin supplement for OA patients for more than 12 weeks.
     !NULL: In terms of adverse events, the addition of Curcuma longa extract and curcumin to NSAIDs did not increase adverse events.
  REF-2164 [narrative-review] 2017 Critical Reviews in Food Science and Nut | Curcumin, an active component of turmeric (Curcuma longa), and its effects on health | doi:10.1080/10408398.2015.1077195 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Furthermore, it is aimed to increase the biological activity and physiological effects of the curcumin on the body by synthesizing curcumin analogues. This article reviews the history, chemical and physical features, analogues, metabolites, mechanisms of its physiological activities, and effects on health of curcumin.
  REF-2165 [systematic-review] 2016 Phytotherapy Research | Effects of turmeric (Curcuma longa) on skin health: a systematic review of the clinical evidence | doi:10.1002/ptr.5640 
     used: A:anti-inflammatory, D:skin-irritation, M:inflammation
     C: However, currently published studies are limited and further studies will be essential to better evaluate efficacy and the mechanisms involved. Copyright © 2016 John Wiley & Sons, Ltd.
  REF-2167 [meta-analysis] 2022 Frontiers in Immunology | Curcumin and Curcuma longa extract in the treatment of 10 types of autoimmune diseases: a systematic review and meta-analysis of 31 randomized control | doi:10.3389/fimmu.2022.896476 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Curcumin and Curcuma longa Extract had good clinical efficacy in the treatment of Psoriasis, UC and RA, so Curcumin and Curcuma longa Extract could be used in the treatment of the above diseases in the future. The results of Meta-analysis showed that Curcumin and Curcuma longa Extract did not show efficacy in the treatment of oral lichen planus, while Takayasu arteritis, SLE, MS, AS, BD and CD did not report sufficie
     !NULL: The results of Meta-analysis showed that Curcumin and Curcuma longa Extract did not show efficacy in the treatment of oral lichen planus, while Takayasu arteritis, SLE, MS, AS, BD and CD did not report sufficient clinical data for meta-analysis.
  REF-2168 [narrative-review] 2021 Phytotherapy Research | A review of therapeutic potentials of turmeric (Curcuma longa) and its active constituent, curcumin, on inflammatory disorders, pain, and their relate | doi:10.1002/ptr.7224 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: However, because of inadequate clinical trials, further high-quality studies are needed to firmly establish the clinical efficacy of the plant. Consistent with the human tendency to the usage of phytocompounds rather than synthetic drugs, particular consideration must be dedicated to bond the worth of turmeric and curcumin from basic sciences to clinical applications.
  REF-2169 [narrative-review] 2021 BioFactors | Experimental and clinical reports on anti-inflammatory, antioxidant, and immunomodulatory effects of Curcuma longa and curcumin, an updated and compre | doi:10.1002/biof.1716 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: Treatment with C. longa and CUR also improved immunoglobulin E (Ig)E, pro-inflammatory cytokine interleukin 4 (IL)-4, transforming growth factor-beta, IL-17, interferon-gamma levels, and type 1/type 2 helper cells (Th1)/(Th2) ratio in conditions with disturbance in the immune system. Therefore C. longa and CUR showed anti-inflammatory, antioxidant, and immunomodulatory effects, indicating a potential therapeutic effe
  REF-2170 [narrative-review] 2009 Alternative Medicine Review | Anti-inflammatory properties of curcumin, a major constituent of Curcuma longa: a review of preclinical and clinical research | NO-ID 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Because of curcumin's rapid plasma clearance and conjugation, its therapeutic usefulness has been somewhat limited, leading researchers to investigate the benefits of complexing curcumin with other substances to increase systemic bioavailability. Numerous in-progress clinical trials should provide an even deeper understanding of the mechanisms and therapeutic potential of curcumin.
  REF-2171 [narrative-review] 2018 Biomedicine & Pharmacotherapy | Antidotal or protective effects of Curcuma longa (turmeric) and its active ingredient, curcumin, against natural and chemical toxicities: a review | doi:10.1016/j.biopha.2018.01.072 
     used: A:antioxidant
     C: The recent studies have shown that C. longa and curcumin, its important active ingredient, have protective effects against toxic agents. In this review article, we collected in vitro and animal studies which are related to protective effects of turmeric and its active ingredient against natural and chemical toxic agents.
  REF-2172 [narrative-review] 2001 Memorias do Instituto Oswaldo Cruz | Biological activities of Curcuma longa L. | doi:10.1590/s0074-02762001000500026 
     used: A:antimicrobial, M:infection, M:wounds
     C: In vivo, there are experiments showing the anti-parasitic, anti-inflammatory potency of curcumin and extracts of C. longa L. by parenteral and oral application in animal models. In this present work we make an overview of the pharmacological activities of C. longa L., showing its importance.

## cynara-scolymus - Cynara scolymus - Artichoke, Globe artichoke, Garden artichoke
actions: choleretic=['REF-0461', 'REF-0462']; digestive=['REF-0461', 'REF-0462']; hepatoprotective=['REF-0461', 'REF-1634', 'REF-1635', 'REF-1639', 'REF-2568']; lipid-lowering=['REF-0461', 'REF-0584', 'REF-0585', 'REF-2566', 'REF-2567', 'REF-2569']
- **bloating** [verified,ev1] note="Digestive aid for dyspeptic complaints - indigestion, bloating and fullness"
    D=['REF-0462'] N=[] X=['REF-0461'] M=[]
- **cardiovascular-support** [needs-review,ev8] !INF note="inferred from lipid-lowering action"
    D=['REF-0461', 'REF-0584', 'REF-0585'] N=[] X=[] M=['REF-2566<lipid-lowering', 'REF-2567<lipid-lowering', 'REF-2569<lipid-lowering']
- **detox** [needs-review,ev1] note="inferred from hepatoprotective action"
    D=[] N=[] X=['REF-0461'] M=['REF-1634<hepatoprotective', 'REF-1635<hepatoprotective', 'REF-1639<hepatoprotective', 'REF-2568<hepatoprotective']
- **high-cholesterol** [needs-review,ev9] !INF note="inferred from lipid-lowering action"
    D=['REF-0461', 'REF-0584', 'REF-0585', 'REF-2566', 'REF-2567', 'REF-2569'] N=[] X=[] M=[]
- **indigestion** [verified,ev1] note="Digestive aid for dyspeptic complaints - indigestion, bloating and fullness"
    D=['REF-0462'] N=[] X=['REF-0461'] M=[]
- **liver-support** [verified,ev7] note="Hepatoprotective / liver support (protects liver cells and may aid their regeneration)"
    D=['REF-0461', 'REF-2568'] N=[] X=[] M=['REF-0462<choleretic', 'REF-1634<hepatoprotective', 'REF-1635<hepatoprotective', 'REF-1639<hepatoprotective']
  REF-0461 [narrative-review] 2015 Plant Foods for Human Nutrition | Pharmacological Studies of Artichoke Leaf Extract and Their Health Benefits | doi:10.1007/s11130-015-0503-8 
     used: A:choleretic, A:digestive, A:hepatoprotective, A:lipid-lowering, D:cardiovascular-support, D:high-cholesterol, D:liver-support
     C: Boiled wild artichoke reduced postprandial glycemic and insulinemic responses in normal subjects but has no effect on metabolic syndrome patients. This article intended to review the wide ranging pharmacological effects of artichoke leaf extract.
     !NULL: Boiled wild artichoke reduced postprandial glycemic and insulinemic responses in normal subjects but has no effect on metabolic syndrome patients.
  REF-0462 [traditional] n.d.  | European Union herbal monograph on Cynara cardunculus L. (syn. Cynara scolymus L.), folium (Cynarae folium) | NO-ID 
     used: A:choleretic, A:digestive, D:bloating, D:indigestion, M:liver-support
     (no abstract)
  REF-0584 [systematic-review] 2013 Cochrane Database of Systematic Reviews | Artichoke leaf extract for treating hypercholesterolaemia | doi:10.1002/14651858.CD003335.pub3 
     used: A:lipid-lowering, D:cardiovascular-support, D:high-cholesterol
     C: There is an indication that ALE has potential in lowering cholesterol levels, but the evidence is, as yet, not convincing. The limited data on safety suggest only mild, transient and infrequent adverse events with the short term use of ALE.
  REF-0585 [rct] 2012 International Journal of Food Sciences a | Beneficial effects of artichoke leaf extract supplementation on increasing HDL-cholesterol in subjects with primary mild hypercholesterolaemia: a doub | doi:10.3109/09637486.2012.700920 
     used: A:lipid-lowering, D:cardiovascular-support, D:high-cholesterol
     C: A significantly decreased difference was also found for the mean change in total cholesterol (p = 0.033), low-density lipoprotein (LDL)-cholesterol (p < 0.001), total cholesterol/HDL ratio (p < 0.001) and LDL/HDL ratio (p < 0.001), when verum and placebo treatment were compared. These results indicate that ALE could play a relevant role in the management of mild hypercholesterolaemia, favouring in particular the incr
  REF-1634 [narrative-review] 2024 Nutrients | Functional and Therapeutic Potential of Cynara scolymus in Health Benefits | doi:10.3390/nu16060872 
     used: A:hepatoprotective, M:detox, M:liver-support
     C: As a result, C. scolymus has the potential to contribute to the treatment of chronic diseases, including intestinal disorders, cardiovascular diseases, and neurodegenerative pathologies. The current review discussed the nutritional profiles, potential benefits, and pharmacological effects of C. scolymus.
  REF-1635 [meta-analysis] 2019 Phytotherapy Research | The antioxidant activity of artichoke (Cynara scolymus): A systematic review and meta-analysis of animal studies | doi:10.1002/ptr.6213 
     used: A:hepatoprotective, M:detox, M:liver-support
     C: Finding of animal studies indicated that artichoke extract supplementation increased superoxide dismutase, catalase, glutathione, and glutathione peroxidase level in liver, as well as, decreased malondialdehyde level in liver and plasma of animals with induced disease significantly compared with comparison group. This meta-analysis provided convincing evidence for antioxidant activity of artichoke in animals.
  REF-1639 [preclinical] 2019 Journal of Basic and Clinical Physiology | Modulatory effects of artichoke (Cynara scolymus L.) leaf extract against oxidative stress and hepatic TNF-alpha gene expression in acute diazinon-ind | doi:10.1515/jbcpp-2018-0180 
     used: A:hepatoprotective, M:detox, M:liver-support
     C: This study confirmed that Art leaf extract has liver protective effects and causes downregulation of oxidative stress in acute DZN-induced liver injury in rats.
  REF-2566 [meta-analysis] 2017 Critical Reviews in Food Science and Nut | Lipid-lowering activity of artichoke extracts: A systematic review and meta-analysis | doi:10.1080/10408398.2017.1332572 
     used: A:lipid-lowering, D:high-cholesterol, M:cardiovascular-support
     C: A significant association between the LDL-lowering effect of artichoke and baseline LDL-C concentrations (slope: -0.170; 95%CI: -0.288, 0.051; p = 0.005) was observed. Thus, supplementation with artichoke extract was associated with a significant reduction in both total and LDL-C, and triglycerides, suggesting that supplementation may be synergistic with lipid-lowering therapy in patients with hyperlipidemia.
     !NULL: No significant alteration in plasma High Density Lipoprotein-Cholesterol (HDL-C) concentrations was observed (WMD: 1.
  REF-2567 [meta-analysis] 2021 Phytotherapy Research | Effects of artichoke leaf extract supplementation or artichoke juice consumption on lipid profile: A systematic review and dose-response meta-analysis | doi:10.1002/ptr.7247 
     used: A:lipid-lowering, D:high-cholesterol, M:cardiovascular-support
     C: Combining the two effect sizes revealed that artichoke juice supplementation significantly reduced TG (WMD: -3.34 mg/dl, 95%CI: -5.51, -1.17, p = .003), TC (WMD: -18.04 mg/dl, 95%CI: -20.30, -15.78, p < .001), LDL-C (WMD: -1.75 mg/dl, 95%CI: -3.02, -0.48, p = .007), and HDL-C levels (WMD: -4.21 mg/dl, 95%CI: -5.49, -2.93, p < .001). In conclusion, we found that artichoke supplementation may favor CVD prevention by ac
     !NULL: No significant effect of artichoke on HDL-C level was detected (WMD: 0.
  REF-2568 [meta-analysis] 2022 Journal of Medicinal Food | Therapeutic Potential of Artichoke in the Treatment of Fatty Liver: A Systematic Review and Meta-Analysis | doi:10.1089/jmf.2022.0025 
     used: A:hepatoprotective, D:liver-support, M:detox
     C: The study was registered on the PROSPERO database with the Registration No. CRD42020182502 ( https://www.crd.york.ac.uk/prospero).
  REF-2569 [narrative-review] 2018 Pharmacological Research | The effect of artichoke on lipid profile: A review of possible mechanisms of action | doi:10.1016/j.phrs.2018.10.007 
     used: A:lipid-lowering, D:high-cholesterol, M:cardiovascular-support
     C: On the other hand, the effects of cooked artichoke hearts can be attributed mainly to its soluble fibres, particularly inulin. Despite the convincing evidence on its health benefits, additional long-term clinical trials are pivotal to fully elucidate the potential effects of ALE administration on positive cardiovascular outcomes.
