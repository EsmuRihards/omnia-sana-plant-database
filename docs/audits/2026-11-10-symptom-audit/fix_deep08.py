"""Deep re-sweep of batch 8 (geum-rivale .. hippophae-rhamnoides) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3563..REF-3593 (PubMed efetch, deep/abstracts.json).
The Ginkgo display-name fix ("Ginko" -> "Ginkgo", former_slugs: [ginko]) was a text edit made before this ran."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3563', '41641880', 'ginkgocochrane2026', 'systematic-review'),
    ('REF-3564', '23744597', 'ginkgoclaudicationcochrane', 'systematic-review'),
    ('REF-3565', '39895346', 'egb761milddementia', 'meta-analysis'),
    ('REF-3566', '16808927', 'egb761anxiety', 'rct'),
    ('REF-3567', '38562465', 'ginkgodepression', 'meta-analysis'),
    ('REF-3568', '35781715', 'ginkgoinflammation', 'meta-analysis'),
    ('REF-3569', '30391446', 'licoricesorethroat', 'meta-analysis'),
    ('REF-3570', '23921656', 'licoricegargle', 'rct'),
    ('REF-3571', '37786470', 'licoriceaphthous', 'systematic-review'),
    ('REF-3572', '39929150', 'gutgardreflux', 'rct'),
    ('REF-3573', '21747893', 'gutgarddyspepsia', 'rct'),
    ('REF-3574', '36870516', 'licoriceburns', 'rct'),
    ('REF-3575', '9621139', 'hamamelisuvb', 'rct'),
    ('REF-3576', '11185727', 'harpagophytumdiacerhein', 'rct'),
    ('REF-3577', '12725580', 'ivyasthmareview', 'meta-analysis'),
    ('REF-3578', '24916707', 'ivyasthmaaddon', 'rct'),
    ('REF-3579', '31413233', 'hericiumcognition', 'rct'),
    ('REF-3580', '40959699', 'hericiumsr', 'systematic-review'),
    ('REF-3581', '34837382', 'rosellecochrane', 'systematic-review'),
    ('REF-3582', '39870328', 'hibiscusoverview', 'meta-analysis'),
    ('REF-3583', '32156406', 'hibiscusglycemic', 'meta-analysis'),
    ('REF-3584', '31833112', 'hibiscuslipids', 'meta-analysis'),
    ('REF-3585', '38878905', 'hibiscusobesity', 'meta-analysis'),
    ('REF-3586', '36043374', 'seabuckthornmets', 'meta-analysis'),
    ('REF-3587', '17593932', 'seabuckthorninfections', 'rct'),
    ('REF-3588', '23131570', 'seabuckthornhemodialysis', 'rct'),
    ('REF-3589', '19288149', 'seabuckthornlipids', 'rct'),
    ('REF-3590', '41829976', 'seabuckthornconstipation', 'rct'),
    ('REF-3591', '25104582', 'seabuckthornvaginal', 'rct'),
    ('REF-3592', '33792111', 'seabuckthornburns', 'rct'),
    ('REF-3593', '15539258', 'seabuckthornatopic', 'clinical'),
])

BIB = dict(
    retag={'REF-0824': 'narrative-review', 'REF-0825': 'narrative-review',   # Ginkgo reviews tagged traditional/preclinical
           'REF-0826': 'narrative-review', 'REF-0828': 'narrative-review',   # licorice reviews tagged traditional
           'REF-0834': 'narrative-review',                                    # ivy review tagged traditional
           'REF-2052': 'preclinical'},                                        # witch hazel: fibroblast gene expression, not an RCT
    delete=['REF-0157',            # Lion's mane: no abstract, no identifier, not on Crossref/PubMed
            'REF-0049', 'REF-0319',   # Sea buckthorn: unlocatable (no identifier, not on Crossref)
            'REF-0835'],           # Ivy + Coptis mixture (animal study of a two-herb mixture)
    new=NEW)

PLAN = {
    'geum_rivale': [
        ('arm', 'antidiarrheal', ['REF-2769', 'REF-2768']), ('arm', 'vulnerary', ['REF-2769']),   # 1954 tannin anatomy; elastase/tannin screen
        ('refadd', ['REF-2769']),
        ('note', 'inflammation', 'Water avens extract strongly inhibited an inflammatory pathway (PAF-induced exocytosis) in lab tests (preclinical)'),
        ('note', 'infection', 'Extracts and their triterpenes were antibacterial and antifungal in lab tests (preclinical)'),
        ('note', 'wounds', 'inferred from antimicrobial and astringent action'),
        ('note', 'skin-irritation', 'inferred from anti-inflammatory and astringent action'),
        ('note', 'diarrhea', 'inferred from astringent (tannin) action'),
    ],
    'ginkgo_biloba': [
        ('arm', 'neuroprotective', ['REF-0056']),   # the GEM prevention trial was null - not evidence for the action
        ('add', 'cognitive-function', ['REF-3563', 'REF-3565']), ('add', 'memory', ['REF-3563', 'REF-3565']),
        ('nulladd', 'cardiovascular-support', ['REF-3564']),
        ('add', 'inflammation', ['REF-3568']),
        ('newpair', 'anxiety', ['REF-3566', 'REF-2546'], 'Ginkgo extract EGb 761 reduced anxiety vs placebo in a randomized trial in generalized anxiety and adjustment disorder; a network meta-analysis also found it effective (small trials)'),
        ('newpair', 'depression', ['REF-3567'], 'A meta-analysis of 21 trials found ginkgo lowered depression scores compared with control groups'),
        ('note', 'cognitive-function', 'Ginkgo extract EGb 761 improved cognition in people with dementia in trials and meta-analyses; a 2026 Cochrane review found small to moderate benefits in dementia but probably little or no effect in mild cognitive impairment, and a large prevention trial found it did not reduce dementia'),
        ('note', 'memory', 'Ginkgo extract EGb 761 improved cognition in people with dementia in trials and meta-analyses; a 2026 Cochrane review found probably little or no effect in mild cognitive impairment, and a large prevention trial found it did not reduce dementia'),
        ('note', 'cardiovascular-support', 'Used for peripheral arterial disease (intermittent claudication) (WHO monograph); a Cochrane review found no clinically significant benefit'),
        ('note', 'inflammation', 'Ginkgo leaf extract lowered the inflammation markers CRP, IL-6 and TNF-alpha vs placebo in a meta-analysis of trials'),
    ],
    'glycyrrhiza_glabra': [
        ('newpair', 'sore-throat', ['REF-3569', 'REF-3570', 'REF-0308'], 'Gargling or applying licorice before surgery prevented postoperative sore throat (meta-analysis; randomized trial); a traditional soothing remedy for sore throats (WHO monograph)'),
        ('newpair', 'oral-health', ['REF-3571'], 'Topical licorice (paste, patch or mouthwash) helped recurrent mouth ulcers heal in clinical trials (systematic review)'),
        ('newpair', 'wounds', ['REF-3574'], 'A licorice root extract sped healing of second-degree burns in a randomized trial'),
        ('add', 'acid-reflux', ['REF-3572']), ('add', 'indigestion', ['REF-3573']),
        ('note', 'acid-reflux', 'A deglycyrrhizinated licorice extract (GutGard) relieved heartburn and regurgitation vs placebo in a randomized trial; traditional use for burning sensation and indigestion (EU herbal monograph)'),
        ('note', 'indigestion', 'A licorice extract (GutGard) relieved functional dyspepsia vs placebo in a randomized trial; traditional use for dyspepsia (EU herbal monograph; WHO monograph)'),
        ('note', 'arthritis', 'Traditional anti-inflammatory for rheumatism and arthritis (WHO monograph); anti-inflammatory compounds reported in lab studies (reviews)'),
        ('note', 'bronchitis', 'Traditional expectorant for coughs and bronchial catarrh (WHO monograph)'),
        ('note', 'cold', 'Traditional expectorant for cough associated with colds (EU herbal monograph)'),
        ('note', 'cough', 'Traditional expectorant for cough (EU herbal monograph; WHO monograph)'),
        ('note', 'infection', 'Traditional antiviral use (WHO monograph); glycyrrhetinic acid was active against tuberculosis bacteria in the lab (preclinical)'),
        ('note', 'inflammation', 'Traditional anti-inflammatory for allergic reactions and arthritis (WHO monograph); licorice flavonoids reduced inflammatory markers in lab studies (preclinical)'),
        ('note', 'respiratory-support', 'Traditional expectorant for cough and bronchial catarrh (EU herbal monograph; WHO monograph)'),
    ],
    'gymnema_sylvestre': [
        ('add', 'metabolic-support', ['REF-2541']), ('add', 'high-cholesterol', ['REF-2540']),
        ('note', 'blood-sugar', 'Gymnema lowered fasting and post-meal blood sugar and HbA1c in type 2 diabetes in meta-analyses of mostly small, low-quality trials'),
        ('note', 'metabolic-support', 'In meta-analyses gymnema lowered blood sugar, blood lipids and diastolic blood pressure (low-quality trials)'),
        ('note', 'high-cholesterol', 'Gymnema lowered triglycerides and total and LDL cholesterol in meta-analyses (low-quality trials)'),
    ],
    'hamamelis_virginiana': [
        ('arm', 'vulnerary', ['REF-2052']), ('refadd', ['REF-2052']),   # UV-A fibroblast gene-expression study, not wound healing
        ('add', 'skin-irritation', ['REF-3575']), ('add', 'inflammation', ['REF-3575']),
        ('nulladd', 'skin-irritation', ['REF-3527']), ('nulladd', 'inflammation', ['REF-3527']),
        ('note', 'skin-irritation', 'Astringent for minor skin inflammation, applied topically (EU herbal monograph); a 10% witch hazel lotion reduced sunburn redness in one randomized trial, but an extract was no better than its base cream in another'),
        ('note', 'inflammation', 'Astringent for minor inflammation of the skin and mouth (EU herbal monograph); a 10% witch hazel lotion reduced sunburn redness in one randomized trial, but an extract was no better than its base cream in another'),
        ('note', 'oral-health', 'Astringent for minor inflammation of the mouth lining (EU herbal monograph)'),
        ('note', 'diarrhea', 'Traditional astringent for diarrhoea (Herbal Reality)'),
        ('note', 'cancer', 'Hamamelitannin slowed colon cancer cells in the lab without harming normal cells (preclinical)'),
    ],
    'harpagophytum_procumbens': [
        ('add', 'back-pain', ['REF-1261']), ('add', 'pain', ['REF-1261']),
        ('add', 'arthritis', ['REF-3576']),
        ('note', 'arthritis', 'Devil\'s claw powder matched the drug diacerhein for hip and knee osteoarthritis pain in a randomized trial, with fewer side effects; systematic reviews found limited to moderate evidence, and one judged trial quality too poor for a definitive answer'),
        ('note', 'back-pain', 'Extracts with 50-100 mg harpagoside daily relieved chronic low back pain vs placebo, and one matched rofecoxib (Cochrane review: moderate-quality evidence at best; systematic review)'),
        ('note', 'pain', 'Devil\'s claw eased low back and osteoarthritis pain in trials (Cochrane review; systematic reviews; moderate-quality evidence at best)'),
    ],
    'hedera_helix': [
        ('arm', 'antispasmodic', ['REF-2314']), ('refadd', ['REF-2314']),   # the extract CONTRACTED stomach smooth muscle
        ('drop', 'muscle-spasm'),   # inferred from airway/gut smooth-muscle work: off-target (inv. 11)
        ('purge', 'REF-0835'),      # ivy + Coptis two-herb mixture
        ('add', 'asthma', ['REF-3577']), ('nulladd', 'asthma', ['REF-3578']),
        ('note', 'asthma', 'A review of randomized trials found ivy leaf extract improved lung function in children with chronic asthma (small evidence base, one placebo-controlled trial); an add-on trial found no effect on its main lung-function outcomes'),
        ('note', 'bronchitis', 'Ivy leaf extract eased productive cough and acute bronchitis in trials, including vs placebo; an updated systematic review found the effects minimal at best'),
        ('note', 'cough', 'Ivy leaf extract eased acute productive cough vs placebo in a randomized trial; an updated systematic review found the effects minimal at best'),
        ('note', 'respiratory-support', 'Ivy leaf extract eased productive cough in acute respiratory infections in trials; an updated systematic review found the effects minimal at best'),
    ],
    'hericium_erinaceus': [
        ('purge', 'REF-0157'),
        ('arm', 'anti-inflammatory', ['REF-0170']), ('arm', 'digestive', ['REF-0170']), ('arm', 'immunomodulator', ['REF-0170']),
        ('add', 'cognitive-function', ['REF-3579', 'REF-3580']), ('nulladd', 'memory', ['REF-3579']),
        ('note', 'cognitive-function', 'Lion\'s mane improved cognitive scores in mild cognitive impairment and early Alzheimer\'s disease in small placebo-controlled trials (systematic review); acute effects in healthy young adults were mixed'),
        ('note', 'memory', 'Lion\'s mane improved cognitive scores in mild cognitive impairment and early Alzheimer\'s disease in small placebo-controlled trials, but memory-specific tests and an acute trial in young adults showed no clear effect'),
        ('note', 'cancer', 'Lion\'s mane compounds slowed gastric cancer cells in lab studies (review; preclinical)'),
        ('note', 'inflammation', 'Lion\'s mane polysaccharides eased colitis in mice, and anti-inflammatory effects are reported in lab studies (review; preclinical)'),
        ('note', 'immune-support', 'Lion\'s mane polysaccharides stimulated immune cells in the lab (preclinical)'),
    ],
    'hibiscus_sabdariffa': [
        ('add', 'high-blood-pressure', ['REF-1846', 'REF-1847', 'REF-3582']), ('nulladd', 'high-blood-pressure', ['REF-3581']),
        ('add', 'cardiovascular-support', ['REF-3582']), ('nulladd', 'cardiovascular-support', ['REF-3581']),
        ('add', 'high-cholesterol', ['REF-3584', 'REF-3583', 'REF-3582']), ('nulladd', 'high-cholesterol', ['REF-0567']),
        ('add', 'blood-sugar', ['REF-3583', 'REF-3582']),
        ('add', 'metabolic-support', ['REF-3582', 'REF-3584']), ('nulladd', 'metabolic-support', ['REF-3585']),
        ('note', 'high-blood-pressure', 'Hibiscus lowered blood pressure in meta-analyses, most in people with raised blood pressure, and matched captopril in one trial; a Cochrane review judged the evidence vs placebo insufficient (very low certainty)'),
        ('note', 'cardiovascular-support', 'Hibiscus lowered blood pressure and improved some blood lipid and sugar markers in meta-analyses; a Cochrane review judged the blood pressure evidence vs placebo insufficient (very low certainty)'),
        ('note', 'high-cholesterol', 'Meta-analyses disagree: some found hibiscus lowered total and LDL cholesterol, others found no significant effect on blood lipids'),
        ('note', 'blood-sugar', 'Hibiscus lowered fasting blood sugar in meta-analyses of randomized trials'),
        ('note', 'metabolic-support', 'Hibiscus improved blood pressure, cholesterol and blood sugar markers in meta-analyses; it did not reduce body weight in a 2024 meta-analysis'),
    ],
    'hippophae_rhamnoides': [('arm', a, ['REF-0206']) for a in ('anti-inflammatory', 'antidiabetic', 'antioxidant', 'emollient', 'immunomodulator', 'vulnerary')] + [
        ('refadd', ['REF-0206']),   # 1971 taxonomic monograph: kept as a taxonomy reference, never as activity evidence
        ('purge', 'REF-0049'), ('purge', 'REF-0319'),
        ('drop', 'cold'),           # immunomodulator-inferred; the berries did not prevent colds in an RCT (REF-3587)
        ('nulladd', 'immune-support', ['REF-3587']),
        ('add', 'inflammation', ['REF-3587']), ('nulladd', 'inflammation', ['REF-3588']),
        ('nulladd', 'blood-sugar', ['REF-3586']),
        ('add', 'cardiovascular-support', ['REF-3586']),
        ('newpair', 'high-cholesterol', ['REF-3586'], 'Sea buckthorn lowered triglycerides and total and LDL cholesterol in a meta-analysis of 15 trials, mainly in people with abnormal blood lipids; a trial in healthy adults found no effect'),
        ('nulladd', 'high-cholesterol', ['REF-3589']),
        ('newpair', 'constipation', ['REF-3590'], 'A sea buckthorn fruit extract increased complete bowel movements and normalised stools vs placebo in chronic constipation in a randomized trial'),
        ('newpair', 'menopause', ['REF-3591'], 'Sea buckthorn oil capsules improved vaginal atrophy (dryness) in postmenopausal women vs placebo in a randomized trial'),
        ('add', 'wounds', ['REF-3592']),
        ('nulladd', 'eczema', ['REF-3593']),
        ('note', 'immune-support', 'Sea buckthorn polysaccharides stimulated immune cells in lab studies (reviews); the berries did not prevent colds or digestive infections in a randomized trial'),
        ('note', 'inflammation', 'Sea buckthorn berries lowered CRP, an inflammation marker, in a randomized trial; oil capsules did not change inflammation markers in haemodialysis patients'),
        ('note', 'blood-sugar', 'Reviewed for blood-sugar benefits (review); a meta-analysis of trials found no effect on blood sugar'),
        ('note', 'cardiovascular-support', 'Reviewed for cardiovascular protection (reviews); improved blood lipids in a meta-analysis of trials'),
        ('note', 'cancer', 'Sea buckthorn compounds and fruit-peel extract reduced tumour promotion and breast tumours in animal models (preclinical)'),
        ('note', 'wounds', 'Sea buckthorn cream healed second-degree burns faster than silver sulfadiazine in a randomized trial; traditional wound remedy (review)'),
        ('note', 'eczema', 'Traditional skin remedy with dermatological effects reviewed (review); oral seed and pulp oils did no better than placebo for atopic eczema in a controlled trial'),
        ('note', 'skin-irritation', 'Traditional skin remedy with anti-inflammatory and skin-healing effects reviewed (review)'),
    ],
}

NOTES = {
    'geum_rivale': 'Deep re-sweep. REF-2769 (1954 tannin anatomy, no abstract) removed from antidiarrheal and vulnerary actions (kept in references); REF-2768 (Rosaceae elastase/tannin screen) removed from antidiarrheal. Notes rewritten to their lab sources. No trials on PubMed.',
    'ginkgo_biloba': 'Deep re-sweep. Primary common name fixed: "Ginko" was a misspelling -> "Ginkgo" (owner decision 2026-11-12); former_slugs [ginko] so every /ginko/ URL 301s to /ginkgo/. GEM prevention trial REF-0056 removed from the neuroprotective action (null trial). Added 2026 Cochrane review REF-3563 (small-moderate benefit in dementia, little or no effect in MCI) + EGb 761 mild-dementia MA REF-3565 to cognitive-function/memory; superseded Cochrane 2009 (19160216) not added. Cochrane claudication REF-3564 recorded as no-effect on cardiovascular-support. Inflammatory-marker MA REF-3568 added. New pairs (owner rule): anxiety (RCT REF-3566 + held NMA REF-2546), depression (MA REF-3567). REF-0824/REF-0825 retagged narrative-review. Not added (gaps): hyperlipidemia MA 42102021 (HDL vs Western medicine only; a T2DM MA 38264278 found no lipid or glucose effect).',
    'glycyrrhiza_glabra': 'Deep re-sweep. New pairs (owner rule): sore-throat (MA REF-3569 + RCT REF-3570 + WHO demulcent use), oral-health (aphthous-ulcer SR REF-3571), wounds (burn RCT REF-3574). GutGard (G. glabra, deglycyrrhizinated) RCTs added: reflux REF-3572, functional dyspepsia REF-3573. Inferred notes rewritten to the WHO/EU monographs. REF-0826/REF-0828 retagged narrative-review. OWNER DECISION, not added: liver-support - two NAFLD RCTs (22308054, 35785498) lowered liver enzymes, but the record\'s own contraindication lists liver disease. Gap: atopic-dermatitis gel trial 14522625 reports 2% vs 1% only, not vs base gel - no eczema pair.',
    'gymnema_sylvestre': 'Deep re-sweep. Notes rewritten to the held MAs (REF-2540, REF-2541); REF-2541 wired to metabolic-support and REF-2540 to high-cholesterol. REF-3060 (Leach 2007 SR) abstract states no conclusion - kept as is.',
    'hamamelis_virginiana': 'Deep re-sweep. REF-2052 retagged preclinical (fibroblast gene expression with volunteers\' plasma metabolites) and removed from the vulnerary action (kept in references). Hamamelis 10% lotion UVB-erythema RCT REF-3575 (beat vehicle) added to skin-irritation/inflammation; UV-erythema RCT REF-3527 (not significant vs vehicle) recorded as no-effect. Diaper-dermatitis RCT 41468068 not used (comparator was breast milk, no placebo).',
    'harpagophytum_procumbens': 'Deep re-sweep. Cochrane LBP 2014 REF-1261 ("seem to reduce pain more than placebo", moderate quality at best) added to back-pain and pain. OA RCT vs diacerhein REF-3576 added to arthritis (11143915 is the same trial in another journal - not added twice). Notes simplified.',
    'hedera_helix': 'Deep re-sweep. Muscle-spasm dropped (airway/gut smooth-muscle work; off-target, inv. 11). REF-2314 removed from antispasmodic (the extract contracted stomach strips; kept in references). REF-0835 (ivy + Coptis two-herb mixture, animals) purged and deleted. Asthma: review of RCTs REF-3577 added as support, add-on RCT REF-3578 (primary outcomes null) as no-effect. REF-0834 retagged narrative-review. Notes now state the updated SR REF-0833 finding (effects minimal at best).',
    'hericium_erinaceus': 'Deep re-sweep. REF-0157 (no abstract or identifier, not on Crossref/PubMed) purged and deleted. MCI trial REF-0170 removed from anti-inflammatory, digestive and immunomodulator actions. RCT REF-3579 (MMSE improved; memory tests did not) added to cognitive-function and recorded as no-effect for memory; SR REF-3580 added to cognitive-function. Gaps (not added): stress - REF-0640 only a trend (p=0.051); depression/anxiety - RCT 20834180 shows within-group change only, and the SR\'s mood claim rests on animal data.',
    'hibiscus_sabdariffa': 'Deep re-sweep. Cochrane 2021 REF-3581 (evidence vs placebo insufficient, very low certainty) recorded as no-effect for high-blood-pressure and cardiovascular-support; held trials REF-1846/REF-1847 wired directly to high-blood-pressure. Overview of reviews REF-3582, glycaemic/lipid MA REF-3583 and MetS lipid MA REF-3584 added; REF-0567 (no significant lipid effect) recorded as no-effect for high-cholesterol; obesity MA REF-3585 (no benefit) as no-effect for metabolic-support (weight).',
    'hippophae_rhamnoides': 'Deep re-sweep. REF-0206 (1971 taxonomic study) removed from all six actions (kept in references). REF-0049 and REF-0319 (no identifiers, unlocatable) purged and deleted. Cold dropped: immunomodulator-inferred and contradicted by the RCT REF-3587 (berries did not prevent colds); REF-3587 also no-effect for immune-support and support for inflammation (CRP lowered); haemodialysis RCT REF-3588 no-effect for inflammation. MetS MA REF-3586: no-effect for blood-sugar, support for cardiovascular-support; new pairs (owner rule): high-cholesterol (REF-3586; healthy-adult RCT REF-3589 no-effect), constipation (RCT REF-3590), menopause (vaginal atrophy RCT REF-3591). Burn RCT REF-3592 added to wounds. Oral-oil atopic dermatitis trial REF-3593 (no better than placebo) no-effect for eczema. Gaps: psoriasis trial 30679968 (single-blind, randomisation not stated); bloating (secondary outcome of REF-3590 only).',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 8', os.path.join(HERE, 'deep', 'd08_changes.tsv'), **BIB)
