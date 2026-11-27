"""Research-deepening batch 33 (syzygium-aromaticum, tanacetum-parthenium, tanacetum-vulgare, taraxacum-officinale,
theobroma-cacao). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5670.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 33'

SPEC = [
    # cacao
    ('REF-5670', '35253583', 'cocoat2dcardiometabolicma', 'meta-analysis'),
    ('REF-5671', '41858752', 'cocoametabolicsyndromema', 'meta-analysis'),
    ('REF-5672', '42662243', 'chocolatemigrainetrigger', 'meta-analysis'),
    ('REF-5673', '38883222', 'cacaoallergycase', 'clinical'),
    ('REF-5674', '38763644', 'chocolateheavymetals', 'preclinical'),
    ('REF-5675', '39796308', 'chocolatecadmiumserbia', 'preclinical'),
    # feverfew
    ('REF-5676', '34434419', 'feverfewbleeding', 'clinical'),
    ('REF-5677', '18021604', 'feverfewmoisturizerdermatitis', 'clinical'),
    # dandelion
    ('REF-5678', '42398668', 'dandelionrootdiuresis', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== clove
PLAN['syzygium_aromaticum'] = []
NOTES['syzygium_aromaticum'] = (
    'Searched PubMed (Syzygium aromaticum / Eugenia caryophyllata / clove oil, bud, extract or gel tiab, "clove(s)" in '
    'titles; eugenol alone was not searched because it is mostly dental-cement literature; many hits were CLOVES '
    'syndrome or garlic cloves: 71 HT, 18 SR, 328 SAFE hits), Europe PMC, ClinicalTrials.gov (66) and OpenAlex. Oral-'
    'health and pain (5) were not changed. Not added: topical clove oil before dental injections compared with EMLA, '
    'lignocaine or benzocaine (active comparators), 2017 chronic pruritus trial (between-group difference not '
    'significant), 2025 clove + lavender aromatherapy for post-spinal headache (not significant vs control), 2016 '
    '"clove-based herbal" mouthwash for radiation mucositis (14 patients, composition not stated), a comparative clove '
    'mouthwash trial for ventilator pneumonia (not assessed as placebo-controlled), 2019 clove polyphenol glucose study (open-'
    'label), binge-drinking inflammatory markers (surrogate), 2025 dental-pain systematic review (qualitative, many '
    'agents), hyperhidrosis study (no vocabulary condition), fragrance safety assessments.')

# ================================================================== feverfew
PLAN['tanacetum_parthenium'] = []
POST['tanacetum_parthenium'] = [
    ('cinew', {'note': 'Bleeding: a 36-year-old woman who had taken feverfew 800 mg three times daily for 9 months for '
                       'migraine developed vaginal bleeding, longer periods and abnormal clotting tests; causality was '
                       'rated probable (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5676']}),
    ('dciadd', 'anticoagulants-antiplatelets', ['REF-5676']),
    ('ciadd', 'it can cause allergic reactions in people sensitive to ragweed and related plants', ['REF-5677']),
]
NOTES['tanacetum_parthenium'] = (
    'Searched PubMed (Tanacetum parthenium / feverfew / Chrysanthemum parthenium / MIG-99 tiab: 44 HT, 13 SR, 106 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (3) and OpenAlex. Migraine (9) and headache (8) were not padded. Added: 2021 '
    'bleeding / abnormal-coagulation case (Naranjo probable) as a caution and to the approved anticoagulants '
    'interaction; 2007 moisturizer contact-dermatitis cases to the Asteraceae allergy note. Not added: feverfew + '
    'willow and other combinations, IMOD and Septimeb (multi-herb products), pollen-allergen proteomics, 2019 '
    'occupational dermatitis letter (no abstract), essential-oil toxicity in rodents.')

# ================================================================== tansy
PLAN['tanacetum_vulgare'] = []
NOTES['tanacetum_vulgare'] = (
    'Searched PubMed (Tanacetum vulgare / common tansy tiab, "tansy" in titles; tansy ragwort, Jacobaea vulgaris, is a '
    'different and pyrrolizidine-toxic plant: 5 HT, 0 SR, 37 SAFE hits), Europe PMC, ClinicalTrials.gov (0) and '
    'OpenAlex. Nothing new: tansy ragwort livestock poisonings (other species), older Compositae and plant contact-'
    'dermatitis case reports, rodent toxicity and insecticidal studies. Settled.')

# ================================================================== dandelion
PLAN['taraxacum_officinale'] = [
    ('nulladd', 'urinary-support', ['REF-5678']),
    ('note', 'urinary-support',
     'Traditional diuretic for kidney gravel and stones (Grieve, A Modern Herbal; Herbal Reality); a leaf extract raised '
     'urine frequency in a small pilot study, but in a 2026 open-label crossover in 14 active young adults, about 2 g of '
     'dandelion root powder with 1 L of water did not increase urine output more than water alone'),
]
NOTES['taraxacum_officinale'] = (
    'Searched PubMed (Taraxacum officinale / dandelion / Taraxaci radix or herba tiab: 44 HT, 6 SR, 183 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (7) and OpenAlex. Added: 2026 dandelion-root diuresis crossover as a NULL result on '
    'urinary-support. Not added: dandelion + borneol after jaw surgery, D-mannose-based and other multi-ingredient '
    'supplements, BNO 1030, ayurvedic and plant-based liver nutraceuticals (combinations), breast-milk microbiome '
    'mastitis study (surrogate), 2017 dandelion allergen paper (no abstract), allergen-sensitization surveys (pollen), '
    'Taraxacum kok-saghyz rubber studies (other species), lab and animal studies.')

# ================================================================== cacao
PLAN['theobroma_cacao'] = [
    ('newpair', 'blood-sugar', ['REF-5670', 'REF-5671'],
     'In a 2022 meta-analysis of 12 randomized trials in type 2 diabetes, long-term cocoa products lowered blood glucose '
     '(by about 9 mg/dL); a 2026 meta-analysis of 13 RCTs in metabolic syndrome and related conditions also suggested '
     'lower glycaemic measures'),
]
POST['theobroma_cacao'] = [
    ('cinew', {'note': 'Allergy: a person with tree-nut allergy had anaphylaxis after eating a piece of chocolate; skin '
                       'tests showed cocoa sensitization with cross-reactivity to tree nuts (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5673']}),
    ('cinew', {'note': 'Migraine: about 14% of people with migraine report chocolate as a trigger (meta-analysis of '
                       'self-report studies); effects vary between individuals, so a headache diary is more useful than '
                       'routine avoidance.',
               'severity': 'info', 'reference_ids': ['REF-5672']}),
    ('cinew', {'note': 'Heavy metals: in 155 chocolates on the US market, cadmium and lead were higher in dark chocolate '
                       '(50% cacao or more), and highest in cacao from Central and South America; in 155 Serbian chocolates, '
                       'weekly cadmium intake stayed below the tolerable limit but reached about 60% of it for children '
                       '(product analyses).',
               'severity': 'info', 'reference_ids': ['REF-5674', 'REF-5675']}),
]
NOTES['theobroma_cacao'] = (
    'Searched PubMed (Theobroma cacao / cocoa flavanol(s) / cocoa extract or powder / cacao tiab, "cocoa" and '
    '"chocolate" in titles: 751 HT (listing capped at 200), 120 SR, 433 SAFE hits), Europe PMC, ClinicalTrials.gov '
    '(122) and OpenAlex. High-blood-pressure (8), cardiovascular-support, cognitive-function and memory (7) were not '
    'padded. Added: NEW blood-sugar pair (2022 T2D and 2026 metabolic-syndrome meta-analyses); allergy caution; migraine-'
    'trigger and heavy-metal info notes. GAPS: high-cholesterol - the 2022 T2D meta-analysis found lower LDL, but a 2025 '
    'dose-response meta-analysis in T2D found only triglycerides changed (low certainty) and the 2026 metabolic-syndrome '
    'meta-analysis found cholesterol lower only in subgroups, so no pair; depression/anxiety - a 2022 meta-analysis of 9 '
    'studies found lower depressive and anxiety scores, but 5 were single-dose and only 2 lasted over a week, mostly in '
    'healthy people (owner flag), so no pair. Not added: observational chocolate-and-disease cohort meta-analyses, '
    'oxidative-stress, CRP, flow-mediated dilation and arterial-stiffness meta-analyses (surrogates), sport performance, '
    'chocolate milk recovery, Mexican-ancestral-foods meta-analysis (combinations), COCOA birth-cohort studies (acronym, '
    'not cocoa).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r33_changes.tsv')
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
