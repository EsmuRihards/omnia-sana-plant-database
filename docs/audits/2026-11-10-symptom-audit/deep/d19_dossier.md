# Deep dossier batch 19

## veronica-officinalis - Veronica officinalis - Speedwell, Common speedwell, Heath speedwell
actions: anti-inflammatory=['REF-0513']; antioxidant=['REF-0513', 'REF-1378', 'REF-2554', 'REF-2555']; digestive=['REF-0514', 'REF-2552']; expectorant=['REF-0513', 'REF-0514', 'REF-0632']
- **bloating** [needs-review,ev1] !INF note="inferred from digestive action"
    D=['REF-0514'] N=[] X=['REF-2552'] M=[]
- **bronchitis** [needs-review,ev2] !INF !NAME['REF-0632'] note="inferred from expectorant action"
    D=['REF-0514', 'REF-0632'] N=[] X=['REF-0513'] M=[]
- **cough** [needs-review,ev2] !NAME['REF-0632'] note="Traditional expectorant for cough and respiratory complaints (iridoid glycosides inhibit lung inflammation) - a standardised extract suppressed COX-2 and eotaxin via the NF-kB pathway in human lung epithelial cells"
    D=['REF-0514', 'REF-0632'] N=[] X=['REF-0513'] M=[]
- **indigestion** [needs-review,ev2] note="Mild digestive / stomach tonic (indigestion)"
    D=['REF-0514', 'REF-2552'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev2] note="Traditional expectorant for cough and respiratory complaints (iridoid glycosides inhibit lung inflammation) - a standardised extract suppressed COX-2 and eotaxin via the NF-kB pathway in human lung epithelial cells"
    D=['REF-0514', 'REF-0632'] N=[] X=['REF-0513'] M=[]
- **respiratory-support** [needs-review,ev2] !INF note="inferred from expectorant action"
    D=['REF-0514', 'REF-0632'] N=[] X=['REF-0513'] M=[]
- **skin-irritation** [needs-review,ev1] note="Soothing for skin irritation (topical)"
    D=['REF-0514'] N=[] X=['REF-0513'] M=[]
  REF-0513 [traditional] 2017 Frontiers in Pharmacology | Veronica officinalis Product Authentication Using DNA Metabarcoding and HPLC-MS Reveals Widespread Adulteration with Veronica chamaedrys | doi:10.3389/fphar.2017.00378 
     used: A:anti-inflammatory, A:antioxidant, A:expectorant
     C: This study highlights the need for authentication of raw herbals along the value chain of these products. An integrative methodology can assess both the quality of herbal products in terms of target compound concentrations and species composition, as well as admixture and substitution with other chemical compounds and plants.
  REF-0514 [traditional] n.d.  | Veronica (Speedwell) | NO-ID 
     used: A:digestive, A:expectorant, D:bloating, D:bronchitis, D:cough, D:indigestion, D:inflammation, D:respiratory-support, D:skin-irritation
     (no abstract)
  REF-0632 [preclinical] 2012 Journal of Ethnopharmacology | Traditionally used Veronica officinalis inhibits proinflammatory mediators via the NF-kB signalling pathway in a human lung cell line | doi:10.1016/j.jep.2012.10.039 
     used: A:expectorant, D:bronchitis, D:cough, D:inflammation, D:respiratory-support
     C: Our results are a contribution to explaining the observed anti-inflammatory effects of Veronica offcinalis extract on a molecular level. However, its clinical potency has at first to be proven in animals and subsequently in clinical trials.
  REF-1378 [preclinical] 2015 International Journal of Molecular Scien | Phytochemical Characterization of Veronica officinalis L., V. teucrium L. and V. orchidea Crantz from Romania and Their Antioxidant and Antimicrobial  | doi:10.3390/ijms160921109 
     used: A:antioxidant
     C: Regarding the antimicrobial activity of the investigated species, Staphylococcus aureus, Listeria monocytogenes and Listeria ivanovii were the most sensitive strains with MIC values between 3.9 and 15.62 mg/mL. The results obtained by this study may serve to promote better use of representatives from the genus Veronica as antioxidant and antimicrobial agents.
  REF-2552 [preclinical] 1985 Journal of Ethnopharmacology | Experimental anti-ulcer activity of Veronica officinalis L. extracts | doi:10.1016/0378-8741(85)90003-0 
     used: A:digestive, D:indigestion
     C: In ulcer healing experiments performed in rats by administering reserpine, the extracts were found to enhance the regeneration of the gastric mucosa. These results seem to confirm the popular observations according to which the decoction from Veronica officinalis L. possessed useful properties in the treatment of gastric ulcers.
  REF-2554 [preclinical] 1973 Acta Poloniae Pharmaceutica | Phytochemical studies of the Veronica officinalis L. | NO-ID 
     used: A:antioxidant
     (no abstract)
  REF-2555 [preclinical] 1977 Acta Poloniae Pharmaceutica | Occurrence of 6-hydroxyluteolin 7-glucoside in the herb of Veronica officinalis L. | NO-ID 
     used: A:antioxidant
     (no abstract)

## viburnum-opulus - Viburnum opulus - Cramp Bark, Guelder rose, Snowball tree
actions: analgesic=['REF-0439', 'REF-1139']; anticancer=['REF-1142']; antispasmodic=['REF-0439', 'REF-0440', 'REF-0610']
- **back-pain** [needs-review,ev1] !INF note="inferred from analgesic action"
    D=['REF-0439'] N=[] X=['REF-1139'] M=[]
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1142'] N=[] X=[] M=[]
- **headache** [needs-review,ev1] !INF note="inferred from analgesic action"
    D=['REF-0439'] N=[] X=['REF-1139'] M=[]
- **menstrual-cramps** [verified,ev2] !NAME['REF-0610'] note="Antispasmodic for menstrual cramps (relaxes uterine smooth muscle)"
    D=['REF-0439', 'REF-0440', 'REF-0610', 'REF-1140'] N=[] X=[] M=[]
- **muscle-spasm** [verified,ev1] note="Antispasmodic for general muscle spasm and cramping (smooth-muscle relaxant)"
    D=['REF-0439'] N=[] X=[] M=['REF-0440<antispasmodic', 'REF-0610<antispasmodic']
- **pain** [needs-review,ev1] note="Mild analgesic for cramping pain"
    D=['REF-0439'] N=[] X=[] M=['REF-1139<analgesic']
  REF-0439 [traditional] n.d.  | Cramp Bark (Viburnum opulus): Benefits, Uses, Safety | NO-ID 
     used: A:analgesic, A:antispasmodic, D:back-pain, D:headache, D:menstrual-cramps, D:muscle-spasm, D:pain
     (no abstract)
  REF-0440 [traditional] n.d.  | Viburnum opulus - an overview | NO-ID !TAG review-title/traditional
     used: A:antispasmodic, D:menstrual-cramps, M:muscle-spasm
     (no abstract)
  REF-0610 [traditional] 2020 Nutrients | Viburnum opulus L. - A Review of Phytochemistry and Biological Effects | doi:10.3390/nu12113398 !TAG review-title/traditional
     used: A:antispasmodic, D:menstrual-cramps, M:muscle-spasm
     C: The health benefits of VO result from the presence of bioactive components such as phenolic compounds, vitamin C, carotenoids, iridoids, and essential oils. The aim of this review is to present an overview of the botanical characteristics, chemical compositions, including bioactive compounds, and pro-health properties of VO different morphological parts.
  REF-1139 [clinical] 2021 International Journal of Clinical Practi | Gilaburu extract (Viburnum opulus Linnaeus) is as effective as Tamsulosin in medical expulsive therapy of distal ureteral calculi | doi:10.1111/ijcp.14950 
     used: A:analgesic, M:pain
     C: V. opulus can be used effectively and safely for the treatment of MET in distal ureteral calculi.
     !NULL: Results There was no difference between the groups in terms of stone expulsion rates and time until the expulsion in all stones.
  REF-1140 [preclinical] 2016 Journal of Ethnopharmacology | Viburnum opulus L.: A remedy for the treatment of endometriosis demonstrated by rat model of surgically-induced endometriosis | doi:10.1016/j.jep.2016.09.029 
     used: D:menstrual-cramps
     C: The results of the present study indicate that the effectiveness of the fruit extract of V. opulus could be partially attributed chlorogenic acid. Other phenolic compounds could potentiate the activity due to their amount.
  REF-1142 [preclinical] 2020 Turkish Journal of Biology | Comparison of anticarcinogenic properties of Viburnum opulus and its active compound p-coumaric acid on human colorectal carcinoma | doi:10.3906/biy-2002-30 
     used: A:anticancer, D:cancer
     C: This is the first study of pharmacological exploration of V.opulus in human colon cancer. Its antiproliferative effects may be due to the presence of p -CA.

