"""Batch-2 fixes (2026-11-10 symptom audit): althaea .. artemisia-vulgaris.
Run from the repo root: python docs/audits/2026-11-10-symptom-audit/fix_batch02.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

AB = ('arthritis', 'bloating', 'blood-sugar', 'indigestion', 'infection', 'inflammation', 'menstrual-cramps',
      'metabolic-support', 'muscle-spasm', 'skin-irritation', 'wounds')
AV = ('arthritis', 'bloating', 'indigestion', 'infection', 'inflammation', 'insomnia', 'menstrual-cramps',
      'muscle-spasm', 'skin-irritation', 'wounds')

PLAN = {
    'althaea_officinalis': [
        ('rm', 'acid-reflux', ['REF-0481']),
        ('rm', 'eczema', ['REF-0482']),
        ('rm', 'skin-irritation', ['REF-0482', 'REF-1370']),
        ('add', 'sore-throat', ['REF-0482']), ('add', 'indigestion', ['REF-0482']),
    ],
    'andrographis_paniculata': [
        ('rm', 'arthritis', ['REF-0393', 'REF-0394']),
        ('rm', 'fever', ['REF-0394']),
        ('rm', 'immune-support', ['REF-0393', 'REF-0394']), ('add', 'immune-support', ['REF-0395']),
        ('rm', 'inflammation', ['REF-0394']), ('add', 'inflammation', ['REF-0395']),
        ('rm', 'skin-irritation', ['REF-0393', 'REF-0394']),
        ('rm', 'sore-throat', ['REF-0395']), ('add', 'sore-throat', ['REF-1615']),
        ('rm', 'wounds', ['REF-0393', 'REF-0394']),
    ],
    'anethum_graveolens': [
        ('merge', 'REF-0103', 'REF-1391'),  # same trial; REF-0103's DOI does not resolve
        ('merge', 'REF-0310', 'REF-3094'),  # same WHO monograph (Fructus Anethi)
        ('null', 'inflammation', ['REF-1391']),  # hs-CRP measured, no significant change
    ] + [('rm', c, ['REF-3094']) for c in ('arthritis', 'cardiovascular-support', 'infection', 'metabolic-support',
                                          'skin-irritation', 'swelling', 'uti', 'wounds')],
    'angelica_archangelica': [
        ('rm', c, ['REF-0695']) for c in ('acid-reflux', 'appetite-loss', 'arthritis', 'bloating', 'bronchitis', 'cold',
                                          'cough', 'fever', 'indigestion', 'insomnia', 'memory', 'respiratory-support',
                                          'skin-irritation', 'stress')
    ] + [('rm', 'arthritis', ['REF-0397', 'REF-0696']), ('rm', 'skin-irritation', ['REF-0397'])],
    'arctium_lappa': [
        ('purge', 'REF-2858'), ('purge', 'REF-2860'),  # arctigenin, no source species named
    ] + [('rm', c, ['REF-0309', 'REF-0313']) for c in ('arthritis', 'bloating', 'eczema', 'indigestion', 'inflammation',
                                                      'skin-irritation')]
      + [('rm', c, ['REF-0705', 'REF-0709']) for c in ('arthritis', 'eczema', 'skin-irritation')]
      + [('rmk', 'bloating', ['REF-0706']), ('rmk', 'indigestion', ['REF-0706'])],
    'arctium_minus': [('purge', 'REF-0476'), ('purge', 'REF-0477')],  # pages describe A. lappa
    'arctostaphylos_uva_ursi': [
        ('purge', 'REF-2862'),  # arbutin across ~50 plant families, no species
        ('null', 'uti', ['REF-0700', 'REF-0701']), ('null', 'infection', ['REF-0700', 'REF-0701']),
        ('null', 'urinary-support', ['REF-0700', 'REF-0701']),
        ('rm', 'diarrhea', ['REF-0405', 'REF-0407']),
        ('rm', 'skin-irritation', ['REF-0405', 'REF-0407']),
        ('rm', 'wounds', ['REF-0405']),
        ('rmk', 'urinary-support', ['REF-2376']),
        ('add', 'uti', ['REF-0407']), ('add', 'infection', ['REF-0407']),
    ],
    'arnica_montana': [
        ('purge', 'REF-0399'), ('purge', 'REF-2098'), ('purge', 'REF-2103'),  # homeopathic arnica
    ] + [('rm', c, ['REF-0398']) for c in ('arthritis', 'back-pain', 'bruising', 'headache', 'muscle-soreness',
                                          'pain', 'skin-irritation', 'swelling', 'wounds')]
      + [('add', c, ['REF-0726']) for c in ('arthritis', 'bruising', 'inflammation')],
    'artemisia_absinthium': [('rm', c, ['REF-0112']) for c in AB]
      + [('rm', c, ['REF-0098']) for c in ('arthritis', 'blood-sugar', 'inflammation', 'menstrual-cramps',
                                          'metabolic-support', 'muscle-spasm', 'skin-irritation', 'wounds')]
      + [('rm', 'cancer', ['REF-0728'])],
    'artemisia_vulgaris': [('rm', c, ['REF-0149']) for c in AV]
      + [('rm', c, ['REF-0098']) for c in ('bloating', 'infection', 'insomnia', 'menstrual-cramps', 'muscle-spasm',
                                          'skin-irritation', 'wounds')],
}

NOTES = {
    'althaea_officinalis': 'EU (HMPC) + ESCOP monographs cover dry cough, oral/pharyngeal irritation and mild gastric discomfort only: REF-0481 removed from acid-reflux, REF-0482 (ESCOP) removed from eczema/skin-irritation and wired to sore-throat + indigestion. REF-1370 (rat wound healing) removed from skin-irritation.',
    'andrographis_paniculata': 'REF-0393 (review, was mis-tagged rct) and REF-0394 kept only where their abstracts name the use. MSKCC About Herbs (REF-0395) names colds/flu, URIs, fevers, infectious disease, immunostimulation, inflammation - not sore throat; wired accordingly. REF-1615 (RCT, A. paniculata spray in acute pharyngitis, positive) added to sore-throat.',
    'anethum_graveolens': 'Merged duplicates REF-0103 -> REF-1391 (same Haidari 2020 trial; REF-0103 DOI unresolvable) and REF-0310 -> REF-3094 (same WHO Fructus Anethi monograph). WHO text (vol. 3): dyspepsia, gastritis, flatulence, stomach ache; traditional dysuria, diarrhoea, dysmenorrhoea, insomnia; experimental anti-inflammatory/analgesic - so removed from arthritis, cardiovascular, infection, metabolic, skin, swelling, uti, wounds. REF-1391 measured hs-CRP with no significant change -> null_result_ids for inflammation.',
    'angelica_archangelica': 'REF-0695 (narrative review) names anti-anxiety, cognition enhancer, antiviral, anti-inflammatory, gastroprotective activities only - kept for anxiety, nervous-tension, cognitive-function, inflammation; removed from 14 other pairs. REF-0397 (columbianetin) and REF-0696 (fibromyalgia model) removed from arthritis/skin.',
    'arctium_lappa': 'REF-0309 (WHO monographs 2002: no burdock monograph found in WHO vols 1-4) and REF-0313 (Xu 2008, could not be located) removed from every symptom as unverifiable. REF-0705/REF-0709 kept only for inflammation (REF-0709 names contact dermatitis as a SIDE EFFECT, not a use). REF-2858/2860 purged (arctigenin, species not named).',
    'arctium_minus': 'REF-0476 (Herbal Reality) and REF-0477 (Drugs.com) purged: both describe Arctium lappa and only list A. minus as an alternate name (owner decision 2026-11-10: wrong species). Only A. minus-specific studies remain.',
    'arctostaphylos_uva_ursi': 'REF-0701 (ATAFUTI: no effect on symptom severity) and REF-0700 (more symptom burden than fosfomycin) moved to null_result_ids. EU + ESCOP monographs cover lower UTI only - removed from diarrhea, skin-irritation, wounds; ESCOP REF-0407 wired to uti + infection. REF-2862 purged (arbutin, no species).',
    'arnica_montana': 'Homeopathic studies purged (owner decision 2026-11-10: not evidence for the plant): REF-0399 (also non-significant vs placebo, p=0.059), REF-2098, REF-2103 (Alpine/Boiron pellets; p=0.097/0.074). REF-0398 abstract names only antibacterial/anti-inflammatory/antitumour activity. REF-0726 quotes the EU monograph (blunt injuries, inflammations, rheumatic muscle and joint complaints) - wired to bruising, inflammation, arthritis.',
    'artemisia_absinthium': "REF-0112 (Hoffmann, Medical Herbalism) unverifiable - removed. Grieve (A Modern Herbal, Common Wormwood) supports flatulence, enfeebled digestion and antiseptic use; its gout line is about Roman wormwood - removed from the other 8 pairs. REF-0728 abstract names no cancer use.",
    'artemisia_vulgaris': "REF-0149 (Kung & Ko 2002) could not be located - removed as unverifiable. Grieve (Mugwort) supports stomach disorders, rheumatism (moxa) and 'swellings of the tonsils'; emmenagogue/nervine are not menstrual cramps or insomnia - removed from 7 pairs.",
}

if __name__ == '__main__':
    fixlib.main(PLAN, NOTES, 'batch 2', os.path.join(os.path.dirname(__file__), 'batch02_changes.tsv'))
