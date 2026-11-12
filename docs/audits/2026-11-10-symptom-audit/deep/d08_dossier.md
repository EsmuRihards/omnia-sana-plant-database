# Deep dossier batch 8

## geum-rivale - Geum rivale - Water avens, purple avens, chocolate root
actions: astringent=['REF-2761', 'REF-2768']; antidiarrheal=['REF-2768', 'REF-2769']; antioxidant=['REF-2761', 'REF-2770']; antimicrobial=['REF-2763']; anti-inflammatory=['REF-2767']; anticancer=[]; antiviral=[]; neuroprotective=['REF-2761']; antidiabetic=[]; vulnerary=['REF-2769']
- **diarrhea** [needs-review,ev1] note="inferred from astringent (tannin) action"
    D=[] N=[] X=['REF-2768'] M=['REF-2761<astringent']
- **inflammation** [verified,ev2] note=""
    D=['REF-2767'] N=[] X=[] M=[]
- **infection** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-2763', 'REF-2761'] N=[] X=[] M=[]
- **wounds** [needs-review,ev1] note="inferred from astringent/antimicrobial action and traditional wound-wash use"
    D=[] N=[] X=['REF-2769'] M=['REF-2763<antimicrobial', 'REF-2761<astringent', 'REF-2768<astringent']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory/antimicrobial skin activity"
    D=[] N=[] X=[] M=['REF-2767<anti-inflammatory', 'REF-2761<astringent', 'REF-2768<astringent']
  REF-2761 [preclinical] 2022 Plants (Basel) | Phytochemical Characterization of Water Avens (Geum rivale L.) Extracts: Structure Assignment and Biological Activity of the Major Phenolic Constituen | doi:10.3390/plants11212859 
     used: A:antioxidant, A:astringent, A:neuroprotective, D:infection, M:diarrhea, M:skin-irritation, M:wounds
     C: However, the antibacterial activity of the fractions could not be associated with any of the isolated individual major phenolics (excepting 3- O -methylellagic acid). Thus, the aerial parts of water avens represent a promising source of polyphenolic compounds with antioxidant activity and therefrom derived human health benefits, although the single constituents isolated so far lack a dominant selectively bioactive co
  REF-2763 [preclinical] 2000 Phytotherapy Research | In vitro antimicrobial activity of extracts and isolated constituents of Geum rivale | doi:10.1002/1099-1573(200011)14:7<561::aid-ptr651>3.0.co;2-h 
     used: A:antimicrobial, D:infection, M:wounds
     C: The antimicrobial activity of extracts of Geum rivale (Rosaceae) and that of some isolated constituents, on bacteria and fungi, was evaluated. The activity was concentrated in the triterpenes fraction and, for gram+ and gram- bacteria, also in the flavonoids fraction.
  REF-2767 [preclinical] 1995 Journal of Ethnopharmacology | Evaluation of anti-inflammatory activity of some Swedish medicinal plants. Inhibition of prostaglandin biosynthesis and PAF-induced exocytosis | doi:10.1016/0378-8741(95)01285-l 
     used: A:anti-inflammatory, D:inflammation, M:skin-irritation
     C: In the PAF-test, high inhibition was obtained by 19 extracts, the most potent of which were from Geum rivale, G. urbanum, Solanum dulcamara, Symphytum x uplandicum and Vaccinium vitis-idaea. The in vitro effects in relation to the traditional use, chemical contents and botanical classification, as well as the possibilities and the limitations of the methods are discussed.
  REF-2768 [preclinical] 1990 Annales Pharmaceutiques Francaises | Tannin content and inhibiting activity of elastase in Rosaceae | NO-ID 
     used: A:antidiarrheal, A:astringent, M:skin-irritation, M:wounds
     C: From 42 Rosaceae species, only the Rosoideae species exhibit high tannin content and elastase inhibiting activity such as Filipendula ulmaria, Geum montanum, G. rivale, Alchemilla xanthochlora and Sanguisorba minor. Other studied species from Spiraeoideae, Maloideae and Prunoideae subfamilies are less rich in tannin and also less active.
  REF-2769 [traditional] 1954 Aptechnoe Delo | Anatomical structure of Geum urbanum and Geum rivale and localization of tannins | NO-ID 
     used: A:antidiarrheal, A:vulnerary
     (no abstract)
  REF-2770 [narrative-review] 2025 Molecules | Ellagitannins and Other Polyphenols Along with Dietary Components of the Rosaceae Medicinal Plants | doi:10.3390/molecules30234574 
     used: A:antioxidant
     C: Due to their resistance to fungal diseases and pathogens, the medicinal plants are free from pesticide residues. Sanguisorba , Geum , and Agrimonia are tasty and aromatic and can be the basis of dishes, salads, or beverages.

## ginkgo-biloba - Ginkgo biloba - Ginko, Ginkgo, maidenhair tree
actions: anti-inflammatory=['REF-0308', 'REF-2179']; antioxidant=['REF-0308', 'REF-0824', 'REF-2180', 'REF-2181', 'REF-2182', 'REF-2184']; neuroprotective=['REF-0056', 'REF-0128', 'REF-0308', 'REF-0824', 'REF-0825', 'REF-2179', 'REF-2180', 'REF-2182', 'REF-2184', 'REF-2185', 'REF-2186']
- **cardiovascular-support** [verified,ev1] note=""
    D=['REF-0308'] N=[] X=[] M=[]
- **cognitive-function** [needs-review,ev9] !INF note="inferred from neuroprotective action"
    D=['REF-0128', 'REF-0308', 'REF-2186', 'REF-2185'] N=['REF-0056'] X=[] M=['REF-0824<neuroprotective', 'REF-0825<neuroprotective', 'REF-2179<neuroprotective', 'REF-2180<neuroprotective', 'REF-2182<neuroprotective', 'REF-2184<neuroprotective']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0308'] M=['REF-2179<anti-inflammatory']