## viola-odorata - Viola odorata - Sweet Violet, Garden violet, English violet
actions: anti-inflammatory=['REF-0517', 'REF-1143', 'REF-1146']; anticancer=['REF-1145', 'REF-1152']; demulcent=['REF-0517', 'REF-0609', 'REF-1143']; expectorant=['REF-0517', 'REF-0609', 'REF-1143', 'REF-1148']; sedative=['REF-0517', 'REF-1143', 'REF-1149', 'REF-1150', 'REF-1151']
- **arthritis** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0517'] N=[] X=['REF-1146'] M=['REF-1143<anti-inflammatory']
- **asthma** [verified,ev5] note="Demulcent / expectorant for cough, bronchitis and catarrh (mucilage soothes; saponins loosen mucus) - a double-blind RCT found violet-flower syrup, added to standard treatment, sped cough suppression in children with asthma"
    D=['REF-0517', 'REF-0609'] N=[] X=[] M=[]
- **bronchitis** [verified,ev5] !NAME['REF-0609'] note="Demulcent / expectorant for cough, bronchitis and catarrh (mucilage soothes; saponins loosen mucus) - a double-blind RCT found violet-flower syrup, added to standard treatment, sped cough suppression in children with asthma"
    D=['REF-0517', 'REF-0609'] N=[] X=[] M=['REF-1143<expectorant', 'REF-1148<expectorant']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1145', 'REF-1152'] N=[] X=[] M=[]
- **cough** [verified,ev5] note="Demulcent / expectorant for cough, bronchitis and catarrh (mucilage soothes; saponins loosen mucus) - a double-blind RCT found violet-flower syrup, added to standard treatment, sped cough suppression in children with asthma"
    D=['REF-0517', 'REF-0609'] N=[] X=[] M=['REF-1143<demulcent', 'REF-1143<expectorant', 'REF-1148<expectorant']
- **headache** [needs-review,ev1] note="Mild sedative for sleeplessness and to ease headache (traditional)"
    D=['REF-0517'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev1] !INF note="inferred from anti-inflammatory action"
    D=['REF-0517'] N=[] X=['REF-1146'] M=['REF-1143<anti-inflammatory']
- **insomnia** [needs-review,ev6] note="Mild sedative for sleeplessness and to ease headache (traditional)"
    D=['REF-0517', 'REF-1150', 'REF-1151'] N=[] X=['REF-1149'] M=['REF-1143<sedative']
- **respiratory-support** [needs-review,ev6] !INF note="inferred from expectorant action"
    D=['REF-0517', 'REF-0609', 'REF-1148'] N=[] X=[] M=['REF-1143<expectorant']
- **skin-irritation** [needs-review,ev1] !INF note="inferred from demulcent action"
    D=['REF-0517'] N=[] X=['REF-0609', 'REF-1146'] M=['REF-1143<anti-inflammatory', 'REF-1143<demulcent']
