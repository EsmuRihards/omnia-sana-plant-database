"""Batch-12 fixes (2026-11-10 symptom audit): origanum-majorana .. petroselinum. Run from the repo root.
No new owner policy this batch; standing rules applied (null results incl. Cochrane, "may be effective" =
support as written, superseded Cochrane version merged into the current one, wrong species, unverifiable or
condition-less sources, compound papers labelled, an RCT/SR counts only for what it measured)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'
KIEFER_ABS = ("The herbal remedies referred to as \"ginseng\" are derived from the roots of several plants. One of the most "
              "commonly used and researched of the ginsengs is Panax ginseng, also called Asian or Korean ginseng. The main "
              "active components of Panax ginseng are ginsenosides, which have been shown to have a variety of beneficial "
              "effects, including anti-inflammatory, antioxidant, and anticancer effects. Results of clinical research "
              "studies demonstrate that Panax ginseng may improve psychologic function, immune function, and conditions "
              "associated with diabetes. Overall, Panax ginseng appears to be well tolerated, although caution is advised "
              "about concomitant use with some pharmaceuticals, such as warfarin, oral hypoglycemic agents, insulin, and "
              "phenelzine. Panax ginseng does not appear to enhance physical performance. Products with a standardized "
              "ginsenoside concentration are available.")

BIB = dict(
    retag={'REF-0485': 'narrative-review', 'REF-0486': 'narrative-review', 'REF-0941': 'narrative-review',
           'REF-0014': 'narrative-review', 'REF-0137': 'narrative-review', 'REF-0192': 'narrative-review',
           'REF-0493': 'narrative-review', 'REF-0426': 'narrative-review', 'REF-0489': 'narrative-review',
           'REF-0546': 'narrative-review', 'REF-0954': 'narrative-review', 'REF-0545': 'preclinical'},
    sets={'REF-0137': {'journal': 'American Family Physician', 'volume': '68', 'number': '8', 'pages': '1539--1542',
                       'pmid': '14596440', 'abstract': KIEFER_ABS},
          'REF-0192': {'year': '2012', 'journal': 'Journal of Ginseng Research'},
          'REF-0426': {'journal': 'Pediatrics in Review', 'pmid': '17545337'}},
    delete=['REF-0124',   # Cochrane on cranberry products for UTI: trials used American cranberry (V. macrocarpon)
            'REF-1869'],  # Cochrane 2008 Pelargonium, superseded by the 2013 update REF-1870 (invariant 11)
)

MAJ10 = ('arthritis', 'bloating', 'indigestion', 'infection', 'inflammation', 'insomnia', 'menstrual-cramps',
         'muscle-spasm', 'skin-irritation', 'wounds')
GIN12 = ('arthritis', 'blood-sugar', 'cardiovascular-support', 'cognitive-function', 'cold', 'fatigue', 'immune-support',
         'inflammation', 'memory', 'metabolic-support', 'muscle-soreness', 'skin-irritation')
BUT9 = ('allergy', 'asthma', 'cough', 'fever', 'headache', 'menstrual-cramps', 'migraine', 'muscle-spasm')

PLAN = {
    'origanum_majorana': [('rm', c, ['REF-0112']) for c in MAJ10],
    'origanum_vulgare': [('rm', c, ['REF-0486']) for c in ('arthritis', 'inflammation', 'skin-irritation', 'wounds')]
      + [('rm', c, ['REF-0485']) for c in ('skin-irritation', 'wounds')]
      + [('note', 'indigestion', 'inferred from digestive action')],
    'oxycoccus_palustris': [('purge', 'REF-0124')],
    'panax_ginseng': [('rm', c, ['REF-0014', 'REF-0192']) for c in GIN12]
      + [('rm', c, ['REF-0137']) for c in ('arthritis', 'cardiovascular-support', 'cognitive-function', 'cold',
                                          'fatigue', 'memory', 'muscle-soreness', 'skin-irritation')]
      + [('null', 'cognitive-function', ['REF-1475'])],
    'passiflora_incarnata': [('rm', 'insomnia', ['REF-0490']), ('rm', 'nervous-tension', ['REF-0490', 'REF-0491']),
                             ('rm', 'anxiety', ['REF-0491'])],
    'paullinia_cupana': [('rm', 'fatigue', ['REF-0106', 'REF-0955']), ('null', 'fatigue', ['REF-0951']),
                         ('rm', 'memory', ['REF-0950'])],
    'pelargonium_sidoides': [('merge', 'REF-1869', 'REF-1870'), ('rm', 'cold', ['REF-0492']),
                             ('rm', 'sinusitis', ['REF-0492']), ('rm', 'immune-support', ['REF-0493'])]
      + [('add', c, ['REF-1870']) for c in ('bronchitis', 'cold', 'sinusitis')],
    'petasites_hybridus': [('rm', c, ['REF-0426']) for c in BUT9],
    'petroselinum_crispum': [('rm', c, ['REF-0489']) for c in ('bad-breath', 'bloating', 'detox', 'swelling', 'uti')]
      + [('rm', c, ['REF-0545']) for c in ('swelling', 'uti')]
      + [('rm', c, ['REF-0546']) for c in ('detox', 'swelling', 'uti')]
      + [('note', 'bloating', 'inferred from digestive action'),
         ('note', 'indigestion', 'Traditional stomach tonic for indigestion (review of traditional uses)')],
}

NOTES = {
    'origanum_majorana': 'REF-0112 (Hoffmann; unverifiable since batch 2) removed from all 10 pairs; infection (antifungal rat study) and muscle-spasm (gut antispasmodic study) keep their direct sources.',
    'origanum_vulgare': 'REF-0486 (carvacrol review; carvacrol is oregano\'s signature phenol - compound evidence) names antimicrobial, antioxidant and anticancer activity only - kept for infection, removed from 4 pairs. REF-0485 (O. vulgare antimicrobial review; retagged) removed from skin and wounds.',
    'oxycoccus_palustris': 'REF-0124 purged (wrong species): the Cochrane review on cranberries for UTI covers trials of American cranberry (Vaccinium macrocarpon) products, not the European small cranberry. REF-0941 (V. oxycoccos review: urinary-tract protection, antibacterial) remains; retagged.',
    'panax_ginseng': 'Cochrane REF-1475 ("Ginseng for cognition": "a lack of convincing evidence") was cited as SUPPORT - moved to null_result_ids. REF-0014 (Attele 1999 commentary) and REF-0192 (traditional prescriptions; year corrected to 2012, not an RCT) name no condition - removed from all 12 pairs. REF-0137 (Kiefer 2003 AFP, PubMed 14596440: may improve psychologic function, immune function and diabetes-related conditions; anti-inflammatory; "does not appear to enhance physical performance") kept for immune-support, blood-sugar, metabolic-support, inflammation only.',
    'passiflora_incarnata': 'REF-0490 (SR of neuropsychiatric trials: reduced anxiety) removed from insomnia and nervous-tension (it reviewed anxiety outcomes). EU monograph REF-0491 (relief of mild symptoms of mental stress and to aid sleep - EMA page 429, flagged for owner spot-check) removed from anxiety and nervous-tension, kept for stress and insomnia.',
    'paullinia_cupana': 'REF-0951 (MA: guarana "did not reduce cancer-related fatigue", p=0.98) was cited as SUPPORT - moved to null_result_ids. REF-0106 (acute RCT: memory and alertness) and REF-0955 (cycling time-trial) measured no fatigue - removed. REF-0950 (MA: faster response time) names no memory outcome - removed from memory.',
    'pelargonium_sidoides': 'Cochrane 2008 REF-1869 merged into its 2013 update REF-1870 (invariant 11); the 2013 review ("may be effective" for acute bronchitis, rhinosinusitis and the common cold; low-quality evidence) wired as support per the owner\'s may-be-effective rule. REF-0492 (paediatric aRTI review) kept for infection, bronchitis, sore throat; removed from cold and sinusitis. REF-0493 (registration review; retagged) names bronchitis only.',
    'petasites_hybridus': 'REF-0426 (Sadler 2007 Pediatrics in Review column; no abstract, text not retrievable) ' + UNVER + '. Fever pair (its note described HAY fever) dropped. Allergy (SR + Ze 339), migraine/headache (two RCTs) and asthma (open trial) keep their sources.',
    'petroselinum_crispum': 'REF-0489 (2024 review of traditional uses; was tagged rct) names diuretic, liver and stomach tonic, urolithiasis, indigestion, hepato- and nephroprotection - removed from bad breath, bloating, detox, swelling, UTI. REF-0545 (rat diuretic) and REF-0546 (review) removed from swelling/UTI/detox (diuresis is not swelling or infection evidence - birch precedent).',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 12', os.path.join(os.path.dirname(__file__), 'batch12_changes.tsv'), **BIB)

# Follow-up (2026-11-12): claim note on a pair left mechanistic-only.
FOLLOWUP = {'passiflora_incarnata': [('note', 'nervous-tension', 'inferred from anxiolytic action')]}
FOLLOWUP_NOTES = {'passiflora_incarnata': 'nervous-tension note reset (pair now mechanistic-only).'}
