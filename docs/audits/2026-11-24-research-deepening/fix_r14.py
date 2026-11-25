"""Research-deepening batch 14 (foeniculum-vulgare, fomitopsis-betulina, galium-album, galium-aparine, ganoderma-lingzhi).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5356.. (reserved)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 14'

SPEC = [
    # fennel
    ('REF-5356', '23926506', 'fennelpms', 'rct'),
    ('REF-5357', '32835919', 'fennelkneeosteoarthritis', 'rct'),
    ('REF-5358', '29755029', 'fennelmenopauseplacebo', 'rct'),
    ('REF-5359', '26325431', 'pregnancyherbssouthitaly', 'clinical'),
    ('REF-5360', '18970951', 'fennelprematurethelarche', 'clinical'),
    ('REF-5361', '24030028', 'fenneltealthelarche', 'clinical'),
    ('REF-5362', '1957997', 'spiceallergycelery', 'clinical'),
    ('REF-5363', '24067338', 'mugwortfennelallergy', 'clinical'),
    ('REF-5364', '10460442', 'plantinducedseizures', 'clinical'),
    # lingzhi (Ganoderma lucidum in East Asian research counts for G. lingzhi, inv. 11)
    ('REF-5365', '18097505', 'reishiluts', 'rct'),
    ('REF-5366', '18097503', 'reishilutsdose', 'rct'),
    ('REF-5367', '40077714', 'reishisporeoillipids', 'rct'),
    ('REF-5368', '27511742', 'reishimetabolicsyndrome', 'rct'),
    ('REF-5369', '41438309', 'reishikombuchat2dm', 'rct'),
    ('REF-5370', '17597499', 'reishisafetyhealthy', 'rct'),
    ('REF-5371', '2098581', 'reishiplatelets', 'clinical'),
    ('REF-5372', '37885515', 'reishiliverinjury', 'clinical'),
    ('REF-5373', '34911873', 'reishieosinophilia', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== fennel
PLAN['foeniculum_vulgare'] = [
    ('newpair', 'pms', ['REF-5356'],
     'Fennel extract reduced premenstrual syndrome symptoms more than placebo in a single-blind randomized trial in students'),
    ('newpair', 'arthritis', ['REF-5357'],
     'Fennel seed extract capsules reduced knee pain and improved WOMAC scores more than placebo after two weeks in women with '
     'knee osteoarthritis (randomized double-blind trial)'),
    ('nulladd', 'menopause', ['REF-5358']),
    ('note', 'menopause', 'Fennel improved menopausal symptoms vs placebo in a meta-analysis and a randomized trial, though another '
     'placebo-controlled trial found no difference because of a high placebo response'),
]
POST['foeniculum_vulgare'] = [
    ('cinew', {'note': 'Children: long-term use of fennel preparations or fennel tea in babies and young girls has been linked to '
                       'premature breast development (premature thelarche), which regressed after fennel was stopped (case '
                       'reports).',
               'severity': 'caution', 'reference_ids': ['REF-5360', 'REF-5361']}),
    ('cinew', {'note': 'Essential oil: fennel essential oil is among the plant oils known to provoke seizures, because of ketones '
                       'such as fenchone (case series with literature review).',
               'severity': 'caution', 'reference_ids': ['REF-5364']}),
]
FEN_PREG = ('Pregnancy: in an observational study of 600 women in southern Italy, regular fennel use during pregnancy was linked '
            'to a shorter pregnancy (an association, not proof of harm).')
FEN_ALLERGY = ('Allergy: people allergic to celery, birch or mugwort pollen often react to fennel and other carrot-family spices '
               'in skin tests (the celery-mugwort-spice syndrome), and a combined fennel and mugwort allergy has been traced to a '
               'shared allergen (allergy studies).')
NOTES['foeniculum_vulgare'] = (
    'Searched PubMed (Foeniculum vulgare / fennel tiab: 140 HT, 44 SR, 239 SAFE hits; SR/MA, safety and single-herb trials '
    'read in depth), Europe PMC, ClinicalTrials.gov (22) and OpenAlex. Menstrual cramps and pain (9) are already MA-backed and '
    'were not padded. Added: NEW pms pair (2011 single-blind placebo RCT, Shahrekord); NEW arthritis pair (2020 double-blind '
    'placebo RCT in knee osteoarthritis); 2018 placebo RCT (high placebo response, no difference) as no-effect for menopause; '
    'premature thelarche (2008 series, 2014 case) and essential-oil seizure (1999 series and review) cautions. SOURCED TWO '
    'UNSOURCED NOTES (needs-review, consumer-database wording): the pregnancy note said fennel "has been linked to preterm '
    'birth" - the 2012 Italian cohort linked ALMOND OIL to preterm birth, and the 2015 southern-Italy cohort linked regular '
    'fennel to a shorter gestational age, so the note was rewritten to the 2015 finding; the celery / carrot / mugwort allergy '
    'note was rewritten to what the 1991 skin-test study and the 2013 mugwort-fennel case state (carrot not named). The other '
    'unsourced notes (oral and skin safety, breastfeeding neurotoxicity, infant colic, bleeding, hormone-sensitive conditions) '
    'are unchanged and still need sources. Not added: fennel sleep RCT 2018 (no difference), lipid RCT 2018 (no difference), '
    'fennel seed powder and sexual desire 2020 (no difference), menstrual-bleeding MA 2018 (no abstract), vaginal creams '
    '(vaginal atrophy, no vocab condition), hirsutism gels, fennel vs dimethicone, mefenamic acid or evening primrose (active '
    'comparators), fennel + chamomile, saffron, valerian, Rosa damascena, Echium, ginger, curcumin and other combinations, '
    'the 2020 Cochrane galactagogue review (fennel not separable in the abstract), heated fennel compresses.')

# ================================================================== lingzhi
PLAN['ganoderma_lingzhi'] = [
    ('newpair', 'prostate-support', ['REF-5365', 'REF-5366'],
     'An ethanol extract of reishi improved urinary symptom scores (IPSS) more than placebo in men with lower urinary tract '
     'symptoms in two randomized trials, without changing prostate size or PSA'),
    ('newpair', 'high-cholesterol', ['REF-5367'],
     'Reishi spore oil lowered cholesterol and triglycerides vs placebo in a 2025 randomized crossover trial, but a '
     'fruiting-body extract had no effect on cardiovascular risk factors in a 2016 placebo-controlled trial, and a Cochrane '
     'review found the evidence does not support reishi for cardiovascular risk factors'),
    ('nulladd', 'high-cholesterol', ['REF-5368', 'REF-3559']),
    ('add', 'blood-sugar', ['REF-5369']),
    ('nulladd', 'blood-sugar', ['REF-5368']),
    ('note', 'blood-sugar', 'Results are mixed: a 2025 randomized trial found lower fasting glucose and HbA1c than in controls in '
     'type 2 diabetes, but a 2016 placebo-controlled trial found no effect on HbA1c and a Cochrane review found the trials do '
     'not support reishi for blood sugar; antidiabetic effects in lab and animal studies (review)'),
]
POST['ganoderma_lingzhi'] = [
    ('ciadd', 'Generally well tolerated at standard doses', ['REF-5370', 'REF-5371']),
    ('cinew', {'note': 'Liver: acute hepatitis has been reported after taking reishi powder with alcohol, and in another case a '
                       'reishi product caused very high eosinophil counts with liver nodules that cleared after it was stopped '
                       '(case reports).',
               'severity': 'caution', 'reference_ids': ['REF-5372', 'REF-5373']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'In patients with atherosclerotic disease, reishi (1 g three times a day for 2 weeks) reduced '
                             'platelet aggregation by up to about 30% (clinical study), so it may add to the effect of '
                             'antiplatelet and anticoagulant medicines.',
                'reference_ids': ['REF-5371']}),
]
NOTES['ganoderma_lingzhi'] = (
    'Searched PubMed (Ganoderma lingzhi / G. lucidum / reishi / lingzhi tiab, Ganoderma ti: 110 HT, 37 SR, 471 SAFE hits; '
    'SR/MA, safety and single-product trials read in depth), Europe PMC, ClinicalTrials.gov (51) and OpenAlex. "Ganoderma '
    'lucidum" in East Asian research counts here (inv. 11). Added: NEW prostate-support pair (two 2008 placebo RCTs in men '
    'with LUTS, IPSS improved); NEW high-cholesterol pair (2025 spore-oil crossover RCT) with the 2016 Klupp placebo RCT and '
    'the Cochrane review REF-3559 as no-effect; 2025 RCT vs kombucha and control to blood-sugar with the 2016 RCT as '
    'no-effect (note says mixed); 2007 healthy-volunteer safety RCT and the 1990 platelet study to the safety note; liver '
    'caution (2023 hepatitis case, 2021 eosinophilic liver nodules); DRAFT anticoagulant interaction from the platelet study '
    '(needs owner sign-off). Not added: liver-support from a 2017 crossover RCT in healthy volunteers (lower liver enzymes) - '
    'withheld alongside the new liver-injury caution (inv. 12d spirit); spore powder in Alzheimer\'s disease 2018 (no '
    'difference); immune RCTs (pair already 7, not padded); fibromyalgia mood and fitness trials (no vocab condition); '
    'Ganoderma + Cordyceps, San Miao San, Lion\'s mane blend and other combinations; the 2020 Lingzhi/Yunzhi interaction SR '
    '(no Lingzhi pharmacokinetic study); G. applanatum, G. tsugae, G. sinense and other species.')

# ================================================================== birch polypore, bedstraws
PLAN['fomitopsis_betulina'] = []
NOTES['fomitopsis_betulina'] = (
    'Searched PubMed (Fomitopsis betulina / Piptoporus betulinus / birch polypore tiab): 0 HT, 0 SR, 0 SAFE hits; Europe '
    'PMC, ClinicalTrials.gov (0) and OpenAlex found nothing beyond the 2026-11-16 deep search. Still no human study. Settled.')
PLAN['galium_album'] = []
NOTES['galium_album'] = (
    'Searched PubMed (Galium album / G. mollugo / white / hedge bedstraw tiab): 0 HT, 0 SR, 1 SAFE hit (unrelated); Europe '
    'PMC, ClinicalTrials.gov (0) and OpenAlex found no human study. Settled.')
PLAN['galium_aparine'] = []
NOTES['galium_aparine'] = (
    'Searched PubMed (Galium aparine / cleavers / goosegrass tiab: 1 HT, 0 SR, 11 SAFE hits, mostly weed science), Europe '
    'PMC, ClinicalTrials.gov (0) and OpenAlex. No human study of cleavers. Settled.')


def text_edits():
    """Rewrite two unsourced fennel notes to what their new sources state (rd_fix ops do not rewrite text)."""
    path = 'plants/foeniculum_vulgare.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    cp = [c for c in d['contraindications'] if c['note'].startswith('Pregnancy: Fennel is possibly unsafe')]; assert len(cp) == 1
    cp[0].update(note=FEN_PREG, status='verified', severity='caution'); cp[0]['reference_ids'] = ['REF-5359']
    ca = [c for c in d['contraindications'] if c['note'].startswith('Allergy to celery, carrot or mugwort')]; assert len(ca) == 1
    ca[0].update(note=FEN_ALLERGY, status='verified', severity='caution'); ca[0]['reference_ids'] = ['REF-5362', 'REF-5363']
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r14_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        text_edits()
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
