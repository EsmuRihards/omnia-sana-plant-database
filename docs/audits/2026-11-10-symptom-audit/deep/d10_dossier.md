# Deep dossier batch 10

## laurus-nobilis - Laurus nobilis - Bay Leaf, Bay Laurel, Sweet Bay
actions: analgesic=[]; anti-inflammatory=[]; anticancer=['REF-1687']; antimicrobial=['REF-1679', 'REF-1686']; antioxidant=['REF-1679', 'REF-1680', 'REF-1681']; digestive=[]; neuroprotective=[]; vulnerary=['REF-1678']
- **bruising** [needs-review,ev1] note="inferred from vulnerary action"
    D=[] N=[] X=[] M=['REF-1678<vulnerary']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1687'] N=[] X=[] M=[]
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=[] M=['REF-1679<antimicrobial', 'REF-1686<antimicrobial']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-1686'] M=['REF-1679<antimicrobial', 'REF-1678<vulnerary']
  REF-1678 [preclinical] 2024 Veterinary Medicine International | Effects of Laurus nobilis Leaf Extract on Healing of Experimentally Induced Wounds in Rabbits | doi:10.1155/2024/2889480 
     used: A:vulnerary, M:bruising, M:wounds
     C: Histopathological results at the end of the study show that the thick epidermal layer covers a mass of granulation with congested blood vessels and the dermis transforms into a denser layer gradually due to the improvements of the cellularity in the C group and also revealed a well-formed skin appearance, widespread of collagen, and fibrosis within the dermis with an appearance near the normal dermis in the group tre
  REF-1679 [preclinical] 2017 Molecules | Laurus nobilis: Composition of Essential Oil and Its Biological Activities | doi:10.3390/molecules22060930 
     used: A:antimicrobial, A:antioxidant, M:infection, M:wounds
     C: Antimicrobial and antifungal activities of EO and 1,8-cineole were determined in vitro. The cytotoxicity of the EO was evaluated against SH-SY5Y cell line, as well as the influence of the EO on the expression of adenylate cyclase 1 (ADCY1), suggesting possible oil effects on the Central Nervous System.
  REF-1680 [preclinical] 2021 Mitochondrion | Laurus nobilis ethanolic extract attenuates hyperglycemia and hyperinsulinemia-induced insulin resistance in HepG2 cell line through the reduction of  | doi:10.1016/j.mito.2021.06.003 
     used: A:antioxidant
     C: Ethanolic plant extract increased insulin sensitivity, since an elevated expression of master transcripts responsible for insulin sensitivity including IRS1, IRS2, INSR was found. Taken together, obtained data suggest that L. nobilis ethanolic extract offers new insights in the development of potential antioxidant, insulin sensitizing as well as hepatoprotective drugs.
  REF-1681 [narrative-review] 2022 Foods | Isolation of Laurus nobilis Leaf Polyphenols: A Review on Current Techniques and Future Perspectives | doi:10.3390/foods11020235 
     used: A:antioxidant
     C: In order to enable efficient industrial utilization of these valuable compounds, it is crucial to establish optimal extraction procedures resulting in the highest yields and quality of the extracts. This paper offers the first systematic review of current literature on the influence of conventional and advanced extraction techniques, including microwave-assisted, ultrasound-assisted, enzyme-assisted, supercritical-CO
  REF-1686 [preclinical] 2002 Chemical & Pharmaceutical Bulletin | Trypanocidal terpenoids from Laurus nobilis L. | doi:10.1248/cpb.50.1514 
     used: A:antimicrobial, M:infection
     C: Activity-guided fractionation of the methanol extract resulted in the isolation of two guaianolides, dehydrocostus lactone (1) and zaluzanin D (2), and a new p-menthane hydroperoxide, (1R,4S)-1-hydroperoxy-p-menth-2-en-8-ol acetate (3). The minimum lethal concentrations of these compounds against epimastigotes of Trypanosoma cruzi were 6.3, 2.5, and 1.4 microM, respectively.
  REF-1687 [preclinical] 2015 Nutrition and Cancer | Laurus nobilis L. Seed Extract Reveals Collateral Sensitivity in Multidrug-Resistant P-Glycoprotein-Expressing Tumor Cells | doi:10.1080/01635581.2015.1019632 
     used: A:anticancer, D:cancer
     C: A microarray-based profile of 20 genes predicted resistance to doxorubicin and 7 other anticancer drugs involved in the multidrug resistance phenotype but not to limonene, eucalyptol and oleic acid. In conclusion, our results show that Laurus nobilis seed extract is suitable to kill multidrug-resistant P-glycoprotein expressing tumor cells.

