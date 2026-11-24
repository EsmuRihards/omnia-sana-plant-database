"""Research-deepening batch 3 (althaea-officinalis, andrographis-paniculata, anethum-graveolens, angelica-archangelica,
arctium-lappa). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5132.. (reserved block)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 3'

SPEC = [
    ('REF-5132', '30064132', 'marshmallowcoughsurveys', 'clinical'),
    ('REF-5137', '26603219', 'hollyhockbreastengorgement', 'rct'),
    ('REF-5138', '38438482', 'marshmallowsyrupchromium', 'preclinical'),
    ('REF-5139', '10589439', 'andrographissha10cold', 'rct'),
    ('REF-5140', '42760788', 'bioimmuneandrographolideurti', 'rct'),
    ('REF-5141', '42735469', 'tcimcovidnma', 'meta-analysis'),
    ('REF-5142', '40822451', 'andrographiscovidsr', 'systematic-review'),
    ('REF-5143', '36570418', 'cimmeg19covid', 'rct'),
    ('REF-5144', '39005565', 'andrographiscovidplacebo', 'rct'),
    ('REF-5145', '37625206', 'andrographisfavipiravir', 'rct'),
    ('REF-5146', '36035418', 'andrographiscovidcohort', 'clinical'),
    ('REF-5147', '38612967', 'herbalucma2024', 'meta-analysis'),
    ('REF-5148', '35153776', 'andrographolideadrsr', 'systematic-review'),
    ('REF-5149', '36309577', 'andrographisaltthai', 'clinical'),
    ('REF-5150', '40169313', 'covidliverinjuryrealworld', 'clinical'),
    ('REF-5151', '28249303', 'andrographishealthythai', 'clinical'),
    ('REF-5152', '22605942', 'andrographisdiabetesopen', 'clinical'),
    ('REF-5153', '32380977', 'andrographolideprogressivems', 'rct'),
    ('REF-5154', '19408036', 'andrographisrheumatoid', 'rct'),
    ('REF-5155', '38264189', 'dilloilpruritus', 'rct'),
    ('REF-5156', '33130423', 'dillseedlaboursr', 'systematic-review'),
    ('REF-5157', '25453516', 'boileddilllabour', 'rct'),
    ('REF-5158', '23351341', 'dillmetabolicsyndrome', 'rct'),
    ('REF-5159', '10831013', 'dillanaphylaxis', 'clinical'),
    ('REF-5160', '40329862', 'dillthyroid', 'rct'),
    ('REF-5161', '39410893', 'dillpostpartumhaemorrhage', 'rct'),
    ('REF-5167', '36636365', 'detoxteadili', 'clinical'),
    ('REF-5168', '31043657', 'burdockdiverticulitis', 'rct'),
]
DOI_SPEC = [
    ('REF-5133', '10.1055/s-0043-1774010', 'marshmallowcoughreview', 'narrative-review', {'journal': 'Planta Medica'}),
    ('REF-5134', '10.4103/nms.nms_42_18', 'althaeastomatitis', 'rct', {}),
    ('REF-5135', '10.32598/jccnc.4.1.37', 'althaeastomatitispain', 'rct', {}),
    ('REF-5136', '10.1186/s40816-021-00306-z', 'althaeaatopiceczema', 'rct', {}),
]
NOABS = [  # case reports with no abstract: title states the event; summary says so; used only where MSKCC agrees
    ('REF-5163', '12786879', 'burdockanaphylaxis', 'Case report (no abstract): anaphylaxis after eating burdock; title-level citation, corroborated by MSKCC.'),
    ('REF-5164', '8549139', 'burdockcontactdermatitis', 'Case report (no abstract): allergic contact dermatitis due to burdock; title-level citation, corroborated by MSKCC.'),
    ('REF-5165', '691140', 'burdockteapoisoning', 'Letter (no abstract): burdock root tea poisoning; title-level citation, corroborated by MSKCC (atropine contamination).'),
    ('REF-5166', '6535850', 'burdockanticholinergic', 'Case reports (no abstract): anticholinergic poisonings associated with commercial burdock root tea; corroborated by MSKCC.'),
]
WEB = {'mskcc2025burdock': ('REF-5162', [
    ('author', 'Memorial Sloan Kettering Cancer Center'), ('title', 'Burdock (About Herbs)'), ('year', '2025'),
    ('url', 'https://www.mskcc.org/cancer-care/integrative-medicine/herbs/burdock'), ('note', 'REF-5162'), ('study_type', 'traditional'),
    ('summary', 'MSKCC About Herbs, last updated 23 May 2025, read 2026-11-24. Some burdock teas have been contaminated with atropine '
                'from belladonna, causing nervous-system effects; reported adverse reactions: allergic contact dermatitis, anaphylaxis '
                '(53-year-old man after boiled burdock), acute liver injury (36-year-old woman after a liver detox tea containing '
                'burdock); do not take if allergic to chrysanthemums (cross-sensitivity) or pregnant (may stimulate the uterus); '
                'animal studies show the root extract lowers blood sugar; no evidence supports use for cancer, infections or diabetes.')])}


def _noabs(pmid, rid, slug, summary):
    x = deep_lib.CACHE[pmid]
    au = x['authors']
    author = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
    f = [('author', author), ('title', deep_lib._clean(x['title']).rstrip('.')), ('journal', deep_lib._journal(x['journal'])),
         ('year', x['year'])] + [(k, x[k]) for k in ('volume', 'number', 'pages') if x.get(k)]
    if x.get('doi'):
        f.append(('doi', x['doi']))
    f += [('pmid', pmid), ('note', rid), ('study_type', 'clinical'), ('summary', summary)]
    return deep_lib.autokey(pmid, slug), (rid, f)


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
    for rid, pmid, slug, summ in NOABS:
        k, v = _noabs(pmid, rid, slug, summ); new[k] = v
    new.update(WEB)
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== marshmallow
PLAN['althaea_officinalis'] = [
    ('add', 'cough', ['REF-5132', 'REF-5133']),
    ('note', 'cough', 'Demulcent antitussive for dry, irritating cough (EU herbal monograph; ESCOP); most users of an aqueous '
     'marshmallow root extract reported rapid relief of dry cough in two pharmacy surveys, supported by a 2023 review; in animal '
     'studies the root rhamnogalacturonan suppresses the cough reflex'),
    ('newpair', 'oral-health', ['REF-5134'],
     'A mouthwash containing marshmallow root extract improved chemotherapy-induced mouth sores (stomatitis) more than the '
     'routine mouthwash in a double-blind randomized trial'),
    ('add', 'eczema', ['REF-5136']),
    ('note', 'eczema', 'A 1% marshmallow ointment reduced atopic dermatitis severity more than 1% hydrocortisone in a small '
     'double-blind trial in children; in adults, a liposomal marshmallow flower extract matched a topical steroid after 4 weeks '
     'in a double-blind trial'),
    ('refadd', ['REF-5135', 'REF-5137', 'REF-5138']),
]
NOTES['althaea_officinalis'] = (
    'Searched PubMed (Althaea officinalis / marshmallow root / marsh mallow / Althaeae radix tiab), Europe PMC, ClinicalTrials.gov '
    '(2: an infant reflux alginate and an Ectoin + althaea honey spray - both combinations) and OpenAlex (found the Iranian '
    'trials). NEW pair oral-health: Kashan double-blind RCT 2016 (stomatitis severity, Nurs Midwifery Stud 2019, REF-5134); its '
    'companion paper on the same 50 patients (pain, J Client-Centered Nurs Care 2018, REF-5135) is bucketed, not counted twice. '
    'Cough: STW42 pharmacy surveys (822 users) and Kelber 2023 Planta Med review (congress abstract, so narrative-review). The '
    'ACE-inhibitor cough placebo RCT (Rouhi 2007, Pakistan J Nutr, doi 10.3923/pjn.2007.256.258) is cited only through that '
    'review: its publisher (ANSI) is on Beall\'s list of potentially predatory publishers. Eczema: liposomal flower-extract '
    'split-body RCT vs steroid (Clin Phytoscience 2021). Bucket: hollyhock (Althaea officinalis) leaf compress add-on RCT for '
    'breast engorgement (not a lactation-support claim), chromium-impurity risk assessment of Polish syrups (all far below '
    'limits). Not added: BNO 1030, Pedicough mouthwash, saliva substitutes and other combinations; animal/horse "marsh mallow" '
    'toxicosis (that is Malva parviflora).')

# ================================================================== andrographis
PLAN['andrographis_paniculata'] = [
    ('add', 'cold', ['REF-5139', 'REF-5140']),
    ('add', 'sore-throat', ['REF-5139']),
    ('add', 'infection', ['REF-5141', 'REF-5142', 'REF-5143']),
    ('nulladd', 'infection', ['REF-5144', 'REF-5145', 'REF-5146']),
    ('note', 'infection', 'Symptomatic relief of the common cold and acute upper respiratory infections (systematic reviews); in '
     'COVID-19, a network meta-analysis found andrographis extract probably reduced progression to severe disease and a pilot '
     'add-on trial was positive, but two placebo-controlled trials and a cohort study found no clear benefit'),
    ('nulladd', 'ibd', ['REF-5147']),
    ('note', 'ibd', 'An Andrographis extract (HMPL-004) gave more clinical responses than placebo in mild-to-moderate ulcerative '
     'colitis and was comparable to mesalazine in a second trial, but a 2024 meta-analysis of the placebo-controlled trials found '
     'no significant benefit for response or remission'),
    ('refadd', ['REF-5153', 'REF-5154']),
]
POST['andrographis_paniculata'] = [
    ('cinew', {'note': 'Small rises in the liver enzyme ALT were linked to andrographis use in a survey of Thai patients, and mild '
                       'liver-enzyme elevations were the main side effect in COVID-19 trials; a real-world COVID-19 study found no '
                       'rise with it. Stop and seek advice if signs of liver problems appear.',
               'severity': 'caution', 'reference_ids': ['REF-5149', 'REF-5142', 'REF-5150']}),
    ('cinew', {'note': 'Most serious reactions on record, including allergic reactions, involve injectable andrographolide-derived '
                       'drugs used in China (adverse reactions in about 4-5% of treated patients); herbal preparations of the plant '
                       'taken by mouth had a better safety record in a systematic review.',
               'severity': 'info', 'reference_ids': ['REF-5148']}),
    ('ciadd', 'May lower blood pressure and blood sugar', ['REF-5151', 'REF-5152']),
]
NOTES['andrographis_paniculata'] = (
    'Searched PubMed (Andrographis paniculata / andrographis tiab; Kalmegh / andrographolide ti), Europe PMC, ClinicalTrials.gov '
    '(28) and OpenAlex. Added: Caceres 1999 SHA-10 cold RCT (cold, sore throat), 2026 Bio-Immune andrographolide URTI RCT (cold; '
    'signature-compound evidence), COVID evidence to infection (TCIM NMA 2026 and 2025 SR positive; CIM-MEG19 pilot; '
    'placebo RCT 2023, favipiravir add-on RCT and Thai cohort recorded as no-effect). IBD: 2024 herbal UC MA (AP RR 0.95 for '
    'response, 1.31 for remission, both NS) recorded as no-effect. Safety: ALT rise in a Thai survey, COVID-trial liver-enzyme '
    'elevations vs a null real-world study (new caution); SR showing ADRs concentrate in injectable andrographolide derivatives '
    '(new info); transient BP drop in healthy volunteers and HbA1c/insulin fall in an open diabetes study to the BP/sugar '
    'caution. Bucket: progressive-MS RCT (disability, not fatigue), RA RCT (within-group changes only). Not added: Kan Jang and '
    'ImmunoGuard (with Eleutherococcus), andrographolide sulfonate / Xiyanping injections (derivative drugs), malaria open '
    'trial, CYP review (data insufficient), allergic-reaction letter 2026 (no abstract).')

# ================================================================== dill
PLAN['anethum_graveolens'] = [
    ('add', 'skin-irritation', ['REF-5155']),
    ('note', 'skin-irritation', 'Dill oil reduced itching (pruritus) more than placebo in a double-blind randomized trial in people '
     'on haemodialysis'),
    ('status', 'skin-irritation', 'verified'),
    ('newpair', 'pregnancy-support', ['REF-5156', 'REF-5157'],
     'Boiled dill seed shortened the stages of labour in a systematic review of two randomized trials and two cohort studies and '
     'in a randomized trial; for use only alongside maternity care'),
    ('nulladd', 'metabolic-support', ['REF-5158']),
    ('note', 'metabolic-support', 'Dill improved insulin resistance and LDL cholesterol in a meta-analysis of randomized trials, '
     'and glycaemic control in a trial in type 2 diabetes; a 12-week trial in metabolic syndrome found no difference from placebo'),
    ('arm', 'anti-inflammatory', ['REF-1391', 'REF-0174']), ('arm', 'antimicrobial', ['REF-1391', 'REF-0174']),
    ('arm', 'antioxidant', ['REF-0174']), ('arm', 'digestive', ['REF-0174']), ('arm', 'diuretic', ['REF-1391', 'REF-0174']),
    ('refadd', ['REF-0210', 'REF-5160', 'REF-5161']),
]
POST['anethum_graveolens'] = [('ciadd', 'Widely used as a food herb', ['REF-5159'])]
NOTES['anethum_graveolens'] = (
    'Searched PubMed (Anethum graveolens tiab, dill ti), Europe PMC, ClinicalTrials.gov (5) and OpenAlex. Added: haemodialysis '
    'pruritus RCT (skin-irritation now direct and verified); NEW pregnancy-support pair (labour-duration SR 2020 + boiled-seed RCT '
    '2014; condition synonyms include labour support); MetS 12-week RCT recorded as no-effect; anaphylaxis case report to the '
    'allergy caution. CLEANUP: the 2020 T2DM RCT (REF-1391) and the 2022 lipid/glycaemic MA (REF-0174) had been pasted onto '
    'anti-inflammatory, antimicrobial, digestive and diuretic (and the MA onto antioxidant), which neither states; removed, and '
    'two actions they do support added (lipid-lowering, antidiabetic). Both cautions also cited them plus the POWO taxon page '
    'REF-0210 (moved to references); removed. The allergy caution named an "Egyptian Drug Authority" source that was never '
    'cited; that attribution is removed (the WHO monograph remains). Bucket: thyroid RCT (no vocab condition), postpartum '
    'haemorrhage RCT (near-miss, not heavy menstrual bleeding). Not added: Apiaceae dysmenorrhoea MA 41653970 (judged before: '
    'no dill-specific result), dill vs mefenamic acid/gemfibrozil/chlorhexidine trials (active comparators only), dill + '
    'chamomile oil, blackberry-dill, black sticky rice + dill combinations, case reports without abstracts (contact urticaria, '
    'occupational dermatitis, fresh-dill allergy).')

# ================================================================== angelica
PLAN['angelica_archangelica'] = []
NOTES['angelica_archangelica'] = (
    'Searched PubMed (Angelica archangelica / Archangelica officinalis / garden angelica tiab; 5 HT, 0 SR, 12 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (68, nearly all Chinese multi-herb formulas or Angelica gigas/sinensis) and OpenAlex. No new usable '
    'human study: Feru-guard trials in mild cognitive impairment and frontotemporal dementia combine ferulic acid with the '
    'extract (combination product); the NOGO overactive-bladder trial is already held (REF-3439, no-effect). Settled for now.')

# ================================================================== burdock
PLAN['arctium_lappa'] = [('refadd', ['REF-0211', 'REF-5168'])]
POST['arctium_lappa'] = [('ciadd', 'Generally safe as a food plant', ['REF-5162', 'REF-5163', 'REF-5164', 'REF-5165', 'REF-5166',
                                                                     'REF-5167'])]
BD_CAUTION = ('Generally safe as a food plant. Allergic contact dermatitis and anaphylaxis have been reported, and people allergic '
              'to chrysanthemums may cross-react. Some commercial burdock root teas have been contaminated with atropine from '
              'belladonna, causing anticholinergic poisoning. Acute liver injury was reported after a "liver detox" tea that '
              'combined burdock root with five other herbs. Avoid in pregnancy: burdock may stimulate the uterus.')
NOTES['arctium_lappa'] = (
    'Searched PubMed ("Arctium lappa" OR burdock tiab), Europe PMC, ClinicalTrials.gov (7) and OpenAlex. SAFETY: the caution cited '
    'only the POWO taxon page REF-0211, which states nothing about safety; rewritten from MSKCC About Herbs Burdock (REF-5162, '
    'read 2026-11-24; NCCIH has no burdock page, 404) with the case reports it corroborates (anaphylaxis, contact dermatitis, '
    'atropine-contaminated tea poisoning 1978/1984, detox-tea liver injury). Dropped as unsourced: "burs cause mechanical '
    'irritation" and "not recommended in biliary obstruction". POWO moved to references; removed from the Duke note too. '
    'Bucket: open RCT of burdock tea preventing recurrence of colonic diverticulitis (no vocab condition; no effect on '
    'diverticular bleeding). Not added: "Burdock complex" H. pylori RCT (composition not given), burdock + aqua-exercise RCTs in '
    'elderly women (no burdock-alone vs placebo contrast), fruit-extract skin-ageing RCT, Essiac, Menohelp, GBS-01 phase I '
    '(arctigenin-rich fruit extract, cancer, safety only), yellow dock + burdock tea thrombocytopenia case (two herbs).')


def text_edits():
    path = 'plants/anethum_graveolens.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    for c in d['contraindications']:
        c['reference_ids'] = [r for r in c['reference_ids'] if r not in ('REF-1391', 'REF-0174', 'REF-0210')]
    c0 = [c for c in d['contraindications'] if c['note'].startswith('Widely used as a food herb')]; assert len(c0) == 1
    assert '; Egyptian Drug Authority, n.d.' in c0[0]['note']
    c0[0]['note'] = c0[0]['note'].replace('; Egyptian Drug Authority, n.d.', '').replace('“', '"').replace('”', '"')
    acts = {a['action'] for a in d['actions']}
    assert 'lipid-lowering' not in acts and 'antidiabetic' not in acts
    d['actions'].append({'action': 'lipid-lowering', 'reference_ids': ['REF-0174', 'REF-3435', 'REF-1391'], 'status': 'verified'})
    d['actions'].append({'action': 'antidiabetic', 'reference_ids': ['REF-0174', 'REF-1391'], 'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/arctium_lappa.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    for c in d['contraindications']:
        c['reference_ids'] = [r for r in c['reference_ids'] if r != 'REF-0211']
    c0 = [c for c in d['contraindications'] if c['note'].startswith('Generally safe as a food plant')]; assert len(c0) == 1
    c0[0].update(note=BD_CAUTION, severity='caution', status='verified')
    assert '—' not in BD_CAUTION and '–' not in BD_CAUTION
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r03_changes.tsv')
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in PLAN]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
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
