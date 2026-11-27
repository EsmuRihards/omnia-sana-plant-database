"""Research-deepening batch 27 (prunus-africana, prunus-serotina, psilocybe-cubensis, pulmonaria-officinalis,
reynoutria-japonica). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5612.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 27'

SPEC = [
    # pygeum
    ('REF-5612', '12164269', 'pygeumrattoxicity', 'preclinical'),
    ('REF-5613', '30691591', 'pygeumrattargetorgans', 'preclinical'),
    # Japanese knotweed
    ('REF-5614', '41630279', 'huzhangliverinjury', 'clinical'),
    ('REF-5615', '41304883', 'knotweedmethotrexate', 'preclinical'),
    # psilocybin mushroom
    ('REF-5616', '32899469', 'psilocybinanxietyma', 'meta-analysis'),
    ('REF-5617', '30627509', 'psilocybecubensisaki', 'clinical'),
    ('REF-5618', '42538465', 'psilocybincardiovascular', 'narrative-review'),
    ('REF-5619', '37288212', 'psilocybincardiacarrest', 'clinical'),
    ('REF-5620', '34348413', 'psychedeliclithiumseizures', 'clinical'),
    ('REF-5621', '37810598', 'psilocybinmania', 'clinical'),
    ('REF-5622', '39420616', 'psilocybinpsychosis', 'clinical'),
    ('REF-5623', '42093782', 'psilocybincatatonia', 'clinical'),
    ('REF-5624', '37523886', 'psilocybinworseningipd', 'meta-analysis'),
    ('REF-5625', '42616497', 'oregonpsilocybinservices', 'clinical'),
    ('REF-5626', '37291890', 'psilocybinssriattenuation', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== pygeum
PLAN['prunus_africana'] = []
POST['prunus_africana'] = [
    ('cinew', {'note': 'Lab safety: in rats, a bark extract caused no harm at up to 1,000 mg/kg daily for 8 weeks, with liver, '
                       'kidney and heart damage only at 3.3 g/kg; another month-long rat study at 50-100 mg/kg raised '
                       'creatinine and LDH and named the kidney, skeletal muscle and heart as possible targets (animal '
                       'studies).',
               'severity': 'info', 'reference_ids': ['REF-5612', 'REF-5613']}),
]
NOTES['prunus_africana'] = (
    'Searched PubMed (Prunus africana / Pygeum africanum / pygeum / African cherry / Tadenan tiab: 48 HT, 12 SR, 42 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (4) and OpenAlex. Prostate-support and urinary-support (9) were not padded: '
    'the 2000 Am J Med meta-analysis and the older French and Italian placebo RCTs are the trials the held Cochrane review '
    'pools. Added: two rat toxicity studies as an info note. Not added: Pygeum + Urtica, Pygeum + benzydamine, '
    'L-cystine + saw palmetto + pumpkin seed + pygeum hair-loss trial, Prostaquil (combinations), 1991 high-dose sexual-'
    'function series (18 patients, no control group), open Tadenan studies, the 2000 occupational asthma case from '
    '"African cherry" (Makore) wood dust (Tieghemella heckelii, a different tree), East African cancer reviews.')

# ================================================================== wild cherry
PLAN['prunus_serotina'] = []
NOTES['prunus_serotina'] = (
    'Searched PubMed (Prunus serotina / wild black cherry / wild cherry bark / black cherry bark tiab; "black cherry" in '
    'titles only: 1 HT, 0 SR, 9 SAFE hits, mostly ecology or veterinary), Europe PMC, ClinicalTrials.gov (17; none '
    'tested wild cherry bark - tart cherry, aronia, fruit juices and unrelated products) and OpenAlex. Not added: goat poisoning cases (veterinary; the cyanogenic caution '
    'already covers this), 2019 acute kidney injury case from a "black cherry concentrate" taken for gout (fruit '
    'concentrate, species not stated; this record is the bark), tart cherry (Prunus cerasus) trials. Settled.')

# ================================================================== psilocybin mushroom
PLAN['psilocybe_cubensis'] = [
    ('add', 'anxiety', ['REF-5616']),
    ('note', 'anxiety',
     'Psilocybin reduced anxiety in people with life-threatening cancer in a randomized trial, and a 2020 meta-analysis of '
     'clinical trials in life-threatening illness found lower anxiety scores with psilocybin than with control (compound '
     'evidence; purified psilocybin in supervised settings); mushroom extracts reduced anxiety-like behaviour in rodents '
     '(preclinical)'),
]
POST['psilocybe_cubensis'] = [
    ('ciadd', 'Avoid mixing with lithium (seizure risk)', ['REF-5620']),
    ('ciadd', 'triggering of latent psychiatric conditions', ['REF-5621', 'REF-5622']),
    ('cinew', {'note': 'Kidneys: a 15-year-old developed acute kidney injury 36 hours after eating Psilocybe cubensis '
                       'mushrooms confirmed to contain psilocin; kidney function recovered fully (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5617']}),
    ('cinew', {'note': 'Heart and blood pressure: in supervised studies psilocybin raised blood pressure by about 19/9 mmHg '
                       'on average, peaking 1 to 1.5 hours after dosing and settling within 4 to 6 hours; serious heart '
                       'events were uncommon in screened participants, but risk depends on heart disease and interacting '
                       'medicines. A man taking the stimulant lisdexamfetamine had ventricular fibrillation after using '
                       'psilocybin mushrooms (narrative review; case report).',
               'severity': 'caution', 'reference_ids': ['REF-5618', 'REF-5619']}),
    ('cinew', {'note': 'Mental health: a man with no psychiatric history developed catatonia, with six months of mutism and '
                       'inability to feed himself, after taking psilocybin for the first time (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5623']}),
    ('cinew', {'note': 'Supervised and regulated use: in a pooled analysis of three depression trials, clinically significant '
                       'worsening occurred in about 10% of people given psilocybin, similar to escitalopram and less than '
                       'on a waitlist. In 346 clients of Oregon\'s state-regulated psilocybin services, 4 (1.2%, all '
                       'first-time users) had behavioural reactions needing medical attention, and about 2% described the '
                       'experience as harmful (meta-analysis; cohort study).',
               'severity': 'info', 'reference_ids': ['REF-5624', 'REF-5625']}),
    ('dcinew', {'drug_class': 'antidepressants-serotonergic', 'severity': 'caution',
                'mechanism': 'In 611 online reports of taking psilocybin mushrooms with an antidepressant, the effects were '
                             'weaker than expected in about half of reports with SSRIs or SNRIs, and the weakening was '
                             'also reported after stopping the antidepressant (report analysis). Antidepressant changes '
                             'should be supervised by a prescriber.',
                'reference_ids': ['REF-5626']}),
]
NOTES['psilocybe_cubensis'] = (
    'Searched PubMed (Psilocybe cubensis / psilocybin or magic mushroom(s) tiab, plus "psilocybin" in titles: 445 HT '
    '(listing capped at 200, so headache trials were searched directly), 116 SR, 393 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (104) and OpenAlex. Depression (10) was not padded. Added: 2020 psilocybin meta-analysis in '
    'life-threatening illness to anxiety (was 5, resting on one RCT and rodent studies); 2021 analysis of online reports '
    '(seizures with lithium) and mania/psychosis case reports added to the existing caution; new cautions: acute kidney '
    'injury after confirmed P. cubensis, blood pressure/heart (2026 narrative review + VF case), catatonia after a first '
    'dose; info note on symptom worsening (2023 IPD meta-analysis) and Oregon regulated-service safety (2026 cohort); '
    'DRAFT antidepressants-serotonergic interaction (2023 analysis of 611 reports; needs owner approval). GAPS: migraine - '
    'a 2021 double-blind placebo crossover (10 people) found fewer migraine days after one dose, but randomization of the '
    'order is stated only in the trial registry (abstract silent, full text not open), and a 2026 randomized trial (18 '
    'people) missed its primary outcome, so no pair; cluster headache - the 2022 randomized trial was not significant and '
    'its extension compared within-group; alcohol use, smoking, OCD, anorexia, PTSD and bipolar depression (no '
    'vocabulary condition, or open-label pilots); chronic pain, fibromyalgia and phantom limb pain (open-label pilots and '
    'case reports). Not added: 2024 Cochrane review (pools psilocybin with LSD), 2020 Psychiatry Res meta-analysis '
    '(within-group effect sizes), takotsubo case after Psilocybe semilanceata (other species), letters without '
    'abstracts (Japanese serotonin-syndrome cases, prolonged mania case, JAMA Netw Open adverse outcomes), microdosing '
    'review (pools LSD).')

# ================================================================== lungwort
PLAN['pulmonaria_officinalis'] = []
NOTES['pulmonaria_officinalis'] = (
    'Searched PubMed (Pulmonaria officinalis / Pulmonariae herba / common lungwort tiab, "lungwort" in titles; tree '
    'lungwort, the lichen Lobaria pulmonaria, is a different organism: 1 HT, 0 SR, 3 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (0) and OpenAlex. Nothing new: a genome study, held genotoxicity and insulin-mimetic lab studies, '
    'and a 1992 anticoagulant study of Pulmonaria mollissima (other species). Settled.')

# ================================================================== Japanese knotweed
PLAN['reynoutria_japonica'] = []
POST['reynoutria_japonica'] = [
    ('cinew', {'note': 'Liver: a 72-year-old developed liver injury after 14 days of a herbal formula containing Japanese '
                       'knotweed root (Huzhang); causality was rated probable, and the authors point to its emodin content, '
                       'especially for older people and long-term users (case report and review).',
               'severity': 'caution', 'reference_ids': ['REF-5614']}),
    ('dcinew', {'drug_class': 'immunosuppressants', 'severity': 'insufficient',
                'mechanism': 'In rats, knotweed root at 1-2 g/kg changed blood levels of methotrexate (lower early '
                             'exposure, longer persistence at the higher dose) by acting on the BCRP drug transporter '
                             '(animal and lab study).',
                'reference_ids': ['REF-5615']}),
]
NOTES['reynoutria_japonica'] = (
    'Searched PubMed (Reynoutria japonica / Polygonum cuspidatum / Fallopia japonica / Japanese knotweed / Hu Zhang / '
    'Polygoni Cuspidati tiab; "resveratrol" alone was not searched because most resveratrol comes from other sources: 34 '
    'HT, 11 SR, 92 SAFE hits), Europe PMC, ClinicalTrials.gov (1) and OpenAlex. Added: 2026 RUCAM-assessed liver-injury '
    'case as a caution; 2025 rat methotrexate pharmacokinetic study as a DRAFT immunosuppressants interaction '
    '(insufficient; needs owner approval). Not added: Huzhang granule, Tongfeng and Huzhang Sanhuang formulas, knotweed + '
    'hawthorn for carotid plaque, aloe + grape + knotweed platelet supplement, pomegranate + knotweed + red clover TMAO '
    'trial (combinations); 2010 extract trial and 2013 basketball-player study (inflammatory markers only, surrogate); '
    '2021 Gulf War illness resveratrol crossover (pseudo-randomized; no vocabulary condition); polydatin alcoholism pilot '
    '(compound, surrogate); resveratrol-only trials and reviews (compound with many sources); a general review of TCM liver '
    'injury; lab and animal studies.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r27_changes.tsv')
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