## lavandula-angustifolia - Lavandula angustifolia - Lavender, English lavender, true lavender
actions: anti-inflammatory=['REF-0043', 'REF-0155', 'REF-0265', 'REF-2205', 'REF-2213']; anticancer=['REF-2214']; antimicrobial=['REF-0043', 'REF-0155', 'REF-0265', 'REF-2207']; antioxidant=['REF-0043', 'REF-0155', 'REF-0265', 'REF-2211']; antispasmodic=['REF-0043', 'REF-0155', 'REF-0265']; emollient=['REF-0043', 'REF-0155', 'REF-0265']; sedative=['REF-0043', 'REF-0155', 'REF-0265', 'REF-2206', 'REF-2208', 'REF-2209', 'REF-2210', 'REF-2212', 'REF-2215']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0265', 'REF-0043', 'REF-0155'] M=['REF-2205<anti-inflammatory', 'REF-2213<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2214'] N=[] X=[] M=[]
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0265', 'REF-0043', 'REF-0155'] M=['REF-2207<antimicrobial']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0265', 'REF-0043', 'REF-0155'] M=['REF-2205<anti-inflammatory', 'REF-2213<anti-inflammatory']
- **insomnia** [needs-review,ev1] note="EU traditional use to aid sleep and relieve mild mental stress and exhaustion"
    D=['REF-3071'] N=['REF-0858'] X=['REF-2208', 'REF-2210', 'REF-2212', 'REF-2215', 'REF-0043', 'REF-0155', 'REF-0265'] M=['REF-2206<sedative', 'REF-2209<sedative']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0265', 'REF-0043', 'REF-0155'] M=['REF-2205<anti-inflammatory', 'REF-2213<anti-inflammatory']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0265', 'REF-0043', 'REF-0155'] M=['REF-2207<antimicrobial']
  REF-0043 [narrative-review] 2002  | Biological activities of lavender essential oil | doi:10.1002/ptr.1103 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:emollient, A:sedative
     C: However, methodological and oil identification problems have severely hampered the evaluation of the therapeutic significance of much of the research on Lavandula spp. These issues need to be resolved before we have a true picture of the biological activities of lavender essential oil.
     !NULL: Although the data are still inconclusive and often controversial, there does seem to be both scientific and clinical data that support the traditional uses of lavender.
  REF-0155 [traditional] 2002  | Lavender: The Genus Lavandula | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:emollient, A:sedative
     (no abstract)
  REF-0265 [preclinical] 2013  | Lavender oil-potent anxiolytic properties via modulating voltage dependent calcium channels | doi:10.1371/journal.pone.0059998 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:antispasmodic, A:emollient, A:sedative
     C: In the hippocampus, one brain region important for anxiety disorders, we show that inhibition by lavender oil is mainly mediated via N-type and P/Q-type VOCCs. Taken together, we provide a pharmacological and molecular rationale for the clinical use of the oral application of lavender oil in patients suffering from anxiety.
  REF-0858 [rct] 2021 Complementary Therapies in Medicine | Lavender essential oil on postmenopausal women with insomnia: Double-blind randomized trial | doi:10.1016/j.ctim.2021.102726 
     used: N:insomnia
     C: Although no significant differences were observed between groups, our data presented a tendency of improvement in WASO. Moreover, AG participants had enhanced overall sleep pattern, quality and sleep efficiency. Weekly follow-up and sleep hygiene instructions were essential for both groups to show improvement in almost all outcomes. Clinical trial registration Brazilian Registry of Clinical Trials, www.ensaiosclinico
     !NULL: Results There were no significant differences between groups after intervention in the primary outcome (P = 0.
     !NULL: Conclusion Although no significant differences were observed between groups, our data presented a tendency of improvement in WASO.
  REF-2205 [narrative-review] 2009 Holistic Nursing Practice | Lavandula angustifolia Miller: English lavender | doi:10.1097/01.HNP.0000343210.56710.fc 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Current research focusing on the inherent synergism of Lavandula angustifolia Miller demonstrates great potential for future applications. Today's investigations may provide the key to eradicating degenerative inflammatory disease, infectious disease, and carcinogenesis.
  REF-2206 [systematic-review] 2004 Journal of Herbal Pharmacotherapy | Lavender (Lavandula angustifolia Miller) | doi:10.1080/j157v04n02_07 
     used: A:sedative, M:insomnia
     C: An evidence-based systematic review including scientific evidence, expert opinion, folkloric precedent, history, pharmacology, kinetics/dynamics, interactions, adverse effects, toxicology, and dosing.
  REF-2207 [preclinical] 2024 Molecules | Phytochemical composition and antimicrobial properties of new Lavandula angustifolia ecotypes | doi:10.3390/molecules29081740 
     used: A:antimicrobial, M:infection, M:wounds
     C: The test results confirmed that leaf and flower extracts, even at low concentrations (0.313-0.63%), significantly inhibit the growth of selected Gram-negative and Gram-positive bacteria and Candida yeasts. Inhibition of mold growth was observed at a dose extract of at least 1 mL/100 mL.
  REF-2208 [preclinical] 2023 BioMed Research International | Antiseizure effects of Lavandula angustifolia L. | doi:10.1155/2023/4121998 
     used: A:sedative
     C: In mice, the hydroalcoholic extracts of P. harmala and L. angustifolia showed antiseizure activity against PTZ-induced seizures. We could not delineate the exact antiseizure mechanisms of these extracts in the current study.
  REF-2209 [systematic-review] 2023 Heliyon | Use of Lavandula angustifolia essential oil as a complementary therapy in adult health care: a scoping review | doi:10.1016/j.heliyon.2023.e15446 
     used: A:sedative, M:insomnia
     C: Most studies demonstrate the efficacy of L. angustifolia Mill. essential oil in relieving pain and decreasing anxiety. Few studies evaluated the anti-psoriatic, anti-toxoplasmotic, and wound healing properties and the protective actions against cerebral ischemia. One study reported on its safety, specifically the allergenic potential of linalool, the main chemical component of L. angustifolia essential oil. However, 
  REF-2210 [preclinical] 2023 Journal of Applied Oral Science | Antinociceptive and anxiolytic-like effects of Lavandula angustifolia essential oil on rat models of orofacial pain | doi:10.1590/1678-7757-2002-0304 
     used: A:sedative
     C: LAV EO inhalation results in antinociceptive and anxiolytic-like effects in orofacial pain models, which encourages further studies on LAV EO indications and effectiveness on orofacial pain conditions.
  REF-2211 [preclinical] 2024 Chemistry & Biodiversity | Lavandula angustifolia herb from Ukraine: comparative chemical profile and in vitro antioxidant activity | doi:10.1002/cbdv.202400640 
     used: A:antioxidant
     C: Cluster analysis showed priority in the selection of marker compounds (vanillic acid, hyperoside, chlorogenic acid, rosmarinic acid) for lavender herb based on their quantitative content in the samples. In the future, lavender herb from Ukraine can be considered as a promising raw material with neuroprotective properties as part of its complex use, as research continues.
  REF-2212 [systematic-review] 2021 Journal of Complementary & Integrative M | Efficacy and tolerability of Lavandula angustifolia in treating patients with the diagnosis of depression: a systematic review of randomized controlle | doi:10.1515/jcim-2020-0498 
     used: A:sedative
     C: Despite obtaining promising results, they are not enough to recommend prescribing lavender to depressed patients. Further high-quality, large-scale studies for rectifying the shortcomings of existing studies are recommended.
  REF-2213 [preclinical] 2018 Evidence-Based Complementary and Alterna | Effect of lavender (Lavandula angustifolia) essential oil on acute inflammatory response | doi:10.1155/2018/1413940 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: In dextran-induced paw edema model, LEO at doses of 75 and 100 mg/kg reduced paw edema and MPO activity. In conclusion, LEO presented anti-inflammatory activity, and the mechanism proposed of LEO seems to be, at least in part, involving the participation of prostanoids, NO, proinflammatory cytokines, and histamine.
  REF-2214 [preclinical] 2022 Molecules | Chemical evaluation, in vitro and in vivo anticancer activity of Lavandula angustifolia grown in Jordan | doi:10.3390/molecules27185910 
     used: A:anticancer, D:cancer
     C: Moreover, undetected tumor was found in 12.5% of the sample size. In conclusion, this study provides novel insight and evidence on the antiproliferative efficacy of L. angustifolia ethanol extract against breast cancer with potent anti-oxidant potential.
  REF-2215 [preclinical] 2018 Molecules | Lavandula angustifolia essential oil and linalool counteract social aversion induced by social defeat | doi:10.3390/molecules23102694 
     used: A:sedative
     C: Our results showed that linalool inhibits pERK and PKA expression in the SH-SY5Y cell, but no effect was detected with the LA essential oil. Therefore, the LA essential oil and linalool may be considered as useful alternative tools to the available traditional treatments for social stress-induced mental illnesses.
     !NULL: Acute administration of LA essential oil blocked stress-induced anxiety, while linalool showed no effects.
     !NULL: Our results showed that linalool inhibits pERK and PKA expression in the SH-SY5Y cell, but no effect was detected with the LA essential oil.
  REF-3071 [traditional] 2012  | Community herbal monograph on Lavandula angustifolia Miller, flos | NO-ID 
     used: D:insomnia
     (no abstract)

## lentinula-edodes - Lentinula edodes - Shiitake (mushroom), Shiitake, Chinese forest mushroom
actions: anticancer=['REF-0293', 'REF-0300', 'REF-0315', 'REF-1165', 'REF-1166', 'REF-1167']; antidiabetic=['REF-0293', 'REF-0300', 'REF-0315']; antimicrobial=['REF-0293', 'REF-0300', 'REF-0315', 'REF-1167']; antioxidant=['REF-0293', 'REF-0300', 'REF-0315']; antiviral=['REF-0293', 'REF-0300', 'REF-0315', 'REF-1167']; immunomodulator=['REF-0293', 'REF-0300', 'REF-0315', 'REF-1163', 'REF-1164', 'REF-1167', 'REF-1170', 'REF-1171']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1166'] N=[] X=['REF-0300', 'REF-0315', 'REF-0293'] M=['REF-1165<anticancer', 'REF-1167<anticancer']
- **cold** [needs-review,ev1] note="inferred from antiviral action"
    D=[] N=[] X=['REF-0300', 'REF-0315', 'REF-1170', 'REF-0293'] M=['REF-1167<antiviral', 'REF-1163<immunomodulator', 'REF-1164<immunomodulator', 'REF-1167<immunomodulator', 'REF-1171<immunomodulator']
- **immune-support** [needs-review,ev1] note=""
    D=[] N=[] X=['REF-0300', 'REF-0315', 'REF-1170', 'REF-0293'] M=['REF-1163<immunomodulator', 'REF-1164<immunomodulator', 'REF-1167<immunomodulator', 'REF-1171<immunomodulator']
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0300', 'REF-0315', 'REF-0293'] M=['REF-1167<antimicrobial', 'REF-1167<antiviral']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0293', 'REF-0300', 'REF-0315'] M=['REF-1167<antimicrobial']
  REF-0293 [traditional] 1996  | Lentinan — a novel immunomodulator | NO-ID 
     used: A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:antiviral, A:immunomodulator
     (no abstract)
  REF-0300 [narrative-review] 2011  | Current findings, future trends, and unsolved problems in studies of medicinal mushrooms | doi:10.1007/s00253-010-3067-4 
     used: A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:antiviral, A:immunomodulator
     C: Several of the mushroom polysaccharide compounds have proceeded through phases I, II, and III clinical trials and are used extensively and successfully in Asia to treat various cancers and other diseases. A total of 126 medicinal functions are thought to be produced by medicinal mushrooms and fungi including antitumor, immunomodulating, antioxidant, radical scavenging, cardiovascular, antihypercholesterolemia, antivi
  REF-0315 [traditional] 1989  | Observatory trial of anti-obesity activity of Eritadenine | NO-ID !TAG trial-title/traditional
     used: A:anticancer, A:antidiabetic, A:antimicrobial, A:antioxidant, A:antiviral, A:immunomodulator
     (no abstract)
  REF-1163 [preclinical] 2023 Iranian Journal of Basic Medical Science | Lentinan and beta-glucan extract from shiitake mushroom, Lentinula edodes, alleviate acute LPS-induced hematological changes in mice | doi:10.22038/IJBMS.2023.67669.14820 
     used: A:immunomodulator, M:cold, M:immune-support
     C: These findings suggest that β-glucans from L. edodes might be effective in attenuating the effects of inhaled LPS on peripheral blood parameters. Thus, these findings might be useful in acute inflammatory diseases particularly pulmonary infectious diseases in which the hematological parameters would be affected.
     !NULL: Total white blood cells, neutrophils, and monocyte counts did not show any significant difference among the groups.
  REF-1164 [preclinical] 2017 Scientific Reports | Lentinan from shiitake selectively attenuates AIM2 and non-canonical inflammasome activation while inducing pro-inflammatory cytokine production | doi:10.1038/s41598-017-01462-4 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Lentinan attenuated IL-1β secretion resulting from Listeria-mediated AIM2 inflammasome activation and reduced endotoxin lethality via inhibition of non-canonical inflammasome activation. Thus, lentinan is suggested as an anti-AIM2 and anti-non-canonical inflammasome candidate despite its up-regulation of cytokine expression.
  REF-1165 [preclinical] 2004 BioFactors | Lentinan from shiitake mushroom (Lentinus edodes) suppresses expression of cytochrome P450 1A subfamily in the mouse liver | doi:10.1002/biof.552210180 
     used: A:anticancer, M:cancer
     C: Recent our studies have demonstrated that lentinan suppresses hepatic CYP1As expression in the both constitutive and inducible levels through the production of tumor necrosis factor-alpha and an increase in the DNA-binding activity of nuclear factor-kappaB. This paper discusses on the effective lentinan dosage and route of administration for suppression of CYP1As.
  REF-1166 [preclinical] 2002 Journal of Alternative and Complementary | Inhibition of human colon carcinoma development by lentinan from shiitake mushrooms (Lentinus edodes) | doi:10.1089/107555302320825093 
     used: A:anticancer, D:cancer
     C: This study showed that the antitumor property of lentinan was maintained with oral administration. In addition, "primed" lymphocytes, when given passively to immunodeficient mice, were able to retard the development of tumors in these mice.
  REF-1167 [narrative-review] 2010 Current Medicinal Chemistry | Lentinus edodes: a macrofungus with pharmacological activities | doi:10.2174/092986710791698495 
     used: A:anticancer, A:antimicrobial, A:antiviral, A:immunomodulator, M:cancer, M:cold, M:immune-support, M:infection, M:wounds
     C: The aim of this review is to discuss the therapeutic applications of this macrofungus. The potential of this macrofungus is unquestionable in the most important areas of applied biotechnology.
  REF-1170 [preclinical] 2009 Fish & Shellfish Immunology | Modulation of splenic immune responses to bacterial lipopolysaccharide in rainbow trout (Oncorhynchus mykiss) fed lentinan, a beta-glucan from mushroo | doi:10.1016/j.fsi.2008.10.012 
     used: A:immunomodulator
     C: In conclusion, lentinan decreased the expression of genes involved in acute inflammatory reactions to the inflammatory agent while major parts of the immune response remained unchanged. Such effects are expected for IS, which should modify immunity by enhancing beneficial and reducing detrimental responses.
  REF-1171 [preclinical] 2019 Carbohydrate Polymers | Selenium-containing polysaccharides from Lentinula edodes-Biological activity | doi:10.1016/j.carbpol.2019.115078 
     used: A:immunomodulator, M:cold, M:immune-support
     C: However, we observed no effect of the polysaccharide fractions on the production of reactive oxygen species by granulocytes in vitro. The selenium content increased the biological activity of the tested polysaccharide fractions.
     !NULL: However, we observed no effect of the polysaccharide fractions on the production of reactive oxygen species by granulocytes in vitro.

