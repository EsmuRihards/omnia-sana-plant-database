"""Batch-3 fixes (asclepias .. campanula) plus the no-effect / not-a-source flags raised by the
truncated-abstract repair (truncated_abstracts.md). Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVERIFIED = 'removed from every symptom as unverifiable'

PLAN = {
    # ---------------- batch 3
    'asclepias_tuberosa': [
        ('rm', c, ['REF-0495']) for c in ('arthritis', 'bronchitis', 'cold', 'cough', 'fever', 'inflammation',
                                          'respiratory-support', 'skin-irritation')
    ] + [('rm', 'bronchitis', ['REF-1948']), ('rm', 'respiratory-support', ['REF-1948']),
         ('mexcl', 'cold', ['REF-1948']), ('mexcl', 'cough', ['REF-1948']), ('mexcl', 'fever', ['REF-1948']),
         ('rm', 'cough', ['REF-0494']), ('rm', 'fever', ['REF-0494']),
         ('rm', 'skin-irritation', ['REF-1947'])],
    'astragalus_membranaceus': [
        ('rm', c, ['REF-0402']) for c in ('arthritis', 'fatigue', 'kidney-support', 'skin-irritation', 'stress')
    ] + [('rm', 'cold', ['REF-0401']),
         ('null', 'kidney-support', ['REF-0586']),  # Cochrane: no definitive conclusions possible
         ('add', 'fatigue', ['REF-2261'])],          # SR: "may benefit" (owner rule: support as written)
    'bacopa_monnieri': [('merge', 'REF-0038', 'REF-0740')]  # same Calabrese 2008 RCT
      + [('rm', c, ['REF-0309']) for c in ('arthritis', 'cognitive-function', 'inflammation', 'insomnia', 'memory',
                                          'skin-irritation')],
    'betula_pendula': [('rm', 'swelling', ['REF-0080']), ('rm', 'uti', ['REF-0080'])],
    'bistorta_officinalis': [
        ('rm', c, ['REF-0411']) for c in ('arthritis', 'bruising', 'diarrhea', 'heavy-bleeding', 'inflammation',
                                          'skin-irritation', 'sore-throat', 'wounds')
    ] + [('rm', c, ['REF-0746']) for c in ('arthritis', 'bruising', 'sore-throat', 'wounds')]
      + [('rm', 'infection', ['REF-0627'])],
    'borago_officinalis': [('purge', 'REF-0129')]  # GLA review, never names borage
      + [('rm', c, ['REF-0309']) for c in ('arthritis', 'back-pain', 'bloating', 'cold', 'eczema', 'headache',
                                          'immune-support', 'indigestion', 'inflammation', 'pain',
                                          'respiratory-support', 'skin-irritation')]
      + [('add', c, ['REF-0749']) for c in ('cold', 'respiratory-support', 'inflammation')],
    'boswellia_serrata': [
        ('purge', 'REF-0423'),  # boswellic acids of "different Boswellia species", no B. serrata
        ('purge', 'REF-1817'),  # Curcuma + Boswellia combination product
        ('purge', 'REF-2874'), ('purge', 'REF-2875'),  # AKBA, species not named / "Boswellia" genus only
    ],
    'calendula_officinalis': [('purge', 'REF-0183')]  # phantom: no such RCT in PubMed, no DOI/journal
      + [('rm', c, ['REF-0112']) for c in ('arthritis', 'bruising', 'eczema', 'infection', 'inflammation',
                                          'skin-irritation', 'wounds')]
      + [('rm', c, ['REF-0199']) for c in ('bruising', 'inflammation', 'skin-irritation')]
      + [('add', 'wounds', ['REF-0752', 'REF-2125']),
         ('mexcl', 'bruising', ['REF-0752', 'REF-2125', 'REF-2129'])],
    'camellia_sinensis': [
        ('null', 'cancer', ['REF-1961']),  # Cochrane 2020: no conclusive evidence
        ('rm', 'memory', ['REF-0184']),
    ] + [('rm', c, ['REF-0045']) for c in ('arthritis', 'cognitive-function', 'infection', 'inflammation', 'memory',
                                          'skin-irritation', 'wounds')]
      + [('rm', c, ['REF-0061']) for c in ('blood-sugar', 'cardiovascular-support', 'metabolic-support')],
    'campanula_persicifolia': [('rm', c, ['REF-2816']) for c in ('inflammation', 'skin-irritation', 'sore-throat',
                                                                'respiratory-support')]
      + [('mexcl', c, ['REF-2816']) for c in ('wounds', 'infection')],
    # ---------------- flags from the truncated-abstract repair
    'cynara_scolymus': [],  # REF-0584 'potential ... not yet convincing' = support as written (owner rule)
    'epilobium_parviflorum': [('rm', 'prostate-support', ['REF-0404']), ('rm', 'urinary-support', ['REF-0404'])],
    'hibiscus_sabdariffa': [('nulladd', 'high-blood-pressure', ['REF-1844']), ('nulladd', 'cardiovascular-support', ['REF-1844'])],
    'lavandula_angustifolia': [('nulladd', 'insomnia', ['REF-0858'])],
    'oenothera_biennis': [('purge', 'REF-2588')],
    'rhododendron_tomentosum': [('purge', 'REF-0881')],
    'serenoa_repens': [('null', 'prostate-support', ['REF-1895']), ('null', 'urinary-support', ['REF-1895'])],
    'tanacetum_parthenium': [('purge', 'REF-1577')],
    'thymus_vulgaris': [('purge', 'REF-0593')],
}
del PLAN['cynara_scolymus']

NOTES = {
    'asclepias_tuberosa': 'REF-0495 (Herbs2000, 403) and REF-1948 (Lockwood 1848, no text found) ' + UNVERIFIED + '. REF-0494 (Naturopathic Herbalist) names bronchitis, pleurisy/breathing, influenza and inflammation of serous tissues - not cough or fever (expectorant/diaphoretic are actions). REF-1947 (fibroblast proliferation) is not skin-irritation evidence.',
    'astragalus_membranaceus': 'REF-0586 (Cochrane CKD: definitive conclusions could not be made) moved to null_result_ids. REF-0402 (AS-IV review) kept only for infection/inflammation/cancer/immune uses it names; REF-0401 removed from cold. REF-2261 (SR, post-stroke fatigue, "may benefit") added to fatigue per owner rule 2026-11-10 (may-help reviews count as written).',
    'bacopa_monnieri': 'Merged duplicate REF-0038 -> REF-0740 (same Calabrese 2008 RCT). REF-0309 (generic "WHO Monographs" 2002; no Bacopa monograph found) ' + UNVERIFIED + '.',
    'betula_pendula': 'EMA birch-leaf summary (REF-0080) covers flushing of the urinary tract in minor urinary complaints only - removed from swelling and uti.',
    'bistorta_officinalis': 'REF-0411 (WebMD page, now 404) ' + UNVERIFIED + '. REF-0746 kept for diarrhoea, skin, antibacterial and anti-inflammatory uses it names; removed from arthritis, bruising, sore-throat, wounds. REF-0627 is GC-MS chemistry only - removed from infection.',
    'borago_officinalis': 'REF-0129 purged (GLA review never names borage). REF-0309 (generic WHO 2002, no borage monograph) ' + UNVERIFIED + '. REF-0749 review names colds, influenza, respiratory disorders and inflammation - wired as direct source there.',
    'boswellia_serrata': 'Purged REF-0423 (boswellic acids of unnamed Boswellia species), REF-1817 (Curcuma + Boswellia product), REF-2874/2875 (AKBA, species not named). Asthma and IBD rested only on REF-0423.',
    'calendula_officinalis': 'REF-0183 purged as a phantom: the "double-blind RCT of a monograph-based Calendula cream" (Nicolaus 2017) is not in PubMed and had no DOI or journal; it had lifted 6 pairs to 5/10. REF-0112 (Hoffmann) ' + UNVERIFIED + '. REF-0199 (rat excision wounds) kept for wounds only. Added REF-0752 (SR: some evidence for wound healing) and REF-2125 (RCT, burn wounds, positive) to wounds.',
    'camellia_sinensis': 'REF-1961 (Cochrane 2020: no conclusive evidence for green tea and cancer) moved to null_result_ids. REF-0045 abstract (PubMed 20370896) names cancer, heart/liver disease, obesity, type 2 diabetes, CV risk only. REF-0061 (Drake 2015) could not be located - ' + UNVERIFIED + '. REF-0184 (L-theanine EEG RCT: alertness/attention) kept for cognitive-function only.',
    'campanula_persicifolia': 'REF-2816 is a genus-level Campanula review that never names C. persicifolia (prose-only attribution) - removed from every symptom; no species-level evidence remains.',
    'epilobium_parviflorum': 'REF-0404 (ProstateEZE Max, multi-herb product) removed from prostate-support and urinary-support (kept for its safety notes).',
    'hibiscus_sabdariffa': 'REF-1844 (SR: trials do not provide reliable evidence to recommend H. sabdariffa for hypertension) moved to null_result_ids for high-blood-pressure and cardiovascular-support.',
    'lavandula_angustifolia': 'REF-0858 (RCT, lavender oil inhalation, postmenopausal insomnia: no significant difference on the primary outcome) recorded in null_result_ids for insomnia.',
    'oenothera_biennis': 'REF-2588 purged: a 4-herb nutraceutical, not evening primrose alone.',
    'rhododendron_tomentosum': 'REF-0881 purged: homeopathic (Arnica 50M / Ledum 50M pads) - not evidence for the plant (owner rule 2026-11-10).',
    'serenoa_repens': 'REF-1895 (12-week RCT: no significant benefit over placebo) moved to null_result_ids for prostate-support and urinary-support.',
    'tanacetum_parthenium': 'REF-1577 purged: feverfew + white willow combination (Mig-RL), not feverfew alone.',
    'thymus_vulgaris': 'REF-0593 purged: thyme + ivy combination product, not thyme alone.',
}

if __name__ == '__main__':
    fixlib.main(PLAN, NOTES, 'batch 3', os.path.join(os.path.dirname(__file__), 'batch03_changes.tsv'))
