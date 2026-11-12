"""Batch-8 fixes (2026-11-10 symptom audit): geum-rivale .. hippophae. Run from the repo root.
No new owner policy this batch; standing rules applied (null results, source must name the symptom,
multi-herb products, wrong species, genus-level reviews, unverifiable sources, bot-blocked
monographs kept on known indication text and flagged)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'

ASL_ABS = ("The roots and rhizomes of licorice (Glycyrrhiza) species have long been used worldwide as a herbal medicine and "
           "natural sweetener. Licorice root is a traditional medicine used mainly for the treatment of peptic ulcer, "
           "hepatitis C, and pulmonary and skin diseases, although clinical and experimental studies suggest that it has "
           "several other useful pharmacological properties such as antiinflammatory, antiviral, antimicrobial, "
           "antioxidative, anticancer activities, immunomodulatory, hepatoprotective and cardioprotective effects. A large "
           "number of components have been isolated from licorice, including triterpene saponins, flavonoids, "
           "isoflavonoids and chalcones, with glycyrrhizic acid normally being considered to be the main biologically "
           "active component. This review summarizes the phytochemical, pharmacological and pharmacokinetics data, "
           "together with the clinical and adverse effects of licorice and its bioactive components.")

BIB = dict(
    retag={'REF-0532': 'narrative-review', 'REF-0473': 'clinical', 'REF-0012': 'narrative-review',
           'REF-0089': 'narrative-review', 'REF-2768': 'preclinical', 'REF-0642': 'narrative-review',
           'REF-0645': 'narrative-review', 'REF-0444': 'narrative-review', 'REF-0562': 'narrative-review'},
    sets={  # verified against PubMed 2026-11-11
        'REF-0012': {'journal': 'Phytotherapy Research', 'volume': '22', 'number': '6', 'pages': '709--724',
                     'doi': '10.1002/ptr.2362', 'pmid': '18446848', 'abstract': ASL_ABS},
        'REF-0089': {'year': '2005', 'journal': 'Journal of Ethnopharmacology'},
        'REF-0308': {'title': 'WHO Monographs on Selected Medicinal Plants, Volume 1'},
        'REF-3060': {'pmid': '18047444'},
    },
    delete=['REF-0179',   # a PubMed search-results URL, not a source
            'REF-0465',   # meta-analysis of Hibiscus COMBINED with other plant extracts
            'REF-2777',   # tests Geum urbanum, not G. rivale
            'REF-0305'],  # duplicate of REF-0308 (WHO Monographs vol. 1, 1999) - merged
)

GLY_ALL = ('acid-reflux', 'arthritis', 'bronchitis', 'cold', 'cough', 'immune-support', 'indigestion', 'infection',
           'inflammation', 'menstrual-cramps', 'muscle-spasm', 'respiratory-support', 'skin-irritation', 'wounds')
HIP_ALL = ('arthritis', 'blood-sugar', 'bruising', 'cardiovascular-support', 'cold', 'eczema', 'immune-support',
           'inflammation', 'metabolic-support', 'skin-irritation', 'wounds')

PLAN = {
    'curcuma_longa': [('merge', 'REF-0305', 'REF-0308')],
    'geum_rivale': [('purge', 'REF-2777'), ('rm', 'diarrhea', ['REF-2768']), ('rm', 'sore-throat', ['REF-2763']),
                    ('mexcl', 'diarrhea', ['REF-2769']), ('add', 'infection', ['REF-2761'])],
    'ginkgo_biloba': [('null', 'cognitive-function', ['REF-0056']), ('null', 'memory', ['REF-0056'])]
      + [('rm', c, ['REF-0308']) for c in ('arthritis', 'inflammation', 'skin-irritation')]
      + [('add', 'cognitive-function', ['REF-2186', 'REF-2185']), ('add', 'memory', ['REF-2186', 'REF-2185'])],
    'glycyrrhiza_glabra': [('merge', 'REF-0305', 'REF-0308')]
      + [('rm', c, ['REF-0012', 'REF-0089']) for c in GLY_ALL]
      + [('rm', c, ['REF-0308']) for c in ('acid-reflux', 'cold', 'immune-support', 'menstrual-cramps', 'muscle-spasm',
                                          'skin-irritation', 'wounds')]
      + [('add', c, ['REF-3081']) for c in ('acid-reflux', 'indigestion', 'cough', 'cold', 'respiratory-support')],
    'gymnema_sylvestre': [('rm', 'blood-sugar', ['REF-2543'])],
    'hamamelis_virginiana': [('rm', 'bruising', ['REF-0531']), ('rm', 'wounds', ['REF-0531']),
                             ('rm', 'oral-health', ['REF-0532']), ('add', 'wounds', ['REF-0532']),
                             ('rm', 'arthritis', ['REF-0533'])],
    'harpagophytum_procumbens': [('rm', c, ['REF-0443']) for c in ('arthritis', 'back-pain', 'headache', 'inflammation',
                                                                  'pain', 'skin-irritation')]
      + [('rm', 'inflammation', ['REF-0444']), ('add', 'arthritis', ['REF-0561']),
         ('nulladd', 'arthritis', ['REF-1834'])],
    'hedera_helix': [('nulladd', c, ['REF-0833']) for c in ('cough', 'bronchitis', 'respiratory-support')],
    'hericium_erinaceus': [('purge', 'REF-0179'), ('rm', 'cancer', ['REF-0157']), ('add', 'cancer', ['REF-0645']),
                           ('null', 'cognitive-function', ['REF-0641']), ('null', 'memory', ['REF-0641']),
                           ('rm', 'memory', ['REF-0640', 'REF-0642']), ('rm', 'cognitive-function', ['REF-0642']),
                           ('add', 'cognitive-function', ['REF-2419']), ('add', 'memory', ['REF-2419']),
                           ('rm', 'cold', ['REF-0644']), ('rm', 'bloating', ['REF-0645']),
                           ('rm', 'indigestion', ['REF-0645'])],
    'hibiscus_sabdariffa': [('purge', 'REF-0465'), ('rm', 'metabolic-support', ['REF-0567']),
                            ('nulladd', 'high-cholesterol', ['REF-1843'])],
    'hippophae_rhamnoides': [('rm', c, ['REF-0049', 'REF-0319']) for c in HIP_ALL]
      + [('add', 'blood-sugar', ['REF-2319']), ('add', 'cardiovascular-support', ['REF-2317']),
         ('add', 'immune-support', ['REF-2317'])]
      + [('add', c, ['REF-2318']) for c in ('wounds', 'eczema', 'skin-irritation', 'inflammation')],
}

NOTES = {
    'curcuma_longa': 'REF-0305 merged into REF-0308 (both were WHO Monographs on Selected Medicinal Plants vol. 1, 1999).',
    'geum_rivale': 'REF-2777 purged: its urolithin study tested Geum urbanum (and other plants), not G. rivale. REF-2768 (Rosaceae tannin/elastase screen) names no diarrhoea - removed; retagged preclinical. REF-2769 (1954 tannin anatomy) hidden from diarrhoea cards. REF-2763 (in vitro antimicrobial) removed from sore-throat. REF-2761 (antibacterial vs E. coli and S. aureus) added to infection.',
    'ginkgo_biloba': 'REF-0056 (GEM trial, DeKosky 2008, 3,069 people): G. biloba "was not effective in reducing either the overall incidence rate of dementia or AD incidence" - moved to null_result_ids for cognitive-function and memory. REF-0308 (WHO vol. 1, Folium Ginkgo) kept for cognitive-function, memory and cardiovascular-support per its known uses (cerebrovascular insufficiency with memory deficit; peripheral arterial occlusive disease) - WHO PDF bot-blocked, flagged for owner spot-check; removed from arthritis, inflammation, skin. Positive meta-analyses REF-2186 (EGb 761 in dementia) and REF-2185 (early AD, "might improve") moved from mechanistic to direct.',
    'glycyrrhiza_glabra': 'REF-0012 (Asl & Hosseinzadeh 2008, "Glycyrrhiza sp.") is a genus-level review with prose-only attribution - removed from all pairs; metadata and abstract added. REF-0089 (Fiore 2005; year corrected) abstract names no condition - removed from all pairs. REF-0305 merged into REF-0308 (WHO vol. 1, Radix Glycyrrhizae): kept for cough, bronchitis, respiratory-support, indigestion (dyspepsia, ulcers), arthritis and inflammation (anti-inflammatory use in rheumatism and arthritis) and infection (tuberculosis) per its known Medicinal uses text - WHO PDF bot-blocked, flagged; removed from 7 pairs. EU monograph REF-3081 (digestive symptoms incl. burning sensation and dyspepsia; expectorant in cough associated with cold - EMA page 429, flagged) added to acid-reflux, indigestion, cough, cold, respiratory-support.',
    'gymnema_sylvestre': 'REF-2543 (14-day RCT on sugar cravings and chocolate intake) measured no blood glucose - removed from blood-sugar.',
    'hamamelis_virginiana': 'EU monograph REF-0531 (known indications: minor skin inflammation and dryness, minor inflammation of the oral mucosa, itching and burning of haemorrhoids - EMA page 429, flagged for owner spot-check) removed from bruising and wounds. REF-0532 is a 2025 review, not an RCT (retagged): names antimicrobial, anti-inflammatory, wound-healing and skin effects - removed from oral-health, added to wounds. Herbal Reality REF-0533 (page read) names bruises, wounds, diarrhoea, haemorrhoids, varicose veins, skin - removed from arthritis.',
    'harpagophytum_procumbens': 'REF-0443 (Natural Standard SR) abstract names no condition and its text is not retrievable - removed from all pairs. REF-0444 (Chrubasik 2004 review, retagged) names arthrotic and low back pain only - removed from inflammation. SR REF-0561 (OA and low back pain) added to arthritis. REF-1834 (2006 OA review: the evidence "cannot provide a definitive answer" to whether it works) recorded in null_result_ids for arthritis.',
    'hedera_helix': 'REF-0833 (Sierocinski 2021 updated SR): ivy leaf is safe but "effects are minimal at best and of uncertain clinical importance" - recorded in null_result_ids for cough, bronchitis and respiratory-support (owner rule: not convincing = no effect). REF-0473 (Hedussin post-authorisation study, non-randomised) retagged clinical.',
    'hericium_erinaceus': 'REF-0179 purged: it was a PubMed search-results URL, not a source. REF-0157 (hericenone B anti-gastric-cancer, no journal; not in PubMed or OpenAlex) ' + UNVER + '; REF-0645 (WJG 2025 commentary: antineoplastic role in gastric carcinogenesis, H. pylori activity) added to cancer and removed from bloating/indigestion (it is about atrophic gastritis). REF-0641 (acute RCT: no significant effect on global cognition or mood) moved to null_result_ids for cognitive-function and memory. REF-0640 (pilot RCT: speed of performance, stress) kept for cognitive-function only. REF-0642 (review, retagged) names neuroprotection, not cognition or memory. Pilot RCT REF-2419 (erinacine A mycelia in mild AD: better CASI, MMSE, IADL) moved to direct for cognitive-function and memory. REF-0644 (macrophage immunostimulation) removed from cold.',
    'hibiscus_sabdariffa': 'REF-0465 purged: the meta-analysis pooled Hibiscus COMBINED with other plant extracts. REF-0567 names glycaemic status and blood pressure, not metabolic syndrome - removed from metabolic-support. REF-1843 (2013 MA: "does not support the efficacy" for lowering serum lipids) recorded in null_result_ids for high-cholesterol.',
    'hippophae_rhamnoides': 'REF-0049 (Chodak 2014) and REF-0319 (Zuniga-Lopez 2021) could not be located in PubMed or OpenAlex - ' + UNVER + '. Replaced where verified sources name the use: REF-2318 (dermatology review: wounds, burns, ulcers, inflammation, anti-atopic dermatitis, anti-psoriasis) -> wounds, eczema, skin-irritation, inflammation; REF-2317 (immunomodulatory, anti-atherogenic) -> immune-support, cardiovascular-support; REF-2319 (clinical lipid, blood pressure and blood glucose effects) -> blood-sugar.',
}

PLAN_NOTES = {
    'geum_rivale': [('note', 'diarrhea', 'inferred from astringent (tannin) action')],
}

if __name__ == '__main__':
    for k, ops in PLAN_NOTES.items():
        PLAN[k] = PLAN[k] + ops
    fixlib.main_with_bib(PLAN, NOTES, 'batch 8', os.path.join(os.path.dirname(__file__), 'batch08_changes.tsv'), **BIB)

# Follow-up applied after the main run (2026-11-12): wound/burn papers are not bruise evidence.
FOLLOWUP = {'hippophae_rhamnoides': [('mexcl', 'bruising', ['REF-2318'])]}
FOLLOWUP_NOTES = {'hippophae_rhamnoides': 'REF-2318 (wounds, burns) hidden from the bruising mechanistic cards; bruising dropped.'}
# run: python -c "import sys; sys.path.insert(0,'docs/audits/2026-11-10-symptom-audit'); import fix_batch08 as f, fixlib; fixlib.main(f.FOLLOWUP, f.FOLLOWUP_NOTES, 'batch 8', 'docs/audits/2026-11-10-symptom-audit/batch08_followup_changes.tsv')"