## leonurus-cardiaca - Leonurus cardiaca - Motherwort, throw-wort, lion's tail
actions: anti-inflammatory=['REF-0198', 'REF-0270', 'REF-0860', 'REF-0865', 'REF-0866', 'REF-0867']; antioxidant=['REF-0198', 'REF-0270', 'REF-0861', 'REF-0865', 'REF-0868']; antispasmodic=['REF-0198', 'REF-0270']; sedative=['REF-0198', 'REF-0270', 'REF-0861', 'REF-0864']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0866', 'REF-0867', 'REF-0198', 'REF-0270'] M=['REF-0860<anti-inflammatory', 'REF-0865<anti-inflammatory']
- **cardiovascular-support** [verified,ev2] note=""
    D=['REF-0860', 'REF-0861', 'REF-0866', 'REF-0867'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0861'] N=[] X=['REF-0198', 'REF-0270'] M=['REF-0860<anti-inflammatory', 'REF-0865<anti-inflammatory', 'REF-0866<anti-inflammatory', 'REF-0867<anti-inflammatory']
- **insomnia** [needs-review,ev2] !INF note="inferred from sedative action"
    D=['REF-0861'] N=[] X=['REF-0198', 'REF-0270', 'REF-0864'] M=[]
- **menstrual-cramps** [verified,ev2] note=""
    D=['REF-0860'] N=[] X=['REF-0198', 'REF-0270'] M=[]
- **skin-irritation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0861'] N=[] X=['REF-0866', 'REF-0867', 'REF-0198', 'REF-0270'] M=['REF-0860<anti-inflammatory', 'REF-0865<anti-inflammatory']
  REF-0198 [traditional] 2003  | A Handbook of Medicinal Plants | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:sedative
     (no abstract)
  REF-0270 [traditional] 2014  | The genus Leonurus: traditional uses, phytochemistry and pharmacology | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:sedative
     (no abstract)
  REF-0860 [narrative-review] 2019 BioMed Research International | Leonurus cardiaca L. as a Source of Bioactive Compounds: An Update of the European Medicines Agency Assessment Report (2010) | doi:10.1155/2019/4303215 
     used: A:anti-inflammatory, D:cardiovascular-support, D:menstrual-cramps, M:arthritis, M:inflammation, M:skin-irritation
     C: Although its use in oriental and occidental medicine is relatively well documented, the recent progress registered raises the need for an update of the Medicines Agency assessment report on Leonurus cardiaca L., herba (2010). The current study presents the progress made within the 2010-2018 timeframe regarding the potential applications and scientific evidences supporting the traditional use of motherwort, in the sam
  REF-0861 [narrative-review] 2013 Phytotherapy Research | Leonurus cardiaca L. (motherwort): a review of its phytochemistry and pharmacology | doi:10.1002/ptr.4850 
     used: A:antioxidant, A:sedative, D:cardiovascular-support, D:inflammation, D:insomnia, D:skin-irritation
     C: Pharmacological studies have confirmed its antibacterial, antioxidant, anti-inflammatory and analgesic activity, as well as its effects on the heart and the circulatory system. Sedative and hypotensive activity has been demonstrated in clinical trials.
  REF-0864 [preclinical] 2021 Plants (Basel) | Phytochemical and Psychotropic Research of Motherwort (Leonurus cardiaca L.) Modified Dry Extracts | doi:10.3390/plants10020230 
     used: A:sedative
     C: The results obtained indicate the presence of anxiolytic activity in the motherwort extracts studied in complex with amino acids. The extracts with glycine, valine, and arginine were more effective in reducing anxiety in animals.
  REF-0865 [preclinical] 2021 Plants (Basel) | Phytochemical Profile and Biological Activities of Crude and Purified Leonurus cardiaca Extracts | doi:10.3390/plants10020195 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: Notably, quercetin, caffeic acid, lavandulifolioside, verbascoside, chlorogenic acid, rutin, and ursolic acid influenced the main variations in the bioactivities found in L. cardiaca extracts. Our findings provide further insights into the chemico-biological traits of L. cardiaca and a scientific basis for the development of nutraceuticals and food supplements.
  REF-0866 [preclinical] 2019 Molecules | Molecular Mechanisms of Leonurus cardiaca L. Extract Activity in Prevention of Staphylococcal Endocarditis - Study on in Vitro and ex Vivo Models | doi:10.3390/molecules24183318 
     used: A:anti-inflammatory, D:cardiovascular-support, M:inflammation
     C: Moreover, using FACS we showed also that LCE significantly reduced GP IIb/IIIa expression on blood platelets, thus the disruption of platelet-fibrinogen interactions seems to explain antiplatelet effect of LCE. The obtained results prove the usefulness of LCE in the prevention of S. aureus adhesion, platelet activation, and vegetations development, however, also pointed out the necessity of excluding the cationic ant
  REF-0867 [preclinical] 2025 Molecules | Phenolic and Iridoid Glycosides from Leonurus cardiaca L. and Their Effects on the alpha, delta, and gamma Subtypes of the PPAR System | doi:10.3390/molecules30020419 
     used: A:anti-inflammatory, D:cardiovascular-support, M:inflammation
     C: For PPARγ, no significant effects were observed. This activity of Leonurus extracts and especially of their active constituent 7-chloro-6-desoxy-harpagide on the δ subtype of the PPAR system strongly indicates their potential for anti-obesity therapy.
     !NULL: For PPARγ, no significant effects were observed.
  REF-0868 [preclinical] 2019 Antioxidants (Basel) | Hepatoprotection of Leonurus cardiaca L., Leonurus japonicus Houtt. and Leonurus sibiricus L. | doi:10.3390/antiox8080267 
     used: A:antioxidant
     C: While L. cardiaca extract showed moderate biological effects, M. aquatica extract displayed high antioxidant activity in chemical models, and that of L. dentata was effective in counteracting potassium dichromate-induced ROS generation in human hepatocarcinoma cells. Moreover, M. aquatica extract (50 μg/mL) and its mixture (50%/50%) with L. dentata extract displayed an effective cytoprotective effect.

## linum-usitatissimum - Linum usitatissimum - Flaxseed, linseed, common flax
actions: anti-inflammatory=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217', 'REF-2219', 'REF-2220', 'REF-2223', 'REF-2224']; anticancer=['REF-2222']; antioxidant=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2218', 'REF-2220', 'REF-2222']; digestive=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217', 'REF-2219']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217'] M=['REF-2219<anti-inflammatory', 'REF-2220<anti-inflammatory', 'REF-2223<anti-inflammatory', 'REF-2224<anti-inflammatory']
- **bloating** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217'] M=['REF-2219<digestive']
- **cancer** [needs-review,ev5] !INF note="inferred from anticancer action"
    D=['REF-2222', 'REF-0288'] N=[] X=[] M=[]
- **cardiovascular-support** [verified,ev5] note="Flaxseed lowered blood pressure in people with hypertension (review of trials); its lignan SDG is linked to lower lipids and blood pressure"
    D=['REF-0001', 'REF-0039', 'REF-3395'] N=['REF-2217'] X=[] M=[]
- **indigestion** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217'] M=['REF-2219<digestive']
- **inflammation** [needs-review,ev2] note="Flax lignan (SDG) metabolites reduce oxidative stress and inflammation (review) - compound evidence"
    D=['REF-0001'] N=[] X=['REF-0105', 'REF-0152', 'REF-2217'] M=['REF-2219<anti-inflammatory', 'REF-2220<anti-inflammatory', 'REF-2223<anti-inflammatory', 'REF-2224<anti-inflammatory']
