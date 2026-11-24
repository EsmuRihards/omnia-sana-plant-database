"""Research-deepening batch 5 (asclepias-tuberosa, astragalus-membranaceus, bacopa-monnieri, betula-pendula,
bistorta-officinalis). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5187.. (reserved block)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 5'

SPEC = [
    ('REF-5187', '41903404', 'milkweedkeratoconjunctivitis', 'clinical'),
    ('REF-5189', '41235391', 'astragaluskneepain', 'rct'),
    ('REF-5190', '27773802', 'astragaluspoststrokefatigue', 'rct'),
    ('REF-5191', '31034954', 'astragalusdiabetickidney', 'meta-analysis'),
    ('REF-5192', '42078932', 'astragaluswoundsanimal', 'meta-analysis'),
    ('REF-5193', '39692050', 'astragalusherbdrug', 'narrative-review'),
    ('REF-5194', '41678913', 'brahmiginkgonma', 'meta-analysis'),
    ('REF-5195', '18683852', 'bacopakeenmind90day', 'rct'),
    ('REF-5196', '23354535', 'brahmiforthebetter', 'rct'),
    ('REF-5197', '32236999', 'bacopaanhedonia', 'rct'),
    ('REF-5198', '40507208', 'bacopasafetyreview', 'narrative-review'),
    ('REF-5199', '37829299', 'adaptogensantidepressants', 'clinical'),
    ('REF-5200', '36689495', 'oleogels10ease', 'rct'),
    ('REF-5201', '28400148', 'betulingeldonorsites', 'rct'),
    ('REF-5202', '25034442', 'triterpenessurgicalwounds', 'rct'),
    ('REF-5203', '37658982', 'birchbarkextractreview', 'narrative-review'),
]
DOI_SPEC = [
    ('REF-5188', '10.1089/act.2006.12.214', 'eclecticsinfluenza', 'narrative-review', {}),
]
WEB = {'ema2026filsuvez': ('REF-5204', [
    ('author', 'European Medicines Agency'),
    ('title', 'Filsuvez (birch bark extract) gel: EPAR product information, Summary of Product Characteristics'),
    ('year', '2026'),
    ('url', 'https://www.ema.europa.eu/en/documents/product-information/filsuvez-epar-product-information_en.pdf'),
    ('note', 'REF-5204'), ('study_type', 'pharmacopoeial'),
    ('summary', 'EU product information, first authorised 21 June 2022, product information last updated 6 October 2026, PDF '
                'read 2026-11-24. Section 2: 1 g of gel contains 100 mg of refined dry extract of the bark (cortex) of Betula '
                'pendula Roth, Betula pubescens Ehrh. and their hybrids, with 84-95 mg triterpenes (betulin, betulinic acid, '
                'erythrodiol, lupeol, oleanolic acid); extraction solvent n-heptane. Section 4.1: treatment of partial thickness '
                'wounds associated with dystrophic and junctional epidermolysis bullosa in patients 6 months and older. Section '
                '4.3/4.4: contraindicated in hypersensitivity to the active substance; hypersensitivity reactions have occurred '
                '(stop immediately); wound infection is an important complication (interrupt treatment).')])}
RETAG = {'REF-0626': 'clinical'}  # Mikkelsen 2017, a case report of corneal toxicity, was tagged preclinical


def bib_new():
    new = deep_lib.newrefs(SPEC)
    for rid, doi, slug, st, over in DOI_SPEC:
        _, (r, fields) = rd_doi.newref_doi(doi, rid, 'x', st)
        f = dict(fields)
        au = [_initials(a.strip()) for a in rd_doi.fetch(doi)['authors']]
        f['author'] = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
        f.update(over)
        order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'pmid', 'note', 'study_type', 'abstract']
        new[_ascii(f['author'].split(',')[0]) + f['year'] + slug] = (rid, [(k, f[k]) for k in order if k in f])
    new.update(WEB)
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== pleurisy root
PLAN['asclepias_tuberosa'] = [
    ('add', 'cold', ['REF-5188']),
    ('note', 'cold', 'Used by Eclectic physicians to treat influenza during the 1918 pandemic (historical review); no clinical '
     'trials'),
]
POST['asclepias_tuberosa'] = [('ciadd', 'Contains cardiac glycosides', ['REF-5187'])]
AT_OLD = ("The plant's cardenolide-rich latex is directly toxic - a documented case caused corneal injury through Na/K-ATPase "
          "inhibition.")
AT_NEW = ("The plant's cardenolide-rich latex is directly toxic: two case reports describe corneal injury with blurred or lost "
          "vision after handling the plant, one in a contact-lens wearer after gardening.")
NOTES['asclepias_tuberosa'] = (
    'Searched PubMed ("Asclepias tuberosa" OR "pleurisy root" tiab, "butterfly weed" ti: 0 HT, 0 SR, 3 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (9, all about the disease pleurisy, none on the plant) and OpenAlex (85 no-PMID works, mostly '
    'horticulture and pollinator ecology). No human study of the plant exists. Added: 2026 toxic keratoconjunctivitis case '
    'after handling the plant (to the cardiac-glycoside caution, whose text now covers both case reports); Abascal & Yarnell '
    '2006 review of Eclectic botanicals used in the 1918 influenza pandemic, which names pleurisy root (to the cold pair, '
    'which no longer rests on inference alone; stays needs-review, historical evidence). REF-0626 (Mikkelsen 2017) retagged '
    'clinical: it is a case report, not a lab study. Not used: homoeopathic-journal remedy lists, a seed antidiabetic review '
    'in a low-quality journal.')

# ================================================================== astragalus
PLAN['astragalus_membranaceus'] = [
    ('add', 'arthritis', ['REF-5189']),
    ('note', 'arthritis', 'A standardized astragalus root extract reduced knee pain and improved WOMAC scores more than placebo '
     'over 28 days in a small double-blind randomized trial in adults with functional knee joint pain'),
    ('status', 'arthritis', 'verified'),
    ('add', 'fatigue', ['REF-5190']),
    ('note', 'fatigue', 'Reduced fatigue after stroke and in cancer patients in meta-analyses of trials (low-quality evidence), '
     'in a placebo-controlled trial after stroke and in a trial in nurses with post-COVID fatigue; an Astragalus polysaccharide '
     'infusion did not reduce chemotherapy fatigue overall'),
    ('newpair', 'kidney-support', ['REF-5191'],
     'Added to usual treatment, astragalus reduced protein in the urine and serum creatinine in people with diabetic kidney '
     'disease in a meta-analysis of 66 low-quality trials; most trials used an injection, but oral preparations also reduced '
     'albumin in the urine (4 trials)'),
]
POST['astragalus_membranaceus'] = [
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'A 2025 review reports that astragalus and its main compounds can alter drug-metabolising enzymes '
                             'and the P-glycoprotein drug pump (CYP2C9, CYP3A4, UGT1A6), so it may interact with drugs such as '
                             'midazolam, tolbutamide or digoxin; studies disagree on its effect on CYP3A4.',
                'reference_ids': ['REF-5193']}),
]
NOTES['astragalus_membranaceus'] = (
    'Searched PubMed (Astragalus membranaceus / A. mongholicus / Astragali radix / Huangqi / Radix Astragali tiab: 339 HT, 186 '
    'SR, 657 SAFE hits), Europe PMC, ClinicalTrials.gov (89) and OpenAlex. Most hits are multi-herb formulas, decoctions or '
    'Astragalus injection; injection trials are not used as support (a hospital drug route, not herbal use; same rule as '
    'the andrographolide injections in batch 3). Added: 2025 Indian placebo RCT of a root extract for knee joint pain '
    '(arthritis, was inferred-only; now verified); 2016 placebo RCT in post-stroke fatigue; NEW kidney-support pair from Zhang '
    '2019 MA in diabetic kidney disease (oral subgroup 4 RCTs, 236 people, less albuminuria; conclusion "may be effective", '
    'low-quality evidence); preclinical MA on wound healing (new vulnerary action); 2025 herb-drug review (new DRAFT CYP3A4 '
    'interaction, insufficient, needs owner sign-off). Considered, not added: Cochrane 2016 on preventing respiratory '
    'infections in children (no eligible trials - an empty review, not a null); open-label RCT and Chinese companion paper '
    'on diastolic function in hypertensive women with MetS (tiny echo changes, surrogate, no symptom outcome); HFrEF and AMI '
    'meta-analyses (preparation not stated, mostly injection); injection-only DN MA 2011; Astragalus polysaccharide cancer '
    'MAs (mostly injection); Lectranal hay-fever RCT (herbal-mineral complex); Myelophil, SHPro, AstraGin, Rubus + Astragalus '
    'and Huang Qi formula trials (combinations); stroke-recovery and SAH trials (no vocab condition).')

# ================================================================== bacopa
PLAN['bacopa_monnieri'] = [
    ('add', 'memory', ['REF-5194', 'REF-5195']),
    ('nulladd', 'memory', ['REF-5196']),
    ('note', 'memory', 'Improved memory recall and retention in randomized trials in healthy adults and older people (systematic '
     'review); a 2026 network meta-analysis found high doses improved working and short-term memory, though one 12-week trial '
     'in healthy adults found no effect'),
    ('add', 'cognitive-function', ['REF-5194']),
    ('nulladd', 'cognitive-function', ['REF-5196']),
    ('note', 'cognitive-function', 'Improved attention and processing speed in a meta-analysis of randomized trials, and '
     'cognitive performance in older adults in placebo-controlled trials; a 2026 network meta-analysis found gains in working '
     'memory but not in attention or processing speed, and one 12-week trial found no effect on any cognitive measure'),
    ('nulladd', 'anxiety', ['REF-5196']),
    ('note', 'anxiety', 'Anxiety scores fell in older adults taking Bacopa for 12 weeks (and rose on placebo) in a randomized '
     'trial; two other trials found no clear change in anxiety'),
    ('add', 'depression', ['REF-5197']),
    ('note', 'depression', 'Depression scores fell in older adults taking Bacopa for 12 weeks (and rose on placebo) in a '
     'randomized trial, and added to citalopram it improved depression and anhedonia scores more than citalopram alone in a '
     '4-week trial'),
]
POST['bacopa_monnieri'] = [
    ('cinew', {'note': 'Reviews advise care when taking it with some medicines and in hyperthyroidism (an overactive thyroid); '
                       'safety in pregnancy and breastfeeding has not been established.',
               'severity': 'caution', 'reference_ids': ['REF-5198']}),
    ('dcinew', {'drug_class': 'antidepressants-serotonergic', 'severity': 'caution',
                'mechanism': 'In a review of adverse-event reports, bacopa taken with antidepressants was linked to back pain '
                             'and heavy sweating (with agomelatine) and to a heart attack (with moclobemide); this rests on two '
                             'reports, with no controlled study.',
                'reference_ids': ['REF-5199']}),
]
NOTES['bacopa_monnieri'] = (
    'Searched PubMed (Bacopa monnieri / monniera / Herpestis monniera tiab; Bacopa, brahmi ti), Europe PMC, ClinicalTrials.gov '
    '(65) and OpenAlex. Added: 2026 Brahmi vs Ginkgo network MA (29 RCTs, healthy adults; high dose improved working and '
    'short-term memory vs placebo, no effect on attention or processing speed) to memory and cognitive-function; Stough 2008 '
    '90-day RCT to memory; Sathyanarayanan 2013 12-week RCT (no effect on any cognitive measure, only a non-significant '
    'anxiety trend) recorded as no-effect for memory, cognitive-function and anxiety; Micheli 2020 citalopram add-on trial in '
    'anhedonia to depression. Safety: 2025 review (care with some medicines, hyperthyroidism, pregnancy) as a new caution; '
    'pharmacovigilance chart review (agomelatine, moclobemide reports) as a new DRAFT serotonergic-antidepressant '
    'interaction, needs owner sign-off. Memory and cognitive-function stay needs-review (status not changed by this pass). '
    'Considered, not added: Brahmi vati, Brahmi ghrita, Medhya Rasayana and other Ayurvedic formulations; Bacopa + ginseng, '
    'Pycnogenol, micronutrient and multi-ingredient products; Bacopa vs donepezil (active comparator); 2025 older-adult '
    'plant NMA ("bacopa compound", a combination); dementia SR 2022 (very low quality, mixes combinations); ADHD, '
    'schizophrenia and Parkinson trials (no vocab condition); cevimeline toxicity case (supplement also had '
    'phosphatidylserine); necrotising myopathy letter (no abstract); in vitro CYP screen (negligible inhibition).')

# ================================================================== birch
PLAN['betula_pendula'] = [
    ('newpair', 'wounds', ['REF-5200', 'REF-5201', 'REF-5202', 'REF-5203', 'REF-5204'],
     'A licensed gel of birch bark extract (from silver and downy birch) closed epidermolysis bullosa wounds more often than a '
     'control gel in a double-blind randomized trial, and sped healing of skin-graft donor sites in randomized trials; the gel '
     'is approved in the EU for wounds in epidermolysis bullosa'),
]
POST['betula_pendula'] = [
    ('cinew', {'note': 'The licensed birch bark gel can cause allergic (hypersensitivity) reactions and must be stopped at once '
                       'if they occur; wound infection is a known complication of treatment (EU product information).',
               'severity': 'info', 'reference_ids': ['REF-5204']}),
]
NOTES['betula_pendula'] = (
    'Searched PubMed (Betula pendula / B. verrucosa / silver birch / Betulae folium tiab; birch leaf / leaves / sap ti), Europe '
    'PMC, ClinicalTrials.gov (8) and OpenAlex: nearly all hits are birch pollen allergy or forestry; no human trial of birch '
    'leaf. A second targeted PubMed search ("birch bark", Oleogel-S10, Filsuvez, Episalyl, birch triterpenes) found the bark '
    'extract trials. Species: the EMA Filsuvez SmPC (REF-5204, PDF read 2026-11-24) names the bark of Betula pendula, B. '
    'pubescens and their hybrids; the 2023 review (REF-5203) identifies Filsuvez with Oleogel-S10; Episalvan was the same '
    '10% extract in sunflower oil. NEW wounds pair: EASE phase III double-blind RCT (223 EB patients, 41.3% vs 28.9% target '
    'wound closure by day 45), two parallel phase III donor-site RCTs (219 patients, 1.1 days faster), phase II donor-site RCT '
    '(24 patients). Safety: SmPC hypersensitivity and wound-infection warnings as a new info note. Considered, not added: '
    'Brno single-centre report (a subset of the phase III donor-site trial), burns RCT vs Octenilin gel (active comparator '
    'only), EASE 24-month open extension and paediatric follow-up (no new contrast), actinic keratosis placebo RCT 2015 '
    '(no effect; no vocab condition), hepatitis C pilot, betulin lab and nanofibre papers, birch sap rat studies.')

# ================================================================== bistort
PLAN['bistorta_officinalis'] = []
NOTES['bistorta_officinalis'] = (
    'Searched PubMed (Bistorta officinalis / Polygonum bistorta / Persicaria bistorta / bistort tiab: 0 HT, 1 SR, 3 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (0) and OpenAlex (5). No human study exists; hits were a veterinary Polygonaceae '
    'review, Chinese multi-herb cancer mixtures (antitumor B, PV-1), a Bistortae Rhizoma authentication paper and a piglet '
    'tannin feed trial. Settled for now. Open item: the two tannin/medical-assessment info notes and the pregnancy caution '
    'carry no reference.')


def text_edits():
    path = 'plants/asclepias_tuberosa.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if AT_OLD in x['note']]; assert len(c) == 1
    assert '—' not in AT_NEW and '–' not in AT_NEW
    c[0]['note'] = c[0]['note'].replace(AT_OLD, AT_NEW)
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/astragalus_membranaceus.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    assert 'vulnerary' not in {a['action'] for a in d['actions']}
    d['actions'].append({'action': 'vulnerary', 'reference_ids': ['REF-5192'], 'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r05_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new(), retag=RETAG)
        bib = open('bibliography.bibtex', encoding='utf-8', newline='').read()
        for k in WEB:
            assert bib.count('@article{' + k + ',') == 1
            bib = bib.replace('@article{' + k + ',', '@misc{' + k + ',')
        open('bibliography.bibtex', 'w', encoding='utf-8', newline='').write(bib)
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        text_edits()
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
