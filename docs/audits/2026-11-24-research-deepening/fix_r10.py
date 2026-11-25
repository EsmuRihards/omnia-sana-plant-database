"""Research-deepening batch 10 (crataegus-monogyna, crocus-sativus, cuminum-cyminum, curcuma-longa, cynara-scolymus).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5287.. (reserved block)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 10'

SPEC = [
    # saffron
    ('REF-5287', '36141931', 'crocusinsomnia', 'meta-analysis'),
    ('REF-5288', '36570145', 'saffroncvriskfactors', 'meta-analysis'),
    ('REF-5289', '42186868', 'saffronpregnancy', 'narrative-review'),
    # cumin
    ('REF-5290', '42088310', 'cuminoilcognition', 'rct'),
    ('REF-5291', '42519315', 'cuminanaphylaxischild', 'clinical'),
    # turmeric
    ('REF-5292', '38560351', 'turmericoralmucositisma', 'meta-analysis'),
    ('REF-5293', '41804916', 'turmericoralmucositissr', 'systematic-review'),
    ('REF-5294', '30838707', 'turmericoralmucositis2019', 'systematic-review'),
    ('REF-5295', '39053552', 'turmericleadchromate', 'clinical'),
    ('REF-5296', '25214856', 'turmericleadbangladesh', 'clinical'),
    ('REF-5297', '38427579', 'turmericoxalatenephropathy', 'clinical'),
    ('REF-5298', '25230280', 'turmericfluindione', 'clinical'),
    # artichoke
    ('REF-5299', '35949559', 'artichokeliverenzymes', 'meta-analysis'),
    ('REF-5300', '35949557', 'artichokebloodpressure', 'meta-analysis'),
    ('REF-5301', '31484191', 'artichokehypertensionrct', 'rct'),
    # Europe PMC pass (non-flagged trials only; see saffron NOTES)
    ('REF-5302', '38408971', 'saffronvitaminelibido', 'rct'),
    ('REF-5303', '34463070', 'affronperimenopause', 'rct'),
    ('REF-5304', '31082462', 'saffroncyp1a2', 'clinical'),
    ('REF-5305', '18693099', 'saffrontabletsafety', 'clinical'),
    ('REF-5306', '35440328', 'saffronrivaroxaban', 'clinical'),
    ('REF-5307', '23733488', 'saffroncoagulation', 'clinical'),
    ('REF-5308', '34652861', 'turmericdyspepsiarct', 'rct'),
    ('REF-5309', '41877056', 'curcuminoidhotflashes', 'rct'),
    ('REF-5310', '40943181', 'curcuminmenopausesr', 'systematic-review'),
    ('REF-5311', '42247029', 'curcuminbphma', 'meta-analysis'),
    ('REF-5312', '40671058', 'curcuminpmsdysmenorrhea', 'rct'),
    ('REF-5313', '40976665', 'curcuminfatiguemenopause', 'rct'),
    ('REF-5314', '33126534', 'cynaraifgrct', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== common hawthorn
PLAN['crataegus_monogyna'] = [
    ('newpair', 'high-blood-pressure', ['REF-5282'],
     'Hawthorn (Crataegus spp.) extracts lowered systolic blood pressure by a clinically significant amount in a 2025 '
     'meta-analysis of placebo-controlled randomized trials in hypertension'),
]
POST['crataegus_monogyna'] = [('ciadd', 'Generally well tolerated. Hawthorn should not replace', ['REF-5285'])]
NOTES['crataegus_monogyna'] = (
    'Searched PubMed (Crataegus monogyna / common / single-seed hawthorn tiab; hawthorn, Crataegus, WS 1442 ti), Europe PMC, '
    'ClinicalTrials.gov (38) and OpenAlex; the hit list largely duplicates the C. laevigata search (batch 9). Same attribution '
    'as the existing cardiovascular pair (Crataegus spp. extracts; the EU monograph covers both species): NEW '
    'high-blood-pressure pair from the 2025 MA of placebo RCTs (REF-5282, held since batch 9); 2006 adverse-event SR (REF-5285) '
    'added to the safety note. C. oxyacantha trials (berry extract, ECG) stay on C. laevigata, where that name is recorded '
    'as a synonym. No C. monogyna-specific human trial found.')

# ================================================================== saffron
PLAN['crocus_sativus'] = [
    ('add', 'insomnia', ['REF-5287']),
    ('note', 'insomnia', 'Saffron improved sleep quality and duration vs placebo in a 2022 meta-analysis of randomized trials '
     '(very low to moderate quality), and a standardised extract improved subjective and objective sleep in older adults with '
     'sleep complaints; described as hypnotic in Avicenna\'s Canon (historical review)'),
    ('newpair', 'high-cholesterol', ['REF-5288'],
     'Saffron supplements lowered triglycerides, total and LDL cholesterol in a 2022 dose-response meta-analysis of randomized '
     'trials'),
    ('newpair', 'high-blood-pressure', ['REF-5288'],
     'Saffron supplements lowered systolic blood pressure in a 2022 dose-response meta-analysis of randomized trials'),
    ('newpair', 'low-libido', ['REF-5302'],
     'Saffron capsules taken with vitamin E improved overall sexual function, including libido, more than vitamin E alone '
     'in women with sexual dysfunction (triple-blind randomized trial)'),
    ('newpair', 'menopause', ['REF-5303'],
     'A standardised saffron extract (affron) eased the mood and psychological symptoms of perimenopause (anxiety and low '
     'mood) more than placebo in a randomized double-blind trial, but not hot flushes or physical symptoms'),
]
POST['crocus_sativus'] = [
    ('ciadd', 'Culinary use is entirely safe', ['REF-5289']),
    ('cinew', {'note': 'Medicines: drinking saffron infusion for six days modestly reduced the activity of CYP1A2, a liver enzyme '
                       'that clears some drugs (by about 14%, mainly in men); the authors judged meaningful drug interactions '
                       'unlikely, except possibly with CYP1A2-cleared drugs in men (study in healthy volunteers).',
               'severity': 'info', 'reference_ids': ['REF-5304']}),
    ('cinew', {'note': 'In placebo-controlled safety studies in healthy volunteers, saffron tablets of 200 to 400 mg a day for a '
                       'week were well tolerated and did not change clotting factors or clotting times; 400 mg lowered standing '
                       'blood pressure and slightly changed some blood counts and kidney markers, all within normal ranges.',
               'severity': 'info', 'reference_ids': ['REF-5305', 'REF-5307']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'A man taking the anticoagulant rivaroxaban developed nosebleeds and bleeding gums after starting '
                             'a saffron supplement (case report); a placebo-controlled study in healthy volunteers found no effect '
                             'of 200 to 400 mg saffron a day for a week on clotting factors or clotting times.',
                'reference_ids': ['REF-5306', 'REF-5307']}),
]
NOTES['crocus_sativus'] = (
    'Searched PubMed (Crocus sativus / saffron tiab; crocin, safranal ti: 384 HT, 141 SR, 606 SAFE hits; SR/MA read in depth), '
    'Europe PMC, ClinicalTrials.gov (32) and OpenAlex. Depression (10), anxiety, PMS, period pain, metabolic and blood-sugar '
    'pairs are already MA-backed and were not padded. Added: 2022 insomnia MA to insomnia; NEW high-cholesterol and '
    'high-blood-pressure pairs from the 2022 cardiovascular-risk dose-response MA; 2026 integrative pregnancy review (low '
    'doses promising for labour, excessive intake risky) to the pregnancy caution. Not added: erectile-dysfunction MA 2018 '
    '(not low libido: near-miss, inv. 12c/f), crocin lipid MA 2025 (inconclusive), saffron + fenugreek glucose MA '
    '(combined), umbrella reviews of depression (already at 10). Europe PMC pass: NEW low-libido pair (2024 Tabriz '
    'triple-blind RCT, saffron + vitamin E vs vitamin E alone, libido domain improved) and NEW menopause pair (2021 affron '
    'RCT in perimenopause: psychological symptoms improved, vasomotor and somatic did not); CYP1A2 phenotyping study 2019 '
    'and two healthy-volunteer safety studies (2008 tablets, 2014 coagulation) as info notes; DRAFT anticoagulant '
    'interaction from a 2022 rivaroxaban bleeding case report, stated with the negative 2014 coagulation study (needs owner '
    'sign-off). HELD pending owner decision: a 2026 data-integrity analysis (Research Integrity and Peer Review, PMID '
    '42288935) found that 223 RCTs from one psychopharmacology research group were unlikely to have been randomised and '
    'cautioned against using them; it estimates the group produced about a third of saffron-vs-placebo trials. Three '
    'candidate trials share that group\'s senior author and were not added: hot flushes in postmenopausal depression (PMID '
    '29332222; the only positive hot-flush trial, so no hot-flushes pair), fluoxetine-induced sexual dysfunction in women '
    '(23280545; desire not improved) and female sexual dysfunction (36186931); nor the 2019 sexual-dysfunction MA pooling '
    'such trials (31516855). Existing pairs citing that group are unchanged pending the owner. Not added: preprints '
    '(Safr\'Inside menopause and PMS RCTs 2026, glycaemic MA 2026), crocin-only trials outside the vocabulary.')

# ================================================================== cumin
PLAN['cuminum_cyminum'] = [
    ('newpair', 'cognitive-function', ['REF-5290'],
     'Daily cuminaldehyde-rich cumin essential oil improved cognitive function in healthy older Japanese adults in a '
     'randomized double-blind trial'),
]
POST['cuminum_cyminum'] = [('ciadd', 'Allergy risk: cumin can trigger allergic reactions', ['REF-5291'])]
NOTES['cuminum_cyminum'] = (
    'Searched PubMed (Cuminum cyminum tiab, cumin ti), Europe PMC, ClinicalTrials.gov (34) and OpenAlex; "black cumin" '
    '(Nigella sativa) and Bunium persicum hits excluded as other species. Metabolic (9) and cholesterol (8) are already '
    'MA-backed. Added: NEW cognitive-function pair (2026 Japanese placebo RCT, UMIN000050328); 2026 paediatric cumin '
    'anaphylaxis case and review to the allergy note. Dead end: 2015 double-blind RCT in NASH found no difference from placebo '
    '(no liver pair exists). Not added: IBS case series (uncontrolled), cumin + lime, cumin + cinnamon and other combinations, '
    'saliva substitute with ginger, 1997 anaphylaxis letter (no abstract).')

# ================================================================== turmeric
PLAN['curcuma_longa'] = [
    ('newpair', 'oral-health', ['REF-5292', 'REF-5293', 'REF-5294'],
     'Turmeric and curcumin, mostly as a gel or mouthwash, reduced the severity and pain of radiotherapy-induced mouth sores '
     '(oral mucositis) in head and neck cancer in a 2024 meta-analysis and systematic reviews'),
    ('add', 'indigestion', ['REF-5308']),
    ('note', 'indigestion', 'Turmeric (Curcuma longa) capsules eased the pain and other symptoms of functional dyspepsia more '
     'than placebo, and about as well as omeprazole, in a randomized double-blind trial; traditional remedy for dyspepsia '
     '(WHO monograph)'),
    ('newpair', 'hot-flashes', ['REF-5309'],
     'Curcuminoids, turmeric\'s signature compounds (1,000 mg a day), reduced how often hot flushes occurred vs placebo in a '
     'small pilot randomized trial in postmenopausal women; a 2025 systematic review found the trial evidence on hot flushes '
     'conflicting'),
    ('nulladd', 'hot-flashes', ['REF-5310']),
    ('newpair', 'prostate-support', ['REF-5311'],
     'Curcumin, turmeric\'s signature compound, added to standard prostate medicines improved urinary symptom scores vs '
     'placebo in men with benign prostatic hyperplasia in a 2026 meta-analysis of randomized and non-randomized studies'),
    ('newpair', 'pms', ['REF-5312'],
     'Curcumin capsules (turmeric\'s signature compound) reduced premenstrual symptoms more than placebo in a double-blind '
     'randomized trial in students'),
    ('newpair', 'menstrual-cramps', ['REF-5312'],
     'Curcumin capsules (turmeric\'s signature compound) reduced period pain more than placebo in the second and third '
     'cycles of a double-blind randomized trial in students'),
    ('newpair', 'fatigue', ['REF-5313'],
     'Curcumin (turmeric\'s signature compound, 1 g a day) reduced fatigue and improved musculoskeletal health vs placebo in '
     'postmenopausal women in a double-blind randomized trial'),
]
POST['curcuma_longa'] = [
    ('cinew', {'note': 'Contamination: turmeric powder sold in parts of South Asia has been adulterated with lead chromate to '
                       'brighten its colour, with lead levels high enough to raise children\'s blood lead; contaminated '
                       'turmeric was a likely lead source for children in rural Bangladesh. Buy from reputable sources.',
               'severity': 'caution', 'reference_ids': ['REF-5295', 'REF-5296']}),
    ('cinew', {'note': 'Kidneys: a man taking turmeric supplements long-term was found to have kidney failure from oxalate '
                       'nephropathy (oxalate crystals in the kidney) (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5297']}),
    ('dciadd', 'anticoagulants-antiplatelets', ['REF-5298']),
]
NOTES['curcuma_longa'] = (
    'Searched PubMed (Curcuma longa tiab; turmeric, curcumin, curcuminoids ti: 1,467 HT, 507 SR, 4,120 SAFE hits; SR/MA and '
    'safety read in depth), Europe PMC, ClinicalTrials.gov (248) and OpenAlex. Arthritis, inflammation, blood sugar, '
    'cholesterol, BP, IBD, psoriasis and depression are already MA-backed and were not padded. Added: NEW oral-health pair '
    '(2024 oral-mucositis MA, 2026 and 2019 SRs); lead-chromate adulteration (South Asia 2024; Bangladesh 2014) as a new '
    'caution; oxalate nephropathy case 2024 as a new caution; a probable fluindione (vitamin K antagonist) INR-rise case to '
    'the approved anticoagulant interaction (its only source was a rat study; text unchanged). NOT ADDED: liver-support '
    '(MASLD MAs) because the record carries a serious liver-injury warning (inv. 12d); periodontitis adjunct MAs (local '
    'delivery, mixed photodynamic designs); oral lichen planus vs corticosteroids (active comparator); earlier PMS / '
    'dysmenorrhoea trials whose outcomes were sleep, cognition, immunity or vitamin D; further liver-injury case reports '
    '(the serious warning already has three case series). Europe PMC pass added: 2022 Thai placebo RCT in functional '
    'dyspepsia (indigestion was resting on the WHO monograph alone); NEW hot-flashes pair (2026 curcuminoid pilot RCT, with '
    'the 2025 menopause SR as no-effect since it found hot-flush results conflicting); NEW prostate-support (2026 BPH MA, '
    'curcumin as add-on); NEW pms and menstrual-cramps (2025 Tabriz placebo RCT, PSST and pain VAS); NEW fatigue (2025 BMJ '
    'Open placebo RCT in postmenopausal women). Not added: 2026 Japanese cognition RCT (2 of 35 endpoints significant), '
    'chemotherapy-neuropathy RCTs (sensory symptoms, not pain: near-miss), curcumin vs triamcinolone for mouth ulcers '
    '(active comparator), preprints.')

# ================================================================== artichoke
PLAN['cynara_scolymus'] = [
    ('add', 'liver-support', ['REF-5299']),
    ('add', 'high-blood-pressure', ['REF-5300', 'REF-5301']),
    ('note', 'high-blood-pressure', 'Artichoke lowered systolic and diastolic blood pressure in meta-analyses of randomized trials, '
     'and artichoke powder lowered systolic pressure in a placebo-controlled trial in people with hypertension'),
    ('add', 'blood-sugar', ['REF-5314']),
    ('note', 'blood-sugar', 'Artichoke products lowered fasting blood sugar in a meta-analysis of randomized trials, and a '
     'standardised artichoke extract improved fasting glucose and HbA1c vs placebo in overweight people with impaired '
     'fasting glucose (randomized trial)'),
]
NOTES['cynara_scolymus'] = (
    'Searched PubMed (Cynara scolymus / C. cardunculus / artichoke leaf / artichoke extract tiab, artichoke ti), Europe PMC, '
    'ClinicalTrials.gov (37) and OpenAlex. Added: 2022 liver-enzyme MA (ALT and AST fell) to liver-support; 2022 BP '
    'dose-response MA and the 2020 placebo RCT in hypertension to high-blood-pressure. Not added: anthropometric MA 2021 '
    '(waist circumference only; no metabolic pair created), bergamot, red yeast rice, ginger and other combinations, '
    'Jerusalem artichoke (a different plant), NAFLD network MAs (artichoke not separable). Europe PMC pass: 2020 placebo '
    'RCT of a standardised Cynara scolymus extract in impaired fasting glucose added to blood-sugar.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r10_changes.tsv')
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