- **metabolic-support** [verified,ev8] note="A flaxseed lignan (SDG) supplement modestly improved HbA1c in type 2 diabetes (RCT); lignan reviews report lower lipids and glucose - compound evidence"
    D=['REF-0001', 'REF-0190', 'REF-2221'] N=['REF-2217'] X=[] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0001', 'REF-0105', 'REF-0152', 'REF-2217'] M=['REF-2219<anti-inflammatory', 'REF-2220<anti-inflammatory', 'REF-2223<anti-inflammatory', 'REF-2224<anti-inflammatory']
  REF-0001 [narrative-review] 2010  | Health effects with consumption of the flax lignan secoisolariciresinol diglucoside | doi:10.1017/S0007114509992753 
     used: A:anti-inflammatory, A:antioxidant, A:digestive, D:cardiovascular-support, D:inflammation, D:metabolic-support
     C: Flaxseed and its lignan extracts appear to be safe for most adult populations, though animal studies suggest that pregnant women should limit their exposure. The present review discusses the potential health benefits of SDG in humans, with supporting evidence from animal studies, and offers suggestions for future research.
  REF-0039 [narrative-review] 2014  | Flaxseed for hypertension: implications for improved cardiovascular risk | doi:10.1007/s11906-014-0499-8 
     used: D:cardiovascular-support
     C: This review will highlight the recent data for flaxseed and its extracts in blood pressure regulation in both animal models and clinical trials. Insight into the proposed anti-hypertensive mechanism of flaxseed and the implications of flaxseed as a potential global anti-hypertensive therapy will be discussed.
  REF-0105 [traditional] 2012  | Stearidonic acid as a surrogate for eicosapentaenoic acid in cardiovascular risk reduction: update and recommendation | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:digestive
     (no abstract)
  REF-0152 [traditional] n.d.  | Linsēkla Latvijā | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:digestive
     (no abstract)
  REF-0190 [rct] 2007 PLoS One | Effects of a flaxseed-derived lignan supplement in type 2 diabetic patients: a randomized, double-blind, cross-over trial | pmid:17987126 doi:10.1371/journal.pone.0001148 
     used: D:metabolic-support
     C: Further studies are needed to validate these findings and explore the efficacy of lignans on type 2 diabetes. ClinicalTrials.gov NCT00363233.
     !NULL: 001) compared to placebo; however, no significant changes were observed in fasting glucose and insulin concentrations, insulin resistance and blood lipid profiles.
  REF-0288 [rct] 2006  | Dietary flaxseed alters tumor biological markers in postmenopausal breast cancer | doi:10.1158/1078-0432.CCR-04-2326 
     used: D:cancer
     C: Dietary flaxseed has the potential to reduce tumor growth in patients with breast cancer.
     !NULL: No significant differences in caloric and macronutrient intake were seen between groups and between pre- and posttreatment periods.
  REF-2217 [narrative-review] 2007 Journal of the Society for Integrative O | Flax and flaxseed oil (Linum usitatissimum): a review by the Natural Standard Research Collaboration | doi:10.2310/7200.2007.005 
     used: A:anti-inflammatory, A:digestive, N:cardiovascular-support, N:metabolic-support
     C: Most of the available evidence investigates the efficacy of alpha-linoleic acid found in flaxseed compared with fish oil, and almost all of the available studies are poor quality. Although flaxseed and flaxseed oil have several promising future uses, the available literature does not support recommendation for any condition at this time.
     !NULL: Although flaxseed and flaxseed oil have several promising future uses, the available literature does not support recommendation for any condition at this time.
  REF-2218 [narrative-review] 2020 Critical Reviews in Food Science and Nut | Lignans from linseed (Linum usitatissimum L.) and its allied species: retrospect, introspect and prospect | doi:10.1080/10408398.2020.1784840 
     used: A:antioxidant
     C: It summarizes various methods for the determination of lignan content in plants. Biotechnological interventions ( in planta and in vitro) aimed at enriching lignan content and adoption of integrative approaches that might further enhance lignan content and medicinal and nutraceutical value of Linum spp. have also been discussed.
  REF-2219 [narrative-review] 2019 Current Drug Discovery Technologies | A review on pharmacological and clinical aspects of Linum usitatissimum L. | doi:10.2174/1570163815666180521101136 
     used: A:anti-inflammatory, A:digestive, M:arthritis, M:bloating, M:indigestion, M:inflammation, M:skin-irritation
     C: Despite so much animal studies that have been accomplished, there have not been enough clinical trials done on pharmacological properties of L. usitatissimum. Therefore, this study could be considered as a concise and up to date overview for further facile studies and clinical trials over the valuable plant, L. usitatissimum.
  REF-2220 [narrative-review] 2021 Mini Reviews in Medicinal Chemistry | A comprehensive review on Linum usitatissimum medicinal plant: its phytochemistry, pharmacology, and ethnomedicinal uses | doi:10.2174/1389557521666210203153436 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: Further studies are expected to comprehend the detailed mode of action of its dynamic constituents as potent therapeutics and to completely reveal its preventive and healing potentials.
  REF-2221 [meta-analysis] 2024 Complementary Therapies in Medicine | The effects of flaxseed (Linum usitatissimum) supplementation on anthropometric indices: an updated systematic review and meta-analysis of randomized  | doi:10.1016/j.ctim.2024.103066 
     used: D:metabolic-support
     C: Our systematic review and meta-analysis suggests that supplementation with flaxseed (Linum usitatissimum) leads to meaningful improvements in body weight, BMI, and WC. Therefore, flaxseed can be considered as an adjunctive therapeutic approach in improving obesity.
     !NULL: According to three trials included in the systematic review, flaxseed did not affect anthropometric indices.
  REF-2222 [narrative-review] 2022 Critical Reviews in Food Science and Nut | A comprehensive review of flaxseed (Linum usitatissimum L.): health-affecting compounds, mechanism of toxicity, detoxification, anticancer and potenti | doi:10.1080/10408398.2022.2092718 
     used: A:anticancer, A:antioxidant, D:cancer
     C: However, such detoxification is also a challenge for the development, scalability, and real-time quantification of these bioactive substances. This review focuses on the health affecting composition of flaxseed, along with health benefits and potential toxicity of its components, detoxification methods and mechanisms with evidence supported by animal and human studies.
  REF-2223 [preclinical] 2011 Indian Journal of Experimental Biology | Anti-inflammatory, analgesic and antipyretic activities of Linum usitatissimum L. (flaxseed/linseed) fixed oil | NO-ID 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The oil contains 57.38% alpha-linolenic acid. Dual inhibition of arachidonic acid metabolism, antihistaminic and antibradykinin activities of the oil could account for the biological activity and the active principle could be alpha-linolenic acid an omega-3 (18:3, n-3) fatty acid.
  REF-2224 [preclinical] 2017 Journal of Evidence-Based Complementary  | The analgesic and anti-inflammatory activity of Linum usitatissimum in Balb/c mice | doi:10.1177/2156587217717416 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The extract had phenolic, flavonoid, and flavonol compounds with antioxidant activity. Linum usitatissimum L dose dependently had analgesic activity partially like morphine and might be used as analgesic and anti-inflammatory agent.
  REF-3395 [rct] 2013 Hypertension | Potent antihypertensive action of dietary flaxseed in hypertensive patients | pmid:24126178 doi:10.1161/HYPERTENSIONAHA.113.02094 
     used: D:cardiovascular-support
     C: Circulating α-linolenic acid levels correlated with SBP and DBP, and lignan levels correlated with changes in DBP. In summary, flaxseed induced one of the most potent antihypertensive effects achieved by a dietary intervention.
     !NULL: Plasma levels of the ω-3 fatty acid α-linolenic acid and enterolignans increased 2- to 50-fold in the flaxseed-fed group but did not increase significantly in the placebo group.
     !NULL: Patient body weights were not significantly different between the 2 groups at any time.

## lysimachia-vulgaris - Lysimachia vulgaris - Yellow loosestrife, garden loosestrife, yellow willowherb (loosestrife)
actions: antioxidant=['REF-2796', 'REF-2799', 'REF-2801', 'REF-2805']; anti-inflammatory=['REF-2795']; antimicrobial=['REF-2796']; anticancer=['REF-2796']; hepatoprotective=['REF-2794']; lipid-lowering=['REF-2793', 'REF-2797']; antidiarrheal=['REF-2795', 'REF-2796']; astringent=['REF-2796']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2796'] N=[] X=[] M=[]
- **liver-support** [verified,ev2] note="Ameliorates liver fibrosis/NASH in animal models."
    D=['REF-2794', 'REF-2797'] N=[] X=[] M=[]
- **high-cholesterol** [verified,ev2] note="PCSK9 inhibition and reduced hepatic lipogenesis (lipid-lowering)."
    D=['REF-2793'] N=[] X=['REF-2797'] M=[]
- **diarrhea** [verified,ev2] note="Improves diarrhoea-predominant IBS; traditional astringent antidiarrhoeal."
    D=['REF-2795', 'REF-2796'] N=[] X=[] M=[]
- **ibs** [verified,ev2] note="Improved diarrhoea-predominant irritable bowel syndrome (var. davurica)."
    D=['REF-2795'] N=[] X=[] M=[]
- **inflammation** [verified,ev2] note=""
    D=['REF-2796'] N=[] X=['REF-2795'] M=[]
- **infection** [needs-review,ev2] !INF note="inferred from antibacterial action"
    D=['REF-2796'] N=[] X=[] M=[]
- **wounds** [needs-review,ev2] !INF note="inferred from astringent/styptic traditional use"
    D=['REF-2796'] N=[] X=[] M=[]
  REF-2793 [preclinical] 2022 ACS Omega | Isocoumarins and Benzoquinones with Their Proprotein Convertase Subtilisin/Kexin Type 9 (PCSK9) Expression Inhibitory Activities from Dried Roots of L | doi:10.1021/acsomega.2c06660 
     used: A:lipid-lowering, D:high-cholesterol
     C: Of the isolates, 1 and 3 were found to inhibit PCSK9, inducible degrader of the low-density lipoprotein receptor (IDOL), and SREBP2 mRNA expression. Further computational dockings of both 1 and 3 to C-ring of IDOL E3 ubiquitin ligase predicted the mechanism behind the inhibitory effect of these compounds on the enzyme.
  REF-2794 [preclinical] 2021 BMC Complementary Medicine and Therapies | Yellow loosestrife (Lysimachia vulgaris var. davurica) ameliorates liver fibrosis in db/db mice with methionine- and choline-deficient diet-induced no | doi:10.1186/s12906-021-03212-6 
     used: A:hepatoprotective, D:liver-support
     C: Lipid accumulation and inflammatory responses in the liver were alleviated by feeding LV extract to NASH-induced mice. Moreover, the LV extract strongly prevented liver fibrosis by blocking TGFβ/Smad signaling. Hence, LV showed sufficient potency for use as a therapeutic agent against NASH.
  REF-2795 [preclinical] 2024 Molecules | Development and Validation of a High-Performance Liquid Chromatography Method to Quantify Marker Compounds in Lysimachia vulgaris var. davurica and It | doi:10.3390/molecules29071489 
     used: A:anti-inflammatory, A:antidiarrheal, D:diarrhea, D:ibs
     C: Furthermore, we developed and validated a high-performance liquid chromatography method using two marker compounds, namely, chlorogenic acid and rutin, for quality control analysis. Our study results suggest the feasibility of the methanol extract of LV for developing therapeutic agents to treat IBS-D by acting as a 5-HT 3 receptor antagonist.
  REF-2796 [preclinical] 2017 African Journal of Traditional, Compleme | Evaluation of Antibacterial, Antitumor, Antioxidant Activities and Phenolic Constituents of Field-Grown and In Vitro-Grown Lysimachia vulgaris L. | doi:10.21010/ajtcam.v14i2.19 
     used: A:anticancer, A:antidiarrheal, A:antimicrobial, A:antioxidant, A:astringent, D:cancer, D:diarrhea, D:infection, D:inflammation, D:wounds
     C: Future investigations should be focused on fractionation of the extracts to identify active components for biological activity.
  REF-2797 [preclinical] 2019 Journal of Agricultural and Food Chemist | Reduction of Hepatic Lipogenesis by Loliolide and Pinoresinol from Lysimachia vulgaris via Degrading Liver X Receptors | doi:10.1021/acs.jafc.9b01488 
     used: A:lipid-lowering, D:liver-support
     C: Importantly, loliolide and pinoresinol significantly accelerated the protein degradation of LXRs by enhanced ubiquitination, which inhibited lipogenesis. These results suggest that loliolide and pinoresinol might be potential candidate supplementary treatments for nonalcoholic fatty liver disease (NAFLD) by reducing lipogenesis through increased ubiquitination of LXRs.
  REF-2799 [preclinical] 2016 Natural Product Research | A new ultra-high pressure liquid chromatography method for the determination of antioxidant flavonol aglycones in six Lysimachia species | doi:10.1080/14786419.2016.1174233 
     used: A:antioxidant
     C: The observed radical scavenging capacities of the extracts showed a relationship with the measured flavonol aglycone content and composition. The acidic treatment resulted in an increased free radical scavenging activity compared to the untreated methanol extract.
  REF-2801 [preclinical] 2014 Natural Product Communications | Polyphenol composition and antioxidant capacity of three Lysimachia species | doi:10.1177/1934578x1400901017 
     used: A:antioxidant
     C: L. punctata extracts had the strongest DPPH and ABTS+ radical scavenger activity (IC50=43.3 μg/mL and 21.3 μg/mL), due to their high myricitrin and quercetin-hexoside content. Correlation between polyphenol content and radical scavenging activity of each column chromatographic fractions is also included.
  REF-2805 [preclinical] 2008 Bioresource Technology | Antioxidant activities of extracts and fractions from Lysimachia foenum-graecum Hance | doi:10.1016/j.biortech.2008.07.021 
     used: A:antioxidant
     C: This similar order of the amounts of total phenolics and total flavonoids shows that the extent of antioxidant and radical-scavenging activities is in accordance with the amounts of phenolics and flavonoids present in extracts and fractions. The extracts of L. foenum-graecum Hance might be valuable antioxidant natural sources and seemed to be applicable in both healthy medicine and food industry.

