"""Research-deepening batch 31 (schisandra-chinensis, scrophularia-nodosa, scutellaria-lateriflora, serenoa-repens,
silybum-marianum). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5655.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 31'

SPEC = [
    # milk thistle
    ('REF-5655', '38671838', 'silymarincardiovascularma', 'meta-analysis'),
    ('REF-5656', '30834633', 'silymarinlipidsma', 'meta-analysis'),
    # schisandra
    ('REF-5657', '19280523', 'schisandratalinolol', 'clinical'),
    # saw palmetto
    ('REF-5658', '42812739', 'sawpalmettodili', 'clinical'),
    ('REF-5659', '42480876', 'sawpalmettofaers', 'clinical'),
    ('REF-5660', '41507085', 'postserenoasyndrome', 'clinical'),
    ('REF-5661', '37463655', 'serenoapharmacovigilance', 'clinical'),
    ('REF-5662', '37426613', 'sawpalmettohematoma', 'clinical'),
    ('REF-5663', '21867545', 'sawpalmettopancreatitis', 'clinical'),
    ('REF-5664', '22768426', 'sawpalmettorhabdomyolysis', 'clinical'),
    ('REF-5665', '26043832', 'serenoachildendocrine', 'clinical'),
    ('REF-5666', '14663456', 'sawpalmettocyp', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== schisandra
PLAN['schisandra_chinensis'] = []
POST['schisandra_chinensis'] = [
    ('ciadd', 'inhibition of CYP3A and P-glycoprotein is documented', ['REF-5657']),
]
NOTES['schisandra_chinensis'] = (
    'Searched PubMed (Schisandra chinensis / Schizandra chinensis / Wu wei zi / Fructus Schisandrae tiab, "Schisandra" '
    'in titles; Schisandra sphenanthera is a different species: 52 HT, 19 SR, 335 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (27) and OpenAlex. Cognitive-function, fatigue and stress (7) were not padded. Added: 2009 human '
    'talinolol study (schisandra raised talinolol exposure by 47%, P-glycoprotein inhibition) to the drug-interaction '
    'info note. Not added: 2015 obese-women RCT (no between-group differences; microbiota only; there is no metabolic '
    'pair), ADAPT-232, Saengmaeksan, Shengmai, ImmunoGuard, schisandra + sesamin, ginseng-schisandra decoction and other '
    'Chinese formulas (combinations), Chinese patent-medicine insomnia network meta-analyses (formulas), preclinical '
    'liver and muscle meta-analyses.')

# ================================================================== figwort
PLAN['scrophularia_nodosa'] = []
NOTES['scrophularia_nodosa'] = (
    'Searched PubMed (Scrophularia nodosa / common or woodland figwort tiab, "figwort" in titles; Ningpo figwort, S. '
    'ningpoensis, and S. striata are different species: 0 HT, 0 SR, 0 SAFE hits), Europe PMC, ClinicalTrials.gov (0) '
    'and OpenAlex (Scrophularia striata oral-ulcer preprint, homeopathy and unrelated items). No human study of '
    'Scrophularia nodosa was found. Settled.')

# ================================================================== American skullcap
PLAN['scutellaria_lateriflora'] = []
NOTES['scutellaria_lateriflora'] = (
    'Searched PubMed (Scutellaria lateriflora / American, blue or mad-dog skullcap tiab; bare "skullcap" was not searched '
    'because it usually means Chinese skullcap, S. baicalensis: 4 HT (all already held), 2 SR, 8 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (2, a homeopathic complex and a migraine blend) and OpenAlex. Nothing new: general reviews of '
    'herbs for anxiety, germander-adulteration detection methods (the adulteration caution already exists), baicalin and '
    'baicalein pharmacokinetics (Chinese skullcap compounds). Settled.')

# ================================================================== saw palmetto
PLAN['serenoa_repens'] = []
POST['serenoa_repens'] = [
    ('cinew', {'note': 'Liver: a 70-year-old man developed biopsy-confirmed cholestatic drug-induced liver injury after about '
                       'four months of saw palmetto, which improved after stopping it (case report), and FDA adverse-event '
                       'reports show a disproportionate number of liver and bile-duct problems with saw palmetto '
                       '(pharmacovigilance study).',
               'severity': 'caution', 'reference_ids': ['REF-5658', 'REF-5659']}),
    ('cinew', {'note': 'Sexual and mental health: an Italian case series described persistent sexual, psychiatric and '
                       'physical symptoms after saw palmetto, resembling post-finasteride syndrome, lasting years in most '
                       'people; causality was rated probable in 54% (case series).',
               'severity': 'caution', 'reference_ids': ['REF-5660']}),
    ('cinew', {'note': 'Rare serious reactions: acute pancreatitis (case report, possibly due to saw palmetto) and '
                       'rhabdomyolysis with kidney failure in an 82-year-old taking several health foods, in whom a '
                       'lymphocyte test pointed to saw palmetto (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5663', 'REF-5664']}),
    ('cinew', {'note': 'Children: a 10-year-old girl taking a saw palmetto supplement for excess hair developed hot flushes '
                       'that stopped when it was stopped and returned on re-challenge, and reached menarche about 4 months '
                       'later; the authors suggest hormonal effects (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5665']}),
    ('cinew', {'note': 'Reporting data: in 1,810 worldwide reports of suspected reactions to saw palmetto products, 44% were '
                       'serious; serious reactions were more likely with dietary supplements, with several products taken '
                       'together and with use for more than 14 days (pharmacovigilance study).',
               'severity': 'info', 'reference_ids': ['REF-5661']}),
    ('cinew', {'note': 'Liver enzymes: in 12 healthy volunteers, saw palmetto 320 mg daily for 14 days did not change the '
                       'activity of the drug-metabolising enzymes CYP2D6 or CYP3A4 (pharmacokinetic study).',
               'severity': 'info', 'reference_ids': ['REF-5666']}),
    ('ciadd', 'use caution with anticoagulant medicines and before surgery', ['REF-5662', 'REF-5659']),
    ('dciadd', 'anticoagulants-antiplatelets', ['REF-5659', 'REF-5662']),
]
NOTES['serenoa_repens'] = (
    'Searched PubMed (Serenoa repens / saw palmetto / Sabal serrulata / Permixon / lipidosterolic extract tiab: 257 HT '
    '(listing capped at 200), 52 SR, 222 SAFE hits), Europe PMC, ClinicalTrials.gov (7) and OpenAlex. Prostate-support '
    '(9) and urinary-support (10) were not changed: the record already cites the null 2023 Cochrane review and large US '
    'trials as no-effect studies (owner flag: the computed score does not fall when null results are recorded). Added: '
    'liver (2026 DILI case + 2027 FAERS analysis), post-Serenoa syndrome, rare pancreatitis/rhabdomyolysis and paediatric '
    'endocrine cautions; worldwide pharmacovigilance info note; 2003 CYP2D6/CYP3A4 volunteer study (no change; found via '
    'Europe PMC) as an info note; the 2020 post-surgical haematoma case and FAERS '
    'haemorrhage-with-aspirin signal to the bleeding caution and the approved anticoagulants interaction. Not added: '
    'chronic prostatitis/CPPS meta-analysis letter, hair-loss network meta-analysis (no vocabulary condition), male '
    'infertility review (combination with selenium and lycopene), fixed drug eruption letter, supplement-psychosis case '
    '(multi-ingredient), older Cochrane versions (superseded by 2023).')

# ================================================================== milk thistle
PLAN['silybum_marianum'] = [
    ('newpair', 'high-cholesterol', ['REF-5655', 'REF-5656'],
     'In a 2024 dose-response meta-analysis of 33 controlled trials (1,943 people), silymarin from milk thistle lowered '
     'total cholesterol, LDL cholesterol and triglycerides; an earlier 2019 meta-analysis found the cholesterol fall '
     'mainly when silymarin was combined with other treatments (compound evidence)'),
]
NOTES['silybum_marianum'] = (
    'Searched PubMed (Silybum marianum / milk thistle / Legalon tiab, "silymarin", "silibinin" and "silybin" in titles '
    '(compound evidence): 434 HT (listing capped at 200), 79 SR, 1272 SAFE hits), Europe PMC, ClinicalTrials.gov (135) '
    'and OpenAlex; lactation RCTs were also searched directly. Liver-support (9) and blood-sugar (8) were not padded '
    '(2025-2026 cirrhosis, MASLD and insulin-resistance meta-analyses). Added: NEW high-cholesterol pair (2024 dose-'
    'response meta-analysis of 33 trials; 2019 lipid meta-analysis alongside). GAPS: kidney-support - a 2025 meta-'
    'analysis of 7 trials found lower serum creatinine, mostly in drug-induced acute kidney injury, with 93% '
    'heterogeneity (creatinine only), so no pair; lactation-support - a 2008 placebo-controlled study of micronized '
    'silymarin (BIO-C) reported more milk but does not state randomization, a 2015 double-blind RCT in mothers of preterm '
    'infants did not show a clear benefit, and a 2016 trial combined silymarin with galega, so no pair; high blood '
    'pressure - diastolic pressure fell by only 1.25 mmHg in the 2024 meta-analysis. Not added: silymarin OCD and '
    'depression trials and reviews (no OCD condition; depression review mostly preclinical), network meta-analyses '
    'pooling curcumin, resveratrol and berberine, radioprotection and cardiotoxicity reviews (mostly preclinical).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r31_changes.tsv')
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
