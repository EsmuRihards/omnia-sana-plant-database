"""Batch 6-7 follow-up: indication notes are shown on the site as the claim text, so a note must not
describe evidence that the audit removed. Rewrites the notes that still cited purged or nulled
sources (California poppy combination RCT, Euphrasia D3 eye-drop cohort, willowherb review) and
the notes of pairs left mechanistic-only. Run from the repo root."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

PLAN = {
    'eschscholzia_californica': [
        ('note', 'anxiety', 'Anxiolytic for anxiety and nervous tension (its alkaloids act on GABA-A receptors; laboratory evidence)'),
        ('note', 'nervous-tension', 'Anxiolytic for anxiety and nervous tension (its alkaloids act on GABA-A receptors; laboratory evidence)'),
        ('note', 'stress', 'EU traditional use for mild symptoms of mental stress'),
        ('note', 'insomnia', 'Mild sedative to aid sleep (EU traditional use; acts on GABA-A receptors in the laboratory)'),
    ],
    'euphrasia_officinalis': [
        ('note', 'eye-strain', 'Traditional eye compress or bath for eye irritation, redness and eye strain. Clinical evidence is lacking: the EMA found its efficacy undocumented and advises against home-made eye preparations, which are not sterile'),
    ],
    'foeniculum_vulgare': [
        ('note', 'menstrual-cramps', 'Relieves primary dysmenorrhoea (menstrual) pain - meta-analyses of small RCTs find fennel reduces pain intensity versus placebo, similar to mefenamic acid; a Cochrane review judged the fennel evidence inconsistent. EU traditional use for minor menstrual spasm'),
        ('note', 'cough', 'EU traditional use as an expectorant in cough associated with a cold'),
    ],
    'gentiana_lutea': [
        ('note', 'indigestion', 'Bitter digestive aid for mild dyspeptic complaints such as indigestion and fullness (EU traditional use)'),
        ('note', 'bloating', 'inferred from digestive action'),
    ],
    'filipendula_ulmaria': [
        ('note', 'arthritis', 'EU traditional use for minor joint (articular) pain'),
        ('note', 'pain', 'EU traditional use for minor joint (articular) pain'),
    ],
    'elymus_repens': [
        ('note', 'swelling', 'inferred from diuretic action'),
    ],
    'epilobium_parviflorum': [
        ('note', 'prostate-support', 'EU traditional use for lower urinary tract symptoms of benign prostatic hyperplasia, once serious conditions are excluded by a doctor; a review judged the clinical evidence not yet conclusive'),
        ('note', 'urinary-support', 'EU traditional use for lower urinary tract symptoms related to benign prostatic hyperplasia'),
    ],
}
NOTES = {k: 'indication notes rewritten so they describe only the sources still cited (batch 6-7 follow-up).' for k in PLAN}

if __name__ == '__main__':
    fixlib.main(PLAN, NOTES, 'batch 7 notes', os.path.join(os.path.dirname(__file__), 'batch07_notes_changes.tsv'))
