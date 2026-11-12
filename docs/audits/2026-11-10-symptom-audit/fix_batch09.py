"""Batch-9 fixes (2026-11-10 symptom audit): humulus .. lamium-album. Run from the repo root.
Owner decision this batch (2026-11-12): health-content web pages with no checkable references are not
sources (Ask-Ayurveda wiki); referenced, practitioner-written pages such as Herbal Reality remain
acceptable for what they name. Standing rules otherwise (multi-herb products, wrong species, genus-level
reviews, compound papers naming no species, superseded monograph versions, unverifiable sources)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'
SHASHKINA_ABS = ("Data on the chemical composition and pharmacological activity of chaga (Inonotus obliquus) are reviewed. "
                 "The possible mechanisms of action and factors responsible for the discrepancy of data available in the "
                 "literature are discussed. The physical and chemical characteristics of melanin (polyphenolic chromogenic "
                 "humin-like complex present in chaga) and its role in the regulation of physiological processes are "
                 "considered.")

BIB = dict(
    retag={'REF-0455': 'narrative-review', 'REF-0588': 'preclinical', 'REF-0845': 'narrative-review',
           'REF-0272': 'narrative-review', 'REF-0093': 'preclinical', 'REF-0445': 'preclinical'},
    sets={'REF-0272': {'title': 'Chemical and medicobiological properties of chaga (review)',
                       'journal': 'Pharmaceutical Chemistry Journal', 'volume': '40', 'number': '10',
                       'pages': '560--568', 'doi': '10.1007/s11094-006-0194-4', 'abstract': SHASHKINA_ABS}},
    delete=['REF-0141',   # valerian + hops combination overview
            'REF-0456',   # berberine chemistry review, names no goldenseal (compound paper)
            'REF-2811',   # tested Knautia drymeia and K. macedonica, not K. arvensis
            'REF-0339',   # Ask-Ayurveda wiki: no checkable references (owner decision)
            'REF-0073'],  # 2010 juniper monograph, superseded by the 2021 revision REF-3066
)

HYP_ALL = ('arthritis', 'bruising', 'cold', 'eczema', 'infection', 'inflammation', 'insomnia', 'skin-irritation', 'wounds')
CHAGA_ALL = ('arthritis', 'cold', 'immune-support', 'infection', 'inflammation', 'metabolic-support', 'skin-irritation',
             'wounds')
JUN_ALL = ('bloating', 'indigestion', 'infection', 'swelling', 'urinary-support', 'uti', 'wounds')

PLAN = {
    'humulus_lupulus': [('purge', 'REF-0141'), ('add', 'insomnia', ['REF-3077']),
                        ('note', 'insomnia', 'EU traditional use to aid sleep')],
    'hydrastis_canadensis': [('purge', 'REF-0456'), ('rm', 'wounds', ['REF-0588'])]
      + [('rm', c, ['REF-0455']) for c in ('arthritis', 'bloating', 'diarrhea', 'indigestion', 'sore-throat')],
    'hypericum_perforatum': [('rm', c, ['REF-0181']) for c in HYP_ALL],
    'hyssopus_officinalis': [('rm', c, ['REF-0845']) for c in ('arthritis', 'bronchitis', 'cough', 'inflammation',
                                                              'respiratory-support', 'skin-irritation')]
      + [('rm', 'bronchitis', ['REF-1804']), ('rm', 'cough', ['REF-1804'])],
    'inonotus_obliquus': [('rm', c, ['REF-0272']) for c in CHAGA_ALL]
      + [('note', 'cognitive-function', 'Chaga extract improved learning and memory in mice with drug-induced amnesia (preclinical)')],
    'inula_helenium': [('rm', 'bronchitis', ['REF-0445']), ('rm', 'wounds', ['REF-0445', 'REF-0539'])],
    'juniperus_communis': [('merge', 'REF-0073', 'REF-3066')]
      + [('rm', c, ['REF-0035']) for c in JUN_ALL]
      + [('rm', 'swelling', ['REF-3066']), ('rm', 'uti', ['REF-3066'])],
    'knautia_arvensis': [('purge', 'REF-2811')],
    'lactuca_virosa': [('rm', 'stress', ['REF-0526'])]
      + [('rm', c, ['REF-0526', 'REF-0527', 'REF-0622']) for c in ('headache', 'back-pain')]
      + [('add', 'insomnia', ['REF-0527']), ('add', 'cough', ['REF-0527'])],
    'lamium_album': [('purge', 'REF-0339'), ('rm', 'cough', ['REF-0348']), ('rm', 'skin-irritation', ['REF-0348']),
                     ('add', 'respiratory-support', ['REF-0348'])]
      + [('add', c, ['REF-1746']) for c in ('bronchitis', 'inflammation', 'skin-irritation')],
}

NOTES = {
    'humulus_lupulus': 'REF-0141 purged: an overview of the valerian + hops COMBINATION (multi-herb product). EU monograph REF-3077 (relief of mild symptoms of mental stress and to aid sleep - EMA page 429, flagged for owner spot-check) added to insomnia.',
    'hydrastis_canadensis': 'REF-0455 is a critical review, not an RCT (retagged): names wounds, digestive disorders, ulcers, skin and eye ailments/infections, antimicrobial and anti-inflammatory effects - removed from arthritis, bloating, diarrhoea, indigestion (vague "digestive disorders") and sore-throat. REF-0456 purged (berberine chemistry review; names no goldenseal; berberine is not specific to this plant). REF-0588 (MRSA, in vitro) removed from wounds; retagged preclinical.',
    'hypericum_perforatum': 'REF-0181 (Natural Standard 2013; truncated title, no URL, paywalled) ' + UNVER + '.',
    'hyssopus_officinalis': 'REF-0845 is a genus-level Hyssopus review (7 species, prose-only attribution) - removed from all pairs; retagged narrative-review. REF-1804 (asthmatic mouse model) names airway inflammation and asthma only - removed from bronchitis and cough.',
    'inonotus_obliquus': 'REF-0272 (Shashkina 2006, Pharm Chem J; DOI and Springer abstract added) - its abstract names no condition, only chemistry, pharmacology and melanin - removed from all 8 pairs. Cognitive-function note corrected: it described a Parkinson model, but the cited study (REF-2990) is scopolamine amnesia.',
    'inula_helenium': 'REF-0445 (Kenny 2022: in vitro anti-staphylococcal; "respiratory and dermal ailments" in Irish ethnomedicine) removed from bronchitis and wounds; retagged preclinical. REF-0539 (anti-staphylococcal essential oil) removed from wounds.',
    'juniperus_communis': 'REF-0073 (2010 Community monograph) merged into its 2021 revision REF-3066 (invariant 11). REF-0035 (British Herbal Pharmacopoeia 1983, not available online) ' + UNVER + '. REF-3066 (known indications: urinary flushing in minor urinary complaints; dyspeptic complaints such as bloating and flatulence - EMA page 429, flagged for owner spot-check) kept for urinary-support, bloating and indigestion; removed from swelling and UTI (birch precedent).',
    'knautia_arvensis': 'REF-2811 purged: it tested Knautia drymeia and K. macedonica, not K. arvensis (its only link to field scabious is genus-level prose). All 6 pairs dropped; plant leaves the Symptom tool.',
    'lactuca_virosa': 'Herbal Reality REF-0526 (page read) names anxiety, nervous tension, insomnia, cough and pain, not stress, headache or back pain. RxList REF-0527 (page read) names pain, insomnia, cough, restlessness - added to insomnia and cough, removed from headache and back-pain. REF-0622 (lactucin and lactucopicrin, compounds characteristic of L. virosa; mouse analgesia and sedation) kept for pain and insomnia as compound evidence, removed from headache and back-pain.',
    'lamium_album': 'REF-0339 purged (owner decision 2026-11-12: an Ask-Ayurveda wiki page with no checkable references is not a source). Herbal Reality REF-0348 (page read) names bruises, diarrhoea, wounds, inflammation, joint aches/gout and upper-respiratory catarrh - removed from cough and skin, added to respiratory-support. REF-1746 (Planta Med 2017; traditional use in chronic bronchitis, pharyngitis and skin inflammation, anti-inflammatory in neutrophils) added to bronchitis, inflammation, skin-irritation.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 9', os.path.join(os.path.dirname(__file__), 'batch09_changes.tsv'), **BIB)

# Follow-up (2026-11-12): pairs left mechanistic-only must not carry a claim-style note.
FOLLOWUP = {
    'hydrastis_canadensis': [('note', 'indigestion', 'inferred from digestive action')],
    'inula_helenium': [('note', 'bronchitis', 'inferred from expectorant action'),
                       ('note', 'cough', 'inferred from expectorant action')],
    'lamium_album': [('note', 'cough', 'inferred from expectorant action')],
}
FOLLOWUP_NOTES = {k: 'notes of pairs left mechanistic-only reset to "inferred from ... action".' for k in FOLLOWUP}
