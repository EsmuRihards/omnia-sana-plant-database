"""Research-deepening batch 20 (linum-usitatissimum, lysimachia-vulgaris, mahonia-aquifolium, malva-sylvestris,
marrubium-vulgare). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5467.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 20'

SPEC = [
    # flax
    ('REF-5467', '38663513', 'flaxseednafldmeta', 'meta-analysis'),
    ('REF-5468', '26983396', 'flaxseednafldpilot', 'rct'),
    ('REF-5469', '30806856', 'flaxseedpoulticehandoa', 'rct'),
    ('REF-5470', '39759908', 'flaxseedendometriosispain', 'rct'),
    ('REF-5471', '29245212', 'flaxseedanaphylaxiskorea', 'clinical'),
    ('REF-5472', '34085936', 'flaxseedallergens', 'clinical'),
    ('REF-5473', '33303502', 'flaxseedoilgynecomastia', 'clinical'),
    ('REF-5474', '37927501', 'flaxseedsexhormonesmeta', 'meta-analysis'),
    ('REF-5475', '25708890', 'linseedcyanide', 'clinical'),
    ('REF-5476', '40421205', 'flaxseeddabigatran', 'rct'),
    ('REF-5477', '36380973', 'herbsplateletaggregation', 'systematic-review'),
    # Oregon grape
    ('REF-5478', '38304488', 'oregongrapepglycoprotein', 'preclinical'),
    # mallow
    ('REF-5479', '30585511', 'phytodermatitisturkey', 'clinical'),
    # horehound
    ('REF-5481', '34431289', 'marrubiinbioactivation', 'preclinical'),
    # flax (Europe PMC follow-up)
    ('REF-5482', '23577799', 'flaxlignanhypoglycemiasafety', 'rct'),
]
DOI_SPEC = [
    ('REF-5480', '10.22038/ijogi.2024.79693.6082', 'mallowepisiotomypain', 'rct',
     {'journal': 'Iranian Journal of Obstetrics, Gynecology and Infertility'}),
]


def bib_new():
    new = deep_lib.newrefs(SPEC)
    for rid, doi, slug, st, over in DOI_SPEC:
        _, (r, fields) = rd_doi.newref_doi(doi, rid, 'x', st)
        f = dict(fields)
        au = [_initials(a.strip()) for a in rd_doi.fetch(doi)['authors']]
        f['author'] = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
        f.update(over)
        order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'pmid', 'note', 'study_type', 'abstract']
        new[_ascii(f['author'].split(',')[0]) + f['year'] + slug] = (rid, [(k, f[k]) for k in order if k in f])
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== flax
PLAN['linum_usitatissimum'] = [
    ('newpair', 'liver-support', ['REF-5467', 'REF-5468'],
     'Flaxseed lowered the liver enzyme ALT and blood triglycerides in people with non-alcoholic fatty liver disease in a '
     'meta-analysis of randomized trials, and 30 g a day of ground flaxseed with lifestyle advice reduced liver fibrosis and '
     'fat (steatosis) scores more than lifestyle advice alone (randomized trial)'),
    ('add', 'arthritis', ['REF-5469']),
    ('note', 'arthritis',
     'A warm flaxseed poultice applied to the hands once a day for 7 days eased pain and improved hand function in hand '
     'osteoarthritis more than a hot compress or no extra treatment (randomized trial)'),
    ('newpair', 'menstrual-cramps', ['REF-5470'],
     'Flaxseed capsules (1 g three times a day for 8 weeks) reduced period pain, pelvic pain and pain during sex compared '
     'with placebo in women with endometriosis (randomized trial)'),
]
POST['linum_usitatissimum'] = [
    ('cinew', {'note': 'Allergy: flaxseed can cause severe allergic reactions, including anaphylaxis; one woman reacted to half '
                       'a teaspoon of flaxseed flour (case report). Its seed storage proteins (2S albumin, Lin u 1, and 11S '
                       'globulin) were the allergens in five people with severe reactions, and Lin u 1 cross-reacted with '
                       'peanut and cashew proteins in lab tests (patient study).',
               'severity': 'caution', 'reference_ids': ['REF-5471', 'REF-5472']}),
    ('cinew', {'note': 'Hormones: a 70-year-old man developed breast enlargement (gynaecomastia) three months after starting a '
                       'daily tablespoon of flaxseed oil (case report); a meta-analysis of ten randomized trials found flaxseed '
                       'did not significantly change sex hormones such as FSH, SHBG or testosterone.',
               'severity': 'info', 'reference_ids': ['REF-5473', 'REF-5474']}),
    ('cinew', {'note': 'Cyanide: flaxseed contains cyanogenic glycosides. In a crossover study in 12 adults, a linseed meal '
                       'containing 6.8 mg of cyanide equivalents raised blood cyanide to a peak of about 5.7 micromolar, '
                       'roughly a third of the peak after cassava or bitter apricot kernels with the same amount, because '
                       'linseed releases its cyanide more slowly.',
               'severity': 'info', 'reference_ids': ['REF-5475']}),
    ('cinew', {'note': 'Medicines: in a small randomized crossover study in healthy volunteers, 30 g of flaxseed taken with the '
                       'blood thinner dabigatran lowered dabigatran exposure (AUC) compared with placebo, although the authors '
                       'concluded flaxseed did not affect its pharmacokinetics overall.',
               'severity': 'info', 'reference_ids': ['REF-5476']}),
    ('cinew', {'note': 'Blood sugar and blood pressure: in a 6-month randomized double-blind trial in adults aged 49-87, a flax '
                       'lignan supplement (543 mg a day) caused no episodes of low blood sugar or low blood pressure.',
               'severity': 'info', 'reference_ids': ['REF-5482']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'insufficient',
                'mechanism': 'Flaxseed reduced platelet aggregation in randomized trials in healthy people (systematic review). '
                             'In a small crossover study, 30 g of flaxseed lowered exposure to the anticoagulant dabigatran in '
                             'one comparison, though the authors concluded it did not meaningfully affect the drug.',
                'reference_ids': ['REF-5477', 'REF-5476']}),
]
NOTES['linum_usitatissimum'] = (
    'Searched PubMed (Linum usitatissimum / flaxseed / flax seed / linseed tiab, flax and secoisolariciresinol ti: 606 HT, 110 '
    'SR, 543 SAFE hits), Europe PMC (flax queries timed out and were re-run), ClinicalTrials.gov (109) and OpenAlex. Huge '
    'plant: screened the SR family, conditions without a pair and safety; blood sugar (9), blood pressure (9), cholesterol '
    '(8), metabolic support (8), inflammation (7) and constipation (6) were not padded, and ALA-only or mixed omega-3 '
    'studies were not counted as flaxseed. Added: NEW liver-support pair (2024 NAFLD MA; 2016 randomized open-label trial, '
    'between-group fibrosis and steatosis differences); hand-osteoarthritis poultice RCT to arthritis; NEW menstrual-cramps '
    'pair (2024 block-randomized placebo RCT in endometriosis); allergy caution (anaphylaxis case, storage-protein patient '
    'study); hormone info note (gynaecomastia case with the null sex-hormone MA); cyanide info note (2016 human crossover '
    'study); dabigatran info note; flax-lignan safety RCT (no hypoglycaemia or hypotension, found via Europe PMC) as an info '
    'note; DRAFT anticoagulants-antiplatelets interaction (insufficient; platelet SR + dabigatran '
    'study). Not added: menopause and hot flushes (2013 SR of controlled flax trials found no difference from control and '
    'judged flax not indicated for vasomotor symptoms; a 2016 MA found a non-significant benefit; a 2024 single-blind Cureus '
    'RCT reported large benefits, so the evidence is conflicting and no pair was created); 2025 NAFLD RCT 39878023 (within-'
    'group changes only in the abstract); 2021 flaxseed + hesperidin NAFLD trial (factorial, mostly vs baseline); 2018 '
    'topical flaxseed oil knee OA RCT 29705472 (no abstract); 2020 flaxseed-oil artificial tear (differs from its '
    'comparator by two ingredients, trehalose and flaxseed oil, and the primary endpoint did not differ); 2025 flaxseed oil '
    'vs betamethasone in psoriasis (active comparator); 2014 topical linseed oil RCT in carpal tunnel syndrome (better '
    'symptom and function scores vs placebo; no vocab condition for nerve entrapment) and 2017 flaxseed-oil gel vs splint '
    '(active comparator); PCOS trials (no vocab condition; 29117618 carries a 2018 note of '
    'concern); IVF oocyte, mastalgia and lupus nephritis studies (no vocab condition, single-arm, or not significant); 2021 '
    'OTC constipation SR (only a yogurt + prunes + linseed oil combination); 2014 flax and breast cancer SR (re-reviews the '
    'trial already on the cancer pair); 2018 raw-smoothie cyanide survey (journal of uncertain standing); anaphylaxis, '
    'rhinoconjunctivitis and pseudolymphoma reports with no abstract.')

# ================================================================== yellow loosestrife
PLAN['lysimachia_vulgaris'] = []
NOTES['lysimachia_vulgaris'] = (
    'Searched PubMed (Lysimachia vulgaris / yellow loosestrife / garden loosestrife tiab): 0 HT, 0 SR, 1 SAFE hit (the HPLC '
    'method paper already held); Europe PMC, ClinicalTrials.gov (0) and OpenAlex (38 no-PMID hits: invasive-plant ecology '
    'and lab work) found no human study. Settled.')

# ================================================================== Oregon grape
PLAN['mahonia_aquifolium'] = []
POST['mahonia_aquifolium'] = [
    ('ciadd', 'Berberine impairs the metabolism of some medicines', ['REF-5478']),
]
NOTES['mahonia_aquifolium'] = (
    'Searched PubMed (Mahonia aquifolium / Berberis aquifolium / Oregon grape / Relieva tiab: 15 HT, 3 SR, 19 SAFE hits; many '
    '"Relieva" hits were a sinus stent of the same name), Europe PMC, ClinicalTrials.gov (1, a combination) and OpenAlex. '
    'Psoriasis (9) and eczema (8) were not padded. Added: a 2023 cell study in which Oregon grape root extracts inhibited '
    'P-glycoprotein efflux of cyclosporine and digoxin, to the medicines caution. Not added: 1996 intraindividual psoriasis '
    'study and 1999 ointment biomarker study (psoriasis already 9), 2007 vehicle-controlled ointment with Viola and other '
    'herbs (combination), berberine-only reviews (shared with goldenseal, barberry and Coptis), homeopathic preparations, '
    'a 2026 eye injury from the spiny leaves (physical injury, not use of the herb).')

# ================================================================== mallow
PLAN['malva_sylvestris'] = [
    ('add', 'pain', ['REF-5480']),
    ('note', 'pain',
     'A mallow mouthwash eased chemotherapy mouth-sore pain in a randomized trial. For episiotomy pain the results are mixed: '
     'a mallow ointment reduced pain more than placebo on days 5 and 10 in one randomized triple-blind trial, but a cream did '
     'not in another; analgesic effects reported in lab and animal studies (reviews)'),
]
POST['malva_sylvestris'] = [
    ('cinew', {'note': 'Skin: mallow was among the plants that caused irritant contact dermatitis in a prospective study of 34 '
                       'patients with plant-related skin reactions in eastern Turkey.',
               'severity': 'info', 'reference_ids': ['REF-5479']}),
]
NOTES['malva_sylvestris'] = (
    'Searched PubMed (Malva sylvestris / common, high or blue mallow tiab, mallow ti: 21 HT, 3 SR, 39 SAFE hits; "mallow" '
    'also matched marsh mallow, Malva parviflora livestock poisoning and the Irish town of Mallow), Europe PMC, '
    'ClinicalTrials.gov (5) and OpenAlex (56 no-PMID hits). Added: 2024 triple-blind randomized placebo trial of mallow '
    'ointment for episiotomy pain (Iranian Journal of Obstetrics, Gynecology and Infertility; DOI only, OpenAlex abstract) '
    'to pain beside the null cream trial; irritant dermatitis from a 2019 prospective phytodermatitis study as an info note. '
    'GAP: constipation - the 2015 placebo-controlled flower-extract trial still does not state randomisation, and the 2024 '
    'food-supplement study is an uncontrolled consumer survey. Not added: 2026 J Herb Med episiotomy-healing report from '
    'the same group (no abstract); 2014 letter on fulminant liver and kidney failure linked to Malva sylvestris (no '
    'abstract; worth re-checking if the full text becomes available); 1948 report of mallow leaves confused with chamico '
    '(Datura) (no abstract); KalobaTUSS and other cough syrups, Persian compound mouthwashes, saliva substitutes, vaginal '
    'gels and eye drops with hyaluronic acid (combinations); Malva parviflora animal poisonings (other species).')

# ================================================================== horehound
PLAN['marrubium_vulgare'] = []
POST['marrubium_vulgare'] = [
    ('cinew', {'note': 'Liver: liver enzymes (CYP2C9, CYP2C19 and CYP3A4) convert marrubiin, horehound\'s main bitter compound, '
                       'into reactive metabolites in lab and rat studies, a furan-ring activation the authors link to possible '
                       'liver toxicity; whether this applies to people is not known.',
               'severity': 'info', 'reference_ids': ['REF-5481']}),
]
NOTES['marrubium_vulgare'] = (
    'Searched PubMed (Marrubium vulgare / white or common horehound tiab, horehound and marrubiin ti: 4 HT, 1 SR, 21 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex (70 no-PMID hits, mostly lab, ethnobotany and diabetes surveys). '
    'Added: a 2021 study of marrubiin metabolic activation (furan ring, CYP2C9/2C19/3A4, rat bile) as an info note. Not '
    'added: 2024 acute kidney injury case after a three-plant mixture (with wormwood and centaury; not attributable); '
    'SEDIFLU and other paediatric cough syrups (combinations); 2004 Cecropia vs Marrubium diabetes trial (already judged: '
    'no glucose effect for horehound); Moroccan and Algerian use surveys. Settled for human efficacy: no trial of horehound '
    'alone.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r20_changes.tsv')
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
