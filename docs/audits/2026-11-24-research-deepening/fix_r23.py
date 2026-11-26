"""Research-deepening batch 23 (ononis-arvensis, origanum-majorana, origanum-vulgare, oxalis-stricta, oxycoccus-palustris).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5545.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 23'

SPEC = [
    ('REF-5545', '36609950', 'herbalrhinosinusitisnma', 'meta-analysis'),
    ('REF-5546', '8630713', 'oreganothymeallergy', 'clinical'),
    ('REF-5547', '41096727', 'marjoramtoxicology', 'preclinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== field restharrow
PLAN['ononis_arvensis'] = []
NOTES['ononis_arvensis'] = (
    'Searched PubMed (Ononis arvensis / Ononis hircina / field restharrow / restharrow tiab): 1 HT, 0 SR, 0 SAFE hits; '
    'Europe PMC, ClinicalTrials.gov (0) and OpenAlex (rhizobia and vegetation papers). The only trial (2019 secondary '
    'analysis, acute cystitis) tested Aqualibra, a fixed combination of restharrow root, Java tea and goldenrod, not field '
    'restharrow alone. Settled.')

# ================================================================== marjoram
PLAN['origanum_majorana'] = []
POST['origanum_majorana'] = [
    ('cinew', {'note': 'Lab safety: a marjoram leaf extract caused dose-dependent DNA damage in cell tests at higher '
                       'concentrations, although rats given a single dose up to 2,000 mg/kg showed no toxicity (lab and '
                       'animal study).',
               'severity': 'info', 'reference_ids': ['REF-5547']}),
]
NOTES['origanum_majorana'] = (
    'Searched PubMed (Origanum majorana / Majorana hortensis / sweet marjoram / marjoram tiab: 28 HT, 2 SR, 65 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (8) and OpenAlex. Added: 2025 cyto/genotoxicity and acute toxicity study as an info '
    'note. GAP: stress/anxiety - in a 2023 RCT of marjoram oil inhalation in ICU nurses, stress and anxiety fell only '
    'within the marjoram group, with no difference from the almond-oil control, so no pair. Not added: 2021 Parkinson\'s '
    'tea RCT (motor score unchanged; depression and non-motor gains reported within-group), 2025 Parkinson\'s oxidative-'
    'stress biomarkers, marjoram + cinnamon PCOS tea (combination; the earlier PCOS hormone RCT REF-1227 is already held), '
    'aromatherapy blends with lavender, clary sage or neroli (dysmenorrhoea, neck pain, blood pressure, arthritis), '
    'bruxism inhalation pilots (no vocab condition), heavy-metal risk assessments of marjoram ointments.')

# ================================================================== oregano
PLAN['origanum_vulgare'] = [
    ('newpair', 'sinusitis', ['REF-5545'],
     'In a 2023 network meta-analysis of 47 randomized trials of herbal medicines for rhinosinusitis, Origanum vulgare ranked '
     'most beneficial for symptoms and quality of life in chronic rhinosinusitis without nasal polyps (low-certainty '
     'evidence)'),
]
POST['origanum_vulgare'] = [
    ('cinew', {'note': 'Allergy: eating oregano (and thyme) caused three systemic allergic reactions in one person, confirmed by '
                       'skin and IgE tests; plants of the mint family (Lamiaceae) can cross-react (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5546']}),
]
NOTES['origanum_vulgare'] = (
    'Searched PubMed (Origanum vulgare / oregano tiab: 53 HT, 20 SR, 235 SAFE hits; most were animal-feed and food-'
    'preservation studies), Europe PMC, ClinicalTrials.gov (19) and OpenAlex. Added: NEW sinusitis pair (2023 NMA of '
    'herbal medicines for rhinosinusitis, low certainty); 1996 systemic allergy case as a caution. Not added: 2022 soldiers '
    'study (muscle-damage and oxidative-stress blood markers only), 2022 athletes essential-oil trial (O. vulgare subsp. '
    'hirtum raised HDL over 14 days; small, healthy people, surrogate), spice-blend meal trials (combinations), oregano + '
    'lemon balm vaginal tablet vs metronidazole (combination, active comparator), essential-oil cystitis real-world use '
    '(blends), Origanum onites and O. dubium studies (other species), carvacrol-only studies, irritant dermatitis letter '
    'with no abstract.')

# ================================================================== yellow woodsorrel
PLAN['oxalis_stricta'] = []
NOTES['oxalis_stricta'] = (
    'Searched PubMed (Oxalis stricta / Oxalis fontana / yellow woodsorrel / Xanthoxalis stricta tiab): 0 HT, 0 SR, 1 SAFE '
    'hit (a nanoparticle lab study); Europe PMC, ClinicalTrials.gov (0) and OpenAlex (lab, ecology) found no human study. '
    'Settled.')

# ================================================================== European cranberry
PLAN['oxycoccus_palustris'] = []
NOTES['oxycoccus_palustris'] = (
    'Searched PubMed (Oxycoccus palustris / Vaccinium oxycoccos / small, bog or European cranberry tiab; "cranberry" alone '
    'was not searched because nearly all cranberry trials use American cranberry, Vaccinium macrocarpon, a separate '
    'record): 3 HT, 2 SR, 6 SAFE hits; Europe PMC, ClinicalTrials.gov (0) and OpenAlex. Nothing new: a 2025 open-label '
    'pilot of a cranberry supplement found no change in the urinary microbiome (surrogate; the product species is not '
    'clear from the abstract); Cochrane cranberry reviews pool V. macrocarpon products. Settled for human evidence specific '
    'to this species.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r23_changes.tsv')
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
