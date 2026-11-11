"""Batch-5 fixes (2026-11-10 symptom audit): cnicus .. cynara. Run from the repo root.
Owner decision this batch: real sources that block automated reading (WHO vol. 1, NIH LactMed)
stay on the uses their known indication text names, flagged for owner spot-check."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'

PLAN = {
    'cnicus_benedictus': [('rm', c, ['REF-0419']) for c in ('appetite-loss', 'arthritis', 'bloating', 'indigestion',
                                                           'infection', 'inflammation', 'skin-irritation', 'wounds')]
      + [('rm', c, ['REF-0420']) for c in ('appetite-loss', 'bloating', 'indigestion', 'lactation-support')],
    'coffea_arabica': [
        ('rm', 'cardiovascular-support', ['REF-0081', 'REF-0178']),
        ('rm', 'cognitive-function', ['REF-0096', 'REF-0109', 'REF-0205']),
        ('rm', 'memory', ['REF-0109', 'REF-0178']),
        ('rm', 'metabolic-support', ['REF-0059', 'REF-0178']),
    ],
    'cordyceps_militaris': [('purge', 'REF-0111')],  # 6-mushroom blend, not C. militaris alone
    'coriandrum_sativum': [('rm', c, ['REF-0308']) for c in ('arthritis', 'bloating', 'indigestion', 'infection',
                                                            'inflammation', 'menstrual-cramps', 'metabolic-support',
                                                            'muscle-spasm', 'skin-irritation', 'wounds')]
      + [('rm', c, ['REF-0151']) for c in ('arthritis', 'bloating', 'indigestion', 'menstrual-cramps', 'muscle-spasm',
                                          'skin-irritation', 'wounds')],
    'crataegus_laevigata': [('rm', c, ['REF-0108']) for c in ('arthritis', 'cardiovascular-support', 'inflammation',
                                                             'insomnia', 'menstrual-cramps', 'muscle-spasm',
                                                             'skin-irritation')]
      + [('add', 'cardiovascular-support', ['REF-0082']), ('add', 'insomnia', ['REF-0082'])],
    'crocus_sativus': [('rm', c, ['REF-0115']) for c in ('arthritis', 'blood-sugar', 'cognitive-function', 'memory',
                                                        'menstrual-cramps', 'metabolic-support', 'skin-irritation')],
    'cuminum_cyminum': [('rm', c, ['REF-0008']) for c in ('arthritis', 'menstrual-cramps', 'skin-irritation', 'wounds')]
      + [('rm', 'bloating', ['REF-0656']), ('rm', 'indigestion', ['REF-0656']),
         ('null', 'metabolic-support', ['REF-0654', 'REF-0655']),
         ('rm', 'metabolic-support', ['REF-0286', 'REF-0652'])],
    'curcuma_longa': [('rm', c, ['REF-0305']) for c in ('blood-sugar', 'cardiovascular-support', 'metabolic-support')]
      + [('rm', c, ['REF-0002']) for c in ('arthritis', 'blood-sugar', 'infection', 'skin-irritation', 'wounds')]
      + [('add', 'arthritis', ['REF-0791', 'REF-0792']), ('add', 'skin-irritation', ['REF-2165'])],
    'cynara_scolymus': [('rm', c, ['REF-0461']) for c in ('bloating', 'detox', 'ibs', 'indigestion')],
}

NOTES = {
    'cnicus_benedictus': 'REF-0419 (folk-uses review) names no specific use - removed from 8 pairs. REF-0420 (Drugs.com, 403) ' + UNVER + '. REF-0421 (NIH LactMed) kept for lactation-support; page blocks automated reading - flagged for owner spot-check. Re-sourcing candidate: EU monograph Cnici benedicti herba (loss of appetite, dyspeptic complaints).',
    'coffea_arabica': 'REF-0081 (EFSA caffeine SAFETY opinion) is not cardiovascular-benefit evidence. MedlinePlus caffeine (REF-0178; caffeine = signature compound) supports alertness only (it lists raised blood pressure as an effect) - kept for cognitive-function. REF-0096 (sport performance), REF-0109 and REF-0205 (Parkinson risk) removed from cognitive/memory; REF-0059 (CVD cohort SR) removed from metabolic.',
    'cordyceps_militaris': 'REF-0111 purged: the RCT tested a 6-mushroom blend containing C. militaris, not C. militaris alone.',
    'coriandrum_sativum': 'REF-0308 ("WHO Monographs" 1999 = vol. 1, which has no coriander monograph) ' + UNVER + '. REF-0151 (Laribi 2015, PubMed 25776008) names antimicrobial, hypoglycemic, anti-inflammatory and other activities - kept for infection, inflammation, metabolic-support only.',
    'crataegus_laevigata': 'REF-0108 (Hedgerow Medicine, book) ' + UNVER + '. The EU monograph Crataegus spp. folium cum flore (REF-0082) covers C. laevigata explicitly (nervous cardiac complaints, mild mental stress, aid sleep) - added to cardiovascular-support and insomnia.',
    'crocus_sativus': 'REF-0115 is Hosseinzadeh & Nassiri-Asl 2013 (Avicenna Canon of Medicine and saffron, PubMed 22815242): names antidepressant, hypnotic, anti-inflammatory, hepatoprotective, bronchodilatory, emmenagogue uses - kept for insomnia and inflammation, removed from 7 pairs.',
    'cuminum_cyminum': 'REF-0654 (MA: results "do not support" cumin for glycemic markers) and REF-0655 (RCT: no effect on MetS components except DBP) moved to null_result_ids for metabolic-support. REF-0286/REF-0652 (lipid-only meta-analyses) removed from metabolic-support. REF-0656 (bowel motility after surgery) is not bloating/indigestion evidence. REF-0008 (Allaq 2020) full text names flatulence, dyspepsia, antispasmodic, antimicrobial, anti-inflammatory, antidiabetic - removed from arthritis, menstrual-cramps, skin, wounds.',
    'curcuma_longa': 'REF-0305 (WHO vol. 1, Rhizoma Curcumae Longae) kept on dyspepsia/acid dyspepsia, rheumatic pain and inflammation, skin diseases, ringworm and slow-healing wounds per its known Medicinal uses text; the WHO PDF blocks automated reading - flagged for owner spot-check. Removed from blood-sugar, cardiovascular, metabolic. REF-0002 (curcumin review; signature compound) kept for cardiovascular, metabolic, inflammation, cancer. Arthritis SR/MAs REF-0791/REF-0792 and skin SR REF-2165 moved from mechanistic-only to direct.',
    'cynara_scolymus': 'REF-0461 (review) names choleretic, hepatoprotective and lipid-lowering effects only - removed from bloating, detox, IBS, indigestion (the EU monograph REF-0462 still supports bloating/indigestion).',
}

if __name__ == '__main__':
    fixlib.main(PLAN, NOTES, 'batch 5', os.path.join(os.path.dirname(__file__), 'batch05_changes.tsv'))
