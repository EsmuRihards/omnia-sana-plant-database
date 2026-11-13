"""Deep audit of batch 19 (veronica-officinalis .. zingiber-officinale): 2nd-pass strict-match + deep checks. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3850..REF-3877 (Grieve x6 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib
import yamlsplice as Y

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3853', '35734476', 'violetinsomniama', 'meta-analysis'),
    ('REF-3854', '38177831', 'violetmenopausesleep', 'rct'),
    ('REF-3856', '11159568', 'vitexpmsschellenberg', 'rct'),
    ('REF-3857', '20334585', 'vitexpmschina2010', 'rct'),
    ('REF-3858', '19269753', 'vitexpmschina2009', 'rct'),
    ('REF-3859', '23022391', 'vitexze440', 'rct'),
    ('REF-3860', '42199854', 'ashwagandhacognitionma', 'meta-analysis'),
    ('REF-3861', '36017529', 'ashwagandhaanxietystressma', 'meta-analysis'),
    ('REF-3862', '40746175', 'ashwagandhacortisolma', 'meta-analysis'),
    ('REF-3863', '41644067', 'ashwagandhamentalhealthma', 'meta-analysis'),
    ('REF-3864', '42367407', 'ashwagandhaliverinjury', 'narrative-review'),
    ('REF-3865', '42337792', 'gingert2dma', 'meta-analysis'),
    ('REF-3866', '42566667', 'gingerbpma', 'meta-analysis'),
    ('REF-3867', '38625733', 'gingercinvma', 'meta-analysis'),
    ('REF-3868', '38770631', 'gingerdysmenorrheama', 'meta-analysis'),
    ('REF-3869', '33293189', 'gingermigrainema', 'meta-analysis'),
    ('REF-3870', '31398997', 'gingermigraineprophylaxis', 'rct'),
    ('REF-3871', '20418184', 'gingermusclepain', 'rct'),
    ('REF-3872', '30299178', 'gingerrunners', 'rct'),
    ('REF-3873', '25300574', 'gingeroama2015', 'meta-analysis'),
    ('REF-3874', '32214292', 'gingerkneeoama2020', 'meta-analysis'),
    ('REF-3875', '41123858', 'gingerinflammationma', 'meta-analysis'),
])


def grieve(key, rid, name, url, summary):
    NEW[key] = (rid, [('author', 'Grieve, M'), ('title', f'{name} - A Modern Herbal'), ('year', '1931'), ('url', url),
                      ('note', rid), ('study_type', 'traditional'),
                      ('summary', f'Grieve, A Modern Herbal (1931). {summary} Read 2026-11-13.')])


grieve('grieve1931speedwell', 'REF-3850', 'Speedwell, Common (Veronica officinalis)', 'https://www.botanical.com/botanical/mgmh/s/specom75.html',
       'Diaphoretic, alterative, diuretic, expectorant and tonic; an infusion for coughs and catarrh, and a simple remedy in skin diseases; formerly for pectoral and kidney complaints and wounds.')
grieve('grieve1931guelderrose', 'REF-3851', 'Guelder Rose (Cramp Bark, Viburnum opulus)', 'https://www.botanical.com/botanical/mgmh/g/gueros44.html',
       'Nerve sedative and antispasmodic, used "in cramps and spasms of all kinds", convulsions, asthma, hysteria, nervous complaints, palpitation and rheumatism.')
grieve('grieve1931violet', 'REF-3852', 'Violet, Sweet (Viola odorata)', 'https://www.botanical.com/botanical/mgmh/v/vioswe12.html',
       'Expectorant flowers and a slightly laxative syrup; older writers used it for sleeplessness, headache, quinsy and throat roughness, pleurisy and inflammation; seeds for urinary complaints and gravel. The root is strongly emetic and purgative.')
grieve('grieve1931heartsease', 'REF-3855', 'Heartsease (Viola tricolor)', 'https://www.botanical.com/botanical/mgmh/h/hearts10.html',
       'Similar to the violet; a decoction for skin diseases, ointments and poultices for eczema and other skin troubles, scabs and itching; internally for bronchitis; formerly for epilepsy and asthma.')
grieve('grieve1931ginger', 'REF-3876', 'Ginger (Zingiber officinale)', 'https://www.botanical.com/botanical/mgmh/g/ginger13.html',
       'Stimulant and carminative, given in dyspepsia and flatulent colic and alcoholic gastritis, and for diarrhoea from a relaxed bowel; ginger tea for menses stopped by cold.')
grieve('grieve1931cornsilk', 'REF-3877', 'Corn Silk (Zea mays)', 'https://www.botanical.com/botanical/mgmh/c/corsi105.html',
       'A mild stimulant, diuretic and demulcent, useful in acute and chronic cystitis and in bladder irritation from uric acid and phosphatic gravel.')

BIB = dict(
    retag={'REF-0007': 'narrative-review', 'REF-0164': 'narrative-review', 'REF-0610': 'narrative-review', 'REF-1139': 'rct',
           'REF-0463': 'preclinical', 'REF-2577': 'narrative-review', 'REF-0435': 'narrative-review', 'REF-2580': 'narrative-review',
           'REF-2255': 'narrative-review', 'REF-0436': 'narrative-review', 'REF-0557': 'preclinical'},
    delete=['REF-0440'],   # ScienceDirect Topics page: 403, cannot be checked
    new=NEW)

PLAN = {
    'veronica_officinalis': [
        ('rm', 'bloating', ['REF-0514']), ('rm', 'bronchitis', ['REF-0514']),
        ('rmk', 'bronchitis', ['REF-0632']), ('rmk', 'cough', ['REF-0632']),
        ('arm', 'anti-inflammatory', ['REF-0513']), ('arm', 'antioxidant', ['REF-0513']), ('arm', 'expectorant', ['REF-0513']), ('refadd', ['REF-0513']),   # DNA-barcoding adulteration study
        ('arm', 'antioxidant', ['REF-2554', 'REF-2555']), ('refadd', ['REF-2554', 'REF-2555']),   # 1970s phytochemistry
        ('add', 'cough', ['REF-3850']), ('add', 'respiratory-support', ['REF-3850']), ('add', 'skin-irritation', ['REF-3850']),
        ('aadd', 'expectorant', ['REF-3850']),
        ('note', 'cough', 'Traditional remedy for coughs and catarrh (Grieve, A Modern Herbal; HerbaZest); speedwell extract reduced inflammatory signals in human lung cells (preclinical)'),
        ('note', 'inflammation', 'Traditionally used for inflammatory pain (HerbaZest); speedwell extract reduced inflammatory signals in human lung cells (preclinical)'),
        ('note', 'indigestion', 'Traditional remedy for stomach complaints (HerbaZest); speedwell extract helped gastric ulcers heal in rats (preclinical)'),
        ('note', 'respiratory-support', 'Traditional remedy for coughs, catarrh and chest complaints (Grieve, A Modern Herbal; HerbaZest)'),
        ('note', 'skin-irritation', 'Traditionally used for skin diseases and to calm irritated skin (Grieve, A Modern Herbal; HerbaZest)'),
    ],
    'viburnum_opulus': [
        ('purge', 'REF-0440'),
        ('rm', 'headache', ['REF-0439']),   # Herbal Reality page does not name headache
        ('rmk', 'menstrual-cramps', ['REF-0610']),
        ('rm', 'menstrual-cramps', ['REF-1140']), ('refadd', ['REF-1140']),   # rat endometriosis lesions
        ('arm', 'analgesic', ['REF-1139']), ('refadd', ['REF-1139']),   # ureteral stone expulsion vs tamsulosin
        ('add', 'muscle-spasm', ['REF-3851']), ('aadd', 'antispasmodic', ['REF-3851']),
        ('status', 'menstrual-cramps', 'needs-review'),
        ('note', 'menstrual-cramps', 'Traditional remedy for menstrual cramps (Herbal Reality); no clinical trials'),
        ('note', 'muscle-spasm', 'Traditional antispasmodic for cramps and spasms of all kinds (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'back-pain', 'Traditionally used for back and muscle pain (Herbal Reality)'),
        ('note', 'pain', 'Traditionally used for cramping and nerve pain (Herbal Reality)'),
        ('note', 'cancer', 'Cramp bark extract slowed colorectal cancer cell growth in the lab (preclinical)'),
    ],
    'viola_odorata': [
        ('rm', 'arthritis', ['REF-0517']),   # Herbal Reality names arthritis for V. tricolor, not sweet violet
        ('rm', 'bronchitis', ['REF-0609']),
        ('arm', 'anti-inflammatory', ['REF-1146']),
        ('newpair', 'fever', ['REF-1146'], 'Sweet violet oil reduced fever vs placebo in children with febrile neutropenia in a triple-blind randomized trial'),
        ('add', 'cough', ['REF-1148', 'REF-3852']), ('add', 'headache', ['REF-1148', 'REF-3852']),
        ('add', 'insomnia', ['REF-3853', 'REF-3854', 'REF-3852']), ('add', 'sore-throat', ['REF-3852']),
        ('arm', 'sedative', ['REF-1149']), ('refadd', ['REF-1149']),   # memory study in rodents
        ('note', 'asthma', 'Violet flower syrup, added to standard treatment, sped cough relief in children with asthma in a randomized trial'),
        ('note', 'cough', 'Violet syrup sped cough relief in children with asthma and eased cough in COVID-19 in randomized trials; traditional expectorant (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'bronchitis', 'Traditional remedy for bronchitis and catarrh (Herbal Reality)'),
        ('note', 'headache', 'Violet syrup eased headache among other COVID-19 symptoms in a randomized trial; traditional for headache (Grieve, A Modern Herbal)'),
        ('note', 'insomnia', 'Violet extract improved sleep quality and insomnia severity vs placebo in a meta-analysis and randomized trials; traditional for sleeplessness (Grieve, A Modern Herbal)'),
        ('note', 'sore-throat', 'Traditional remedy for sore throat (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'respiratory-support', 'Violet syrup eased cough in randomized trials; traditional for coughs, colds and catarrh (Herbal Reality)'),
        ('note', 'skin-irritation', 'Traditionally used for eczema and inflamed skin (Herbal Reality)'),
        ('note', 'inflammation', 'Traditionally used for inflammatory skin conditions (Herbal Reality)'),
        ('note', 'cancer', 'Sweet violet extract and its peptides were active against breast cancer cells in the lab (preclinical)'),
    ],
    'viola_tricolor': [
        ('rmk', 'arthritis', ['REF-0463', 'REF-0617']), ('rmk', 'eczema', ['REF-0617']), ('rmk', 'psoriasis', ['REF-0617']),
        ('rm', 'eczema', ['REF-2579']), ('refadd', ['REF-2579']),   # case report, multi-herb products
        ('rm', 'inflammation', ['REF-2577']), ('arm', 'anti-inflammatory', ['REF-2577']), ('refadd', ['REF-2577']),   # multi-herb anti-cytokine preparation
        ('arm', 'demulcent', ['REF-0463']), ('arm', 'emollient', ['REF-0463']), ('arm', 'expectorant', ['REF-0463']),   # immune-cell study
        ('add', 'eczema', ['REF-3855', 'REF-0517']), ('add', 'psoriasis', ['REF-0517']), ('add', 'arthritis', ['REF-0517']),
        ('add', 'skin-irritation', ['REF-3855', 'REF-0517']),
        ('aadd', 'demulcent', ['REF-3855']), ('aadd', 'expectorant', ['REF-3855']),
        ('note', 'eczema', 'Traditional remedy for eczema and other skin troubles (Grieve, A Modern Herbal; Herbal Reality); heartsease cyclotides calmed overactive immune cells in the lab (preclinical)'),
        ('note', 'psoriasis', 'Traditionally used for psoriasis (Herbal Reality); heartsease cyclotides calmed overactive immune cells in the lab (preclinical)'),
        ('note', 'arthritis', 'Traditionally used for arthritis (Herbal Reality)'),
        ('note', 'skin-irritation', 'Traditionally applied to itching, scabs and inflamed skin (Grieve, A Modern Herbal; Herbal Reality); a heartsease gel reduced sunburn inflammation in rats (preclinical)'),
        ('note', 'inflammation', 'Heartsease extracts reduced inflammation in lab and animal studies (preclinical)'),
        ('note', 'immune-support', 'Heartsease cyclotides inhibited HIV in the lab (preclinical)'),
        ('note', 'cancer', 'Heartsease extracts killed cancer cells and blocked new blood vessels in lab studies (preclinical)'),
    ],
    'vitex_agnus_castus': [('rm', c, ['REF-2580']) for c in ('acne', 'menopause', 'menstrual-cramps', 'pms')]
                          + [('rm', c, ['REF-1610']) for c in ('menstrual-cramps', 'pain', 'pms')] + [
        ('refadd', ['REF-2580', 'REF-1610']),   # genus-level review; cohort of VAC-containing products incl. a homeopathic combination
        ('rm', 'pms', ['REF-0435']), ('refadd', ['REF-0435']),   # hyperprolactinaemia review
        ('null', 'pms', ['REF-1607']),   # MA: most trials cannot be used as evidence (incomplete reporting)
        ('add', 'pms', ['REF-3856', 'REF-3857', 'REF-3858', 'REF-3859']),
        ('note', 'pms', 'Vitex extracts relieved premenstrual syndrome vs placebo in randomized trials in Germany and China and in meta-analyses, though reviews flag high risk of bias and incomplete reporting; it matched fluoxetine for the physical symptoms of PMDD'),
        ('note', 'pain', 'Vitex eased cyclical breast pain (mastalgia) in a meta-analysis of trials; it lowers prolactin (reviews)'),
        ('note', 'menstrual-cramps', 'Vitex extracts eased premenstrual and menstrual-cycle complaints in clinical trials (systematic review)'),
        ('note', 'menopause', 'Proposed for menopausal complaints, but rigorous trials of vitex alone are lacking (review)'),
    ],
    'withania_somnifera': [
        ('add', 'insomnia', ['REF-2245']), ('add', 'memory', ['REF-2253', 'REF-3860']), ('add', 'cognitive-function', ['REF-2253', 'REF-3860']),
        ('newpair', 'stress', ['REF-2247', 'REF-3861', 'REF-2248', 'REF-2251'], 'Ashwagandha lowered stress scores and cortisol vs placebo in meta-analyses and randomized trials (low-certainty evidence); a 2025 meta-analysis found lower cortisol but no change in perceived stress'),
        ('nulladd', 'stress', ['REF-3862']),
        ('newpair', 'anxiety', ['REF-2247', 'REF-3861', 'REF-3863'], 'Ashwagandha reduced anxiety vs placebo in meta-analyses of randomized trials (low-certainty evidence)'),
        ('newpair', 'depression', ['REF-3863'], 'Ashwagandha reduced depression symptoms in a 2026 meta-analysis of randomized trials (heterogeneous studies)'),
        ('note', 'insomnia', 'Ashwagandha extract improved sleep in adults in a meta-analysis of randomized trials'),
        ('note', 'memory', 'Ashwagandha root extract improved memory in mild cognitive impairment in a randomized trial and in a 2026 meta-analysis'),
        ('note', 'cognitive-function', 'Ashwagandha improved memory, attention and executive function in a 2026 meta-analysis and a randomized trial in mild cognitive impairment'),
        ('note', 'cancer', 'Withaferin A and other withanolides killed cancer cells in lab and animal studies (review; preclinical)'),
    ],
    'zea_mays': [
        ('rmk', 'arthritis', ['REF-0436']), ('rmk', 'inflammation', ['REF-0436']), ('rmk', 'skin-irritation', ['REF-0436']),
        ('drop', 'cough'), ('drop', 'sore-throat'), ('drop', 'infection'),   # nothing names them; its demulcent use is urinary
        ('rmk', 'uti', ['REF-0436', 'REF-0557']), ('add', 'uti', ['REF-3877']),
        ('add', 'urinary-support', ['REF-3877']), ('aadd', 'diuretic', ['REF-3877']), ('aadd', 'demulcent', ['REF-3877']),
        ('note', 'uti', 'Traditional demulcent and diuretic for acute and chronic cystitis and bladder irritation (Grieve, A Modern Herbal)'),
        ('note', 'urinary-support', 'Traditional diuretic and demulcent for bladder irritation and gravel (Grieve, A Modern Herbal); corn silk extract was diuretic in rats (preclinical)'),
        ('note', 'swelling', 'Corn silk extract was diuretic in rats (preclinical); traditional diuretic (review)'),
        ('note', 'inflammation', 'Corn silk compounds reduced inflammation in lab and animal studies (preclinical)'),
        ('note', 'cancer', 'Corn silk extract killed breast cancer cells in the lab (preclinical)'),
    ],
    'zingiber_officinale': [('rmk', c, ['REF-0007']) for c in ('back-pain', 'bloating', 'headache', 'menstrual-cramps', 'respiratory-support', 'skin-irritation')]
                           + [('rm', c, ['REF-0164']) for c in ('arthritis', 'back-pain', 'pain', 'skin-irritation')]
                           + [('arm', a, ['REF-0269']) for a in ('analgesic', 'anti-inflammatory', 'antioxidant', 'antispasmodic', 'digestive')]
                           + [('arm', a, ['REF-0639']) for a in ('analgesic', 'anti-inflammatory', 'antioxidant', 'antispasmodic', 'digestive')]
                           + [('arm', a, ['REF-0295']) for a in ('analgesic', 'anti-inflammatory', 'antioxidant', 'antispasmodic')]
                           + [('arm', a, ['REF-0077']) for a in ('analgesic', 'anti-inflammatory', 'antioxidant')] + [
        ('refadd', ['REF-0269', 'REF-0639']),
        ('rm', 'indigestion', ['REF-0295', 'REF-0634', 'REF-0635']),   # pregnancy / chemotherapy nausea, not indigestion
        ('drop', 'muscle-spasm'),   # gut antispasmodic: off-target
        ('rmk', 'inflammation', ['REF-0638']),
        ('newpair', 'blood-sugar', ['REF-0639', 'REF-3865'], 'Ginger improved HbA1c and other metabolic markers in type 2 diabetes in meta-analyses of trials (fasting blood sugar did not change in one)'),
        ('newpair', 'high-blood-pressure', ['REF-3866'], 'Ginger modestly lowered blood pressure in a 2026 meta-analysis of randomized trials (low-certainty evidence)'),
        ('newpair', 'migraine', ['REF-3869'], 'Ginger relieved migraine pain at 2 hours in a meta-analysis of randomized trials; it did not prevent attacks in a placebo-controlled trial'),
        ('nulladd', 'migraine', ['REF-3870']),
        ('newpair', 'muscle-soreness', ['REF-3871', 'REF-3872'], 'Daily ginger reduced exercise-induced muscle pain and running-induced soreness in randomized placebo-controlled trials'),
        ('add', 'nausea', ['REF-3867']), ('nulladd', 'nausea', ['REF-0634']),
        ('add', 'menstrual-cramps', ['REF-3868']), ('status', 'menstrual-cramps', 'verified'),
        ('add', 'headache', ['REF-3869']), ('add', 'pain', ['REF-3871']),
        ('add', 'arthritis', ['REF-3873']), ('nulladd', 'arthritis', ['REF-3874']),
        ('add', 'inflammation', ['REF-3875']), ('add', 'cardiovascular-support', ['REF-3866']),
        ('add', 'bloating', ['REF-3876']), ('add', 'indigestion', ['REF-3876']),
        ('note', 'nausea', 'Ginger relieved nausea in pregnancy vs placebo in meta-analyses (not vomiting), and helped severe chemotherapy nausea as an add-on in a meta-analysis, though one large placebo-controlled trial found no effect on acute chemotherapy nausea; the EU herbal monograph covers motion sickness'),
        ('note', 'menstrual-cramps', 'Ginger reduced period pain vs placebo, as much as NSAIDs, in meta-analyses of randomized trials'),
        ('note', 'arthritis', 'Ginger modestly reduced osteoarthritis pain and disability vs placebo in a meta-analysis, though a 2020 knee-osteoarthritis meta-analysis found the evidence insufficient'),
        ('note', 'pain', 'Ginger reduced period pain, osteoarthritis pain and exercise-induced muscle pain in meta-analyses and randomized trials'),
        ('note', 'headache', 'Ginger relieved migraine headache at 2 hours in a meta-analysis of randomized trials'),
        ('note', 'inflammation', 'Ginger lowered inflammatory markers (CRP, IL-6) in a meta-analysis of randomized trials'),
        ('note', 'bloating', 'Traditional remedy for bloating, flatulence and mild spasmodic stomach complaints (EU herbal monograph; Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Traditional remedy for dyspepsia and mild spasmodic stomach complaints (EU herbal monograph; Grieve, A Modern Herbal)'),
        ('note', 'cardiovascular-support', 'Ginger modestly lowered blood pressure in a meta-analysis of randomized trials; reviewed for cardiovascular effects'),
    ],
}

NOTES = {
    'veronica_officinalis': 'Deep audit (2nd pass + deep). HerbaZest REF-0514 (12 sources) kept for what it names; removed from bloating (dropped) and bronchitis. Lung-cell study REF-0632 moved to mechanistic for cough/bronchitis. DNA-barcoding adulteration study REF-0513 and two 1970s phytochemistry papers removed from actions. Grieve REF-3850 added (coughs, catarrh, skin diseases).',
    'viburnum_opulus': 'Deep audit. ScienceDirect Topics page REF-0440 (403, auto-collected excerpts) purged and deleted. Herbal Reality REF-0439 (references; read 2026-11-13) does not name headache: removed, headache dropped. Rat endometriosis study REF-1140 and the Nutrients review REF-0610 (never names cramps) removed from menstrual-cramps, which now rests on traditional use only (verified -> needs-review). Ureteral-stone RCT REF-1139 (retagged rct) removed from the analgesic action. Grieve REF-3851 added to muscle-spasm.',
    'viola_odorata': 'Deep audit. Herbal Reality REF-0517 names arthritis for V. tricolor only: removed from arthritis. Asthma-cough RCT REF-0609 removed from bronchitis (never named). Insomnia MA REF-3853 and menopausal-sleep RCT REF-3854 added; COVID RCT REF-1148 added to cough and headache. New pair (owner rule): fever (triple-blind placebo RCT REF-1146). Grieve REF-3852 added. Gap: allergic-rhinitis RCT 32507426 (no abstract available).',
    'viola_tricolor': 'Deep audit. Immune-cell studies REF-0463 (retagged preclinical) and REF-0617 moved to mechanistic where they never name the symptom, and REF-0463 removed from the demulcent/emollient/expectorant actions. A case report on multi-herb products REF-2579 and a multi-herb anti-cytokine preparation REF-2577 removed. Grieve REF-3855 and Herbal Reality REF-0517 (covers V. tricolor) added for eczema, psoriasis, arthritis, skin irritation. Gap: the only RCT is a three-herb ointment.',
    'vitex_agnus_castus': 'Deep audit. Genus-level Vitex review REF-2580 removed from 4 pairs (acne dropped). A cohort of VAC-containing products incl. a homeopathic combination REF-1610 and a hyperprolactinaemia review REF-0435 removed. 2019 MA REF-1607 ("most trials cannot be used as evidence") moved to no-effect for PMS; four placebo RCTs (Schellenberg 2001 BMJ, two Chinese BNO 1095 trials, Ze 440) added. Gaps: menstrual-bleeding MA REF-3115 found no effect (no heavy-bleeding pair).',
    'withania_somnifera': 'Deep audit. Every pair was mechanistic only although held RCTs/MAs named the symptoms: sleep MA REF-2245 wired to insomnia, MCI RCT REF-2253 and the 2026 cognition MA REF-3860 to memory/cognition. New pairs (owner rule): stress (2 MAs + 2 RCTs; cortisol-only MA REF-3862 recorded as no-effect for perceived stress), anxiety (3 MAs), depression (2026 MA). New safety note: idiosyncratic, often cholestatic liver injury (2026 scoping review REF-3864). Safety note #1 is still unsourced (needs-review). Gap: glucose MA (very low certainty).',
    'zea_mays': 'Deep audit. Review REF-0436 (retagged narrative-review) never names arthritis, inflammation, skin irritation, cough, sore throat, infection or UTI: moved to mechanistic; cough, sore-throat and infection dropped (its demulcent use is urinary). Grieve corn silk REF-3877 (cystitis, bladder irritation, gravel) now carries UTI and urinary support. Rat diuresis study REF-0557 retagged preclinical. Gap: corn silk decoction lipid MA (Chinese modified decoctions, unblinded).',
    'zingiber_officinale': 'Deep audit. 2008 review REF-0007 (retagged narrative-review) moved to mechanistic on 6 pairs it never names; respiratory-support dropped. Unreadable review REF-0164 kept only on inflammation. Warfarin-bleeding study REF-0269 and the T2D MA REF-0639 removed from 5 actions; EU monograph REF-0077 from 3. Pregnancy/chemotherapy nausea studies removed from indigestion; muscle-spasm dropped (off-target). Added: dysmenorrhoea MA, OA MA (2020 knee-OA MA no-effect), CINV MA (CINV RCT REF-0634 no-effect), inflammation-marker MA, Grieve REF-3876. New pairs (owner rule): blood-sugar, high-blood-pressure, migraine (MA; prophylaxis RCT no-effect), muscle-soreness (2 RCTs).',
}


def post():
    path = 'plants/withania_somnifera.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    d['contraindications'].append({'note': 'Ashwagandha supplements have been linked to rare, often cholestatic liver injury (jaundice, itching, dark urine); stop it if these appear, and avoid it with chronic liver disease (scoping review of published cases).',
                                   'severity': 'caution', 'reference_ids': ['REF-3864'], 'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 19', os.path.join(HERE, 'deep', 'd19_changes.tsv'), **BIB)
    post()
