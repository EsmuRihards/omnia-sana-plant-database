"""Research-deepening batch 28 (rhodiola-rosea, rhododendron-tomentosum, ribes-nigrum, rosa-canina, rosa-rugosa).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5627.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 28'

SPEC = [
    # rhodiola
    ('REF-5627', '26613955', 'rhodiolacyp2c9', 'rct'),
    ('REF-5628', '41544018', 'rhodiolasupplementquality', 'preclinical'),
    # marsh Labrador tea
    ('REF-5629', '21186373', 'labradorteacyp3a4', 'preclinical'),
    # blackcurrant
    ('REF-5630', '34445035', 'blackcurrantmusclerecovery', 'rct'),
    ('REF-5631', '25153307', 'blackcurrantnectarmuscledamage', 'rct'),
    ('REF-5632', '32470924', 'blackcurranthalfmarathon', 'rct'),
    ('REF-5633', '37893207', 'blackcurrantmenopauselipids', 'rct'),
    # dog rose
    ('REF-5634', '25834460', 'rosehipvisceralfat', 'rct'),
    ('REF-5635', '22166897', 'rosehipobesecardiometabolic', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== rhodiola
PLAN['rhodiola_rosea'] = []
POST['rhodiola_rosea'] = [
    ('cinew', {'note': 'Medicines: in a randomized crossover study in 13 healthy volunteers, rhodiola reduced the activity of '
                       'the liver enzyme CYP2C9 by about 21% (losartan probe), with no effect on CYP1A2, 2C19, 2D6 or 3A4; '
                       'the authors note this could matter for CYP2C9-metabolised drugs with a narrow safety margin '
                       '(pharmacokinetic study).',
               'severity': 'caution', 'reference_ids': ['REF-5627']}),
    ('cinew', {'note': 'Product quality: in a 2026 analysis of US rhodiola supplements, rosavin and salidroside content ranged '
                       'from almost none to about 3% and often differed from the label, one product appeared to contain '
                       'added synthetic salidroside, and all capsule products had trace arsenic, cobalt and lead (two at '
                       'notably higher levels) (product analysis).',
               'severity': 'info', 'reference_ids': ['REF-5628']}),
]
NOTES['rhodiola_rosea'] = (
    'Searched PubMed (Rhodiola rosea / roseroot / golden root / Arctic root / SHR-5 / WS 1375 tiab; bare "rhodiola" was '
    'not searched because Chinese rhodiola products are often R. crenulata or R. wallichiana: 134 HT, 27 SR, 139 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (29) and OpenAlex; stress/anxiety RCTs were also searched directly. Fatigue '
    '(7), cognitive-function (6) and depression (5) were not padded: the 2009 SHR-5 stress-fatigue RCT and 2000 exam-'
    'stress RCT fit fatigue, and the 2025 milder-depression meta-analysis rests on a single rhodiola placebo RCT. '
    'Added: 2016 human CYP cocktail crossover (CYP2C9 inhibition) as a medicines caution; 2026 US supplement quality '
    'analysis as an info note. GAP: stress/anxiety - the 2015 Vitano trial (held as cropley2015rhodiola) randomized 80 '
    'mildly anxious adults to rhodiola or no treatment (not placebo), outcomes were self-reported and the authors state '
    'they cannot determine a causal relationship, so no pair; the burnout, life-stress (WS 1375), GAD and chronic-fatigue '
    'studies were open-label or single-arm. Not added: sport-performance RCTs and the 2026 Rhodiola-species meta-analysis '
    '(antioxidant only, no ergogenic effect; no vocabulary condition), caffeine + rhodiola, rhodiola + saffron, Cimicifuga '
    '+ rhodiola, ADAPT-232 and other combinations, Chinese "rhodiola" injections and capsules (species not R. rosea or not '
    'stated), R. crenulata trials (other species), healthy-volunteer reaction-time study (not padded), preprints.')

# ================================================================== marsh Labrador tea
PLAN['rhododendron_tomentosum'] = []
POST['rhododendron_tomentosum'] = [
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'In lab tests of 17 Cree medicinal plants, an ethanol extract of marsh Labrador tea was a weak '
                             'mechanism-based inactivator of the drug-metabolising enzyme CYP3A4 (lab study); no human data.',
                'reference_ids': ['REF-5629']}),
]
NOTES['rhododendron_tomentosum'] = (
    'Searched PubMed (Rhododendron tomentosum / Ledum palustre / marsh Labrador tea / marsh tea tiab, "Labrador tea" in '
    'titles; bog Labrador tea, R. groenlandicum, is a different species: 4 HT, 0 SR, 10 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (2) and OpenAlex. Added: 2011 CYP3A4 inactivation lab study as a DRAFT cyp3a4-substrates '
    'interaction (insufficient; needs owner approval). Not added: homeopathic Ledum trials and the Arnica + Ledum bruising '
    'study (homeopathy / combination), 1996 homeopathic after-bite gel trial (homeopathy), the 2014 Cree tea CYP3A4 study (its conclusion names '
    'R. groenlandicum and juniper, not marsh Labrador tea), Ledum palustre var. diversipilosum dermatitis study (animal), '
    'methylmercury rat study. Settled for human efficacy evidence.')

# ================================================================== blackcurrant
PLAN['ribes_nigrum'] = [
    ('newpair', 'muscle-soreness', ['REF-5630'],
     'In a 2021 randomized double-blind trial in 27 untrained adults, New Zealand blackcurrant extract taken before and '
     'after strenuous arm exercise reduced muscle soreness at 24 and 48 hours and sped recovery of strength compared with '
     'placebo; a 2016 nectar trial and a 2020 half-marathon trial found no difference in soreness'),
    ('nulladd', 'muscle-soreness', ['REF-5631', 'REF-5632']),
    ('add', 'cardiovascular-support', ['REF-5633']),
    ('note', 'cardiovascular-support',
     'Blackcurrant extract lowered cholesterol in a small pilot study in women and protected blood vessels in animal '
     'studies; in a 2023 six-month randomized placebo-controlled pilot trial in 38 women in the menopause transition, '
     'blackcurrant anthocyanins lowered triglycerides and inflammatory markers dose-dependently; cardiovascular uses '
     'reviewed (review)'),
]
NOTES['ribes_nigrum'] = (
    'Searched PubMed (Ribes nigrum / blackcurrant(s) / black currant(s) tiab: 206 HT (listing capped at 200), 20 SR, 79 '
    'SAFE hits), Europe PMC, ClinicalTrials.gov (57) and OpenAlex. Most trials were sport-performance studies of New '
    'Zealand blackcurrant extract (no vocabulary condition). Added: NEW muscle-soreness pair (2021 RCT) with two null RCTs '
    'recorded alongside (2016 nectar, 2020 half-marathon); 2023 menopause-transition RCT (triglycerides, inflammation) to '
    'cardiovascular-support. GAPS: high blood pressure - a 2023 meta-analysis of four blackcurrant RCTs found no effect on '
    'systolic or diastolic pressure (a 2020 7-day crossover in 14 older adults was positive), so no pair; eczema - a 2010 '
    'RCT of blackcurrant seed oil (vs olive oil) given to mothers from early pregnancy and then to infants lowered atopic '
    'dermatitis at 12 but not 24 months, but the record cautions that maternal trials do not mean use in pregnancy is '
    'recommended (inv. 12d), so no pair; glaucoma - a 2012 two-year RCT slowed visual-field loss, but there is no glaucoma '
    'condition (eye-strain is not a match). Not added: acute cognition and mood studies in healthy young adults, exercise '
    'GI-symptom trial, osteoporosis pilot (no vocabulary condition), asthma feasibility study (5 people), Chinese '
    'blackcurrant-oil capsule study (observational), postprandial glucose studies (blood-sugar not padded), mixed berry, '
    'polyphenol-juice and anthocyanin-blend trials (combinations).')

# ================================================================== dog rose
PLAN['rosa_canina'] = [
    ('add', 'metabolic-support', ['REF-5634']),
    ('note', 'metabolic-support',
     'Rose hip flesh and extracts reduced fat build-up and improved blood sugar in animal studies (preclinical); seed '
     'lipid-lowering effects reviewed (systematic review); in a 2015 randomized double-blind trial in 32 pre-obese adults, '
     'rose hip extract for 12 weeks reduced abdominal visceral fat, body weight and BMI more than placebo'),
    ('newpair', 'high-cholesterol', ['REF-5635'],
     'In a 2012 randomized double-blind crossover trial in 31 obese adults, a rose hip powder drink for 6 weeks lowered '
     'total cholesterol by 4.9% and LDL cholesterol by 6% compared with a control drink; a 2023 systematic review found '
     'mixed effects on blood lipids across trials'),
    ('newpair', 'high-blood-pressure', ['REF-5635'],
     'In the same 2012 randomized double-blind crossover trial in obese adults, the rose hip drink lowered systolic blood '
     'pressure by 3.4% compared with a control drink; diastolic pressure did not change'),
]
NOTES['rosa_canina'] = (
    'Searched PubMed (Rosa canina / dog rose / rosehip(s) / rose hip(s) / LitoZin / Hyben Vital tiab; species confirmed '
    'in the full text for the two new trials: 58 HT, 15 SR, 61 SAFE hits), Europe PMC, ClinicalTrials.gov (5) and '
    'OpenAlex. Arthritis (10) and inflammation (8) were not padded (2003 OA RCT, gait study and Litozin re-analysis). '
    'Added: 2015 visceral-fat RCT to metabolic-support (previously preclinical and reviews only); NEW high-cholesterol and '
    'high-blood-pressure pairs (2012 Lund crossover; rose hips from Chile, Rosa canina). Not added: 2023 rosehip lipid and '
    'glucose systematic review (mixed results; mentioned in the note), 2026 orthostatic-intolerance RCT in type 2 diabetes '
    '(no vocabulary condition), rosehip seed oil trials (2020 hand-lesion RCT was open-label and favoured the control; '
    '2016 radiotherapy epithelitis study not randomized; species not stated), Rosa mosqueta oil dermatitis (other species), '
    'false-positive digoxin assay letter (no abstract; hibiscus + rose hip tea), 2021 liver-injury case (multi-herb '
    'collection), Lady Prelox and cartilage + rosehip products (combinations), standardized extract toxicity study '
    '(species not stated in the abstract).')

# ================================================================== Japanese rose
PLAN['rosa_rugosa'] = []
NOTES['rosa_rugosa'] = (
    'Searched PubMed (Rosa rugosa / rugosa rose tiab; "Japanese rose" is ambiguous: 2 HT, 1 SR, 15 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (3, all multi-herb sachets or teas) and OpenAlex. Nothing new: a 2025 physiological study of '
    'inhaled volatile extracts in healthy people (surrogate), rose-pollen allergy cases (species not stated), lab and '
    'animal studies. Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r28_changes.tsv')
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
