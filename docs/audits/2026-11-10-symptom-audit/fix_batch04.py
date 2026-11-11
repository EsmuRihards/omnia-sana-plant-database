"""Batch-4 fixes (2026-11-10 symptom audit): cannabis .. cinnamomum-verum.
Owner decisions this batch: unnamed "cinnamon" clinical evidence -> Cassia only; a plant's
signature compound (capsaicin) counts, labelled in the note; never list a plant for the organ
its own serious warning is about (celandine / liver). Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'
GENERIC_CINNAMON = ['REF-0006', 'REF-0136', 'REF-0598', 'REF-0599', 'REF-0666', 'REF-0667', 'REF-0429']
CAPSAICIN_NOTE = ('Evidence is for capsaicin, chili\'s signature pungent compound (topical high-concentration '
                  'capsaicin for neuropathic pain), not for eating chili.')

PLAN = {
    'cannabis_sativa': [('rm', c, ['REF-0044']) for c in ('cardiovascular-support', 'inflammation', 'skin-irritation')],
    'capsella_bursa_pastoris': [('rm', 'skin-irritation', ['REF-0507'])],
    'capsicum_annuum': [
        ('purge', 'REF-0021'),  # phantom: DOI unresolvable, title not found
        ('rm', 'arthritis', ['REF-0010']), ('rm', 'back-pain', ['REF-0010', 'REF-0057']),
        ('rm', 'cardiovascular-support', ['REF-0161']),  # "spicy foods" cohort, no plant/species
        ('rm', 'wounds', ['REF-0169']),
        ('note', 'pain', CAPSAICIN_NOTE),
    ],
    'carum_carvi': [('rm', c, ['REF-0078']) for c in ('appetite-loss', 'indigestion', 'infection', 'wounds')]
      + [('rm', c, ['REF-0126']) for c in ('appetite-loss', 'bloating', 'indigestion', 'infection', 'wounds')],
    'centaurium_erythraea': [('rm', c, ['REF-0431']) for c in ('acid-reflux', 'arthritis', 'bloating', 'detox',
                                                              'inflammation', 'liver-support', 'skin-irritation')]
      + [('rm', c, ['REF-0619']) for c in ('acid-reflux', 'arthritis', 'bloating', 'detox', 'skin-irritation')]
      + [('add', 'appetite-loss', ['REF-0619'])],
    'centella_asiatica': [
        ('rm', 'bruising', ['REF-0457', 'REF-0458']), ('rm', 'eczema', ['REF-0457']), ('rm', 'stress', ['REF-0457']),
        ('rm', 'hemorrhoids', ['REF-0458', 'REF-0569', 'REF-0570']),
        ('rm', 'swelling', ['REF-0570']), ('rm', 'varicose-veins', ['REF-0570']),  # class review of 10 phlebotonics
        ('null', 'cognitive-function', ['REF-0568']),  # SR: "not strong evidence ... cognitive function"
        ('add', 'cognitive-function', ['REF-0457']),
        ('mexcl', 'bruising', ['REF-2087', 'REF-2088', 'REF-2090', 'REF-2091']),  # wound/scar papers, not bruises
    ],
    'chamerion_angustifolium': [('purge', 'REF-0146'), ('purge', 'REF-0317'),  # phantoms: wrong DOIs, titles not found
                                ('rmk', 'wounds', ['REF-0022'])],
    'chelidonium_majus': [('drop', 'liver-support')]  # serious liver-injury warning (owner rule)
      + [('rm', c, ['REF-0460']) for c in ('arthritis', 'back-pain', 'bloating', 'headache', 'indigestion',
                                          'menstrual-cramps', 'muscle-spasm', 'skin-irritation', 'warts', 'wounds')]
      + [('add', 'warts', ['REF-2269'])],
    'cinnamomum_cassia': [
        ('add', 'blood-sugar', ['REF-0006', 'REF-0136', 'REF-0667']),
        ('add', 'cardiovascular-support', ['REF-0006', 'REF-0136', 'REF-0666', 'REF-0667']),
        ('add', 'high-cholesterol', ['REF-0136', 'REF-0666', 'REF-0667']),
        ('add', 'metabolic-support', ['REF-0006', 'REF-0136', 'REF-0667']),
    ],
    'cinnamomum_verum': [('purge', r) for r in GENERIC_CINNAMON]
      + [('rm', c, ['REF-0101']) for c in ('arthritis', 'bloating', 'blood-sugar', 'cardiovascular-support',
                                          'indigestion', 'infection', 'inflammation', 'metabolic-support',
                                          'skin-irritation', 'wounds')]
      + [('null', 'cardiovascular-support', ['REF-2413'])],  # C. zeylanicum RCT: no LDL-C reduction
}

NOTES = {
    'cannabis_sativa': 'REF-0044 (hemp-as-food review) names none of cardiovascular, inflammation or skin - removed from those pairs.',
    'capsella_bursa_pastoris': 'Herbal Reality (REF-0507) names diarrhoea, heavy menstrual bleeding, period pain, PMS and wounds/bleeding, not skin irritation - removed from skin-irritation.',
    'capsicum_annuum': 'REF-0021 purged as a phantom (DOI 10.1007/s11101-023-09875-8 does not resolve; title not found). Capsaicin (signature compound) counts per owner rule 2026-11-11, labelled in the pain note; REF-0010/REF-0057 cover neuropathic pain only - removed from arthritis/back-pain. REF-0161 ("spicy foods" cohort) names no plant - removed from cardiovascular. REF-0169 (capsaicin vs microbes) kept for infection only.',
    'carum_carvi': 'EU monograph REF-0078: "problems of the digestive system such as bloating and flatulence" - kept for bloating only. REF-0126 (cumin + caraway update) names none of the paired symptoms.',
    'centaurium_erythraea': 'EU monograph (REF-0431): mild indigestion / stomach and gut disorders and temporary loss of appetite only - removed from 7 pairs. Herbal Reality (REF-0432) names all 9 uses. REF-0619 names dyspeptic complaints, loss of appetite, anti-inflammatory and hepatoprotective activity - wired to appetite-loss, removed from acid-reflux, arthritis, bloating, detox, skin.',
    'centella_asiatica': 'REF-0568 (SR: "not strong evidence to support ... cognitive function") moved to null_result_ids; REF-0457 (names preventing cognitive deficits) added. REF-0570 (Cochrane, 10 phlebotonics pooled) is class-level - removed. Bruising had only wound/scar papers - dropped.',
    'chamerion_angustifolium': 'REF-0146 ("Phytochemical and Pharmacological Review of Chamerion angustifolium", DOI resolves to a tomato-virus paper) and REF-0317 ("Ivan-chai ...", DOI resolves to a yeast-media paper) purged as phantoms: neither title exists in OpenAlex. Only Epilobium angustifolium-specific studies remain.',
    'chelidonium_majus': 'liver-support dropped (owner rule 2026-11-11: never list a plant for the organ its own serious warning is about - oral celandine causes liver injury). REF-0460 kept for anti-inflammatory, antimicrobial and analgesic uses it names; REF-2269 (latex vs HPV, folk use against warts) added to warts.',
    'cinnamomum_cassia': 'Owner rule 2026-11-11: clinical evidence on unnamed "cinnamon" goes to Cassia (the species most trials used, e.g. Khan 2003, Akilen 2010). Added REF-0006, REF-0136, REF-0666, REF-0667 here (moved from True cinnamon).',
    'cinnamomum_verum': 'Unnamed-"cinnamon" studies purged (owner rule 2026-11-11, they go to Cassia): REF-0006, 0136, 0429, 0598, 0599, 0666, 0667. REF-0101 (Groves, Body into Balance) ' + UNVER + '. REF-2413 (C. zeylanicum RCT): no LDL-C reduction -> null for cardiovascular; FBS lowering in T2DM kept for blood-sugar.',
}

if __name__ == '__main__':
    fixlib.main(PLAN, NOTES, 'batch 4', os.path.join(os.path.dirname(__file__), 'batch04_changes.tsv'))