## mahonia-aquifolium - Mahonia aquifolium - Oregon Grape, Oregon grape root, Holly-leaved barberry
actions: anti-inflammatory=['REF-0487', 'REF-1179', 'REF-1182']; anticancer=['REF-0487', 'REF-1175', 'REF-1176', 'REF-1178']; antimicrobial=['REF-0488', 'REF-1174', 'REF-1177', 'REF-1180', 'REF-1181']
- **arthritis** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0488'] N=[] X=['REF-0487'] M=['REF-1179<anti-inflammatory', 'REF-1182<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1175'] N=[] X=['REF-0487'] M=['REF-1176<anticancer', 'REF-1178<anticancer']
- **eczema** [verified,ev7] note="Topical for atopic dermatitis (eczema) and skin irritation"
    D=['REF-0487'] N=[] X=[] M=[]
- **infection** [needs-review,ev2] note="Antimicrobial (berberine) - supports skin and mucosal infection"
    D=['REF-0488', 'REF-1177'] N=[] X=[] M=['REF-1174<antimicrobial', 'REF-1180<antimicrobial', 'REF-1181<antimicrobial']
- **inflammation** [needs-review,ev7] !INF note="inferred from anti-inflammatory action"
    D=['REF-0487', 'REF-1182'] N=[] X=[] M=['REF-1179<anti-inflammatory']
- **psoriasis** [verified,ev9] note="Topical 10% Mahonia aquifolium cream reduced plaque severity in mild-to-moderate psoriasis (double-blind placebo-controlled RCT and other trials; the cream is registered in the US as a homeopathic product but is a 10% plant extract)"
    D=['REF-0487', 'REF-0591', 'REF-1173', 'REF-1179'] N=[] X=[] M=[]
- **skin-irritation** [verified,ev8] note="Topical for atopic dermatitis (eczema) and skin irritation"
    D=['REF-0487', 'REF-1173'] N=[] X=[] M=['REF-1179<anti-inflammatory', 'REF-1182<anti-inflammatory']
- **wounds** [needs-review,ev1] !INF note="inferred from antimicrobial action"
    D=['REF-0488'] N=[] X=['REF-1180'] M=['REF-1174<antimicrobial', 'REF-1177<antimicrobial', 'REF-1181<antimicrobial']
  REF-0487 [systematic-review] 2018 Journal of Clinical and Aesthetic Dermat | Review of the Efficacy and Safety of Topical Mahonia aquifolium for the Treatment of Psoriasis and Atopic Dermatitis | NO-ID 
     used: A:anti-inflammatory, A:anticancer, D:eczema, D:inflammation, D:psoriasis, D:skin-irritation
     C: Several studies have shown that Mahonia aquifolium leads to a statistically significant improvement of symptoms in psoriasis and atopic dermatitis with minimal side effects.
  REF-0488 [traditional] n.d.  | Oregon Grape Root (Berberis aquifolium): Benefits, Uses, Safety | NO-ID 
     used: A:antimicrobial, D:arthritis, D:infection, D:wounds
     (no abstract)
  REF-0591 [rct] 2006 American Journal of Therapeutics | Treatment of mild to moderate psoriasis with Relieva, a Mahonia aquifolium extract - a double-blind, placebo-controlled study | doi:10.1097/00045391-200603000-00007 
     used: D:psoriasis
     C: The side effects reported were infrequent, < 1% and minor; the most frequent side effects were rash, a burning sensation when applying the cream, and clothing stain. These data indicate that Reliéva, a proprietary form of M. aquifolium, is effective and well tolerated in patients with mild to moderate psoriasis.
  REF-1173 [clinical] 2005 American Journal of Therapeutics | A report on three recent clinical trials using Mahonia aquifolium 10% topical cream and a review of the worldwide clinical experience with Mahonia aqu | doi:10.1097/01.mjt.0000174350.82270.da !TAG review-title/clinical
     used: D:psoriasis, D:skin-irritation
     C: Results from these 3 open-label clinical trials are in agreement with published data that include placebo-controlled studies. Taken together, these clinical studies conducted by several investigators in several countries indicate that Mahonia aquifolium is a safe and effective treatment of patients with mild to moderate psoriasis.
  REF-1174 [preclinical] 2002 Folia Microbiologica | Antimicrobial activity of berberine--a constituent of Mahonia aquifolium | doi:10.1007/BF02818693 
     used: A:antimicrobial, M:infection, M:wounds
     C: The antimicrobial activity of the protoberberine alkaloid, berberine, isolated from Mahonia aquifolium, was evaluated against 17 microorganisms including two Gram-negative bacteria--Pseudomonas aeruginosa and Escherichia coli (both resistant and sensitive), two Gram-positive bacteria--Bacillus subtilis and Staphylococcus aureus, Zoogloea ramigera, six filamentous fungi--Penicilium chrysogenum, Aspergillus niger, Aure
  REF-1175 [preclinical] 2020 Molecules | Mahonia aquifolium Extracts Promote Doxorubicin Effects against Lung Adenocarcinoma Cells In Vitro | doi:10.3390/molecules25225233 
     used: A:anticancer, D:cancer
     C: Furthermore, cells treated with doxorubicin/extract combinations were shown to have lower migratory and colony formation potentials than untreated cells or cells treated with doxorubicin alone. The obtained results suggest that nontoxic M. aquifolium extracts can enhance the activity of doxorubicin, thus potentially allowing the application of lower doxorubicin doses in vivo, which may decrease its toxic effects in n
  REF-1176 [preclinical] 2002 BMC Complementary and Alternative Medici | Potential antimutagenic activity of berberine, a constituent of Mahonia aquifolium | doi:10.1186/1472-6882-2-2 
     used: A:anticancer, M:cancer
     C: Taken together, the results indicate that berberine possesses promising antimutagenic/anticarcinogenic potential that is worth to be investigated further.
     !NULL: Especially berberine elicited, at a very low dose, remarkable suppression of the AO-induced mutagenicity, its antimutagenic potency being almost three orders of magnitude higher when compared to its close analogue, jatrorrhizine.
  REF-1177 [preclinical] 2004 Phytotherapy Research | Antimicrobial activity of Mahonia aquifolium crude extract and its major isolated alkaloids | doi:10.1002/ptr.1517 
     used: A:antimicrobial, D:infection, M:wounds
     C: The minimum inhibitory concentrations obtained in this study illustrate the varying degrees of antibacterial and antifungal activity of the tested agents. The results indicate a rational basis for the traditional use of Mahonia aquifolium for localized skin and mucosal infection therapy, as well as for the possible development of a preparation for supportive therapy of the diseases mentioned above.
  REF-1178 [preclinical] 2018 Journal of Pharmaceutical and Biomedical | Identification of cytotoxic metabolites from Mahonia aquifolium using 1H NMR-based metabolomics approach | doi:10.1016/j.jpba.2017.11.075 
     used: A:anticancer, M:cancer
     C: An OPLS multivariate analysis method was used to correlate the chemical composition of the plant extracts with the results of cytotoxic activity against Human cervical adenocarcinoma cell line. Protoberberine alkaloids berberinе and palmatine, along with bisbenzylisoquinoline alkaloid berbamine were identified as the most influential in the OPLS model, with the highest cytotoxic activity.
  REF-1179 [preclinical] 1994 Planta Medica | The antipsoriatic Mahonia aquifolium and its active constituents; I. Pro- and antioxidant properties and inhibition of 5-lipoxygenase | doi:10.1055/s-2006-959523 
     used: A:anti-inflammatory, D:psoriasis, M:arthritis, M:inflammation, M:skin-irritation
     C: Pro-oxidant effects by M. aquifolium or its constituents can be excluded, since deoxyribose degradation was not influenced as determined by the release of malondialdehyde. The most prominent feature of M. aquifolium is its efficacy in inhibition of lipid peroxidation (IC50 = 5 microM) which was not mediated by the alkaloids berberine, berbamine, and oxyacanthine.
  REF-1180 [preclinical] 2007 Schweizer Monatsschrift fur Zahnmedizin | Antimicrobial activity of Mahonia aquifolium and two of its alkaloids against oral bacteria | NO-ID 
     used: A:antimicrobial, M:infection
     C: The values for the minimum bactericidal concentrations were in the same range, indicating that the test substances most probably acted in a bactericidal manner. The most susceptible bacterium against all three test substances was Porphyromonas gingivalis.
  REF-1181 [preclinical] 2003 Phytotherapy Research | Antifungal activity of Mahonia aquifolium extract and its major protoberberine alkaloids | doi:10.1002/ptr.1256 
     used: A:antimicrobial, M:infection, M:wounds
     C: The effects of the alkaloids were compared with those of fluconazole and bifonazole for which the MIC ranges were 12.5 to >100 micro g/mL. Our results suggest that jatrorrhizine may serve as a leading compound for further studies to develop new antifungal agents with highly potent antifungal activity and low host toxicity.
  REF-1182 [preclinical] 2002 Planta Medica | Effect of Mahonia aquifolium active compounds on interleukin-8 production in the human monocytic cell line THP-1 | doi:10.1055/s-2002-23126 
     used: A:anti-inflammatory, D:inflammation, M:arthritis, M:skin-irritation
     C: Weak or no inhibition of IL-8 production was found after treatment with 0.5 microg/ml of protoberberine alkaloids berberine and jatrorrhizine and with berbamine from the group of BBI alkaloids. In contrast, the production was inhibited after treatment with BBI alkaloids baluchistine (about 20%) and aromoline (up to 30%).
     !NULL: The fraction of protoberberine alkaloids had no significant inhibitory activity.

