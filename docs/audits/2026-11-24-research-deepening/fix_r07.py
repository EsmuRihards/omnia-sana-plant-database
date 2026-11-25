"""Research-deepening batch 7 (cannabis-sativa, capsella-bursa-pastoris, capsicum-annuum, carum-carvi,
centaurium-erythraea). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5231.. (reserved)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 7'

SPEC = [
    # hemp / cannabis
    ('REF-5231', '26103030', 'cannabinoidsmedicaluse', 'meta-analysis'),
    ('REF-5232', '36716312', 'cannabinoidspaintsa', 'meta-analysis'),
    ('REF-5233', '31959586', 'cannabinoidscancerpain', 'meta-analysis'),
    ('REF-5234', '37519000', 'nabiximolsmsspasticity', 'meta-analysis'),
    ('REF-5235', '38924898', 'cbdanxietydisorders', 'meta-analysis'),
    ('REF-5236', '31341892', 'cannabinoidscachexia', 'meta-analysis'),
    ('REF-5237', '28000146', 'cannabinoidhyperemesis', 'systematic-review'),
    ('REF-5238', '40527600', 'cannabiscardiovascular', 'meta-analysis'),
    ('REF-5239', '31563981', 'cannabispsychosis', 'systematic-review'),
    ('REF-5240', '32268347', 'cbdadverseeffects', 'meta-analysis'),
    ('REF-5241', '38868665', 'cannabinoiddrugdrug', 'systematic-review'),
    ('REF-5242', '38655747', 'cbdthccyp450', 'systematic-review'),
    ('REF-5243', '40589083', 'cannabinoidbirthoutcomes', 'systematic-review'),
    # chili
    ('REF-5244', '36938807', 'capsaicinweightloss', 'meta-analysis'),
    ('REF-5245', '36513480', 'capsinoidsbodycomposition', 'meta-analysis'),
    ('REF-5246', '42237588', 'capsaicinpatchhiv', 'meta-analysis'),
    # caraway
    ('REF-5247', '24319489', 'carawayobesitywomen', 'rct'),
    ('REF-5248', '24638976', 'carawaysafetyrct', 'rct'),
    ('REF-5249', '24741485', 'carawayantitubercular', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== hemp / cannabis
PLAN['cannabis_sativa'] = [
    ('add', 'pain', ['REF-5231', 'REF-5232']),
    ('nulladd', 'pain', ['REF-5233']),
    ('note', 'pain', 'A full-spectrum cannabis extract reduced chronic low back pain in a phase 3 trial, and topical hemp seed '
     'oil reduced knee osteoarthritis pain (randomized trials); meta-analyses found cannabinoid medicines reduce chronic pain '
     'modestly, with more side effects, and adding them to opioids did not ease cancer pain'),
    ('newpair', 'muscle-spasm', ['REF-5234', 'REF-5231'],
     'Nabiximols, a cannabis extract mouth spray containing THC and CBD, reduced multiple sclerosis spasticity resistant to '
     'standard treatment in a meta-analysis, and a broader meta-analysis found moderate-quality evidence for cannabinoids in '
     'spasticity'),
    ('newpair', 'insomnia', ['REF-5231', 'REF-5232'],
     'Cannabinoid medicines improved sleep in meta-analyses of randomized trials (low-quality evidence; mostly in people with '
     'chronic pain)'),
    ('newpair', 'anxiety', ['REF-5235'],
     'Cannabidiol (CBD), the non-intoxicating cannabis compound, reduced anxiety in a meta-analysis of small trials in anxiety '
     'disorders (compound evidence)'),
    ('newpair', 'appetite-loss', ['REF-5236', 'REF-5231'],
     'Cannabinoids increased appetite in people with cancer in a meta-analysis, though quality of life fell, and were linked to '
     'weight gain in HIV infection (low-quality evidence)'),
]
POST['cannabis_sativa'] = [
    ('ciadd', 'Industrial hemp (low-THC cannabis)', ['REF-5241', 'REF-5242', 'REF-5243']),
    ('cinew', {'note': 'Heart and blood vessels: cannabis use was linked to a higher risk of major cardiovascular events such as '
                       'heart attack and stroke in a 2025 meta-analysis of real-world data.',
               'severity': 'warning', 'reference_ids': ['REF-5238']}),
    ('cinew', {'note': 'Mental health: psychotic illness is more common in cannabis users, the risk rises with dose, onset comes '
                       'earlier, and people with psychosis who use cannabis relapse more often (review of reviews).',
               'severity': 'warning', 'reference_ids': ['REF-5239']}),
    ('cinew', {'note': 'Regular (daily to weekly) cannabis use can cause cannabinoid hyperemesis syndrome: repeated bouts of '
                       'severe nausea and vomiting that settle when cannabis is stopped (systematic review).',
               'severity': 'caution', 'reference_ids': ['REF-5237']}),
    ('cinew', {'note': 'CBD side effects: in placebo-controlled trials, CBD caused more diarrhoea; in childhood epilepsy trials, '
                       'where it was often taken with clobazam or valproate, it also raised liver enzymes and caused sleepiness '
                       'and sedation (meta-analysis).',
               'severity': 'caution', 'reference_ids': ['REF-5240']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'Interactions between cannabis or cannabinoids and warfarin are among the most often reported, with '
                             'bleeding risk among the effects (2024 systematic review of case reports and studies).',
                'reference_ids': ['REF-5241']}),
    ('dcinew', {'drug_class': 'immunosuppressants', 'severity': 'caution',
                'mechanism': 'Cannabis and cannabinoids have been reported to change blood levels of the transplant drugs '
                             'tacrolimus and sirolimus, which have a narrow safe range (2024 systematic review).',
                'reference_ids': ['REF-5241']}),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'caution',
                'mechanism': 'CBD and THC inhibit several drug-metabolising CYP450 enzymes, which can raise levels of medicines '
                             'cleared by them and increase side effects; clinical data are still limited (2024 systematic '
                             'reviews).',
                'reference_ids': ['REF-5242', 'REF-5241']}),
]
NOTES['cannabis_sativa'] = (
    'Searched PubMed (Cannabis sativa / hemp seed / hempseed / hemp oil / hemp extract tiab; cannabis, cannabinoid(s), '
    'cannabidiol, nabiximols, medical cannabis ti: 4,605 HT, 1,505 SR, 7,714 SAFE hits; only SR/MA and safety reviews were read '
    'in depth), Europe PMC, ClinicalTrials.gov (378) and OpenAlex. Cannabinoid reviews pool plant extracts, nabiximols and '
    'THC/CBD medicines; labelled as cannabinoid (signature-compound) evidence. Added: Whiting 2015 JAMA (moderate-quality '
    'evidence for chronic pain and spasticity; low-quality for nausea, HIV weight gain, sleep) and the 2023 TSA MA (chronic '
    'pain reduced but of questionable importance, harms outweigh benefits; sleep improved) to pain; cancer-pain MA 2020 '
    'recorded as no-effect. NEW pairs: muscle-spasm (nabiximols MS spasticity MA 2023), insomnia, anxiety (CBD MA 2024, '
    'compound evidence), appetite-loss (cancer cachexia MA 2019). Safety: cardiovascular-risk MA 2025 and psychosis review '
    'of reviews (new warnings), cannabinoid hyperemesis SR (new caution), CBD adverse-effects MA (new caution), drug-drug '
    'interaction and CYP450 SRs plus birth-outcome SR added to the existing hemp caution; three DRAFT interactions '
    '(warfarin, tacrolimus/sirolimus, CYP450), need owner sign-off. NOT ADDED: nausea pair (low-quality evidence for chemo '
    'nausea, but regular use itself causes cyclic vomiting - flagged for owner, same rule as tea and insomnia); Cochrane 2018 '
    'neuropathic pain (benefit may be outweighed by harms; not a null), nabilone fibromyalgia Cochrane (synthetic analogue), '
    'dementia Cochrane, epilepsy MAs (no vocab condition; CBD-clobazam is already in the approved anticonvulsant '
    'interaction), cannabis-use-disorder, driving and adolescent literature.')

# ================================================================== chili
PLAN['capsicum_annuum'] = [
    ('add', 'pain', ['REF-5246']),
    ('note', 'pain', 'High-concentration capsaicin patches (capsaicin is chili\'s signature compound) relieved chronic '
     'neuropathic pain in some patients, including HIV-related nerve pain in a 2026 meta-analysis; low-concentration capsaicin '
     'creams showed no meaningful effect (Cochrane reviews; compound evidence)'),
    ('newpair', 'metabolic-support', ['REF-5244'],
     'Capsaicin supplements modestly reduced body weight, BMI and waist size in overweight and obese people in a meta-analysis '
     'of trials (compound evidence); a meta-analysis of capsinoids found no overall effect'),
    ('nulladd', 'metabolic-support', ['REF-5245']),
]
NOTES['capsicum_annuum'] = (
    'Searched PubMed (Capsicum annuum tiab; capsaicin, chili, chilli, cayenne, red pepper, capsinoids, capsicum ti: 971 HT, '
    '90 SR, 1,017 SAFE hits; SR/MA read in depth), Europe PMC, ClinicalTrials.gov (196) and OpenAlex. Added: 2026 MA of 8% '
    'capsaicin patches for HIV neuropathy to pain; NEW metabolic-support pair (2023 capsaicin weight-loss MA, modest effect) '
    'with the 2022 capsinoid MA (no overall effect) recorded as no-effect. Recorded as dead ends (no pair exists; all null): '
    'capsaicin glycaemic-control MA 2021, red pepper / capsaicin blood-pressure MA 2021, capsaicin vs menthol IBS MA 2024 '
    '(capsaicin not significant). NOT ADDED because the record\'s own caution says to avoid mucous membranes (inv. 12d): '
    'capsaicin for burning mouth syndrome and orofacial pain (2026 SR and MA), intranasal capsaicin for non-allergic rhinitis '
    '(also a near-miss for allergy). Also not added: topical capsaicin for cannabinoid hyperemesis (single-arm and '
    'retrospective data), oropharyngeal dysphagia (no vocab condition), observational mortality and cancer-risk MAs.')

# ================================================================== caraway
PLAN['carum_carvi'] = [
    ('newpair', 'metabolic-support', ['REF-5247'],
     'A caraway extract reduced weight, BMI, body fat and waist-to-hip ratio more than placebo over 90 days in a triple-blind '
     'randomized trial in overweight and obese women who exercised'),
]
POST['carum_carvi'] = [
    ('ciadd', 'Generally very safe as a food spice', ['REF-5248']),
    ('dcinew', {'drug_class': 'antibiotics', 'severity': 'caution',
                'mechanism': 'In 20 healthy volunteers, 100 mg of caraway extract raised blood levels of the tuberculosis '
                             'antibiotics rifampicin, isoniazid and pyrazinamide by roughly a quarter to a third; anyone on '
                             'tuberculosis treatment should not add caraway extracts without medical advice.',
                'reference_ids': ['REF-5249']}),
]
NOTES['carum_carvi'] = (
    'Searched PubMed (Carum carvi / caraway tiab), Europe PMC, ClinicalTrials.gov (5) and OpenAlex. Most caraway trials test '
    'Menthacarin or caraway oil + L-menthol combinations (functional dyspepsia, IBS) and are not used (combinations). Added: '
    'NEW metabolic-support pair (Kazemipoor 2013 triple-blind placebo RCT, NCT01833377); its companion safety report (same 70 '
    'women, no adverse changes over 12 weeks) to the caution; healthy-volunteer PK study (caraway extract raised rifampicin, '
    'isoniazid and pyrazinamide levels) as a DRAFT antibiotics interaction, needs owner sign-off. Not added: Bunium persicum '
    '("black caraway") trials (a different species), Komouni and other Persian formulas, ginger/caraway/peppermint TB trial '
    '(caraway arm not reported as effective), computational re-analyses of the obesity trial.')

# ================================================================== shepherd's purse
PLAN['capsella_bursa_pastoris'] = []
NOTES['capsella_bursa_pastoris'] = (
    'Searched PubMed (Capsella bursa-pastoris / shepherd\'s purse tiab: 4 HT, 1 SR, 17 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (1, a three-herb vaginal pessary) and OpenAlex. No new usable human study: the postpartum-haemorrhage '
    'RCT is already held; a warfarin-bleeding case in lupus was attributed to phenyramidol, not the herb; vaginitis pessaries '
    'combine three plants; the rest is weed science and plant genetics. Settled. Open item: the heart-rhythm/medicines caution '
    'rests only on Herbal Reality (needs-review).')

# ================================================================== centaury
PLAN['centaurium_erythraea'] = []
NOTES['centaurium_erythraea'] = (
    'Searched PubMed (Centaurium erythraea / C. umbellatum / Erythraea centaurium / centaury tiab: 5 HT, 2 SR, 13 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (0) and OpenAlex. No human study of centaury alone exists: the cystitis, pyelonephritis and '
    'diabetic-nephropathy trials test Canephron N (centaury + lovage + rosemary); a kidney-injury case involved a three-herb '
    'mixture. A rodent study found no toxicity from a water extract (acute and 90-day); not needed for any current claim. '
    'Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r07_changes.tsv')
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
