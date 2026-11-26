"""Research-deepening batch 21 (matricaria-chamomilla, melissa-officinalis, mentha-piperita, momordica-charantia,
morinda-citrifolia). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5483.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 21'

SPEC = [
    # chamomile
    ('REF-5483', '37336118', 'chamomileflatulence', 'rct'),
    ('REF-5484', '37926605', 'chamomilepdph', 'rct'),
    ('REF-5485', '33038782', 'chamomilerhinosinusitis', 'rct'),
    ('REF-5486', '39283344', 'chamomileradiodermatitisgel', 'rct'),
    ('REF-5487', '40374153', 'chamomileadverseevents', 'systematic-review'),
    ('REF-5488', '19050375', 'chamomileteaanaphylaxis', 'clinical'),
    ('REF-5489', '37730613', 'chamomilecoagulation', 'rct'),
    ('REF-5490', '38300838', 'chamomilecoagulationacute', 'rct'),
    # lemon balm
    ('REF-5491', '30548118', 'lemonbalmglycemic', 'rct'),
    ('REF-5492', '30681971', 'lemonbalmproductdiabetes', 'rct'),
    ('REF-5493', '29844788', 'lemonbalmdysmenorrhea', 'rct'),
    ('REF-5494', '29369810', 'lemonbalmpms', 'rct'),
    ('REF-5495', '29796033', 'lemonbalmsexualdesire', 'rct'),
    ('REF-5496', '25870482', 'lemonbalmwithdrawal', 'clinical'),
    ('REF-5497', '38461950', 'lemonbalmtoxicology', 'preclinical'),
    # peppermint
    ('REF-5498', '41311590', 'peppermintmenstrual', 'systematic-review'),
    ('REF-5499', '30087294', 'peppermintoilcognition', 'clinical'),
    ('REF-5500', '40189738', 'pepperminttea', 'rct'),
    ('REF-5501', '29850445', 'peppermintpregnancynausea', 'rct'),
    ('REF-5502', '39172635', 'peppermintpatchtesting', 'clinical'),
    ('REF-5503', '36918212', 'peppermintcapsulesallergy', 'clinical'),
    ('REF-5504', '26784183', 'berlinherbliverinjury', 'clinical'),
    ('REF-5505', '28011360', 'peppermintteaenzymes', 'clinical'),
    # bitter melon
    ('REF-5506', '39079610', 'bittermelonanthropometric', 'meta-analysis'),
    ('REF-5507', '37808602', 'bittermelonliverinjury', 'clinical'),
    ('REF-5508', '41700226', 'asowosiliverinjury', 'clinical'),
    ('REF-5509', '34232214', 'bittermelonnephritis', 'clinical'),
    ('REF-5510', '34569860', 'bittermelonpazopanib', 'clinical'),
    # noni
    ('REF-5511', '15756098', 'nonihepatitis', 'clinical'),
    ('REF-5512', '16094725', 'nonihepatotoxicitytwo', 'clinical'),
    ('REF-5513', '21119544', 'nonihepatotoxicityboy', 'clinical'),
    ('REF-5514', '23467452', 'noniphenobarbital', 'clinical'),
    ('REF-5515', '41805431', 'nonitopicalliverinjury', 'clinical'),
    ('REF-5516', '20443518', 'nonisafetystudy', 'rct'),
    ('REF-5517', '10676732', 'nonihyperkalemia', 'clinical'),
    ('REF-5518', '22580040', 'noniranitidine', 'clinical'),
    ('REF-5519', '26179835', 'noniphenytoin', 'clinical'),
    ('REF-5520', '41560756', 'phenytoinfoodherb', 'systematic-review'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== chamomile
PLAN['matricaria_chamomilla'] = [
    ('add', 'bloating', ['REF-5483']),
    ('note', 'bloating',
     'Chamomile drops reduced flatulence after laparoscopic gallbladder surgery compared with placebo (randomized '
     'triple-blind trial); traditional use for minor stomach and gut complaints such as bloating (EU herbal monograph)'),
    ('newpair', 'headache', ['REF-5484'],
     'A chamomile ointment lowered the rate of headache after spinal anaesthesia (post-dural-puncture headache) at 6 and 12 '
     'hours compared with placebo in women having a caesarean section (randomized double-blind trial)'),
    ('newpair', 'sinusitis', ['REF-5485'],
     'Chamomile extract nasal drops improved chronic rhinosinusitis symptoms, quality of life and nasal examination findings '
     'more than placebo (randomized double-blind trial)'),
    ('nulladd', 'skin-irritation', ['REF-5486']),
    ('note', 'skin-irritation',
     'Traditional use for minor skin inflammation such as sunburn (EU herbal monograph); an extract was no better than its '
     'base cream for UV skin redness in a randomized trial, and adding chamomile to a liposomal gel did not reduce '
     'radiation dermatitis in breast cancer radiotherapy (randomized double-blind trial)'),
]
POST['matricaria_chamomilla'] = [
    ('ciadd', 'Rare allergic reactions in individuals sensitive to the Asteraceae family', ['REF-5488']),
    ('cinew', {'note': 'Side effects: in a 2025 systematic review of 72 trials in which 2,896 people took chamomile, side effects '
                       'were uncommon and mild, mainly digestive upset and drowsiness. No allergic reactions occurred in the '
                       'trials, but case reports describe allergic reactions including anaphylaxis (for example a man who '
                       'reacted an hour after a cup of chamomile tea). Data on use in pregnancy and breastfeeding are '
                       'insufficient.',
               'severity': 'info', 'reference_ids': ['REF-5487', 'REF-5488']}),
    ('cinew', {'note': 'Blood clotting: in a randomized placebo-controlled crossover study in 12 healthy volunteers, a week of '
                       'chamomile tea (9 bags a day) or extract capsules did not change clotting tests; in another small '
                       'crossover study a single cup slightly lengthened prothrombin time (by 0.7 seconds, below a 10% '
                       'threshold for clinical relevance). The volunteers were not taking warfarin.',
               'severity': 'info', 'reference_ids': ['REF-5489', 'REF-5490']}),
]
NOTES['matricaria_chamomilla'] = (
    'Searched PubMed (Matricaria chamomilla / recutita, Chamomilla recutita, German chamomile tiab; chamomile, camomile ti: '
    '186 HT, 41 SR, 237 SAFE hits), Europe PMC, ClinicalTrials.gov (70) and OpenAlex. Strong pairs (anxiety 9, oral health '
    '9, insomnia 8, pain 8) were not padded. Added: 2023 triple-blind RCT (post-surgery flatulence) to bloating; NEW '
    'headache pair (2024 double-blind RCT, post-dural-puncture headache prevention); NEW sinusitis pair (2021 double-blind '
    'nasal-drop RCT in chronic rhinosinusitis); 2025 liposomal-gel radiodermatitis RCT as a no-effect study on '
    'skin-irritation; 2025 adverse-event SR and a 2009 anaphylaxis case; two randomized clotting studies (2023, 2024) as '
    'an info note. The approved anticoagulant interaction (warfarin case) is unchanged. Not added: 2024 post-ear-surgery '
    'nausea RCT (different only at 4 h), 2025 musculoskeletal-pain MA (pools the knee OA trial already cited), 2017 '
    'topical-oil enuresis RCT (no vocab condition for bedwetting), mastalgia, carpal tunnel, PCOS, phlebitis and '
    'neutropenia trials (no vocab condition), compound chamomile-lidocaine gels, Iberogast/STW 5 and other combinations, '
    'vs-clotrimazole and vs-cabergoline trials (active comparators), 2020 oral provocation study (no systemic dermatitis '
    'from chamomile tea; flare-ups equal on placebo), ductus arteriosus letter and retracted dermatitis paper (no abstract / '
    'retracted), Roman chamomile and globe chamomile reports (other species). Integrity hold: no flagged-group authors.')

# ================================================================== lemon balm
PLAN['melissa_officinalis'] = [
    ('newpair', 'blood-sugar', ['REF-5491'],
     'A lemon balm extract (700 mg a day for 12 weeks) lowered fasting blood sugar and HbA1c compared with placebo in type 2 '
     'diabetes (randomized double-blind trial); a lemon-balm-based product did not change blood sugar compared with control '
     'in another randomized trial'),
    ('nulladd', 'blood-sugar', ['REF-5492']),
    ('add', 'menstrual-cramps', ['REF-5493']),
    ('note', 'menstrual-cramps',
     'Lemon balm capsules taken for 3 days from the start of bleeding eased period pain more than placebo in students with '
     'primary dysmenorrhoea (randomized double-blind trial)'),
    ('newpair', 'pms', ['REF-5494'],
     'Lemon balm capsules (1,200 mg a day over three menstrual cycles) improved psychosomatic symptoms, anxiety, sleep '
     'problems and social functioning compared with placebo in teenage girls with premenstrual syndrome (randomized trial)'),
    ('newpair', 'low-libido', ['REF-5495'],
     'Lemon balm extract (500 mg twice a day for 4 weeks) improved sexual desire and overall sexual function compared with '
     'placebo in women with low sexual desire (randomized double-blind trial)'),
]
POST['melissa_officinalis'] = [
    ('cinew', {'note': 'Stopping it: a 30-year-old developed restlessness, tremor, poor concentration and sweating after stopping '
                       'long-term lemon balm use, which the authors interpreted as possible withdrawal (case report).',
               'severity': 'info', 'reference_ids': ['REF-5496']}),
    ('cinew', {'note': 'Toxicology: in guideline tests an aqueous lemon balm leaf extract was not genotoxic, and rats fed it for '
                       '90 days showed no treatment-related adverse effects (lab and animal studies).',
               'severity': 'info', 'reference_ids': ['REF-5497']}),
]
NOTES['melissa_officinalis'] = (
    'Searched PubMed (Melissa officinalis / lemon balm / Cyracos tiab: 124 HT, 34 SR, 161 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (25) and OpenAlex. INTEGRITY HOLD checked: no new reference is first- or last-authored by the '
    'flagged Tehran psychopharmacology group. Anxiety (9), depression (9) and cholesterol (9) were not padded. Added: NEW '
    'blood-sugar pair (2019 double-blind placebo RCT, FBS and HbA1c) with a 2019 lemon-balm-product RCT recorded as no '
    'effect; 2017 double-blind dysmenorrhoea RCT to menstrual-cramps (replacing the inferred note); NEW pms pair (2018 '
    'placebo RCT in adolescents, GHQ outcomes) and NEW low-libido pair (2018 double-blind placebo RCT, FSFI); a withdrawal '
    'case and 2024 guideline toxicology as info notes. GAP: cognitive function - the 2022 and 2020 Japanese rosmarinic-acid '
    'extract RCTs found no cognitive difference vs placebo, and the 2026 Zensera acute RCT missed its primary calmness '
    'outcome. Not added: 2021 premature-beats tea RCT and 2015 palpitation RCT (no matching condition, as before); 2018 '
    'menstrual bleeding/systemic symptoms RCT (secondary outcomes only); 2026 Melissa phospholipid sleep study (dose '
    'comparison; insomnia already 6); valerian, Nepeta, Echium, Ze 185 and other combinations; vs-citalopram, '
    'vs-fluoxetine and vs-clonidine trials (active comparators); AV-block case with a seven-ingredient product; homeopathic '
    'preparations.')

# ================================================================== peppermint
PLAN['mentha_piperita'] = [
    ('add', 'menstrual-cramps', ['REF-5498']),
    ('note', 'menstrual-cramps',
     'Peppermint reduced period pain in a 2025 systematic review of five randomized trials in primary dysmenorrhoea and '
     'premenstrual syndrome (two of the trials were judged low quality)'),
    ('add', 'cognitive-function', ['REF-5499', 'REF-5500']),
    ('note', 'cognitive-function',
     'Peppermint essential oil capsules improved performance on demanding attention and arithmetic tasks and reduced mental '
     'fatigue compared with placebo in healthy adults (placebo-controlled crossover study), and a cup of peppermint tea '
     'improved cognitive test performance more than placebo (small randomized single-blind trial); peppermint extract '
     'inhibited acetylcholinesterase in vitro (preclinical)'),
    ('nulladd', 'nausea', ['REF-5501']),
    ('note', 'nausea',
     'Inhaled peppermint oil reduced nausea and vomiting after surgery in randomized trials; for nausea and vomiting in '
     'pregnancy, peppermint oil inhalation was no better than placebo (single-blind randomized trial)'),
]
POST['mentha_piperita'] = [
    ('cinew', {'note': 'Allergy: peppermint oil caused allergic contact dermatitis in 0.6% of 28,128 patients patch-tested in '
                       'North America (2009-2020), mostly on the face and lips, from toothpaste and other oral-care products, '
                       'foods and lip products. Some peppermint oil capsules (for example Colpermin) contain peanut (arachis) '
                       'oil, which caused a whole-body rash in a woman with soya allergy (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5502', 'REF-5503']}),
    ('cinew', {'note': 'Liver: in a Berlin hospital surveillance study of 198 cases of liver injury (2002-2011), peppermint was '
                       'judged a possible cause in one.',
               'severity': 'info', 'reference_ids': ['REF-5504']}),
    ('cinew', {'note': 'Medicines: six days of peppermint tea (2 g of leaf twice a day) slightly lowered the activity of the '
                       'drug-metabolising enzyme NAT2 in 9 healthy volunteers, with no significant effect on CYP1A2, CYP2A6, '
                       'xanthine oxidase or UGT1A1/1A6.',
               'severity': 'info', 'reference_ids': ['REF-5505']}),
]
NOTES['mentha_piperita'] = (
    'Searched PubMed (Mentha piperita / Mentha x piperita / peppermint tiab: 390 HT, 93 SR, 420 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (100) and OpenAlex. IBS (10) and pain (8) were not padded (incl. a 2026 paediatric IBS RCT). '
    'Added: 2025 SR of five RCTs to menstrual-cramps (replacing the inferred note); 2018 placebo-controlled crossover '
    '(oil capsules; randomisation not stated, tagged clinical) and 2025 randomized single-blind tea RCT to '
    'cognitive-function; 2018 single-blind placebo RCT in pregnancy nausea as a no-effect study on nausea; allergy caution '
    '(NACDG patch-test series; peanut-oil capsule case); Berlin HILI surveillance and 2017 peppermint-tea enzyme study as '
    'info notes. Not added: functional dyspepsia (Menthacarin and other peppermint + caraway combinations), 2016 '
    'chronic-pruritus oil study (randomisation not stated), 2018 Cochrane PONV and 2024 cancer-nausea aromatherapy MAs (not '
    'peppermint-specific pooled; nausea already 6), colonoscopy antispasmodic trials (procedural), vs-lidocaine migraine '
    'trial (active comparator), lemon/ginger/lavender blends, menthol-only studies (not species-specific), 2025 '
    'hepatotoxicity letter, 2005 chemical-burn report and cheilitis letters (no abstract).')

# ================================================================== bitter melon
PLAN['momordica_charantia'] = [
    ('nulladd', 'metabolic-support', ['REF-5506']),
    ('note', 'metabolic-support',
     'Antidiabetic effects reviewed (reviews); a Cochrane review and a later systematic review found no clear effect on '
     'metabolic markers, and a 2024 meta-analysis of 10 randomized trials found no effect on body weight, BMI, waist size or '
     'body fat'),
]
POST['momordica_charantia'] = [
    ('cinew', {'note': 'Liver: a man who drank large amounts of "asowosi" (bitter melon) cleansing tea developed severe liver '
                       'injury rated highly probable on a causality scale, and another man had biopsy-supported herb-induced '
                       'liver injury after weeks of herbal remedies including asowosi; both recovered (case reports).',
               'severity': 'caution', 'reference_ids': ['REF-5507', 'REF-5508']}),
    ('cinew', {'note': 'Kidneys: a woman who took a pure bitter melon extract for 7 months developed biopsy-proven acute '
                       'interstitial nephritis, which improved after stopping it and steroid treatment (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5509']}),
    ('dcinew', {'drug_class': 'chemotherapy-agents', 'severity': 'caution',
                'mechanism': 'A man on long-term pazopanib (a cancer drug) developed acute pancreatitis four days after starting '
                             'bitter melon extract; it settled after both were stopped, and pazopanib was later restarted '
                             'without recurrence, suggesting an interaction (case report).',
                'reference_ids': ['REF-5510']}),
]
NOTES['momordica_charantia'] = (
    'Searched PubMed (Momordica charantia / bitter melon / bitter gourd / karela tiab: 93 HT, 31 SR, 252 SAFE hits; many '
    'were crop-science papers), Europe PMC, ClinicalTrials.gov (29) and OpenAlex. Blood sugar (8, with nulls) and '
    'cholesterol (7) were not padded (2025 prediabetes RCT and 2018 Japanese lipid RCT not added; the lipid MA already '
    'pools such trials). Added: 2024 anthropometric MA as a no-effect study on metabolic-support; liver caution (2023 '
    'RUCAM highly probable asowosi case; 2026 biopsy-supported case); kidney caution (2021 pure-extract interstitial '
    'nephritis); DRAFT chemotherapy-agents interaction (2022 pazopanib pancreatitis case). Not added: 2017 nephritis case '
    'with Hyponidd (multi-herb tablet), red yeast rice and other combinations, in silico interaction studies, 2022 obesity '
    'pilot (metabolic-support already has nulls).')

# ================================================================== noni
PLAN['morinda_citrifolia'] = []
POST['morinda_citrifolia'] = [
    ('cinew', {'note': 'Liver: acute hepatitis has been reported in several people drinking noni juice, after three weeks to a '
                       'few months of use, some confirmed by biopsy; one man needed a liver transplant, a 14-year-old boy was '
                       'affected, and most recovered after stopping (case reports). Liver injury has also followed months of '
                       'a noni-containing skin cream. A 28-day double-blind safety study of a commercial noni juice in 96 '
                       'healthy volunteers found no adverse effects.',
               'severity': 'caution',
               'reference_ids': ['REF-5511', 'REF-5512', 'REF-5513', 'REF-5514', 'REF-5515', 'REF-5516']}),
    ('cinew', {'note': 'Kidneys and potassium: noni juice contains about as much potassium as orange or tomato juice (56 '
                       'mmol/L); a man with chronic kidney disease developed high blood potassium while drinking it despite a '
                       'low-potassium diet (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5517']}),
    ('cinew', {'note': 'Medicines: a noni fruit extract taken 30 minutes before ranitidine increased how much ranitidine reached '
                       'the blood in a randomized crossover study in 20 healthy volunteers, consistent with faster stomach '
                       'emptying.',
               'severity': 'info', 'reference_ids': ['REF-5518']}),
    ('dcinew', {'drug_class': 'anticonvulsants', 'severity': 'caution',
                'mechanism': 'A man on long-term phenytoin had persistently low, sometimes undetectable, phenytoin levels and '
                             'poor seizure control while drinking noni juice daily (case report; the authors suggest faster '
                             'breakdown by CYP2C9), and a 2025 systematic review of phenytoin food and herb interactions '
                             'advises avoiding the combination.',
                'reference_ids': ['REF-5519', 'REF-5520']}),
]
NOTES['morinda_citrifolia'] = (
    'Searched PubMed (Morinda citrifolia / noni tiab: 64 HT, 12 SR, 136 SAFE hits; "noni" also matched "non-IID" machine '
    'learning papers), Europe PMC, ClinicalTrials.gov (10) and OpenAlex. Added: liver caution (2005 biopsy-confirmed case, '
    '2005 two cases incl. a transplant, 2011 boy, 2013 case with phenobarbital, 2026 topical-cream case; balanced by the '
    '2009 28-day double-blind safety study of TAHITIAN NONI juice); potassium caution (2000 hyperkalaemia case in chronic '
    'kidney disease); ranitidine absorption study as an info note; DRAFT anticonvulsants interaction (2015 phenytoin case + '
    '2025 SR). No-effect study recorded here only (no pair exists): the 2013 double-blind placebo RCT of noni capsules in '
    'primary dysmenorrhoea found no reduction in pain or bleeding. Not added: 2018 diabetes juice study (uncontrolled), '
    'dental irrigant and root-canal studies (no vocab condition), 2006 Digestion case (disputed: interferon-beta also '
    'given), 2015 case with Herbalife products (confounded), 2008 and 2007 hepatotoxicity letters and the 2004 warfarin-'
    'resistance letter (no abstract; the record\'s general caution already mentions warfarin), rebuttal articles (2006 "not '
    'hepatotoxic" review, 2017 letter), papaya and other combinations.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r21_changes.tsv')
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
