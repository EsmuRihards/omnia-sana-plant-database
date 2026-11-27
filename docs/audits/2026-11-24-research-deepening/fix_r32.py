"""Research-deepening batch 32 (solidago-canadensis, solidago-virgaurea, stachys-officinalis, stellaria-media,
symphytum-officinale). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5667.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 32'

SPEC = [
    # chickweed
    ('REF-5667', '12641574', 'chickweederythemamultiforme', 'clinical'),
    # comfrey
    ('REF-5668', '28463019', 'foxglovecomfreyfatal', 'clinical'),
    ('REF-5669', '27840092', 'comfreylycopsamineskin', 'preclinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== Canadian goldenrod
PLAN['solidago_canadensis'] = []
NOTES['solidago_canadensis'] = (
    'Searched PubMed (Solidago canadensis / Canadian or Canada goldenrod tiab: 0 HT, 0 SR, 8 SAFE hits, all '
    'environmental), Europe PMC, ClinicalTrials.gov (0) and OpenAlex (cultivation, invasion ecology and pollinator '
    'studies). No human study was found. Settled.')

# ================================================================== European goldenrod
PLAN['solidago_virgaurea'] = []
NOTES['solidago_virgaurea'] = (
    'Searched PubMed (Solidago virgaurea / European goldenrod / Virgaureae herba tiab, "goldenrod" in titles: 4 HT, 0 '
    'SR, 20 SAFE hits), Europe PMC, ClinicalTrials.gov (2) and OpenAlex. Nothing new: Phytodolor / STW 1 (aspen + ash + '
    'goldenrod, combination) reviews, general reviews of herbs for urinary infections, rayless goldenrod (Isocoma pluriflora, a '
    'different genus) livestock poisoning studies, a 2017 contact-dermatitis review whose abstract gives no goldenrod-'
    'specific findings, and a 1998 systemic contact dermatitis case (no abstract). Settled.')

# ================================================================== wood betony
PLAN['stachys_officinalis'] = []
NOTES['stachys_officinalis'] = (
    'Searched PubMed (Stachys officinalis / Betonica officinalis / wood betony tiab, "betony" in titles: 1 HT, 0 SR, 3 '
    'SAFE hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex. Nothing new: the 2013 PCOS RCT used Stachys '
    'lavandulifolia (a different species also called "wood betony" in Iran), a 1977 Russian lactation study has no '
    'abstract, and other hits were ethnobotany and ecology. Settled.')

# ================================================================== chickweed
PLAN['stellaria_media'] = []
POST['stellaria_media'] = [
    ('cinew', {'note': 'Skin: a gardener with 13 years of recurrent erythema multiforme after weeding had eczema-like patch-'
                       'test reactions to fresh chickweed leaves (and to dandelion, sow thistle and white clover), worsened '
                       'by light (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5667']}),
]
NOTES['stellaria_media'] = (
    'Searched PubMed (Stellaria media / common chickweed tiab, "chickweed" in titles; mouse-ear chickweed, Cerastium, is '
    'a different plant: 1 HT, 0 SR, 6 SAFE hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex. Added: 2003 erythema '
    'multiforme / contact allergy case as a skin caution. Not added: a 2012 anti-obesity study (animal), heavy-metal '
    'surveys of wild greens, sesquiterpene-lactone patch testing (Asteraceae, not chickweed). No human efficacy trial '
    'found. Settled.')

# ================================================================== comfrey
PLAN['symphytum_officinale'] = []
POST['symphytum_officinale'] = [
    ('cinew', {'note': 'Foraging: a 55-year-old woman died of heart-rhythm failure after drinking tea made from foxglove '
                       'leaves she had mistaken for comfrey, despite antidote treatment (case report); see the foxglove '
                       'lookalike entry for how to tell them apart.',
               'severity': 'warning', 'reference_ids': ['REF-5668']}),
    ('cinew', {'note': 'Skin absorption: in lab tests on human skin, only 0.04-0.22% of lycopsamine, a main pyrrolizidine '
                       'alkaloid of comfrey, passed through the epidermis from a comfrey ointment within 24 hours (lab '
                       'study); internal use remains unsafe.',
               'severity': 'info', 'reference_ids': ['REF-5669']}),
]
NOTES['symphytum_officinale'] = (
    'Searched PubMed (Symphytum officinale / comfrey / Kytta / Symphyti radix tiab: 28 HT, 12 SR, 87 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (1) and OpenAlex. Back-pain (8) and pain (7) were not padded. Arthritis (5) was not raised: '
    'the 2013 Cochrane topical-herb OA review bases its comfrey finding on the single 220-person knee trial the record '
    'already cites (not cited twice). Added: 2017 fatal foxglove-for-comfrey case as a foraging WARNING (the approved '
    'foxglove lookalike entry cites non-fatal cases); 2017 human-skin lycopsamine penetration study as an info note. Not '
    'added: Traumaplant / Symphytum herb cream trials for myalgia, wounds and ankle sprain (Russian comfrey, '
    'Symphytum x uplandicum, a different species), comfrey + tannic acid, comfrey + methyl nicotinate and 4Jointz '
    '(combinations), the 2016 Cochrane back-pain review (same review as the 2014 version already cited), PA analytical '
    'and rodent toxicity studies, a 2008 general-practice case of a non-healing scalp sore packed with comfrey leaves '
    '(the abstract does not report a reaction to comfrey).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r32_changes.tsv')
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
