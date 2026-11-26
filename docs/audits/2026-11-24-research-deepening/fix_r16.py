"""Research-deepening batch 16 (hamamelis-virginiana, harpagophytum-procumbens, hedera-helix, hericium-erinaceus,
hibiscus-sabdariffa). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5391.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 16'

SPEC = [
    # devil's claw
    ('REF-5391', '18236448', 'harpagophytumsafety', 'systematic-review'),
    ('REF-5392', '24600731', 'devilsclawgibleeding', 'narrative-review'),
    ('REF-5393', '28355406', 'devilsclawsiadh', 'clinical'),
    ('REF-5394', '10920504', 'anticoagulantsmedicinalplants', 'narrative-review'),
    # ivy
    ('REF-5395', '31832428', 'ivyea575bronchitis', 'rct'),
    ('REF-5396', '24007931', 'ivysyrupanaphylaxis', 'clinical'),
    ('REF-5397', '20236156', 'ivyfalcarinoldermatitis', 'clinical'),
    # lion's mane
    ('REF-5398', '36582308', 'hericiumcognitionnull', 'clinical'),
    ('REF-5399', '14714963', 'hericiumards', 'clinical'),
    # hibiscus
    ('REF-5400', '42367450', 'hibiscuswarfarin', 'clinical'),
    ('REF-5401', '28925046', 'hibiscussimvastatin', 'clinical'),
    ('REF-5402', '15151167', 'hibiscusacetaminophen', 'clinical'),
    ('REF-5403', '24549255', 'hibiscusliversteatosis', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== devil's claw
PLAN['harpagophytum_procumbens'] = []
POST['harpagophytum_procumbens'] = [
    ('ciadd', 'Because it is a bitter that increases stomach-acid', ['REF-5392']),
    ('ciadd', 'May add to the effect of anticoagulants', ['REF-5394']),
    ('cinew', {'note': 'Side effects: in a 2008 systematic review of 28 clinical trials, minor side effects, mainly digestive, '
                       'occurred in about 3% of patients, and no double-blind trial found more side effects than with placebo.',
               'severity': 'info', 'reference_ids': ['REF-5391']}),
    ('cinew', {'note': 'Low blood sodium: a woman taking devil\'s claw for osteoarthritis twice developed low blood sodium caused '
                       'by inappropriate antidiuretic hormone secretion (SIADH), the second time after restarting it (case '
                       'report).',
               'severity': 'caution', 'reference_ids': ['REF-5393']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'insufficient',
                'mechanism': 'Reviews list devil\'s claw among herbs that may strengthen the effect of warfarin; the warning rests '
                             'on case reports, and no clinical study has measured the interaction (reviews).',
                'reference_ids': ['REF-0443', 'REF-5394']}),
]
NOTES['harpagophytum_procumbens'] = (
    'Searched PubMed (Harpagophytum procumbens / devil\'s claw / Harpagophytum tiab, harpagoside ti: 40 HT, 16 SR, 74 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (8) and OpenAlex. Arthritis, back pain and pain (8) are already SR/MA-backed and '
    'were not padded (Teltonal vs active drug 2021, Loxacon and other combinations, observational studies logged here). '
    'Added: 2008 safety SR (adverse events no higher than placebo) as an info note; the 2013 Prescrire review of '
    'gastrointestinal bleeding cases to the ulcer caution; a 2017 SIADH case (positive rechallenge) as a caution; a 2000 '
    'review to the anticoagulant caution and a DRAFT anticoagulant interaction (severity insufficient; needs owner '
    'sign-off) - the caution already warned about warfarin but the herb-drug checker had no entry. Not added: a 2015 '
    'hypertension case report (no abstract), a bezoar from an unnamed herbal preparation, the 2016 Spine republication of '
    'the Cochrane low back pain review (the 2014 Cochrane update is already cited as REF-1261; the 2006 and 2007 versions '
    'are superseded).')

# ================================================================== ivy
PLAN['hedera_helix'] = [
    ('add', 'cough', ['REF-5395']),
    ('note', 'cough', 'Ivy leaf extract EA 575 eased acute cough more than placebo in two randomized trials (2016 and 2019), and '
     'ivy extracts helped productive cough in other clinical studies, though an updated systematic review of all ivy products '
     'found the effects minimal at best'),
    ('add', 'bronchitis', ['REF-5395']),
    ('note', 'bronchitis', 'Ivy leaf extract eased productive cough and acute bronchitis in trials, including two placebo-'
     'controlled randomized trials of EA 575 (2016 and 2019); an updated systematic review found the effects minimal at best'),
]
POST['hedera_helix'] = [
    ('ciadd', 'Generally well tolerated; occasional gastrointestinal upset', ['REF-5396', 'REF-5397']),
]
NOTES['hedera_helix'] = (
    'Searched PubMed (Hedera helix / ivy leaf / English ivy / ivy extract tiab, Prospan / EA 575 ti: 56 HT, 11 SR, 96 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (6) and OpenAlex. Added: 2019 EA 575 placebo RCT in acute bronchitis to cough and '
    'bronchitis. The 2022 IPD meta-analysis (PMID 36414647) pools exactly this trial and REF-0575 (2016), so it was NOT '
    'added (it would count the same two trials twice). Also added: a 2012 report of two anaphylaxis cases '
    'after ivy syrup and the 2010 falcarinol patch-test series and review to the allergy note. Not added: ivy + thyme, ivy + '
    'primula, ivy + coptis (AG NPP709) and other combinations, two-arm ivy-vs-ivy trials, post-marketing and observational '
    'studies, antibiotic-use cohorts, a 2017 in vitro CYP2C8/2C19 inhibition study (preclinical), plant contact dermatitis '
    'case reports beyond the review.')

# ================================================================== lion's mane
PLAN['hericium_erinaceus'] = [
    ('nulladd', 'cognitive-function', ['REF-5398']),
]
POST['hericium_erinaceus'] = [
    ('cinew', {'note': 'Lungs: a man developed acute respiratory distress syndrome, an immune-type lung reaction, after taking a '
                       'lion\'s mane extract diet product; he recovered with steroid treatment (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5399']}),
]
NOTES['hericium_erinaceus'] = (
    'Searched PubMed (Hericium erinaceus / lion\'s mane / yamabushitake tiab: 23 HT, 11 SR, 53 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (15) and OpenAlex. Added: 2022 single-blind placebo study (10 g a day for 4 weeks, no effect on '
    'cognition) as no-effect for cognitive-function; a 2003 acute respiratory distress syndrome case as a lung caution. Not '
    'added: 2019 mood and sleep study in overweight adults (no control group), 2010 depression and anxiety RCT (already '
    'judged: within-group change only), guayusa and lion\'s mane acute cognition study (two products), a liver-injury case '
    'attributed to Agaricus blazei in a mixed mushroom powder, a 1985 atrophic gastritis study (no abstract), toxicology '
    'in rodents.')

# ================================================================== hibiscus
PLAN['hibiscus_sabdariffa'] = [
    ('newpair', 'liver-support', ['REF-5403'],
     'A hibiscus extract reduced body weight and body fat and improved fatty liver (steatosis) compared with a control group in '
     'a small randomized trial in obese adults'),
]
POST['hibiscus_sabdariffa'] = [
    ('ciadd', 'May alter the absorption or levels of some medicines', ['REF-5402']),
    ('dcinew', {'drug_class': 'statins', 'severity': 'caution',
                'mechanism': 'In healthy volunteers, hibiscus tea taken with simvastatin cut the amount of simvastatin reaching '
                             'the blood by about a third (randomized crossover study), so it may weaken the drug; the authors '
                             'advise against combining them.',
                'reference_ids': ['REF-5401']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'A woman on long-term warfarin developed a markedly raised INR after starting hibiscus tea, with no '
                             'other cause found; it normalised after stopping the tea and giving vitamin K (case report).',
                'reference_ids': ['REF-5400']}),
]
NOTES['hibiscus_sabdariffa'] = (
    'Searched PubMed (Hibiscus sabdariffa / roselle / sour tea / hibiscus tea / karkade tiab: 104 HT, 26 SR, 151 SAFE hits), '
    'Europe PMC, ClinicalTrials.gov (43) and OpenAlex. Blood pressure (10), blood sugar, cardiovascular, cholesterol (9) and '
    'metabolic support (8) were not padded. Added: NEW liver-support pair (2014 randomized trial vs control in obese adults, '
    'steatosis improved); the 2004 zobo-drink acetaminophen study (faster elimination) to the medicines caution; two DRAFT '
    'interactions (needs owner sign-off): statins (2017 human crossover, simvastatin AUC ratio 0.65) and anticoagulants '
    '(2026 warfarin INR case). Not added: hibiscus + valsartan vs valsartan + hydrochlorothiazide in CKD (active '
    'comparator), Lippia + hibiscus appetite trials, Aqualief and L-methionine combinations, iron-status trials (no vocab '
    'condition), an amlodipine interaction study (rats), an erlotinib skin-toxicity letter (no abstract), an IVF thrombosis '
    'case (speculative), the 2023 memory MA (preclinical).')

# ================================================================== witch hazel
PLAN['hamamelis_virginiana'] = []
NOTES['hamamelis_virginiana'] = (
    'Searched PubMed (Hamamelis virginiana / witch hazel / hamamelis tiab: 24 HT, 5 SR, 35 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (3) and OpenAlex. Dead end: a 1995 double-blind randomized trial in atopic eczema found hamamelis '
    'distillate cream no better than its vehicle (hydrocortisone superior; no eczema pair exists). Not added: a 1993 '
    'experimental UV-erythema study (overlaps the cited UVB study REF-3575), cosmetic and multi-ingredient skin products, '
    'a children\'s observational study (uncontrolled), HEC ointment anaphylaxis (phenazone-tannin-witch hazel '
    'combination), contact allergy letters (no abstract), ingestion of alcohol-based witch hazel toner.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r16_changes.tsv')
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
