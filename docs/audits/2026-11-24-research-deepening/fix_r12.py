"""Research-deepening batch 12 (elymus-repens, epilobium-parviflorum, equisetum-arvense, equisetum-pratense,
equisetum-sylvaticum). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5342.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 12'

SPEC = [
    # field horsetail
    ('REF-5342', '26019907', 'horsetailepisiotomy', 'rct'),
    ('REF-5343', '28112963', 'horsetailpancreatitis', 'clinical'),
    ('REF-5344', '27903949', 'horsetailantiretrovirals', 'clinical'),
    ('REF-5345', '41069090', 'horsetailcosmeticsafety', 'narrative-review'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== field horsetail
PLAN['equisetum_arvense'] = [
    ('add', 'wounds', ['REF-5342']),
    ('note', 'wounds', 'Horsetail ointment improved the healing of episiotomy wounds and reduced their pain more than placebo '
     'in a randomized double-blind trial; traditionally used for minor wounds (EU herbal monograph)'),
]
POST['equisetum_arvense'] = [
    ('cinew', {'note': 'Pancreas: a woman had repeated mild attacks of acute pancreatitis that stopped once she gave up '
                       'drinking horsetail infusions regularly (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5343']}),
    ('cinew', {'note': 'Skin products: a 2026 Cosmetic Ingredient Review safety assessment concluded that five field '
                       'horsetail-derived ingredients are safe as used in cosmetics.',
               'severity': 'info', 'reference_ids': ['REF-5345']}),
    ('dcinew', {'drug_class': 'antiretrovirals', 'severity': 'caution',
                'mechanism': 'Two people on long-standing efavirenz-based HIV treatment had their virus return (virological '
                             'breakthrough) after taking a herbal supplement containing horsetail; the authors suspected an '
                             'interaction and advised avoiding the combination (case reports).',
                'reference_ids': ['REF-5344']}),
]
NOTES['equisetum_arvense'] = (
    'Searched PubMed (Equisetum arvense / field / common horsetail tiab; horsetail, Equisetum ti: 24 HT, 1 SR, 57 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (9) and OpenAlex. Added: 2015 episiotomy ointment placebo RCT to wounds; a 2017 '
    'pancreatitis case as a new caution; the 2026 CIR cosmetic safety assessment as an info note; DRAFT antiretroviral '
    'interaction (two virological-breakthrough cases with a horsetail-containing supplement, 2017; needs owner sign-off). '
    'Dead end: the 2022 antihypertensive RCT compared horsetail only with hydrochlorothiazide (active comparator, no '
    'placebo), so no blood-pressure pair. Not added: hyponatraemia case letters (2018, horsetail juice; 2021, with SIADH) '
    'and a 2004 carrot/horsetail anaphylaxis case - no abstract, worth a manual read; vanishing bile duct case (garcinia + '
    'horsetail + ketoprofen); silicon absorption and Tamm-Horsfall protein studies (no clinical outcome); Urox, Viviscal, '
    'CELcomplex, PEA + horsetail and other combinations; nail lacquer trials (horsetail one ingredient); perineal-trauma '
    'and PROM vaginal-cream RCTs (no vocab condition); E. bogotense, E. myriochaetum, E. telmateia, E. hyemale (other '
    'species).')

# ================================================================== couch grass
PLAN['elymus_repens'] = []
NOTES['elymus_repens'] = (
    'Searched PubMed (Elymus repens / Agropyron repens / Elytrigia repens / couch / quack / twitch grass tiab: 3 HT, 0 SR, '
    '9 SAFE hits), Europe PMC, ClinicalTrials.gov (3) and OpenAlex. No human study of couch grass alone: the kidney-stone '
    'trials and registered studies use multi-ingredient products (potassium citrate + Agropyrum 2012; Renalof, Neorenal '
    'Forte; Agropyron + mannitol + magnesium). Settled.')

# ================================================================== small-flowered willowherb
PLAN['epilobium_parviflorum'] = []
NOTES['epilobium_parviflorum'] = (
    'Searched PubMed (Epilobium parviflorum / small-flowered / hoary willowherb tiab; willowherb, Epilobium ti: 8 HT, 0 SR, '
    '10 SAFE hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex. No human study of E. parviflorum alone: prostate '
    'products combine Epilobium (often E. angustifolium, another species) with other ingredients (PEA + Calendula '
    'suppositories, a Solidago phyto-complex, a multi-herb food supplement); the rest is a canine BPH case and lab work. '
    'Settled.')

# ================================================================== shady and wood horsetail
PLAN['equisetum_pratense'] = []
NOTES['equisetum_pratense'] = (
    'Searched PubMed (Equisetum pratense / meadow / shady horsetail tiab): 0 hits in every query family; Europe PMC, '
    'ClinicalTrials.gov and OpenAlex found no human study. Settled (sparse-literature species; field horsetail evidence is '
    'not inherited).')
PLAN['equisetum_sylvaticum'] = []
NOTES['equisetum_sylvaticum'] = (
    'Searched PubMed (Equisetum sylvaticum / wood / woodland horsetail tiab): 0 hits in every query family; Europe PMC, '
    'ClinicalTrials.gov and OpenAlex found no human study. Settled (sparse-literature species; field horsetail evidence is '
    'not inherited).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r12_changes.tsv')
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