## malva-sylvestris - Malva sylvestris - Mallow, Common mallow, High mallow
actions: analgesic=['REF-0541', 'REF-0542', 'REF-1190']; anti-inflammatory=['REF-0541', 'REF-0542', 'REF-1184', 'REF-1185', 'REF-1188', 'REF-1189', 'REF-1191', 'REF-1192']; anticancer=['REF-1183']; antimicrobial=['REF-0541', 'REF-0542']; antioxidant=['REF-0541', 'REF-0542', 'REF-1183', 'REF-1186', 'REF-1187', 'REF-1191']; demulcent=['REF-0480', 'REF-1184']; laxative=['REF-0480']; vulnerary=['REF-0541', 'REF-0542', 'REF-1190', 'REF-1191']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-1185', 'REF-1188', 'REF-1189', 'REF-1191', 'REF-0541', 'REF-0542'] M=['REF-1184<anti-inflammatory', 'REF-1192<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1183'] N=[] X=[] M=[]
- **cough** [verified,ev2] note="Demulcent for irritation of the mouth or throat and associated dry cough (soothing mucilage)"
    D=['REF-0480', 'REF-0542'] N=[] X=[] M=['REF-1184<demulcent']
- **infection** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0541', 'REF-0542'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0541', 'REF-0542', 'REF-1185', 'REF-1188', 'REF-1192'] N=[] X=[] M=['REF-1184<anti-inflammatory', 'REF-1189<anti-inflammatory', 'REF-1191<anti-inflammatory']
- **pain** [needs-review,ev2] !INF note="inferred from analgesic action"
    D=['REF-0541', 'REF-0542'] N=['REF-1190'] X=[] M=[]
- **skin-irritation** [verified,ev2] note="Soothes irritated and inflamed skin and mucous membranes"
    D=['REF-1189'] N=[] X=['REF-1185', 'REF-1188', 'REF-1191', 'REF-0480'] M=['REF-0541<anti-inflammatory', 'REF-0542<anti-inflammatory', 'REF-1184<anti-inflammatory', 'REF-1192<anti-inflammatory', 'REF-1184<demulcent']
- **sore-throat** [verified,ev1] note=""
    D=['REF-0480'] N=[] X=[] M=['REF-1184<demulcent']