- **memory** [needs-review,ev9] !INF note="inferred from neuroprotective action"
    D=['REF-0128', 'REF-0308', 'REF-2186', 'REF-2185'] N=['REF-0056'] X=[] M=['REF-0824<neuroprotective', 'REF-0825<neuroprotective', 'REF-2179<neuroprotective', 'REF-2180<neuroprotective', 'REF-2182<neuroprotective', 'REF-2184<neuroprotective']
  REF-0056 [rct] 2008  | Ginkgo biloba for prevention of dementia: a randomized controlled trial | doi:10.1001/jama.2008.683 
     used: A:neuroprotective, N:cognitive-function, N:memory
     C: In this study, G. biloba at 120 mg twice a day was not effective in reducing either the overall incidence rate of dementia or AD incidence in elderly individuals with normal cognition or those with MCI. Trial Registration clinicaltrials.gov Identifier: NCT00010803.
     !NULL: biloba also had no effect on the rate of progression to dementia in participants with MCI (HR, 1.
     !NULL: biloba at 120 mg twice a day was not effective in reducing either the overall incidence rate of dementia or AD incidence in elderly individuals with normal cognition or those with MCI.
  REF-0128 [rct] 1996  | Proof of efficacy of the ginkgo biloba special extract EGb 761 in outpatients suffering from mild to moderate primary degenerative dementia of the Alz | doi:10.1016/s0944-7113(97)80021-9 
     used: A:neuroprotective, D:cognitive-function, D:memory
     C: Thus, the clinical efficacy of the ginkgo biloba special extract EGb 761 in dementia of the Alzheimer type and multi-infarct dementia was confirmed. The investigational drug was found to be well tolerated.
  REF-0308 [traditional] 1999  | WHO Monographs on Selected Medicinal Plants, Volume 1 | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:neuroprotective, D:cardiovascular-support, D:cognitive-function, D:memory
     (no abstract)
  REF-0824 [traditional] 2019 Neurotherapeutics | Neuroprotective and Antioxidant Effect of Ginkgo biloba Extract Against AD and Other Neurological Disorders | doi:10.1007/s13311-019-00767-8 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: This review summarizes recent advancements in our understanding of the potential use of Ginkgo biloba extract in the prevention of AD including its antioxidant property. A better understanding of the mechanisms of action of GBE against AD will be important for designing therapeutic strategies, for basic understanding of the underlying neurodegenerative processes, and for a better understanding of the effectiveness an
  REF-0825 [preclinical] 2013 Psychiatric Clinics of North America | Ginkgo biloba: indications, mechanisms, and safety | doi:10.1016/j.psc.2012.12.006 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: Possible interactions with monoamine oxidase inhibitors, alprazolam, haloperidol, warfarin, and nifedipine have been reported. Optimal dosage/duration, dose-response characteristics, drug interactions, bioavailability, long-term effects, and optimal intervention timing should be the focus of future work.
  REF-2179 [preclinical] 2024 CNS Neuroscience & Therapeutics | Investigating the effects of Ginkgo biloba leaf extract on cognitive function in Alzheimer's disease | doi:10.1111/cns.14914 
     used: A:anti-inflammatory, A:neuroprotective, M:cognitive-function, M:inflammation, M:memory
     C: GBE shows promise as a potential treatment for AD. Its beneficial effects on cognitive function, neuronal morphology, and inflammation may be attributed to its modulation of the PI3K/AKT/NF-κB signaling pathway. These findings provide experimental evidence for the application of Ginkgo biloba leaf in AD treatment and highlight its potential mechanisms of action.
  REF-2180 [narrative-review] 2000 Archives of Physical Medicine and Rehabi | Ginkgo biloba extract: mechanisms and clinical indications | doi:10.1016/s0003-9993(00)90052-2 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: Ginkgo shows promise in treating some of the neurologic sequelae associated with Alzheimer's disease, TBI, stroke, normal aging, edema, tinnitus, and macular degeneration. Mechanisms of action may include antioxidant, neurotransmitter/receptor modulatory, and antiplatelet activating factor properties. While safe, caution is advised when recommending ginkgo to patients taking anticoagulants. Future studies should exam
  REF-2181 [narrative-review] 2004 Kathmandu University Medical Journal | Ginkgo biloba--an appraisal | NO-ID 
     used: A:antioxidant
     C: Ginkgo biloba inhibits microsomal enzymes and has a potential for drug interactions. Further studies to establish the efficacy of Ginkgo biloba are required.
  REF-2182 [narrative-review] 2004 Frontiers in Bioscience | Ginkgo biloba and neurodegenerative disorders | doi:10.2741/1462 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: Ambitious interventional studies are underway and may provide new evidence regarding the effect of EGb 761 in preventing Alzheimer's disease in humans. Positive findings would be particularly interesting since this drug is very safe to use.
  REF-2184 [narrative-review] 2000 Current Drug Targets | Ginkgo biloba extract (EGb 761) and CNS functions: basic studies and clinical applications | doi:10.2174/1389450003349380 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: Regarding EGb 761-induced regulation of cerebral glucose utilization, bilobalide increases the respiratory control ratio of mitochondria by protecting against uncoupling of oxidative phosphorylation, thereby increasing ATP levels, a result that is supported by the finding that bilobalide increases the expression of the mitochondrial DNA-encoded COX III subunit of cytochrome oxidase. With regard to its "anti-stress" e
  REF-2185 [meta-analysis] 2022 Cells | Can we use Ginkgo biloba extract to treat Alzheimer's disease? Lessons from preclinical and clinical studies | doi:10.3390/cells11030479 
     used: A:neuroprotective, D:cognitive-function, D:memory
     C: GBE displayed generally consistent anti-AD effects in animal experiments, and it might improve AD symptoms in early-stage AD patients after high doses and long-term administration. A lack of sample size calculations and the poor quality of the methods are two obvious limitations of the studies. Nevertheless, the preclinical and clinical data suggest that further large-scale clinical trials may be needed in order to e
  REF-2186 [meta-analysis] 2015 World Journal of Biological Psychiatry | Efficacy of Ginkgo biloba extract EGb 761 in dementia with behavioural and psychological symptoms: a systematic review | doi:10.3109/15622975.2015.1066513 
     used: A:neuroprotective, D:cognitive-function, D:memory
     C: The pooled analyses provide evidence of efficacy of EGb 761 ® at a daily dose of 240 mg in the treatment of out-patients suffering from Alzheimer's, vascular or mixed dementia with BPSD.

## glycyrrhiza-glabra - Glycyrrhiza glabra - Licorice root, liquorice, sweet root
actions: anti-inflammatory=['REF-0012', 'REF-0089', 'REF-0308', 'REF-2187', 'REF-0826', 'REF-0828', 'REF-2192', 'REF-2194']; antimicrobial=['REF-0012', 'REF-0089', 'REF-0308', 'REF-2191']; antispasmodic=['REF-0012', 'REF-0089', 'REF-0308']; antiviral=['REF-0012', 'REF-0089', 'REF-0308']; expectorant=['REF-0012', 'REF-0089', 'REF-0308']; gastroprotective=['REF-0012', 'REF-0089', 'REF-0308']; immunomodulator=['REF-0012', 'REF-0089', 'REF-0308']
- **acid-reflux** [needs-review,ev1] !INF note="inferred from gastroprotective action"
    D=['REF-3081'] N=[] X=['REF-0012', 'REF-0089', 'REF-0308'] M=[]
- **arthritis** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0308'] N=[] X=['REF-0012', 'REF-0089'] M=['REF-2187<anti-inflammatory', 'REF-0826<anti-inflammatory', 'REF-0828<anti-inflammatory', 'REF-2192<anti-inflammatory', 'REF-2194<anti-inflammatory']
- **bronchitis** [needs-review,ev1] !INF note="inferred from expectorant action"
    D=['REF-0308'] N=[] X=['REF-0012', 'REF-0089'] M=[]
- **cold** [needs-review,ev1] !INF note="inferred from antiviral action"
    D=['REF-3081'] N=[] X=['REF-0012', 'REF-0089', 'REF-0308'] M=[]
- **cough** [needs-review,ev1] !INF note="inferred from expectorant action"
    D=['REF-0308', 'REF-3081'] N=[] X=['REF-0012', 'REF-0089'] M=[]
- **indigestion** [needs-review,ev1] !INF note="inferred from gastroprotective action"
    D=['REF-0308', 'REF-3081'] N=[] X=['REF-0012', 'REF-0089'] M=[]
- **infection** [needs-review,ev1] !INF note="inferred from antimicrobial action"
    D=['REF-0308'] N=[] X=['REF-0012', 'REF-0089'] M=['REF-2191<antimicrobial']
- **inflammation** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0308'] N=[] X=['REF-0012', 'REF-0089'] M=['REF-2187<anti-inflammatory', 'REF-0826<anti-inflammatory', 'REF-0828<anti-inflammatory', 'REF-2192<anti-inflammatory', 'REF-2194<anti-inflammatory']
- **respiratory-support** [needs-review,ev1] !INF note="inferred from expectorant action"
    D=['REF-0308', 'REF-3081'] N=[] X=['REF-0012', 'REF-0089'] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0012', 'REF-0089', 'REF-0308'] M=['REF-2187<anti-inflammatory', 'REF-0826<anti-inflammatory', 'REF-0828<anti-inflammatory', 'REF-2192<anti-inflammatory', 'REF-2194<anti-inflammatory']
  REF-0012 [narrative-review] 2008 Phytotherapy Research | Review of pharmacological effects of Glycyrrhiza sp. | pmid:18446848 doi:10.1002/ptr.2362 
     used: A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:antiviral, A:expectorant, A:gastroprotective, A:immunomodulator
     C: A large number of components have been isolated from licorice, including triterpene saponins, flavonoids, isoflavonoids and chalcones, with glycyrrhizic acid normally being considered to be the main biologically active component. This review summarizes the phytochemical, pharmacological and pharmacokinetics data, together with the clinical and adverse effects of licorice and its bioactive components.
  REF-0089 [narrative-review] 2005 Journal of Ethnopharmacology | A history of the therapeutic use of liquorice in Europe | doi:10.1016/j.jep.2005.04.015 
     used: A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:antiviral, A:expectorant, A:gastroprotective, A:immunomodulator
     C: In the second part, the historical records of diseases treated with liquorice have been presented. Finally, a comparison between traditional use in and outside Europe, with the most important recent scientific studies concerning its use, is presented.
  REF-0308 [traditional] 1999  | WHO Monographs on Selected Medicinal Plants, Volume 1 | NO-ID 
     used: A:anti-inflammatory, A:antimicrobial, A:antispasmodic, A:antiviral, A:expectorant, A:gastroprotective, A:immunomodulator, D:arthritis, D:bronchitis, D:cough, D:indigestion, D:infection, D:inflammation, D:respiratory-support
     (no abstract)
  REF-0826 [traditional] 2018 Phytotherapy Research | Liquorice (Glycyrrhiza glabra): A phytochemical and pharmacological review | doi:10.1002/ptr.6178 !TAG review-title/traditional
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: This review addresses all those issues and focuses on the pharmacological activities reported for G. glabra. Therefore, an updated, critical, and extensive overview on the current knowledge of G. glabra composition and biological activities is provided here in order to explore its therapeutic potential and future challenges to be utilized for the formulation of new products that will contribute to human well-being.
  REF-0828 [traditional] 2020 Biomolecules | Traditional Uses, Bioactive Chemical Constituents, and Pharmacological and Toxicological Activities of Glycyrrhiza glabra L. (Fabaceae) | doi:10.3390/biom10030352 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Additionally, it shows antioxidant, antifungal, anticarcinogenic, anti-inflammatory, and cytotoxic activities. The current review examined the phytochemical composition, pharmacological activities, pharmacokinetics, and toxic activities of G. glabra extracts as well as its phytoconstituents.
  REF-2187 [narrative-review] 2021 Plants | Glycyrrhiza glabra (licorice): a comprehensive review on its phytochemistry, biological activities, clinical evidence and toxicology | doi:10.3390/plants10122751 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Licorice could be a natural alternative for current therapy to exterminate new emerging disorders with mild side effects. This review will provide systematic insights into this ancient drug for further development and clinical use.
  REF-2191 [preclinical] 2015 Current Topics in Medicinal Chemistry | Anti-tubercular agents from Glycyrrhiza glabra | doi:10.2174/1568026615666150317223323 
     used: A:antimicrobial, M:infection
     C: This is the first ever report on the anti-tubercular potential of GA and its derivatives. These results may be of great help in anti-tubercular drug development from a very common, inexpensive, and non toxic natural product.
  REF-2192 [preclinical] 2019 Antioxidants | Antioxidant and anti-inflammatory activities of flavanones from Glycyrrhiza glabra L. (licorice) leaf phytocomplexes: identification of licoflavanone  | doi:10.3390/antiox8060186 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Interestingly, licoflavanone markedly decreased pro-inflammatory cytokines and cyclooxygenase 2/inducible nitric oxide synthase (COX-2/iNOS) expression levels ( p < 0.001). A modulation of nuclear factor kappa B/mitogen-activated protein kinases (NF-kB/MAPK) pathway underlay such behavior, highlighting the potential of this natural compound as a new scaffold in anti-inflammatory drug research.
  REF-2194 [narrative-review] 2016 Pakistan Journal of Pharmaceutical Scien | Review - Glycyrrhiza glabra L. (liquorice) | NO-ID 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Plant requires a lot of attention as it has been reduced in population due to over-use in Baluchistan. The plant conservationists should consider this herb as priority species and should start its cultivation on the commercial scale to fulfill the requirements of the local markets and pharmaceutical industries as well as reduce the pressure on the wild plants.
  REF-3081 [traditional] 2013  | Community herbal monograph on Glycyrrhiza glabra L. and/or Glycyrrhiza inflata Bat. and/or Glycyrrhiza uralensis Fisch., radix | NO-ID 
     used: D:acid-reflux, D:cold, D:cough, D:indigestion, D:respiratory-support
     (no abstract)

## gymnema-sylvestre - Gymnema sylvestre - Gymnema, Gurmar, Australian Cowplant
actions: antidiabetic=['REF-2465', 'REF-2466', 'REF-2467', 'REF-2469', 'REF-2540', 'REF-2541', 'REF-2542', 'REF-2543', 'REF-3060']; lipid-lowering=['REF-2466', 'REF-2541', 'REF-3059']
- **blood-sugar** [verified,ev10] note=""
    D=['REF-2465', 'REF-2466', 'REF-2467', 'REF-2540', 'REF-2541', 'REF-2542', 'REF-3060'] N=[] X=['REF-2543'] M=['REF-2469<antidiabetic']
- **metabolic-support** [needs-review,ev7] !INF note="inferred from antidiabetic action"
    D=['REF-2465', 'REF-2466', 'REF-2542'] N=[] X=[] M=['REF-2467<antidiabetic', 'REF-2469<antidiabetic', 'REF-2540<antidiabetic', 'REF-2541<antidiabetic', 'REF-2543<antidiabetic', 'REF-3060<antidiabetic']
- **high-cholesterol** [needs-review,ev8] !INF note="inferred from lipid-lowering action"
    D=['REF-2466', 'REF-2541', 'REF-3059'] N=[] X=[] M=[]
  REF-2465 [clinical] 1990 Journal of Ethnopharmacology | Antidiabetic effect of a leaf extract from Gymnema sylvestre in non-insulin-dependent diabetes mellitus patients | doi:10.1016/0378-8741(90)90108-6 
     used: A:antidiabetic, D:blood-sugar, D:metabolic-support
     C: These data suggest that the beta cells may be regenerated/repaired in Type 2 diabetic patients on GS4 supplementation. This is supported by the appearance of raised insulin levels in the serum of patients after GS4 supplementation.
  REF-2466 [clinical] 2010 Journal of Dietary Supplements | An open label study on the supplementation of Gymnema sylvestre in type 2 diabetics | doi:10.3109/19390211.2010.505901 
     used: A:antidiabetic, A:lipid-lowering, D:blood-sugar, D:high-cholesterol, D:metabolic-support
     C: Supplementation of the diet with GS reduced polyphagia, fatigue, blood glucose (fasting and post-prandial), and glycated hemoglobin and there was a favorable shift in lipid profiles and in other clinico-biochemical tests. These findings suggest a beneficial effect of GS in the management of diabetes mellitus.
  REF-2467 [narrative-review] 2018 Phytotherapy Research | Enzymes inhibitors from natural sources with antidiabetic activity: A review | doi:10.1002/ptr.6211 
     used: A:antidiabetic, D:blood-sugar, M:metabolic-support
     C: Some of the group of phytochemicals isolated with enzyme inhibition activities are Alkaloids, sesquiterpene and saponins, polysaccharides, flavonoids, dietary fibers, ferulic acid, tannins, limonene, and oleuropeoside. This review will provide very useful material to enhance the efficiency of rational antidiabetic drug design.
  REF-2469 [narrative-review] 2012 Journal of Pharmacy and Bioallied Scienc | A pharmacological appraisal of medicinal plants with antidiabetic potential | doi:10.4103/0975-7406.92727 
     used: A:antidiabetic, M:blood-sugar, M:metabolic-support
     C: These include Allium sativa, Eugenia jambolana, Panax ginseng, Gymnema sylvestre, Momrodica charantia, Ocimum sanctum, Phyllanthus amarus, Pterocarpus marsupium, Trigonella foenum graecum and Tinospora cordifolia. All of them have shown a certain degree of antidiabetic activity by different mechanisms of action.
  REF-2540 [meta-analysis] 2021 Phytotherapy Research | The effect of Gymnema sylvestre supplementation on glycemic control in type 2 diabetes patients: A systematic review and meta-analysis | doi:10.1002/ptr.7265 
     used: A:antidiabetic, D:blood-sugar, M:metabolic-support
     C: Further, our study also found that GS significantly reduces triglycerides (SMD 1.81 mg/dl, 95% CI 2.95 to -0.66, p < .0001, I 2 : 96%), and total cholesterol (SMD 4.10 mg/dl, 95% CI 7.21 to -0.99, p < .0001, I 2 : 98%) compared to baseline. Our study shows that GS supplementation is effective in improving glycemic control and reducing lipid levels in T2DM patients and suggests that such supplementation might be used 
  REF-2541 [meta-analysis] 2022 Phytotherapy Research | The effects of Gymnema Sylvestre supplementation on lipid profile, glycemic control, blood pressure, and anthropometric indices in adults: A systemati | doi:10.1002/ptr.7585 
     used: A:antidiabetic, A:lipid-lowering, D:blood-sugar, D:high-cholesterol, M:metabolic-support
     C: Our outcomes suggest that GS supplementation may improve cardiovascular risk factors. Future large-high-quality RCTs with longer duration and various populations are needed to firmly establish the clinical efficacy of the plant.
  REF-2542 [rct] 2024 Nutrients | Comparative Effects of Gymnema sylvestre and Berberine on Adipokines, Body Composition, and Metabolic Parameters in Obese Patients: A Randomized Study | doi:10.3390/nu16142284 
     used: A:antidiabetic, D:blood-sugar, D:metabolic-support
     C: In patients with obesity, BBR has a better effect on body composition, blood pressure, and the gene expression of adipokines related to metabolic risk, while GS has a better effect on fasting glucose and adipokines related to insulin resistance, with minimal side effects.
  REF-2543 [rct] 2022 Nutrients | The Effect of a 14-Day Gymnema sylvestre Intervention to Reduce Sugar Cravings in Adults | doi:10.3390/nu14245287 
     used: A:antidiabetic, M:metabolic-support
     C: There was no habituation to the mint over the 14-day period. This study is the first to investigate the effect of longer-term gymnema acid consumption on sweet food consumption outside of a laboratory setting; further research is needed to assess how long the effect of the 14-day intervention persists.
     !NULL: 02); there were no differences between groups at day 15 (INT = 2.
     !NULL: No differences were found in the intake of 9 food categories between groups at any timepoint.
     !NULL: There were no differences in consumption of low sugar healthy foods between visits, or by group.
  REF-3059 [narrative-review] 2014 BioMed Research International | Phytochemical and pharmacological properties of Gymnema sylvestre: an important medicinal plant | doi:10.1155/2014/830285 
     used: A:lipid-lowering, D:high-cholesterol
     C: The herbal extract is used in dietary supplements since it reduces body weight, blood cholesterol, and triglyceride levels and holds great prospects in dietary as well as pharmacological applications. This review explores the transition of a traditional therapeutic to a modern contemporary medication with an overview of phytochemistry and pharmacological activities of the herb and its phytoconstituents.
  REF-3060 [systematic-review] 2007 Journal of Alternative and Complementary | Gymnema sylvestre for diabetes mellitus: a systematic review | pmid:18047444 doi:10.1089/acm.2006.6387 
     used: A:antidiabetic, D:blood-sugar, M:metabolic-support
     C: In order to answer this question, a systematic review of the literature and a discussion of the best available evidence on gymnema are needed. The findings of such a review are presented in this paper.

## hamamelis-virginiana - Hamamelis virginiana - Witch Hazel, Common witch hazel, Winterbloom
actions: anti-inflammatory=['REF-0531', 'REF-0532', 'REF-0533', 'REF-2049', 'REF-0831', 'REF-2050', 'REF-2051']; anticancer=['REF-2056']; antioxidant=['REF-0532', 'REF-0831']; astringent=['REF-0531', 'REF-0532', 'REF-0533', 'REF-2051']; vulnerary=['REF-0531', 'REF-0533', 'REF-2052']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0531', 'REF-0532', 'REF-0831', 'REF-2049', 'REF-2050', 'REF-0533'] M=['REF-2051<anti-inflammatory']
- **bruising** [verified,ev1] note="Vulnerary for minor wounds, bruises and insect bites"
    D=['REF-0533'] N=[] X=['REF-0531'] M=['REF-2052<vulnerary']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2056'] N=[] X=[] M=[]
- **diarrhea** [needs-review,ev1] !INF note="inferred from astringent action"
    D=['REF-0533'] N=[] X=['REF-0531', 'REF-0532', 'REF-2051'] M=[]
- **hemorrhoids** [verified,ev1] note="Relief of haemorrhoid symptoms (astringent and anti-inflammatory)"
    D=['REF-0531', 'REF-0533'] N=[] X=[] M=[]
- **inflammation** [verified,ev2] note="Astringent for skin irritation and minor inflammation of the skin and oral mucosa (tannins), applied topically"
    D=['REF-0531', 'REF-0532'] N=[] X=[] M=['REF-0533<anti-inflammatory', 'REF-2049<anti-inflammatory', 'REF-0831<anti-inflammatory', 'REF-2050<anti-inflammatory', 'REF-2051<anti-inflammatory']
- **oral-health** [verified,ev1] note="Astringent for skin irritation and minor inflammation of the skin and oral mucosa (tannins), applied topically"
    D=['REF-0531'] N=[] X=[] M=[]
- **skin-irritation** [verified,ev2] note="Astringent for skin irritation and minor inflammation of the skin and oral mucosa (tannins), applied topically"
    D=['REF-0531', 'REF-0532'] N=[] X=[] M=['REF-0533<anti-inflammatory', 'REF-2049<anti-inflammatory', 'REF-0831<anti-inflammatory', 'REF-2050<anti-inflammatory', 'REF-2051<anti-inflammatory', 'REF-0533<astringent', 'REF-2051<astringent']
- **wounds** [verified,ev2] note="Vulnerary for minor wounds, bruises and insect bites"
    D=['REF-0533', 'REF-0532'] N=[] X=['REF-2051', 'REF-0531'] M=['REF-2052<vulnerary']
  REF-0531 [traditional] n.d.  | European Union herbal monograph on Hamamelis virginiana L., cortex/folium/aqua (Hamamelidis cortex) | NO-ID 
     used: A:anti-inflammatory, A:astringent, A:vulnerary, D:hemorrhoids, D:inflammation, D:oral-health, D:skin-irritation
     (no abstract)
  REF-0532 [narrative-review] 2025 Molecules | Hamamelis virginiana L. in Skin Care: A Review of Its Pharmacological Properties and Cosmetological Applications | doi:10.3390/molecules30132744 
     used: A:anti-inflammatory, A:antioxidant, A:astringent, D:inflammation, D:skin-irritation, D:wounds
     C: Moreover, the extracts exert anti-inflammatory effects by modulating cytokine expression and NF-κB signaling, improve skin regeneration, and protect against UV-induced damage and pollution. This review highlights H. virginiana as a complex botanical resource to be used in dermatology and cosmetology and shows that current research offers encouraging results for its future therapeutic use, especially in skin treatment
  REF-0533 [traditional] n.d.  | Witch Hazel (Hamamelis virginiana): Benefits, Safety, Uses | NO-ID 
     used: A:anti-inflammatory, A:astringent, A:vulnerary, D:bruising, D:diarrhea, D:hemorrhoids, D:wounds, M:inflammation, M:skin-irritation
     (no abstract)
  REF-0831 [preclinical] 2022 Antioxidants (Basel) | Anti-Inflammatory and Anti-Acne Effects of Hamamelis virginiana Bark in Human Keratinocytes | doi:10.3390/antiox11061119 
     used: A:anti-inflammatory, A:antioxidant, M:inflammation, M:skin-irritation
     C: The effects of HVE are primarily based on the proanthocyanidin content, as HT was found inactive on all the parameters tested. These results suggest further investigations of HVE in other inflammatory-based skin diseases.
  REF-2049 [preclinical] 2022 International Journal of Molecular Scien | Unveiling the Ability of Witch Hazel (Hamamelis virginiana L.) Bark Extract to Impair Keratinocyte Inflammatory Cascade Typical of Atopic Eczema | doi:10.3390/ijms23169279 
     used: A:anti-inflammatory, M:inflammation, M:skin-irritation
     C: Notably, HT showed activity on well-known targets of IL-4 pathway (CCL26, K10, cell proliferation). To the best of our knowledge, this work represents the first demonstration of the potential role of Hamamelis virginiana in the control of AD symptoms, such as itch and skin barrier impairment, supporting the relevance of the whole phytocomplex.
  REF-2050 [preclinical] 2024 Anais da Academia Brasileira de Ciencias | Hamamelis virginiana L. extract presents antimicrobial and antibiofilm effects, absence of cytotoxicity, anti-inflammatory action, and potential to fi | doi:10.1590/0001-3765202320200031 
     used: A:anti-inflammatory, M:inflammation, M:skin-irritation
     C: NO production was similar or higher than the control group. Thus, H. virginiana L. extract showed antimicrobial and antibiofilm effects; absence of cytotoxicity for RAW 264.7; anti-inflammatory action; and potential to fight infections through the NO production.
  REF-2051 [preclinical] 2002 Toxicon | Hamamelitannin from Hamamelis virginiana inhibits the tumour necrosis factor-alpha (TNF)-induced endothelial cell death in vitro | doi:10.1016/s0041-0101(01)00195-7 
     used: A:anti-inflammatory, A:astringent, M:arthritis, M:inflammation, M:skin-irritation
     C: Thus, hamamelitannin inhibits the TNF-mediated endothelial cell death without altering the TNF-induced upregulation of endothelial adhesiveness. The observed anti-TNF activity of hamamelitannin may explain the antihamorrhaegic use of H. virginiana in traditional medicine and its claimed use as a protective agent for UV radiation.
     !NULL: Concentrations (1-100 microM) of hamamelitannin that inhibited the TNF-mediated cell death and DNA fragmentation, however, failed to inhibit the TNF-induced ICAM-1 expression and EAhy926 cell adhesiveness to U937 cells.
  REF-2052 [rct] 2021 Frontiers in Pharmacology | Human Metabolites of Hamamelis virginiana (Extract) Modulate Fibroblast Extracellular Matrix Components in Response to UV-A Irradiation | doi:10.3389/fphar.2021.747638 
     used: A:vulnerary, M:bruising, M:wounds
     C: However, the activation of the expression of 10 different genes involved in repair processes for the maintenance of skin integrity, suggest that the metabolites can play a role in damage recovery. To our knowledge, this is the first study that demonstrates the bioavailability of Hamaforton™ phenolic compounds, and the effects of its metabolites on cultured dermal fibroblast response to ultraviolet A irradiation.
     !NULL: While, ultraviolet A irradiation of dermal fibroblasts affected the expression of extracellular matrix genes, the presence of Hamaforton™ metabolites in the culture media did not affect the expression of most of those genes.
  REF-2056 [preclinical] 2012 Journal of Natural Products | Hamamelitannin from witch hazel (Hamamelis virginiana) displays specific cytotoxic activity against colon cancer cells | doi:10.1021/np200426k 
     used: A:anticancer, D:cancer
     C: Furthermore, at concentrations that inhibit the growth of HT29 cells by 50%, hamamelitannin had no harmful effects on NCM460 normal colonocytes, whereas pentagalloylglucose inhibited both cancerous and normal cell growth. Using the TNPTM assay, we identified a highly reactive phenolic position in hamamelitannin, which may explain its efficacy at inhibiting colon cancer growth.

## harpagophytum-procumbens - Harpagophytum procumbens - Devil's Claw, Grapple plant, Wood spider
actions: analgesic=['REF-0443', 'REF-0444', 'REF-1829', 'REF-1830', 'REF-1832', 'REF-1834', 'REF-1835', 'REF-1837', 'REF-1838']; anti-inflammatory=['REF-0443', 'REF-0444', 'REF-1829', 'REF-1831', 'REF-1832', 'REF-1833', 'REF-1834', 'REF-1836', 'REF-1837', 'REF-1839']
- **arthritis** [verified,ev7] note="Anti-inflammatory and analgesic for osteoarthritis (hip and knee) pain; General joint pain and arthritis support"
    D=['REF-0444', 'REF-0561'] N=['REF-1834'] X=['REF-1836', 'REF-0443'] M=['REF-1829<anti-inflammatory', 'REF-1831<anti-inflammatory', 'REF-1832<anti-inflammatory', 'REF-1833<anti-inflammatory', 'REF-1837<anti-inflammatory', 'REF-1839<anti-inflammatory']
- **back-pain** [verified,ev7] note="Effective at standardised doses (~50-60 mg harpagoside/day); an aqueous extract was non-inferior to rofecoxib for short-term chronic low back pain; Relief of chronic non-specific low back pain"
    D=['REF-0444', 'REF-0561', 'REF-0562'] N=[] X=['REF-1830', 'REF-1834', 'REF-1835', 'REF-1838', 'REF-0443'] M=['REF-1829<analgesic', 'REF-1832<analgesic', 'REF-1837<analgesic']
- **headache** [needs-review,ev1] note="inferred from analgesic action"
    D=[] N=[] X=['REF-0444', 'REF-1830', 'REF-1834', 'REF-1835', 'REF-1838', 'REF-0443'] M=['REF-1829<analgesic', 'REF-1832<analgesic', 'REF-1837<analgesic']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0443', 'REF-0444'] M=['REF-1829<anti-inflammatory', 'REF-1831<anti-inflammatory', 'REF-1832<anti-inflammatory', 'REF-1833<anti-inflammatory', 'REF-1834<anti-inflammatory', 'REF-1836<anti-inflammatory', 'REF-1837<anti-inflammatory', 'REF-1839<anti-inflammatory']
- **pain** [verified,ev7] note="Anti-inflammatory and analgesic for osteoarthritis (hip and knee) pain; Effective at standardised doses (~50-60 mg harpagoside/day); an aqueous extract was non-inferior to rofecoxib for short-term chronic low back pain; General joint pain and arthritis support; Relief of chronic non-specific low back pain"
    D=['REF-0444', 'REF-0561', 'REF-0562'] N=[] X=['REF-0443'] M=['REF-1829<analgesic', 'REF-1830<analgesic', 'REF-1832<analgesic', 'REF-1834<analgesic', 'REF-1835<analgesic', 'REF-1837<analgesic', 'REF-1838<analgesic']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0444', 'REF-1831', 'REF-1834', 'REF-1836', 'REF-0443'] M=['REF-1829<anti-inflammatory', 'REF-1832<anti-inflammatory', 'REF-1833<anti-inflammatory', 'REF-1837<anti-inflammatory', 'REF-1839<anti-inflammatory']
  REF-0443 [systematic-review] 2006 Journal of Herbal Pharmacotherapy | Devil's Claw (Harpagophytum procumbens DC): an evidence-based systematic review by the Natural Standard Research Collaboration | doi:10.1080/j157v06n01_09 
     used: A:analgesic, A:anti-inflammatory
     C: An evidence-based systematic review including written and statistical analysis of scientific literature, expert opinion, folkloric precedent, history, pharmacology, kinetics/dynamics, interaction, adverse effects, toxicology, and dosing.
  REF-0444 [narrative-review] 2004 Der Orthopade | Devil's claw extract as an example of the effectiveness of herbal analgesics | doi:10.1007/s00132-004-0675-7 
     used: A:analgesic, A:anti-inflammatory, D:arthritis, D:back-pain, D:pain
     C: From an evidence based view, extract with at least 50 mg harpagoside in the daily dose should be recommended for the treatment of pain. Treatment with devil's claw extract is associated with a lower risk of adverse events than treatment with synthetic analgesics, and may contribute in the majority of patients to the relief of pain.
  REF-0561 [systematic-review] 2004 BMC Complementary and Alternative Medici | Harpagophytum procumbens for osteoarthritis and low back pain: a systematic review | doi:10.1186/1472-6882-4-13 
     used: D:arthritis, D:back-pain, D:pain
     C: There is limited evidence for an ethanolic Harpagophytum extract containing less than <30 mg harpagoside per day in the treatment of knee and hip osteoarthritis. There is moderate evidence of effectiveness for (1) the use of a Harpagophytum powder at 60 mg harpagoside in the treatment of osteoarthritis of the spine, hip and knee; (2) the use of an aqueous Harpagophytum extract at a daily dose of 100 mg harpagoside in
     !NULL: Conclusions There is limited evidence for an ethanolic Harpagophytum extract containing less than <30 mg harpagoside per day in the treatment of knee and hip osteoarthritis.
  REF-0562 [narrative-review] 2004 Phytotherapy Research | Effectiveness of Harpagophytum extracts and clinical efficacy | doi:10.1002/ptr.1416 
     used: D:back-pain, D:pain
     C: The studies offering preparations with 50-60 mg harpagoside in the daily dosage are of better quality and provide more reliable evidence on efficacy than a proprietary ethanol extract with half the amount of harpagoside per day. However, confirmatory studies are required for all extracts before they can gain a place in treatment guidelines.
  REF-1829 [narrative-review] 2012 Journal of Ethnopharmacology | Devil's Claw - a review of the ethnobotany, phytochemistry and biological activity of Harpagophytum procumbens | doi:10.1016/j.jep.2012.08.013 
     used: A:analgesic, A:anti-inflammatory, M:arthritis, M:back-pain, M:headache, M:inflammation, M:pain, M:skin-irritation
     C: Harpagophytum procumbens is used to treat a wide range of ailments. Some of the ethnobotanical claims have been confirmed through in vitro studies, however, when the constituents deemed to be the biologically active compounds were isolated the efficacy was lower than that of the whole extract. This necessitates the use of a different approach where all the metabolites are considered using a robust method such as spec
  REF-1830 [preclinical] 2015 Natural Product Research | Harpagophytum procumbens extract potentiates morphine antinociception in neuropathic rats | doi:10.1080/14786419.2015.1052069 
     used: A:analgesic, M:pain
     C: H. procumbens cooperates synergistically with morphine in resolving hyperalgesia and allodynia, two typical symptoms of neuropathic pain. The results support the strategy of using an adjuvant drug to improve opioid analgesic efficacy.
  REF-1831 [preclinical] 2022 Pharmaceuticals | Harpagophytum procumbens Root Extract Mediates Anti-Inflammatory Effects in Osteoarthritis Synoviocytes through CB2 Activation | doi:10.3390/ph15040457 
     used: A:anti-inflammatory, M:arthritis, M:inflammation
     C: Pure compounds were less effective than the whole phytocomplex, thus suggesting the involvement of synergistic interactions. Present findings encourage further mechanistic studies and support the scientific basis of the use of H. procumbens in joint disorders.
  REF-1832 [narrative-review] 2022 Molecules | The Fight against Infection and Pain: Devil's Claw (Harpagophytum procumbens) a Rich Source of Anti-Inflammatory Activity: 2011-2022 | doi:10.3390/molecules27113637 
     used: A:analgesic, A:anti-inflammatory, M:arthritis, M:back-pain, M:headache, M:inflammation, M:pain, M:skin-irritation
     C: Based on the literature results, there was a dramatic decrease in the number of studies conducted on the anti-inflammatory and analgesic activity of Devil's claw, thereby presenting a potential research gap. It is also evident that currently in vivo clinical studies are needed to validate the prior massive in vitro studies, therefore delivering an ideal anti-inflammatory and analgesic agent in the form of H. procumbe
  REF-1833 [narrative-review] 2019 Phytotherapy Research | Devil's claw (Harpagophytum procumbens) and chronic inflammatory diseases: A concise overview on preclinical and clinical data | doi:10.1002/ptr.6395 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: However, harpagoside is the most responsible for therapeutic activity, and its content is used as reference standard. Here, we analyzed and summarized preclinical and clinical studies focusing on therapeutic efficacy of devil's claw preparations in pathological conditions in which inflammation plays a key causative role.
  REF-1834 [systematic-review] 2006 Journal of Alternative and Complementary | Devil's Claw (Harpagophytum procumbens) as a treatment for osteoarthritis: a review of efficacy and safety | doi:10.1089/acm.2006.12.981 
     used: A:analgesic, A:anti-inflammatory, M:inflammation, M:pain, N:arthritis
     C: The methodological quality of the existing clinical trials is generally poor, and although they provide some support, there are a considerable number of methodologic caveats that make further clinical investigations warranted. The clinical evidence to date cannot provide a definitive answer to the two questions posed: (1) Does it work? And (2) is it safe? A definitive high-quality trial that addresses the necessary m
  REF-1835 [preclinical] 2020 Neuromolecular Medicine | Harpagophytum procumbens Extract Ameliorates Allodynia and Modulates Oxidative and Antioxidant Stress Pathways in a Rat Model of Spinal Cord Injury | doi:10.1007/s12017-019-08585-z 
     used: A:analgesic, M:pain
     C: Concurrent studies of cultured murine BV-2 microglial cells revealed that Hp suppressed oxidative/nitrosative stress and inflammatory responses, including production of nitric oxide and reactive oxygen species, phosphorylation of cytosolic phospholipases A 2 , and upregulation of the antioxidative stress pathway involving the nuclear factor erythroid 2-related factor 2 and HO-1. These results support the use of Hp fo
  REF-1836 [preclinical] 2020 Antioxidants | Multidirectional Pharma-Toxicological Study on Harpagophytum procumbens DC. ex Meisn.: An IBD-Focused Investigation | doi:10.3390/antiox9020168 
     used: A:anti-inflammatory, M:inflammation
     C: The extract was also able to exert a pro-homeostatic effect on the levels of a wide plethora of colon proteins, thus corroborating a protective effect. Conversely, the supraphysiological downregulation of cytoskeletal-related proteins involved in tissue morphology and antimicrobial barrier function suggests a warning in the use of food supplements containing H. procumbens extracts.
  REF-1837 [preclinical] 1997 Planta Medica | An analytical study, anti-inflammatory and analgesic effects of Harpagophytum procumbens and Harpagophytum zeyheri | doi:10.1055/s-2006-957638 
     used: A:analgesic, A:anti-inflammatory, M:arthritis, M:back-pain, M:headache, M:inflammation, M:pain, M:skin-irritation
     C: The aqueous extracts of both drugs show similar analgesic and anti-inflammatory properties. Harpagophytum procumbens and Harpagophytum zeyheri should be accepted as sources for the drug Harpagophyti radix.
  REF-1838 [preclinical] 2014 Molecules | Analgesic effect of Harpagophytum procumbens on postoperative and neuropathic pain in rats | doi:10.3390/molecules19011060 
     used: A:analgesic, M:pain
     C: After 21 days of continuous treatment with H. procumbens extracts at 300 mg/kg, the treated group showed significantly alleviated SNI-induced hypersensitivity responses by MWT, compared with the control group. These results suggest that H. procumbens extracts have potential analgesic effects in the case of acute postoperative pain and chronic neuropathic pain in rats.
  REF-1839 [preclinical] 2003 Journal of Pharmacological Sciences | Harpagophytum procumbens suppresses lipopolysaccharide-stimulated expressions of cyclooxygenase-2 and inducible nitric oxide synthase in fibroblast ce | doi:10.1254/jphs.93.367 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The aqueous extract of Harpagophytum procumbens was shown to suppress PGE(2) synthesis and nitric oxide production by inhibiting lipopolysaccharide-stimulated enhancement of the cyclooxygenase-2 and inducible nitric oxide synthase (iNOS) mRNAs expressions in L929 cells. These results suggest that Harpagophytum procumbens exerts anti-inflammatory and analgesic effects probably by suppressing cyclooxygenase-2 and iNOS 

## hedera-helix - Hedera helix - Ivy Leaf, Common ivy, English ivy
actions: antispasmodic=['REF-0472', 'REF-2309', 'REF-2311', 'REF-2314']; bronchodilator=['REF-0472', 'REF-2309']; expectorant=['REF-0472', 'REF-0473', 'REF-0575', 'REF-0834', 'REF-0833', 'REF-0835']
- **asthma** [needs-review,ev1] note="inferred from bronchodilator action"
    D=[] N=[] X=['REF-0472'] M=['REF-2309<bronchodilator']
- **bronchitis** [verified,ev7] note="Expectorant / secretolytic for productive cough and acute bronchitis (loosens and helps clear mucus)"
    D=['REF-0472', 'REF-0473', 'REF-0575'] N=['REF-0833'] X=[] M=['REF-0834<expectorant', 'REF-0835<expectorant']
- **cough** [verified,ev7] note="Expectorant / secretolytic for productive cough and acute bronchitis (loosens and helps clear mucus)"
    D=['REF-0472', 'REF-0473', 'REF-0575'] N=['REF-0833'] X=[] M=['REF-2309<bronchodilator', 'REF-0834<expectorant', 'REF-0835<expectorant']
- **menstrual-cramps** [needs-review,ev1] note="inferred from antispasmodic action"
    D=[] N=[] X=['REF-0472'] M=['REF-2309<antispasmodic', 'REF-2311<antispasmodic', 'REF-2314<antispasmodic']
- **muscle-spasm** [needs-review,ev1] note="inferred from antispasmodic action"
    D=[] N=[] X=['REF-0472'] M=['REF-2309<antispasmodic', 'REF-2311<antispasmodic', 'REF-2314<antispasmodic']
- **respiratory-support** [needs-review,ev7] !INF note="inferred from expectorant action"
    D=['REF-0472', 'REF-0473', 'REF-0575'] N=['REF-0833'] X=[] M=['REF-0834<expectorant', 'REF-0835<expectorant']
  REF-0472 [clinical] 2020 Evidence-Based Complementary and Alterna | Assessment of the Efficacy and Safety of Ivy Leaf Cough Syrup Compared with Acetylcysteine in Adults and Children with Acute Bronchitis | doi:10.1155/2020/1910656 
     used: A:antispasmodic, A:bronchodilator, A:expectorant, D:bronchitis, D:cough, D:respiratory-support
     C: Observations of the tolerability were comparable for both products. The study results indicate that ivy leaf extract might be an effective alternative to acetylcysteine with respect to the improvement of respiratory function in children and adults at a slightly better evaluation of efficacy.
  REF-0473 [clinical] 2017 Wiadomosci Lekarskie | Efficacy of dry extract of ivy leaves in the treatment of productive cough | NO-ID 
     used: A:expectorant, D:bronchitis, D:cough, D:respiratory-support
     C: The results of this study support the efficacy of Hedussin® prescribed for the treatment of productive cough in the course of respiratory tract infections. Hedussin® was well tolerated by sick children aged 2-12 years.
  REF-0575 [rct] 2016 Die Pharmazie | A randomized, controlled, double-blind, multi-center trial to evaluate the efficacy and safety of a liquid containing ivy leaves dry extract (EA 575)  | doi:10.1691/ph.2016.6712 
     used: A:expectorant, D:bronchitis, D:cough, D:respiratory-support
     C: All adverse events (AEs) in this clinical trial were non-serious, mild or of moderate severity and not drug-related. This clinical trial proved consistent superiority of the ivy leaves cough liquid treatment versus placebo and confirmed the EA 575® preparation to be a safe and efficacious option for the treatment of acute cough.
  REF-0833 [systematic-review] 2021 European Journal of Clinical Pharmacolog | Ivy leaf (Hedera helix) for acute upper respiratory tract infections: an updated systematic review | doi:10.1007/s00228-021-03090-4 
     used: A:expectorant, N:bronchitis, N:cough, N:respiratory-support
     C: Ivy leaf preparations are safe for use in cough due to acute URTIs and bronchitis. However, effects are minimal at best and of uncertain clinical importance.
     !NULL: Non-antibiotic over-the-counter cough medications such as ivy leaf extract are frequently used but their efficacy is uncertain.
     !NULL: However, effects are minimal at best and of uncertain clinical importance.
  REF-0834 [traditional] 2021 Advances in Experimental Medicine and Bi | The Effects of Ivy (Hedera helix) on Respiratory Problems and Cough in Humans: A Review | doi:10.1007/978-3-030-73234-9_23 !TAG review-title/traditional
     used: A:expectorant, M:bronchitis, M:cough, M:respiratory-support
     C: It comes with several formulations, including tablets, liquids, and topical ointments. In this review, we focus on the respiratory effects of tablet and liquid forms of H. helix.
  REF-0835 [preclinical] 2015 Yonsei Medical Journal | Expectorant and antitussive effect of Hedera helix and Rhizoma coptidis extracts mixture | doi:10.3349/ymj.2015.56.3.819 
     used: A:expectorant, M:bronchitis, M:cough, M:respiratory-support
     C: This study provides evidence for antitussive and expectorant effect of a 3:1 mixture of HH and RC, which may be a useful therapeutic option for respiratory diseases.
  REF-2309 [preclinical] 2009 Biochemistry | Alpha-hederin, but not hederacoside C and hederagenin from Hedera helix, affects the binding behavior, dynamics, and regulation of beta-2-adrenergic r | doi:10.1021/bi802036b 
     used: A:antispasmodic, A:bronchodilator, M:asthma, M:cough, M:menstrual-cramps, M:muscle-spasm
     C: Pretreatment of HASM cells with alpha-hederin (1 microM, 24 h) revealed an increased intracellular cAMP level of 13.5 +/- 7.0% under stimulating conditions. Remarkably, structure-related saponins like hederacoside C and hederagenin did not influence either the binding behavior of beta(2)AR or the intracellular cAMP level.
  REF-2311 [preclinical] 1997 Planta Medica | In vitro antispasmodic compounds of the dry extract obtained from Hedera helix | doi:10.1055/s-2006-957627 
     used: A:antispasmodic, M:menstrual-cramps, M:muscle-spasm
     C: In view of their relative high concentration the saponins contribute most to the anti-spasmodic activity, followed by dicaffeoylquinic acids and the flavonol derivatives. The results indicate that the summed PE value of the compounds mentioned is an acceptable agreement with the PE value of the whole extract determined biologically.
  REF-2314 [preclinical] 2011 Journal of Ethnopharmacology | The effect of the whole extract of common ivy (Hedera helix) leaves and selected active substances on the motoric activity of rat isolated stomach str | doi:10.1016/j.jep.2011.01.036 
     used: A:antispasmodic, M:menstrual-cramps, M:muscle-spasm
     C: Eventually, the whole extract of Hedera helix in a dose containing 60 μM of hederacoside C produced a strong contraction which strength was comparable with the reaction generated by acetylcholine. According to the results, it is very likely that α-hederin, but not hederacoside C contributes to the contractile response of isolated stomach corpus and fundus strips to the application of Hedera helix leaves' extract.
     !NULL: The second tested saponin, hederacoside C, did not alter the motility of rat isolated stomach corpus and fundus strips when administered in the concentration up to 100 μM, however, if applied in the concentration of 350 μM it induced a remarkable concentration of smooth muscle.

## hericium-erinaceus - Hericium erinaceus - Lions mane, Lauvas krēpes
actions: anti-inflammatory=['REF-0157', 'REF-0170', 'REF-0642', 'REF-0643', 'REF-2418', 'REF-2421']; anticancer=['REF-0157']; digestive=['REF-0157', 'REF-0170', 'REF-0643', 'REF-0645']; immunomodulator=['REF-0157', 'REF-0170', 'REF-0644', 'REF-2420']; neuroprotective=['REF-0157', 'REF-0170', 'REF-0640', 'REF-0641', 'REF-0642', 'REF-2418', 'REF-2419']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0157', 'REF-0170', 'REF-0642', 'REF-0643'] M=['REF-2418<anti-inflammatory', 'REF-2421<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-0645'] N=[] X=['REF-0157'] M=[]
- **cognitive-function** [needs-review,ev7] !INF note="inferred from neuroprotective action"
    D=['REF-0170', 'REF-0640', 'REF-2419'] N=['REF-0641'] X=['REF-0157', 'REF-0642'] M=['REF-2418<neuroprotective']
- **cold** [needs-review,ev1] note="inferred from immunomodulator action"
    D=[] N=[] X=['REF-0157', 'REF-0170', 'REF-0644'] M=['REF-2420<immunomodulator']
- **immune-support** [verified,ev2] note=""
    D=['REF-0644'] N=[] X=['REF-0157', 'REF-0170'] M=['REF-2420<immunomodulator']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0642', 'REF-0643'] N=[] X=['REF-0157', 'REF-0170'] M=['REF-2418<anti-inflammatory', 'REF-2421<anti-inflammatory']
- **memory** [needs-review,ev6] !INF note="inferred from neuroprotective action"
    D=['REF-0170', 'REF-2419'] N=['REF-0641'] X=['REF-0157', 'REF-0640', 'REF-0642'] M=['REF-2418<neuroprotective']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0157', 'REF-0170', 'REF-0642', 'REF-0643'] M=['REF-2418<anti-inflammatory', 'REF-2421<anti-inflammatory']
  REF-0157 [traditional] 2016  | An experimental research on the anti-gastric-cancer activity of hericenone B extracted from Hericium erinaceus | NO-ID 
     used: A:anti-inflammatory, A:anticancer, A:digestive, A:immunomodulator, A:neuroprotective
     (no abstract)
  REF-0170 [rct] 2009  | Improving effects of the mushroom Yamabushitake (Hericium erinaceus) on mild cognitive impairment: a double-blind placebo-controlled clinical trial | doi:10.1002/ptr.2634 
     used: A:anti-inflammatory, A:digestive, A:immunomodulator, A:neuroprotective, D:cognitive-function, D:memory
     C: Laboratory tests showed no adverse effect of Yamabushitake. The results obtained in this study suggest that Yamabushitake is effective in improving mild cognitive impairment.
  REF-0640 [rct] 2023 Nutrients | The Acute and Chronic Effects of Lion's Mane Mushroom Supplementation on Cognitive Function, Stress and Mood in Young Adults: A Double-Blind, Parallel | doi:10.3390/nu15224842 
     used: A:neuroprotective, D:cognitive-function
     C: The findings tentatively suggest that Hericium erinaceus may improve speed of performance and reduce subjective stress in healthy, young adults. However, null and limited negative findings were also observed. Given the small sample size, these findings should be interpreted with caution. Further investigation in larger sample sizes is crucial, however the findings of this trial offer a promising avenue of interest.
  REF-0641 [rct] 2025 Frontiers in Nutrition | Acute effects of a standardised extract of Hericium erinaceus (Lion's Mane mushroom) on cognition and mood in healthy younger adults: a double-blind r | doi:10.3389/fnut.2025.1405796 
     used: A:neuroprotective, N:cognitive-function, N:memory
     C: In conclusion, acute consumption of H. erinaceus fruiting body did not demonstrate a significant overall improvement in cognitive performance and mood compared to the placebo and any benefits may be task or domain specific. Further investigations should investigate the effects of chronic supplementation of H. erinaceus fruiting body on cognition and mood in healthy younger adults, as well as establish optimal dosage 
     !NULL: Results and discussion The results showed no significant effect of the H.
  REF-0642 [narrative-review] 2023 International Journal of Molecular Scien | Neurotrophic and Neuroprotective Effects of Hericium erinaceus | doi:10.3390/ijms242115960 
     used: A:anti-inflammatory, A:neuroprotective, D:inflammation
     C: Advancements in isolation and characterization techniques, along with improved access to pure analytical standards, will play a critical role in achieving standardized, high-quality dietary supplements based on H. erinaceus . The aim of this study is to analyze the protective and nourishing effects of H. erinaceus on the nervous system and present the most up-to-date research findings related to this topic.
  REF-0643 [preclinical] 2024 International Journal of Biological Macr | Polysaccharides from an edible mushroom, Hericium erinaceus, alleviate ulcerative colitis in mice by inhibiting the NLRP3 inflammasomes and reestablis | doi:10.1016/j.ijbiomac.2024.131251 
     used: A:anti-inflammatory, A:digestive, D:inflammation
     C: These findings suggest that HEFPs alleviate UC by suppressing the NLRP3 inflammasome/Caspase-1 pathway. Lachnospiraceae, Clostridiales, Parabacteroides, Oscillibacter, and Clostridium XlVa genera were more abundant in the gut microbiota of the HEFPs group than that of the MC group.
  REF-0644 [preclinical] 2024 International Journal of Biological Macr | Polysaccharides from Hericium erinaceus and its immunomodulatory effects on RAW 264.7 macrophages | doi:10.1016/j.ijbiomac.2024.134947 
     used: A:immunomodulator, D:immune-support
     C: The results revealed that HEP improved the immunostimulatory activity of RAW264.7 cells, evident from increased production of IL-6 and TNF-α. These findings suggest that HEP is capable of enhancing the immune activity of RAW 264.7 macrophage.
  REF-0645 [narrative-review] 2025 World Journal of Gastroenterology | Potential of traditional Chinese medicine in gastrointestinal disorders: Hericium erinaceus in chronic atrophic gastritis | doi:10.3748/wjg.v31.i20.106615 
     used: A:digestive, D:cancer
     C: Preclinical cellular evidence also indicates an antineoplastic role in gastric carcinogenesis, mediated by two components: Erinacine A and S. Further evidence is needed to propose this fungus as a potential complementary therapeutic approach for CAG.
  REF-2418 [narrative-review] 2025 Nutrients | Lion's Mane Mushroom (Hericium erinaceus): A Neuroprotective Fungus with Antioxidant, Anti-Inflammatory, and Antimicrobial Potential - A Narrative Rev | doi:10.3390/nu17081307 
     used: A:anti-inflammatory, A:neuroprotective, M:arthritis, M:cognitive-function, M:inflammation, M:memory, M:skin-irritation
     C: Future research should prioritize large-scale clinical trials, the standardization of extraction methods, and the elucidation of pharmacokinetics to facilitate its integration into evidence-based medicine. The potential of H. erinaceus as a functional food, nutraceutical, and adjunct therapeutic agent highlights the need for interdisciplinary collaboration between researchers, clinicians, and regulatory bodies.
  REF-2419 [clinical] 2020 Frontiers in Aging Neuroscience | Prevention of Early Alzheimer's Disease by Erinacine A-Enriched Hericium erinaceus Mycelia Pilot Double-Blind Placebo-Controlled Study | doi:10.3389/fnagi.2020.00155 
     used: A:neuroprotective, D:cognitive-function, D:memory
     C: Three 350 mg/g EAHE capsules intervention for 49 weeks demonstrated higher CASI, MMSE, and IADL scores and achieved a better contrast sensitivity in patients with mild AD when compared to the placebo group, suggesting that EAHE is safe, well-tolerated, and may be important in achieving neurocognitive benefits. Clinical trial registration ClinicalTrials.gov, identifier NCT04065061.
     !NULL: Using diffusion tensor imaging, the mean apparent diffusion coefficient (ADC) values from the arcuate fasciculus region in the dominant hemisphere significantly increased in the placebo group while no significant difference was found in the EAHE group in comparison to their baselines.
     !NULL: Moreover, ADC values from the parahippocampal cingulum region in the dominant hemisphere significantly decreased in the EAHE group whereas no significant difference was found in the placebo group when compared to their baselines.
  REF-2420 [narrative-review] 2015 Journal of Agricultural and Food Chemist | Chemistry, Nutrition, and Health-Promoting Properties of Hericium erinaceus (Lion's Mane) Mushroom Fruiting Bodies and Mycelia and Their Bioactive Com | doi:10.1021/acs.jafc.5b02914 
     used: A:immunomodulator, M:cold, M:immune-support
     C: A wide range of research advances and techniques are described and evaluated. The collated information and suggestion for further research might facilitate and guide further studies to optimize the use of the whole mushrooms and about 70 characterized actual and potential bioactive secondary metabolites to help prevent or treat human chronic, cognitive, and neurological diseases.
  REF-2421 [preclinical] 2022 Molecules | Secondary Metabolites from Hericium erinaceus and Their Anti-Inflammatory Activities | doi:10.3390/molecules27072157 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The results showed that compounds 5 and 9 exhibited moderate activity against TNF-α (IC 50 : 78.50 μM and 62.46 μM), IL-6 (IC 50 : 56.33 μM and 48.50 μM) and NO (IC 50 : 87.31 μM and 76.16 μM) secretion. These results supply new information about the secondary metabolites of Hericium erinaceus and their anti-inflammatory effects.

## hibiscus-sabdariffa - Hibiscus sabdariffa - Hibiscus, Roselle, Sorrel
actions: antidiabetic=['REF-0567', 'REF-1842', 'REF-1848']; antihypertensive=['REF-0464', 'REF-0566', 'REF-0567', 'REF-1844', 'REF-1845', 'REF-1846', 'REF-1847']; antioxidant=['REF-0464', 'REF-1840', 'REF-1841']; lipid-lowering=['REF-0464', 'REF-1843', 'REF-1845', 'REF-1848']
- **blood-sugar** [needs-review,ev7] !INF note="inferred from antidiabetic action"
    D=['REF-0567'] N=[] X=[] M=['REF-1842<antidiabetic', 'REF-1848<antidiabetic']
- **cardiovascular-support** [needs-review,ev9] !INF note="inferred from antihypertensive action"
    D=['REF-0464', 'REF-0566', 'REF-0567'] N=['REF-1844'] X=[] M=['REF-1845<antihypertensive', 'REF-1846<antihypertensive', 'REF-1847<antihypertensive', 'REF-1843<lipid-lowering', 'REF-1845<lipid-lowering', 'REF-1848<lipid-lowering']
- **high-blood-pressure** [verified,ev9] note="Lowers blood pressure, with the greatest effect in people with raised blood pressure"
    D=['REF-0464', 'REF-0566', 'REF-0567'] N=['REF-1844'] X=[] M=[]
- **high-cholesterol** [needs-review,ev7] !INF note="inferred from lipid-lowering action"
    D=['REF-0464'] N=['REF-1843'] X=[] M=['REF-1845<lipid-lowering', 'REF-1848<lipid-lowering']
- **metabolic-support** [needs-review,ev1] note="inferred from antidiabetic action"
    D=[] N=[] X=['REF-0567'] M=['REF-1842<antidiabetic', 'REF-1848<antidiabetic']
  REF-0464 [systematic-review] 2022 Nutrition Reviews | A systematic review and meta-analysis of the effects of Hibiscus sabdariffa on blood pressure and cardiometabolic markers | doi:10.1093/nutrit/nuab104 
     used: A:antihypertensive, A:antioxidant, A:lipid-lowering, D:cardiovascular-support, D:high-blood-pressure, D:high-cholesterol
     C: Regular consumption of hibiscus could confer reduced cardiovascular disease risk. More studies are warranted to establish an effective dose response and treatment duration. Systematic review registration PROSPERO registration no. CRD42020167295.
  REF-0566 [systematic-review] 2022 Journal of Cardiovascular Pharmacology | Efficacy of Hibiscus sabdariffa on Reducing Blood Pressure in Patients With Mild-to-Moderate Hypertension: A Systematic Review and Meta-Analysis of Pu | doi:10.1097/FJC.0000000000001161 
     used: A:antihypertensive, D:cardiovascular-support, D:high-blood-pressure
     C: Hibiscus sabdariffa is effective in reducing the SBP and DBP in patients with mild-to-moderate hypertension, but was neither effective in those with MetS nor superior to antihypertensive drugs. Further RCTs are required to determine the long-term efficacy of H. sabdariffa and to describe patients who would benefit most from this treatment.
     !NULL: Subgroup analysis showed that change in SBP and DBP was statistically significant in patients with only hypertension, whereas not significant in patients with hypertension associated with MetS.
     !NULL: sabdariffa was compared with active controls (antihypertensive drugs or other herbals), the change in SBP and DBP was not statistically significant (all P > 0.
  REF-0567 [systematic-review] 2020 Phytotherapy Research | The efficacy of sour tea (Hibiscus sabdariffa L.) on selected cardiovascular disease risk factors: A systematic review and meta-analysis of randomized | doi:10.1002/ptr.6541 
     used: A:antidiabetic, A:antihypertensive, D:blood-sugar, D:cardiovascular-support, D:high-blood-pressure
     C: Although no significant effect was observed on triacylglycerol, total cholesterol, and high-density lipoprotein cholesterol following sour tea consumption, a trend toward a significant reduction was found in low-density lipoprotein cholesterol serum concentrations (p = 0.08). This systematic review and meta-analysis suggests that sour tea consumption could have beneficial effect in controlling glycemic status and blo
     !NULL: Although no significant effect was observed on triacylglycerol, total cholesterol, and high-density lipoprotein cholesterol following sour tea consumption, a trend toward a significant reduction was found in low-density lipoprotein cholesterol serum concentrations (p = 0.
  REF-1840 [narrative-review] 2014 Food Chemistry | Hibiscus sabdariffa L. - a phytochemical and pharmacological review | doi:10.1016/j.foodchem.2014.05.002 
     used: A:antioxidant
     C: More well designed controlled clinical trials are needed which use phytochemically characterised preparations. Hs has an excellent safety and tolerability record.
  REF-1841 [narrative-review] 2018 Biomedicine & Pharmacotherapy | A review on phytochemistry and therapeutic uses of Hibiscus sabdariffa L. | doi:10.1016/j.biopha.2018.03.023 
     used: A:antioxidant
     C: Most studies supported and provided the scientific basis for the statement that Hibiscus sabdariffa and their active constituents play an important role in the prevention of chronic and degenerative diseases that are associated with oxidative stress. Our study suggests, that good research is needed, to establish a potential strategy that can balance the pharmacological and toxic effects of roselle and standardized fi
  REF-1842 [narrative-review] 2022 Foods | Hibiscus sabdariffa in Diabetes Prevention and Treatment - Does It Work? An Evidence-Based Review | doi:10.3390/foods11142134 
     used: A:antidiabetic, M:blood-sugar, M:metabolic-support
     C: The aim of this review was to update the knowledge about the therapeutic effects of roselle in diabetes and its comorbidities based on in vitro, animal, and human studies. After a careful analysis of the scientific literature, it can be stated that roselle is a promising product that can be used either on its own or as an addition to the conventional treatment regimens to prevent or treat diabetes and its accompanyin
  REF-1843 [meta-analysis] 2013 Journal of Ethnopharmacology | Effects of Hibiscus sabdariffa L. on serum lipids: a systematic review and meta-analysis | doi:10.1016/j.jep.2013.09.042 
     used: A:lipid-lowering, M:cardiovascular-support, N:high-cholesterol
     C: The available evidence from RCTs does not support the efficacy of Hibiscus sabdariffa L. in lowering serum lipids. Further rigorously designed trials with larger sample sizes are warranted to confirm the effects of HS on serum lipids.
     !NULL: Conclusions The available evidence from RCTs does not support the efficacy of Hibiscus sabdariffa L.
  REF-1844 [systematic-review] 2009 Phytomedicine | The effectiveness of Hibiscus sabdariffa in the treatment of hypertension: a systematic review | doi:10.1016/j.phymed.2009.09.002 
     used: A:antihypertensive, N:cardiovascular-support, N:high-blood-pressure
     C: The four randomized controlled studies identified in this review do not provide reliable evidence to support recommending Hibiscus sabdariffa for the treatment of primary hypertension in adults.
  REF-1845 [narrative-review] 2013 Fitoterapia | Hibiscus sabdariffa L. in the treatment of hypertension and hyperlipidemia: a comprehensive review of animal and human studies | doi:10.1016/j.fitote.2013.01.003 
     used: A:antihypertensive, A:lipid-lowering, M:cardiovascular-support, M:high-cholesterol
     C: A number of potential mechanisms have been proposed to explain the hypotensive and anticholesterol effects, but the most common explanation is the antioxidant effects of the anthocyanins inhibition of LDL-C oxidation, which impedes atherosclerosis, an important cardiovascular risk factor. This comprehensive body of evidence suggests that extracts of HS are promising as a treatment of hypertension and hyperlipidemia, 
     !NULL: There is no evidence of hepatic or renal toxicity as the result of HS extract consumption, except for possible adverse hepatic effects at high doses.
     !NULL: There is evidence that HS acts as a diuretic, however in most cases the extract did not significantly influence electrolyte levels.
  REF-1846 [clinical] 2014 Molecular Nutrition & Food Research | Hibiscus sabdariffa extract lowers blood pressure and improves endothelial function | doi:10.1002/mnfr.201300774 
     used: A:antihypertensive, M:cardiovascular-support
     C: Diuresis and inhibition of the angiotensin I-converting enzyme were found to be less important mechanisms than those related to the antioxidant, anti-inflammatory, and endothelium-dependent effects to explain the beneficial actions. Notably, polyphenols induced a favorable endothelial response that should be considered in the management of metabolic cardiovascular risks.
  REF-1847 [rct] 2020 Journal of Human Hypertension | Hypertension treatment with Combretum micranthum or Hibiscus sabdariffa, as decoction or tablet: a randomized clinical trial | doi:10.1038/s41371-020-00415-1 
     used: A:antihypertensive, M:cardiovascular-support
     C: Bissap and kinkeliba appeared, at doses utilized, to be as effective as captopril over the 6 months' follow-up. In subsequent studies, brews might be started with a lower dosage.
  REF-1848 [narrative-review] 2013 Cardiovascular & Hematological Agents in | Hibiscus sabdariffa Linnaeus (Malvaceae), curcumin and resveratrol as alternative medicinal agents against metabolic syndrome | doi:10.2174/1871525711311010006 
     used: A:antidiabetic, A:lipid-lowering, M:blood-sugar, M:cardiovascular-support, M:high-cholesterol, M:metabolic-support
     C: Thus, due to their efficacy in the regulation of multiple targets, polyphenols have received considerable interest as potential therapeutic agents for the prevention and treatment of MS. This review discusses the therapeutic use of HSE, as well as curcumin and resveratrol, in the context of obesity as an initiator of insulin resistance and hypertension, the two main features of MS, together with the underlying mechan

## hippophae-rhamnoides - Hippophae rhamnoides - Sea buckthorn, common sea buckthorn, seaberry
actions: anti-inflammatory=['REF-0049', 'REF-0206', 'REF-0319', 'REF-2317', 'REF-2320']; anticancer=['REF-2321', 'REF-2326']; antidiabetic=['REF-0049', 'REF-0206', 'REF-0319']; antioxidant=['REF-0049', 'REF-0206', 'REF-0319', 'REF-2317', 'REF-2323', 'REF-2324', 'REF-2325']; emollient=['REF-0049', 'REF-0206', 'REF-0319', 'REF-2318']; immunomodulator=['REF-0049', 'REF-0206', 'REF-0319', 'REF-2322', 'REF-2327']; vulnerary=['REF-0049', 'REF-0206', 'REF-0319', 'REF-2318']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=['REF-2317<anti-inflammatory', 'REF-2320<anti-inflammatory']
- **blood-sugar** [needs-review,ev2] !INF note="inferred from antidiabetic action"
    D=['REF-2319'] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=[]
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-2321', 'REF-2326'] N=[] X=[] M=[]
- **cardiovascular-support** [verified,ev2] note=""
    D=['REF-2319', 'REF-2317'] N=[] X=[] M=[]
- **cold** [needs-review,ev1] note="inferred from immunomodulator action"
    D=[] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=['REF-2322<immunomodulator', 'REF-2327<immunomodulator']
- **eczema** [needs-review,ev2] !INF note="inferred from emollient action"
    D=['REF-2318'] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=[]
- **immune-support** [verified,ev2] note=""
    D=['REF-2317'] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=['REF-2322<immunomodulator', 'REF-2327<immunomodulator']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-2318'] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=['REF-2317<anti-inflammatory', 'REF-2320<anti-inflammatory']
- **skin-irritation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-2318'] N=[] X=['REF-0206', 'REF-2320', 'REF-0049', 'REF-0319'] M=['REF-2317<anti-inflammatory']
- **wounds** [needs-review,ev2] !INF note="inferred from vulnerary action"
    D=['REF-2318'] N=[] X=['REF-0206', 'REF-0049', 'REF-0319'] M=[]
  REF-0049 [traditional] 2014  | Sea buckthorn — values and medicinal properties | NO-ID 
     used: A:anti-inflammatory, A:antidiabetic, A:antioxidant, A:emollient, A:immunomodulator, A:vulnerary
     (no abstract)
  REF-0206 [traditional] 1971  | The genus Hippophae L.: a taxonomic study | NO-ID 
     used: A:anti-inflammatory, A:antidiabetic, A:antioxidant, A:emollient, A:immunomodulator, A:vulnerary
     (no abstract)
  REF-0319 [traditional] 2021  | Sea buckthorn (Hippophae rhamnoides L.) polysaccharides | NO-ID 
     used: A:anti-inflammatory, A:antidiabetic, A:antioxidant, A:emollient, A:immunomodulator, A:vulnerary
     (no abstract)
  REF-2317 [narrative-review] 2011 Journal of Ethnopharmacology | Medicinal and therapeutic potential of Sea buckthorn (Hippophae rhamnoides L.) | doi:10.1016/j.jep.2011.09.024 
     used: A:anti-inflammatory, A:antioxidant, D:cardiovascular-support, D:immune-support, M:arthritis, M:inflammation, M:skin-irritation
     C: It is clear that Sea buckthorn is an important plant because of its immense medicinal and therapeutic potential. However, several knowledge gaps identified in this paper would give impetus to new academic and R&D activities especially for the development of Sea buckthorn based herbal medicine and nutraceuticals.
  REF-2318 [narrative-review] 2021 Journal of Ethnopharmacology | Ethnomedicinal uses, phytochemistry and dermatological effects of Hippophae rhamnoides L.: a review | doi:10.1016/j.jep.2020.113434 
     used: A:emollient, A:vulnerary, D:eczema, D:inflammation, D:skin-irritation, D:wounds
     C: Pharmacological evaluation confirmed the ethnomedically claimed biological actions and other beneficial effects on the skin of H. rhamnoides using scientifically accepted protocols and controls, although some of the studies require more elaborative studies. Its full application in the dermatology may be attributed to the presence of a variety of flavonoids, vitamins, and unsaturated fatty acids. Great use of plant in
  REF-2319 [narrative-review] 2024 Frontiers in Cardiovascular Medicine | Research progress of sea buckthorn (Hippophae rhamnoides) in prevention and treatment of cardiovascular disease | doi:10.3389/fcvm.2024.1477636 
     used: D:blood-sugar, D:cardiovascular-support
     C: To summarize, sea buckthorn has a beneficial effect on cardiovascular disease and may give a novel strategy for clinical intervention and therapy. This paper summarizes the phytochemistry, pharmacology, clinical applications, safety, and toxicity of sea buckthorn in order to better understand the mechanism of action of the various bioactive components in sea buckthorn, investigate its medicinal potential, and provide
  REF-2320 [preclinical] 2005 International Immunopharmacology | Anti-inflammatory activity of seabuckthorn (Hippophae rhamnoides) leaves | doi:10.1016/j.intimp.2005.03.017 
     used: A:anti-inflammatory, M:arthritis, M:inflammation
     C: Administration of SBT extract on the same day or 5 days prior to inflammatory insult into the joint, significantly reduced the inflammation as compared to the untreated animals in a dose dependent manner. These observations suggest that the SBT leaf extract has a significant anti-inflammatory activity and has the potential for the treatment of arthritis.
  REF-2321 [preclinical] 2009 Fitoterapia | Anti-tumor promoters phenolics and triterpenoid from Hippophae rhamnoides | doi:10.1016/j.fitote.2009.01.006 
     used: A:anticancer, D:cancer
     C: These compounds were evaluated for their inhibitory effects on TPA-induced inflammation (1 microg/ear) in mice. Within the tested compounds, 3 and 4 showed marked anti-inflammatory effects, with a 50% inhibitory dose of 1.7 and 0.2 mumol/ear.
  REF-2322 [preclinical] 2023 Chemistry & Biodiversity | Flash extraction, characterization, and immunoenhancement activity of polysaccharide from Hippophae rhamnoides Linn. | doi:10.1002/cbdv.202200776 
     used: A:immunomodulator, M:cold, M:immune-support
     C: In addition, the in vitro antioxidant and immunoenhancement activities of HRP-1 and HRP-2 were analyzed, and the two fractions showed good free radical scavenging activity against ⋅OH, ABTS⋅ + , DPPH⋅, and extremely strong immunomodulatory activity against RAW264.7 cells. Indicating that flash extraction is suitable for extraction of HRP, the structural study of HRP provides a scientific theoretical basis for the dev
  REF-2323 [narrative-review] 2023 Phytochemistry Reviews | Phytochemistry and pharmacology of sea buckthorn (Elaeagnus rhamnoides; syn. Hippophae rhamnoides): progress from 2010 to 2021 | doi:10.1007/s11101-022-09832-1 
     used: A:antioxidant
     C: In addition, biosynthetic pathways of the main groups of these compounds have been shortly described. Graphical abstract
  REF-2324 [narrative-review] 2020 Food Research International | Why is sea buckthorn (Hippophae rhamnoides L.) so exceptional? A review | doi:10.1016/j.foodres.2020.109170 
     used: A:antioxidant
     C: The article also deals with the effects of sea buckthorn components on the course of non-enzymatic browning of food and in vivo glycation. In addition, sensory perception of sea buckthorn and its constituents from the consumers point of view is discussed.
  REF-2325 [narrative-review] 2022 Critical Reviews in Food Science and Nut | Health promoting properties and sensory characteristics of phytochemicals in berries and leaves of sea buckthorn (Hippophae rhamnoides) | doi:10.1080/10408398.2020.1869921 
     used: A:antioxidant
     C: Studies regarding the bioavailability of the compounds and the influence of the processing conditions are also part of this review. Finally, the role of the sensory properties is emphasized in the development of SB products to increase utilization of the berry as a common meal component and to obtain value-added products to support human health.
  REF-2326 [preclinical] 2025 Frontiers in Pharmacology | Chemopreventive and therapeutic effects of Hippophae rhamnoides L. fruit peels evaluated in preclinical models of breast carcinoma | doi:10.3389/fphar.2025.1561436 
     used: A:anticancer, D:cancer
     C: This study of H. rhamnoides in rodent BC models shows promising data but requires rigorous, long-term validation. Integrating plant-based nutraceuticals into oncology necessitates precise cancer-type profiling and patient stratification for effective personalized treatments.
  REF-2327 [narrative-review] 2024 International Journal of Biological Macr | Advance in Hippophae rhamnoides polysaccharides: extraction, structural characteristics, pharmacological activity, structure-activity relationship and | doi:10.1016/j.ijbiomac.2024.132420 
     used: A:immunomodulator, M:cold, M:immune-support
     C: The structure-activity relationship, safety evaluation, application, as well as the shortcomings of current research and promising prospects are also highlighted. This article aims to offer a comprehensive understanding of HRPs and lay a groundwork for future research and utilization of HRPs as multifunctional biomaterials and therapeutic agents.
