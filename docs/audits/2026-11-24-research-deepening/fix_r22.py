"""Research-deepening batch 22 (nepeta-cataria, nigella-sativa, ocimum-tenuiflorum, oenothera-biennis, olea-europaea).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5521.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 22'

SPEC = [
    # catnip
    ('REF-5521', '9397511', 'catniptoddler', 'clinical'),
    # black seed
    ('REF-5522', '36150238', 'blackseedkneeoa', 'rct'),
    ('REF-5523', '38650731', 'blackseedosteoarthritis', 'systematic-review'),
    ('REF-5524', '28378356', 'blackseedprocessedkneeoa', 'rct'),
    ('REF-5525', '32548864', 'blackseedacnegel', 'rct'),
    ('REF-5526', '34722227', 'blackseedrhinosinusitis', 'rct'),
    ('REF-5527', '30873671', 'blackseedkidneystones', 'rct'),
    ('REF-5528', '38288065', 'blackcuminsleep', 'rct'),
    ('REF-5529', '37139438', 'blackcuminstresssleep', 'rct'),
    ('REF-5530', '30073256', 'blackseedoilcontactdermatitis', 'clinical'),
    ('REF-5531', '38844000', 'blackseedrhabdomyolysis', 'clinical'),
    ('REF-5532', '32201245', 'blackseedliverkidney', 'meta-analysis'),
    ('REF-5533', '32637272', 'blackseedprimrosethrombocytopenia', 'clinical'),
    # holy basil
    ('REF-5534', '33110312', 'tulsidentifrice', 'rct'),
    ('REF-5535', '24948862', 'tulsimouthwash', 'rct'),
    # evening primrose
    ('REF-5536', '29928122', 'primroseoilmsfatigue', 'rct'),
    ('REF-5537', '17764919', 'primroseoilepilepsy', 'narrative-review'),
    ('REF-5538', '21085832', 'primroseoillipoidpneumonia', 'clinical'),
    # olive
    ('REF-5539', '36271405', 'oliveleafcardiovascular', 'meta-analysis'),
    ('REF-5540', '39818111', 'oliveleafdiabetespilot', 'rct'),
    ('REF-5541', '9034680', 'oliveoilpatchtest', 'clinical'),
    # Europe PMC follow-up
    ('REF-5542', '41267796', 'blackseedpremenstrual', 'rct'),
    ('REF-5543', '40465634', 'blackseedepisiotomyemulgel', 'rct'),
    ('REF-5544', '41805711', 'oliveextractbloodpressure', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

THROMBO = ('Blood count: a woman who had taken black seed oil and evening primrose oil daily for about a month developed a '
           'severe drop in platelets with blood clots after surgery; the authors thought the supplements made it worse, but '
           'the cause is uncertain (case report).')

# ================================================================== catnip
PLAN['nepeta_cataria'] = []
POST['nepeta_cataria'] = [
    ('cinew', {'note': 'Children: a toddler who ate a large amount of catnip became drowsy and poorly responsive (central '
                       'nervous system depression) with no other cause found (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5521']}),
]
NOTES['nepeta_cataria'] = (
    'Searched PubMed (Nepeta cataria / catnip / catmint tiab: 3 HT, 3 SR, 22 SAFE hits; mostly insect-repellent and cat '
    'studies), Europe PMC, ClinicalTrials.gov (2: a multi-herb PCOS formula and Nepeta menthoides, another species) and '
    'OpenAlex. No human trial of catnip. Added: 1997 toddler CNS-depression case as a caution. Not added: 2023 essential-oil '
    'inhalation study in hypertensive women (24 oils, randomisation not stated), mosquito-repellent reviews (no vocab '
    'condition), Nepeta menthoides / meyeri / racemosa studies (other species). Settled.')

# ================================================================== black seed
PLAN['nigella_sativa'] = [
    ('add', 'arthritis', ['REF-5522', 'REF-5523']),
    ('nulladd', 'arthritis', ['REF-5524']),
    ('note', 'arthritis',
     'Oral black seed oil reduced knee osteoarthritis pain, WOMAC scores and paracetamol use compared with placebo '
     '(randomized double-blind trial); in a 2024 systematic review, topical oil beat placebo for pain in three of four '
     'trials but oral forms were inconsistent, and a processed black seed formula did not differ from placebo (randomized '
     'trial)'),
    ('newpair', 'acne', ['REF-5525'],
     'A black seed hydrogel applied twice a day for 2 months reduced acne severity, comedones, papules and pustules compared '
     'with a placebo gel (randomized double-blind trial)'),
    ('newpair', 'sinusitis', ['REF-5526'],
     'Black seed extract nasal drops improved chronic rhinosinusitis symptoms (SNOT-22) more than sesame oil placebo after 4 '
     'weeks (randomized double-blind trial)'),
    ('newpair', 'kidney-support', ['REF-5527'],
     'Black seed capsules (500 mg twice a day for 10 weeks) led to more kidney stones being passed or shrinking than '
     'placebo (randomized triple-blind trial)'),
    ('newpair', 'insomnia', ['REF-5528', 'REF-5529'],
     'A proprietary black seed oil extract (BlaQmax) improved sleep efficiency, total sleep time and time to fall asleep '
     'compared with placebo in people with unrefreshing sleep, and improved sleep scores over 90 days (randomized '
     'double-blind trials of the same product)'),
    ('newpair', 'stress', ['REF-5529'],
     'A proprietary black seed oil extract (BlaQmax) lowered perceived stress scores compared with placebo over 90 days '
     '(randomized double-blind trial)'),
    ('newpair', 'pms', ['REF-5542'],
     'Black seed supplements for 2 months reduced overall premenstrual syndrome scores compared with placebo (randomized '
     'double-blind trial)'),
    ('add', 'wounds', ['REF-5543']),
    ('note', 'wounds',
     'A black seed emulgel applied to episiotomy wounds improved healing (less redness, swelling and bruising) compared with '
     'placebo at 10 days after birth (randomized triple-blind trial)'),
    ('add', 'pain', ['REF-5543']),
    ('note', 'pain',
     'A black seed emulgel applied to episiotomy wounds lowered pain compared with placebo at 10 days after birth '
     '(randomized triple-blind trial); pain-relieving effects reported in animal studies (review)'),
]
POST['nigella_sativa'] = [
    ('cinew', {'note': 'Skin: black seed oil applied to the skin has caused severe allergic contact dermatitis; three women needed '
                       'hospital care for blistering, target-like lesions spreading beyond where the oil was applied, '
                       'resembling Stevens-Johnson syndrome, with fever and over 15% of the skin detaching (case series). '
                       'Thymoquinone may be the main culprit.',
               'severity': 'warning', 'reference_ids': ['REF-5530']}),
    ('cinew', {'note': 'Muscles, kidneys and liver: muscle breakdown (rhabdomyolysis), acute kidney injury and liver injury '
                       'followed drinking black seed oil (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5531']}),
    ('cinew', {'note': 'Liver and kidney tests: in a meta-analysis of 19 randomized trials (1,295 people), black seed lowered the '
                       'liver enzyme ALP and blood urea; creatinine rose slightly in three adjusted trials, and doses above '
                       '2,000 mg a day were reported to raise blood urea.',
               'severity': 'info', 'reference_ids': ['REF-5532']}),
    ('cinew', {'note': THROMBO, 'severity': 'info', 'reference_ids': ['REF-5533']}),
]
NOTES['nigella_sativa'] = (
    'Searched PubMed (Nigella sativa / black seed / black cumin / kalonji tiab, thymoquinone ti: 344 HT, 118 SR, 895 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (73) and OpenAlex. Huge plant: screened SRs, conditions without a pair and '
    'safety; blood sugar, blood pressure, cholesterol, metabolic and cardiovascular pairs (8) were not padded. INTEGRITY '
    'HOLD checked: no new reference is from the flagged group. Added: 2022 double-blind knee OA RCT + 2024 OA SR to '
    'arthritis (replacing the inferred note), 2017 processed-seed OA RCT as no effect; NEW acne (2020 hydrogel RCT), '
    'sinusitis (2021 nasal-drop RCT), kidney-support (2019 triple-blind kidney-stone RCT), insomnia and stress (2023 '
    'BlaQmax RCTs, same proprietary product) pairs; via Europe PMC: NEW pms pair (2025 double-blind placebo RCT) and a 2025 '
    'triple-blind episiotomy emulgel RCT to wounds and pain (replacing the inferred notes); severe topical-oil dermatitis WARNING (2018 JAMA Dermatology series), '
    'rhabdomyolysis/AKI caution (2024 case), liver/kidney-marker MA and a thrombocytopenia case (with evening primrose oil) '
    'as info notes. Not added: 2023 H. pylori RCT (appetite outcome only), 2015 honey-based dyspepsia formula '
    '(combination), 2023 navel-oil urinary incontinence RCT (topical abdominal route; stress incontinence unchanged), 2022 '
    'depression adjunct trial (randomisation not stated), 2019 mucositis rinse and 2026 gingivitis mouthwash (active '
    'comparators), thymoquinone gel (compound), male infertility (multi-herb SR only; the RCT was not retrieved), '
    'olive + black seed oil episiotomy trial (combination), rheumatoid arthritis biomarker trials (no clinical outcome), '
    'contact-dermatitis letters with no abstract, thymoquinone CYP and cyclosporine studies (lab and rodent).')

# ================================================================== holy basil
PLAN['ocimum_tenuiflorum'] = [
    ('newpair', 'oral-health', ['REF-5534', 'REF-5535'],
     'A 4% tulsi toothpaste reduced gingivitis and plaque more than a placebo toothpaste in teenagers over 3 weeks '
     '(randomized triple-blind trial), and a tulsi mouthwash reduced gum bleeding and plaque compared with saline, about as '
     'well as chlorhexidine (randomized triple-blind trial)'),
]
NOTES['ocimum_tenuiflorum'] = (
    'Searched PubMed (Ocimum tenuiflorum / Ocimum sanctum / holy basil / tulsi tiab: 61 HT, 13 SR, 173 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (18) and OpenAlex. Stress (8) and blood sugar (8) were not padded (2012 OciBest stress RCT not '
    'added). Added: NEW oral-health pair (2020 placebo-dentifrice and 2014 saline-controlled mouthwash triple-blind RCTs). '
    'Not added: 2017 overweight open-label trial (within-group changes; only HDL differed), halitosis and other mouthwash '
    'trials vs chlorhexidine only (active comparators), turmeric/aloe/calendula combinations, Ayurvedic multi-herb COVID '
    'regimens, genotoxicity and toxicology studies of Holixer and OciBest (lab and animal; no concern found), '
    'antiepileptic interaction studies (rodents).')

# ================================================================== evening primrose
PLAN['oenothera_biennis'] = [
    ('newpair', 'fatigue', ['REF-5536'],
     'Evening primrose oil reduced fatigue and pain and improved vitality and quality of life compared with placebo in '
     'people with multiple sclerosis over 3 months (randomized double-blind trial)'),
]
POST['oenothera_biennis'] = [
    ('cinew', {'note': 'Epilepsy: the old warning that evening primrose oil can trigger seizures traces back to two reports from '
                       'the early 1980s; a 2007 review re-examined them, judged the link spurious, and recommended removing '
                       'epilepsy as a contraindication (review).',
               'severity': 'info', 'reference_ids': ['REF-5537']}),
    ('cinew', {'note': 'Lungs: a woman with acid reflux who had used evening primrose oil for a long time was diagnosed with '
                       'lipoid pneumonia (oil droplets inhaled into the lungs); she improved after stopping it (case '
                       'report).',
               'severity': 'caution', 'reference_ids': ['REF-5538']}),
    ('cinew', {'note': THROMBO, 'severity': 'info', 'reference_ids': ['REF-5533']}),
]
NOTES['oenothera_biennis'] = (
    'Searched PubMed (Oenothera biennis / evening primrose tiab: 230 HT, 50 SR, 161 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (15) and OpenAlex. Pain (9), hot flushes (9) and menopause (8) were not padded (2025 diabetic '
    'neuropathy RCT and 2020 post-appendectomy pain RCT not added). Added: NEW fatigue pair (2018 double-blind placebo RCT '
    'in multiple sclerosis); 2007 epilepsy-safety review as an info note; lipoid pneumonia case caution; thrombocytopenia '
    'case (with black seed oil) as an info note. NOT PAIRED (inv. 12d): cervical ripening / labour induction (2023 MA, 2021 '
    'MA REF-1462 and RCTs) conflicts with the record\'s caution against medicinal use in pregnancy, so no pregnancy-support '
    'pair was created. Not added: PCOS, isotretinoin side-effect and acne trials (no vocab condition or surrogate skin '
    'measures), Hot-nature diet with hemp seed + EPO MS trials (combination), fish oil + EPO combinations, misoprostol + EPO '
    'trials, 1993 cholestasis case (EPO used as a treatment, not a cause), BMJ Clinical Evidence summaries (superseded).')

# ================================================================== olive
PLAN['olea_europaea'] = [
    ('newpair', 'high-blood-pressure', ['REF-5539', 'REF-2537'],
     'Olive leaf extract lowered systolic blood pressure compared with control in a 2022 meta-analysis of 12 randomized '
     'trials (by about 5 mmHg systolic and 2.5 mmHg diastolic in people with hypertension), and 500 mg a day lowered systolic '
     'pressure vs placebo or no treatment in a 2021 meta-analysis; in a 2026 double-blind randomized trial a standardised '
     'olive extract lowered systolic pressure by about 8 mmHg, but not significantly more than placebo'),
    ('nulladd', 'high-blood-pressure', ['REF-5544']),
    ('nulladd', 'blood-sugar', ['REF-5540']),
    ('note', 'blood-sugar',
     'Olive leaf extract lowered HbA1c in one randomized trial and improved insulin sensitivity in another; meta-analyses of '
     'olive leaf extract and of extra virgin olive oil found no significant effect on blood sugar, and a 2025 pilot '
     'randomized trial in type 2 diabetes found no HbA1c difference vs placebo'),
]
POST['olea_europaea'] = [
    ('cinew', {'note': 'Skin: in patch tests in 100 people with eczema, olive oil was a weak skin irritant, more so under '
                       'covering dressings, and only one reaction looked allergic; the authors judged it less suitable for '
                       'eczema of the lower legs linked to poor circulation.',
               'severity': 'info', 'reference_ids': ['REF-5541']}),
]
NOTES['olea_europaea'] = (
    'Searched PubMed (Olea europaea / olive leaf / olive leaves / oleuropein tiab, olive oil ti: 748 HT, 108 SR, 814 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (108) and OpenAlex. Huge plant: screened SRs, conditions without a pair and '
    'safety; olive oil trials mostly compare it with other fats (active comparators). Added: NEW high-blood-pressure pair '
    '(2022 olive leaf MA of 12 RCTs + the 2021 MA REF-2537 already cited for the antihypertensive interaction); 2025 '
    'ESOLED pilot RCT as a no-effect study on blood-sugar; 2026 double-blind olive extract RCT (systolic fell 8.3 vs 7.3 '
    'mmHg on placebo, not significant; found via Europe PMC) as a no-effect study on high-blood-pressure; 1997 patch-test study as an info note. Not added: 2025 olive '
    'leaf BP MA 40325976 (pre-post analysis only), olive oil lipid MAs and HDL-polyphenol MA (comparisons with other oils; '
    'high-cholesterol left without a pair - the 2022 leaf MA lowered triglycerides overall but total and LDL cholesterol '
    'only in subgroups), cohort mortality MAs (observational), 2023 swallowed dry-leaf bowel perforation (accident), 2016 '
    'olive leaf toxicity letter and contact dermatitis letters (no abstract), African wild olive (subspecies) PK study, '
    'olive pollen allergy (not related to use), combination radiodermatitis creams.')


def text_edits():
    """Add the accepted synonym Ocimum sanctum L. (most holy basil trials use it; the species audit reads synonyms)."""
    p = 'plants/ocimum_tenuiflorum.yaml'
    t = open(p, encoding='utf-8', newline='').read()
    old = 'wp_post_id: 154\nparts_used:'
    assert old in t
    open(p, 'w', encoding='utf-8', newline='').write(t.replace(old, 'wp_post_id: 154\nsynonyms:\n- Ocimum sanctum L.\nparts_used:', 1))


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r22_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        text_edits()
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