- **wounds** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0541'] N=['REF-1190'] X=['REF-1191', 'REF-0542'] M=[]
  REF-0480 [traditional] n.d.  | European Union herbal monograph on Malva sylvestris L., folium and flos (Malvae folium / Malvae sylvestris flos) | NO-ID 
     used: A:demulcent, A:laxative, D:cough, D:sore-throat
     (no abstract)
  REF-0541 [narrative-review] 2024 Combinatorial Chemistry & High Throughpu | Phytochemistry and Pharmacological Activity of Malva sylvestris L.: A Detailed Insight | doi:10.2174/0113862073269336231009110313 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:vulnerary, D:infection, D:inflammation, D:pain, D:wounds, M:skin-irritation
     C: The plant also contains Malvone A, which is responsible for antibacterial action. The plant also possesses anti-inflammatory, analgesic, wound healing properties and various other activities.
  REF-0542 [narrative-review] 2022 Naunyn-Schmiedeberg's Archives of Pharma | The phytochemical profiling, pharmacological activities, and safety of Malva sylvestris: a review | doi:10.1007/s00210-022-02329-w 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:vulnerary, D:cough, D:infection, D:inflammation, D:pain, M:skin-irritation
     C: It has also summarised the work on developing copper oxide nanoparticles using Malva sylvestris leaf extract and its potential use in food and medicine. This review aims to highlight the traditional uses, phytochemistry, pharmacological activities, and safety of Malva sylvestris.
  REF-1183 [narrative-review] 2021 Evidence-Based Complementary and Alterna | A Review on Health Benefits of Malva sylvestris L. Nutritional Compounds for Metabolites, Antioxidants, and Anti-Inflammatory, Anticancer, and Antimic | doi:10.1155/2021/5548404 
     used: A:anticancer, A:antioxidant, D:cancer
     C: This amazing plant has antimicrobial, hepatoprotective, anti-inflammatory, and antioxidant properties and is considered as one of the most promising herbal medicinal species. This plant's traditional use in treating many diseases and preparing pharmaceutical compounds can show us how to know in depth the plant origin of drugs used to produce antibiotics and other therapeutic agents.
  REF-1184 [narrative-review] 2012 Journal of Pharmacy and Pharmacology | Ethnobotanical and scientific aspects of Malva sylvestris L.: a millennial herbal medicine | doi:10.1111/j.2042-7158.2011.01383.x 
     used: A:anti-inflammatory, A:demulcent, M:arthritis, M:cough, M:inflammation, M:skin-irritation, M:sore-throat
     C: The research has provided evidence that M. sylvestris has potential use as a medicinal plant and has highlighted a need for more studies involving clinical and toxicological aspects of its use. Summary This review can contribute to the field with its historical context, and by describing the progress made, new ideas for researchers can arise.
  REF-1185 [preclinical] 2019 Journal of Neuroimmunology | Malva sylvestris extract alleviates the astrogliosis and inflammatory stress in LPS-induced depression mice | doi:10.1016/j.jneuroim.2019.577029 
     used: A:anti-inflammatory, D:inflammation
     C: Finally, our findings showed that the extract of MS relieved inflammatory stress induced by LPS injury, indicated by the down-regulation of IL-1β/6 and TNF-α, and up-regulation of IL-4 level both in vitro and in vivo. Collectively, MS extract exhibits neuro-protective activity in vivo, and therefore, it may be widely used for food to relieve the symptoms of neuro-inflammation associated disorders such as depression.
  REF-1186 [preclinical] 2016 Biomedicine & Pharmacotherapy | Malva sylvestris extract protects upon lithium carbonate-induced kidney damages in male rat | doi:10.1016/j.biopha.2016.10.026 
     used: A:antioxidant
     C: However, pretreatment with Malva sylvestris extract restored the status of all parameters studied. It can be concluded that lithium carbonate has induced oxidative stress, biochemical changes and histopathological damage but the supplementation with Malva sylvestris extract has prevented such toxicity.
  REF-1187 [preclinical] 2017 Biomedicine & Pharmacotherapy | Cardioprotective effect of Malva sylvestris L. in myocardial ischemic/reperfused rats | doi:10.1016/j.biopha.2017.08.111 
     used: A:antioxidant
     C: The present results indicate the cardioprotective effects of MS of reducing oxidative stress and the inflammatory response in MI/R rats.
  REF-1188 [preclinical] 2015 PLoS One | Malva sylvestris Inhibits Inflammatory Response in Oral Human Cells. An In Vitro Infection Model | doi:10.1371/journal.pone.0140331 
     used: A:anti-inflammatory, D:inflammation
     C: Malva sylvestris and its chloroform fraction minimized the A. actinomycetemcomitans infection and inflammation processes in oral human cells by a putative pathway that involves important cytokines and receptors. Therefore, this natural product may be considered as a successful dual anti-inflammatory-antimicrobial candidate.
     !NULL: The extract and all fractions were assessed using a cytotoxicity test and results showed that concentrations under 100 μg/mL did not significantly reduce cell viability compared to the control group (p > 0.
  REF-1189 [preclinical] 2017 Biomedicine & Pharmacotherapy | Pre-clinical efficacy assessment of Malva sylvestris on chronic skin inflammation | doi:10.1016/j.biopha.2017.06.083 
     used: A:anti-inflammatory, D:skin-irritation, M:inflammation
     C: It was found that the anti-inflammatory effects of the extract did not involve the glucocorticoid system, and its incubation with HaCaT keratinocytes caused low toxicity and reduced cell proliferation by apoptosis. Thus, HEMS proved to be effective as an anti-psoriatic therapy, with the ability to prevent keratinocyte hyperproliferation and with low toxicity by topical application.
  REF-1190 [rct] 2022 International Journal of Community Based | The Effect of Malva sylvestris Cream on Episiotomy Pain and Healing: A Randomized Controlled Clinical Trial | doi:10.30476/IJCBNM.2022.95772.2082 
     used: A:analgesic, A:vulnerary, N:pain, N:wounds
     C: Despite showing the positive effect of Malva Sylvestris extract on wound healing in animal and in-vitro studies, this clinical study failed to show the positive effect of this extract on wound healing and pain relief of episiotomy. However, future clinical trials are needed to substantiate the above findings. Trial Registration Number: IRCT20190826044621N1.
     !NULL: Results There were no significant statistical differences between the two groups in demographic characteristics (P>0.
     !NULL: No significant statistical differences were found in both groups in terms of perineal healing (B=-0.
     !NULL: Conclusion Despite showing the positive effect of Malva Sylvestris extract on wound healing in animal and in-vitro studies, this clinical study failed to show the positive effect of this extract on wound healing and pain relief of episiotomy.
  REF-1191 [preclinical] 2023 Biomedicine & Pharmacotherapy | Potential benefits of Malva sylvestris in dry-eye disease pathology in vitro based on antioxidant, wound-healing and anti-inflammatory properties | doi:10.1016/j.biopha.2023.115782 
     used: A:anti-inflammatory, A:antioxidant, A:vulnerary, M:inflammation
     C: Moreover, the flower extract and the mucilage fraction at low concentration could stimulate meibomian gland cells' lipid accumulation. The isolated single compounds showed no effect on analysed parameters, except a coumarin derivative and malvin which showed ROS inhibition effects.
     !NULL: The isolated single compounds showed no effect on analysed parameters, except a coumarin derivative and malvin which showed ROS inhibition effects.
  REF-1192 [preclinical] 2014 Biomedical Chromatography | Malva sylvestris L. extract suppresses desferrioxamine-induced PGE2 and PGD2 release in differentiated U937 cells | doi:10.1002/bmc.3106 
     used: A:anti-inflammatory, D:inflammation, M:arthritis, M:skin-irritation
     C: This method was successfully applied using U937-d cells. A significant dose-dependent reduction of PGE2 and PGD2 levels occurred using 10 µg/mL (10.74 ± 2.86 and 9.60 ± 6.89%) and 50 µg/mL of extract (48.37 ± 3.24 and 53.06 ± 6.15%), suggesting that the anti-inflammatory mechanisms evoked by M. sylvestris may be related to modulation of these mediators.

## marrubium-vulgare - Marrubium vulgare - Horehound, White horehound, Common horehound
actions: anticancer=['REF-2558']; antispasmodic=['REF-0469', 'REF-0925']; bitter-tonic=['REF-0468']; digestive=['REF-0468']; expectorant=['REF-0468', 'REF-0469', 'REF-0921', 'REF-0926']
- **appetite-loss** [verified,ev2] note="Bitter digestive for dyspeptic complaints (indigestion, bloating, flatulence) and loss of appetite"
    D=['REF-0468', 'REF-0921', 'REF-0469'] N=[] X=[] M=[]
- **bloating** [verified,ev1] note="Bitter digestive for dyspeptic complaints (indigestion, bloating, flatulence) and loss of appetite"
    D=['REF-0468', 'REF-0469'] N=[] X=[] M=[]
- **bronchitis** [verified,ev2] note="Expectorant for productive cough and catarrh of the upper respiratory tract / bronchitis"
    D=['REF-0921'] N=[] X=['REF-0926', 'REF-0468', 'REF-0469'] M=[]
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2558'] N=[] X=[] M=[]
- **cough** [needs-review,ev1] note="EU traditional use as an expectorant in cough associated with a cold"
    D=['REF-0468'] N=[] X=['REF-0926', 'REF-0469', 'REF-0921'] M=[]
- **indigestion** [verified,ev2] note="Bitter digestive for dyspeptic complaints (indigestion, bloating, flatulence) and loss of appetite"
    D=['REF-0468', 'REF-0921', 'REF-0469'] N=[] X=[] M=[]
- **respiratory-support** [needs-review,ev2] !INF note="inferred from expectorant action"
    D=['REF-0468', 'REF-0469', 'REF-0921', 'REF-0926'] N=[] X=[] M=[]
  REF-0468 [traditional] 2013  | European Union herbal monograph on Marrubium vulgare L., herba (Marrubii herba) | NO-ID 
     used: A:bitter-tonic, A:digestive, A:expectorant, D:appetite-loss, D:bloating, D:cough, D:indigestion, D:respiratory-support
     (no abstract)
  REF-0469 [traditional] n.d.  | Marrubii herba (White Horehound) monograph | NO-ID 
     used: A:antispasmodic, A:expectorant, D:appetite-loss, D:bloating, D:indigestion, D:respiratory-support
     (no abstract)
  REF-0921 [narrative-review] 2016 Phytotherapy Research | An Insight into a Blockbuster Phytomedicine; Marrubium vulgare L. Herb. More of a Myth than a Reality? | doi:10.1002/ptr.5661 
     used: A:expectorant, D:appetite-loss, D:bronchitis, D:indigestion, D:respiratory-support
     C: It is time to systematize and critically analyse the quality of results found to date. Copyright © 2016 John Wiley & Sons, Ltd.
  REF-0925 [preclinical] 2024 Chemistry & Biodiversity | Chemical Investigation and Antinociceptive Activity Evaluation of Marrubium vulgare L. Aqueous Extract | doi:10.1002/cbdv.202400228 
     used: A:antispasmodic
     C: High-performance liquid chromatography (HPLC) analysis identified important bioactive compounds, with marrubiin being a major component. Furthermore, AEMV demonstrated robust antinociceptive properties in all conducted tests, highlighting its potential as a valuable natural source of bioactive compounds suitable for a wide range of therapeutic applications.
  REF-0926 [preclinical] 2022 Dose-Response | Tunisian Horehound (Marrubium vulgare) Aqueous Extract Improves Treatment of Bleomycin-Induced Lung Fibrosis in Rat | doi:10.1177/15593258221119300 
     used: A:expectorant, D:respiratory-support
     C: The Mae treatment reversed all disturbances of BLM-induced oxidative stress parameters promoting antioxidant and anti-inflammatory of the latter. These findings point to Mae as a promising candidate for the treatment of pulmonary fibrosis.
  REF-2558 [preclinical] 2006 Oncology Reports | Anti-proliferative effect of horehound leaf and wild cherry bark extracts on human colorectal cancer cells | doi:10.3892/or.15.1.275 
     used: A:anticancer, D:cancer
     C: Our data suggest the mechanisms by which these extracts suppress cell growth and induce apoptosis involve enhanced NAG-1 expression and/or down-regulation of beta-catenin signaling, followed by reduced cyclin D1 expression in human colorectal cancer cells. These findings may provide mechanisms for traditional anti-inflammatory products as cancer chemopreventive agents.

## matricaria-chamomilla - Matricaria chamomilla - Chamomile, German chamomile, blue chamomile
actions: analgesic=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-2349', 'REF-2351']; anti-inflammatory=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-1153', 'REF-1157', 'REF-1158', 'REF-1159', 'REF-1162', 'REF-2349']; antimicrobial=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-1153']; antispasmodic=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-1153', 'REF-1157', 'REF-1158', 'REF-2351']; digestive=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-1153', 'REF-1157', 'REF-1162']; emollient=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280']; sedative=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280', 'REF-1153', 'REF-1154', 'REF-1155', 'REF-1156', 'REF-1159', 'REF-1160', 'REF-1162']; vulnerary=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280']; anxiolytic=['REF-1155', 'REF-1160']; antidepressant=['REF-2348']; antidiabetic=['REF-2350']
- **arthritis** [needs-review,ev5] !INF note="inferred from anti-inflammatory action"
    D=['REF-0280', 'REF-2349'] N=[] X=['REF-0079', 'REF-0112', 'REF-0189'] M=['REF-1153<anti-inflammatory', 'REF-1157<anti-inflammatory', 'REF-1158<anti-inflammatory', 'REF-1159<anti-inflammatory', 'REF-1162<anti-inflammatory']
- **bloating** [needs-review,ev1] !INF note="inferred from digestive action"
    D=['REF-0079'] N=[] X=['REF-0112', 'REF-0189', 'REF-0280'] M=['REF-1153<digestive', 'REF-1157<digestive', 'REF-1162<digestive']
- **indigestion** [needs-review,ev1] !INF note="inferred from digestive action"
    D=['REF-0079'] N=[] X=['REF-0112', 'REF-0189', 'REF-0280'] M=['REF-1153<digestive', 'REF-1157<digestive', 'REF-1162<digestive']
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0112', 'REF-0189', 'REF-0280', 'REF-0079'] M=['REF-1153<antimicrobial']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0079', 'REF-0280'] N=[] X=['REF-0112', 'REF-0189'] M=['REF-1153<anti-inflammatory', 'REF-1157<anti-inflammatory', 'REF-1158<anti-inflammatory', 'REF-1159<anti-inflammatory', 'REF-1162<anti-inflammatory', 'REF-2349<anti-inflammatory']
- **insomnia** [needs-review,ev7] !INF note="inferred from sedative action"
    D=['REF-0280', 'REF-1154'] N=[] X=['REF-0079', 'REF-1155', 'REF-1156', 'REF-1160', 'REF-0112', 'REF-0189'] M=['REF-1153<sedative', 'REF-1159<sedative', 'REF-1162<sedative']
- **menstrual-cramps** [needs-review,ev7] !INF note="inferred from antispasmodic action"
    D=['REF-2351'] N=[] X=['REF-0079', 'REF-0112', 'REF-0189', 'REF-0280'] M=['REF-1153<antispasmodic', 'REF-1157<antispasmodic', 'REF-1158<antispasmodic']
- **muscle-spasm** [needs-review,ev2] !INF note="inferred from antispasmodic action"
    D=['REF-0079', 'REF-0280'] N=[] X=['REF-0112', 'REF-0189'] M=['REF-1153<antispasmodic', 'REF-1157<antispasmodic', 'REF-1158<antispasmodic', 'REF-2351<antispasmodic']
- **pain** [verified,ev2] note=""
    D=['REF-0280'] N=[] X=['REF-0079', 'REF-0112', 'REF-0189'] M=['REF-2349<analgesic', 'REF-2351<analgesic']
