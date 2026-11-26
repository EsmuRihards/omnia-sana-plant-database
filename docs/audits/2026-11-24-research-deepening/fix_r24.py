"""Research-deepening batch 24 (panax-ginseng, passiflora-incarnata, paullinia-cupana, pelargonium-sidoides,
petasites-hybridus). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5548.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 24'

SPEC = [
    # guarana
    ('REF-5548', '11419773', 'guaranaventricularfibrillation', 'clinical'),
    ('REF-5549', '25632790', 'guaranacaffeinepoisoning', 'clinical'),
    # pelargonium
    ('REF-5550', '17696580', 'pelargoniumallergy', 'clinical'),
    ('REF-5551', '22381150', 'pelargoniumlivercausality', 'clinical'),
    ('REF-5552', '41890334', 'pelargoniumliversafety', 'clinical'),
    ('REF-5553', '36865690', 'pelargoniumchildrensafety', 'clinical'),
    # butterbur
    ('REF-5554', '31083451', 'petadolexliverinjury', 'clinical'),
    ('REF-5555', '35585841', 'petasitesmigrainereview', 'narrative-review'),
    # passionflower
    ('REF-5556', '10696928', 'passionflowerqt', 'clinical'),
    ('REF-5557', '29458926', 'passionflowerpregnancy', 'clinical'),
    ('REF-5558', '19441067', 'valerianpassionflowerlorazepam', 'clinical'),
    # ginseng
    ('REF-5559', '35691259', 'ginsengmenopause', 'meta-analysis'),
    ('REF-5560', '28707603', 'ginsenghypertension', 'meta-analysis'),
    ('REF-5561', '42943019', 'ginsengrg3bloodpressure', 'rct'),
    ('REF-5562', '35509826', 'ginsengmetabolic', 'meta-analysis'),
    ('REF-5563', '40289951', 'redginsengstress', 'rct'),
    ('REF-5564', '34858175', 'redginsenghandoa', 'rct'),
    ('REF-5565', '42994854', 'redginsengfibroids', 'rct'),
    ('REF-5566', '18204104', 'ginsengpregnancy', 'systematic-review'),
    # ginseng (Europe PMC follow-up)
    ('REF-5567', '41838185', 'ginsengcancerfatigue', 'rct'),
    ('REF-5568', '41268314', 'whiteginsengstress', 'rct'),
    ('REF-5569', '42395024', 'redginsengdiabetesadjunct', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== ginseng
PLAN['panax_ginseng'] = [
    ('newpair', 'menopause', ['REF-5559'],
     'Ginseng reduced menopausal symptoms and improved quality of life compared with placebo in a 2022 meta-analysis of '
     'randomized trials (most trials at risk of bias)'),
    ('newpair', 'hot-flashes', ['REF-5559'],
     'Ginseng lowered hot flushes compared with placebo in a 2022 meta-analysis of randomized trials (small effect; most '
     'trials at risk of bias)'),
    ('newpair', 'high-blood-pressure', ['REF-5560', 'REF-5561', 'REF-5562'],
     'Korean red ginseng lowered blood pressure compared with placebo in people with prehypertension or hypertension '
     '(meta-analysis of double-blind trials; American ginseng trials did not), Rg3-enriched Korean ginseng lowered systolic '
     'pressure by 7-10 mmHg vs placebo over 12 weeks (randomized double-blind trial), and a 2022 meta-analysis found lower '
     'systolic and diastolic pressure'),
    ('newpair', 'stress', ['REF-5563', 'REF-5568'],
     'Red Panax ginseng lowered perceived stress and negative mood more than placebo in moderately stressed adults, and '
     'white ginseng lowered a composite stress index more than placebo over 12 weeks (randomized double-blind trials)'),
    ('add', 'fatigue', ['REF-5567']),
    ('note', 'fatigue',
     'Asian and American ginseng reduced fatigue in people with chronic illness (systematic review), and Panax ginseng '
     'extract reduced fatigue more than placebo in gastrointestinal cancer survivors over 4 weeks (randomized double-blind '
     'trial)'),
    ('nulladd', 'blood-sugar', ['REF-5569']),
    ('note', 'blood-sugar',
     'Blood-sugar lowering effects reviewed (review); a systematic review of red ginseng trials in type 2 diabetes found the '
     'evidence not convincing, and in a 2026 double-blind trial added to diabetes medicines, Korean red ginseng did not '
     'change fasting glucose or HbA1c compared with placebo'),
    ('add', 'arthritis', ['REF-5564']),
    ('note', 'arthritis',
     'Korean red ginseng eased hand osteoarthritis pain and improved hand function compared with placebo in postmenopausal '
     'women (randomized double-blind trial)'),
]
POST['panax_ginseng'] = [
    ('cinew', {'note': 'Hormones: in a 6-month randomized double-blind trial in 69 premenopausal women with uterine fibroids, '
                       'Korean red ginseng did not make the fibroids grow more than placebo and did not change reproductive '
                       'hormones.',
               'severity': 'info', 'reference_ids': ['REF-5565']}),
    ('cinew', {'note': 'Pregnancy: a 2008 systematic review found no adverse effects in a pregnancy cohort study and judged '
                       'reports of masculinising effects in a newborn to be due to an adulterant, but advised caution, '
                       'especially in the first trimester; there are no human studies in breastfeeding.',
               'severity': 'info', 'reference_ids': ['REF-5566']}),
]
NOTES['panax_ginseng'] = (
    'Searched PubMed (Panax ginseng / Korean, Asian or Korean red ginseng / red ginseng tiab: 405 HT, 130 SR, 905 SAFE '
    'hits), Europe PMC (re-run after an interrupted session), ClinicalTrials.gov (100) and OpenAlex. Huge plant: screened '
    'SRs, conditions without a pair and safety; low libido (8), fatigue (7) and cholesterol (7) were not padded; American '
    'ginseng (P. quinquefolius) and notoginseng results were not counted. Added: NEW menopause and hot-flashes pairs (2022 '
    'MA of placebo RCTs; the 2013 SR it updates was not added), NEW high-blood-pressure pair (2017 MA of double-blind RCTs, '
    '2026 Rg3 RCT, 2022 metabolic MA), NEW stress pair (2025 RCT), 2021 hand OA RCT to arthritis (replacing the inferred '
    'note); fibroid-safety RCT and pregnancy SR as info notes; via Europe PMC: 2026 cancer-survivor fatigue RCT to fatigue, '
    '2025 white ginseng RCT to stress, 2026 diabetes add-on RCT as a no-effect study on blood-sugar. Not added: 2021 '
    'genitourinary-syndrome RCT (only patient-reported symptoms improved), 2026 red ginseng glucose RCT (within-group '
    'changes only), ginseng berry andropause RCT (libido already 8), KRG hangover complex (combination); 2019 Thorax COPD RCT (no difference from placebo; '
    'no respiratory pair exists), immune-enhancement RCTs (NK-cell markers only), 2019 high-stress RCT (biomarkers and one '
    'cognitive test), prediabetes RCTs and the metabolic MA for blood sugar (blood-sugar left as is beside its null SR), '
    'ginseng in multi-herb products (Saengmaeksan, aronia mixture, chia fibre), injectable Chinese products (Shenmai, '
    'Shenfu, Aidi), mouse drug-interaction studies.')

# ================================================================== passionflower
PLAN['passiflora_incarnata'] = []
POST['passiflora_incarnata'] = [
    ('cinew', {'note': 'Heart: a 34-year-old woman developed severe nausea, vomiting, drowsiness, a prolonged QT interval and '
                       'runs of ventricular tachycardia after taking passionflower at usual doses, and needed hospital '
                       'heart monitoring (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5556']}),
    ('ciadd', 'Use in pregnancy and breastfeeding is not recommended.', ['REF-5557']),
    ('dciadd', 'sedatives-cns-depressants', ['REF-5558']),
]
NOTES['passiflora_incarnata'] = (
    'Searched PubMed (Passiflora incarnata / passionflower / passion flower / maypop tiab: 62 HT, 22 SR, 76 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (12) and OpenAlex. INTEGRITY HOLD applies (owner decision 2026-11-25): existing pairs '
    'unchanged and nothing new added from the flagged group; anxiety (10), stress (8) and insomnia (7) were not padded '
    'anyway (dental-anxiety RCTs 2021-2025, sertraline add-on trial, Cochrane 2007 not added). Added: 2000 QT-prolongation '
    'and ventricular tachycardia case as a heart caution; 2018 case series of five pregnancies with neonatal complications '
    'to the pregnancy caution; 2009 valerian + passionflower + lorazepam case to the approved sedatives interaction. Not '
    'added: 2001 opioid-withdrawal RCT (no vocab condition), ADHD reviews, menopause comparison with St John\'s wort '
    '(active comparator), melatonin vs passionflower (active comparator), Euphytose, Ze 185 and other combinations, '
    'benzodiazepine-tapering real-world studies, Passiflora edulis (passion fruit) studies.')

# ================================================================== guarana
PLAN['paullinia_cupana'] = []
POST['paullinia_cupana'] = [
    ('cinew', {'note': 'Heart rhythm: guarana products can deliver dangerous doses of caffeine. A 25-year-old woman with mitral '
                       'valve prolapse developed ventricular fibrillation after a guarana "natural energy" drink, and a man '
                       'who swallowed guarana tablets containing 1.6 g of caffeine developed caffeine poisoning with atrial '
                       'fibrillation (case reports).',
               'severity': 'warning', 'reference_ids': ['REF-5548', 'REF-5549']}),
]
NOTES['paullinia_cupana'] = (
    'Searched PubMed (Paullinia cupana / guarana tiab: 61 HT, 15 SR, 105 SAFE hits; many were energy-drink or '
    'multi-ingredient studies), Europe PMC, ClinicalTrials.gov (19) and OpenAlex. Fatigue (9) and cognition (8) were not '
    'padded (2017 head-and-neck chemoradiotherapy RCT, 2023-2024 exercise-cognition RCTs not added). Added: 2001 '
    'ventricular fibrillation and 2014 caffeine-poisoning atrial fibrillation cases as a heart-rhythm warning. Not added: '
    '2016 anorexia and 2013 hot-flush pilots (single-arm, uncontrolled), energy-drink case reports and reviews (many '
    'ingredients), Ma Huang + guarana and other weight-loss combinations, multivitamin + guarana trials, topical '
    'cosmetic studies, 2000 myoglobinuria case with ginkgo and kava (combination).')

# ================================================================== pelargonium
PLAN['pelargonium_sidoides'] = []
POST['pelargonium_sidoides'] = [
    ('cinew', {'note': 'Allergy: the WHO pharmacovigilance programme received 34 reports of suspected allergic reactions to '
                       'pelargonium extract (all from Germany), some of them immediate-type reactions; two people needed '
                       'treatment for circulatory collapse (pharmacovigilance review).',
               'severity': 'caution', 'reference_ids': ['REF-5550']}),
    ('cinew', {'note': 'Liver: a structured causality assessment of 15 German spontaneous reports of suspected liver injury '
                       'found no probable link to pelargonium, with other possible causes and poor data in almost all cases; '
                       'a 2026 post-authorisation study of 300 adults found no signs of liver toxicity after 7 days, and an '
                       'open randomized trial in 591 children aged 1-5 raised no safety concerns.',
               'severity': 'info', 'reference_ids': ['REF-5551', 'REF-5552', 'REF-5553']}),
]
NOTES['pelargonium_sidoides'] = (
    'Searched PubMed (Pelargonium sidoides / EPs 7630 / Umckaloabo tiab: 69 HT, 20 SR, 54 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (9) and OpenAlex. Bronchitis (9), cold (8), sinusitis (8), sore throat, cough and infection (7) '
    'were not padded (2026 Swiss pragmatic bronchitis trial, 2022 cough MA, 2023 work-inability MA, 2019 common cold RCT '
    'and older company RCTs not added; most are already pooled in the cited MAs). Added: 2007 WHO pharmacovigilance '
    'allergy review as a caution; liver-causality analysis, 2026 liver-safety study and 2023 paediatric safety trial as an '
    'info note. Not added: honey/propolis/zinc combinations, EPs 7630 vs amoxicillin or roxithromycin (active comparators), '
    'hand-foot-and-mouth disease open study (no vocab condition), chemokine studies (surrogate), nephrotoxicity cell study.')

# ================================================================== butterbur
PLAN['petasites_hybridus'] = []
POST['petasites_hybridus'] = [
    ('cinew', {'note': 'Liver: even the PA-free root extract Petadolex has been linked to rare cases of herb-induced liver '
                       'injury; most were mild, but nine were severe and two people needed a liver transplant, while the '
                       'others recovered after stopping (case analysis). Many patients also took other pain medicines that '
                       'can harm the liver. In rats, bile-duct changes appeared only at 45-90 times the maximum clinical '
                       'dose (review).',
               'severity': 'warning', 'reference_ids': ['REF-5554', 'REF-5555']}),
]
NOTES['petasites_hybridus'] = (
    'Searched PubMed (Petasites hybridus / butterbur / Petadolex / Ze 339 tiab: 46 HT, 9 SR, 88 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (1) and OpenAlex. Allergy (7) and migraine/headache (6) were not padded: the placebo RCTs of Ze 339 '
    'in allergic rhinitis and the 2006 migraine SR pool trials the record\'s SR and RCTs already cite. Added: 2019 analysis '
    'of Petadolex liver-injury cases with the 2022 safety review as a liver WARNING (the record had only the raw-plant PA '
    'caution). Not added: 2008 paediatric migraine RCT (butterbur better than placebo only at follow-up, not after '
    'treatment), 2004 asthma add-on crossover (airway challenge and exhaled NO only, surrogate), Ze 185 combination, '
    'Japanese butterbur (Petasites japonicus) anaphylaxis cases and toxicology (other species), postmarketing surveillance '
    'studies (uncontrolled).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r24_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
