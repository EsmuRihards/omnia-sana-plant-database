"""Deep re-sweep of batch 5 (cnicus-benedictus .. cynara-scolymus) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3507..REF-3535 (PubMed efetch, deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3507', '14653829', 'artichokedyspepsia', 'rct'),
    ('REF-3508', '33465383', 'artichokebp', 'meta-analysis'),
    ('REF-3509', '34383355', 'artichokeliver', 'meta-analysis'),
    ('REF-3510', '41274796', 'artichokesteatosis', 'rct'),
    ('REF-3511', '41270328', 'artichokecardiometabolic', 'meta-analysis'),
    ('REF-3512', '32951745', 'artichokeglycemic', 'meta-analysis'),
    ('REF-3513', '18424099', 'artichokecholesterol', 'rct'),
    ('REF-3514', '19019730', 'spicehawthorn', 'rct'),
    ('REF-3515', '19789403', 'herbchf', 'rct'),
    ('REF-3516', '16762125', 'hawthornbp', 'rct'),
    ('REF-3517', '41693488', 'saffronmood', 'meta-analysis'),
    ('REF-3518', '40762630', 'saffronsleep', 'rct'),
    ('REF-3519', '40965059', 'saffronoa', 'rct'),
    ('REF-3520', '18271889', 'saffronpms', 'rct'),
    ('REF-3521', '41151539', 'saffronpmsma', 'meta-analysis'),
    ('REF-3522', '39931766', 'saffronmets', 'meta-analysis'),
    ('REF-3523', '20831681', 'saffronalzheimer', 'rct'),
    ('REF-3524', '24459154', 'coffeediabetes', 'meta-analysis'),
    ('REF-3525', '26284906', 'cordycepsimmunity', 'rct'),
    ('REF-3526', '23466353', 'corianderoiltinea', 'rct'),
    ('REF-3527', '23337964', 'uverythemaplants', 'rct'),
    ('REF-3528', '25766448', 'cuminweight', 'rct'),
    ('REF-3529', '37748368', 'curcuminglycemic', 'meta-analysis'),
    ('REF-3530', '37230418', 'curcuminlipids', 'meta-analysis'),
    ('REF-3531', '38220376', 'curcuminbp', 'meta-analysis'),
    ('REF-3532', '35091013', 'curcuminuc', 'meta-analysis'),
    ('REF-3533', '31423805', 'curcumindepression', 'meta-analysis'),
    ('REF-3534', '36804260', 'curcumininflammation', 'meta-analysis'),
    ('REF-3535', '36882287', 'curcuminobesity', 'meta-analysis'),
])

_c286 = deep_lib.CACHE['34825421']
BIB = dict(
    sets={'REF-0158': {'title': 'Potential benefits of Cuminum cyminum L supplementation on components of metabolic syndrome in adults with metabolic disorders: a GRADE-assessed systematic review and meta-analysis of randomized controlled trials',
                       'journal': 'Frontiers in Nutrition', 'doi': '10.3389/fnut.2025.1618108', 'pmid': '41608519'},
          'REF-0026': {'doi': '10.3389/falgy.2025.1698559'},   # had "/full" appended
          # REF-0286 is Tavakoli-Rouzbehani 2022 (PMID 34825421); its url pointed to an unrelated PMC paper
          'REF-0286': {'author': 'Tavakoli-Rouzbehani, O.M., Faghfouri, A.H., Anbari, M. et al.',
                       'title': deep_lib._clean(_c286['title']).rstrip('.'), 'journal': 'Phytotherapy Research',
                       'doi': _c286['doi'], 'pmid': '34825421', 'url': 'https://pubmed.ncbi.nlm.nih.gov/34825421/',
                       'abstract': deep_lib._clean(_c286['abstract'])}},
    delete=['REF-0584',   # Cochrane 2013 artichoke/cholesterol - WITHDRAWN by Cochrane Heart in 2016 (PMID 27195440)
            'REF-1702'],  # duplicate of REF-0151 (same DOI 10.1016/j.fitote.2015.03.012)
    new=NEW,
)

CUMIN_ACTS = ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive')
CUMIN_NONEVIDENCE = ['REF-0026', 'REF-0066', 'REF-0067', 'REF-0116', 'REF-0147', 'REF-0156', 'REF-0175', 'REF-0267',
                     'REF-0307', 'REF-0171']   # allergy reviews, EU journal texts, dictionary, history pieces, a fibrillation study
SAFFRON_ACTS = ('anti-inflammatory', 'anticancer', 'antidiabetic', 'antioxidant', 'neuroprotective', 'sedative')
TURMERIC_ACTS = ('anti-inflammatory', 'anticancer', 'antidiabetic', 'antimicrobial', 'antioxidant', 'gastroprotective')
HAWTHORN_HF = 'Hawthorn extract improved symptoms and exercise capacity as add-on treatment for chronic heart failure (Cochrane review); two large trials (SPICE, HERB CHF) found no benefit on their main outcomes; traditionally used for nervous heart complaints (EU herbal monograph)'

PLAN = {
    'cnicus_benedictus': [
        ('note', 'cancer', 'Leaf extract slowed cervical cancer cells in the lab (preclinical)'),
    ],
    'coffea_arabica': [
        ('arm', 'antioxidant', ['REF-0081', 'REF-0121', 'REF-0096', 'REF-0135', 'REF-0059', 'REF-0178', 'REF-0205']),
        ('arm', 'neuroprotective', ['REF-0081', 'REF-0121', 'REF-0096', 'REF-0135', 'REF-0059', 'REF-0178']),
        ('refadd', ['REF-0081', 'REF-0121', 'REF-0096']),
        ('newpair', 'liver-support', ['REF-0135'], 'Drinking more coffee was linked to a much lower risk of liver cirrhosis in a meta-analysis of observational studies'),
        ('newpair', 'blood-sugar', ['REF-3524'], 'Coffee drinking, caffeinated or decaffeinated, was linked to a lower risk of type 2 diabetes in a meta-analysis of prospective studies'),
        ('note', 'cardiovascular-support', 'Moderate coffee drinking (3-5 cups a day) was linked to lower cardiovascular disease risk in a meta-analysis of cohort studies; coffee extracts inhibited platelet aggregation in the lab'),
        ('note', 'cognitive-function', 'Caffeine, coffee\'s signature compound, improves alertness (MedlinePlus; compound evidence)'),
        ('note', 'metabolic-support', 'Coffee drinking has been linked to lower type 2 diabetes risk (review); coffee-leaf extracts lowered blood glucose in lab studies'),
    ],
    'cordyceps_militaris': [
        ('add', 'immune-support', ['REF-3525']),
        ('note', 'immune-support', 'C. militaris increased natural killer cell activity and lymphocyte proliferation vs placebo in healthy men (randomized trial)'),
    ],
    'coriandrum_sativum': [
        ('merge', 'REF-1702', 'REF-0151'), ('purge', 'REF-0308'),   # WHO vol. 1 has no coriander monograph
        ('add', 'infection', ['REF-3526']), ('nulladd', 'inflammation', ['REF-3527']),
        ('drop', 'skin-irritation'),   # contradicted: not significantly better than vehicle in a placebo-controlled UV-erythema test
        ('note', 'infection', 'A coriander-oil ointment cleared athlete\'s foot (tinea pedis) in a small randomized trial; antimicrobial activity in lab studies (review)'),
        ('note', 'inflammation', 'Anti-inflammatory activity in lab and animal studies (review); in a placebo-controlled skin test, coriander did not significantly reduce UV-induced redness'),
        ('note', 'metabolic-support', 'Blood-sugar-lowering and other metabolic activities reported in lab and animal studies (review)'),
    ],
    'crataegus_laevigata': [
        ('nulladd', 'cardiovascular-support', ['REF-3514', 'REF-3515']),
        ('newpair', 'high-blood-pressure', ['REF-3516'], 'Hawthorn (C. laevigata) extract lowered diastolic blood pressure in a randomized trial in people with type 2 diabetes on medication'),
        ('arm', 'anti-inflammatory', ['REF-2442']), ('arm', 'antioxidant', ['REF-2442']),
        ('arm', 'antispasmodic', ['REF-2442', 'REF-1785', 'REF-1786']), ('arm', 'sedative', ['REF-2442']),
        ('refadd', ['REF-1785', 'REF-1786']),
        ('note', 'cardiovascular-support', HAWTHORN_HF),
        ('note', 'insomnia', 'Traditionally used to aid sleep (EU herbal monograph)'),
    ],
    'crataegus_monogyna': [
        ('nulladd', 'cardiovascular-support', ['REF-3514', 'REF-3515']),
        ('arm', 'anti-inflammatory', ['REF-2442', 'REF-0082']), ('arm', 'antioxidant', ['REF-2442', 'REF-0082']),
        ('arm', 'sedative', ['REF-2442']),
        ('note', 'cardiovascular-support', HAWTHORN_HF),
        ('note', 'insomnia', 'Traditionally used to aid sleep (EU herbal monograph)'),
        ('note', 'cancer', 'Hawthorn extract showed anti-leukaemia activity in lab studies (preclinical)'),
    ],
    'crocus_sativus': [('arm', a, ['REF-0005', 'REF-0172']) for a in SAFFRON_ACTS] + [
        ('arm', 'sedative', ['REF-0789', 'REF-2001', 'REF-2002', 'REF-2003']),
        ('newpair', 'anxiety', ['REF-3517', 'REF-2002'], 'Saffron reduced self-rated anxiety in a GRADE-assessed meta-analysis of randomized trials and in a trial in healthy adults; clinician-rated scores did not change significantly'),
        ('add', 'depression', ['REF-3517']),
        ('add', 'insomnia', ['REF-3518']), ('add', 'arthritis', ['REF-3519']),
        ('newpair', 'pms', ['REF-3520', 'REF-3521'], 'Saffron eased premenstrual syndrome symptoms vs placebo in a randomized trial and a meta-analysis'),
        ('newpair', 'menstrual-cramps', ['REF-3521'], 'Saffron reduced period pain (dysmenorrhoea) in a meta-analysis of randomized trials'),
        ('newpair', 'metabolic-support', ['REF-3522'], 'Saffron improved fasting glucose, HbA1c, cholesterol and blood pressure in metabolic syndrome (meta-analysis of randomized trials)'),
        ('newpair', 'blood-sugar', ['REF-2502', 'REF-3522'], 'Saffron lowered fasting glucose and HbA1c vs placebo in diabetes (meta-analyses of randomized trials)'),
        ('add', 'cognitive-function', ['REF-3523']), ('add', 'memory', ['REF-3523']),
        ('note', 'insomnia', 'A standardised saffron extract improved subjective and objective sleep quality in older adults with sleep complaints (randomized trial); described as hypnotic in Avicenna\'s Canon (historical review)'),
        ('note', 'inflammation', 'Described as anti-inflammatory in Avicenna\'s Canon; saffron compounds reduced inflammation in lab and animal studies (historical review)'),
        ('note', 'cancer', 'Saffron and its compounds slowed tumours in lab and animal studies (reviews)'),
        ('note', 'arthritis', 'Saffron reduced osteoarthritis symptoms, inflammation and painkiller use in a small randomized trial'),
        ('note', 'cognitive-function', 'Saffron improved cognition vs placebo over 16 weeks in mild-to-moderate Alzheimer\'s disease (randomized trial)'),
        ('note', 'memory', 'Saffron improved cognition, including memory tests, vs placebo in mild-to-moderate Alzheimer\'s disease (randomized trial)'),
    ],
    'cuminum_cyminum': [('arm', a, CUMIN_NONEVIDENCE + ['REF-0654', 'REF-0286', 'REF-0158']) for a in CUMIN_ACTS] + [
        ('refadd', CUMIN_NONEVIDENCE),
        ('rm', 'muscle-spasm', ['REF-0008']),   # gut smooth-muscle "antispasmodic" is not muscle cramps (off-target, inv. 11)
        ('newpair', 'high-cholesterol', ['REF-0652', 'REF-0286'], 'Cumin lowered total cholesterol and some other blood lipids in meta-analyses of randomized trials'),
        ('add', 'metabolic-support', ['REF-3528']),
        ('note', 'bloating', 'Traditionally used for flatulence (review of ethnopharmacology)'),
        ('note', 'indigestion', 'Traditionally used for dyspepsia (review of ethnopharmacology)'),
        ('note', 'infection', 'Antimicrobial activity reported in lab studies (review)'),
        ('note', 'inflammation', 'Anti-inflammatory activity reported in lab and animal studies (review)'),
        ('note', 'metabolic-support', 'Cumin improved blood glucose, triglycerides and waist size in some meta-analyses of trials and helped weight loss as much as orlistat in one trial; another meta-analysis and a trial of cumin oil found no effect on glycaemic markers or most metabolic-syndrome components'),
    ],
    'curcuma_longa': [('arm', a, ['REF-0273']) for a in TURMERIC_ACTS] + [
        ('refadd', ['REF-0273']),
        ('add', 'arthritis', ['REF-2167']),
        ('newpair', 'blood-sugar', ['REF-3529', 'REF-0793'], 'Turmeric/curcumin lowered fasting glucose and HbA1c in meta-analyses and systematic reviews of randomized trials'),
        ('newpair', 'high-cholesterol', ['REF-3530'], 'Turmeric/curcumin improved total, LDL and HDL cholesterol and triglycerides in a GRADE-assessed meta-analysis (low-certainty evidence)'),
        ('newpair', 'high-blood-pressure', ['REF-3531'], 'Turmeric/curcumin modestly lowered blood pressure in a GRADE-assessed meta-analysis of randomized trials'),
        ('newpair', 'ibd', ['REF-3532', 'REF-2167'], 'Adding curcumin to standard treatment increased clinical remission in ulcerative colitis (meta-analyses of randomized trials)'),
        ('newpair', 'psoriasis', ['REF-2167'], 'Curcumin and turmeric extract improved psoriasis in a meta-analysis of randomized trials in autoimmune diseases'),
        ('newpair', 'depression', ['REF-3533'], 'Curcumin added to standard care improved depressive and anxiety symptoms in a meta-analysis of small randomized trials'),
        ('add', 'inflammation', ['REF-0791', 'REF-3534']), ('add', 'metabolic-support', ['REF-3535']),
        ('note', 'arthritis', 'Turmeric extract and curcumin improved arthritis symptoms and inflammation in meta-analyses of randomized trials (low-quality evidence); traditional use for rheumatic pain (WHO monograph)'),
        ('note', 'cancer', 'Curcumin, turmeric\'s signature compound, showed anticancer effects in lab and animal studies (review; compound evidence)'),
        ('note', 'cardiovascular-support', 'Curcumin\'s anti-inflammatory effects have been studied in cardiovascular disease (review; compound evidence)'),
        ('note', 'inflammation', 'Turmeric/curcumin lowered inflammatory markers such as CRP in meta-analyses of randomized trials; traditional anti-inflammatory use (WHO monograph)'),
        ('note', 'metabolic-support', 'Turmeric/curcumin improved weight, waist size and adiposity hormones in a meta-analysis of randomized trials'),
        ('note', 'acid-reflux', 'Traditional remedy for acid dyspepsia (WHO monograph)'),
        ('note', 'indigestion', 'Traditional remedy for dyspepsia (WHO monograph)'),
        ('note', 'infection', 'Traditional remedy for ringworm (WHO monograph); antimicrobial activity in lab studies (review)'),
        ('note', 'skin-irritation', 'Traditional remedy for skin diseases (WHO monograph); a systematic review found limited but promising clinical evidence for skin conditions'),
        ('note', 'wounds', 'Traditional remedy for slow-healing wounds (WHO monograph)'),
    ],
    'cynara_scolymus': [
        ('purge', 'REF-0584'),
        ('add', 'indigestion', ['REF-3507']),
        ('newpair', 'high-blood-pressure', ['REF-3508'], 'Artichoke lowered blood pressure in people with hypertension (meta-analysis of randomized trials)'),
        ('add', 'liver-support', ['REF-3509', 'REF-3510']),
        ('add', 'cardiovascular-support', ['REF-3511', 'REF-2566', 'REF-2567']),
        ('add', 'high-cholesterol', ['REF-3513']),
        ('newpair', 'blood-sugar', ['REF-3512'], 'Artichoke products lowered fasting blood sugar in a meta-analysis of randomized trials'),
        ('note', 'cardiovascular-support', 'Artichoke modestly improved cholesterol, triglycerides and other cardiometabolic risk markers in meta-analyses of randomized trials'),
        ('note', 'high-cholesterol', 'Artichoke leaf extract lowered total and LDL cholesterol and triglycerides in meta-analyses of randomized trials'),
        ('note', 'liver-support', 'Artichoke lowered liver enzymes, especially in fatty liver disease, and reduced liver fat in meta-analyses and trials (in one trial in obesity, liver enzymes rose); liver-protective effects in animal studies'),
        ('note', 'indigestion', 'Artichoke leaf extract relieved functional dyspepsia better than placebo in a randomized trial; traditional digestive aid (EU herbal monograph)'),
        ('note', 'bloating', 'Traditional digestive aid for bloating and fullness (EU herbal monograph)'),
    ],
}

NOTES = {
    'cnicus_benedictus': 'Deep re-sweep. Cancer note rewritten. No trials on PubMed. Gap: EU monograph uses (loss of appetite, dyspepsia) have no source held.',
    'coffea_arabica': 'Deep re-sweep. The antioxidant/neuroprotective actions held non-evidence: EFSA caffeine SAFETY opinion REF-0081, ICO trade report REF-0121, ISSN sport position stand REF-0096 (kept in references), a cirrhosis MA REF-0135, a CVD cohort MA REF-0059 and MedlinePlus caffeine REF-0178 - removed. New pairs (owner rule): liver-support from REF-0135 (cirrhosis MA), blood-sugar from Ding 2014 MA REF-3524 (observational association, labelled).',
    'cordyceps_militaris': 'Deep re-sweep. Kang 2015 RCT REF-3525 (NK activity, lymphocyte proliferation) added to immune-support. Cordyceps sinensis (Ophiocordyceps) trials not used - other species. 2024 beverage RCT 38580687 not added (within-group changes only).',
    'coriandrum_sativum': 'Deep re-sweep. REF-1702 was a duplicate of REF-0151 (same DOI) - merged and deleted. REF-0308 (WHO vol. 1 has no coriander monograph) purged from the actions. Tinea-pedis RCT REF-3526 added to infection. UV-erythema RCT REF-3527 (coriander not significantly better than vehicle; only Aloe was) recorded as no-effect for inflammation; skin-irritation (inferred only) dropped as contradicted (inv. 11). REF-3527 also covers chamomile, lemon balm, witch hazel and tea tree - to be wired in their batches. Carmint (3-herb product) not used.',
    'crataegus_laevigata': 'Deep re-sweep. SPICE REF-3514 (WS 1442: no effect on primary endpoint) and HERB CHF REF-3515 (no symptomatic or functional benefit) recorded as no-effect for cardiovascular-support (Crataegus spp. extracts, as the Cochrane review). New high-blood-pressure pair from Walker 2006 RCT REF-3516 (C. laevigata; owner rule). Cochrane HF review REF-2442 removed from anti-inflammatory/antioxidant/antispasmodic/sedative actions (not evidence for them); arrhythmia rat studies REF-1785/REF-1786 removed from the antispasmodic action (REF-1786 found Crataegus aggravated arrhythmias; kept in references).',
    'crataegus_monogyna': 'Deep re-sweep. SPICE REF-3514 and HERB CHF REF-3515 recorded as no-effect for cardiovascular-support. Cochrane REF-2442 and EU monograph REF-0082 removed from actions they do not support (anti-inflammatory, antioxidant; REF-2442 also sedative).',
    'crocus_sativus': 'Deep re-sweep. Depression RCTs REF-0005/REF-0172 were filed under six unrelated actions, and depression reviews/RCTs REF-0789/2001/2002 plus the ADHD trial REF-2003 under "sedative" - removed (still cited for depression / in references). Added: GRADE MA REF-3517 (depression; new anxiety pair with REF-2002), sleep RCT REF-3518 (insomnia), OA RCT REF-3519 (arthritis), AD RCT REF-3523 (cognition, memory). New pairs (owner rule): pms (REF-3520 RCT, REF-3521 MA), menstrual-cramps (REF-3521), metabolic-support (REF-3522), blood-sugar (held MA REF-2502 + REF-3522).',
    'cuminum_cyminum': 'Deep re-sweep. All five actions carried the same ~15-ref bucket: allergy reviews (REF-0026, REF-0156), EU Official Journal texts (REF-0066/0067), a Latvian dictionary (REF-0116), history/blog pieces (REF-0147/0175/0267/0307), an alpha-synuclein study (REF-0171), the null glycaemic MA REF-0654 and clinical MAs REF-0286/REF-0158 - removed (kept in references or still cited for their pairs). REF-0286 repaired (its url pointed to an unrelated variational-autoencoder paper; it is Tavakoli-Rouzbehani 2022, PMID 34825421); REF-0158 and REF-0026 DOIs fixed (trailing "/full"). New high-cholesterol pair (owner rule; REF-0652, REF-0286). Weight-loss RCT REF-3528 added to metabolic-support. Muscle-spasm dropped: REF-0008\'s "antispasmodic" is gut smooth muscle (off-target, inv. 11).',
    'curcuma_longa': 'Deep re-sweep. Piperine pharmacokinetics study REF-0273 removed from all six actions (kept in references). Held MAs REF-2167 (RA, psoriasis, UC) and REF-0791 wired. New pairs from GRADE-assessed MAs (owner rule; curcumin = signature compound, labelled): blood-sugar (REF-3529 + held SR REF-0793), high-cholesterol REF-3530, high-blood-pressure REF-3531, ibd REF-3532 + REF-2167, psoriasis REF-2167, depression REF-3533. Inflammation MA REF-3534 and obesity MA REF-3535 added. Not added (owner to decide): liver-support - a GRADE MA (37178581) exists, but turmeric-associated liver injury is reported (Tuscany phytovigilance SR 32656820); muscle-soreness MA 37408367 was null (no pair exists).',
    'cynara_scolymus': 'Deep re-sweep. Cochrane 2013 REF-0584 was WITHDRAWN by Cochrane Heart in 2016 (PMID 27195440) and its own conclusion was "not convincing" - purged and deleted. Added: Holtmann 2003 dyspepsia RCT REF-3507, liver-enzyme MA REF-3509 and steatosis RCT REF-3510 (liver-support), cardiometabolic MA REF-3511 and held lipid MAs REF-2566/2567 (cardiovascular-support), Bundy 2008 RCT REF-3513 (high-cholesterol). New pairs (owner rule): high-blood-pressure REF-3508, blood-sugar REF-3512.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 5', os.path.join(HERE, 'deep', 'd05_changes.tsv'), **BIB)
