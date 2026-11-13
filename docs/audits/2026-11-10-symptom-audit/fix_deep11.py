"""Deep re-sweep of batch 11 (melissa-officinalis .. ononis-arvensis) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3655..REF-3704 (PubMed efetch, deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3655', '40526027', 'herpeslabialissr', 'systematic-review'),
    ('REF-3656', '39683592', 'melissaphytosomesleep', 'rct'),
    ('REF-3657', '37131158', 'melissat2ddepression', 'rct'),
    ('REF-3658', '34766389', 'melissahypertension', 'rct'),
    ('REF-3659', '27261994', 'melissahyperlipidemia', 'rct'),
    ('REF-3660', '35942669', 'peppermintibs2022', 'meta-analysis'),
    ('REF-3661', '30654773', 'peppermintibs2019', 'meta-analysis'),
    ('REF-3662', '24100754', 'peppermintibs2014', 'meta-analysis'),
    ('REF-3663', '19008265', 'fordibs2008', 'meta-analysis'),
    ('REF-3664', '31470006', 'persuadeibs', 'rct'),
    ('REF-3665', '34319275', 'peppermintibs2021', 'rct'),
    ('REF-3666', '8805113', 'goebelpeppermintheadache', 'rct'),
    ('REF-3667', '37730471', 'peppermintfootbath', 'rct'),
    ('REF-3668', '39436586', 'nipplepainma', 'meta-analysis'),
    ('REF-3669', '41544308', 'peppermintponv2026', 'rct'),
    ('REF-3670', '39447066', 'peppermintponvcervical', 'rct'),
    ('REF-3671', '30385422', 'momordicama2019', 'meta-analysis'),
    ('REF-3672', '38274207', 'momordicasr2023', 'systematic-review'),
    ('REF-3673', '39444254', 'momordicalipids', 'meta-analysis'),
    ('REF-3674', '36448674', 'nonicancersr', 'systematic-review'),
    ('REF-3675', '42280334', 'nonipolysaccharideurti', 'rct'),
    ('REF-3676', '23097636', 'nonismokerslipids', 'rct'),
    ('REF-3677', '21294416', 'noniponv', 'rct'),
    ('REF-3678', '8880292', 'holybasildiabetes', 'rct'),
    ('REF-3679', '41883983', 'epomenopause', 'meta-analysis'),
    ('REF-3680', '34200727', 'epomastalgia', 'meta-analysis'),
    ('REF-3681', '8721802', 'epopms1996', 'systematic-review'),
    ('REF-3682', '32441049', 'epolipids', 'meta-analysis'),
    ('REF-3683', '23625331', 'epohotflashes', 'rct'),
    ('REF-3684', '19052401', 'epoatopic', 'rct'),
    ('REF-3685', '31738736', 'epopsych', 'rct'),
    ('REF-3686', '20359269', 'epomastalgiapilot', 'rct'),
    ('REF-3687', '38287654', 'oliveleafcardiometabolic', 'meta-analysis'),
    ('REF-3688', '42303499', 'oliveleafgrade', 'meta-analysis'),
    ('REF-3689', '41848522', 'oleuropeinma', 'meta-analysis'),
    ('REF-3690', '33941427', 'evooglycemic', 'meta-analysis'),
    ('REF-3691', '31539817', 'oliveoilinflammation', 'meta-analysis'),
    ('REF-3692', '36429639', 'oliveoilpressureulcer', 'meta-analysis'),
    ('REF-3693', '41487705', 'oliveoilperiodontal', 'meta-analysis'),
    ('REF-3694', '41740793', 'evoocognition', 'meta-analysis'),
    ('REF-3695', '29708409', 'evoopolyphenolcv', 'meta-analysis'),
    ('REF-3696', '39181437', 'nigellaglycemic2024', 'meta-analysis'),
    ('REF-3697', '38777430', 'nigellalipids2024', 'meta-analysis'),
    ('REF-3698', '38265398', 'nigellamets', 'meta-analysis'),
    ('REF-3699', '37036558', 'nigellainflammation', 'meta-analysis'),
    ('REF-3700', '31892440', 'nigellaasthma', 'meta-analysis'),
    ('REF-3701', '39372205', 'nigellarhinitis', 'meta-analysis'),
    ('REF-3702', '33728708', 'nigellanafld', 'meta-analysis'),
    ('REF-3703', '40714301', 'nigellacvd', 'meta-analysis'),
    ('REF-3704', '41858302', 'nigellacardiometabolic', 'meta-analysis'),
])

BIB = dict(
    retag={'REF-3048': 'narrative-review'},   # essential-oil neuroprotection review tagged clinical
    delete=['REF-0163',                       # "Fasciolosis in humans" - unrelated to peppermint
            'REF-2759', 'REF-3028', 'REF-3034'],   # Ononis spinosa studies (and a Turkish screen of O. spinosa), not O. arvensis
    new=NEW)

PLAN = {
    'melissa_officinalis': [('arm', a, ['REF-0134']) for a in ('anti-inflammatory', 'antioxidant', 'antispasmodic', 'antiviral', 'digestive')] + [
        ('drop', 'muscle-spasm'),
        ('newpair', 'anxiety', ['REF-1194', 'REF-2539', 'REF-3657'], 'Lemon balm reduced anxiety in a meta-analysis of clinical trials and in randomized trials in people with angina or type 2 diabetes'),
        ('add', 'depression', ['REF-2539', 'REF-3657']),
        ('note', 'depression', 'Lemon balm reduced depression scores in a meta-analysis of clinical trials and in randomized trials in people with angina or type 2 diabetes; trials are few and varied'),
        ('newpair', 'stress', ['REF-2539', 'REF-3078'], 'Lemon balm reduced stress scores in people with chronic stable angina in a randomized trial; traditional use for mild symptoms of mental stress (EU herbal monograph)'),
        ('add', 'insomnia', ['REF-2539', 'REF-3656']), ('nulladd', 'insomnia', ['REF-3657']),
        ('note', 'insomnia', 'Lemon balm improved sleep in randomized trials, including a phytosome extract vs placebo; traditional use to aid sleep (EU herbal monograph); one trial in type 2 diabetes found no change in sleep quality'),
        ('newpair', 'high-cholesterol', ['REF-1195', 'REF-1197', 'REF-3659'], 'Lemon balm lowered total and LDL cholesterol and triglycerides in meta-analyses and in a randomized trial in borderline high cholesterol'),
        ('newpair', 'high-blood-pressure', ['REF-1197', 'REF-3658'], 'Lemon balm lowered systolic blood pressure in a meta-analysis and lowered blood pressure in essential hypertension in a randomized crossover trial; one trial in type 2 diabetes found no effect'),
        ('nulladd', 'high-blood-pressure', ['REF-3657']),
        ('add', 'infection', ['REF-3655']),
        ('note', 'infection', 'Topical lemon balm helped cold sores (herpes labialis) in trials (systematic review); antiviral activity in the lab (review)'),
        ('nulladd', 'skin-irritation', ['REF-3527']), ('nulladd', 'inflammation', ['REF-3527']),
        ('note', 'bloating', 'Traditional use for mild digestive complaints such as bloating and flatulence (EU herbal monograph)'),
        ('note', 'indigestion', 'Traditional use for mild digestive complaints (EU herbal monograph)'),
    ],
    'mentha_piperita': [('arm', a, ['REF-0163']) for a in ('analgesic', 'anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive')]
                       + [('arm', a, ['REF-0004']) for a in ('analgesic', 'anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive')]
                       + [('arm', a, ['REF-0100']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant')] + [
        ('purge', 'REF-0163'), ('refadd', ['REF-0004']),   # rat kidney histopathology study kept as a safety reference only
        ('drop', 'muscle-spasm'),
        ('newpair', 'ibs', ['REF-3660', 'REF-3661', 'REF-3662', 'REF-3663', 'REF-0100'], 'Enteric-coated peppermint oil relieved IBS symptoms and abdominal pain vs placebo in meta-analyses (certainty very low to moderate); two recent randomized trials found no significant benefit on their main outcomes'),
        ('nulladd', 'ibs', ['REF-3664', 'REF-3665']),
        ('add', 'headache', ['REF-3666']), ('nulladd', 'headache', ['REF-3667']),
        ('note', 'headache', '10% peppermint oil rubbed on the forehead and temples eased tension-type headache better than placebo and as well as paracetamol in a randomized trial, and is licensed for this use in Germany (review); a peppermint-oil foot bath did not help chronic headache in youth'),
        ('newpair', 'nausea', ['REF-3669', 'REF-3670'], 'Inhaled peppermint oil reduced nausea and vomiting after surgery in randomized trials'),
        ('add', 'pain', ['REF-3668']),
        ('note', 'pain', 'Enteric-coated peppermint oil relieved abdominal pain in IBS (systematic review), and peppermint applied to the nipples reduced breastfeeding nipple pain (meta-analysis)'),
        ('note', 'infection', 'Peppermint extracts and oil were antiviral, antibacterial and antifungal in lab studies (preclinical)'),
    ],
    'momordica_charantia': [
        ('add', 'blood-sugar', ['REF-3671']), ('nulladd', 'blood-sugar', ['REF-3672']), ('nulladd', 'metabolic-support', ['REF-3672']),
        ('note', 'blood-sugar', 'Bitter melon lowered blood sugar in type 2 diabetes in a randomized trial and a meta-analysis (low-quality evidence); a Cochrane review and a later systematic review found no clear effect'),
        ('note', 'metabolic-support', 'Antidiabetic effects reviewed (reviews); a Cochrane review and a later systematic review found no clear effect on metabolic markers'),
        ('newpair', 'high-cholesterol', ['REF-3673'], 'Bitter melon lowered total cholesterol and triglycerides in a meta-analysis of randomized trials (short trials)'),
        ('note', 'arthritis', 'Bitter melon supplements reduced knee osteoarthritis pain and painkiller use in a single-blind randomized trial'),
        ('note', 'cancer', 'Bitter melon compounds slowed tumours in lab and animal studies (reviews)'),
    ],
    'morinda_citrifolia': [('arm', a, ['REF-0303']) for a in ('analgesic', 'anti-inflammatory', 'antidiabetic', 'antimicrobial', 'antioxidant', 'antiviral', 'immunomodulator')]
                          + [('arm', a, ['REF-0110']) for a in ('analgesic', 'anti-inflammatory', 'antidiabetic', 'antimicrobial', 'antioxidant', 'antiviral')] + [
        ('refadd', ['REF-0303']),   # safety review of noni juice: a safety reference, not activity evidence
        ('add', 'cancer', ['REF-3674']),
        ('note', 'cancer', 'Noni juice and compounds slowed cancer cells and tumours in lab and animal studies (systematic review of preclinical studies; review)'),
        ('nulladd', 'immune-support', ['REF-3675']),
        ('note', 'immune-support', 'A noni fruit polysaccharide stimulated immune cells and anti-tumour responses in mice (preclinical); in a randomized trial fermented noni polysaccharides did not significantly raise natural killer cell activity'),
        ('newpair', 'high-cholesterol', ['REF-3676'], 'Noni juice improved blood lipids vs placebo in heavy smokers in a randomized trial'),
        ('newpair', 'nausea', ['REF-3677'], 'Noni fruit extract taken before surgery reduced early postoperative nausea vs placebo in a randomized trial'),
        ('note', 'inflammation', 'Noni polysaccharides eased colitis in mice, and its compounds reduced inflammatory signals in the lab (preclinical)'),
        ('note', 'skin-irritation', 'Fermented noni eased atopic-dermatitis-like skin lesions in mice (preclinical)'),
    ],
    'nepeta_cataria': [('arm', a, ['REF-0095']) for a in ('anti-inflammatory', 'antimicrobial', 'sedative')] + [
        ('note', 'respiratory-support', 'Catnip oil relaxed airway smooth muscle in lab tissue, in line with its traditional use for cough and asthma (preclinical)'),
        ('note', 'bloating', 'Traditional carminative used for infantile colic (pharmacognosy monograph)'),
        ('note', 'infection', 'Catnip extracts and essential oil were antimicrobial in lab tests (preclinical)'),
    ],
    'nigella_sativa': [
        ('add', 'blood-sugar', ['REF-2516', 'REF-3696']),
        ('note', 'blood-sugar', 'Black seed lowered fasting blood sugar and HbA1c in meta-analyses of randomized trials'),
        ('add', 'metabolic-support', ['REF-3698', 'REF-3704']),
        ('note', 'metabolic-support', 'Black seed improved blood lipids and blood sugar in metabolic syndrome in meta-analyses, without clear effects on insulin resistance or waist size'),
        ('newpair', 'high-blood-pressure', ['REF-2513', 'REF-2512'], 'Black seed lowered systolic and diastolic blood pressure in meta-analyses of randomized trials'),
        ('newpair', 'high-cholesterol', ['REF-3697', 'REF-2516'], 'Black seed lowered total and LDL cholesterol and triglycerides in meta-analyses of randomized trials'),
        ('newpair', 'cardiovascular-support', ['REF-3703', 'REF-3704'], 'Black seed modestly improved several cardiovascular risk factors in meta-analyses of randomized trials'),
        ('add', 'inflammation', ['REF-3699']),
        ('note', 'inflammation', 'Black seed lowered CRP and TNF-alpha inflammation markers in a meta-analysis of randomized trials'),
        ('newpair', 'asthma', ['REF-3700'], 'Black seed added to usual treatment improved asthma control in a meta-analysis of trials'),
        ('newpair', 'allergy', ['REF-3701'], 'Black seed improved allergic rhinitis nasal symptoms in a meta-analysis of randomized trials (few, lower-quality studies)'),
        ('newpair', 'liver-support', ['REF-3702'], 'Black seed improved liver enzymes and fatty liver grade vs placebo in non-alcoholic fatty liver disease in a meta-analysis of randomized trials'),
        ('note', 'immune-support', 'Black seed and thymoquinone modulated immune responses in lab and animal studies (review)'),
        ('note', 'pain', 'Pain-relieving effects reported in animal studies (review)'),
        ('note', 'cancer', 'Black seed and thymoquinone slowed cancer cells in lab and animal studies (review)'),
    ],
    'ocimum_tenuiflorum': [
        ('add', 'blood-sugar', ['REF-3678']),
        ('note', 'blood-sugar', 'Holy basil leaves lowered fasting and post-meal blood sugar in type 2 diabetes in a single-blind randomized trial; a systematic review of human studies reports the same'),
        ('note', 'immune-support', 'A systematic review of human studies reports immune-enhancing effects'),
        ('note', 'cognitive-function', 'Holy basil leaf extract improved reaction time and some cognitive tests vs placebo in healthy adults in a randomized trial'),
        ('note', 'cancer', 'Tulsi and its compounds showed anticancer and radioprotective effects in lab and animal studies (reviews)'),
    ],
    'oenothera_biennis': [
        ('newpair', 'menopause', ['REF-3679', 'REF-3685'], 'Evening primrose oil reduced menopausal symptoms in a meta-analysis, and psychological symptoms in postmenopausal women in a randomized trial'),
        ('add', 'hot-flashes', ['REF-3683', 'REF-3679']),
        ('note', 'hot-flashes', 'Oral evening primrose oil reduced the intensity of hot flashes vs placebo in a randomized trial and menopausal symptoms in a meta-analysis'),
        ('add', 'pain', ['REF-3686']), ('nulladd', 'pain', ['REF-3680']),
        ('note', 'pain', 'Evening primrose oil reduced cyclical breast pain in small randomized trials, but a 2021 meta-analysis found it no better than placebo'),
        ('nulladd', 'pms', ['REF-3681', 'REF-3680']),
        ('note', 'pms', 'Cyclical breast pain improved in some trials, but reviews found evening primrose oil of little value for premenstrual syndrome itself and no better than placebo for breast pain'),
        ('add', 'eczema', ['REF-3684']),
        ('note', 'eczema', 'Oral evening primrose oil was no better than placebo for eczema in a Cochrane review; one later Indian trial reported benefit'),
        ('newpair', 'high-cholesterol', ['REF-3682'], 'Evening primrose oil lowered triglycerides and raised HDL cholesterol in people with high blood lipids in a meta-analysis of randomized trials'),
    ],
    'olea_europaea': [('arm', a, ['REF-0032']) for a in ('antidiabetic', 'antimicrobial', 'antiviral')]
                     + [('arm', a, ['REF-0299']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antiviral')] + [
        ('newpair', 'menopause', ['REF-1445'], 'Olive leaf extract improved postmenopausal symptoms vs placebo in a randomized trial'),
        ('add', 'cardiovascular-support', ['REF-3695', 'REF-3688']),
        ('note', 'cardiovascular-support', 'High-polyphenol extra virgin olive oil improved cardiovascular risk factors in a meta-analysis, and olive leaf supplements helped cardiometabolic risk factors in a GRADE-assessed meta-analysis; olive oil components reviewed (review)'),
        ('nulladd', 'blood-sugar', ['REF-3690', 'REF-3689', 'REF-3687']), ('nulladd', 'metabolic-support', ['REF-3689']),
        ('note', 'blood-sugar', 'Olive leaf extract lowered HbA1c in one randomized trial and improved insulin sensitivity in another; meta-analyses of olive leaf extract and of extra virgin olive oil found no significant effect on blood sugar'),
        ('note', 'metabolic-support', 'Olive leaf polyphenols improved insulin sensitivity in a randomized trial; a 2026 meta-analysis found no significant metabolic effects of olive leaf extract'),
        ('add', 'inflammation', ['REF-3691']), ('nulladd', 'inflammation', ['REF-3689']),
        ('note', 'inflammation', 'Regular olive oil intake lowered inflammation markers such as IL-6 in a meta-analysis; olive leaf extract showed no significant anti-inflammatory effect in a 2026 meta-analysis'),
        ('add', 'wounds', ['REF-3692']),
        ('note', 'wounds', 'Topical olive oil reduced pressure ulcers in a meta-analysis of trials; olive leaf extract was antibacterial in the lab (preclinical)'),
        ('newpair', 'oral-health', ['REF-3693'], 'Olive oil and ozonated olive oil gels improved gum health in periodontal disease in a meta-analysis (short-term)'),
        ('newpair', 'cognitive-function', ['REF-3694'], 'Extra virgin olive oil improved global cognition in older adults with mild cognitive impairment or dementia in a meta-analysis (low-certainty evidence)'),
        ('add', 'infection', ['REF-3655']),
        ('note', 'infection', 'Topical olive leaf extract helped cold sores in trials (systematic review); olive polyphenols are antimicrobial in the lab (review)'),
        ('note', 'arthritis', 'Oleocanthal from virgin olive oil has ibuprofen-like anti-inflammatory activity (review)'),
        ('note', 'cancer', 'Oleuropein from olive leaf slowed melanoma cells in the lab (preclinical)'),
        ('note', 'cold', 'Olive polyphenols are active against respiratory bacteria in lab studies (review)'),
    ],
    'ononis_arvensis': [
        ('purge', 'REF-2759'), ('purge', 'REF-3028'), ('purge', 'REF-3034'),
        ('note', 'cancer', 'Ononis isoflavone extracts slowed breast and prostate cancer cells in the lab (preclinical)'),
        ('note', 'infection', 'Leaf and root extracts were antifungal and antibacterial in lab tests (preclinical)'),
    ],
}

NOTES = {
    'melissa_officinalis': 'Deep re-sweep. REF-0134 (acute mood RCT) removed from five non-sedative actions. Muscle-spasm dropped (off-target). Held MAs REF-1194/REF-1195/REF-1197 and RCT REF-2539 wired. New pairs (owner rule): anxiety, stress, high-cholesterol, high-blood-pressure. RCT REF-3657 (T2D) supports depression/anxiety and is recorded as no-effect for sleep and blood pressure. Herpes labialis SR REF-3655 added to infection. UV-erythema RCT REF-3527 no-effect for skin (batch-7 carry). Not used: psoriasis syrup RCT 34193264 (no between-group DLQI difference reported); palpitations RCT 25680840 (no matching condition).',
    'mentha_piperita': 'Deep re-sweep. REF-0163 ("Fasciolosis in humans") and REF-0004 (rat kidney histopathology) were filed under all six actions - removed (REF-0163 deleted, REF-0004 kept as a safety reference); REF-0100 removed from anti-inflammatory/antimicrobial/antioxidant. REF-3048 retagged narrative-review. Muscle-spasm dropped (off-target). New pairs (owner rule): ibs (4 MAs + held SR; PERSUADE REF-3664 and RCT REF-3665 no-effect), nausea (PONV RCTs). Tension-headache RCT REF-3666 added; foot-bath RCT REF-3667 no-effect. Nipple-pain MA REF-3668 added to pain. Not used: lemon+peppermint menopausal massage (combination); knee-OA aromatherapy massage (massage confound).',
    'momordica_charantia': 'Deep re-sweep. Glycaemia MA REF-3671 (positive, low quality) added; 2023 SR REF-3672 ("metabolic effect cannot be determined") no-effect alongside Cochrane REF-3396. New pair (owner rule): high-cholesterol (MA REF-3673). Notes rewritten.',
    'morinda_citrifolia': 'Deep re-sweep. REF-0303 (safety review) removed from all seven actions (kept in references); REF-0110 (mouse polysaccharide study) kept only for immunomodulator. Preclinical cancer SR REF-3674 added. Fermented-polysaccharide URTI RCT REF-3675 (primary NK activity ns) no-effect for immune-support. New pairs (owner rule): high-cholesterol (smokers RCT REF-3676), nausea (PONV RCT REF-3677).',
    'nepeta_cataria': 'Deep re-sweep. REF-0095 (spasmolytic/bronchodilator oil study) removed from anti-inflammatory, antimicrobial and sedative actions (kept for digestive). Notes rewritten. No trials on PubMed.',
    'nigella_sativa': 'Deep re-sweep. Held MAs REF-2512, REF-2513 (blood pressure) and REF-2516 (T2D glucose/lipids) were never wired. Added glycaemic MA REF-3696, MetS MAs REF-3698/REF-3704, inflammation MA REF-3699. New pairs (owner rule): high-blood-pressure, high-cholesterol, cardiovascular-support (MA REF-3703), asthma (MA REF-3700), allergy (rhinitis MA REF-3701), liver-support (NAFLD MA REF-3702; no liver warning in the record). Not used: RA SR 32274788 (no change in inflammatory biomarkers); herbal mastalgia MA 36446563 (not species-specific).',
    'ocimum_tenuiflorum': 'Deep re-sweep. Single-blind diabetes RCT REF-3678 added to blood-sugar. Notes rewritten. Few trials on PubMed.',
    'oenothera_biennis': 'Deep re-sweep. New pairs (owner rule): menopause (SR/MA REF-3679 + RCT REF-3685), high-cholesterol (MA REF-3682). Hot-flash RCT REF-3683 added. Mastalgia MA REF-3680 (no better than placebo) no-effect for pain and pms; PMS review REF-3681 no-effect. Indian AD RCT REF-3684 added to eczema beside the Cochrane null. Not used: labour-induction/cervical-ripening trials (no matching condition; pregnancy use).',
    'olea_europaea': 'Deep re-sweep. REF-0032 (oleocanthal review) removed from antidiabetic/antimicrobial/antiviral; REF-0299 (olive leaf hypoglycaemia RCT) kept only for antidiabetic. Held RCT REF-1445 -> new menopause pair. CV MAs REF-3695/REF-3688 added. Blood sugar: EVOO and olive-leaf MAs REF-3690/REF-3689/REF-3687 no-effect. Inflammation: olive oil MA REF-3691 support, olive-leaf MA REF-3689 no-effect. Pressure-ulcer MA REF-3692 to wounds; herpes labialis SR REF-3655 to infection. New pairs: oral-health (periodontal MA REF-3693), cognitive-function (EVOO MA REF-3694). Not used: olive-oil lipid MA 36408701 (trivial effects) - no cholesterol pair.',
    'ononis_arvensis': 'Deep re-sweep. REF-2759 and REF-3028 study Ononis spinosa, and REF-3034 screens O. spinosa among Turkish plants - not O. arvensis; purged and deleted (the genus hepatotoxicity warning REF-2758 stays). Notes rewritten.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 11', os.path.join(HERE, 'deep', 'd11_changes.tsv'), **BIB)
