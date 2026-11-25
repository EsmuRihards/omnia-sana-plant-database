"""Research-deepening batch 13 (eschscholzia-californica, eucalyptus-globulus, euphrasia-officinalis, filipendula-ulmaria,
filipendula-vulgaris). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5346.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 13'

SPEC = [
    # eucalyptus (unnamed "eucalyptus oil" goes to E. globulus, inv. 10, as REF-0256 already does)
    ('REF-5346', '24261680', 'cineolebronchitis', 'rct'),
    ('REF-5347', '23853660', 'eucalyptusinhalationtkr', 'rct'),
    ('REF-5348', '40070740', 'eucalyptusallergicrhinitis', 'systematic-review'),
    ('REF-5349', '42124882', 'eucalyptusdialysisheadache', 'rct'),
    ('REF-5350', '7651249', 'eucalyptuspoisoningchildren', 'clinical'),
    ('REF-5351', '8240865', 'eucalyptuspoisoningqueensland', 'clinical'),
    ('REF-5352', '34282989', 'eucalyptusseizures', 'systematic-review'),
    ('REF-5353', '21867365', 'eucalyptusdermalseizure', 'clinical'),
    ('REF-5354', '40432665', 'eucalyptusfatalpoisoning', 'clinical'),
    ('REF-5355', '37010839', 'eucalyptuscosmeticsafety', 'narrative-review'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== eucalyptus
PLAN['eucalyptus_globulus'] = [
    ('newpair', 'bronchitis', ['REF-5346'],
     '1,8-cineole (600 mg a day) relieved acute bronchitis symptoms and cut coughing fits more than placebo within 4 days in '
     'a randomized double-blind trial (compound evidence: 1,8-cineole (eucalyptol) is eucalyptus oil\'s main active '
     'constituent)'),
    ('newpair', 'pain', ['REF-5347'],
     'Inhaling eucalyptus oil reduced pain after knee-replacement surgery more than inhaling almond oil in a randomized trial '
     '(oil species not stated)'),
    ('newpair', 'allergy', ['REF-5348'],
     'Eucalyptus oil improved allergic-rhinitis quality of life vs placebo in a 2025 systematic review of three trials, though '
     'the fall in nasal symptom scores was not significant (oil species not stated)'),
    ('newpair', 'headache', ['REF-5349'],
     'Inhaling eucalyptus oil eased headache during dialysis more than usual care in a small randomized trial (oil species '
     'not stated)'),
]
POST['eucalyptus_globulus'] = [
    ('cinew', {'note': 'Poisoning: eucalyptus oil is a common cause of poisoning in young children. In a Melbourne series of 109 '
                       'children who swallowed it, 59% had symptoms such as drowsiness, vomiting or unsteadiness and three were '
                       'unconscious after 5 to 10 mL; all recovered, and another series found most children symptom-free. '
                       'Seizures have followed swallowing, inhaling or rubbing the oil on the skin (a review of 110 cases), '
                       'and an adult died after swallowing 15 mL by mistake. Keep eucalyptus oil out of children\'s reach.',
               'severity': 'caution',
               'reference_ids': ['REF-5350', 'REF-5351', 'REF-5352', 'REF-5353', 'REF-5354']}),
    ('cinew', {'note': 'Skin products: a 2023 Cosmetic Ingredient Review safety assessment concluded that six Eucalyptus '
                       'globulus-derived ingredients are safe in cosmetics when formulated to be non-sensitising.',
               'severity': 'info', 'reference_ids': ['REF-5355']}),
]
NOTES['eucalyptus_globulus'] = (
    'Searched PubMed (Eucalyptus globulus / blue gum tiab; eucalyptus oil, 1,8-cineole, cineole, eucalyptol ti: 54 HT, 10 '
    'SR, 196 SAFE hits), Europe PMC, ClinicalTrials.gov (72) and OpenAlex. Unnamed "eucalyptus oil" goes to E. globulus '
    '(inv. 10, as for REF-0256). Added: NEW bronchitis pair (2013 cineole placebo RCT, compound evidence, labelled); NEW pain '
    'pair (2013 RCT, eucalyptus oil vs almond oil inhalation after knee replacement); NEW allergy pair (2025 SR of three '
    'trials: quality of life improved, nasal symptom score not significant); NEW headache pair (2026 small RCT vs usual '
    'care in haemodialysis); a poisoning caution (Melbourne 1995 and Queensland 1993 paediatric series, 2021 seizure case '
    'series and SR, 2011 dermal seizure case, 2025 fatal adult case); the 2023 CIR cosmetic safety assessment as an info '
    'note. Not added: 2014 pre-operative anxiety RCT (the cineole arm reduced anxiety but the eucalyptus-oil arm did not '
    'clearly beat control, so no anxiety pair); 2020 eucalyptol nursing-home pilot (not randomised, MMSE unchanged); 2026 '
    'eucalyptus leaf extract (oenothein B) liver-fat pilot (difference only in a post-unblinding sensitivity analysis; '
    'species not stated); eucalyptus vs miswak toothpaste (active comparator); 2024 cineole cold-timing study (not '
    'randomised); combinations (eucalyptol-limonene-pinene capsules, turpentine ointment, NESOSPRAY sprays, Atusin, aromatic '
    'herb sprays, peppermint + eucalyptus headache preparations, Neuragen, Myostaal); the 2022 cough MA (already logged as '
    'negative); the Berlin herb-induced liver injury study (one possible E. globulus case); a mouse diazepam interaction '
    'study; the 2015 contact-allergy review and poisoning letters with no abstract.')

# ================================================================== California poppy
PLAN['eschscholzia_californica'] = []
NOTES['eschscholzia_californica'] = (
    'Searched PubMed (Eschscholzia californica / California poppy tiab: 5 HT, 0 SR, 20 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (6) and OpenAlex. Still no published human trial of California poppy alone. GAP: A. Vogel\'s '
    'placebo-controlled RCT of Eschscholzia tablets in insomnia (NCT06795776) completed in November 2025 with no results or '
    'publication yet - recheck. Not added: Eschscholzia + valerian insomnia RCT 2026, Crataegus + Eschscholzia + magnesium '
    '(already excluded), AUDISTIM and other combinations, mother-tincture case series in an AkiNik homoeopathy journal '
    '(uncontrolled), a dog anxiety supplement.')

# ================================================================== eyebright
PLAN['euphrasia_officinalis'] = []
NOTES['euphrasia_officinalis'] = (
    'Searched PubMed (Euphrasia officinalis / E. rostkoviana / E. stricta / eyebright tiab, Euphrasia ti: 5 HT, 0 SR, 4 '
    'SAFE hits), Europe PMC, ClinicalTrials.gov (4) and OpenAlex. Nothing new: the 2020 preterm-neonate RCT (PMID 32850558) '
    'is the Weleda Euphrasia D3 trial already purged as REF-2173 (homeopathic; primary outcome null, p=0.85), and the 2000 '
    'cohort (PMID 11152054) is the anthroposophic single-dose drops purged as REF-0613; NCT04122300 (same Weleda product), '
    'Belladonna + Euphrasia drops and homoeopathic dry-eye studies excluded. Settled.')

# ================================================================== meadowsweet
PLAN['filipendula_ulmaria'] = []
NOTES['filipendula_ulmaria'] = (
    'Searched PubMed (Filipendula ulmaria / Spiraea ulmaria / meadowsweet tiab: 2 HT, 0 SR, 18 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (2) and OpenAlex. No human trial of meadowsweet alone. Not added: severe gastrointestinal bleeding '
    'in a 4-year-old after a multi-herb syrup containing meadowsweet and willow (2011; salicylates confirmed, but a '
    'combination product), the three-herb functional beverage RCT (already logged), a devil\'s claw + blackcurrant + '
    'meadowsweet trial (registered, not yet recruiting), Gastrokur and other combinations; a 2024 Russian study of '
    'meadowsweet for cognitive impairment in chronic cerebral ischaemia (DOI 10.51620/2687-1521-2024-3-19-23-29) has no '
    'retrievable abstract - unread. Settled for now.')

# ================================================================== dropwort
PLAN['filipendula_vulgaris'] = []
NOTES['filipendula_vulgaris'] = (
    'Searched PubMed (Filipendula vulgaris / F. hexapetala / dropwort tiab: 1 HT, 0 SR, 25 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (0) and OpenAlex. Every human hit was water dropwort (Oenanthe crocata, O. javanica - a different, '
    'often deadly genus), not Filipendula. No human study of dropwort. Settled.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r13_changes.tsv')
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
