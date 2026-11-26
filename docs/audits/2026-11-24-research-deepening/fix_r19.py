"""Research-deepening batch 19 (lamium-album, laurus-nobilis, lavandula-angustifolia, lentinula-edodes, leonurus-cardiaca).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5426.. (reserved)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-26'
LABEL = 'research-deepening batch 19'

SPEC = [
    # bay laurel
    ('REF-5426', '19177188', 'bayleaftype2diabetes', 'rct'),
    ('REF-5429', '41598335', 'bayleafliverinjury', 'clinical'),
    ('REF-5431', '8496654', 'bayleafoesophagus', 'clinical'),
    ('REF-5432', '17577382', 'laureloilmassagedermatitis', 'clinical'),
    ('REF-5433', '25933076', 'laureloilerythemamultiforme', 'clinical'),
    ('REF-5434', '8899117', 'bayleafoccupationalasthma', 'clinical'),
    ('REF-5435', '37885923', 'oleanderbaymisidentification', 'clinical'),
    # lavender
    ('REF-5436', '24731891', 'lavenderdysmenorrhea', 'rct'),
    ('REF-5437', '32379682', 'lavendermenopausemeta', 'meta-analysis'),
    ('REF-5438', '29778129', 'lavendermenopausesymptoms', 'rct'),
    ('REF-5439', '27388435', 'lavenderhotflushes', 'rct'),
    ('REF-5440', '30712745', 'lavendermenopausequalityoflife', 'rct'),
    ('REF-5441', '38754638', 'lavenderoraloilmenopause', 'rct'),
    ('REF-5442', '38919308', 'lavenderhaemodialysisfatigue', 'meta-analysis'),
    ('REF-5443', '35803088', 'lavenderfatiguems', 'rct'),
    ('REF-5444', '39775962', 'lavenderfatiguechemotherapy', 'rct'),
    ('REF-5445', '27863613', 'lavenderkneeoamassage', 'rct'),
    ('REF-5446', '40192256', 'lavenderkneeoaoil', 'rct'),
    ('REF-5447', '22558691', 'lavenderaphthousulcer', 'rct'),
    ('REF-5448', '23724853', 'lavenderpremenstrual', 'rct'),
    ('REF-5449', '17267908', 'lavendergynecomastia', 'clinical'),
    ('REF-5450', '31393563', 'lavenderthelarche', 'clinical'),
    ('REF-5451', '32147050', 'lavenderendocrinereview', 'systematic-review'),
    ('REF-5452', '35663791', 'lavenderendocrineprevalence', 'clinical'),
    ('REF-5453', '37906319', 'linaloolendocrinetesting', 'preclinical'),
    ('REF-5454', '30779160', 'lavendercontactallergy', 'clinical'),
    ('REF-5455', '18759894', 'lavenderoiloxidation', 'clinical'),
    ('REF-5456', '23401474', 'silexancytochrome', 'rct'),
    ('REF-5457', '25319228', 'silexancontraceptive', 'rct'),
    ('REF-5458', '33221027', 'silexandriving', 'rct'),
    ('REF-5459', '33300578', 'silexanabuse', 'rct'),
    ('REF-5460', '28319423', 'silexanwithdrawal', 'rct'),
    # shiitake
    ('REF-5461', '35814366', 'ahcchpvclearance', 'rct'),
    ('REF-5462', '22164761', 'lentinexelderlyimmune', 'rct'),
    ('REF-5463', '24168107', 'shiitakegabapentin', 'clinical'),
    ('REF-5464', '35466167', 'shiitakebowelobstruction', 'clinical'),
    ('REF-5465', '31413838', 'shiitakebowelobstructiontwo', 'clinical'),
    ('REF-5466', '35404185', 'shiitakedermatitisfrance', 'clinical'),
]
DOI_SPEC = [
    ('REF-5427', '10.51745/najfnr.8.17.86-98', 'bayleafteelipids', 'rct', {}),
    ('REF-5428', '10.1038/s41598-026-73555-y', 'bayleafteastress', 'rct', {}),
    ('REF-5430', '10.33706/jemcr.972191', 'bayleafhepatotoxicity', 'clinical', {}),
]


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
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== white dead-nettle
PLAN['lamium_album'] = []
NOTES['lamium_album'] = (
    'Searched PubMed (Lamium album / white dead nettle / white deadnettle tiab: 2 HT, 0 SR, 3 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (0) and OpenAlex (68 no-PMID hits, all lab or animal work). Nothing new: the only human trial (2005, '
    'atopic dermatitis) tested a combination with Eleutherococcus and yarrow; a 2022 screen of many plants on CYP3A4 and '
    'P-glycoprotein is lab-only; Lamium wound, liver, ovary and diabetes studies are in rats. Settled.')

# ================================================================== bay laurel
PLAN['laurus_nobilis'] = [
    ('newpair', 'blood-sugar', ['REF-5426'],
     'In a small randomized placebo-controlled trial in type 2 diabetes, 1-3 g of ground bay leaf a day for 30 days lowered '
     'fasting blood glucose by about a fifth to a quarter, while the placebo group did not change'),
    ('newpair', 'high-cholesterol', ['REF-5426', 'REF-5427'],
     'Ground bay leaf (1-3 g a day for 30 days) lowered total and LDL cholesterol in people with type 2 diabetes (small '
     'randomized placebo trial), and daily bay leaf tea for 10 days gave lower LDL and higher HDL cholesterol than a placebo '
     'tea in healthy adults (randomized double-blind pilot trial)'),
    ('newpair', 'stress', ['REF-5428'],
     'Daily bay leaf tea for 10 days lowered perceived stress scores more than a placebo tea in healthy adults (small '
     'randomized double-blind pilot trial)'),
    ('newpair', 'anxiety', ['REF-5428'],
     'Daily bay leaf tea for 10 days lowered anxiety scores (STAI) more than a placebo tea in healthy adults (small '
     'randomized double-blind pilot trial)'),
]
POST['laurus_nobilis'] = [
    ('cinew', {'note': 'Liver: two women who regularly drank bay leaf tea developed liver injury (case reports). In one, the '
                       'link was rated probable and she improved after stopping the tea; the other, who had drunk it daily '
                       'for a month, died of liver failure.',
               'severity': 'caution', 'reference_ids': ['REF-5429', 'REF-5430']}),
    ('cinew', {'note': 'Swallowing the leaves: whole bay leaves have lodged in the oesophagus (gullet) and blocked it (two case '
                       'reports); remove whole leaves from food before eating.',
               'severity': 'caution', 'reference_ids': ['REF-5431']}),
    ('cinew', {'note': 'Allergy: bay (laurel) leaf oil can cause allergic contact dermatitis, for example after a massage with '
                       'it, sometimes as an unusual target-like (erythema multiforme-like) rash; in a food-industry worker, '
                       'breathing in bay leaf and other herb dusts caused asthma, confirmed by inhalation tests (case '
                       'reports).',
               'severity': 'caution', 'reference_ids': ['REF-5432', 'REF-5433', 'REF-5434']}),
    ('cinew', {'note': 'Identification: an 84-year-old developed complete heart block after drinking a tea of oleander leaves '
                       'mistaken for bay leaves, and needed an antidote and a pacemaker (case report). Oleander contains heart '
                       'poisons (cardiac glycosides) in all its parts.',
               'severity': 'warning', 'reference_ids': ['REF-5435']}),
]
BAY_OLD = 'Generally safe when used in food amounts. Not toxic to people and safe to cook with.'
BAY_NEW = ('Generally safe in food amounts. Insufficient reliable information about safety during pregnancy or breastfeeding - '
           'stick to food amounts. Large amounts of bay leaf tea may cause vomiting (emetic properties) and drowsiness '
           '(sedative properties). In high doses, bay laurel has cytotoxic activity.')
NOTES['laurus_nobilis'] = (
    'Searched PubMed (Laurus nobilis / bay leaf / bay leaves / bay laurel tiab: 9 HT, 4 SR, 63 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (3) and OpenAlex (72 no-PMID hits). Added: NEW blood-sugar pair (2009 placebo trial in type 2 '
    'diabetes; the abstract says only "divided into 4 groups", the PMC full text says "divided randomly"; within-group '
    'analysis, baseline glucose differed between groups); NEW high-cholesterol pair (same trial + 2024 randomized '
    'double-blind placebo pilot of bay leaf tea, PACTR202205671550114); NEW stress and anxiety pairs (2026 Sci Rep '
    'randomized double-blind placebo pilot, PACTR202205585377035; the two 2024/2026 pilots report the same 55 participants '
    'with different outcomes, each cited only for its own outcome); liver caution (2026 RUCAM-probable case; 2021 fatal '
    'fulminant hepatitis case, DOI only); oesophageal impaction caution (1993, two cases); allergy caution (laurel oil '
    'contact dermatitis 2007 and 2015; occupational asthma 1996); oleander-mistaken-for-bay warning (2023). TEXT EDIT: the '
    'unsourced needs-review caution lost "Not toxic to people and safe to cook with" (contradicted by the liver cases) and '
    'its leaf-rigidity and laurel-oil dermatitis sentences (now sourced cautions); the rest stays needs-review. Not added: '
    '2017 randomized crossover bay-leaf cookie trial (glucose lower at 30 and 45 min only, no difference in the overall '
    'glucose response, iAUC p = 0.41); 2011 Res J Med Plant diabetes study (randomisation not stated, abstract wording '
    'closely copies the 2009 paper); 2007 FASEB abstract (same trial as 2009); 2023 essential-oil inhalation study in 849 '
    'hypertensive women (24 oils, randomisation not stated); 2020 spice-blend meal trial (13 spices); 2026 insomnia '
    'preprint; impaction, perforation and bleeding case letters with no abstract (1980-1999: duodenum, small bowel, '
    'Meckel diverticulum, hypopharynx); bay leaf phytodermatitis and erythema multiforme letters with no abstract; chemical '
    'burn from a three-oil mixture (combination); Frullania cross-sensitisation chemistry (1975); West Indian bay (Pimenta '
    'racemosa) GRAS review (other species); 2022 and 2020 uncontrolled tea studies (REF-1682/1683, cited for dosage only). '
    'Possible follow-up for the owner: oleander as a formal Dangerous Lookalikes entry (needs a sourced toxicology and '
    'distinguishing-features write-up).')

# ================================================================== lavender
PLAN['lavandula_angustifolia'] = [
    ('newpair', 'menstrual-cramps', ['REF-5436'],
     'Inhaling lavender (in sesame oil) over four menstrual cycles eased period-pain symptoms more than placebo in 96 students '
     'with primary dysmenorrhoea (randomized trial)'),
    ('newpair', 'menopause', ['REF-5437', 'REF-5438', 'REF-5440'],
     'Lavender aromatherapy reduced menopausal symptoms in a meta-analysis of trials (some combined lavender with other aromas) '
     'and in randomized trials of inhaled lavender, including menopause-specific quality of life; an oral lavender oil '
     'capsule did not beat placebo on overall symptoms (randomized trial)'),
    ('nulladd', 'menopause', ['REF-5441']),
    ('newpair', 'hot-flashes', ['REF-5439', 'REF-5437'],
     'Smelling lavender for 20 minutes twice a day for 12 weeks reduced the number of hot flushes compared with a control '
     'scent (randomized crossover trial); a meta-analysis of lavender aromatherapy also reported fewer hot flushes'),
    ('newpair', 'fatigue', ['REF-5442', 'REF-5443', 'REF-5444'],
     'Lavender reduced fatigue in a meta-analysis of trials of inhaled oil in haemodialysis patients, in a randomized '
     'double-blind trial of lavender flower capsules in multiple sclerosis, and in a randomized trial of inhaled oil during '
     'chemotherapy for blood cancers'),
    ('add', 'arthritis', ['REF-5445', 'REF-5446']),
    ('note', 'arthritis',
     'Lavender oil eased knee osteoarthritis pain: aromatherapy massage with lavender oil reduced pain compared with no massage '
     'for up to a week but not at four weeks (randomized trial), and lavender oil worked about as well as piroxicam gel, '
     'while an untreated group did not change (randomized double-blind trial)'),
    ('newpair', 'oral-health', ['REF-5447'],
     'Lavender oil applied to recurrent mouth ulcers (aphthous ulcers) reduced ulcer size, inflammation and pain and shortened '
     'healing compared with placebo (randomized double-blind trial)'),
    ('newpair', 'pms', ['REF-5448'],
     'A single 10-minute inhalation of lavender in the premenstrual phase eased low mood and confusion and raised calming '
     '(parasympathetic) nerve activity compared with water in women with premenstrual symptoms (small randomized crossover '
     'trial)'),
]
POST['lavandula_angustifolia'] = [
    ('cinew', {'note': 'Children: in case reports, a few prepubertal boys developed breast growth, and girls early breast '
                       'development, while lavender-containing products (oils, lotions, colognes; in some cases with tea tree '
                       'oil) were used on them regularly; it went away after the products were stopped. A systematic review '
                       'found little evidence of a causal link, a survey of 556 children found no cases, and guideline tests '
                       'of lavender oil\'s main compounds found no hormone activity (case reports; review; survey; lab and '
                       'animal studies).',
               'severity': 'caution',
               'reference_ids': ['REF-5449', 'REF-5450', 'REF-5451', 'REF-5452', 'REF-5453']}),
    ('cinew', {'note': 'Skin allergy: lavender is an uncommon cause of allergic contact dermatitis, mostly from personal-care '
                       'products and essential oils (2.2% of 2,178 patients patch-tested with lavender at an Australian clinic '
                       'reacted). Lavender oil left exposed to air oxidises into stronger skin allergens (patch-test and lab '
                       'study).',
               'severity': 'caution', 'reference_ids': ['REF-5454', 'REF-5455']}),
    ('cinew', {'note': 'Medicines: in randomized crossover studies in healthy volunteers, the oral lavender oil Silexan (160 mg a '
                       'day) had no relevant effect on the drug-clearing enzymes CYP1A2, CYP2C9, CYP2D6 and CYP3A4 (the '
                       'CYP2C19 result was inconclusive) and did not change levels of an ethinyl estradiol/levonorgestrel '
                       'contraceptive pill.',
               'severity': 'info', 'reference_ids': ['REF-5456', 'REF-5457']}),
    ('cinew', {'note': 'Driving and dependence: in randomized trials, Silexan did not impair simulated driving (unlike '
                       'lorazepam), was not liked more than placebo by recreational drug users even at eight times the usual '
                       'dose, and caused no withdrawal symptoms when stopped abruptly after 10 weeks.',
               'severity': 'info', 'reference_ids': ['REF-5458', 'REF-5459', 'REF-5460']}),
]
NOTES['lavandula_angustifolia'] = (
    'Searched PubMed (Lavandula angustifolia / Lavandula officinalis / Silexan tiab, lavender ti: 347 HT, 58 SR, 193 SAFE '
    'hits), Europe PMC, ClinicalTrials.gov (123) and OpenAlex. Huge plant: screened the SR family, conditions without a pair '
    'and safety; anxiety (9), depression (9), insomnia (8), pain (8), stress (7) and wounds (7) were not padded. INTEGRITY '
    'HOLD checked: no new reference is first- or last-authored by the flagged Tehran psychopharmacology group; the 2003 '
    'lavender tincture vs imipramine depression trial (12551734) is from that group and was not added. Added: NEW '
    'menstrual-cramps (2014 placebo RCT), menopause (2020 MA + two RCTs; 2024 oral-oil RCT recorded as no-effect on overall '
    'symptoms), hot-flashes (2016 crossover RCT + the MA; 29778129 and 27388435 report the same Ardabil trial and are cited '
    'on different pairs), fatigue (2024 haemodialysis MA, 2022 MS capsule RCT, 2025 chemotherapy RCT), oral-health (2012 '
    'aphthous-ulcer placebo RCT) and pms (2013 crossover RCT) pairs; knee osteoarthritis RCTs (2016, 2025) to arthritis; '
    'cautions on prepubertal breast growth (case reports with the review, survey and guideline tests that question '
    'causality) and on skin allergy (Australian patch-test series; oxidised oil); info notes on Silexan drug, contraceptive, '
    'driving, abuse and withdrawal studies. Not added: headache (2022 post-dural-puncture RCT different only immediately '
    'after inhalation; 2012 migraine trial does not state randomisation; clove+lavender and nitroglycerin-headache trials '
    'not significant or vs acetaminophen); sexual function (benefit only in a domain of the oral-oil RCT, aromatherapy '
    'combinations); 2025 post-intubation sore-throat gauze trial (procedure-specific); 29389470 (same knee OA trial as '
    '27863613); 2024 blood-pressure trial (with ylang-ylang) and a 2013 trial where lavender tended to raise blood pressure; '
    'nausea (peppermint+ginger+lavender blend); restless legs and dementia agitation (no vocab condition); combinations with '
    'bergamot, bitter orange, rosemary, sweet orange or ginger; L. stoechas labour-pain MA and anticholinergic tea case '
    '(other species); retracted burn-pain MA and retracted cardiovascular review; serotonin-toxicity letter with sertraline '
    '(no abstract; a possible interaction worth re-checking if the full text becomes available); aromatherapist contact '
    'dermatitis letters with no abstract.')

# ================================================================== shiitake
PLAN['lentinula_edodes'] = [
    ('add', 'infection', ['REF-5461']),
    ('note', 'infection',
     'AHCC, a standardised extract of cultured shiitake mycelium, helped clear persistent high-risk HPV infection: 14 of 22 '
     'women were HPV-negative after 6 months vs 2 of 19 on placebo (randomized double-blind trial)'),
    ('add', 'immune-support', ['REF-5462']),
    ('note', 'immune-support',
     'Eating shiitake daily improved immune cell function and raised secretory IgA in healthy adults in a randomized trial; '
     'a shiitake mycelium beta-glucan (Lentinex) raised B-cell numbers vs placebo in healthy older adults (randomized '
     'crossover trial)'),
]
POST['lentinula_edodes'] = [
    ('cinew', {'note': 'Bowel blockage: shiitake eaten in large or poorly chewed pieces has blocked the small bowel; two people '
                       'without teeth who ate uncut shiitake needed surgery (case reports).',
               'severity': 'caution', 'reference_ids': ['REF-5464', 'REF-5465']}),
    ('ciadd', 'Eating raw or undercooked shiitake can cause shiitake dermatitis', ['REF-5466']),
    ('cinew', {'note': 'Medicines: a shiitake-rich diet slightly increased the kidneys\' clearance of gabapentin without changing '
                       'its overall blood levels (volunteer study).',
               'severity': 'info', 'reference_ids': ['REF-5463']}),
]
NOTES['lentinula_edodes'] = (
    'Searched PubMed (Lentinula edodes / Lentinus edodes / shiitake tiab, lentinan ti: 113 HT, 22 SR, 362 SAFE hits), '
    'Europe PMC (two queries timed out and were re-run), ClinicalTrials.gov (22) and OpenAlex. Lentinan injections and '
    'intrapleural infusions excluded (route); the cancer pair (8) was not padded. Added: 2022 AHCC randomized placebo HPV '
    'trial to infection (NCT02405533; AHCC is a cultured L. edodes mycelium extract); 2011 Lentinex crossover RCT to '
    'immune-support; bowel-obstruction caution (2019 two surgical cases, 2022 case); French poison-centre series (59 '
    'dermatitis cases 2014-2019) to the shiitake-dermatitis caution; gabapentin diet study as an info note. Not added: '
    '2021 double-blind RCT of shiitake bars (only triglycerides fell, 10%; no cholesterol change, so no high-cholesterol '
    'pair; the abstract also reports dermatitis in "10% of individuals sensitive to the mushroom", wording unclear); 2012 '
    'anticaries crossover RCT (plaque metabolism only, a surrogate) and 2011 mouthrinse study (randomisation not stated); '
    '2023 lentinan nasal drops in COVID-19 (faster antigen clearance, no symptom difference); 2023 AHCC taste-disorder RCT '
    'and 2025 L.E.M. neuropathy RCT (no vocab condition; the neuropathy primary endpoint was null); 2013 eccentric-exercise '
    'crossover study (no effect on inflammation); 2018 AHCC stress study (design unclear); 2020 Lentinex well-being RCT (no '
    'vocab condition); fermented rice bran (MGN-3/Biobran) and mushroom-blend or multi-ingredient products; dermatitis case '
    'reports already covered by REF-1168/REF-1169.')

# ================================================================== motherwort
PLAN['leonurus_cardiaca'] = []
NOTES['leonurus_cardiaca'] = (
    'Searched PubMed (Leonurus cardiaca / motherwort tiab: 17 HT, 10 SR, 36 SAFE hits), Europe PMC (one query timed out and '
    'was re-run), ClinicalTrials.gov (1, not yet recruiting) and OpenAlex. Nothing new: almost all trials and meta-analyses '
    'are of Chinese motherwort injection (L. japonicus; other species and route) for postpartum or post-abortion bleeding. '
    'GAP: a 2011 study of L. cardiaca oil extract (1,200 mg a day for 28 days) in 50 people with hypertension plus anxiety '
    'and sleep problems reported improvement but had no control group, so no pair was created. A 2015 review lists '
    '"motherwort" among herbs that reduce platelet aggregation without naming the species, so it was not added to the '
    'anticoagulant caution.')


def text_edits():
    """Trim the unsourced bay laurel caution to what is not now covered by sourced cautions (rd_fix ops do not rewrite text)."""
    path = 'plants/laurus_nobilis.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'].startswith(BAY_OLD)]; assert len(c) == 1
    c[0]['note'] = BAY_NEW
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r19_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
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
