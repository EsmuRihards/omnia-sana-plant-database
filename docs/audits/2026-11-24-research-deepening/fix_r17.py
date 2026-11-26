"""Research-deepening batch 17 (hippophae-rhamnoides, humulus-lupulus, hydrastis-canadensis, hypericum-perforatum,
hyssopus-officinalis). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5404.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 17'

SPEC = [
    # sea buckthorn
    ('REF-5404', '20554904', 'seabuckthornoildryeye', 'rct'),
    ('REF-5405', '30497904', 'seabuckthornspraydryeye', 'clinical'),
    ('REF-5406', '33917994', 'seabuckthornglucose', 'rct'),
    ('REF-5407', '12854177', 'seabuckthornliverfibrosis', 'rct'),
    ('REF-5408', '22759730', 'seabuckthornyellowskin', 'clinical'),
    # hops
    ('REF-5409', '26960416', 'maturedhopbodyfat', 'rct'),
    ('REF-5410', '43007037', 'hopsbetaacidsbreath', 'meta-analysis'),
    ('REF-5411', '32285669', 'hopdruginteractions', 'clinical'),
    ('REF-5412', '12512192', 'hopurticaria', 'clinical'),
    ('REF-5413', '39519459', 'hopallergenicity', 'preclinical'),
    # goldenseal
    ('REF-5414', '39943692', 'goldensealmetformin', 'clinical'),
    ('REF-5415', '14551183', 'goldensealindinavir', 'clinical'),
    ('REF-5416', '17079360', 'goldensealdigoxin', 'rct'),
    ('REF-5417', '17585008', 'goldensealhypernatremia', 'clinical'),
    ('REF-5418', '21300790', 'goldensealrodenttoxicity', 'preclinical'),
    # St John's wort
    ('REF-5419', '27444983', 'sjwcontraceptives', 'systematic-review'),
    # hyssop
    ('REF-5420', '39959798', 'hyssopasthma', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== sea buckthorn
PLAN['hippophae_rhamnoides'] = [
    ('newpair', 'eye-strain', ['REF-5404', 'REF-5405'],
     'Oral sea buckthorn oil (2 g a day) limited the rise in tear-film osmolarity and eased dry-eye redness and burning vs '
     'placebo in a randomized double-blind trial, and a sea buckthorn oil spray on closed eyelids relieved dry-eye symptoms '
     'more than a reference spray'),
    ('add', 'blood-sugar', ['REF-5406']),
    ('note', 'blood-sugar', 'Results are mixed: a meta-analysis of trials found no effect on blood sugar, while sea buckthorn fruit '
     'puree slightly lowered fasting glucose vs placebo in people with impaired glucose regulation (randomized crossover '
     'trial); reviewed for blood-sugar benefits (review)'),
    ('newpair', 'liver-support', ['REF-5407'],
     'A sea buckthorn extract lowered blood markers of liver fibrosis and sped the normalisation of liver enzymes compared with '
     'a vitamin B control in people with cirrhosis (randomized trial)'),
]
POST['hippophae_rhamnoides'] = [
    ('cinew', {'note': 'Skin colour: eating large amounts of sea buckthorn for months turned a man\'s skin yellow (from its '
                       'carotenoid pigments); it is harmless but can be mistaken for jaundice (case report).',
               'severity': 'info', 'reference_ids': ['REF-5408']}),
]
NOTES['hippophae_rhamnoides'] = (
    'Searched PubMed (Hippophae rhamnoides / sea buckthorn / seabuckthorn tiab: 63 HT, 14 SR, 151 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (7) and OpenAlex. Added: NEW eye-strain pair (2010 double-blind placebo RCT of oral oil in dry eye; '
    '2019 eyelid spray study); 2021 randomized crossover trial (fasting glucose -0.14 vs +0.07 mmol/L) to blood-sugar beside '
    'the null MA; NEW liver-support pair (2003 randomized trial in cirrhosis vs vitamin B control); yellow-skin case as an '
    'info note. Not added: 2018 postprandial trial (no effect on glucose; insulin only), nephrotic syndrome add-on study '
    '(randomisation not stated), cholesterol juice study (pair already 7), compound sea buckthorn suppositories and other '
    'combinations, tear-film fatty-acid and flavonol absorption studies (no clinical outcome), the retracted 2017 seed-oil RCT '
    '(already judged), acceptance and taste studies.')

# ================================================================== hops
PLAN['humulus_lupulus'] = [
    ('newpair', 'metabolic-support', ['REF-5409'],
     'A matured hop extract drink reduced visceral (belly) fat and overall body fat vs placebo over 12 weeks in healthy '
     'overweight adults (randomized double-blind trial)'),
    ('newpair', 'bad-breath', ['REF-5410'],
     'Toothpastes with a hops beta-acid extract reduced morning-breath sulphur compounds more than the same toothpaste without '
     'hops, more so at higher hop concentrations, in a pooled analysis of seven randomized company studies'),
]
POST['humulus_lupulus'] = [
    ('cinew', {'note': 'Medicines: a standardised hop extract taken for 2 weeks caused no clinically relevant change in drugs '
                       'cleared by CYP2C9, CYP1A2, CYP2D6 or CYP3A4 (only a 7.6% fall in alprazolam levels) in peri- and '
                       'postmenopausal women (clinical study).',
               'severity': 'info', 'reference_ids': ['REF-5411']}),
    ('cinew', {'note': 'Allergy: hops can cause skin allergy and, more rarely, hives, rhinitis or asthma, mostly in people who '
                       'handle the plant; one person had repeated whole-body hives traced to wild hop (case report), and hop '
                       'proteins cross-react with pollen allergens (lab study).',
               'severity': 'caution', 'reference_ids': ['REF-5412', 'REF-5413']}),
]
NOTES['humulus_lupulus'] = (
    'Searched PubMed (Humulus lupulus / hop(s) extract tiab; hops, xanthohumol, 8-prenylnaringenin ti: 108 HT, 8 SR, 205 '
    'SAFE hits; many "hops" hits were jumping or beer studies), Europe PMC, ClinicalTrials.gov (96) and OpenAlex. Added: '
    'NEW metabolic-support pair (2016 matured hop extract placebo RCT, visceral fat); NEW bad-breath pair (2026 pooled '
    'participant-level analysis of seven randomized breath studies, hops beta-acid toothpastes, company-run); the 2020 '
    'phase I drug-interaction study as an info note; an allergy caution (2002 urticaria case with review; 2024 pollen '
    'cross-reactivity). Not added: hop vaginal gel vs oestradiol in sexual dysfunction (active comparator), hop + valerian, '
    'soy + hop, Lactium and other combinations, xanthohumol-only safety and microbiome trials (compound), bitter-hop '
    'appetite studies (no vocab condition), dental biofilm studies (plaque, a surrogate), 8-prenylnaringenin bone trial '
    '(no vocab condition).')

# ================================================================== goldenseal
PLAN['hydrastis_canadensis'] = []
POST['hydrastis_canadensis'] = [
    ('cinew', {'note': 'Medicines: in human studies goldenseal did not meaningfully change blood levels of the HIV drug indinavir '
                       'or of digoxin, and in people with type 2 diabetes it did not change metformin exposure overall, though '
                       'at low metformin doses exposure fell by about 20%. Its stronger effect on CYP3A4 and CYP2D6 is listed '
                       'under drug interactions.',
               'severity': 'info', 'reference_ids': ['REF-5414', 'REF-5415', 'REF-5416']}),
    ('cinew', {'note': 'Salt balance: in an 11-year-old girl with newly diagnosed type 1 diabetes, goldenseal appeared to worsen '
                       'severe high blood sodium (hypernatraemia) (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5417']}),
    ('cinew', {'note': 'Long-term use: in 2-year toxicity studies, goldenseal root powder increased liver tumours in rats and '
                       'mice; whether this applies to people is not known (animal studies).',
               'severity': 'caution', 'reference_ids': ['REF-5418']}),
]
NOTES['hydrastis_canadensis'] = (
    'Searched PubMed (Hydrastis canadensis / goldenseal tiab, hydrastine ti: 14 HT, 3 SR, 74 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (6) and OpenAlex. Berberine-only trials were not searched as goldenseal evidence (berberine is '
    'shared with Berberis and Coptis). Still no efficacy trial of goldenseal itself. Added: human interaction studies '
    '(2025 metformin in T2DM, 2003 indinavir, 2007 digoxin) as an info note; a 2007 hypernatraemia case and the 2011 NTP '
    'two-year rodent study (liver tumours) as cautions. Not added: berberine pharmacokinetic studies (compound), a '
    'photosensitivity case with a ginseng + goldenseal + bee pollen product (combination), goldenseal catheter case, '
    'psychiatric case reports with multi-agent regimens, in vitro CYP and phototoxicity work.')

# ================================================================== St John's wort
PLAN['hypericum_perforatum'] = []
POST['hypericum_perforatum'] = [
    ('dciadd', 'hormonal-therapies', ['REF-5419']),
]
NOTES['hypericum_perforatum'] = (
    'Searched PubMed (Hypericum perforatum / St John\'s wort tiab; hyperforin, hypericin, Hypericum ti: 583 HT, 177 SR, '
    '1,177 SAFE hits; SR family and safety screened, depression and the many approved interactions not padded), Europe PMC, '
    'ClinicalTrials.gov and OpenAlex. Added: 2016 SR on combined oral contraceptives (breakthrough bleeding, lower hormone '
    'exposure, possible ovulation) to the approved hormonal-therapies interaction. Not added: dental pain SR/MA 2012 '
    '(homeopathic Hypericum with Arnica), OCD, neuropathic pain and smoking-cessation reviews (no benefit or no vocab '
    'condition), rodent pregnancy-safety SR, general interaction overviews already reflected in the approved interactions.')

# ================================================================== hyssop
PLAN['hyssopus_officinalis'] = []
POST['hyssopus_officinalis'] = [
    ('cinew', {'note': 'Asthma: in a small randomized trial of hyssop syrup added to usual asthma treatment, a post-hoc analysis '
                       'found improvement in people with a productive cough but worse lung function in those with a dry cough.',
               'severity': 'caution', 'reference_ids': ['REF-5420']}),
]
NOTES['hyssopus_officinalis'] = (
    'Searched PubMed (Hyssopus officinalis / hyssop tiab: 6 HT, 2 SR, 22 SAFE hits), Europe PMC, ClinicalTrials.gov (0) and '
    'OpenAlex. The 2024 triple-blind placebo RCT of hyssop syrup in mild-moderate asthma reported benefit only in a post-hoc '
    'productive-cough subgroup, with worsening in dry-cough patients, so no asthma pair was created (no whole-group benefit '
    'stated); the subgroup finding is recorded as a caution. Not added: multi-herb syrups, Qingre Huoxue recipe, Labiatae '
    'allergy case (oregano and thyme), essential-oil convulsant studies (already covered by the essential-oil caution).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r17_changes.tsv')
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
