# Deep dossier batch 9

## humulus-lupulus - Humulus lupulus - Hop, Hops, common hop
actions: anti-inflammatory=['REF-1729', 'REF-1730']; antioxidant=['REF-1726', 'REF-1729']; digestive=[]; sedative=['REF-1732']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-1729<anti-inflammatory', 'REF-1730<anti-inflammatory']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-1729<anti-inflammatory', 'REF-1730<anti-inflammatory']
- **insomnia** [needs-review,ev1] note="EU traditional use to aid sleep"
    D=['REF-3077'] N=[] X=['REF-1732'] M=[]
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-1729<anti-inflammatory', 'REF-1730<anti-inflammatory']
  REF-1726 [preclinical] 2022 Journal of Natural Medicines | Humulus lupulus L. extract and its active constituent xanthohumol attenuate oxidative stress and nerve injury induced by iron overload via activating  | doi:10.1007/s11418-022-01642-1 
     used: A:antioxidant
     C: These findings demonstrated the protective effect of HLE and XAN against iron-induced memory impairment, which is attributed to its antioxidant profile by activation of AKT/GSK3β and Nrf2/NQO1 pathways. Also, it was suggested that hops could be a potential candidate for iron overload-related neurological diseases treatment.
  REF-1729 [preclinical] 2022 Pharmaceuticals | The Anti-Inflammatory Effect of Humulus lupulus Extract In Vivo Depends on the Galenic System of the Topical Formulation | doi:10.3390/ph15030350 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: In summary, we have shown that 1% HL extract exerts anti-inflammatory effects comparable to 1% HCA, but only when incorporated in our O/W cream. Our findings confirm the critical role of the vehicle in topical anti-inflammatory systems.
  REF-1730 [preclinical] 2020 Journal of Physiology and Pharmacology | Spent hops (Humulus Lupulus L.) extract as modulator of the inflammatory response in lipopolysaccharide stimulated RAW 264.7 macrophages | doi:10.26402/jpp.2020.1.05 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Both mRNA and protein expression of NF-κB was decreased to 38% and 42%, respectively. These results provide the first evidence that SHE decreases the expression of proinflammatory cytokines and inflammatory mediators, which merits further studies to investigate the potential of SHE as anti-inflammatory preparation.
  REF-1732 [rct] 2017 Hormones | Effects of a hops (Humulus lupulus L.) dry extract supplement on self-reported depression, anxiety and stress levels in apparently healthy young adult | doi:10.14310/horm.2002.1738 
     used: A:sedative
     C: In otherwise healthy young adults reporting at least mild depression, anxietyand stress symptoms, daily supplementation with a hops dry extract can significantly improve all these symptoms over a 4-week period. These beneficial effects agree with the indication of hops for anxiety/mood disorders and restlessness, as approved by the German Commission E.
     !NULL: No significant changes in body weight and composition or morning circulating cortisol were noted with the hops or placebo.
  REF-3077 [traditional] 2014  | Community herbal monograph on Humulus lupulus L., flos, Revision 1 | NO-ID 
     used: D:insomnia
     (no abstract)

## hydrastis-canadensis - Hydrastis canadensis - Goldenseal, Orange root, Yellow root
actions: anti-inflammatory=['REF-0455']; antimicrobial=['REF-0455', 'REF-0588', 'REF-1849', 'REF-1850', 'REF-1851', 'REF-1852']; astringent=['REF-0455']; digestive=['REF-0455', 'REF-1851']
- **bloating** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0455'] M=['REF-1851<digestive']
- **indigestion** [needs-review,ev1] note="inferred from digestive action"
    D=[] N=[] X=['REF-0455'] M=['REF-1851<digestive']
- **infection** [needs-review,ev2] note="Antimicrobial (berberine) - supports skin, mucosal and gastrointestinal infections and sore throat; Topical for skin infections and irritation - whole-leaf extract is active in vitro against methicillin-resistant Staphylococcus aureus (MRSA)"
    D=['REF-0455', 'REF-0588'] N=[] X=[] M=['REF-1849<antimicrobial', 'REF-1850<antimicrobial', 'REF-1851<antimicrobial', 'REF-1852<antimicrobial']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0455'] N=[] X=[] M=[]
- **skin-irritation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0455'] N=[] X=[] M=[]
- **wounds** [needs-review,ev2] !INF note="inferred from antimicrobial action"
    D=['REF-0455'] N=[] X=['REF-1851', 'REF-0588'] M=['REF-1849<antimicrobial', 'REF-1850<antimicrobial', 'REF-1852<antimicrobial']
  REF-0455 [narrative-review] 2020 Pharmacological Research | Goldenseal (Hydrastis canadensis L.) and its active constituents: A critical review of their efficacy and toxicological issues | doi:10.1016/j.phrs.2020.105085 
     used: A:anti-inflammatory, A:antimicrobial, A:astringent, A:digestive, D:infection, D:inflammation, D:skin-irritation, D:wounds
     C: Thus, large randomized, double-blind clinical studies need to be conducted on goldenseal supplements and their main alkaloids to provide more evidence on the mechanisms responsible for the pharmaceutical activity, clinical efficacy and safety of these products. Thus, it is very important to review the scientific information about goldenseal to understand about the current scenario.
  REF-0588 [preclinical] 2012 Planta Medica | Quorum quenching and antimicrobial activity of goldenseal (Hydrastis canadensis) against methicillin-resistant Staphylococcus aureus (MRSA) | doi:10.1055/s-0032-1315042 
     used: A:antimicrobial, D:infection
     C: Collectively, our results show that H. canadensis leaf extracts possess a mixture of constituents that act against MRSA via several different mechanisms. These findings lend support for the traditional application of crude H. canadensis extracts in the prevention of infection.
  REF-1849 [preclinical] 2021 Alternative Therapies in Health and Medi | Effects of Hydrastis Canadensis, Commiphora Habessinica, Phytolacca Americana, and Echinacea Purpurea on Bacterial Growth | NO-ID 
     used: A:antimicrobial, M:infection, M:wounds
     C: The results demonstrated that H. canadensis had antibacterial activity against S. epidermidis, but the HMPE formula was not active against S. epidermidis, when a zone of inhibition threshold of 12 millimeters (mm) was used to determine antibiotic activity. Because the HMPE formula was shown to be less effective than H. canadensis alone, the formula might benefit from an increased percentage of H. canadensis.
  REF-1850 [preclinical] 2010 Planta Medica | Goldenseal (Hydrastis canadensis L.) extracts synergistically enhance the antibacterial activity of berberine via efflux pump inhibition | doi:10.1055/s-0030-1250606 
     used: A:antimicrobial, M:infection, M:wounds
     C: Furthermore, extracts from the aerial portions of H. canadensis contain efflux pump inhibitors, while efflux pump inhibitory activity was not observed for the root extract. The three most abundant H. canadensis alkaloids, berberine, hydrastine, and canadine, are not responsible for the efflux pump inhibitory activity of the extracts from H. canadensis aerial portions.
     !NULL: aureus but had no effect on the expulsion of this compound from an isogenic derivative deleted for norA.
  REF-1851 [preclinical] 2003 Phytotherapy Research | In vitro susceptibility of Helicobacter pylori to isoquinoline alkaloids from Sanguinaria canadensis and Hydrastis canadensis | doi:10.1002/ptr.1108 
     used: A:antimicrobial, A:digestive, M:bloating, M:indigestion, M:infection
     C: The crude methanol extract of H. canadensis rhizomes was very active, with an MIC50 of 12.5 microg/ml. Two isoquinoline alkaloids, berberine and beta-hydrastine, were identified as the active constituents, and having an MIC50 of 12.5 and 100.0 microg/ml, respectively.
  REF-1852 [preclinical] 2011 Journal of Natural Products | Synergy-directed fractionation of botanical medicines: a case study with goldenseal (Hydrastis canadensis) | doi:10.1021/np200336g 
     used: A:antimicrobial, M:infection, M:wounds
     C: The flavonoid synergists are present at higher concentration in extracts from H. canadensis leaves, while the antimicrobial alkaloid berberine is present at higher levels in H. canadensis roots. Thus, it may be possible to produce an extract with optimal activity against S. aureus using a combination of goldenseal roots and leaves.

## hypericum-perforatum - Hypericum perforatum - Perforate St John’s-wort, St John's wort, common St John's wort
actions: anti-inflammatory=['REF-0154', 'REF-0181', 'REF-1790']; antioxidant=['REF-0154', 'REF-0181', 'REF-1791']; antiviral=['REF-0154', 'REF-0181']; emollient=['REF-0154', 'REF-0181']; sedative=['REF-0154', 'REF-0181', 'REF-1789', 'REF-0842', 'REF-0843', 'REF-1790', 'REF-1794', 'REF-1796', 'REF-1797', 'REF-1798', 'REF-1799']; vulnerary=['REF-0154', 'REF-0181', 'REF-1789']
- **bruising** [needs-review,ev1] note="inferred from vulnerary action"
    D=[] N=[] X=['REF-0154', 'REF-0181'] M=['REF-1789<vulnerary']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0154', 'REF-0181'] M=['REF-1790<anti-inflammatory']
- **insomnia** [needs-review,ev1] note="inferred from sedative action"
    D=[] N=[] X=['REF-0154', 'REF-0842', 'REF-0843', 'REF-1790', 'REF-1794', 'REF-1796', 'REF-1797', 'REF-1798', 'REF-1799', 'REF-0181'] M=['REF-1789<sedative']
