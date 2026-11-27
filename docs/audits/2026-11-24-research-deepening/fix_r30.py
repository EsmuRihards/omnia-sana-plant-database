"""Research-deepening batch 30 (salvia-hispanica, salvia-officinalis, salvia-rosmarinus, sambucus-nigra,
saponaria-officinalis). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5644.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 30'

SPEC = [
    # sage
    ('REF-5644', '33615001', 'menosansage', 'rct'),
    ('REF-5645', '35106985', 'sagediabetesma', 'meta-analysis'),
    ('REF-5646', '37612717', 'sagearomasexualfunction', 'rct'),
    # rosemary
    ('REF-5647', '41312013', 'rosemaryanxietycrossover', 'rct'),
    ('REF-5648', '33550193', 'rosemarynursesleepiness', 'rct'),
    ('REF-5649', '39503638', 'rosemarypostintubationthroat', 'rct'),
    # chia
    ('REF-5650', '38917708', 'chiaglycemicma', 'meta-analysis'),
    ('REF-5651', '42797010', 'chiaallergyreview', 'narrative-review'),
    # elder
    ('REF-5652', '42572604', 'elderberrypancreatitis', 'clinical'),
    ('REF-5653', '35602846', 'elderberryautoimmunehepatitis', 'clinical'),
    ('REF-5654', '38596626', 'elderberrypazopanib', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== chia
PLAN['salvia_hispanica'] = [
    ('nulladd', 'metabolic-support', ['REF-5650']),
    ('note', 'metabolic-support',
     'Chia reduced the blood sugar rise after a meal and prolonged fullness in a randomized trial; it did not reduce body '
     'weight in trials or a meta-analysis, and a 2024 meta-analysis of 8 RCTs found no effect on fasting blood sugar, HbA1c '
     'or insulin'),
]
POST['salvia_hispanica'] = [
    ('cinew', {'note': 'Allergy: chia seed can cause immediate IgE-mediated allergic reactions, including skin reactions and '
                       'anaphylaxis (case reports and a case series), and its proteins may cross-react with sesame '
                       '(narrative review).',
               'severity': 'caution', 'reference_ids': ['REF-5651']}),
]
NOTES['salvia_hispanica'] = (
    'Searched PubMed (Salvia hispanica / chia seed(s) / Salba tiab, "chia" in titles; Pistacia lentiscus var. Chia, '
    'mastic, and the CHIA gene are not this plant: 55 HT, 23 SR, 73 SAFE hits), Europe PMC, ClinicalTrials.gov (57) and '
    'OpenAlex. Cardiovascular-support and high-blood-pressure (9) were not padded (2025 GRADE dose-response meta-analysis '
    'confirms the blood-pressure fall). Added: 2024 glycaemic meta-analysis as a NULL result on metabolic-support; 2026 '
    'chia allergy review as a caution. GAPS: blood-sugar - three 2024-2025 meta-analyses found no effect on fasting '
    'glucose, HbA1c or insulin, so no pair; high-cholesterol - a 2024 meta-regression of 14 RCTs found small LDL and '
    'triglyceride falls at higher doses, but a 2024 meta-analysis in overweight adults found no lipid change, so no pair; '
    'inflammation - a 2024 meta-analysis lowered CRP only (biomarker). Not added: chia + fennel, nopal + chia + soy + oat, '
    'viscous fibre + Salba + ginseng (combinations), satiety and postprandial single-meal studies, sport-performance '
    'trials, topical chia oil pruritus study, a small HDL study without randomization details.')

# ================================================================== sage
PLAN['salvia_officinalis'] = [
    ('add', 'menopause', ['REF-5644']),
    ('note', 'menopause',
     'Sage reduced menopausal hot flashes in a meta-analysis of trials; in a 2021 randomized double-blind trial in 80 '
     'menopausal women, fresh sage extract tablets (Menosan) for 4 weeks lowered the overall menopause rating score by '
     'about 39% versus placebo, including physical and psychological symptoms; its extract had estrogen-like effects in '
     'rats (preclinical)'),
    ('add', 'blood-sugar', ['REF-5645']),
    ('note', 'blood-sugar',
     'Sage leaves improved blood sugar control in hyperlipidaemic type 2 diabetes in a randomized trial; a 2023 '
     'meta-analysis of three RCTs in diabetes found lower fasting blood sugar and HbA1c with sage'),
    ('add', 'high-cholesterol', ['REF-5645']),
    ('note', 'high-cholesterol',
     'Sage leaf extract lowered total and LDL cholesterol and raised HDL vs placebo in randomized trials; a 2023 '
     'meta-analysis of three RCTs in diabetes found lower total and LDL cholesterol (triglycerides and HDL unchanged)'),
    ('newpair', 'low-libido', ['REF-5646'],
     'In a 2023 randomized controlled trial in postmenopausal women, inhaling sage (Salvia officinalis) scent for 6 weeks '
     'improved sexual function and satisfaction scores compared with a control group'),
]
NOTES['salvia_officinalis'] = (
    'Searched PubMed (Salvia officinalis / common or garden sage / sage leaf, leaves, extract or tea tiab; bare "sage" '
    'was not searched because it matches the SAGE publisher and acronyms, and Spanish sage S. lavandulifolia is a '
    'different species: 72 HT, 20 SR, 151 SAFE hits), Europe PMC, ClinicalTrials.gov (100) and OpenAlex. Research-'
    'integrity check: no new reference is first- or last-authored by the flagged Tehran psychopharmacology group (author '
    'lists checked); existing cognitive-function and memory pairs were left as they are. Cognitive-function and memory '
    '(9) were not padded. Added: 2021 Menosan RCT to menopause (overall menopause rating; not added to hot-flashes '
    'because the 2023 hot-flash meta-analysis already cited likely pools it); 2023 diabetes meta-analysis to blood-sugar '
    'and high-cholesterol (its pooled 2016 statin add-on RCT was not cited separately); NEW low-libido pair (2023 '
    'aromatherapy RCT). Not added: 2019 and 2020 Iranian menopause studies (within-group or unclear between-group '
    'analysis), 2024 periodontitis split-mouth gel trial (within-group), 2021 abdominal massage with sage oil for '
    'chemotherapy nausea (no difference at one week), PCOS insulin-resistance and lipid trials (surrogate; no PCOS '
    'condition), sage vs benzydamine and sage vs clotrimazole (active comparators), "clary sage" study labelled S. '
    'officinalis (species unclear), sage + rosemary + melissa and other mouthwash/lozenge combinations, 2012 ADT hot-'
    'flash pilot (single-arm), 2012 child seizure letter (no abstract).')

# ================================================================== rosemary
PLAN['salvia_rosmarinus'] = [
    ('add', 'anxiety', ['REF-5647']),
    ('note', 'anxiety',
     'Rosemary reduced anxiety in randomized trials in students, in major depression as an add-on, and before surgery '
     '(aromatherapy); in a 2025 randomized double-blind placebo-controlled crossover trial in 40 healthy adults, rosemary '
     'extract for 4 weeks lowered trait anxiety'),
    ('newpair', 'fatigue', ['REF-5648'],
     'In a 2021 randomized controlled trial in 80 shift-working nurses, inhaling rosemary essential oil reduced night-'
     'shift sleepiness and increased alertness compared with no aroma'),
    ('newpair', 'sore-throat', ['REF-5649'],
     'In a 2025 randomized trial in 90 people having endotracheal intubation for kidney-stone surgery, gauze soaked in '
     'rosemary extract placed in the throat reduced post-operative sore throat and hoarseness compared with distilled '
     'water'),
]
NOTES['salvia_rosmarinus'] = (
    'Searched PubMed (Salvia rosmarinus / Rosmarinus officinalis / rosemary tiab: 189 HT, 39 SR, 446 SAFE hits; most '
    'SAFE hits were food-preservation and animal studies), Europe PMC, ClinicalTrials.gov (16) and OpenAlex. Research-'
    'integrity check: none of the new trials is from the flagged group. Cognitive-function and memory (9) were not '
    'padded. Added: 2025 Japanese crossover to anxiety; NEW fatigue pair (2021 nurses inhalation RCT) and NEW '
    'sore-throat pair (2025 post-intubation RCT). Not added: 2022 NAFLD rosemary powder + diet RCT (no difference from '
    'placebo except one insulin index; there is no liver pair), 2019 rosemary tea in type 2 diabetes (single-arm), 2020 '
    'post-hoc mood subgroup (8 vs 13 people), rosemary vs minoxidil, vs mefenamic acid, vs ketoconazole and vs menthol '
    '(active comparators), lavender + rosemary and other aromatherapy blends, multi-ingredient supplements and '
    'toothpastes, 2013 opium withdrawal and 2014 low-blood-pressure studies (no vocabulary condition), hair-growth trials '
    '(no vocabulary condition).')

# ================================================================== elder
PLAN['sambucus_nigra'] = []
POST['sambucus_nigra'] = [
    ('cinew', {'note': 'Pancreas: a 75-year-old woman taking daily black elderberry extract developed mild acute '
                       'pancreatitis that settled after she stopped it; causality was rated possible because other causes '
                       'could not be fully excluded (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5652']}),
    ('cinew', {'note': 'Liver: a person developed autoimmune hepatitis while taking elderberry-containing supplements long '
                       'term; the authors consider the association plausible (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5653']}),
    ('dcinew', {'drug_class': 'chemotherapy-agents', 'severity': 'insufficient',
                'mechanism': 'A woman who had taken elderberry flower supplements for years developed severe nausea, '
                             'diarrhoea and grade 3 liver injury four weeks after starting the cancer drug pazopanib; liver '
                             'tests recovered after both were stopped, and the authors suggest a possible interaction '
                             '(case report).',
                'reference_ids': ['REF-5654']}),
]
NOTES['sambucus_nigra'] = (
    'Searched PubMed (Sambucus nigra / elderberry / elderberries / black elderberry / European elder / Sambucol / '
    'elderflower tiab; bare "elder" was not searched because it matches older people: 96 HT, 14 SR, 122 SAFE hits; many '
    'hits use Sambucus nigra lectin as a laboratory glycan stain), Europe PMC, ClinicalTrials.gov (11) and OpenAlex. '
    'Cold (9) and respiratory-support (8) were not padded. Added: 2026 possible pancreatitis case and 2022 autoimmune '
    'hepatitis case as cautions; 2024 pazopanib liver-injury case as a DRAFT chemotherapy-agents interaction '
    '(insufficient; needs owner approval). Not added: American elderberry (Sambucus canadensis) cognition trials (other '
    'species), one-week elderberry juice metabolic studies (surrogate), lutein + zeaxanthin + elderberry dry-eye trial, '
    'elderberry + violet + calendula COPD study, Sinupret-type combinations and pediatric immune blends (combinations), '
    '2020 pancreatitis case (no abstract).')

# ================================================================== soapwort
PLAN['saponaria_officinalis'] = []
NOTES['saponaria_officinalis'] = (
    'Searched PubMed (Saponaria officinalis / soapwort / bouncing bet tiab: 2 HT, 1 SR, 18 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (0) and OpenAlex. Nothing new: the 2020 acne trial tested a cream combining soapwort, elecampane '
    'and black nightshade (combination); most other hits concern saporin, a soapwort protein used to build research and '
    'experimental cancer immunotoxins (not use of the plant). Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r30_changes.tsv')
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
