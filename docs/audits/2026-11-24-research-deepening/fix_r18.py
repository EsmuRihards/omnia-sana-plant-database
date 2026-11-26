"""Research-deepening batch 18 (inonotus-obliquus, inula-helenium, juniperus-communis, knautia-arvensis, lactuca-virosa).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5421.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 18'

SPEC = [
    # chaga
    ('REF-5421', '23149251', 'chagaoxalatenephropathy', 'clinical'),
    ('REF-5422', '32419395', 'chagaendstagerenal', 'clinical'),
    ('REF-5423', '35451393', 'chagaoxalatenephrotic', 'clinical'),
    # elecampane
    ('REF-5424', '27568784', 'sesquiterpenelactonesystemicdermatitis', 'narrative-review'),
    # wild lettuce
    ('REF-5425', '9778767', 'wildlettuceinjection', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== chaga
PLAN['inonotus_obliquus'] = []
POST['inonotus_obliquus'] = [
    ('cinew', {'note': 'Kidneys: chaga is extremely high in oxalate. People who took chaga powder daily for months developed '
                       'oxalate kidney damage, including kidney failure needing dialysis; one report measured very high oxalate '
                       'in the product itself (case reports).',
               'severity': 'warning', 'reference_ids': ['REF-5421', 'REF-5422', 'REF-5423']}),
]
NOTES['inonotus_obliquus'] = (
    'Searched PubMed (Inonotus obliquus / chaga / Fuscoporia obliqua tiab: 8 HT, 0 SR, 49 SAFE hits; many "Chaga" hits were '
    'Chagas disease), Europe PMC, ClinicalTrials.gov (4) and OpenAlex. Added: a kidney warning from three oxalate '
    'nephropathy case reports (2014 dialysis, 2020 end-stage renal disease with measured oxalate 14.2 g/100 g, 2022 '
    'nephrotic presentation). GAP: a 2008 study in type 2 diabetes found a single prior dose of Fuscoporia obliqua (a '
    'synonym of I. obliquus) lowered the post-meal glucose peak and protected endothelial function, but the abstract does '
    'not state randomisation or a placebo, so no blood-sugar pair was created. Not added: ex vivo DNA-damage study in IBD '
    'lymphocytes, inotodiol and polysaccharide lab and animal studies.')

# ================================================================== elecampane
PLAN['inula_helenium'] = []
POST['inula_helenium'] = [
    ('ciadd', 'The sesquiterpene lactones (especially alantolactone)', ['REF-5424']),
]
NOTES['inula_helenium'] = (
    'Searched PubMed (Inula helenium / elecampane tiab, alantolactone ti: 6 HT, 0 SR, 63 SAFE hits, mostly alantolactone '
    'lab work), Europe PMC, ClinicalTrials.gov (3) and OpenAlex. No human trial of elecampane alone (KalobaTUSS and other '
    'syrups are combinations). Added: a 2017 review naming elecampane among Compositae plants suspected of causing systemic '
    'allergic dermatitis, to the skin-allergy note. Not added: contact dermatitis letters with no abstract (1995 massage '
    'liniment, 1975), a liver-injury case with a six-herb immunostimulant collection (combination), Inula species '
    'anticonvulsant and cytotoxic lab studies.')

# ================================================================== juniper
PLAN['juniperus_communis'] = []
NOTES['juniperus_communis'] = (
    'Searched PubMed (Juniperus communis / juniper berry / common juniper / juniper oil tiab, juniper ti: 17 HT, 4 SR, 49 '
    'SAFE hits; many hits were the Juniper Gardens project or other juniper species), Europe PMC, ClinicalTrials.gov (17) '
    'and OpenAlex. Nothing new: the 2001 Cosmetic Ingredient Review found the data insufficient to judge the safety of '
    'juniper extracts in cosmetics (no change to the record); a hyponatraemia case followed a multi-herb kidney "detox" with '
    'over a gallon of fluid a day (not attributable); a bullous dermatitis case has no abstract; cade oil (J. oxycedrus) '
    'poisonings and J. ashei / chinensis / occidentalis pollen and oil studies are other species; a 1974 juniper bath study '
    'is uncontrolled. Settled.')

# ================================================================== field scabious
PLAN['knautia_arvensis'] = []
NOTES['knautia_arvensis'] = (
    'Searched PubMed (Knautia arvensis / Scabiosa arvensis / field scabious tiab): 0 HT, 1 SR (unrelated), 0 SAFE hits; '
    'Europe PMC, ClinicalTrials.gov and OpenAlex found no human study. Settled.')

# ================================================================== wild lettuce
PLAN['lactuca_virosa'] = []
POST['lactuca_virosa'] = [
    ('cinew', {'note': 'Never inject: three drug users who injected a home-made wild lettuce extract became acutely ill with fever, '
                       'chills, abdominal and back pain and mild liver changes, and none had the opiate-like effect claimed for '
                       'it (case series).',
               'severity': 'caution', 'reference_ids': ['REF-5425']}),
]
NOTES['lactuca_virosa'] = (
    'Searched PubMed (Lactuca virosa / wild / bitter / opium lettuce / lactucarium tiab, lactucin, lactucopicrin ti: 3 HT, '
    '0 SR, 12 SAFE hits), Europe PMC, ClinicalTrials.gov (1) and OpenAlex. Still no human trial. Added: a 1998 case series '
    'of intravenous wild lettuce extract injection as a caution. Not added: lactucin liver-fibrosis lab work, a multi-herb '
    'case report (coltsfoot, kava, blue vervain), veterinary reports.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r18_changes.tsv')
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
