"""Deep audit of batch 18 (trifolium-repens .. verbena-officinalis): 2nd-pass strict-match + deep checks. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3817..REF-3849 (Grieve x6 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3817', '36837450', 'fenugreekhyperglycemia', 'meta-analysis'),
    ('REF-3818', '32087319', 'fenugreeklipidsrct', 'meta-analysis'),
    ('REF-3819', '32385866', 'fenugreeklipidprofile', 'meta-analysis'),
    ('REF-3820', '36763260', 'fenugreekbp', 'meta-analysis'),
    ('REF-3821', '33025616', 'fenugreekvasomotor', 'rct'),
    ('REF-3822', '34587883', 'nettlet2dmetabolic', 'meta-analysis'),
    ('REF-3823', '16635963', 'nettlebphcrossover', 'rct'),
    ('REF-3824', '32981268', 'nettlebphroot2020', 'rct'),
    ('REF-3825', '15045190', 'nettlebazotonuno', 'rct'),
    ('REF-3826', '31126551', 'nettlehotflashes', 'rct'),
    ('REF-3827', '10911825', 'nettlestingthumb', 'rct'),
    ('REF-3828', '18514907', 'nettlestingknee', 'rct'),
    ('REF-3829', '24402038', 'cranberryms', 'rct'),
    ('REF-3830', '20804630', 'cranberrymenluts', 'rct'),
    ('REF-3831', '30340813', 'cranberrygingivitis', 'rct'),
    ('REF-3832', '32945735', 'cranberryoab', 'rct'),
    ('REF-3833', '25923485', 'bilberryeyefatigue', 'rct'),
    ('REF-3834', '32106548', 'bilberryciliary', 'rct'),
    ('REF-3835', '22961907', 'bilberryinflammation', 'rct'),
    ('REF-3836', '40751398', 'bilberrycardiometabolic', 'meta-analysis'),
    ('REF-3837', '40965071', 'valeriandysmenorrheama', 'meta-analysis'),
    ('REF-3838', '21959068', 'valeriandysmenorrhea', 'rct'),
    ('REF-3839', '38359657', 'valerianumbrella', 'systematic-review'),
    ('REF-3840', '21399726', 'valeriancancersleep', 'rct'),
    ('REF-3841', '21775910', 'valerianmenopausesleep', 'rct'),
    ('REF-3842', '28278010', 'valerianhotflashes', 'rct'),
    ('REF-3843', '17054208', 'valeriananxietycochrane', 'systematic-review'),
])


def grieve(key, rid, name, url, summary):
    NEW[key] = (rid, [('author', 'Grieve, M'), ('title', f'{name} - A Modern Herbal'), ('year', '1931'), ('url', url),
                      ('note', rid), ('study_type', 'traditional'),
                      ('summary', f'Grieve, A Modern Herbal (1931). {summary} Read 2026-11-13.')])


grieve('grieve1931nettle', 'REF-3844', 'Nettles (Urtica dioica)', 'https://www.botanical.com/botanical/mgmh/n/nettle03.html',
       'For bronchial and asthmatic troubles, bleeding, incipient dropsy and gouty gravel (acts on the kidneys), nettlerash, burns, rheumatic gout and chronic rheumatism ("urtication"), diabetes (a 1926 report) and as a spring tonic.')
grieve('grieve1931valerian', 'REF-3845', 'Valerian (Valeriana officinalis)', 'https://www.botanical.com/botanical/mgmh/v/valeri01.html',
       'A powerful nervine, stimulant, carminative and antispasmodic; for nervous unrest and overstrain, neuralgic pains and palpitations; "allays pain and promotes sleep"; older herbals used it for cramp. Warns that large, repeated doses cause headache and stupor.')
grieve('grieve1931mullein', 'REF-3846', 'Mullein, Great (Verbascum thapsus)', 'https://www.botanical.com/botanical/mgmh/m/mulgre63.html',
       'For pectoral complaints, coughs and colds, mild catarrhs and asthma; diarrhoea and piles; the flower oil for earache; externally for bruises, frost bites, burns and ringworm.')
grieve('grieve1931vervain', 'REF-3847', 'Vervain (Verbena officinalis)', 'https://www.botanical.com/botanical/mgmh/v/vervai08.html',
       'Astringent, diaphoretic and antispasmodic; for intermittent fevers, ulcers, ophthalmia and pleurisy; a galactagogue; as a poultice for headache, ear neuralgia and rheumatism; for bowel pain and piles.')
grieve('grieve1931coltsfoot', 'REF-3848', 'Coltsfoot (Tussilago farfara)', 'https://www.botanical.com/botanical/mgmh/c/coltsf88.html',
       'Demulcent, expectorant and tonic, "one of the most popular of cough remedies": coughs, colds, asthma, catarrh and chronic bronchitis; externally for erysipelas, hot swellings and inflammations, and wheals.')
grieve('grieve1931fenugreek', 'REF-3849', 'Fenugreek (Trigonella foenum-graecum)', 'https://www.botanical.com/botanical/mgmh/f/fenugr07.html',
       'For fevers and inflamed stomach and intestines; a poultice for abscesses, boils and carbuncles; for gout and diabetes; as a tonic in debility.')

BIB = dict(
    retag={'REF-0148': 'preclinical', 'REF-1117': 'narrative-review', 'REF-0027': 'narrative-review', 'REF-0911': 'narrative-review',
           'REF-0910': 'narrative-review', 'REF-0304': 'preclinical', 'REF-1333': 'narrative-review', 'REF-0390': 'narrative-review',
           'REF-0409': 'narrative-review', 'REF-0594': 'narrative-review', 'REF-2571': 'narrative-review', 'REF-2572': 'narrative-review',
           'REF-1123': 'narrative-review'},
    new=NEW)

PLAN = {
    'trifolium_repens': [('purge', 'REF-0098')]   # Grieve has no white clover entry (only red clover)
                        + [('rm', c, ['REF-0027']) for c in ('arthritis', 'bruising', 'cold', 'immune-support', 'menstrual-cramps', 'muscle-spasm', 'skin-irritation')]
                        + [('arm', a, ['REF-0140']) for a in ('anti-inflammatory', 'antioxidant', 'antispasmodic', 'immunomodulator', 'vulnerary')] + [
        ('drop', 'bruising'), ('drop', 'cold'), ('drop', 'menstrual-cramps'), ('drop', 'muscle-spasm'),
        ('rm', 'wounds', ['REF-2904']), ('arm', 'vulnerary', ['REF-2904']), ('refadd', ['REF-2904']),   # result was for T. canescens
        ('rm', 'infection', ['REF-2941']), ('arm', 'antimicrobial', ['REF-2941']), ('refadd', ['REF-2941']),   # in-silico only
        ('null', 'infection', ['REF-2909']), ('arm', 'antimicrobial', ['REF-2909']),   # tannins: no inhibition of Cryptosporidium
        ('rmk', 'cognitive-function', ['REF-2937']), ('rmk', 'blood-sugar', ['REF-2935']),
        ('status', 'blood-sugar', 'needs-review'),
        ('note', 'wounds', 'A white clover ointment sped wound healing in rats (preclinical)'),
        ('note', 'inflammation', 'White clover compounds had anti-inflammatory activity in the lab (preclinical)'),
        ('note', 'infection', 'White clover essential oil was active against multidrug-resistant bacteria in the lab (preclinical); its tannins did not inhibit Cryptosporidium'),
        ('note', 'kidney-support', 'White clover leaf extract protected the kidneys of mice from paracetamol damage (preclinical)'),
        ('note', 'liver-support', 'White clover extract protected the liver of mice from paracetamol damage (preclinical)'),
        ('note', 'cancer', 'White clover extract blocked the growth of leukaemia cells in the lab (preclinical)'),
        ('note', 'cognitive-function', 'White clover leaf compounds inhibited cholinesterase in the lab (preclinical)'),
        ('note', 'blood-sugar', 'White clover flower extract inhibited a starch-digesting enzyme in the lab (preclinical)'),
    ],
    'trigonella_foenum_graecum': [
        ('purge', 'REF-0308'),   # "WHO Monographs Vol 1" - fenugreek is not in volume 1
        ('arm', 'aphrodisiac', ['REF-0148']), ('arm', 'antidiabetic', ['REF-0148']), ('rm', 'inflammation', ['REF-0148']),
        ('arm', 'anti-inflammatory', ['REF-0182']), ('arm', 'aphrodisiac', ['REF-0182']),
        ('add', 'blood-sugar', ['REF-3817', 'REF-2515', 'REF-3849']), ('add', 'metabolic-support', ['REF-2515']),
        ('add', 'cardiovascular-support', ['REF-3818']), ('add', 'arthritis', ['REF-3849']),
        ('newpair', 'high-cholesterol', ['REF-3818', 'REF-3819', 'REF-2515'], 'Fenugreek lowered total and LDL cholesterol and triglycerides and raised HDL in meta-analyses of trials'),
        ('newpair', 'high-blood-pressure', ['REF-3820'], 'Fenugreek seed lowered systolic (not diastolic) blood pressure in a meta-analysis of randomized trials'),
        ('newpair', 'hot-flashes', ['REF-3821'], 'A fenugreek seed extract reduced hot flashes and other perimenopausal discomforts vs placebo in a randomized trial'),
        ('newpair', 'menopause', ['REF-3821'], 'A fenugreek seed extract reduced vasomotor symptoms and low mood in perimenopausal women vs placebo in a randomized trial'),
        ('note', 'blood-sugar', 'Fenugreek lowered fasting blood sugar and HbA1c in type 2 diabetes and prediabetes in meta-analyses of trials (study quality varies); traditional use in diabetes (Grieve, A Modern Herbal)'),
        ('note', 'metabolic-support', 'Fenugreek improved blood sugar control and blood lipids in meta-analyses of trials'),
        ('note', 'cardiovascular-support', 'Fenugreek improved blood lipids in a meta-analysis of trials; its seeds protected the heart in a rat model of heart attack (preclinical)'),
        ('note', 'arthritis', 'Fenugreek eased rheumatoid arthritis in animal studies (systematic review); traditional use for gout (Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Fenugreek reduced airway and other inflammation in animal studies (preclinical)'),
        ('note', 'cancer', 'Reviewed for anticancer effects in lab and animal studies (preclinical)'),
    ],
    'tussilago_farfara': [
        ('rmk', 'arthritis', ['REF-0911']), ('rmk', 'skin-irritation', ['REF-0911']), ('rmk', 'inflammation', ['REF-0919']),
        ('drop', 'insomnia'),   # nothing names sleep; the PA warning advises against home internal use
        ('add', 'inflammation', ['REF-3848']), ('add', 'skin-irritation', ['REF-3848']),
        ('arm', 'anti-inflammatory', ['REF-0304']), ('arm', 'sedative', ['REF-0304']), ('arm', 'sedative', ['REF-0911']),
        ('note', 'inflammation', 'Traditionally applied to hot swellings and inflammations (Grieve, A Modern Herbal); coltsfoot compounds reduced inflammatory signals in the lab (preclinical)'),
        ('note', 'skin-irritation', 'Traditionally applied to erysipelas, wheals and inflamed skin (Grieve, A Modern Herbal); use only on intact skin (EMA, pyrrolizidine alkaloids)'),
    ],
    'urtica_dioica': [('rm', c, ['REF-0098']) for c in ('arthritis', 'back-pain', 'cold', 'immune-support', 'inflammation', 'skin-irritation', 'swelling', 'urinary-support', 'uti')]
                     + [('arm', a, ['REF-0098']) for a in ('anti-inflammatory', 'anti-rheumatic', 'antioxidant', 'diuretic', 'immunomodulator')]
                     + [('arm', a, ['REF-0263']) for a in ('anti-inflammatory', 'anti-rheumatic', 'antioxidant', 'diuretic', 'immunomodulator')]
                     + [('arm', a, ['REF-0050']) for a in ('antioxidant', 'diuretic', 'immunomodulator')] + [
        ('drop', 'cold'), ('drop', 'immune-support'), ('drop', 'uti'),   # nothing names them (UTI: diuretic only)
        ('rm', 'urinary-support', ['REF-1334', 'REF-1337']), ('refadd', ['REF-1334', 'REF-1337']),   # unnamed BPH review; saw palmetto + nettle combination
        ('add', 'arthritis', ['REF-3844', 'REF-3827']), ('nulladd', 'arthritis', ['REF-3828']),
        ('add', 'skin-irritation', ['REF-3844']), ('add', 'swelling', ['REF-3844']), ('add', 'urinary-support', ['REF-3844']),
        ('aadd', 'diuretic', ['REF-3844']), ('aadd', 'anti-rheumatic', ['REF-3844']),
        ('newpair', 'prostate-support', ['REF-3823', 'REF-3824', 'REF-3825', 'REF-0263'], 'Nettle root extract eased urinary symptoms of an enlarged prostate (BPH) vs placebo in randomized trials'),
        ('newpair', 'blood-sugar', ['REF-1331', 'REF-3822'], 'Nettle lowered fasting blood sugar in type 2 diabetes in meta-analyses of trials (effects on HbA1c were inconsistent)'),
        ('newpair', 'hot-flashes', ['REF-3826'], 'Nettle reduced menopausal hot flashes and improved quality of life vs placebo in a randomized trial'),
        ('note', 'arthritis', 'Nettle leaf stung onto the skin eased base-of-thumb osteoarthritis pain vs placebo in a randomized trial (a knee-pain pilot found no difference); nettle leaf is reviewed for osteoarthritis; traditional for rheumatism and gout (Grieve, A Modern Herbal)'),
        ('note', 'back-pain', 'Nettle leaf is reviewed among herbal anti-inflammatories for chronic low back pain (review)'),
        ('note', 'inflammation', 'Nettle leaf is reviewed among herbal anti-inflammatories for painful osteoarthritis (review); nettle compounds were anti-inflammatory in the lab (preclinical)'),
        ('note', 'skin-irritation', 'Traditionally taken for nettle rash (Grieve, A Modern Herbal)'),
        ('note', 'swelling', 'Traditional diuretic for incipient dropsy (Grieve, A Modern Herbal)'),
        ('note', 'urinary-support', 'Nettle root eased urinary symptoms of an enlarged prostate (reviews); traditional for gravel (Grieve, A Modern Herbal)'),
    ],
    'vaccinium_macrocarpon': [
        ('rm', 'uti', ['REF-1343']), ('refadd', ['REF-1343']),   # high vs low dose comparison, no placebo
        ('rm', 'uti', ['REF-1346']), ('arm', 'urinary-antiseptic', ['REF-1346']), ('refadd', ['REF-1346']),   # lingonberry (V. vitis-idaea) products
        ('nulladd', 'uti', ['REF-3829']), ('nulladd', 'infection', ['REF-3829']),
        ('add', 'urinary-support', ['REF-3830']), ('nulladd', 'urinary-support', ['REF-3832']),
        ('newpair', 'oral-health', ['REF-3831'], 'A cranberry drink reduced gum inflammation and plaque vs control in people with gingivitis in a randomized trial'),
        ('note', 'uti', 'Cranberry reduced recurrent urinary tract infections in women, children and people at risk after medical procedures (Cochrane review), but not in the elderly, people with bladder-emptying problems or multiple sclerosis; it blocks E. coli sticking to the bladder lining'),
        ('note', 'infection', 'Prevention of recurrent urinary tract infections in women and children (Cochrane review); no benefit in multiple sclerosis in a randomized trial'),
        ('note', 'urinary-support', 'Cranberry reduced recurrent urinary tract infections in women (meta-analyses) and improved lower urinary tract symptoms in men in a randomized trial; it did not help overactive bladder in an intention-to-treat analysis'),
    ],
    'vaccinium_myrtillus': [
        ('null', 'eye-strain', ['REF-0408']),   # SR: no support for improved night vision
        ('add', 'eye-strain', ['REF-3833', 'REF-3834']),
        ('arm', 'venotonic', ['REF-0409']),
        ('add', 'inflammation', ['REF-3835']), ('nulladd', 'high-cholesterol', ['REF-3836']),
        ('note', 'eye-strain', 'Bilberry extract eased eye fatigue from screen work and relaxed eye-focusing muscles vs placebo in randomized trials; a systematic review found it does not improve night vision'),
        ('note', 'inflammation', 'Bilberries reduced low-grade inflammation in people with features of metabolic syndrome in a randomized trial (review of clinical studies)'),
        ('note', 'high-cholesterol', 'Reviews describe benefits on blood lipids, but a 2025 meta-analysis found bilberry lowered triglycerides and HbA1c, not cholesterol'),
    ],
    'valeriana_officinalis': [('arm', a, ['REF-0025']) for a in ('anti-inflammatory', 'antioxidant', 'antispasmodic')] + [
        ('drop', 'arthritis'), ('drop', 'inflammation'), ('drop', 'skin-irritation'),   # only Hoffmann (unverifiable) named them
        ('drop', 'muscle-spasm'),
        ('null', 'insomnia', ['REF-1356', 'REF-1351']), ('nulladd', 'insomnia', ['REF-3839', 'REF-3840']),
        ('add', 'insomnia', ['REF-3841', 'REF-3845']),
        ('add', 'menstrual-cramps', ['REF-3837', 'REF-3838']),
        ('aadd', 'sedative', ['REF-3845']), ('aadd', 'antispasmodic', ['REF-3845']),
        ('newpair', 'hot-flashes', ['REF-3842'], 'Valerian reduced the severity and frequency of hot flashes vs placebo in a triple-blind randomized trial'),
        ('newpair', 'anxiety', ['REF-1352'], 'Valerian reduced anxiety in haemodialysis patients in a randomized crossover trial; a Cochrane review found too little evidence to judge it for anxiety disorders'),
        ('nulladd', 'anxiety', ['REF-3843', 'REF-1356']),
        ('newpair', 'depression', ['REF-1352'], 'Valerian reduced depression scores in haemodialysis patients in a randomized crossover trial'),
        ('note', 'insomnia', 'Valerian improved subjective sleep quality in some meta-analyses and trials, but a 2024 umbrella review concluded it lacks firm support for insomnia and several placebo-controlled trials found no benefit; traditional sleep remedy (Grieve, A Modern Herbal)'),
        ('note', 'menstrual-cramps', 'Valerian reduced period pain vs placebo in a meta-analysis and a randomized trial; traditional antispasmodic'),
    ],
    'verbascum_densiflorum': [
        ('drop', 'bronchitis'), ('drop', 'earache'), ('drop', 'pain'),   # EU monograph/ESCOP: cold, cough, sore throat only; ear-drop trials were combinations
        ('rm', 'skin-irritation', ['REF-0441', 'REF-0442', 'REF-1383']), ('refadd', ['REF-1383']),
        ('note', 'cold', 'Traditional use for sore throat with dry cough and a cold (EU herbal monograph); demulcent and mild expectorant for a cold with cough (ESCOP)'),
        ('note', 'cough', 'Traditional use for sore throat with dry cough and a cold (EU herbal monograph); demulcent and mild expectorant for a cold with cough (ESCOP)'),
        ('note', 'sore-throat', 'Traditional use for sore throat with dry cough and a cold (EU herbal monograph; ESCOP)'),
        ('note', 'respiratory-support', 'Traditional demulcent and mild expectorant for a cold with cough and sore throat (EU herbal monograph; ESCOP)'),
    ],
    'verbascum_thapsus': [
        ('rmk', 'arthritis', ['REF-1123']), ('rmk', 'bronchitis', ['REF-1123']), ('rmk', 'skin-irritation', ['REF-1123']),
        ('rm', 'arthritis', ['REF-0186']), ('rm', 'bronchitis', ['REF-0186']), ('rm', 'inflammation', ['REF-0186']), ('rm', 'skin-irritation', ['REF-0186']),
        ('drop', 'insomnia'),
        ('arm', 'sedative', ['REF-0186']), ('arm', 'sedative', ['REF-1123']),
        ('arm', 'expectorant', ['REF-1125']), ('refadd', ['REF-1125']),   # anthelmintic / gut relaxant study
        ('arm', 'anti-inflammatory', ['REF-1131']),
        ('newpair', 'wounds', ['REF-1131'], 'A mullein cream improved episiotomy wound healing vs placebo by day 10 in a randomized trial'),
        ('add', 'cough', ['REF-0441', 'REF-3846']), ('add', 'respiratory-support', ['REF-0441', 'REF-3846']),
        ('note', 'cough', 'Traditional use for sore throat with dry cough and a cold (EU herbal monograph); traditional cough remedy (Grieve, A Modern Herbal)'),
        ('note', 'respiratory-support', 'Traditional remedy for coughs, colds and chest complaints (EU herbal monograph; Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Reviewed for anti-inflammatory activity (review; preclinical)'),
        ('note', 'cancer', 'Mullein extracts had anticancer activity in the lab (preclinical)'),
    ],
    'verbena_officinalis': [('rmk', c, ['REF-0523']) for c in ('anxiety', 'arthritis', 'back-pain', 'bloating', 'depression', 'headache', 'indigestion', 'insomnia', 'nervous-tension', 'skin-irritation', 'stress')] + [
        ('add', 'headache', ['REF-3847']), ('add', 'arthritis', ['REF-3847']),
        ('note', 'anxiety', 'A vervain extract had anxiolytic, sedative and anticonvulsant effects in mice (preclinical)'),
        ('note', 'nervous-tension', 'A vervain extract had anxiolytic and sedative effects in mice (preclinical)'),
        ('note', 'insomnia', 'A vervain extract shortened time to sleep and lengthened sleep in mice (preclinical)'),
        ('note', 'depression', 'Vervain extract had an antidepressant effect in rats (preclinical)'),
        ('note', 'headache', 'Traditionally applied as a poultice for headache (Grieve, A Modern Herbal)'),
        ('note', 'arthritis', 'Traditionally applied as a poultice for rheumatism (Grieve, A Modern Herbal)'),
        ('note', 'stress', 'inferred from anxiolytic action'),
        ('note', 'inflammation', 'Vervain compounds reduced inflammation in lab and animal studies (review; preclinical)'),
    ],
}

NOTES = {
    'trifolium_repens': 'Deep audit (2nd pass + deep). Generic Grieve REF-0098 purged from this record: Grieve has no white clover entry (checked 2026-11-13; only Clover, Red). White clover review REF-0027 (no abstract, retagged narrative-review) was pinned to 9 pairs; kept only where a checkable study agrees (inflammation, wounds). Clover-isoflavone review REF-0140 removed from 5 actions. Bruising, cold, menstrual-cramps, muscle-spasm dropped (nothing names them). T. canescens wound result REF-2904 and in-silico REF-2941 removed; Cryptosporidium tannin study REF-2909 (no inhibition) moved to no-effect. Blood-sugar is in vitro only (verified -> needs-review).',
    'trigonella_foenum_graecum': 'Deep audit. REF-0308 "WHO Monographs Vol 1 (1999)" purged from this record: fenugreek is not in volume 1. Rat MI study REF-0148 (retagged preclinical) and glycaemia MA REF-0182 removed from non-matching actions. Glycaemia MA REF-3817 and held T2D MA REF-2515 added. New pairs (owner rule): high-cholesterol (2 MAs + REF-2515), high-blood-pressure (MA; systolic only), hot-flashes and menopause (placebo RCT). Grieve REF-3849 added (diabetes, gout). Gaps: dysmenorrhoea MA (effect "highly uncertain"), lactation RCT (no significant difference), Alzheimer\'s RCT (within-group only).',
    'tussilago_farfara': 'Deep audit. Review REF-0911 and NO-production study REF-0919 never name arthritis, skin irritation or inflammation: moved to mechanistic. Insomnia dropped (nothing names sleep; the record\'s own PA warning advises against home internal use). PA-content paper REF-0304 (retagged preclinical) removed from the anti-inflammatory and sedative actions. Grieve REF-3848 added (hot swellings, inflammations, wheals). Gap: coltsfoot\'s traditional cough/bronchitis use is not listed as a pair (no RCT; PA toxicity).',
    'urtica_dioica': 'Deep audit. Generic Grieve REF-0098 replaced by the nettle entry REF-3844 (read 2026-11-13: rheumatism, gout, nettlerash, dropsy, gravel). Chrubasik review REF-0050 and the BPH paper REF-0263 removed from actions they do not address. Cold, immune-support and UTI dropped (nothing names them). BPH review REF-1334 (never names urinary) and the saw palmetto + nettle combination REF-1337 removed. Thumb-OA nettle-sting RCT REF-3827 added; knee pilot REF-3828 no-effect. New pairs (owner rule): prostate-support (3 RCTs), blood-sugar (held MA REF-1331 + MA REF-3822), hot-flashes (placebo RCT).',
    'vaccinium_macrocarpon': 'Deep audit. Dose-comparison RCT REF-1343 (no placebo arm) removed from uti; lingonberry (V. vitis-idaea) review REF-1346 removed from uti and the action. MS placebo RCT REF-3829 (no difference) recorded as no-effect. Men-LUTS RCT REF-3830 added; OAB RCT REF-3832 (ITT null) no-effect. New pair (owner rule): oral-health (gingivitis RCT). REF-0390 retagged narrative-review. Gap: RA juice RCT (within-group change only).',
    'vaccinium_myrtillus': 'Deep audit. Night-vision SR REF-0408 concludes no support for improved night vision but was the only card for eye-strain: moved to no-effect; two placebo RCTs on screen-work eye fatigue added. REF-0409 (tagged rct; a review) retagged and removed from the venotonic action. Inflammation RCT REF-3835 added; 2025 cardiometabolic MA REF-3836 (no cholesterol effect) no-effect for high-cholesterol. Four reviews retagged narrative-review.',
    'valeriana_officinalis': 'Deep audit. Hoffmann REF-0112 (unverifiable) was the only card for arthritis, inflammation, skin-irritation and muscle-spasm: dropped. Sleep SR/MA REF-0025 removed from three actions. Insomnia: kava/valerian internet RCT REF-1356 and the 2011 SR REF-1351 moved to no-effect; 2024 umbrella review REF-3839 and the Barton cancer RCT REF-3840 added as no-effect; postmenopausal RCT REF-3841 and Grieve REF-3845 added. Dysmenorrhoea MA + RCT added. New pairs (owner rule): hot-flashes (placebo RCT), anxiety and depression (haemodialysis RCT REF-1352; Cochrane anxiety review REF-3843 no-effect).',
    'verbascum_densiflorum': 'Deep audit. EU monograph REF-0441 (page read 2026-11-13: sore throat with dry cough and cold) and ESCOP REF-0442 (cold with cough, sore throat) name neither bronchitis nor earache: bronchitis, earache and pain dropped (the ear-drop RCTs were combination products). Wound-healing study REF-1383 removed from skin-irritation.',
    'verbascum_thapsus': 'Deep audit. HerbClip REF-0186 (unverifiable) removed from pairs Grieve REF-3846 does not support; review REF-1123 (retagged narrative-review) moved to mechanistic where it never names the symptom. Insomnia dropped (nothing names sleep). Anthelmintic/relaxant study REF-1125 removed from the expectorant action. EU monograph REF-0441 (covers V. thapsus) and Grieve added to cough and respiratory-support. New pair (owner rule): wounds (episiotomy placebo RCT REF-1131).',
    'verbena_officinalis': 'Deep audit. Planta Med review REF-0523 was cited on 11 pairs it never names: moved to mechanistic there. Grieve REF-3847 added (poultice for headache and rheumatism). Remaining direct evidence is animal studies (anxiety, sleep, depression) - notes now say so.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 18', os.path.join(HERE, 'deep', 'd18_changes.tsv'), **BIB)