- **skin-irritation** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0079'] N=[] X=['REF-2349', 'REF-0112', 'REF-0189', 'REF-0280'] M=['REF-1153<anti-inflammatory', 'REF-1157<anti-inflammatory', 'REF-1158<anti-inflammatory', 'REF-1159<anti-inflammatory', 'REF-1162<anti-inflammatory']
- **wounds** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0079', 'REF-0280'] N=[] X=['REF-0112', 'REF-0189'] M=['REF-1153<antimicrobial']
- **anxiety** [verified,ev6] note=""
    D=['REF-1155', 'REF-1160'] N=[] X=[] M=[]
- **depression** [verified,ev5] note=""
    D=['REF-2348'] N=[] X=[] M=[]
- **blood-sugar** [verified,ev5] note=""
    D=['REF-2350'] N=[] X=[] M=[]
  REF-0079 [traditional] 2015  | European Union herbal monograph on Matricaria recutita L., flos | NO-ID 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:digestive, A:emollient, A:sedative, A:vulnerary, D:bloating, D:indigestion, D:inflammation, D:muscle-spasm, D:skin-irritation, D:wounds
     (no abstract)
  REF-0112 [traditional] 2003  | Medical Herbalism | NO-ID 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:digestive, A:emollient, A:sedative, A:vulnerary
     (no abstract)
  REF-0189 [traditional] 2006  | Chamomile: industrial profiles | NO-ID 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:digestive, A:emollient, A:sedative, A:vulnerary
     (no abstract)
  REF-0280 [narrative-review] 2010  | Chamomile: a herbal medicine of the past with bright future | doi:10.3892/mmr.2010.377 
     used: A:analgesic, A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:digestive, A:emollient, A:sedative, A:vulnerary, D:arthritis, D:inflammation, D:insomnia, D:muscle-spasm, D:pain, D:wounds
     C: Many different preparations of chamomile have been developed, the most popular of which is in the form of herbal tea consumed more than one million cups per day. In this review we describe the use of chamomile in traditional medicine with regard to evaluating its curative and preventive properties, highlight recent findings for its development as a therapeutic agent promoting human health.
  REF-1153 [narrative-review] 2022 Life | Chamomile (Matricaria chamomilla L.): A Review of Ethnomedicinal Use, Phytochemistry and Pharmacological Uses | doi:10.3390/life12040479 
     used: A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:digestive, A:sedative, M:arthritis, M:bloating, M:indigestion, M:infection, M:inflammation, M:insomnia, M:menstrual-cramps, M:muscle-spasm, M:skin-irritation, M:wounds
     C: Indeed, M. chamomilla essential oils and extracts showed interesting antioxidant, antibacterial, antifungal, anticancer, antidiabetic, antiparasitic, anti-inflammatory, anti-depressant, anti-pyretic, anti-allergic, and analgesic activities. Moreover, the most important application of M. chamomilla was in the medicinal field on animals and humans.
  REF-1154 [meta-analysis] 2024 Complementary Therapies in Medicine | Effects of chamomile (Matricaria chamomilla L.) on sleep: A systematic review and meta-analysis of clinical trials | doi:10.1016/j.ctim.2024.103071 
     used: A:sedative, D:insomnia
     C: Chamomile improved sleep, especially the number of awakenings after sleep or staying asleep; however, it did not lead to an improvement in the duration of sleep, percentage of sleep efficiency, and daytime functioning measures. Future studies are suggested to assess objective measures.
     !NULL: Daytime functioning measures, including fatigue severity index or postpartum fatigue scale, did not change in all three studies.
     !NULL: Sleep efficiency did not change in two studies and deteriorated in one.
  REF-1155 [rct] 2016 Phytomedicine | Long-term chamomile (Matricaria chamomilla L.) treatment for generalized anxiety disorder: A randomized clinical trial | doi:10.1016/j.phymed.2016.10.012 
     used: A:anxiolytic, A:sedative, D:anxiety
     C: Long-term chamomile was safe and significantly reduced moderate-to-severe GAD symptoms, but did not significantly reduce rate of relapse. Our limited sample size and lower than expected rate of placebo group relapse likely contributed to the non-significant primary outcome finding. Possible chamomile superiority over placebo requires further examination in large-scale studies.
     !NULL: Hazard of relapse was non-significantly lower for chamomile (hazard ratio, 0.
     !NULL: Conclusions Long-term chamomile was safe and significantly reduced moderate-to-severe GAD symptoms, but did not significantly reduce rate of relapse.
     !NULL: Our limited sample size and lower than expected rate of placebo group relapse likely contributed to the non-significant primary outcome finding.
  REF-1156 [clinical] 2020 Journal of Alternative and Complementary | Putative Antidepressant Effect of Chamomile (Matricaria chamomilla L.) Oral Extract in Subjects with Comorbid Generalized Anxiety Disorder and Depress | doi:10.1089/acm.2019.0252 
     used: A:sedative
     C: M. chamomilla L. may produce clinically meaningful antidepressant effects in addition to its anxiolytic activity in subjects with GAD and comorbid depression. Future controlled trials in subjects with primary major depressive disorder are needed to validate this preliminary observation.
  REF-1157 [narrative-review] 2006 Phytotherapy Research | A review of the bioactivity and potential health benefits of chamomile tea (Matricaria recutita L.) | doi:10.1002/ptr.1900 
     used: A:anti-inflammatory, A:antispasmodic, A:digestive, M:arthritis, M:bloating, M:indigestion, M:inflammation, M:menstrual-cramps, M:muscle-spasm, M:skin-irritation
     C: Adverse reactions to chamomile, consumed as a tisane or applied topically, have been reported among those with allergies to other plants in the daisy family, i.e. Asteraceae or Compositae.
  REF-1158 [narrative-review] 2022 Molecules | Chamomile: A Review of Its Traditional Uses, Chemical Constituents, Pharmacological Activities and Quality Control Studies | doi:10.3390/molecules28010133 
     used: A:anti-inflammatory, A:antispasmodic, M:arthritis, M:inflammation, M:menstrual-cramps, M:muscle-spasm, M:skin-irritation
     C: However, more toxicity tests should be carried out to confirm its safety. There is need for further research to provide concrete scientific evidence and validate its medicinal properties.
  REF-1159 [systematic-review] 2016 Electronic Physician | A systematic review study of therapeutic effects of Matricaria recutita chamomile (chamomile) | doi:10.19082/3024 
     used: A:anti-inflammatory, A:sedative, M:arthritis, M:inflammation, M:insomnia, M:skin-irritation
     C: Matricaria recuitta chamomilla L . is widely used for therapeutic and nontherapeutic purposes that trigger its significant value. Various combinations and numerous medicinal properties of its extract, oil, and leaves demand further studies about other useful and unknown properties of this multipurpose plant.
  REF-1160 [rct] 2009 Journal of Clinical Psychopharmacology | A randomized, double-blind, placebo-controlled trial of oral Matricaria recutita (chamomile) extract therapy for generalized anxiety disorder | doi:10.1097/JCP.0b013e3181ac935c 
     used: A:anxiolytic, A:sedative, D:anxiety
     C: This is the first controlled clinical trial of chamomile extract for GAD. The results suggest that chamomile may have modest anxiolytic activity in patients with mild to moderate GAD. Future studies are needed to replicate these observations.
     !NULL: The proportion of patients experiencing 0, 1, 2, or 3 adverse events or more was not significantly different between groups (P = 0.
  REF-1162 [narrative-review] 2011 Pharmacognosy Reviews | Chamomile (Matricaria chamomilla L.): An overview | doi:10.4103/0973-7847.79103 
     used: A:anti-inflammatory, A:digestive, A:sedative, M:arthritis, M:bloating, M:indigestion, M:inflammation, M:insomnia, M:skin-irritation
     C: Furthermore, particular emphasis is given to the biochemistry, biotechnology, market demand, and trade of the plant. This is an attempt to compile and document information on different aspects of chamomile and highlight the need for research and development.
  REF-2348 [rct] 2012 Alternative Therapies in Health and Medi | Chamomile (Matricaria recutita) may provide antidepressant activity in anxious, depressed humans: an exploratory study | NO-ID 
     used: A:antidepressant, D:depression
     C: Chamomile may provide clinically meaningful antidepressant activity that occurs in addition to its previously observed anxiolytic activity.
     !NULL: The team also observed a clinically meaningful but nonsignificant trend for a greater reduction in total HAM-D scores for chamomile vs placebo in participants with current comorbid depression (P = .
     !NULL: 05) and a clinically meaningful but nonsignificant trend for a greater reduction over time for chamomile vs placebo in participants without current or past depression (P = .
  REF-2349 [rct] 2015 Complementary Therapies in Clinical Prac | Efficacy and safety of topical Matricaria chamomilla L. (chamomile) oil for knee osteoarthritis: a randomized controlled clinical trial | doi:10.1016/j.ctcp.2015.06.003 
     used: A:analgesic, A:anti-inflammatory, D:arthritis, M:inflammation, M:pain
     C: Chamomile oil decreased the analgesic demand of patients with knee osteoarthritis. In addition, it may show some beneficial effects on physical function, and stiffness of the patients.
     !NULL: However, there were no significant differences in WOMAC questionnaire domains.
  REF-2350 [rct] 2016 Nutrition | Chamomile tea improves glycemic indices and antioxidants status in patients with type 2 diabetes mellitus | doi:10.1016/j.nut.2015.07.011 
     used: A:antidiabetic, D:blood-sugar
     C: Short term intake of chamomile tea has beneficial effects on glycemic control and antioxidant status in patients with T2 DM. A larger sample population and a longer intervention period may be required to show significant clinical improvements.
  REF-2351 [systematic-review] 2021 International Journal of Community Based | The effect of chamomile on pain and menstrual bleeding in primary dysmenorrhea: a systematic review | doi:10.30476/ijcbnm.2021.87219.1417 
     used: A:analgesic, A:antispasmodic, D:menstrual-cramps, M:muscle-spasm, M:pain
     C: Based on results of the most reviewed studies, Chamomile can be considered as an effective treatment for primary dysmenorrhea and reducing menstrual bleeding.
