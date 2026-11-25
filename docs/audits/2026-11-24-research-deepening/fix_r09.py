"""Research-deepening batch 9 (cnicus-benedictus, coffea-arabica, cordyceps-militaris, coriandrum-sativum,
crataegus-laevigata). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5270.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 9'

SPEC = [
    # coffee
    ('REF-5270', '29167102', 'coffeeumbrellareview', 'systematic-review'),
    ('REF-5271', '26339067', 'coffeedepression', 'meta-analysis'),
    ('REF-5272', '37523229', 'coffeeteacognitive', 'meta-analysis'),
    ('REF-5273', '37710316', 'greencoffeeweight', 'meta-analysis'),
    ('REF-5274', '32550217', 'greencoffeecardiometabolic', 'meta-analysis'),
    ('REF-5275', '26899133', 'coffeecaffeinesleep', 'systematic-review'),
    ('REF-5276', '18341376', 'coffeelevothyroxine', 'clinical'),
    ('REF-5277', '10976659', 'caffeinedruginteractions', 'narrative-review'),
    # coriander
    ('REF-5278', '26889386', 'coriandermigraine', 'rct'),
    ('REF-5279', '41492428', 'corianderseedt2dm', 'clinical'),
    ('REF-5280', '30093499', 'corianderbeeranaphylaxis', 'clinical'),
    ('REF-5281', '40841974', 'corianderleadpoisoning', 'clinical'),
    # hawthorn
    ('REF-5282', '40732315', 'hawthornbpmeta', 'meta-analysis'),
    ('REF-5283', '11807965', 'hawthornbppilot', 'rct'),
    ('REF-5284', '12833999', 'crataegusberrieschf', 'rct'),
    ('REF-5285', '16752934', 'crataegusadverseevents', 'systematic-review'),
    ('REF-5286', '29672935', 'hawthornecg', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== coffee
PLAN['coffea_arabica'] = [
    ('newpair', 'depression', ['REF-5271'],
     'Drinking coffee was linked to a lower risk of depression in a meta-analysis of observational studies (an association, '
     'not proof that coffee prevents it)'),
    ('add', 'cognitive-function', ['REF-5272']),
    ('note', 'cognitive-function', 'Caffeine, coffee\'s signature compound, improves alertness (MedlinePlus; compound evidence); '
     'moderate coffee drinking (about 2.5 cups a day) was linked to the lowest risk of Alzheimer\'s disease in a dose-response '
     'meta-analysis of observational studies'),
    ('add', 'metabolic-support', ['REF-5273', 'REF-5274']),
    ('note', 'metabolic-support', 'Green coffee bean extract (about 500 mg chlorogenic acid a day) lowered body weight, and green '
     'coffee lowered fasting blood sugar, insulin and triglycerides, in meta-analyses of randomized trials; coffee drinking has '
     'been linked to lower type 2 diabetes risk (review); coffee-leaf extracts lowered blood glucose in lab studies'),
]
POST['coffea_arabica'] = [
    ('ciadd', 'Caffeine is the primary psychoactive component', ['REF-5275']),
    ('cinew', {'note': 'An umbrella review of meta-analyses found coffee generally safe within usual intakes, with the largest risk '
                       'reductions at 3 to 4 cups a day; this does not extend to pregnancy, and women at higher risk of fracture '
                       'may need to limit it.',
               'severity': 'info', 'reference_ids': ['REF-5270']}),
    ('dcinew', {'drug_class': 'thyroid-medicines', 'severity': 'caution',
                'mechanism': 'Swallowing levothyroxine with coffee or espresso cut its absorption by roughly a quarter to a third '
                             'in patients and volunteers; drinking the coffee 60 minutes after the tablet avoided the effect '
                             '(clinical study with case series).',
                'reference_ids': ['REF-5276']}),
    ('dcinew', {'drug_class': 'antibiotics', 'severity': 'caution',
                'mechanism': 'Some quinolone antibiotics, such as enoxacin, strongly block CYP1A2, the enzyme that clears caffeine, '
                             'so caffeine from coffee can build up and cause side effects (review).',
                'reference_ids': ['REF-5277']}),
    ('dcinew', {'drug_class': 'antidepressants-serotonergic', 'severity': 'caution',
                'mechanism': 'The antidepressant fluvoxamine strongly blocks CYP1A2, the enzyme that clears caffeine, so caffeine '
                             'from coffee can build up (review).',
                'reference_ids': ['REF-5277']}),
]
NOTES['coffea_arabica'] = (
    'Searched PubMed (Coffea arabica / C. canephora / green coffee tiab, coffee ti: 1,062 HT, 448 SR, 957 SAFE hits; SR/MA and '
    'safety read in depth), Europe PMC, ClinicalTrials.gov (109) and OpenAlex. Added: NEW depression pair (2016 observational '
    'MA, lower risk); 2024 dose-response MA (lower Alzheimer\'s and cognitive-disorder risk) to cognitive-function; green '
    'coffee weight MA 2023 and cardiometabolic MA 2020 to metabolic-support; caffeine-sleep SR 2017 to the caution; BMJ 2017 '
    'umbrella review as a new info note; three DRAFT interactions (levothyroxine absorption study 2008; CYP1A2 inhibitors '
    'enoxacin and fluvoxamine from a 2000 caffeine-interaction review), need owner sign-off. NOT ADDED: high-blood-pressure '
    '(green coffee extract BP MA 2024 and an observational hypertension MA) because the record\'s own caution says excess '
    'caffeine raises blood pressure and people with hypertension should limit it (inv. 12d); gout, gallstone, fracture, '
    'kidney-stone and cancer-risk MAs (no vocab condition or risk-only); ergogenic MAs; Mendelian-randomisation studies.')

# ================================================================== coriander
PLAN['coriandrum_sativum'] = [
    ('newpair', 'migraine', ['REF-5278'],
     'A coriander fruit syrup reduced the frequency, duration and severity of migraine attacks more than placebo in a '
     'triple-blind randomized trial'),
]
POST['coriandrum_sativum'] = [
    ('ciadd', '• Food use is generally safe', ['REF-5279', 'REF-5280']),
    ('cinew', {'note': 'Contamination: a woman developed lead poisoning with anaemia likely linked to imported coriander powder; '
                       'coriander powder from the same source contained very high lead levels, suggesting adulteration (case '
                       'report). Buy spices from reputable sources.',
               'severity': 'caution', 'reference_ids': ['REF-5281']}),
]
NOTES['coriandrum_sativum'] = (
    'Searched PubMed (Coriandrum sativum / coriander / cilantro tiab), Europe PMC, ClinicalTrials.gov (2) and OpenAlex. Added: '
    'NEW migraine pair (2016 triple-blind placebo RCT of coriander fruit syrup); 2025 placebo-controlled trial of coriander '
    'seed powder in type 2 diabetes (randomisation not stated, so not used for a new blood-sugar pair) and a coriander-beer '
    'anaphylaxis case to the existing caution; lead-poisoning case from adulterated imported coriander powder (new caution). '
    'Considered, not added: sensitive-skin seed-oil study (abstract gives no comparison with placebo), diaper dermatitis '
    '(non-randomised), garlic + coriander and other combinations, periodontitis mouthwash vs chlorhexidine, insulin '
    'autoimmune syndrome case (attributed to omeprazole).')

# ================================================================== hawthorn
PLAN['crataegus_laevigata'] = [
    ('add', 'high-blood-pressure', ['REF-5282']),
    ('nulladd', 'high-blood-pressure', ['REF-5283']),
    ('note', 'high-blood-pressure', 'Hawthorn (C. laevigata) extract lowered diastolic blood pressure in a randomized trial in '
     'people with type 2 diabetes taking blood-pressure medicines; a 2025 meta-analysis of placebo-controlled trials of hawthorn '
     '(Crataegus spp.) found a clinically significant fall in systolic pressure, though a small pilot trial found no clear '
     'effect'),
    ('add', 'cardiovascular-support', ['REF-5284']),
]
POST['crataegus_laevigata'] = [
    ('ciadd', 'Generally safe and well tolerated.', ['REF-5285', 'REF-5286']),
]
NOTES['crataegus_laevigata'] = (
    'Searched PubMed (Crataegus laevigata / C. oxyacantha / midland hawthorn tiab; hawthorn, Crataegus, WS 1442 ti), Europe PMC, '
    'ClinicalTrials.gov (38) and OpenAlex. Crataegus spp. extracts follow the existing attribution (EU monograph covers C. '
    'laevigata). Added: 2025 MA of placebo RCTs (SBP -6.7 mmHg) to high-blood-pressure, with the 2002 pilot RCT (no clear '
    'difference) as no-effect; 2003 fresh-berry extract RCT in NYHA II heart failure (C. oxyacantha) to cardiovascular-support; '
    'the 2006 adverse-event SR (well tolerated, no reported interactions) and a 2018 placebo crossover ECG RCT (no QT change) '
    'to the safety note. Dead end: C. laevigata + statin RCT 2011 (LDL trend, no significant difference from placebo; no '
    'cholesterol pair exists). Not added: Pittler 2003 MA (superseded by the Cochrane review REF-2442), secondary HERB CHF and '
    'SPICE reports, C. pinnatifida fruit-drink trials (different species), Crataegus extract mixtures and Scutellaria / '
    'magnesium / chromium combinations, a homeopathic Crataegus series, the platelet letter (no abstract), C. mexicana root '
    'intoxication (different species).')

# ================================================================== cordyceps
PLAN['cordyceps_militaris'] = []
NOTES['cordyceps_militaris'] = (
    'Searched PubMed (Cordyceps militaris tiab, cordycepin ti), Europe PMC, ClinicalTrials.gov (10) and OpenAlex. No new pair: '
    'the duloxetine add-on insomnia RCT (2021) found sleep scores fell MORE on placebo (dead end); the CKD trial (2019, '
    'placebo-controlled, lower proteinuria and creatinine) does not state randomisation, so it does not meet the new-pair bar '
    '(recorded as a gap); exercise, oxygen-uptake and runner anaemia trials have no vocab condition; Ophiocordyceps sinensis '
    'and Cordyceps spp. reviews are other species.')

# ================================================================== blessed thistle
PLAN['cnicus_benedictus'] = []
NOTES['cnicus_benedictus'] = (
    'Searched PubMed (Cnicus benedictus / Centaurea benedicta / blessed / holy thistle tiab: 0 HT, 0 SR, 6 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (0) and OpenAlex. No human study of blessed thistle alone exists (Gastritol is a multi-herb '
    'product). Settled; the galactagogue use remains traditional only.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r09_changes.tsv')
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
