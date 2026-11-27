"""Research-deepening batch 25 (petroselinum-crispum, pimpinella-anisum, pinus-sylvestris, piper-methysticum,
plantago-lanceolata). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5570.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 25'

SPEC = [
    # parsley
    ('REF-5570', '21566309', 'parsleyteaurine', 'clinical'),
    ('REF-5571', '25648063', 'parsleyanaphylaxis', 'clinical'),
    ('REF-5572', '33953901', 'parsleysirolimus', 'clinical'),
    # Scots pine
    ('REF-5573', '38283266', 'scotspineliverinjury', 'clinical'),
    # anise
    ('REF-5574', '27815079', 'aniseoilibs', 'rct'),
    ('REF-5575', '26873392', 'aniseoilibsdepression', 'rct'),
    ('REF-5576', '25767516', 'anisedyspepsia', 'rct'),
    ('REF-5577', '32692701', 'anisepms', 'rct'),
    ('REF-5578', '24250540', 'anisehotflashes', 'rct'),
    ('REF-5579', '38292939', 'anisecovidgi', 'rct'),
    ('REF-5580', '12027075', 'aniseoccupationalallergy', 'clinical'),
    ('REF-5581', '18088024', 'aniseangioedema', 'clinical'),
    ('REF-5582', '8836339', 'aniseasthma', 'clinical'),
    ('REF-5583', '9420134', 'apiaceaespiceallergens', 'preclinical'),
    ('REF-5584', '26875753', 'aniseinfantliverfailure', 'clinical'),
    # kava
    ('REF-5585', '14706720', 'kavasleep', 'rct'),
    ('REF-5586', '25644982', 'herbalinsomniama', 'meta-analysis'),
    ('REF-5587', '25069767', 'kavadermopathyfiji', 'clinical'),
    ('REF-5588', '43031266', 'kavacutaneoustoxicity', 'clinical'),
    ('REF-5589', '40757984', 'kavadresslike', 'clinical'),
    ('REF-5590', '38839731', 'kavaneonataldermopathy', 'clinical'),
    ('REF-5591', '38829029', 'kavawithdrawal', 'clinical'),
    ('REF-5592', '40541460', 'kavawithdrawalphenobarbital', 'clinical'),
    ('REF-5593', '41885052', 'kavakratomwithdrawal', 'clinical'),
    ('REF-5594', '23259514', 'kavadriving', 'rct'),
    ('REF-5595', '26337520', 'kavadrivingreview', 'systematic-review'),
    ('REF-5596', '23348842', 'kavagadsafety', 'rct'),
    # Scots pine (lab safety)
    ('REF-5597', '11313115', 'pineoilgenotoxicity', 'preclinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== parsley
PLAN['petroselinum_crispum'] = [
    ('nulladd', 'urinary-support', ['REF-5570']),
    ('note', 'urinary-support',
     'Parsley increased urine output in rats and is a traditional diuretic (reviews); in a small 2011 crossover study in 20 '
     'healthy volunteers, drinking 1.2 L of parsley leaf tea daily for 2 weeks did not change urine volume or composition '
     'compared with bottled water'),
]
POST['petroselinum_crispum'] = [
    ('cinew', {'note': 'Allergy: a woman who used large amounts of parsley as a home remedy had near-fatal anaphylaxis '
                       '(case report).',
               'severity': 'caution', 'reference_ids': ['REF-5571']}),
    ('dcinew', {'drug_class': 'immunosuppressants', 'severity': 'caution',
                'mechanism': 'A kidney transplant recipient who ate excessive amounts of parsley had a sirolimus blood level '
                             'above the target range; the authors report it as a possible herb-drug interaction (first case '
                             'report). Sirolimus has a narrow therapeutic window and is affected by CYP3A4 and P-glycoprotein.',
                'reference_ids': ['REF-5572']}),
]
NOTES['petroselinum_crispum'] = (
    'Searched PubMed (Petroselinum crispum / P. sativum / parsley tiab: 30 HT, 10 SR, 179 SAFE hits; most were food, '
    'agriculture and lab studies), Europe PMC, ClinicalTrials.gov (14) and OpenAlex. Added: 2011 crossover of parsley leaf '
    'tea in healthy volunteers as a NULL result on urinary-support (no change in urine volume or composition); 2014 near-'
    'fatal anaphylaxis case as an allergy caution; 2021 sirolimus case as a DRAFT immunosuppressants interaction (needs '
    'owner approval). Not added: melasma cream trial (compared only with hydroquinone, an active comparator), parsley-seed '
    'bread study (kidney biomarkers only, surrogate), Mediterranean-diet and multi-herb trials (combinations), '
    'questionnaire surveys of herb use in pregnancy (no outcome).')

# ================================================================== anise
PLAN['pimpinella_anisum'] = [
    ('newpair', 'ibs', ['REF-5574'],
     'In a 2016 randomized double-blind trial in 120 people with IBS, enteric-coated anise oil capsules for 4 weeks left 75% '
     'free of IBS symptoms, versus 35% on placebo and 52.5% on peppermint oil (Colpermin)'),
    ('newpair', 'depression', ['REF-5575'],
     'In the same randomized double-blind trial in people with IBS and mild to moderate depression, anise oil lowered '
     'depression scores more than placebo or peppermint oil at 4 and 6 weeks'),
    ('newpair', 'indigestion', ['REF-5576'],
     'In a 2015 randomized double-blind trial in 107 people with functional dyspepsia (postprandial distress), anise powder '
     '3 g after meals for 4 weeks reduced symptom severity far more than a cornstarch placebo, with the benefit lasting to '
     'week 12'),
    ('newpair', 'pms', ['REF-5577'],
     'In a 2020 randomized double-blind trial in 67 students with premenstrual syndrome, anise reduced symptom severity more '
     'than placebo over two menstrual cycles'),
    ('newpair', 'hot-flashes', ['REF-5578'],
     'In a 2012 randomized double-blind trial in 72 postmenopausal women, anise capsules (330 mg three times daily) for 4 '
     'weeks cut hot flush frequency compared with placebo, and the effect lasted through 4 weeks of follow-up; results for '
     'severity were mixed'),
    ('newpair', 'diarrhea', ['REF-5579'],
     'In a 2024 randomized double-blind add-on trial in 225 adults with COVID-19 and digestive symptoms, aniseed powder for 2 '
     'weeks improved diarrhoea more often than placebo'),
    ('newpair', 'appetite-loss', ['REF-5579'],
     'In the same 2024 randomized double-blind trial in adults with COVID-19, aniseed powder improved loss of appetite more '
     'often than placebo'),
]
POST['pimpinella_anisum'] = [
    ('cinew', {'note': 'Allergy: aniseed can cause IgE-mediated allergy, including tongue swelling after an aniseed liqueur, '
                       'asthma and rhinoconjunctivitis from handling aniseed dust, and food allergy confirmed by a blinded '
                       'oral challenge. People allergic to birch or mugwort pollen, celery, or other parsley-family spices '
                       '(fennel, caraway, coriander, cumin, dill) may cross-react (case reports and lab studies).',
               'severity': 'caution', 'reference_ids': ['REF-5580', 'REF-5581', 'REF-5582', 'REF-5583']}),
    ('cinew', {'note': 'Infants: a 4-month-old given a daily homemade tea of star anise and anise for two months developed '
                       'liver failure, low blood sugar and seizures; do not give homemade herbal teas to infants (case '
                       'report; star anise was also in the tea).',
               'severity': 'caution', 'reference_ids': ['REF-5584']}),
]
NOTES['pimpinella_anisum'] = (
    'Searched PubMed (Pimpinella anisum / aniseed / anise seed / anise tiab: 79 HT, 19 SR, 171 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (15) and OpenAlex. Research-integrity check: no new reference is first- or last-authored by the '
    'flagged Tehran psychopharmacology group (author lists checked). Added NEW pairs (each from one randomized placebo-'
    'controlled trial): ibs and depression (2016 Shiraz enteric-coated anise oil trial and its depression report, same 120 '
    'patients), indigestion (2015 functional dyspepsia trial; its separate SF-36 quality-of-life report, PMID 25709650, is '
    'the same trial and was not cited twice), pms (2020), hot-flashes (2012; randomization and the between-group frequency '
    'difference confirmed in the PMC full text, severity mixed), diarrhea and appetite-loss (2024 COVID-19 add-on trial; '
    'aniseed was mixed with rock-candy powder as the vehicle; the paper reports risk ratios below 1 while describing more '
    'improvement on aniseed, so the direction is taken from the authors\' text). Added cautions: aniseed allergy (3 cases '
    'plus a cross-reactivity lab study) and an infant liver-failure case after star anise + anise tea. GAPS: lactation-'
    'support - a 2023 RCT found more pumped milk with anise tea in mothers of preterm infants, but the record cautions '
    'against medicinal use in breastfeeding (inv. 12d), so no pair; migraine - the 2019 topical anise oil pilot RCT (PMID '
    '30853645) has its abstract replaced by the author-contribution statement in PubMed, Europe PMC and OpenAlex, and the '
    'full text is closed, so the result could not be verified; menopause - a 2026 RCT reported Kupperman-index gains only '
    'within the anise group, and its between-group result is a DASS-21 composite score. Not added: 2026 Apiaceae '
    'dysmenorrhoea meta-analysis (pools anise with fennel and dill), IBS meta-analyses (only the one anise trial, already '
    'cited), six-herb dyspepsia formula, Thai multi-herb remedies (Sahastara, Thatbunjob), Menstrugole (combination), star '
    'anise (Illicium) poisoning cases and studies (other species), alcohol-free aniseed aperitif pseudohyperaldosteronism '
    'cases (caused by liquorice in the drink), feed-additive and insecticide studies.')

# ================================================================== Scots pine
PLAN['pinus_sylvestris'] = []
POST['pinus_sylvestris'] = [
    ('cinew', {'note': 'Liver: a person who used Scots pine to treat asthma developed herb-induced liver injury, the first '
                       'such case reported (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5573']}),
    ('cinew', {'note': 'Lab safety: pine-needle essential oil caused dose-dependent chromosome damage in human white blood '
                       'cells in the lab and raised mutation rates in fruit flies (lab and insect study).',
               'severity': 'info', 'reference_ids': ['REF-5597']}),
]
NOTES['pinus_sylvestris'] = (
    'Searched PubMed (Pinus sylvestris / Scots pine / Scotch pine tiab: 5 HT, 3 SR, 57 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (1) and OpenAlex (almost all forestry, ecology and provenance trials). Added: 2024 liver-injury '
    'case as a caution; 2001 needle-oil genotoxicity study (human lymphocytes in vitro, Drosophila) as an info note. GAP: '
    'blood pressure - in a 2023 study of 849 women with hypertension inhaling single essential oils during relaxation '
    'sessions (randomization not stated), Scotch pine oil had no blood-pressure-lowering effect; there is no pine blood-'
    'pressure pair to attach it to. Not added: blended essential-oil throat spray (combination), essential-oil vapour '
    'antibacterial lab studies, pollen studies (not related to use), wood, pulp and air-pollution studies. Settled for '
    'human efficacy evidence.')

# ================================================================== kava
PLAN['piper_methysticum'] = [
    ('newpair', 'insomnia', ['REF-5585'],
     'In a 2004 randomized double-blind multicentre trial in 61 people with sleep problems linked to anxiety, kava extract '
     'WS 1490 (200 mg daily) for 4 weeks improved sleep quality and feeling refreshed after sleep more than placebo; a 2015 '
     'meta-analysis of herbal medicines for insomnia (including kava) found no herb better than placebo'),
    ('nulladd', 'insomnia', ['REF-5586']),
]
POST['piper_methysticum'] = [
    ('cinew', {'note': 'Skin: regular heavy kava drinking commonly causes kava dermopathy, a dry, scaly, ichthyosis-like skin '
                       'condition (survey of more than 1,000 people in Fiji). Since kava products became widely available, '
                       'acute skin reactions soon after starting kava have also been reported, some resembling a severe '
                       'drug reaction (DRESS), and a baby born to a mother who took a kava and kratom product throughout '
                       'pregnancy had a similar rash (case series and case report).',
               'severity': 'caution', 'reference_ids': ['REF-5587', 'REF-5588', 'REF-5589', 'REF-5590']}),
    ('cinew', {'note': 'Dependence and withdrawal: after heavy daily use, stopping kava has caused severe withdrawal '
                       'resembling sedative withdrawal, with delirium, hallucinations and muscle jerking, treated in hospital '
                       'with phenobarbital (case reports; several people also took kratom).',
               'severity': 'caution', 'reference_ids': ['REF-5591', 'REF-5592', 'REF-5593']}),
    ('cinew', {'note': 'Driving: in a 2013 randomized double-blind crossover trial, a single medicinal dose of kava did not '
                       'impair simulated driving, unlike oxazepam. A 2015 systematic review found no studies of real crashes, '
                       'weak evidence of slower reaction time, and impaired simulated driving when kava was taken with '
                       'alcohol.',
               'severity': 'info', 'reference_ids': ['REF-5594', 'REF-5595']}),
    ('cinew', {'note': 'Trial safety data: in a 6-week randomized placebo-controlled trial of kava for generalised anxiety '
                       'disorder, liver tests, withdrawal and addiction measures did not differ from placebo. This does not '
                       'rule out the rare serious liver injury described above.',
               'severity': 'info', 'reference_ids': ['REF-5596']}),
]
NOTES['piper_methysticum'] = (
    'Searched PubMed (Piper methysticum / kava / kava-kava / kavalactones / WS 1490 tiab: 116 HT, 48 SR, 395 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (18) and OpenAlex. Anxiety (10) and nervous-tension were not padded (the placebo RCTs '
    'and WS 1490 meta-analysis pool trials the record already cites). Added: NEW insomnia pair (2004 WS 1490 RCT in '
    'anxiety-related sleep problems) with the 2015 herbal-insomnia meta-analysis recorded as a NULL result; skin caution '
    '(kava dermopathy and acute cutaneous toxicity); dependence/withdrawal caution; driving and trial-safety info notes. '
    'GAPS: menopause - in the 1991 WS 1490 climacteric RCT the target was anxiety, and the Kupperman-index result is not '
    'reported as a between-group difference; in the 2003 perimenopausal trial only anxiety fell more than in controls. '
    'Depression - KADSS 2009 here is the design paper; the St John\'s wort + kava pilot is a combination. Not added: acute '
    'single-dose cognition/mood studies in healthy volunteers, lab stress study (not randomized, within-group), '
    'kavalactone motivation study in military trainees, AB-free kava smoking-biomarker pilot, kava + kratom blend safety '
    'study, kava + HRT trials (combination), 1995 dopamine-antagonism letter (no abstract), 2025 suspected serotonin-'
    'syndrome case with duloxetine/venlafaxine (single suspected case; the CYP caution already covers raised drug levels), '
    'liver-injury case reports and reviews already represented by the serious liver caution.')

# ================================================================== ribwort plantain
PLAN['plantago_lanceolata'] = []
NOTES['plantago_lanceolata'] = (
    'Searched PubMed (Plantago lanceolata / ribwort plantain / ribwort / narrowleaf or English plantain tiab: 24 HT, 3 SR, '
    '69 SAFE hits), Europe PMC, ClinicalTrials.gov (3) and OpenAlex. Nothing new: the cough trials used combinations '
    '(SEDIFLU with Sisymbrium, Grintuss syrup, plantain + thyme + honey syrups) or Plantago major (other species); safety '
    'hits were mostly pollen allergy (not related to use), a 14-day rat toxicity study of a plantain syrup, and forage / '
    'livestock studies. Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r25_changes.tsv')
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