- **wounds** [needs-review,ev1] note="inferred from vulnerary action"
    D=[] N=[] X=['REF-0154', 'REF-0181'] M=['REF-1789<vulnerary']
- **depression** [verified,ev8] note="Cochrane review and meta-analysis: hypericum extracts are superior to placebo and comparable to standard antidepressants (including SSRIs) in mild-to-moderate major depression, with fewer side effects. Evidence for severe depression is lacking."
    D=['REF-0154', 'REF-0842', 'REF-1797', 'REF-1798'] N=[] X=[] M=[]
  REF-0154 [systematic-review] 2008 Cochrane Database of Systematic Reviews | St John's wort for major depression | doi:10.1002/14651858.CD000448.pub3 
     used: A:anti-inflammatory, A:antioxidant, A:antiviral, A:emollient, A:sedative, A:vulnerary, D:depression
     C: The available evidence suggests that the hypericum extracts tested in the included trials a) are superior to placebo in patients with major depression; b) are similarly effective as standard antidepressants; c) and have fewer side effects than standard antidepressants. The association of country of origin and precision with effects sizes complicates the interpretation.
  REF-0181 [traditional] 2013  | Hypericum perforatum (St | NO-ID 
     used: A:anti-inflammatory, A:antioxidant, A:antiviral, A:emollient, A:sedative, A:vulnerary
     (no abstract)
  REF-0842 [systematic-review] 2017 Journal of Affective Disorders | Clinical use of Hypericum perforatum (St John's wort) in depression: A meta-analysis | doi:10.1016/j.jad.2016.12.048 
     used: A:sedative, D:depression
     C: For patients with mild-to-moderate depression, St John's wort has comparable efficacy and safety when compared to SSRIs. Follow-up studies carried out over a longer duration should be planned to ascertain its benefits.
  REF-0843 [traditional] 2022 Naunyn-Schmiedeberg's Archives of Pharma | St. John's wort (Hypericum perforatum) and depression: what happens to the neurotransmitter systems? | doi:10.1007/s00210-022-02229-z 
     used: A:sedative
     C: In addition, St. John's wort induces a dualistic modulation on the activity of cholinergic signaling, which can be an interesting topic for future studies.
  REF-1789 [narrative-review] 2022 Iranian Journal of Basic Medical Science | Hypericum perforatum: Traditional uses, clinical trials, and drug interactions | doi:10.22038/IJBMS.2022.65112.14338 !TAG trial-title/narrative-review
     used: A:sedative, A:vulnerary, M:bruising, M:insomnia, M:wounds
     C: SJW is a valuable medicinal plant, especially for psychiatric disorders. However, precautions should be taken while administrating the plant.
  REF-1790 [preclinical] 2024 Phytomedicine | Hypericum perforatum L. attenuates depression by regulating Akkermansia muciniphila, tryptophan metabolism and NFkB-NLRP2-Caspase1-IL1beta pathway | doi:10.1016/j.phymed.2024.155847 
     used: A:anti-inflammatory, A:sedative, M:inflammation
     C: The promising therapeutic role of HPL in treating depression is primarily attributed to its regulation of the NFκB-NLRP2-Caspase1-IL1β pathway, specifically by targeting AKK and tryptophan metabolites.
  REF-1791 [narrative-review] 2016 Frontiers in Plant Science | Neuroprotective Activity of Hypericum perforatum and Its Major Components | doi:10.3389/fpls.2016.01004 
     used: A:antioxidant
     C: As for this, it has been demonstrated that H. perforatum extracts and several of its major molecular components have the ability to protect against toxic insults, either directly, through neuroprotective mechanisms, or indirectly, through is antioxidant properties. H. perforatum has therefore the potential to become an effective neuroprotective therapeutic agent, despite further studies that need to be carried out.
  REF-1794 [narrative-review] 2004 Life Sciences | The antidepressant mechanism of Hypericum perforatum | doi:10.1016/j.lfs.2004.04.005 
     used: A:sedative
     C: However, it is still not clear whether these mechanisms can be activated in vivo, since after administration of Hypericum extract brain concentrations of hyperforin are well below those active in vitro. In the rat, Hypericum extract might indirectly activate sigma receptors in vivo (through the formation of an unknown metabolite or production of an endogenous ligand), suggesting a new target for its antidepressant ef
  REF-1796 [narrative-review] 2006 Clinical Pharmacokinetics | Hypericum perforatum: a 'modern' herbal antidepressant: pharmacokinetics of active ingredients | doi:10.2165/00003088-200645050-00002 
     used: A:sedative
     C: Until now, the pharmacokinetic profile of the flavonoids in humans after oral administration of an alcoholic H. perforatum extract has been investigated in only one study. More data are available for rutin and the aglycone quercetin after administration of pure substances or other flavonoid sources.
  REF-1797 [narrative-review] 2001 Pharmacopsychiatry | Hypericum perforatum - a review of clinical studies | doi:10.1055/s-2001-15467 
     used: A:sedative, D:depression
     C: John's wort preparations comprise patients with mild or moderate depression. Based on the existing literature, limitations to efficacy in more severe cases as well as interactions and contraindications have to be respected.
  REF-1798 [narrative-review] 1999 Molecular Psychiatry | The experimental and clinical pharmacology of St John's Wort (Hypericum perforatum L.) | doi:10.1038/sj.mp.4000557 
     used: A:sedative, D:depression
     C: The advantage of hypericum over other antidepressants may result from its favorable side-effect profile. Although pre-clinical and short-term clinical studies demonstrate antidepressant activity, the lack of long-term use and efficacy, and the heterogeneity of patients, interventions, extract preparations from previous clinical studies suggests that more careful and controlled studies are needed to determine the long
  REF-1799 [narrative-review] 2003 Current Topics in Medicinal Chemistry | Hypericum perforatum, a source of neuroactive lead structures | doi:10.2174/1568026033392589 
     used: A:sedative
     C: There has been a proliferation of clinical studies on Hypericum in the last ten years, and even though some of these studies might be methodologically flawed, the preponderance of the evidence proves Hypericum to be beneficial for the treatment of mild-to-moderate depression, with a very favorable side effect profile. One clinical trial carried out using two extracts with different hyperforin content indicate this co

## hyssopus-officinalis - Hyssopus officinalis - Hyssop, common hyssop
actions: anti-inflammatory=['REF-1804']; anticancer=['REF-1802']; antioxidant=['REF-1801', 'REF-1806', 'REF-1808']; expectorant=['REF-1803', 'REF-1804']
- **bronchitis** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=['REF-1804'] M=['REF-1803<expectorant']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1802'] N=[] X=[] M=[]
- **cough** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=['REF-1804'] M=['REF-1803<expectorant']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-1804'] N=[] X=[] M=[]
- **respiratory-support** [verified,ev2] note=""
    D=['REF-1804'] N=[] X=[] M=['REF-1803<expectorant']
  REF-1801 [preclinical] 2019 Drug and Chemical Toxicology | Gastroprotective effect of Hyssopus officinalis L. leaves via reduction of oxidative stress in indomethacin-induced gastric ulcer in experimental rats | doi:10.1080/01480545.2019.1685537 
     used: A:antioxidant
     C: Thus, EEHO possesses gastroprotective activity where the gastroprotection is by strengthening of the gastric mucosa and reduction of oxidative stress. The gastroprotective activity of EEHO was comparable to that of standard drug ranitidine.
  REF-1802 [preclinical] 2022 Journal of Molecular Neuroscience | The Effects of Methanol Extracts of Hyssopus officinalis on Model of Induced Glioblastoma Multiforme (GBM) in Rats | doi:10.1007/s12031-022-02058-y 
     used: A:anticancer, D:cancer
     C: Moreover, the histological analysis indicated a considerable decrease in invasion of tumor cells and inflammation in the hyssop-treated rats. According to the achieved results, it can be stated that hyssop has sufficient potential to inhibit damage of brain tumors, at least in part, by affecting the oxidative stress and cell proliferation pathways.
     !NULL: Given the complexity of pathophysiological processes of brain tumors, ineffective therapies, and high mortality rate, new therapeutic options with less toxicity are necessary.
  REF-1803 [preclinical] 2022 BMC Research Notes | The impact of Hyssop (Hyssopus officinalis) extract on activation of endosomal toll like receptors and their downstream signaling pathways | doi:10.1186/s13104-022-06253-3 
     used: A:expectorant, M:bronchitis, M:cough, M:respiratory-support
     C: Moreover, the release of INF-α and β notably enhanced in cell culture supernatant, while the content of inflammatory cytokines remarkably diminished (P < 0.05). The Hyssop extract was capable of inducing antiviral innate immune responses so can be promising in antiviral drug strategies.
  REF-1804 [preclinical] 2014 Experimental and Therapeutic Medicine | Effect of Hyssopus officinalis L. on inhibiting airway inflammation and immune regulation in a chronic asthmatic mouse model | doi:10.3892/etm.2014.1978 
     used: A:anti-inflammatory, A:expectorant, D:inflammation, D:respiratory-support
     C: However, the EOS ratio in the BALF and the levels of serum IgE and IgG in the Hyssopus officinalis L. treatment group were similar to the results observed in the normal group. In conclusion, Hyssopus officinalis L. not only plays an anti-inflammatory role by inhibiting the invasion of EOS and decreasing the levels of IgE, but also affects immune regulation.
  REF-1806 [preclinical] 2021 Plants | Wild Italian Hyssopus officinalis subsp. aristatus (Godr.) Nyman: From Morphological and Phytochemical Evidences to Biological Activities | doi:10.3390/plants10040631 
     used: A:antioxidant
     C: Safety of use coupled with chemical characterization of this new chemotype set the stage for a better standardization of H. officinalis EOs. The ethanolic extracts, on the other hand, with qualitatively similar chemical profiles in which caftaric, chlorogenic and rosmarinic acid were the main molecules, showed interesting antioxidant activity and a slight cytotoxicity towards the A549 cell line that could indicate a 
     !NULL: In 2017 European Food Safety Authority (EFSA) reported the genotoxicity of similar compounds, therefore, to dismiss any safety concern for the CIV17-EO use as flavouring substance, the Ames test was performed with no evidence of mutagenic activity.
  REF-1808 [preclinical] 2024 Plants | Exploring Conventional and Green Extraction Methods for Enhancing the Polyphenol Yield and Antioxidant Activity of Hyssopus officinalis Extracts | doi:10.3390/plants13152105 
     used: A:antioxidant
     C: The total polyphenol was noted at 70.65 ± 2.76 mg gallic acid equivalents (GAE)/g dry weight (dw) using the aforementioned techniques, and the antioxidant activity was noted as 582.23 ± 16.88 μmol ascorbic acid equivalents (AAE)/g dw (with FRAP method) and 343.75 ± 15.61 μmol AAE/g dw (with the DPPH method). The as-prepared extracts can be utilized in the food and cosmetics industries to bestow or enhance the antioxi

## inonotus-obliquus - Inonotus obliquus - Chaga, Chaga mushroom, clinker polypore
actions: anti-inflammatory=['REF-0093', 'REF-0272', 'REF-2195', 'REF-2196', 'REF-2200', 'REF-2204', 'REF-2970', 'REF-2974', 'REF-2982', 'REF-2985']; anticancer=['REF-0093', 'REF-2970', 'REF-2972', 'REF-2976', 'REF-2977', 'REF-2981', 'REF-2983', 'REF-2986']; antimicrobial=['REF-0093', 'REF-0272']; antioxidant=['REF-0093', 'REF-0272', 'REF-2199', 'REF-2201', 'REF-2203', 'REF-2984', 'REF-2990']; immunomodulator=['REF-0093', 'REF-0272', 'REF-2195', 'REF-2198', 'REF-0849', 'REF-2969', 'REF-2971', 'REF-2974', 'REF-2981', 'REF-2987', 'REF-2992']; nephroprotective=['REF-2975']; neuroprotective=['REF-2979', 'REF-2990']; antidiabetic=['REF-2980', 'REF-2986', 'REF-2989', 'REF-2991']; hepatoprotective=['REF-2983']; lipid-lowering=['REF-2988', 'REF-2991']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0093', 'REF-2196', 'REF-2200', 'REF-2204', 'REF-2970', 'REF-2974', 'REF-2982', 'REF-0272'] M=['REF-2195<anti-inflammatory', 'REF-2985<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-0093', 'REF-2970', 'REF-2976'] N=[] X=[] M=['REF-2972<anticancer', 'REF-2977<anticancer', 'REF-2981<anticancer', 'REF-2983<anticancer', 'REF-2986<anticancer']
- **cold** [needs-review,ev1] note="inferred from immunomodulator action"
    D=[] N=[] X=['REF-0093', 'REF-2969', 'REF-2974', 'REF-2987', 'REF-0272'] M=['REF-2195<immunomodulator', 'REF-2198<immunomodulator', 'REF-0849<immunomodulator', 'REF-2971<immunomodulator', 'REF-2981<immunomodulator', 'REF-2992<immunomodulator']
- **immune-support** [verified,ev2] note=""
    D=['REF-2969'] N=[] X=['REF-0093', 'REF-2974', 'REF-2987', 'REF-0272'] M=['REF-2195<immunomodulator', 'REF-2198<immunomodulator', 'REF-0849<immunomodulator', 'REF-2971<immunomodulator', 'REF-2981<immunomodulator', 'REF-2992<immunomodulator']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0093', 'REF-0272'] M=['REF-2195<anti-inflammatory', 'REF-2196<anti-inflammatory', 'REF-2200<anti-inflammatory', 'REF-2204<anti-inflammatory', 'REF-2970<anti-inflammatory', 'REF-2974<anti-inflammatory', 'REF-2982<anti-inflammatory', 'REF-2985<anti-inflammatory']
- **metabolic-support** [needs-review,ev1] note=""
    D=[] N=[] X=[] M=['REF-2980<antidiabetic', 'REF-2986<antidiabetic', 'REF-2989<antidiabetic', 'REF-2991<antidiabetic']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0093', 'REF-2200', 'REF-2204', 'REF-2970', 'REF-2974', 'REF-2982', 'REF-0272'] M=['REF-2195<anti-inflammatory', 'REF-2196<anti-inflammatory', 'REF-2985<anti-inflammatory']
- **cognitive-function** [needs-review,ev2] note="Chaga extract improved learning and memory in mice with drug-induced amnesia (preclinical)"
    D=['REF-2990'] N=[] X=['REF-2979'] M=[]
- **cardiovascular-support** [needs-review,ev2] note="Chaga polysaccharide lowered lipids in vivo and in vitro."
    D=['REF-2988'] N=[] X=[] M=['REF-2991<lipid-lowering']
  REF-0093 [preclinical] 2018  | Chaga (Inonotus obliquus), a future potential medicinal fungus in oncology? A chemical study and a comparison of the cytotoxicity against human lung a | doi:10.1177/1534735418757912 
     used: A:anti-inflammatory, A:anticancer, A:antimicrobial, A:antioxidant, A:immunomodulator, D:cancer
     C: Results French Chaga contains betulin and betulinic acid at higher levels than in other Chaga, whereas the concentration of inotodiol is greater in the Canadian Chaga. Moreover, the results highlighted a cytotoxic activity of the Chaga's aqueous extract after 48 and 72 hours of exposure with a higher effect on cancer-derived cells A549 than on normal transformed cells BEAS-2B ( P = 0.025 after 48 hours of exposure an
  REF-0272 [narrative-review] 2006 Pharmaceutical Chemistry Journal | Chemical and medicobiological properties of chaga (review) | doi:10.1007/s11094-006-0194-4 
     used: A:anti-inflammatory, A:antimicrobial, A:antioxidant, A:immunomodulator
     C: The possible mechanisms of action and factors responsible for the discrepancy of data available in the literature are discussed. The physical and chemical characteristics of melanin (polyphenolic chromogenic humin-like complex present in chaga) and its role in the regulation of physiological processes are considered.
  REF-0849 [traditional] 2021 Polymers (Basel) | Recent Developments in Inonotus obliquus (Chaga mushroom) Polysaccharides: Isolation, Structural Characteristics, Biological Activities and Applicatio | doi:10.3390/polym13091441 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Furthermore, applications of IOPS were reviewed and discussed; IOPS might be a potential candidate for the treatment of cancers and type 2 diabetes. Besides, new perspectives for the future work of IOPS were also proposed.
  REF-2195 [narrative-review] 2020 Journal of Traditional and Complementary | Inonotus obliquus - from folk medicine to clinical use | doi:10.1016/j.jtcme.2020.08.003 
     used: A:anti-inflammatory, A:immunomodulator, M:arthritis, M:cold, M:immune-support, M:inflammation, M:skin-irritation
     C: This receptor may be a key factor in the anti-inflammatory, antioxidant, and anti-cancer activity of I. obliquus extracts. It can be concluded that I. obliquus fits the definition of functional food and has a potentially positive effect on health beyond basic nutrition; however, studies that meet the evidence-based medicine (EBM) criteria are needed.
  REF-2196 [preclinical] 2019 PLoS One | Inonotus obliquus attenuates histamine-induced microvascular inflammation | doi:10.1371/journal.pone.0220776 
     used: A:anti-inflammatory, M:inflammation, M:skin-irritation
     C: Mast cell activation by C48/80 similarly disrupted endothelial junctions and conducted vasodilation but only histamine was blocked by the histamine antagonist, pyrilamine not C48/80 suggesting the importance of mast cell activation. Data presented here supports that histamine induced inflammation is a major disruptor of junctional integrity, and highlights the important anti-inflammatory properties of Inonotus obliqu
  REF-2198 [narrative-review] 2009 Chinese Journal of Integrative Medicine | Progress of research on Inonotus obliquus | doi:10.1007/s11655-009-0156-2 
     used: A:immunomodulator, M:cold, M:immune-support
     C: And the applications in medicine and food were introduced. Future research on Inonotus obliquus was also discussed in order to make Inonotus obliquus obtain effective exploitation and satisfy people's demands.
  REF-2199 [preclinical] 2019 Biomolecules | Melanins of Inonotus obliquus: bifidogenic and antioxidant properties | doi:10.3390/biom9060248 
     used: A:antioxidant
     C: The greatest activating effect on bifidobacteria was established by using melanin isolated from aqueous microwave extracts in concentrations of 10 -13 , 10 -10 , 10 -5 g/cm 3 . The use of this melanin with antioxidant activity 0.67 ± 0.06 mg/g (expressed as ascorbic acid equivalent), and with redox potential -5.51 ± 2.22 mV as a prebiotic allowed the growth of Bifidobacterium bifidum 1 s to increase by 1.4 times in c
  REF-2200 [preclinical] 2022 American Journal of Translational Resear | Polysaccharide derived from Inonotus obliquus inhibits lipopolysaccharide-induced acute endometritis in mice | NO-ID 
     used: A:anti-inflammatory, M:inflammation
     C: This study proved that the mechanism of action of IOP is to inhibit the TLR4/NF-κB signaling pathway to reduce the release of pro-inflammatory cytokines from body cells, thereby alleviating the symptoms of endometritis induced by LPS. Thus, IOP may act as an effective drug in preventing and curing LPS-induced endometritis.
  REF-2201 [preclinical] 2022 Current Research in Pharmacology and Dru | Inonotus obliquus aqueous extract prevents histopathological alterations in liver induced by environmental toxicant Microcystin | doi:10.1016/j.crphar.2022.100118 
     used: A:antioxidant
     C: The molecular docking interaction of NF-κB-NIK with ergosterol peroxidase showed binding interaction between the two and showed the plausible molecular basis for the effects of IOAE in MC-LR induced liver injury. Collectively, this study revealed the deleterious effects of MC-LR on liver through generation of oxidative stress and activation of caspase-3, which were prevented by treatment with IOAE.
  REF-2203 [preclinical] 2023 FEMS Microbiology Letters | Inonotus obliquus sclerotia epidermis were different from internal tissues in compound composition, antioxidant activity, and associated fungi | doi:10.1093/femsle/fnad126 
     used: A:antioxidant
     C: The study suggests separating the epidermis and internal tissue for medicinal use. The research provides insights into the bioactive components and associated fungi of I. obliquus to inform its practical application in medicine.
     !NULL: The polysaccharide content was no significant in different parts of three sclerotia, but the epidermal polysaccharide content in two sclerotia was significantly higher than in internal tissues.
     !NULL: There was no significant difference in total antioxidant capacity among different parts of three sclerotia, and the internal tissues' total antioxidant capacity in two sclerotia was higher than the epidermis.
  REF-2204 [preclinical] 2024 Toxicology Mechanisms and Methods | Inonotus obliquus aqueous extract inhibits intestinal inflammation and insulin metabolism defects in Drosophila | doi:10.1080/15376516.2024.2368795 
     used: A:anti-inflammatory, M:inflammation
     C: In brief, Inonotus obliquus aqueous extract exhibited considerable potential as a therapeutic intervention for human diseases. Our research has established a foundational framework that supports the potential clinical implementation of Inonotus obliquus .
  REF-2969 [preclinical] 2024 Communications Biology | Fungal polysaccharides from Inonotus obliquus are agonists for Toll-like receptors and induce macrophage anti-cancer activity | doi:10.1038/s42003-024-05853-y 
     used: A:immunomodulator, D:immune-support
     C: In comparison, two prototypical particulate β-glucans, one isolated from I. obliquus and one from Saccharomyces cerevisiae (zymosan), are agonists for Dectin-1 but not TLR2 or TLR4, and are unable to trigger anti-cancer functions of macrophages. We conclude that the water-soluble polysaccharides AcF1 and AcF3 from I. obliquus have a strong potential for cancer immunotherapy by triggering multiple PRRs and by inducing
  REF-2970 [preclinical] 2021 Frontiers in Pharmacology | Inonotus obliquus Polysaccharide Ameliorates Azoxymethane/Dextran Sulfate Sodium-Induced Colitis-Associated Cancer in Mice via Activation of the NLRP3 | doi:10.3389/fphar.2020.621835 
     used: A:anti-inflammatory, A:anticancer, D:cancer, M:inflammation
     C: Finally, overexpression of NLRP3 with plasmid transfection could further enhance the activation of NLRP3 inflammasome by IOP. Taken together, these results suggest that IOP suppresses the development of CAC, possibly by activation of the NLRP3 inflammasome, and reveal that IOP may be a therapeutic drug candidate for CAC.
  REF-2971 [preclinical] 2020 Journal of Functional Foods | Bioactive triterpenoids and water-soluble melanin from Inonotus obliquus (Chaga) with immunomodulatory activity | doi:10.1016/j.jff.2020.104025 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Furthermore, the metabolites were nontoxic against the common gut bacteria E. coli and B. subtilis. The results demonstrate the anti-inflammatory and immunomodulatory effects of I. obliquus melanin and triterpenoids, which could potentially justify the consumption of this increasingly popular “edible” fungus.
  REF-2972 [preclinical] 2020 Molecules | Composition of Triterpenoids in Inonotus obliquus and Their Anti-Proliferative Activity on Cancer Cell Lines | doi:10.3390/molecules25184066 
     used: A:anticancer, M:cancer
     C: Triterpenoids in the outer part were significantly higher than those in the inner part. Anti-proliferative activity of the triterpenoid fraction from the outer part against AGS, MCF-7, and PC3 was also significantly higher than that of the inner part.
  REF-2974 [preclinical] 2017 AMB Express | Inonotus obliquus polysaccharide regulates gut microbiota of chronic pancreatitis in mice | doi:10.1186/s13568-017-0341-1 
     used: A:anti-inflammatory, A:immunomodulator, M:inflammation
     C: Bacteroidetes was found positively correlated with GSH-P X and TAOC, and Firmicutes correlated with TNF-α, TGF-β, and lipase. In conclusion, administration of IOP could regulate gut microbiota composition and diversity to a healthy profile in mice with CP, and some bacterial phylum significantly correlated with characteristic parameters.
  REF-2975 [preclinical] 2016 International Journal of Molecular Scien | Renal Protective Effects of Low Molecular Weight of Inonotus obliquus Polysaccharide (LIOP) on HFD/STZ-Induced Nephropathy in Mice | doi:10.3390/ijms17091535 
     used: A:nephroprotective
     C: Consistently, three days of LIOP (100 μg/mL) incubation also provided protection against STZ + AGEs-induced glucotoxicity in renal tubular cells (LLC-PK1), while the levels of NF-κB and TGF-β expression significantly decreased in a dose-dependent manner. Our findings demonstrate that LIOP treatment could ameliorate glucolipotoxicity-induced renal fibrosis, possibly partly via the inhibition of NF-κB/TGF-β1 signaling 
  REF-2976 [preclinical] 2016 Heliyon | Continuous intake of the Chaga mushroom (Inonotus obliquus) aqueous extract suppresses cancer progression and maintains body temperature in mice | doi:10.1016/j.heliyon.2016.e00111 
     used: A:anticancer, D:cancer
     C: Our findings suggest that the I. obliquus extract could be used as a natural remedy for cancer suppression by promoting energy metabolism.
  REF-2977 [preclinical] 2014 Oncology Reports | Polysaccharide from Inonotus obliquus inhibits migration and invasion in B16-F10 cells by suppressing MMP-2 and MMP-9 via downregulation of NF-κB sign | doi:10.3892/or.2014.3103 
     used: A:anticancer, M:cancer
     C: In addition, PIO decreased the phosphorylation levels of extracellular signal-regulated protein kinase (ERK), c-Jun N-terminal kinase (JNK) and p38 mitogen-activated protein kinase (MAPK); PIO also decreased the expression level of cyclooxygenase (COX)‑2 and inhibited the nuclear translocation of nuclear factor κB (NF-κB) in B16-F10 melanoma cells. These results suggest that PIO could suppress the invasion and migrat
  REF-2979 [preclinical] 2013 Journal of Cellular Biochemistry | 3,4‐Dihydroxybenzalacetone Protects Against Parkinson's Disease‐Related Neurotoxin 6‐OHDA Through Akt/Nrf2/Glutathione Pathway | doi:10.1002/jcb.24643 
     used: A:neuroprotective
     C: Furthermore, DBL activated stress-associated kinases such as Akt, ERK, and p38 MAPK, and PI3K or Akt inhibitors, but not ERK, p38, or JNK inhibitors, diminished DBL-induced glutathione synthesis and protection against 6-OHDA. These results suggest that DBL activates the Nrf2/glutathione pathway through PI3K/Akt, and improves survival of SH-SY5Y cells against 6-OHDA toxicity.
     !NULL: Although DBL did not reduce 6-OHDA-induced reactive oxygen species in the cell-free system, it promoted the translocation of Nrf2 to the nucleus, activated the transcription of Nrf2-dependent antioxidative genes, and increased glutathione synthesis in the cells.
  REF-2980 [preclinical] 2013 Molecules | Bioassay-Guided Isolation of DPP-4 Inhibitory Fractions from Extracts of Submerged Cultured of Inonotus obliquus | doi:10.3390/molecules18011150 
     used: A:antidiabetic, M:metabolic-support
     C: Bioactivity guided fractionation led to the identification of 19 compounds using UPLC-Q-TOF-MS. Molecular docking between the compounds and DPP-4 revealed that compounds 5, 8, 9, 14, 15 may be the active components responsible for the DPP-4 inhibitory activity.
  REF-2981 [preclinical] 2011 Journal of Medicinal Plants Research | Chemical composition and antitumor activity of polysaccharide from Inonotus obliquus | doi:10.5897/jmpr.9000346 
     used: A:anticancer, A:immunomodulator, M:cancer, M:cold, M:immune-support
     C: Furthermore, AIOPA dose-dependently stimulated macrophages to produce NO through the up-regulation of inducible NO synthase (iNOS) activity and the maximal effect occurred at a concentration of 300 ug/ml by AIOPA.These data suggest that the antitumor activity of AIOPA may be associated with its potent immunostimulating effect. Key words: Inonotus obliquus, polysaccharide, immunomodulatory, antitumor.
  REF-2982 [preclinical] 2010 Journal of Biomedicine and Biotechnology | Anti-Inflammatory Effects ofInonotus obliquusin Colitis Induced by Dextran Sodium Sulfate | doi:10.1155/2010/943516 
     used: A:anti-inflammatory, M:inflammation
     C: Extract from IO itself had a weak cytotoxic effect on murine macrophage cell line (RAW264.7 cells). Extract from IO inhibited lipopolysaccharide- (LPS-) induced, TNF-alpha, STAT1, pSTAT1, STAT6, and pSTAT6 production in RAW264.7 cells.
     !NULL: The serum immunoglobulin (Ig)E level decreased in IO treatment groups (C, D) compared to no IO treatment groups (A and B) although there was no significant difference between the IO treatment groups.
  REF-2983 [preclinical] 2008 World Journal of Gastroenterology | Chaga mushroom (Inonotus obliquus ) induces G0/G1 arrest and apoptosis in human hepatoma HepG2 cells | doi:10.3748/wjg.14.511 
     used: A:anticancer, A:hepatoprotective, M:cancer
     C: Chaga mushroom may provide a new therapeutic option, as a potential anticancer agent, in the treatment of hepatoma.
  REF-2984 [preclinical] 2007 Chemical and Pharmaceutical Bulletin | Antioxidant Small Phenolic Ingredients in Inonotus obliquus (persoon) Pilat (Chaga) | doi:10.1248/cpb.55.1222 
     used: A:antioxidant
     C: Finally, seven antioxidant components were isolated and purified from the 80% MeOH extract of Chaga fruiting body, and their chemical structures were determined as small phenolics as follows: 4-hydroxy-3,5-dimethoxy benzoic acid 2-hydroxy-1-hydroxymethyl ethyl ester (BAEE), protocatechic acid (PCA), caffeic acid (CA), 3,4-dihybenzaladehyde (DB), 2,5-dihydroxyterephtalic acid (DTA), syringic acid (SA) and 3,4-dihydrox
  REF-2985 [preclinical] 2007 Journal of Medicinal Food | Ethanol Extract of Inonotus obliquus Inhibits Lipopolysaccharide-Induced Inflammation in RAW 264.7 Macrophage Cells | doi:10.1089/jmf.2006.156 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Based on our findings, the most likely mechanism that can account for this biological effect of IOE70 involves the inhibition of NF-kappaB through the phosphatidylinositol 3-kinase/Akt/IkappaB pathway and the inhibition of JNK activation. Thus, IOE70 might have useful clinical applications in the management of inflammatory diseases and may also be useful as a medicinal food.
  REF-2986 [preclinical] 1999 International journal of medicinal mushr | Antitumor and Hypoglycemic Activities of Polysaccharides from the Sclerotia and Mycelia of Inonotus obliquus (Pers.: Fr.) Pil. (Aphyllophoromycetideae | doi:10.1615/intjmedmushr.v1.i4.20 
     used: A:anticancer, A:antidiabetic, M:cancer, M:metabolic-support
     C: The active principles were β-glucan, heteroglucan, and their protein complexes. No clear antienzymic traits were recognized by polysaccharides prepared from mycelia, but the hypoglycemic effect maintained for 3−48 h by the injection was recognized.
  REF-2987 [preclinical] 2022 International Journal of Biological Macr | A polysaccharide from Inonotus obliquus ameliorates intestinal barrier dysfunction in mice with type 2 diabetes mellitus | doi:10.1016/j.ijbiomac.2022.06.071 
     used: A:immunomodulator
     C: Furthermore, the abundance of Firmicutes was significantly increased with IN treatment, while the levels of Bacteroidetes were significantly inhibited. In conclusion, IN protected against type 2 diabetes mellitus by ameliorating intestinal barrier dysfunction and might serve as a novel drug candidate for type 2 diabetes mellitus.
  REF-2988 [preclinical] 2021 Foods | Lipid-Lowering Effects of Inonotus obliquus Polysaccharide In Vivo and In Vitro | doi:10.3390/foods10123085 
     used: A:lipid-lowering, D:cardiovascular-support
     C: IOP could activate AMPK but decrease the SREBP-1C, FAS, and ACC protein expression related to adipose synthesis in mice. IOP has a certain potential for lipid-lowering effects both in vivo and in vitro.
  REF-2989 [preclinical] 2017 PLoS ONE | Antidiabetic activities of polysaccharides separated from Inonotus obliquus via the modulation of oxidative stress in mice with streptozotocin-induced | doi:10.1371/journal.pone.0180476 
     used: A:antidiabetic, M:metabolic-support
     C: These results show that IOs treatment attenuated diabetic and renal injure in STZ-induced diabetic mice, possibly through the modulation of oxidative stress and inflammatory factors. These results provide valuable evidences to support the use of I. obliquus as a hypoglycemic functional food and/or medicine.
  REF-2990 [preclinical] 2011 Food & Function | Amelioration of scopolamine induced cognitive dysfunction and oxidative stress by Inonotus obliquus– a medicinal mushroom | doi:10.1039/c1fo10037h 
     used: A:antioxidant, A:neuroprotective, D:cognitive-function
     C: Thus, the significant cognitive enhancement observed in mice after MEC administration is closely related to higher brain anti-oxidant properties and inhibition of AChE activity. These findings stress the critical impact of Chaga, a medicinal mushroom, on the higher brain functions like learning and memory.
  REF-2991 [preclinical] 2014 Phytotherapy Research | Insulin‐Sensitizing and Beneficial Lipid‐Metabolic Effects of the Water‐Soluble Melanin Complex Extracted from Inonotus obliquus | doi:10.1002/ptr.5131 
     used: A:antidiabetic, A:lipid-lowering, M:cardiovascular-support, M:metabolic-support
     C: Similarly, the epididymal adipose tissue of melanin complex-treated HF-fed mice had higher expression of fatty acid oxidative genes without significant change in lipogenic gene expression. Together, these results suggest that the water-soluble melanin complex of I. obliquus exerts antihyperglycemic and beneficial lipid-metabolic effects, making it a candidate for promising antidiabetic agent.
     !NULL: Melanin complex-treated 3T3-L1 cells showed no significant change in expression of several lipogenic genes, whereas enhanced expressions of fatty acid oxidative genes were observed.
  REF-2992 [preclinical] 2005 Mycobiology | Immunomodulatory Activity of the Water Extract from Medicinal MushroomInonotus obliquus | doi:10.4489/myco.2005.33.3.158 
     used: A:immunomodulator, M:cold, M:immune-support
     C: Also, the level of TNF-α was elevated by the chemical treatment in control mice, whereas was maintained at the background level in the extract-treated mice, indicating that the extract might effectively suppress TNF-α related pathologic conditions. These results strongly suggest the great potential of the aqueous extract from Inonotus obliquus as immune enhancer during chemotherapy.

## inula-helenium - Inula helenium - Elecampane, Horse-heal, Elf dock
actions: anti-inflammatory=['REF-0538', 'REF-1858', 'REF-1859', 'REF-1860', 'REF-1861']; anticancer=['REF-1865', 'REF-1866', 'REF-1867']; antimicrobial=['REF-0445', 'REF-0539', 'REF-0540', 'REF-1862']; expectorant=['REF-0445', 'REF-1858']
- **arthritis** [verified,ev2] note="Anti-inflammatory - sesquiterpene lactones (alantolactone, isoalantolactone) inhibit NF-kB and MAPK signalling and pro-inflammatory cytokines; total sesquiterpene lactones eased arthritis in animal models (potential in rheumatoid arthritis)"
    D=['REF-0538'] N=[] X=['REF-1858', 'REF-1859', 'REF-1860'] M=['REF-1861<anti-inflammatory']
- **bronchitis** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=['REF-0445'] M=['REF-1858<expectorant']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1865', 'REF-1866', 'REF-1867'] N=[] X=[] M=[]
- **cough** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=['REF-0445'] M=['REF-1858<expectorant']
- **infection** [verified,ev2] note="Antimicrobial, notably anti-staphylococcal (membrane-damaging) and anti-mycobacterial (active against Mycobacterium tuberculosis in vitro); supports respiratory and skin infection"
    D=['REF-0445', 'REF-0539', 'REF-0540'] N=[] X=[] M=['REF-1862<antimicrobial']
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0538'] N=[] X=[] M=['REF-1858<anti-inflammatory', 'REF-1859<anti-inflammatory', 'REF-1860<anti-inflammatory', 'REF-1861<anti-inflammatory']
- **respiratory-support** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=['REF-0445'] M=['REF-1858<expectorant']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=['REF-0538', 'REF-1858'] M=['REF-1859<anti-inflammatory', 'REF-1860<anti-inflammatory', 'REF-1861<anti-inflammatory']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-0540', 'REF-0445', 'REF-0539'] M=['REF-1862<antimicrobial']
  REF-0445 [preclinical] 2022 Molecules | From Monographs to Chromatograms: The Antimicrobial Potential of Inula helenium L. (Elecampane) Naturalised in Ireland | doi:10.3390/molecules27041406 
     used: A:antimicrobial, A:expectorant, D:infection
     C: The findings suggest that the geographical origin of the plant does not influence the anti-bacterial potency nor the chemical composition of traditional elecampane root. Considering the prevalence of staphylococci-associated infections and associated broad spectrum resistance in Irish hospitals, currently, further research is warranted into the usage of the identified compounds as potential candidates in the control 
  REF-0538 [preclinical] 2016 Journal of Ethnopharmacology | Total sesquiterpene lactones prepared from Inula helenium L. has potentials in prevention and therapy of rheumatoid arthritis | doi:10.1016/j.jep.2016.12.020 
     used: A:anti-inflammatory, D:arthritis, D:inflammation
     C: These results indicated potentials of TSL-IHL in prevention and therapy of rheumatoid arthritis.
  REF-0539 [preclinical] 2012 European Journal of Clinical Microbiolog | Antistaphylococcal activity of Inula helenium L. root essential oil: eudesmane sesquiterpene lactones induce cell membrane damage | doi:10.1007/s10096-011-1400-1 
     used: A:antimicrobial, D:infection
     C: The essential oil showed very potent antistaphylococcal activity, with obvious membrane-damaging effects. Sesquiterpene lactones were found to be the most active principles of the oil, whose eudesmane core olefinic bonds, along with the α,β-methylene-lactone ring, are essential structural parts responsible for the exhibited antimicrobial activity.
  REF-0540 [preclinical] 1999 Planta Medica | Antimycobacterial eudesmanolides from Inula helenium and Rudbeckia subtomentosa | doi:10.1055/s-1999-14001 
     used: A:antimicrobial, D:infection
     C: Alantolactone, isoalantolactone and its 4 alpha, 15-epoxide, 1,2-dehydro-3-epi-isotelekin and alloalantolactone gave MICs of 32 micrograms ml-1. All other compounds showed MIC values of 128 micrograms ml-1 or higher.
  REF-1858 [preclinical] 2019 Journal of Ethnopharmacology | Inula helenium and Grindelia squarrosa as a source of compounds with anti-inflammatory activity in human neutrophils and cultured human respiratory ep | doi:10.1016/j.jep.2019.112311 
     used: A:anti-inflammatory, A:expectorant, M:bronchitis, M:cough, M:inflammation, M:respiratory-support
     C: The present study demonstrated that Inula helenium and Grindelia squarrosa, which have been traditionally used in Europe as medicinal plants, are a valuable source of active compounds with anti-inflammatory activity. Our observations justify the traditional use of I. helenium and G. squarrosa for a treatment of inflammation-based diseases in respiratory tract.
  REF-1859 [preclinical] 2018 Phytomedicine | Total sesquiterpene lactones isolated from Inula helenium L. attenuates 2,4-dinitrochlorobenzene-induced atopic dermatitis-like skin lesions in mice | doi:10.1016/j.phymed.2018.04.036 
     used: A:anti-inflammatory, M:inflammation, M:skin-irritation
     C: We suggest that TSL-IHL inhibited the development of AD-like skin symptoms by regulating cytokine expression and may be an effective alternative therapy for AD.
  REF-1860 [preclinical] 2020 Inflammation Research | Igalan from Inula helenium (L.) suppresses the atopic dermatitis-like response in stimulated HaCaT keratinocytes via JAK/STAT3 signaling | doi:10.1007/s00011-020-01322-4 
     used: A:anti-inflammatory, M:inflammation, M:skin-irritation
     C: These findings indicate that igalan, via suppressing JAK/STAT3 signaling, could impair the production of pro-inflammatory chemokines and enhance expression levels of several genes involved in keratinocyte differentiation in AD-like stimulated keratinocytes.
  REF-1861 [preclinical] 2020 International Journal of Biological Macr | Natural soluble epoxide hydrolase inhibitors from Inula helenium and their interactions with soluble epoxide hydrolase | doi:10.1016/j.ijbiomac.2020.04.227 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The inhibition kinetics suggested that 4H-tomentosin (1) and xanthalongin (2) were mixed-competitive type inhibitors with inhibition constant (Ki) values of 7.02 and 6.57 μM, respectively, and linoleic acid (3) was a competitive type inhibitor with a Ki values of 3.52 μM. The potential interactions of 4H-tomentosin (1), xanthalongin (2), and linoleic acid (3) with sEH were analyzed by molecular docking, which indicat
  REF-1862 [preclinical] 2022 Molecules | Biological Activities and Chemical Profile of Gentiana asclepiadea and Inula helenium Ethanolic Extracts | doi:10.3390/molecules27113560 
     used: A:antimicrobial, M:infection, M:wounds
     C: Rat intestinal epithelial cell viability was not affected by the selected concentrations of these two extracts. These data support the ethnomedicinal recommendations of these species and highlight them as valuable sources of bioactive compounds.
  REF-1865 [preclinical] 2018 Phytotherapy Research | Sesquiterpene lactones-enriched fraction of Inula helenium L. induces apoptosis through inhibition of signal transducers and activators of transcripti | doi:10.1002/ptr.6189 
     used: A:anticancer, D:cancer
     C: Our results suggest that HFIH possesses potential anticancer activity, which is mainly mediated through STAT3 signaling pathway. These findings provide the potential of HFIH as a promising phytomedicine for the treatment and prevention of triple-negative breast cancer.
  REF-1866 [preclinical] 2012 Zeitschrift fur Naturforschung C | Antitumour activities of sesquiterpene lactones from Inula helenium and Inula japonica | doi:10.1515/znc-2012-7-804 
     used: A:anticancer, D:cancer
     C: Compounds 3 and 6 were not toxic to human embryonic lung fibroblast cells in vitro. These results demonstrated that the antitumour activities are closely related to the structures of the compounds, that is, an alpha-exomethylene-gamma-lactone ring is necessary for these activities.
  REF-1867 [preclinical] 2019 Natural Product Research | Active ingredients of Inula helenium L. exhibits similar anti-cancer effects as isoalantolactone in pancreatic cancer cells | doi:10.1080/14786419.2018.1543676 
     used: A:anticancer, D:cancer
     C: In addition, F35 inhibited colony-formation and migration of PANC-1 and SW1990 cells. To conclude, F35 exhibited similar anti-proliferation and anti-migration effect as isoalantolactone on two pancreatic cancer cell lines, suggesting that alantolactone or alloalantolactone might have comparable anti-tumor effect as isoalantolactone.

## juniperus-communis - Juniperus communis - Common Juniper, Juniper, Juniper “berries” / juniper cone berries
actions: anticancer=['REF-0853', 'REF-1742', 'REF-1743', 'REF-1744']; antimicrobial=['REF-0035', 'REF-3066', 'REF-1734', 'REF-1735', 'REF-1737', 'REF-1738', 'REF-1739', 'REF-1745']; antioxidant=['REF-0035', 'REF-3066', 'REF-1734', 'REF-1736', 'REF-1740', 'REF-1741']; digestive=['REF-0035', 'REF-3066', 'REF-1736']; diuretic=['REF-0035', 'REF-3066', 'REF-1735', 'REF-1741']; urinary-antiseptic=['REF-0035', 'REF-3066']
- **bloating** [needs-review,ev1] !INF note="inferred from digestive action"
    D=['REF-3066'] N=[] X=['REF-0035'] M=['REF-1736<digestive']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-0853', 'REF-1742', 'REF-1743', 'REF-1744'] N=[] X=[] M=[]
- **indigestion** [needs-review,ev1] !INF note="inferred from digestive action"
    D=['REF-3066'] N=[] X=['REF-0035'] M=['REF-1736<digestive']
- **infection** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-3066', 'REF-0035'] M=['REF-1734<antimicrobial', 'REF-1735<antimicrobial', 'REF-1737<antimicrobial', 'REF-1738<antimicrobial', 'REF-1739<antimicrobial', 'REF-1745<antimicrobial']
- **swelling** [needs-review,ev1] note="inferred from diuretic action"
    D=[] N=[] X=['REF-1741', 'REF-0035', 'REF-3066'] M=['REF-1735<diuretic']
- **urinary-support** [needs-review,ev1] !INF note="inferred from diuretic action"
    D=['REF-3066'] N=[] X=['REF-0035'] M=['REF-1735<diuretic', 'REF-1741<diuretic']
- **uti** [needs-review,ev1] note="inferred from diuretic action"
    D=[] N=[] X=['REF-1741', 'REF-0035', 'REF-3066'] M=['REF-1735<diuretic']
- **wounds** [needs-review,ev1] note="inferred from antimicrobial action"
    D=[] N=[] X=['REF-3066', 'REF-1737', 'REF-1738', 'REF-0035'] M=['REF-1734<antimicrobial', 'REF-1735<antimicrobial', 'REF-1739<antimicrobial', 'REF-1745<antimicrobial']
  REF-0035 [traditional] 1983  | British Herbal Pharmacopoeia | NO-ID 
     used: A:antimicrobial, A:antioxidant, A:digestive, A:diuretic, A:urinary-antiseptic
     (no abstract)
  REF-0853 [preclinical] 2024 Plants (Basel) | Insights into Molecular Mechanisms of Anticancer Activity of Juniperus communis Essential Oil in HeLa and HCT 116 Cells | doi:10.3390/plants13172351 
     used: A:anticancer, D:cancer
     C: The obtained in silico and in vitro results indicated the anticancer potential of J. communis berry essential oil as it interferes with cancer cell molecular mechanisms. Our findings highlight J. communis berry essential oil as a promising natural agent with anticancer potential.
  REF-1734 [narrative-review] 2022 International Journal of Molecular Scien | Zimbro (Juniperus communis L.) as a Promising Source of Bioactive Compounds and Biomedical Activities: A Review on Recent Trends | doi:10.3390/ijms23063197 
     used: A:antimicrobial, A:antioxidant, M:infection, M:wounds
     C: In the last few years, several studies have analyzed the huge potential of this evergreen shrub, describing a wide range of activities with relevance in different biomedical discipline areas, namely antimicrobial potential against human pathogens and foodborne microorganisms, notorious antioxidant and anti-inflammatory activities, antidiabetic, antihypercholesterolemic and antihyperlipidemic effects, and neuroprotect
  REF-1735 [narrative-review] 2014 International Scholarly Research Notices | A Phytopharmacological Review on a Medicinal Plant: Juniperus communis | doi:10.1155/2014/634723 
     used: A:antimicrobial, A:diuretic, M:infection, M:swelling, M:urinary-support, M:uti, M:wounds
     C: The main chemical constituents, which were reported in J. communis L. are α-pinene, β-pinene, apigenin, sabinene, β-sitosterol, campesterol, limonene, cupressuflavone, and many others. This review includes the last 20 years journals and various books update on this plant, representing its pharmacological activity and health benefits against various diseases.
  REF-1736 [narrative-review] 2019 Heliyon | Potential of Juniperus communis L as a nutraceutical in human and veterinary medicine | doi:10.1016/j.heliyon.2019.e02376 
     used: A:antioxidant, A:digestive, M:bloating, M:indigestion
     C: Thus natural antioxidant such as juniper can be used in place synthetic antioxidant for the preservation and improving self-life of meat products. New well designed clinical trials in human and animals using well-characterized J. communis extract or oil need to be conducted so that additional information is generated which can support the use of this natural product as a nutraceutical.
  REF-1737 [preclinical] 2009 Journal of Ethnopharmacology | Antimycobacterial terpenoids from Juniperus communis L. (Cuppressaceae) | doi:10.1016/j.jep.2009.09.007 
     used: A:antimicrobial, M:infection
     C: The presence of antimycobacterial terpenoids in Juniperus communis aerial parts and roots justifies, to some extent, the ethnomedicinal use of this species as a traditional anti-TB remedy.
  REF-1738 [preclinical] 2017 Phytotherapy Research | Antiadhesion activity of juniper (Juniperus communis L.) preparations against Campylobacter jejuni evaluated with PCR-based methods | doi:10.1002/ptr.6005 
     used: A:antimicrobial, M:infection
     C: Furthermore, ≥94% of the antiadhesion activity of juniper fruit crude extract and juniper fruit essential oil remained under food-related conditions: modified culture medium with glucose, or a stainless steel surface, or mixed co-cultures of C. jejuni and Listeria monocytogenes. This study indicates that addition of juniper fruit formulations can control growth and adhesion of C. jejuni and thus limit food chain tran
  REF-1739 [preclinical] 2018 Chemistry & Biodiversity | Chemical Composition, Cytotoxic and Antibacterial Activities of Essential Oils of Cultivated Clones of Juniperus communis and Wild Juniperus Species | doi:10.1002/cbdv.201800183 
     used: A:antimicrobial, M:infection, M:wounds
     C: EOs exhibited better antibacterial activity against Gram-positive bacteria than against Gram-negative bacteria with the highest zone of inhibition against Staphylococcus aureus MTCC 96 (19.2 ± 0.7) by clone-7. As per the conclusion of the findings, EOs of clone-2, clone-5 and clone-7 can be suggested to the growers of lower altitude, as there is more possibility of uses of these EOs in food and medicinal preparations
  REF-1740 [preclinical] 2016 Bioscience, Biotechnology, and Biochemis | Tyrosinase inhibitory flavonoid from Juniperus communis fruits | doi:10.1080/09168451.2016.1217146 
     used: A:antioxidant
     C: This is the first report of the enzyme tyrosinase inhibition by J. communis and its constituent. Therapeutic attempts with J. communis and its active component, hypolaetin 7-O-β-D-xylopyranoside, might be useful in treating melanin pigmentary disorders.
  REF-1741 [preclinical] 2022 Food Science & Nutrition | Juniperus communis extract ameliorates lipopolysaccharide-induced acute kidney injury through the adenosine monophosphate-activated protein kinase pat | doi:10.1002/fsn3.2941 
     used: A:antioxidant, A:diuretic, M:urinary-support
     C: In LPS-stimulated NRK-52E cells, JCo extract inhibited nuclear factor-κB (NF-κB) and increased adenosine monophosphate-activated protein kinase (AMPK) expression, prompting the activation of the antioxidant nuclear factor erythroid 2-related factor-2/heme oxygenase-1 pathway against oxidative stress. JCo extract ameliorated LPS-induced acute kidney injury by suppressing NF-κB signaling and stimulating the release of 
  REF-1742 [preclinical] 2019 The American Journal of Chinese Medicine | Juniperus communis Suppresses Melanoma Tumorigenesis by Inhibiting Tumor Growth and Inducing Apoptosis | doi:10.1142/S0192415X19500605 
     used: A:anticancer, D:cancer
     C: Additionally, JCo extract also reduced cancer stem cell-related angiogenic and metastatic proteins in the process of tumor elimination. Based on these results, this study suggests that JCo extract suppresses tumor growth and induces apoptosis, and JCo extract may be useful for the prevention of melanoma tumorigenesis.
  REF-1743 [preclinical] 2021 Bioscience Reports | Evaluation of anticancer effects of Juniperus communis extract on hepatocellular carcinoma cells in vitro and in vivo | doi:10.1042/BSR20211143 
     used: A:anticancer, D:cancer
     C: JCo extract significantly up-regulated the expression of pro-apoptotic proteins and tumor suppressor p53, suppressed VEGF/VEGFR autocrine signaling, down-regulated cell cycle regulatory proteins and MMP2/MMP9 proteins. Overall, our results provide a basis for exploiting JCo extract as a potential anticancer agent against HCC.
  REF-1744 [preclinical] 2021 Brazilian Journal of Medical and Biologi | Juniperus communis extract induces cell cycle arrest and apoptosis of colorectal adenocarcinoma in vitro and in vivo | doi:10.1590/1414-431X2020e10891 
     used: A:anticancer, D:cancer
     C: In addition, there was no obvious change in body weight or histological morphology of normal organs after treatment. JCo extract suppressed CRC progression by inducing cell cycle arrest and apoptosis in vitro and in vivo, suggesting the potential application of JCo extract in the treatment of CRC.
  REF-1745 [preclinical] 2019 Journal of Medical Microbiology | Synergistic potential of Juniperus communis and Helichrysum italicum essential oils against nontuberculous mycobacteria | doi:10.1099/jmm.0.000962 
     used: A:antimicrobial, M:infection, M:wounds
     C: The leakage of the cellular material is noticeably higher in sMIC, which is probably due to cell wall damage. sMIC of both EOs have an additive or synergistic effect, reducing MICs, limiting adhesion and preventing the formation of biofilms.
  REF-3066 [traditional] 2023  | European Union herbal monograph on Juniperus communis L., galbulus (pseudo-fructus), Revision 1 | NO-ID 
     used: A:antimicrobial, A:antioxidant, A:digestive, A:diuretic, A:urinary-antiseptic, D:bloating, D:indigestion, D:urinary-support
     (no abstract)

## knautia-arvensis - Knautia arvensis - Field scabious, blue buttons, gypsy rose
actions: alterative=[]; anti-inflammatory=[]; antioxidant=['REF-2814']; antimicrobial=[]
  REF-2814 [preclinical] 2024 Chemistry and Biodiversity | Investigation of Phytochemical, Antioxidant and Antidiabetic Potentials of Scabiosa L. (Caprifoliaceae) Species with Chemometric Methods | doi:10.1002/cbdv.202301652 !SP
     used: A:antioxidant
     C: The extracts showed high α-amylase and α-glucosidase inhibitory activity. The results show that Scabiosa methanol extracts may be a source of alternative antioxidants that may be beneficial in slowing or preventing the progression of various oxidative stress-related diseases.

## lactuca-virosa - Lactuca virosa - Wild Lettuce, Bitter lettuce, Opium lettuce
actions: analgesic=['REF-0526', 'REF-0527', 'REF-0622', 'REF-2060']; antitussive=['REF-0526', 'REF-2059']; anxiolytic=['REF-0526']; sedative=['REF-0526', 'REF-0622', 'REF-2060', 'REF-2061', 'REF-2062']
- **anxiety** [needs-review,ev1] !INF note="inferred from anxiolytic action"
    D=['REF-0526'] N=[] X=[] M=[]
- **back-pain** [needs-review,ev1] note="inferred from analgesic action"
    D=[] N=[] X=['REF-0526', 'REF-0527', 'REF-0622'] M=['REF-2060<analgesic']
- **cough** [needs-review,ev1] note="Antitussive for an irritable, dry cough (traditional)"
    D=['REF-0526', 'REF-0527'] N=[] X=[] M=[]
- **headache** [needs-review,ev1] note="inferred from analgesic action"
    D=[] N=[] X=['REF-0526', 'REF-0527', 'REF-0622'] M=['REF-2060<analgesic']
- **insomnia** [needs-review,ev2] note="Sedative for sleeplessness / insomnia - lactucin and lactucopicrin showed sedative activity in animal models"
    D=['REF-0526', 'REF-0622', 'REF-0527'] N=[] X=['REF-2061', 'REF-2062'] M=['REF-2060<sedative']
- **nervous-tension** [needs-review,ev1] note="Calming for nervous tension and restlessness"
    D=['REF-0526'] N=[] X=[] M=[]
- **pain** [needs-review,ev2] note="Mild analgesic / anodyne for pain (lactucin and lactucopicrin act on the central nervous system) - in mice these compounds produced analgesia comparable to ibuprofen"
    D=['REF-0526', 'REF-0527', 'REF-0622'] N=[] X=[] M=['REF-2060<analgesic']
  REF-0526 [traditional] n.d.  | Wild Lettuce (Lactuca virosa): Benefits, Uses, Safety | NO-ID 
     used: A:analgesic, A:antitussive, A:anxiolytic, A:sedative, D:anxiety, D:cough, D:insomnia, D:nervous-tension, D:pain
     (no abstract)
  REF-0527 [traditional] n.d.  | Wild Lettuce: Health Benefits, Side Effects, Uses, Dose & Precautions | NO-ID 
     used: A:analgesic, D:cough, D:insomnia, D:pain
     (no abstract)
  REF-0622 [preclinical] 2006 Journal of Ethnopharmacology | Analgesic and sedative activities of lactucin and some lactucin-like guaianolides in mice | doi:10.1016/j.jep.2006.03.003 
     used: A:analgesic, A:sedative, D:insomnia, D:pain
     C: Lactucopicrin appeared to be the most potent analgetic of the three tested compounds. Lactucin and lactucopicrin, but not 11beta,13-dihydrolactucin, also showed sedative properties in the spontaneous locomotor activity test.
  REF-2059 [traditional] 1815 Medico-Chirurgical Transactions | On the use of the Lactuca Virosa, in Hooping-Cough | doi:10.1177/095952871500600125 
     used: A:antitussive
     (no abstract)
  REF-2060 [traditional] 2005 Kwartalnik Historii Nauki i Techniki | Lettuce, Lactuca sp., as a medicinal plant in Polish publications of the 19th century | NO-ID 
     used: A:analgesic, A:sedative, M:back-pain, M:headache, M:insomnia, M:pain
     C: The possibility of obtaining lactucarium from plants cultivated in Poland caused Polish pharmacists and physicians to take an interest in the stuff and launch their own research of lettuce and the lactescent juice obtained from it. Results of research on lettuce were published in 19th-century journals by, among others, Jan Fryderyk Wolfgang, Florian Sawiczewski and Józef Orkisz.
     !NULL: However, such studies failed to produce the expected results, and the component responsible for the curative properties of letuce was not identified.
  REF-2061 [preclinical] 2003 Presse Medicale | Abuse of Lactuca virosa | NO-ID 
     used: A:sedative
     (no abstract)
  REF-2062 [narrative-review] 2019 Journal of Pharmaceutical and Biomedical | Biomedical analysis of New Psychoactive Substances (NPS) of natural origin | doi:10.1016/j.jpba.2019.112945 
     used: A:sedative
     C: The psychoactive principles contained in the following plants were investigated: Areca catechu, Argyreia nervosa, Ayahuasca, Catha edulis, Ipomoea violacea, Mandragora officinarum, Mitragyna speciosa, Pausinystalia yohimbe, Piper methisticum, Psilocybe, Rivea corymbosa, Salvia divinorum, Sceletium tortuosum, Lactuca virosa. From the results obtained, it can be evidenced that although several analytical methods for th

## lamium-album - Lamium album - White Dead Nettle, White dead-nettle, Bee nettle
actions: anti-inflammatory=['REF-0348', 'REF-1746', 'REF-1747', 'REF-1751']; antioxidant=['REF-0342', 'REF-1749']; astringent=['REF-0348', 'REF-1752']; expectorant=['REF-1753']; vulnerary=['REF-0348', 'REF-1756']
- **arthritis** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0348'] N=[] X=['REF-1751'] M=['REF-1746<anti-inflammatory', 'REF-1747<anti-inflammatory']
- **bronchitis** [needs-review,ev2] !INF note="inferred from expectorant action"
    D=['REF-1746'] N=[] X=[] M=['REF-1753<expectorant']
- **bruising** [needs-review,ev1] !INF note="inferred from vulnerary action"
    D=['REF-0348'] N=[] X=['REF-1756'] M=[]
- **cough** [needs-review,ev1] note="inferred from expectorant action"
    D=[] N=[] X=[] M=['REF-1753<expectorant']
- **diarrhea** [needs-review,ev1] !INF note="inferred from astringent action"
    D=['REF-0348'] N=[] X=['REF-1752'] M=[]
- **inflammation** [needs-review,ev2] !INF note="inferred from anti-inflammatory action"
    D=['REF-0348', 'REF-1746'] N=[] X=[] M=['REF-1747<anti-inflammatory', 'REF-1751<anti-inflammatory']
- **respiratory-support** [needs-review,ev1] !INF note="inferred from expectorant action"
    D=['REF-0348'] N=[] X=[] M=['REF-1753<expectorant']
- **skin-irritation** [needs-review,ev2] !INF note="inferred from astringent action"
    D=['REF-1746'] N=[] X=['REF-1751', 'REF-0348'] M=['REF-1747<anti-inflammatory', 'REF-1752<astringent']
- **wounds** [verified,ev1] note="Vulnerary (minor wounds), applied topically"
    D=['REF-0348'] N=[] X=[] M=['REF-1752<astringent', 'REF-1756<vulnerary']
  REF-0342 [traditional] 1995  | Phenylpropanoid esters from Lamium album flowers | doi:10.1016/0031-9422(94)00727-B 
     used: A:antioxidant
     C: Esters of glycosides were obtained as mixtures of trans/cis isomers. The presence of flavonoid p-coumaroylglucosides links Lamium to other members of the subfamily Lamioideae.
  REF-0348 [traditional] n.d.  | White Deadnettle (Lamium album): Benefits, Uses, Safety | NO-ID 
     used: A:anti-inflammatory, A:astringent, A:vulnerary, D:arthritis, D:bruising, D:diarrhea, D:inflammation, D:respiratory-support, D:wounds
     (no abstract)
  REF-1746 [preclinical] 2017 Planta Medica | Bioassay-Guided Isolation of Iridoids and Phenylpropanoids from Aerial Parts of Lamium album and Their Anti-inflammatory Activity in Human Neutrophils | doi:10.1055/s-0043-107031 
     used: A:anti-inflammatory, D:bronchitis, D:inflammation, D:skin-irritation, M:arthritis
     C: The phenylethanoid glycosides, such as lamiusides A, B, and C as well as 6″-O- β -D-glucopyranosylmartynoside, were isolated and identified. The cells treated with 6″- O - β -D-glucopyranosylmartynoside and lamiuside B produced 29.47 ± 7.11 % and 64.67 ± 5.25 % of interleukin 8, respectively, compared to non-treated control cells.Our results support the traditional use of L. album and indicate it as a potential sourc
  REF-1747 [preclinical] 2018 Molecules | Bioactive Constituents of Lamium album L. as Inhibitors of Cytokine Secretion in Human Neutrophils | doi:10.3390/molecules23112770 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The compounds at a concentration of 25 µM, except for shanzhiside methyl ester ( 6 ), inhibited secretion of IL-8 in the range from 29.1 to 50.0%. In conclusion, L. album might be a valuable source of bioactive compounds and may provide constituents to limit noninfectious inflammation associated with the aforementioned diseases.
  REF-1749 [preclinical] 2020 Molecules | Phenolic Constituents of Lamium album L. subsp. album Flowers: Anatomical, Histochemical, and Phytochemical Study | doi:10.3390/molecules25246025 
     used: A:antioxidant
     C: The corolla in L. album subsp. album has antioxidant properties due to the presence of various polyphenols, as shown by the histo- and phytochemical analyses. The distribution and morphology of trichomes and the content of phenolic compounds in the corolla have taxonomic, pharmacognostic, and practical importance, facilitating the identification of the raw material.
  REF-1751 [preclinical] 2022 Folia Medica | Potential anti-inflammatory effect of Lamium album extract through caspase-3 and cyclooxygenase-2 genes expression in a rat model of middle cerebral a | doi:10.3897/folmed.64.e60562 
     used: A:anti-inflammatory, M:inflammation
     C: Introduction Stroke is one of the most common causes of death worldwide. Inflammation and apoptosis play an important role in the cascade of ischemic stroke.
  REF-1752 [preclinical] 2019 Acta Pharmaceutica | Haemostatic activity of butanolic extracts of Lamium album and Lamium purpureum aerial parts | doi:10.2478/acph-2019-0026 
     used: A:astringent, M:skin-irritation, M:wounds
     C: Based on the qualitative chemical data on iridoid glycosides (HPTLC), 8-acetylshanzhiside methyl ester might be assumed to be responsible for haemostatic activity. Based on the acute toxicity test, none of the extracts showed toxicity.
  REF-1753 [preclinical] 2018 Journal of Pharmacopuncture | Effects of standardized extracts of Lamium album and Urtica dioica on rat tracheal smooth muscle contraction | doi:10.3831/KPI.2018.21.008 
     used: A:expectorant, M:bronchitis, M:cough, M:respiratory-support
     C: The relaxant effect of L. Album on the trachea makes it as a candidate for the managing patients with asthma and obstructive pulmonary diseases. But because of U. Dioica potential constrictive effect on the trachea it is suggested that patients avoid consuming it.
  REF-1756 [preclinical] 2015 Journal of Ophthalmic & Vision Research | The Effect of Lamium album Extract on Cultivated Human Corneal Epithelial Cells (10.014 pRSV-T) | doi:10.4103/2008-322X.170349 
     used: A:vulnerary, M:wounds
     C: Selected Lamium album extracts influence human corneal epithelial cells. Generally, while not toxic, they modulate pro-inflammatory and anti-inflammatory cytokines levels, and decrease NO release by cells; moreover, ethanol and ethyl acetate extracts reduce ROS levels.
     !NULL: Results In NR and MTT assays, Lamium album extracts did not affect cell viability (80% at 125 μg/ml concentration).