- **sore-throat** [verified,ev1] note=""
    D=['REF-0517'] N=[] X=[] M=['REF-0609<demulcent', 'REF-1143<demulcent']
  REF-0517 [traditional] n.d.  | Violets (Viola odorata): Benefits, Safety, Uses | NO-ID 
     used: A:anti-inflammatory, A:demulcent, A:expectorant, A:sedative, D:arthritis, D:asthma, D:bronchitis, D:cough, D:headache, D:inflammation, D:insomnia, D:respiratory-support, D:skin-irritation, D:sore-throat
     (no abstract)
  REF-0609 [rct] 2015 Journal of Evidence-Based Complementary  | The Effect of Viola odorata Flower Syrup on the Cough of Children With Asthma: A Double-Blind, Randomized Controlled Trial | doi:10.1177/2156587215584862 
     used: A:demulcent, A:expectorant, D:asthma, D:bronchitis, D:cough, D:respiratory-support, M:sore-throat
     C: There was a significant inverse correlation between the age of children and rate of cough alleviation and suppression by violet syrup. This study showed that the adjuvant use of violet syrup with short-acting β-agonist can enhance the cough suppression in children with intermittent asthma.
     !NULL: No significant difference was observed in basic characteristics.
     !NULL: There was no significant difference in therapeutic effects between boys and girls.
  REF-1143 [narrative-review] 2017 Phytotherapy Research | A Critical Review on Phytochemistry, Pharmacology of Viola odorata L. and Related Multipotential Products in Traditional Persian Medicine | doi:10.1002/ptr.5909 
     used: A:anti-inflammatory, A:demulcent, A:expectorant, A:sedative, M:arthritis, M:bronchitis, M:cough, M:inflammation, M:insomnia, M:respiratory-support, M:skin-irritation, M:sore-throat
     C: However, more studies are needed to confirm these medicinal properties. Copyright © 2017 John Wiley & Sons, Ltd.
  REF-1145 [preclinical] 2020 Clinical & Translational Oncology | Suppressive role of Viola odorata extract on malignant characters of mammosphere-derived breast cancer stem cells | doi:10.1007/s12094-020-02307-9 
     used: A:anticancer, D:cancer
     C: Viola odorata extract exerted anti-cancerous activity on both breast cancer cell lines and their derived BCSCs. Anti-cancerous activity of this extract was significantly more in MCF7-, SKBR3-derived mammospheres in comparison with dedicated cell lines. Data suggest that Viola odorata extract mostly targets cancerous cells, not normal cells with exception in high concentration. It acts in a cell-dependent manner.
  REF-1146 [rct] 2020 Current Drug Discovery Technologies | The Effect of Viola odorata L. Oil for Fever in Children: A Randomized Triple-blinded Placebo-controlled Clinical Trial | doi:10.2174/1570163816666190620142256 
     used: A:anti-inflammatory
     C: The results of our study showed the safety and efficacy of complementary therapy with Viola odorata L. oil for fever control in febrile neutropenic children during hospital course.
     !NULL: 005), while there was no significant change in the placebo group (p =1.
  REF-1148 [rct] 2022 Journal of Ethnopharmacology | Efficacy and safety of add-on Viola odorata L. in the treatment of COVID-19: A randomized double-blind controlled trial | doi:10.1016/j.jep.2022.116058 
     used: A:expectorant, D:respiratory-support, M:bronchitis, M:cough
     C: This study, the first clinical trial on the effectiveness of Viola odorata on SARS-CoV-2 patients, showed that Viola odorata L. effectively controls prevalent manifestations of COVID-19 including cough, myalgia, headache, and diarrhea. Regarding this survey, the violet syrup can be mentioned as a complementary treatment for viral influenza-like infections in which cough, myalgia, headache, and diarrhea are prominent.
     !NULL: Results No significant difference was between groups regarding demographic characteristics and vital signs before and after the treatment.
  REF-1149 [preclinical] 2021 Frontiers in Pharmacology | Pharmacological Screening of Viola odorata L. for Memory-Enhancing Effect via Modulation of Oxidative Stress and Inflammatory Biomarkers | doi:10.3389/fphar.2021.664832 
     used: A:sedative
     C: Based on behavioral, oxidative stress biomarker, and neuroinflammatory data, it is concluded that V. odorata possesses memory-enhancing activity and may prove a beneficial role in the management of AD.
  REF-1150 [rct] 2020 Journal of Alternative and Complementary | Effects of Viola odorata as an Add-On Therapy on Insomnia in Patients with Obsession or Depression: A Pilot Randomized Double-Blind Placebo-Controlled | doi:10.1089/acm.2019.0254 
     used: A:sedative, D:insomnia
     C: V. odorata syrup significantly improved insomnia symptoms and the scores of depression and OCD.
  REF-1151 [clinical] 2014 Iranian Red Crescent Medical Journal | Efficacy of Viola odorata in Treatment of Chronic Insomnia | doi:10.5812/ircmj.17511 
     used: A:sedative, D:insomnia
     C: VO can be presented as a safe, well-tolerated, and effective herbal preparation in patients with chronic insomnia.
  REF-1152 [preclinical] 2018 Phytochemistry | PepSAVI-MS reveals anticancer and antifungal cycloviolacins in Viola odorata | doi:10.1016/j.phytochem.2018.04.014 
     used: A:anticancer, D:cancer
     C: Downstream implementation of ultraviolet photodissociation (UVPD) tandem mass spectrometry is demonstrated for cyO8 as a method to address traditionally difficult-to-sequence cyclotide species. This work emphasizes the therapeutic and agricultural potential of natural product bioactive peptides and the necessity of developing robust analytical tools to deconvolute nature's complexity.

## viola-tricolor - Viola tricolor - Heartsease, Wild pansy, Johnny-jump-up
actions: anti-inflammatory=['REF-0463', 'REF-0617', 'REF-1600', 'REF-1605', 'REF-2577']; anticancer=['REF-0556', 'REF-1601']; demulcent=['REF-0463']; emollient=['REF-0463', 'REF-1605']; expectorant=['REF-0463']; immunomodulator=['REF-0463', 'REF-0617', 'REF-2578']
- **arthritis** [needs-review,ev2] !INF !NAME['REF-0463', 'REF-0617'] note="inferred from anti-inflammatory action"
    D=['REF-0463', 'REF-0617'] N=[] X=['REF-1600', 'REF-1605', 'REF-2577'] M=[]
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1601'] N=[] X=[] M=['REF-0556<anticancer']
- **eczema** [verified,ev3] !NAME['REF-0617'] note="Anti-inflammatory / immunomodulatory for chronic skin conditions - eczema, psoriasis, itching and scabs (traditional, supported by cyclotide research) - cyclotide-enriched V. tricolor preparations suppress T-cell proliferation and pro-inflammatory cytokine secretion in vitro"
    D=['REF-0463', 'REF-0617', 'REF-2579'] N=[] X=[] M=['REF-1605<emollient']
- **immune-support** [needs-review,ev2] !INF note="inferred from immunomodulator action"
    D=['REF-2578'] N=[] X=['REF-0463', 'REF-0617'] M=[]
- **inflammation** [needs-review,ev3] note="Traditional demulcent / expectorant for cough, bronchitis and chest inflammation"
    D=['REF-0463', 'REF-2577'] N=[] X=[] M=['REF-0617<anti-inflammatory', 'REF-1600<anti-inflammatory', 'REF-1605<anti-inflammatory']
- **psoriasis** [verified,ev2] !NAME['REF-0617'] note="Anti-inflammatory / immunomodulatory for chronic skin conditions - eczema, psoriasis, itching and scabs (traditional, supported by cyclotide research) - cyclotide-enriched V. tricolor preparations suppress T-cell proliferation and pro-inflammatory cytokine secretion in vitro"
    D=['REF-0463', 'REF-0617'] N=[] X=[] M=[]
- **skin-irritation** [verified,ev1] note="Soothes irritated skin (demulcent and anti-inflammatory)"
    D=['REF-0463'] N=[] X=['REF-1600', 'REF-2577'] M=['REF-0617<anti-inflammatory', 'REF-1605<anti-inflammatory', 'REF-1605<emollient']
  REF-0463 [traditional] 2013 Journal of Ethnopharmacology | Immunosuppressive activity of an aqueous Viola tricolor herbal extract | doi:10.1016/j.jep.2013.10.044 
     used: A:anti-inflammatory, A:demulcent, A:emollient, A:expectorant, A:immunomodulator, D:arthritis, D:eczema, D:inflammation, D:psoriasis, D:skin-irritation
     C: An aqueous Viola extract contains bioactive cyclotides, which inhibit proliferation of activated lymphocytes in an IL-2 dependent manner. The findings provide a rationale for use of herbal Viola preparations in the therapy of disorders related to an overactive immune system. However, further studies to evaluate its clinical potency and potential risks have to be performed.
  REF-0556 [preclinical] 2004 Journal of Natural Products | Cytotoxic cyclotides from Viola tricolor | doi:10.1021/np030101l 
     used: A:anticancer, M:cancer
     C: Each forms a head-to-tail cyclic backbone, with six cysteine residues being involved in three disulfide bonds, characteristic of the family of small proteins called the cyclotides. This is the first report on cyclotides from the species V. tricolor and the first report on the sequence of the cytotoxic cyclotide vitri A.
  REF-0617 [preclinical] 2023 Planta Medica | Exploring Immune Modulatory Effects of Cyclotide-Enriched Viola tricolor Preparations | doi:10.1055/a-2173-8627 
     used: A:anti-inflammatory, A:immunomodulator, D:arthritis, D:eczema, D:psoriasis, M:inflammation, M:skin-irritation
     C: Defined cyclotide preparations of V. tricolor have promising pharmacological effects in modulating immune cell responses at the cytokine levels. This is important towards understanding the role of cyclotide-containing herbal drug preparations for future applications in immune disorders, such as inflammatory bowel disease.
  REF-1600 [preclinical] 2018 Iranian Journal of Allergy, Asthma, and  | Effects of Viola tricolor Flower Hydroethanolic Extract on Lung Inflammation in a Mouse Model of Chronic Asthma | doi:10.18502/ijaai.v17i5.299 
     used: A:anti-inflammatory, M:inflammation
     C: As result, it prevented further reduction of inflammatory parameters in this group compared to the Viola tricolor-treated group at 200 mg/kg. Our study demonstrated that Viola tricolor has anti-inflammatory effects via inhibition of T-helper type 2 (Th2) cytokine production and validated its empirical usage in traditional medicine.
  REF-1601 [preclinical] 2014 BioMed Research International | Viola tricolor induces apoptosis in cancer cells and exhibits antiangiogenic activity on chicken chorioallantoic membrane | doi:10.1155/2014/625792 
     used: A:anticancer, D:cancer
     C: Analysis of quality of EtOAc fraction using HPLC fingerprint showed six major peaks with different retention times. The results of the present study suggest that V. tricolor has potential anticancer property by inducing apoptosis and inhibiting angiogenesis.
  REF-1605 [preclinical] 2013 Journal of Ethnopharmacology | Antiinflammatory effects of Viola tricolor gel in a model of sunburn in rats and the gel stability study | doi:10.1016/j.jep.2013.08.040 
     used: A:anti-inflammatory, A:emollient, M:eczema, M:inflammation, M:skin-irritation
     C: These findings suggest that Viola tricolor gel has an antinociceptive and antiinflammatory effect in the ultraviolet-B-induced burn, since maintain the temperature below 25 °C.
  REF-2577 [clinical] 2015 Phytomedicine | Anti-cytokine therapy for prevention of atherosclerosis | doi:10.1016/j.phymed.2015.12.002 
     used: A:anti-inflammatory, D:inflammation
     C: Anti-cytokine therapy may be a promising direction in moderation of atherogenesis, especially when it begins on the early stages of subclinical atherosclerosis. The use of herbal preparations with anti-cytokine mechanism of action is the most perspective for timely prevention of atherosclerosis, as they have no significant side effects and can be prescribed for long-term administration.
     !NULL: The use of herbal preparations with anti-cytokine mechanism of action is the most perspective for timely prevention of atherosclerosis, as they have no significant side effects and can be prescribed for long-term administration.
  REF-2578 [preclinical] 2022 Frontiers in Pharmacology | Inhibition of HIV-1 by Cyclotide-Enriched Extracts of Viola tricolor | doi:10.3389/fphar.2022.888961 
     used: A:immunomodulator, D:immune-support
     C: The identification and characterization of antiviral cyclotides and the determination of the antiviral mechanisms may allow to develop novel agents to combat viral infections. Therefore, cyclotides represent a natural source of bioactive molecules with prospects for development as therapeutics.
  REF-2579 [clinical] 2023 Journal of Complementary & Integrative M | Case study of clinical improvement of atopic dermatitis in a patient treated with herbal-based parapharmaceuticals | doi:10.1515/jcim-2023-0005 
     used: D:eczema
     C: The patient was satisfied with the "clean hands" with no inflammation, with the resolution of the dermatitis in the other body sites and stated that the therapy has improved her perceived quality of life. These botanicals may be effective and play a role in improving the quality of life of a person with AD.

## vitex-agnus-castus - Vitex agnus-castus - Chasteberry, Chaste tree, Monk's pepper
actions: 
- **acne** [needs-review,ev1] note="Cycle-related (hormonal) acne (traditional)"
    D=['REF-2580'] N=[] X=[] M=[]
- **menopause** [needs-review,ev2] note=""
    D=['REF-1612', 'REF-2580'] N=[] X=[] M=[]
- **menstrual-cramps** [needs-review,ev8] note=""
    D=['REF-0433', 'REF-1610', 'REF-2580'] N=[] X=[] M=[]
- **pain** [verified,ev9] !NAME['REF-0433', 'REF-1613', 'REF-3119'] note="Eases cyclical breast pain (mastalgia) and menstrual-cycle complaints including cramping. The proposed mechanism is dopaminergic suppression of latent hyperprolactinaemia."
    D=['REF-0433', 'REF-1609', 'REF-1610', 'REF-1613', 'REF-3119'] N=[] X=[] M=[]
- **pms** [verified,ev10] note="Eases cyclical breast pain (mastalgia) and menstrual-cycle complaints including cramping; Relief of premenstrual syndrome (PMS) symptoms"
    D=['REF-0433', 'REF-0435', 'REF-1607', 'REF-1608', 'REF-1609', 'REF-1610', 'REF-1611', 'REF-1613', 'REF-2580', 'REF-3116', 'REF-3117'] N=[] X=[] M=[]
  REF-0433 [systematic-review] 2012 Planta Medica | Vitex agnus-castus extracts for female reproductive disorders: a systematic review of clinical trials | doi:10.1055/s-0032-1327831 
     used: D:menstrual-cramps, D:pain, D:pms
     C: Limitations include small sample sizes in some studies, heterogeneity of conditions being treated, and a range of reference treatments.Despite some methodological limitations, the results from randomised, controlled trials to date suggest benefits for Vitex extracts in the treatment of premenstrual syndrome, premenstrual dysphoric disorder and latent hyperprolactinaemia. Further research is recommended, and greater t
  REF-0435 [rct] 2023 Frontiers in Endocrinology | Vitex agnus castus effects on hyperprolactinaemia | doi:10.3389/fendo.2023.1269781 
     used: D:pms
     C: It appears that VAC may represent a potentially useful and safe phytotherapic option for the management of selected patients with mild hyperprolactinaemia who wish to be treated with phytotherapy. However, larger studies of high quality are needed to corroborate it.
  REF-1607 [meta-analysis] 2019 Complementary Therapies in Medicine | Vitex agnus-castus in premenstrual syndrome: A meta-analysis of double-blind randomised controlled trials | doi:10.1016/j.ctim.2019.08.024 
     used: D:pms
     C: Although several clinical trials have been carried out with VAC, the majority of the studies cannot be used as evidence for efficacy due to incomplete reporting, especially concerning the description of the used medication. More trials following the CONSORT recommendations are needed to assess the efficacy of VAC extracts.
  REF-1608 [meta-analysis] 2017 American Journal of Obstetrics and Gynec | The treatment of premenstrual syndrome with preparations of Vitex agnus castus: a systematic review and meta-analysis | doi:10.1016/j.ajog.2017.02.028 
     used: D:pms
     C: Although meta-analysis shows a large pooled effect of Vitex agnus castus in placebo-controlled trials, the high risk of bias, high heterogeneity, and risk of publication bias of the included studies preclude a definitive conclusion. The pooled treatment effects should be viewed as merely explorative and, at best, overestimating the real treatment effect of Vitex agnus castus for premenstrual syndrome symptoms. There 
  REF-1609 [meta-analysis] 2020 Journal of Women's Health | Vitex Agnus-Castus for the Treatment of Cyclic Mastalgia: A Systematic Review and Meta-Analysis | doi:10.1089/jwh.2019.7770 
     used: D:pain, D:pms
     C: VAC is a safe and effective treatment option for CM. More high-quality clinical trials are needed to strengthen the evidence base.
  REF-1610 [clinical] 2024 Archives of Gynecology and Obstetrics | Use of Vitex agnus-castus in patients with menstrual cycle disorders: a single-center retrospective longitudinal cohort study | doi:10.1007/s00404-023-07363-4 
     used: D:menstrual-cramps, D:pain, D:pms
     C: These real-world data demonstrate the effectiveness of the VAC-containing products Cyclodynon® and Mastodynon® in the three-month treatment of MCDs, with a pronounced improvement in key disease symptoms and QoL. Intriguingly, while QoL was generally greatly improved, the response to VAC therapy varied depending on the type of underlying MCD.
  REF-1611 [systematic-review] 2017 Archives of Women's Mental Health | Vitex agnus castus for premenstrual syndrome and premenstrual dysphoric disorder: a systematic review | doi:10.1007/s00737-017-0791-0 
     used: D:pms
     C: Main limitations were differences in definition of diagnostic criteria, the instruments used as main outcome measures, and different preparations of VAC extracts limit the comparison of results between studies. In conclusion, the RCTs using VAC for treatment of PMS/PMDD suggested that the VAC extract is a safe and efficacious alternative to be considered for the treatment of PMS/PMDD symptoms.
  REF-1612 [narrative-review] 2009 Journal of Alternative and Complementary | Vitex agnus-castus (Chaste-Tree/Berry) in the treatment of menopause-related complaints | doi:10.1089/acm.2008.0447 
     used: D:menopause
     C: We conclude that, while evidence from rigorous randomized controlled trials is lacking for the individual herb in this context, emerging pharmacological evidence supports a role for V. agnus-castus in the alleviation of menopausal symptoms and suggests that further investigation may be appropriate.
     !NULL: Background The origin of the current practice of administering Vitex agnus-castus in menopause-related complaints is uncertain, but appears to be relatively recent.
  REF-1613 [narrative-review] 2003 Phytomedicine | Chaste tree (Vitex agnus-castus) - pharmacology and clinical indications | doi:10.1078/094471103322004866 
     used: D:pain, D:pms
     C: They were almost identical in their prolactin-suppressive properties than dopamine itself. Hence, it is concluded that dopaminergic compounds present in Vitex agnus castus are clinically the important compounds which improve premenstrual mastodynia and possibly also other symptoms of the premenstrual syndrome.
  REF-2580 [traditional] 2013 Pharmacognosy Reviews | The genus Vitex: A review | doi:10.4103/0973-7847.120522 !TAG review-title/traditional
     used: D:acne, D:menopause, D:menstrual-cramps, D:pms
     C: Despite a long tradition of use of some species, the genus has not been explored properly. In the concluding part, the future scope of Vitex species has been emphasized with a view to establish their multifarious biological activities and mode of action.
  REF-3116 [rct] 2003 Human Psychopharmacology | Fluoxetine versus Vitex agnus castus extract in the treatment of premenstrual dysphoric disorder | pmid:12672170 doi:10.1002/hup.470 
     used: D:pms
     C: There was no statistically significant difference between the groups with respect to the rate of responders. However, fluoxetine was more effective for psychological symptoms while the extract diminished the physical symptoms.
     !NULL: There was no statistically significant difference between the groups with respect to the rate of responders.
  REF-3117 [rct] 2012 Acta Medica Iranica | Therapeutic effect of Vitex agnus castus in patients with premenstrual syndrome | pmid:22359078 
     used: D:pms
     C: Rank of variables differed significantly in active and placebo groups before and after the study (P<0.0001), and there were significant differences for Vitex agnus in comparison with placebo (P<0.0001). Vitex agnus can be considered an effective and well tolerated treatment for the relief of symptoms of mild and moderate PMS.
  REF-3119 [preclinical] 2022 Bratislava Medical Journal | The mechanisms underlying the role of Vitex agnus-castus in mastalgia | pmid:36342880 doi:10.4149/BLL_2022_147 
     used: D:pain
     C: Many medical benefits of VAC have been reported, including mastalgia, regulating menstrual cycles and premenstrual complaints, and infertility. In this review, the known roles of VAC in mastalgia are analyzed and characterized, as well as the mechanism of action reported in in vitro and/or in vivo studies.

## withania-somnifera - Withania somnifera - Ashwagandha, Indian Ginseng, Winter Cherry
actions: anti-inflammatory=['REF-2249']; anticancer=['REF-2255']; antidiabetic=[]; antioxidant=['REF-2250']; ergogenic=['REF-2252', 'REF-2254']; immunomodulator=[]; neuroprotective=['REF-2246', 'REF-2250', 'REF-2253']; sedative=['REF-2245', 'REF-2246', 'REF-2247', 'REF-2248', 'REF-2251']
- **arthritis** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2249<anti-inflammatory']
- **cancer** [needs-review,ev7] !INF note="inferred from anticancer action"
    D=['REF-2255'] N=[] X=[] M=[]
- **cognitive-function** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-2246'] M=['REF-2250<neuroprotective', 'REF-2253<neuroprotective']
- **fatigue** [needs-review,ev1] note="inferred from ergogenic action"
    D=[] N=[] X=[] M=['REF-2252<ergogenic', 'REF-2254<ergogenic']
- **inflammation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2249<anti-inflammatory']
- **insomnia** [needs-review,ev1] note="inferred from sedative action"
    D=[] N=[] X=['REF-2247', 'REF-2248'] M=['REF-2245<sedative', 'REF-2246<sedative', 'REF-2251<sedative']
- **memory** [needs-review,ev1] note="inferred from neuroprotective action"
    D=[] N=[] X=['REF-2246'] M=['REF-2250<neuroprotective', 'REF-2253<neuroprotective']
- **muscle-soreness** [needs-review,ev1] note="inferred from ergogenic action"
    D=[] N=[] X=[] M=['REF-2252<ergogenic', 'REF-2254<ergogenic']
- **skin-irritation** [needs-review,ev1] note="inferred from anti-inflammatory action"
    D=[] N=[] X=[] M=['REF-2249<anti-inflammatory']
  REF-2245 [meta-analysis] 2021 PLoS One | Effect of Ashwagandha (Withania somnifera) extract on sleep: a systematic review and meta-analysis | doi:10.1371/journal.pone.0257843 
     used: A:sedative, M:insomnia
     C: Ashwagandha extract appears to has a beneficial effect in improving sleep in adults. However, data on the serious adverse effects of Ashwagandha extract are limited, and more safety data would be needed to assess whether it would be safe for long-term use.
     !NULL: Ashwagandha extract was also found to improve mental alertness on rising and anxiety level, but no significant effect on quality of life.
  REF-2246 [narrative-review] 2021 Current Neuropharmacology | Effects of Withania somnifera (ashwagandha) on stress and the stress-related neuropsychiatric disorders anxiety, depression, and insomnia | doi:10.2174/1570159X19666210712151556 
     used: A:neuroprotective, A:sedative, M:insomnia
     C: While benefits were seen in the reviewed studies, significant variability in the WS extracts examined prevents a consensus on the optimum WS preparation or dosage for treating neuropsychiatric conditions. WS generally appears safe for human use; however, it will be important to investigate potential herb-drug interactions involving WS if used alongside pharmaceutical interventions. Further elucidation of active compo
  REF-2247 [meta-analysis] 2024 Explore | Effects of Ashwagandha (Withania somnifera) on stress and anxiety: a systematic review and meta-analysis | doi:10.1016/j.explore.2024.103062 
     used: A:sedative
     C: The findings from the included studies indicate that Ashwagandha formulations have beneficial effects on stress and anxiety. The adverse effects associated with Ashwagandha are limited; however, further information is required to determine its safety with long-term administration.
  REF-2248 [rct] 2019 Medicine | An investigation into the stress-relieving and pharmacological actions of an ashwagandha (Withania somnifera) extract: a randomized, double-blind, pla | doi:10.1097/MD.0000000000017186 
     used: A:sedative
     C: These findings suggest that ashwagandha's stress-relieving effects may occur via its moderating effect on the hypothalamus-pituitary-adrenal axis. However, further investigation utilizing larger sample sizes, diverse clinical and cultural populations, and varying treatment dosages are needed to substantiate these findings. Trial registration Clinical Trials Registry-India (CTRI registration number: CTRI/2017/08/00944
     !NULL: 989) over time, although this change was not statistically significant compared with the placebo (P = .
  REF-2249 [narrative-review] 2021 Biomedicine & Pharmacotherapy | Withania somnifera (L.) Dunal (Ashwagandha): a comprehensive review on ethnopharmacology, pharmacotherapeutics, biomedicinal and toxicological aspects | doi:10.1016/j.biopha.2021.112175 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: However, in-depth studies are needed on the clinical use of W. somnifera against human diseases. Besides, detailed toxicological analysis is also to be performed for its safe and efficacious use in preclinical and clinical studies and as a health-promoting herb.
  REF-2250 [narrative-review] 2015 Cellular and Molecular Life Sciences | Pharmacologic overview of Withania somnifera, the Indian ginseng | doi:10.1007/s00018-015-2012-1 
     used: A:antioxidant, A:neuroprotective, M:cognitive-function, M:memory
     C: In view of these pharmacologic properties, W. somnifera is a potential drug candidate to treat various clinical conditions, particularly related to the nervous system. In this review, we summarize the pharmacologic characteristics and discuss the mechanisms of action and potential therapeutic applications of the plant and its active constituents.
  REF-2251 [rct] 2024 Nutrients | Effects of Withania somnifera extract in chronically stressed adults: a randomized controlled trial | doi:10.3390/nu16091293 
     used: A:sedative, M:insomnia
     C: Our findings demonstrate the stress-reduction capabilities of this well-characterized aqueous extract of WS (root and leaf) at the low dose of 125 mg/day, in a dose-dependent manner, via the modulation of the HPA axis. Trial registration This study was registered with the Clinical Trials Registry-India (CTRI) with the registration number: CTRI/2019/11/022100.
  REF-2252 [rct] 2015 Journal of the International Society of  | Examining the effect of Withania somnifera supplementation on muscle strength and recovery: a randomized controlled trial | doi:10.1186/s12970-015-0104-9 
     used: A:ergogenic, M:fatigue, M:muscle-soreness
     C: This study reports that ashwagandha supplementation is associated with significant increases in muscle mass and strength and suggests that ashwagandha supplementation may be useful in conjunction with a resistance training program.
  REF-2253 [rct] 2017 Journal of Dietary Supplements | Efficacy and safety of ashwagandha (Withania somnifera (L.) Dunal) root extract in improving memory and cognitive functions | doi:10.1080/19390211.2017.1284970 
     used: A:neuroprotective, M:cognitive-function, M:memory
     C: Ashwagandha may be effective in enhancing both immediate and general memory in people with MCI as well as improving executive function, attention, and information processing speed.
  REF-2254 [rct] 2021 Journal of Ethnopharmacology | A double-blind, randomized, placebo-controlled trial on the effect of Ashwagandha (Withania somnifera dunal.) root extract in improving cardiorespirat | doi:10.1016/j.jep.2021.113929 
     used: A:ergogenic, M:fatigue, M:muscle-soreness
     C: The present findings suggest that Ashwagandha root extract can successfully enhance cardiorespiratory endurance and improve the quality of life in healthy athletic adults. No adverse events were reported by any of the subjects in this study.
  REF-2255 [systematic-review] 2020 Journal of Ethnopharmacology | Review on anticancerous therapeutic potential of Withania somnifera (L.) Dunal | doi:10.1016/j.jep.2020.113704 
     used: A:anticancer, D:cancer
     C: The present review confirms the various medicinal values of W. somnifera without any significant side effects. Withaferin-A (WA) and Withanolides are its most promising anticancer compounds that play a major role in apoptosis induction. Keeping in mind the anticancerous potential of this plant, it is suggested that this plant may further be investigated and more clinical studies can be performed.

## zea-mays - Zea mays - Corn Silk, Maize silk, Stigma maydis
actions: anti-inflammatory=['REF-0436', 'REF-1625', 'REF-1626', 'REF-1627', 'REF-1631']; anticancer=['REF-1629']; antioxidant=['REF-0436', 'REF-1624', 'REF-1627', 'REF-1632']; demulcent=['REF-0436']; diuretic=['REF-0436', 'REF-0557', 'REF-1632']
- **arthritis** [needs-review,ev1] !INF !NAME['REF-0436'] note="inferred from anti-inflammatory action"
    D=['REF-0436'] N=[] X=[] M=['REF-1625<anti-inflammatory', 'REF-1626<anti-inflammatory', 'REF-1627<anti-inflammatory', 'REF-1631<anti-inflammatory']
- **cancer** [needs-review,ev2] !INF note="inferred from anticancer action"
    D=['REF-1629'] N=[] X=[] M=[]
- **cough** [needs-review,ev1] !INF !NAME['REF-0436'] note="inferred from demulcent action"
    D=['REF-0436'] N=[] X=[] M=[]
- **infection** [verified,ev1] !NAME['REF-0436'] note="Soothing demulcent for urinary-tract irritation and mild urinary infections; supports kidney function"
    D=['REF-0436'] N=[] X=[] M=[]
- **inflammation** [needs-review,ev1] !INF !NAME['REF-0436'] note="inferred from anti-inflammatory action"
    D=['REF-0436'] N=[] X=[] M=['REF-1625<anti-inflammatory', 'REF-1626<anti-inflammatory', 'REF-1627<anti-inflammatory', 'REF-1631<anti-inflammatory']
- **skin-irritation** [needs-review,ev1] !INF !NAME['REF-0436'] note="inferred from demulcent action"
    D=['REF-0436'] N=[] X=['REF-1625'] M=['REF-1626<anti-inflammatory', 'REF-1627<anti-inflammatory', 'REF-1631<anti-inflammatory']
- **sore-throat** [needs-review,ev1] !INF !NAME['REF-0436'] note="inferred from demulcent action"
    D=['REF-0436'] N=[] X=[] M=[]
- **swelling** [verified,ev1] note="Diuretic - increases urine output to support the urinary tract and mild fluid retention/swelling; in conscious rats the aqueous extract is diuretic and kaliuretic and modifies glomerular filtration and potassium excretion"
    D=['REF-0436', 'REF-0557'] N=[] X=[] M=['REF-1632<diuretic']
- **urinary-support** [needs-review,ev1] !INF note="inferred from diuretic action"
    D=['REF-0436', 'REF-0557'] N=[] X=[] M=['REF-1632<diuretic']
- **uti** [verified,ev1] !NAME['REF-0436', 'REF-0557'] note="Diuretic - increases urine output to support the urinary tract and mild fluid retention/swelling; in conscious rats the aqueous extract is diuretic and kaliuretic and modifies glomerular filtration and potassium excretion; Soothing demulcent for urinary-tract irritation and mild urinary infections; supports kidney function"
    D=['REF-0436', 'REF-0557'] N=[] X=[] M=['REF-1632<diuretic']
  REF-0436 [traditional] 2012 Molecules | Corn Silk (Stigma Maydis) in Healthcare: A Phytochemical and Pharmacological Review | doi:10.3390/molecules171112937 !TAG review-title/traditional
     used: A:anti-inflammatory, A:antioxidant, A:demulcent, A:diuretic, D:arthritis, D:cough, D:infection, D:inflammation, D:skin-irritation, D:sore-throat, D:swelling, D:urinary-support, D:uti
     C: As such, this review will cover the research findings on the potential applications of corn silk in healthcare which include its phytochemical and pharmacological activities. In addition, the botanical description and its toxicological studies are also included.
  REF-0557 [traditional] 2005 Phytomedicine | Zea mays L. extracts modify glomerular function and potassium urinary excretion in conscious rats | doi:10.1016/j.phymed.2003.12.010 
     used: A:diuretic, D:swelling, D:urinary-support, D:uti
     C: To summarize, in water-loaded conscious rats (2.5 ml/100 body wt.), corn silk aqueous extract is diuretic at a dose of 500 mg/kg body wt. and kaliuretic at doses of 350 and 500 mg/kg body wt. In water-loaded conscious rats (5.0 ml/100 g body wt.), corn silk aqueous extract is kaliuretic at a dose of 500 mg/kg body wt., but glomerular filtration and filtered load decrease without affecting proximal tubular function, N
  REF-1624 [preclinical] 2018 Biomedicine & Pharmacotherapy | Corn silk (Zea mays L.), a source of natural antioxidants with alpha-amylase, alpha-glucosidase, advanced glycation and diabetic nephropathy inhibitor | doi:10.1016/j.biopha.2018.11.126 
     used: A:antioxidant
     C: These findings suggested the antioxidant activities of corn silk could contribute, at least in part, to its traditionally claimed therapeutic benefits on DM and DN. The phenolic-enriched CS fractions could be considered as a source of natural antioxidants and further developed for the prevention and treatment of DM and its complications including DN.
  REF-1625 [preclinical] 2023 Journal of Agricultural and Food Chemist | Corn Silk Flavonoids Ameliorate Hyperuricemia via PI3K/AKT/NF-kappaB Pathway | doi:10.1021/acs.jafc.3c03422 
     used: A:anti-inflammatory, M:arthritis, M:inflammation
     C: Furthermore, it decreased the levels of TNF-α and IL-6 and restored pathological damage. In summary, CSF is a functional food component to improve HUA by reducing inflammation and apoptosis through the down-regulating PI3K/AKT/NF-κB pathway.
  REF-1626 [preclinical] 1998 Planta Medica | Extract of corn silk (stigma of Zea mays) inhibits the tumour necrosis factor-alpha- and bacterial lipopolysaccharide-induced cell adhesion and ICAM-1 | doi:10.1055/s-2006-957441 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: The extract did not alter the production of TNF by LPS-activated macrophages and failed to inhibit the cytotoxic activity of TNF. It is concluded that corn silk possesses important therapeutic potential for TNF- and LPS-mediated leukocyte adhesion and trafficking.
     !NULL: The extract did not alter the production of TNF by LPS-activated macrophages and failed to inhibit the cytotoxic activity of TNF.
  REF-1627 [narrative-review] 2025 Molecular Nutrition & Food Research | Unlocking Corn Silk's Potential: Bioactive Compounds Targeting Age-Related Diseases | doi:10.1002/mnfr.70117 
     used: A:anti-inflammatory, A:antioxidant, M:arthritis, M:inflammation, M:skin-irritation
     C: Future research should focus on standardizing extraction methods, elucidating mechanisms of action, and exploring synergistic interactions among its bioactive constituents. Together, this review emphasizes the need for continued investigation into corn silk as a natural, multi-target therapeutic agent for aging and age-related diseases, and advancing its potential for clinical applications.
  REF-1629 [preclinical] 2019 Oxidative Medicine and Cellular Longevit | Corn Silk (Zea mays) Induced Apoptosis in Human Breast Cancer (MCF-7) Cells via the ROS-Mediated Mitochondrial Pathway | doi:10.1155/2019/9789241 
     used: A:anticancer, D:cancer
     C: The real-time PCR data showed a significant upregulation in p53, Bax, caspase-3, and caspase-9 and downregulation in the mRNA expression of Bcl-2 genes in MCF-7 cells exposed to CSE. Collectively, the data from this study stated that corn silk extract induced apoptosis via the ROS-mediated mitochondrial pathway in MCF-7 cells.
  REF-1631 [preclinical] 2025 Ultrasonics Sonochemistry | Ultrasound-assisted extraction of anti-inflammatory actives from corn silk (Zea mays L.): Process optimization, machine learning screening, and intera | doi:10.1016/j.ultsonch.2025.107420 
     used: A:anti-inflammatory, M:arthritis, M:inflammation, M:skin-irritation
     C: Molecular docking and molecular dynamics (MD) simulations were combined to elucidate the binding mechanism of isoorientin with COX-2, confirming that stable interactions were mediated by hydrogen bonding and hydrophobic effects. This work provides a theoretical framework for the rapid screening of COX-2 inhibitory compounds, establishes a high-value utilization pathway for corn silk, thereby contributing to the advan
  REF-1632 [narrative-review] 2024 Molecules | An Umbrella Insight into the Phytochemistry Features and Biological Activities of Corn Silk: A Narrative Review | doi:10.3390/molecules29040891 
     used: A:antioxidant, A:diuretic, M:swelling, M:urinary-support, M:uti
     C: Pharmacological studies have shown that corn silk extract has various pharmacological effects, such as reducing blood lipids, lowering blood pressure, regulating blood sugar levels, anti-inflammatory effects, and anti-oxidation effects. In this paper, the related research on corn silk from the past few years is summarized to provide a theoretical reference for the further development and utilization of corn silk.

## zingiber-officinale - Zingiber officinale - Ginger, garden ginger, common ginger
actions: analgesic=['REF-0007', 'REF-0077', 'REF-0639', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0605', 'REF-0637', 'REF-0638']; anti-inflammatory=['REF-0007', 'REF-0077', 'REF-0639', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0637', 'REF-0638']; antioxidant=['REF-0007', 'REF-0077', 'REF-0639', 'REF-0164', 'REF-0269', 'REF-0295']; antispasmodic=['REF-0007', 'REF-0077', 'REF-0639', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0605']; digestive=['REF-0007', 'REF-0077', 'REF-0639', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0634', 'REF-0635']
- **arthritis** [needs-review,ev9] !INF note="inferred from anti-inflammatory action"
    D=['REF-0007', 'REF-0164', 'REF-0637', 'REF-0638'] N=[] X=['REF-0077', 'REF-0269', 'REF-0295', 'REF-0639'] M=[]
- **back-pain** [needs-review,ev3] !INF !NAME['REF-0007'] note="inferred from analgesic action"
    D=['REF-0007', 'REF-0164'] N=[] X=['REF-0077', 'REF-0269', 'REF-0295', 'REF-0605', 'REF-0637', 'REF-0638', 'REF-0639'] M=[]
- **bloating** [needs-review,ev3] !INF !NAME['REF-0007'] note="inferred from digestive action"
    D=['REF-0007', 'REF-0077'] N=[] X=['REF-0164', 'REF-0269', 'REF-0295', 'REF-0634', 'REF-0635', 'REF-0639'] M=[]
- **cardiovascular-support** [verified,ev3] note=""
    D=['REF-0007'] N=[] X=[] M=[]
- **headache** [needs-review,ev3] !INF !NAME['REF-0007'] note="inferred from analgesic action"
    D=['REF-0007'] N=[] X=['REF-0077', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0605', 'REF-0637', 'REF-0638', 'REF-0639'] M=[]
- **indigestion** [needs-review,ev9] !INF !NAME['REF-0295', 'REF-0634', 'REF-0635'] note="inferred from digestive action"
    D=['REF-0007', 'REF-0077', 'REF-0295', 'REF-0634', 'REF-0635'] N=[] X=['REF-0164', 'REF-0269', 'REF-0639'] M=[]
- **inflammation** [needs-review,ev9] !INF !NAME['REF-0638'] note="inferred from anti-inflammatory action"
    D=['REF-0007', 'REF-0164', 'REF-0637', 'REF-0638'] N=[] X=['REF-0077', 'REF-0269', 'REF-0295', 'REF-0639'] M=[]
- **menstrual-cramps** [needs-review,ev8] !INF !NAME['REF-0007'] note="inferred from antispasmodic action"
    D=['REF-0007', 'REF-0605'] N=[] X=['REF-0077', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0639'] M=[]
- **muscle-spasm** [needs-review,ev3] !INF note="inferred from antispasmodic action"
    D=['REF-0007'] N=[] X=['REF-0077', 'REF-0164', 'REF-0269', 'REF-0295', 'REF-0605', 'REF-0639'] M=[]
- **pain** [verified,ev9] note=""
    D=['REF-0007', 'REF-0164', 'REF-0605', 'REF-0637', 'REF-0638'] N=[] X=['REF-0077', 'REF-0269', 'REF-0295', 'REF-0639'] M=[]
- **respiratory-support** [verified,ev3] !NAME['REF-0007'] note=""
    D=['REF-0007'] N=[] X=[] M=[]
- **skin-irritation** [needs-review,ev3] !INF !NAME['REF-0007'] note="inferred from anti-inflammatory action"
    D=['REF-0007', 'REF-0164'] N=[] X=['REF-0077', 'REF-0269', 'REF-0295', 'REF-0637', 'REF-0638', 'REF-0639'] M=[]
- **nausea** [verified,ev8] note="Meta-analyses report that ginger relieves nausea in pregnancy compared with placebo, with no significant effect on vomiting episodes. The EU herbal monograph covers prevention of nausea and vomiting in motion sickness."
    D=['REF-0295', 'REF-0635', 'REF-0077'] N=[] X=[] M=[]
  REF-0007 [clinical] 2008  | Some phytochemical, pharmacological and toxicological properties of ginger (Zingiber officinale Roscoe): a review of recent research | doi:10.1016/j.fct.2007.09.085 !TAG review-title/clinical
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive, D:arthritis, D:back-pain, D:bloating, D:cardiovascular-support, D:headache, D:indigestion, D:inflammation, D:menstrual-cramps, D:muscle-spasm, D:pain, D:respiratory-support, D:skin-irritation
     C: It is considered a safe herbal medicine with only few and insignificant adverse/side effects. More studies are required in animals and humans on the kinetics of ginger and its constituents and on the effects of their consumption over a long period of time.
  REF-0077 [traditional] 2012  | European Union herbal monograph on Zingiber officinale Roscoe, rhizoma (Zingiberis rhizoma) | NO-ID 
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive, D:bloating, D:indigestion, D:nausea
     (no abstract)
  REF-0164 [traditional] 2013  | Anti-oxidative and anti-inflammatory effects of ginger in health and physical activity: a review | NO-ID !TAG review-title/traditional
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive, D:arthritis, D:back-pain, D:inflammation, D:pain, D:skin-irritation
     (no abstract)
  REF-0269 [clinical] 2007  | Risk of warfarin-related bleeding events and supratherapeutic international normalized ratios associated with complementary and alternative medicine | doi:10.1592/phco.27.9.1237 
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive
     C: The use of CAM by patients receiving warfarin is common, and consumption of coenzyme Q(10) or ginger appears to increase the risk of bleeding in this population.
  REF-0295 [systematic-review] 2014  | A systematic review and meta-analysis of the effect and safety of ginger in the treatment of pregnancy-associated nausea and vomiting | doi:10.1186/1475-2891-13-20 
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive, D:indigestion, D:nausea
     C: This review suggests potential benefits of ginger in reducing nausea symptoms in pregnancy (bearing in mind the limited number of studies, variable outcome reporting and low quality of evidence). Ginger did not significantly affect vomiting episodes, nor pose a risk for side-effects or adverse events during pregnancy. Based on evidence from this SR, ginger could be considered a harmless and possibly effective alterna
     !NULL: Ginger did not significantly reduce the number of vomiting episodes during NVP, when compared to placebo, although there was a trend towards improvement (MD 0.
     !NULL: Ginger did not significantly affect vomiting episodes, nor pose a risk for side-effects or adverse events during pregnancy.
  REF-0605 [systematic-review] 2020 Journal of International Medical Researc | Efficacy of herbal medicine (cinnamon/fennel/ginger) for primary dysmenorrhea: a systematic review and meta-analysis of randomized controlled trials | doi:10.1177/0300060520936179 
     used: A:analgesic, A:antispasmodic, D:menstrual-cramps, D:pain
     C: For primary dysmenorrhea, cinnamon/fennel/ginger effectively reduced pain intensity, and cinnamon shortened the duration of pain. Further studies are needed to confirm our results.
  REF-0634 [rct] 2023 Journal of the Academy of Nutrition and  | Effect of a Standardized Ginger Root Powder Regimen on Chemotherapy-Induced Nausea and Vomiting: A Multicenter, Double-Blind, Placebo-Controlled Rando | doi:10.1016/j.jand.2023.09.003 
     used: A:digestive, D:indigestion
     C: Ginger supplementation was a safe adjuvant to antiemetic medications for CINV that enhanced QoL during chemotherapy treatment. Future trials are needed to examine dose-dependent responses to verify optimal dosing regimens.
     !NULL: The null hypothesis was no difference between groups.
     !NULL: There was no effect of ginger on anticipatory or acute CINV, health-related QoL, anxiety, or depression.
  REF-0635 [systematic-review] 2020 Journal of Maternal-Fetal and Neonatal M | Effect of ginger in the treatment of nausea and vomiting compared with vitamin B6 and placebo during pregnancy: a meta-analysis | doi:10.1080/14767058.2020.1712714 
     used: A:digestive, D:indigestion, D:nausea
     C: Ginger supplementation significantly relieve general NVP symptom and nausea compared with placebo, but no significant effect on vomiting. Moreover, ginger is more effective than vitamin B6 in treating NVP, although, there were no significant differences. Further, rigidly designed RCTs with larger sample sizes are needed to verify the effectiveness of ginger supplementation for treatment NVP compared with vitamin B6.
     !NULL: 9%], but not significant in reducing vomiting [SMD = 0.
     !NULL: Besides, ginger intervention has no significant effect on improving general symptom of NVP [OR = 1.
     !NULL: Conclusions Ginger supplementation significantly relieve general NVP symptom and nausea compared with placebo, but no significant effect on vomiting.
  REF-0637 [systematic-review] 2022 Nutrients | A Meta-Analysis of the Impact of Nutritional Supplementation on Osteoarthritis Symptoms | doi:10.3390/nu14081607 
     used: A:analgesic, A:anti-inflammatory, D:arthritis, D:inflammation, D:pain
     C: Thus, curcumin and ginger supplementation can have a favorable impact on knee OA symptoms. Other studies are needed to better assess the effects of omega-3 and vitamin D.
  REF-0638 [systematic-review] 2025 Nutrients | Comparative Effectiveness of Nutritional Supplements in the Treatment of Knee Osteoarthritis: A Network Meta-Analysis | doi:10.3390/nu17152547 
     used: A:analgesic, A:anti-inflammatory, D:arthritis, D:inflammation, D:pain
     C: Nutritional supplements, particularly Boswellia, appear to be effective and well-tolerated for improving KOA symptoms and function. These results suggest that certain supplements may be useful as part of non-pharmacological KOA management. However, further large-scale, well-designed randomized controlled trials (RCTs) are needed to confirm these findings, particularly those that include more standardized dosages and 
  REF-0639 [systematic-review] 2019 Medicine (Baltimore) | Dietary ginger as a traditional therapy for blood sugar control in patients with type 2 diabetes mellitus: A systematic review and meta-analysis | doi:10.1097/MD.0000000000015054 
     used: A:analgesic, A:anti-inflammatory, A:antioxidant, A:antispasmodic, A:digestive
     C: This analysis involving patients with T2DM showed no significant difference in FBS with ginger consumption. However, dietary ginger significantly improved HbA1c from baseline to follow-up showing that this natural medicine might have an impact on glucose control over a longer period of time in patients with T2DM.
     !NULL: The results showed no significant difference in FBS (WMD: 1.
     !NULL: For the T2DM patients who did not consume ginger, no significant difference in FBS was observed (WMD: -0.
     !NULL: 02) whereas in the control group, no significant difference in HbA1c was observed (WMD: -0.
