"""Research-deepening batch 26 (plantago-major, pleurotus-ostreatus, potentilla-erecta, primula-veris,
prunella-vulgaris). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5598.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 26'

SPEC = [
    # greater plantain
    ('REF-5598', '39359439', 'plantagobronchitis', 'rct'),
    ('REF-5599', '32507421', 'plantagomucositis', 'rct'),
    ('REF-5600', '33854559', 'plantagonafld', 'rct'),
    ('REF-5601', '15612001', 'plantagogenotoxdrosophila', 'preclinical'),
    ('REF-5602', '23354396', 'plantagowoundmutagenicity', 'preclinical'),
    # oyster mushroom
    ('REF-5603', '41085920', 'pleuranchewablerti', 'rct'),
    ('REF-5604', '40021713', 'pleuranasthma', 'rct'),
    ('REF-5605', '42299921', 'oystermushroommemory', 'rct'),
    ('REF-5606', '42071226', 'oystermushroomldl', 'rct'),
    ('REF-5607', '33630827', 'oystermushroominhalationallergy', 'clinical'),
    ('REF-5608', '37780800', 'oystermushroomfoodallergy', 'clinical'),
    # selfheal
    ('REF-5609', '41047360', 'prunellaluts', 'rct'),
    ('REF-5610', '38268963', 'prunellaphlebosclerosis', 'clinical'),
    # cowslip
    ('REF-5611', '28960556', 'herbalmedicinespacontamination', 'preclinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== greater plantain
PLAN['plantago_major'] = [
    ('add', 'bronchitis', ['REF-5598']),
    ('note', 'bronchitis',
     'Traditionally used in mild bronchitis (Herbal Reality); in a 2024 randomized double-blind trial in 80 adults with acute '
     'bronchitis, plantain syrup for 10 days lowered bronchitis severity, cough frequency and sputum more than placebo'),
    ('add', 'cough', ['REF-5598']),
    ('note', 'cough',
     'Demulcent / expectorant (coughs, catarrh, irritated airways); in a 2024 randomized double-blind trial in adults with '
     'acute bronchitis, plantain syrup reduced cough frequency more than placebo'),
    ('newpair', 'oral-health', ['REF-5599'],
     'In a 2020 randomized double-blind trial in 46 people with head and neck cancer, plantain syrup during radiotherapy '
     'lowered the severity of mouth sores (oral mucositis) and mouth pain compared with placebo'),
    ('newpair', 'liver-support', ['REF-5600'],
     'In a 2021 randomized double-blind trial in 74 people with non-alcoholic fatty liver disease, plantain seed (2 g twice '
     'daily) for 12 weeks lowered liver enzymes and improved the ultrasound grade of fatty liver more than placebo'),
]
POST['plantago_major'] = [
    ('cinew', {'note': 'Lab safety: a water extract of plantain was genotoxic in fruit flies, while a hydroalcoholic extract '
                       'was not mutagenic in another test (lab and insect studies).',
               'severity': 'info', 'reference_ids': ['REF-5601', 'REF-5602']}),
]
NOTES['plantago_major'] = (
    'Searched PubMed (Plantago major / greater, broadleaf, broad-leaved or common plantain tiab; bare "plantain" was not '
    'searched because it also matches banana plantains and psyllium: 20 HT, 11 SR, 39 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (2) and OpenAlex. Added: 2024 acute bronchitis RCT to bronchitis and cough (both previously rested '
    'only on traditional sources); NEW oral-health pair (2020 radiation mucositis RCT; two systematic reviews of natural '
    'products for radiation mucositis were not cited); NEW liver-support pair (2021 NAFLD RCT: enzymes and ultrasound grade); '
    'genotoxicity lab studies as an info note. GAPS: heavy-bleeding - the 2020 oral syrup trial compared only with '
    'mefenamic acid (active comparator) and was not better for severity; the 2026 systematic review mixes oral syrup with '
    'vaginal and rectal suppositories and postpartum bleeding, and reports haemoglobin falling in the treated groups, so '
    'no pair. IBD - in the 2021 ulcerative colitis seed RCT some symptoms (abdominal tenderness, reflux, gastric pain) '
    'were milder than placebo, but blood in stool and distension improved only within-group and no total activity index '
    'difference is reported, so no pair. Kidney - 2024 diabetic nephropathy trial was open-label with proteinuria only '
    '(surrogate). Urinary - a 1992 double-blind placebo crossover found no diuretic effect for Plantago major (there is no '
    'urinary pair to attach it to). Not added: Aloe vera + plantain diabetic-foot gel, plantain + mallow + honey radiation '
    'dermatitis cream, KalobaTUSS and Butirprost (combinations), 2021 obese-women leptin/VEGF trial (surrogate), 2009 '
    'irritant contact dermatitis letter (no abstract), 1982 Bulgarian chronic bronchitis series (25 patients, no control '
    'group; Europe PMC), psyllium meta-analyses (Plantago ovata, other species), 2019 Lebanese blood-pressure RCT (tested '
    'mint, nettle and violet, not plantain), phytoremediation and veterinary studies.')

# ================================================================== oyster mushroom
PLAN['pleurotus_ostreatus'] = [
    ('add', 'cold', ['REF-5603']),
    ('note', 'cold',
     'Pleuran, the beta-glucan from oyster mushroom, reduced respiratory infection symptoms in placebo-controlled trials in '
     'athletes and children; in a 2025 randomized double-blind trial in 249 children, a chewable pleuran supplement cut '
     'respiratory infections and colds compared with an active placebo containing the same vitamin D and zinc (compound '
     'evidence)'),
    ('newpair', 'asthma', ['REF-5604'],
     'In a 2025 randomized double-blind multicentre trial in 230 children with partly controlled asthma, pleuran (oyster '
     'mushroom beta-glucan) with vitamin C improved asthma control more than vitamin C alone, mainly in children under 12, '
     'and reduced respiratory infections in children aged 12 and over (compound evidence)'),
    ('newpair', 'memory', ['REF-5605'],
     'In a 2026 randomized controlled trial in 80 healthy adults aged 60-80, eating oyster mushroom four times a week for '
     '12 weeks improved delayed word recall and recognition compared with a placebo food'),
    ('nulladd', 'cardiovascular-support', ['REF-5606']),
    ('note', 'cardiovascular-support',
     'Eating oyster mushroom lowered cholesterol and triglycerides, and in some trials blood pressure (systematic review; '
     'low-quality evidence); in a 2026 double-blind RCT, 8.4 g of oyster mushroom powder daily for 4 weeks did not lower LDL '
     'cholesterol in adults with moderately raised LDL'),
]
POST['pleurotus_ostreatus'] = [
    ('ciadd', 'Rare cases of occupational asthma and allergy reported among people working with mushroom cultivation',
     ['REF-5607']),
    ('cinew', {'note': 'Food allergy: one person had an allergic reaction after eating oyster mushroom, confirmed by an oral '
                       'food challenge (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5608']}),
]
NOTES['pleurotus_ostreatus'] = (
    'Searched PubMed (Pleurotus ostreatus / oyster mushroom(s) tiab: 53 HT, 4 SR, 180 SAFE hits; most were cultivation, '
    'bioremediation and feed studies), Europe PMC, ClinicalTrials.gov (13) and OpenAlex. Added: 2025 chewable pleuran RCT '
    'to cold (score was 6; the active placebo had the same vitamin D and zinc, so pleuran is isolated); NEW asthma pair '
    '(2025 pleuran + vitamin C vs vitamin C RCT; benefit partly in age subgroups); NEW memory pair (2026 OYSCOG whole-'
    'mushroom RCT in healthy older adults; anxiety was not paired because the difference came from worsening on placebo); '
    '2026 double-blind LDL trial as a NULL result on cardiovascular-support; inhalation anaphylaxis case added to the '
    'occupational allergy caution; food-allergy case as a caution. GAP: diarrhoea - a 2025 double-blind pleuran RCT in 27 '
    'children with acute gastroenteritis (Europe PMC) found no effect on duration or severity; there is no diarrhoea pair '
    'to attach it to. Not added: 2020 pleuran herpes (HSV-1) RCT (no herpes '
    'condition in the vocabulary), 2017 COPD exacerbation study (non-randomized, open-label), 2016 pleuran cream in atopic '
    'dermatitis (open split-body, no randomization stated), 2014 anti-allergic pleuran RCT (eosinophils and IgE only, '
    'surrogate), 2010 athletes immune-cell study (surrogate), 2022 Mexican diet study (results within-group), 2011 HIV '
    'lipid study (single-arm; non-HDL cholesterol unchanged), Tamogitake extract (Pleurotus cornucopiae, other species), '
    'Mediterranean-diet mushroom trials (white button and oyster together), fungal beta-glucan and mushroom-intake '
    'systematic reviews (pool other species), single-meal GLP-1 studies (acute, surrogate), 2026 occupational allergy '
    'letter (no abstract).')

# ================================================================== tormentil
PLAN['potentilla_erecta'] = []
NOTES['potentilla_erecta'] = (
    'Searched PubMed (Potentilla erecta / P. tormentilla / tormentil / Tormentillae rhizoma tiab: 10 HT, 3 SR, 8 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex. Nothing new: the 2017 systematic review of herbal medicines '
    'for paediatric GI disorders reports no tormentil-specific result in its abstract (the rotavirus RCT is already '
    'cited directly); IBD reviews summarise the open-label study already held; the 2026 oral-ulcer gel was tested in rats only; the 2023 menthol + tormentil + raspberry + loosestrife '
    'oral product (held) is a combination. Settled.')

# ================================================================== cowslip
PLAN['primula_veris'] = []
POST['primula_veris'] = [
    ('cinew', {'note': 'Contamination: in a 2017 survey of 98 herbal medicines from German shops and pharmacies, fixed-'
                       'combination products of cowslip with gentian, sorrel, vervain and elder were commonly contaminated '
                       'with pyrrolizidine alkaloids from Senecio plants (ragworts and groundsels), often above German and '
                       'EU recommended limits; these alkaloids can harm the liver (product analysis).',
               'severity': 'info', 'reference_ids': ['REF-5611']}),
]
NOTES['primula_veris'] = (
    'Searched PubMed (Primula veris / Primula officinalis / Primulae radix / cowslip tiab; marsh cowslip, Caltha, is a '
    'different plant: 3 HT, 0 SR, 3 SAFE hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex. Added: 2017 German market '
    'survey of pyrrolizidine-alkaloid contamination as an info note. Not added: Sinupret, Cardiodoron and a heart-rate-'
    'variability herbal composition (combinations), thymol cough review. Settled for human efficacy evidence: no trial of '
    'cowslip alone was found.')

# ================================================================== selfheal
PLAN['prunella_vulgaris'] = [
    ('newpair', 'prostate-support', ['REF-5609'],
     'In a 2026 randomized double-blind trial in 80 men aged 40-75 with moderate urinary symptoms, selfheal extract (600 mg '
     'daily) for 12 weeks improved prostate symptom scores (IPSS) and quality of life more than placebo; urine flow and '
     'prostate size did not change'),
]
POST['prunella_vulgaris'] = [
    ('cinew', {'note': 'Long-term use: a person who took traditional Chinese medicines, mainly selfheal, for a long time, '
                       'together with vitamin D and calcium supplements, developed mesenteric phlebosclerosis, in which the '
                       'veins of the bowel calcify (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5610']}),
]
NOTES['prunella_vulgaris'] = (
    'Searched PubMed (Prunella vulgaris / self-heal / selfheal / heal-all / Spica Prunellae / Xiakucao tiab; "heal-all" '
    'also matched "time heals all wounds" prose: 36 HT (all already held), 15 SR, 85 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (32) and OpenAlex. Added: NEW prostate-support pair (2026 LUTS RCT); 2024 mesenteric '
    'phlebosclerosis case as a caution. GAPS: thyroid - two meta-analyses (2025, 2027) report that Prunella preparations '
    'added to antithyroid drugs lowered thyroid hormones and antibodies in Graves\' disease and hyperthyroidism (a 2026 '
    'meta-analysis of TCM formulas and a 2020 Hashimoto\'s review also cover Xiakucao), but the vocabulary has no thyroid '
    'condition. '
    'Cancer - a 2018 Frontiers trial in 424 breast cancer patients reported better pathological response and survival '
    'with Prunella oral solution plus taxane, but neither the abstract nor the full text states randomization or blinding, '
    'no trial registration is given, and the regimen is described inconsistently, so it was not added. Not added: SKI '
    '306X / SKCPT (Clematis + Trichosanthes + Prunella combination) knee OA trials, Xiakucao + methimazole retrospective '
    'study, 2019 subacute thyroiditis study (no vocabulary condition), 2024 heavy-metal risk assessment (risks within '
    'acceptable limits), lab and animal studies.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r26_changes.tsv')
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
