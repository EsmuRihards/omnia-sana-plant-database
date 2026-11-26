"""Research-deepening batch 15 (gentiana-lutea, geum-rivale, ginkgo-biloba, glycyrrhiza-glabra, gymnema-sylvestre).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5374.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 15'

SPEC = [
    # ginkgo
    ('REF-5374', '19678774', 'ginkgopms', 'rct'),
    ('REF-5375', '24949064', 'ginkgosexualdesire', 'rct'),
    ('REF-5376', '34290964', 'ginkgosexualfunctionsr', 'systematic-review'),
    ('REF-5377', '12404672', 'ginkgoantidepressantsexual', 'rct'),
    ('REF-5378', '15378664', 'ginkgoantidepressantsexual2004', 'clinical'),
    ('REF-5379', '33090588', 'ginkgot2dmcardiometabolic', 'meta-analysis'),
    ('REF-5380', '29670330', 'ginkgometformint2dm', 'rct'),
    ('REF-5381', '21923430', 'ginkgobleedingrisk', 'meta-analysis'),
    ('REF-5382', '43030747', 'ginkgoclaudication', 'meta-analysis'),
    # licorice
    ('REF-5383', '36451559', 'licoricegargleaphthous', 'rct'),
    ('REF-5384', '32090748', 'glycyrrhizicaciddepression', 'rct'),
    ('REF-5385', '27614124', 'licoricehpylori', 'rct'),
    ('REF-5386', '29433679', 'licoricemetabolicchanges', 'meta-analysis'),
    ('REF-5387', '19808634', 'maternallicoricechildren', 'clinical'),
    ('REF-5388', '28158597', 'maternallicoricepuberty', 'clinical'),
    # gymnema
    ('REF-5389', '20856101', 'gymnemahepatitis', 'clinical'),
    ('REF-5390', '32626054', 'gymnemariskassessment', 'narrative-review'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== ginkgo
PLAN['ginkgo_biloba'] = [
    ('newpair', 'pms', ['REF-5374'],
     'Ginkgo extract reduced the overall severity of premenstrual syndrome symptoms more than placebo in a randomized trial'),
    ('newpair', 'low-libido', ['REF-5375', 'REF-5376'],
     'Ginkgo extract improved sexual desire more than placebo in postmenopausal women in a triple-blind randomized trial, and a '
     '2021 systematic review found benefit in postmenopausal women but not for sexual problems caused by antidepressants, '
     'where placebo-controlled trials found no difference'),
    ('nulladd', 'low-libido', ['REF-5377', 'REF-5378']),
    ('newpair', 'blood-sugar', ['REF-5379', 'REF-5380'],
     'Ginkgo extract lowered HbA1c in a 2020 meta-analysis of trials in type 2 diabetes, though the authors judged the evidence '
     'too limited to be sure, and added to metformin it lowered HbA1c and fasting glucose in a placebo-controlled randomized '
     'trial'),
    ('add', 'cardiovascular-support', ['REF-5382']),
    ('note', 'cardiovascular-support', 'A 2026 meta-analysis of 14 placebo-controlled trials found a modest improvement in walking '
     'distance in peripheral arterial disease (intermittent claudication), clearer after 24 weeks, though an earlier Cochrane '
     'review found no clinically significant benefit; used for intermittent claudication (WHO monograph)'),
]
POST['ginkgo_biloba'] = [
    ('cinew', {'note': 'Bleeding: a 2011 meta-analysis of placebo-controlled trials found that standardized ginkgo extract did not '
                       'change blood-clotting measures in a way that would raise bleeding risk, although case reports link '
                       'ginkgo to bleeding, so the blood-thinner interaction still applies.',
               'severity': 'info', 'reference_ids': ['REF-5381']}),
]
NOTES['ginkgo_biloba'] = (
    'Searched PubMed (Ginkgo biloba tiab; ginkgo, EGb 761 ti: 872 HT, 284 SR, 1,094 SAFE hits; SR/MA and gap conditions '
    'read in depth, cognition not padded at 10), Europe PMC, ClinicalTrials.gov and OpenAlex. Added: NEW pms pair (2009 '
    'placebo RCT, Ozgoli); NEW low-libido pair (2014 triple-blind RCT in postmenopausal women; 2021 sexual-function SR) with '
    'two antidepressant-induced sexual dysfunction placebo trials (2002, 2004) as no-effect; NEW blood-sugar pair (2020 '
    'cardiometabolic MA in T2DM, HbA1c; 2018 metformin add-on placebo RCT); 2026 claudication MA (14 RCTs, modest benefit) '
    'to cardiovascular-support beside the null Cochrane review; 2011 bleeding-risk MA as an info note. Not added: 2014 '
    'essential-hypertension SR (no confirmative conclusion; trials vs antihypertensives), Pittler 2000 claudication MA '
    '(superseded), dizziness, tinnitus, sudden hearing loss, mountain sickness, ADHD, schizophrenia, tardive dyskinesia, '
    'glaucoma and vitiligo reviews (no vocab condition), Chinese ginkgo injections and patent medicines, combinations, '
    'preprints.')

# ================================================================== licorice
PLAN['glycyrrhiza_glabra'] = [
    ('add', 'oral-health', ['REF-5383']),
    ('note', 'oral-health', 'Topical licorice (paste, patch or mouthwash) helped recurrent mouth ulcers heal in clinical trials '
     '(systematic review), and a licorice gargle relieved mouth-ulcer pain more than placebo within a day in a randomized '
     'double-blind trial'),
    ('newpair', 'depression', ['REF-5384'],
     'Glycyrrhizic acid, licorice\'s signature compound, added to SSRI antidepressants relieved depression more than placebo, '
     'with higher response and remission rates, in a randomized trial (compound evidence)'),
    ('add', 'infection', ['REF-5385']),
    ('note', 'infection', 'Adding licorice to standard antibiotic treatment raised Helicobacter pylori eradication (83% vs 63%) in a '
     'randomized trial; traditional antiviral use, and pharmacopoeias list it for tuberculosis (WHO monograph)'),
]
POST['glycyrrhiza_glabra'] = [
    ('ciadd', 'Glycyrrhizin in whole licorice root', ['REF-5386', 'REF-5387', 'REF-5388']),
]
NOTES['glycyrrhiza_glabra'] = (
    'Searched PubMed (Glycyrrhiza glabra / licorice / liquorice tiab; glycyrrhizin, glycyrrhizic and glycyrrhetinic acid ti: '
    '470 HT, 98 SR, 1,720 SAFE hits; SR/MA, safety and gap conditions read in depth), Europe PMC, ClinicalTrials.gov and '
    'OpenAlex. Added: 2022 placebo RCT of licorice gargle for mouth-ulcer pain to oral-health; NEW depression pair '
    '(glycyrrhizic acid + SSRI vs placebo RCT 2020, compound evidence); 2016 H. pylori add-on RCT to infection; to the '
    'glycyrrhizin warning, the 2018 metabolic MA (diastolic BP +1.7 mmHg) and the Finnish maternal-licorice cohorts (2009, '
    '2017: high glycyrrhizin intake in pregnancy linked to lower IQ, poorer memory, more ADHD problems and earlier puberty in '
    'the children). Not added: caries SRs (Streptococcus mutans counts, a surrogate), periodontitis gels vs tetracycline, '
    'dysmenorrhoea vs ibuprofen, licorice vs oestrogen vaginal cream (active comparators), weight (2018 MA -0.4 kg; '
    'conflicts with the BP warning, inv. 12d) and the 2017 obesity RCT (no difference), atopic dermatitis (2017 SR: '
    'insufficient evidence; dipotassium glycyrrhizinate emollient and compound glycyrrhizin products), hot flushes (2016 SR '
    'lists licorice generically), PCOS and vaginal atrophy (no vocab condition), DGL peptic-ulcer trials of the 1970s, '
    'glycyrrhizin injections, compound glycyrrhizin, Kampo and Chinese formulas.')

# ================================================================== gymnema
PLAN['gymnema_sylvestre'] = []
POST['gymnema_sylvestre'] = [
    ('ciadd', 'Gymnema lowers blood sugar and can add', ['REF-5390']),
    ('cinew', {'note': 'Liver: a patient taking gymnema for type 2 diabetes developed drug-induced (toxic) hepatitis (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5389']}),
]
NOTES['gymnema_sylvestre'] = (
    'Searched PubMed (Gymnema sylvestre / gymnema / gurmar tiab, gymnemic acid ti: 40 HT, 13 SR, 75 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (18) and OpenAlex. Blood sugar (10), metabolic support and cholesterol (9) were not padded '
    '(2017 and 2021 RCTs in metabolic syndrome and T2DM logged here). Added: 2010 toxic hepatitis case as a liver caution; '
    'the 2018 EFSA/EU-FORA risk assessment (limited evidence of adverse effects; may enhance antidiabetic drugs) to the '
    'hypoglycaemia caution. Not added: sweet-taste and sugar-craving trials (no vocab condition), combinations (myo-inositol, '
    'Zea mays, Hyponidd and other Ayurvedic mixtures, including an interstitial nephritis case), homeopathic add-on trial, '
    'a 2026 hypersensitivity case (no abstract), other Gymnema species.')

# ================================================================== gentian, water avens
PLAN['gentiana_lutea'] = []
NOTES['gentiana_lutea'] = (
    'Searched PubMed (Gentiana lutea / yellow gentian / gentian root tiab: 10 HT, 1 SR, 25 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (2) and OpenAlex. No new single-herb trial for its pairs: the 2016 microencapsulated-bitter study '
    'measured energy intake in healthy people (not appetite loss or dyspepsia); the rest are combinations (Sinupret, '
    'gentian + licorice cream, gentian + ginger + turmeric) or Veratrum poisonings (a gentian lookalike). Settled.')
PLAN['geum_rivale'] = []
NOTES['geum_rivale'] = (
    'Searched PubMed (Geum rivale / water avens tiab): 0 HT, 0 SR, 0 SAFE hits; Europe PMC, ClinicalTrials.gov and '
    'OpenAlex found no human study. Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r15_changes.tsv')
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
