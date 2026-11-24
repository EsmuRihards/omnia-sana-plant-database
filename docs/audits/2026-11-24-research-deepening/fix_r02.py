"""Research-deepening batch 2 (agrimonia-eupatoria, alchemilla-vulgaris, allium-sativum, aloe-vera, aloysia-citrodora).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5083.. (reserved block).
Also: every campaign entry with a PMID but no DOI gets its PubMed url (build.py best_link otherwise falls back to a
title search on the public source card) - applied to batch 1 entries too."""
import copy, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 2'

SPEC = [
    # lady's mantle
    ('REF-5083', '30904703', 'alchemillagelskinbarrier', 'clinical'),
    ('REF-5084', '17163290', 'alchemillaaphthous', 'clinical'),
    ('REF-5085', '33866772', 'alchemillasorethroat', 'rct'),
    # garlic
    ('REF-5086', '40580481', 'garliccvriskma2026', 'meta-analysis'),
    ('REF-5087', '40628369', 'agedgarlicbplipidsma', 'meta-analysis'),
    ('REF-5088', '38892625', 'garlicglucoselipidsma', 'meta-analysis'),
    ('REF-5089', '23590705', 'garliclipidsma2013', 'meta-analysis'),
    ('REF-5090', '37481521', 'garlicmetsynma', 'meta-analysis'),
    ('REF-5091', '38223588', 'garlicliverdiseasema', 'meta-analysis'),
    ('REF-5092', '36576698', 'garlicnafldma', 'meta-analysis'),
    ('REF-5093', '34760020', 'garlicpms', 'rct'),
    ('REF-5094', '41341173', 'garlicmsfatigue', 'rct'),
    ('REF-5095', '36222178', 'garlicplateletsr', 'systematic-review'),
    ('REF-5096', '32051282', 'garlicinflammatoryma', 'meta-analysis'),
    ('REF-5097', '19749390', 'garlicbptrialquality', 'systematic-review'),
    ('REF-5098', '33571752', 'garlicburnssr', 'systematic-review'),
    ('REF-5099', '34335819', 'garlicendometriosis', 'rct'),
    ('REF-5100', '42861727', 'garlicgenitalwarts', 'rct'),
    # aloe
    ('REF-5102', '15043514', 'aloeulcerativecolitis', 'rct'),
    ('REF-5103', '16749917', 'aloeibs2006', 'rct'),
    ('REF-5104', '32314514', 'aloeibs2020', 'rct'),
    ('REF-5105', '27152917', 'aloeglucosema2016', 'meta-analysis'),
    ('REF-5106', '36249738', 'aloeradiodermatitissr', 'systematic-review'),
    ('REF-5107', '28547955', 'aloeradiodermatitisnull', 'rct'),
    ('REF-5108', '37670716', 'aloediabeticfoot', 'rct'),
    ('REF-5109', '17499928', 'aloeburnssr2007', 'systematic-review'),
    ('REF-5110', '36320801', 'aloeaphthous', 'rct'),
    ('REF-5111', '42317150', 'naturalagentsgingivalma', 'meta-analysis'),
    ('REF-5112', '27856182', 'aloeliverinjury', 'clinical'),
    ('REF-5113', '33132775', 'aloejuiceliver', 'clinical'),
    ('REF-5114', '28539037', 'aloebezoar', 'clinical'),
    ('REF-5115', '33221425', 'aloegelfoodtox', 'systematic-review'),
    ('REF-5116', '31680350', 'aloeemodinreview', 'narrative-review'),
    ('REF-5118', '32924222', 'aloeumbrellareview', 'systematic-review'),
    ('REF-5119', '33383112', 'aloeatrophicvaginitis', 'rct'),
    ('REF-5120', '26742306', 'aloegerd', 'rct'),
    ('REF-5131', '42866774', 'aloeecchymosis', 'rct'),
    # lemon verbena
    ('REF-5122', '35011093', 'lemonverbenastresssleep', 'rct'),
    ('REF-5123', '37216059', 'lemonverbenaaromaanxiety', 'rct'),
    ('REF-5124', '34745923', 'saffronlippiaanxiety', 'rct'),
    ('REF-5125', '27222830', 'lippiateratogenicity', 'preclinical'),
    ('REF-5126', '27642323', 'verbascosideteratogenicity', 'preclinical'),
    ('REF-5127', '20967458', 'lemonverbenaexerciseoxidative', 'rct'),
    ('REF-5128', '42191680', 'lippiacardiometabolicma', 'meta-analysis'),
]
DOI_SPEC = [
    ('REF-5101', '10.1684/phyto.2024.0421', 'alchemillaantiinflammatory', 'preclinical', {}),
    ('REF-5117', '10.2903/j.efsa.2018.5090', 'efsahydroxyanthracenes', 'traditional', {'pmid': '32625659'}),
    ('REF-5121', '10.3390/app15115856', 'lemonverbenaadolescents', 'rct', {}),
]
WEB = {
    'nccih2025garlic': ('REF-5129', [
        ('author', 'National Center for Complementary and Integrative Health'), ('title', 'Garlic: Usefulness and Safety'),
        ('year', '2025'), ('url', 'https://www.nccih.nih.gov/health/garlic'), ('note', 'REF-5129'), ('study_type', 'traditional'),
        ('summary', 'NIH/NCCIH fact sheet, last updated February 2025, read 2026-11-24. Safety: oral garlic used safely in studies '
                    'of up to 7 years; side effects breath and body odour, abdominal pain, flatulence, nausea; allergic reactions '
                    'occur; garlic supplements may increase bleeding risk (tell providers before surgery or with anticoagulants or '
                    'aspirin); fresh raw garlic on the skin can cause severe irritation and chemical burns; may not be safe in '
                    'pregnancy or breastfeeding in amounts greater than food.')]),
    'nccih2025aloevera': ('REF-5130', [
        ('author', 'National Center for Complementary and Integrative Health'), ('title', 'Aloe Vera: Usefulness and Safety'),
        ('year', '2025'), ('url', 'https://www.nccih.nih.gov/health/aloe-vera'), ('note', 'REF-5130'), ('study_type', 'traditional'),
        ('summary', 'NIH/NCCIH fact sheet, last updated February 2025, read 2026-11-24. Topical gel generally well tolerated, with '
                    'occasional burning, itching, rash and eczema; oral aloe latex causes abdominal pain, cramps and diarrhoea; oral '
                    'aloe leaf extracts linked to cases of acute hepatitis; short-term oral gel up to 42 days appears safe; IARC '
                    'classes non-decolorized whole-leaf extract as a possible human carcinogen; FDA removed aloe latex from OTC '
                    'laxatives in 2002; overuse of latex may increase adverse effects of cardiac glycosides such as digoxin; oral '
                    'aloe in any form may be unsafe in pregnancy and breastfeeding.')]),
}


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
    # PubMed record 33132775 carries a wrong DOI (the EFSA opinion's); keep PMID + url only
    for k, (r, f) in list(new.items()):
        if r == 'REF-5113':
            new[k] = (r, [(a, b) for a, b in f if a != 'doi'])
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== agrimony
PLAN['agrimonia_eupatoria'] = []
NOTES['agrimonia_eupatoria'] = (
    'Searched PubMed ("Agrimonia eupatoria" OR agrimony tiab; 5 families), Europe PMC, ClinicalTrials.gov (0) and OpenAlex '
    '(154 trial-worded, all off-topic or animal). No new human study of agrimony alone: the only trials are a multi-herb IBS '
    'formula (bilberry, slippery elm, agrimony, cinnamon; 20954962) and a Chinese rhubarb-based paraquat protocol. Not added: '
    'Ribeiro 2017 (Rev Cienc Agrar) narrative review asserting anticoagulant/antihypertensive interactions without primary data; '
    'rat liver studies (already represented). The held liver-support RCT (REF-3412) and EU monograph remain the human evidence.')

# ================================================================== lady's mantle
PLAN['alchemilla_vulgaris'] = [
    ('aadd', 'vulnerary', ['REF-5083', 'REF-5084', 'REF-3192']),
    ('aadd', 'anti-inflammatory', ['REF-5101']),
    ('refadd', ['REF-5085']),
]
LM_BOT = ('Low perennial herb, only about a foot high and green throughout, from a short, stout, black rootstock. The lower leaves '
          'are 6-8 inches across on stalks 6-18 inches long, somewhat kidney-shaped, and cut into seven or mostly nine broad but '
          'shallow lobes, finely toothed at the edges; the upper leaves are stalkless or short-stalked. The numerous small flowers, '
          'only about 1/8 inch across, are yellow-green, have no petals and four stamens, and are borne in loose clusters from June '
          'to August.')
LM_HARV = ('The whole herb is gathered in June and July, when in flower and when the leaves are at their best, and dried; the root '
           'is sometimes also used, generally fresh.')
LM_HAB = ('Grows in moist, hilly pastures and by streams, up to about 3,600 feet in the Scottish Highlands - essentially a plant of '
          'the north; native to Europe and parts of temperate Asia.')
LM_TRAD = ('Lady\'s mantle was valued as an astringent and styptic herb because of its tannin, and was formerly considered one of the '
           'best wound herbs; Culpeper recommended it for inflamed wounds and to stop bleeding, vomiting and fluxes. In early '
           'twentieth-century herbal practice it was taken as an infusion for excessive menstruation, and a strong decoction of the '
           'fresh root was recommended to stop bleeding.')
LM_INF = ('An infusion of 1 oz of the dried herb to 1 pint of boiling water, taken in teacupful doses (historically for excessive '
          'menstruation); the same infusion was used as a wash.')
LM_DOSE = ('Grieve (1931) gives an infusion of 1 oz (about 28 g) of dried herb to 1 pint (about 570 mL) of boiling water, taken in '
           'teacupful doses as required, and a fluid extract dose of 1/2 to 1 drachm (about 2-4 mL). These are historical doses, not '
           'modern standardised guidance. Educational reference only, not a prescription.')
NOTES['alchemilla_vulgaris'] = (
    'Searched PubMed (Alchemilla vulgaris / xanthochlora / lady\'s mantle / Alchemillae herba), Europe PMC, ClinicalTrials.gov '
    '(0) and OpenAlex. Human data found: hydrogel skin-barrier repair study in volunteers + fibroblast assay (REF-5083), open-label '
    'aphthous-ulcer study of a 3% extract in glycerine (REF-5084) - both wired to vulnerary (no RCT, so no new pair, inv. 12a); '
    'double-blind RCT of Alchemilla in glycerine vs IV dexamethasone for post-intubation sore throat found no difference '
    '(REF-5085, active comparator only; bucketed, no sore-throat pair). Rat anti-inflammatory/analgesic study (Phytotherapie '
    '2024) to anti-inflammatory. Grieve Lady\'s Mantle (REF-3192, read 2026-11-24 by the web-fetch agent) now sources the '
    'description, harvesting, habitat, traditional uses, infusion and a historical dose; POWO REF-0208 no longer cited for '
    'description or harvesting (a taxonomy database states neither) and removed from the general caution (it states nothing '
    'about safety), which now rests on Hoffmann alone and is set to needs-review. EMA status for Alchemillae herba could not be '
    'checked (EMA site 404/403). Not added: weighlevel 4-plant combination; antihaemorrhoidal Alchemilla/Conyza/Nigella mixture.')

# ================================================================== garlic
PLAN['allium_sativum'] = [
    ('newpair', 'liver-support', ['REF-5091', 'REF-5092'],
     'Garlic supplements lowered the liver enzymes ALT and AST vs control in meta-analyses of randomized trials in chronic liver '
     'disease and in non-alcoholic fatty liver disease, where fatty liver also improved more often than with placebo'),
    ('newpair', 'pms', ['REF-5093'],
     'Garlic tablets taken for three cycles reduced the severity of premenstrual symptoms vs placebo in a double-blind randomized '
     'trial'),
    ('newpair', 'fatigue', ['REF-5094'],
     'Garlic extract reduced fatigue and improved quality of life vs placebo in a single-blind randomized trial in people with '
     'multiple sclerosis'),
    ('add', 'high-cholesterol', ['REF-5089', 'REF-5088', 'REF-5087', 'REF-5086']),
    ('add', 'high-blood-pressure', ['REF-5086', 'REF-5087']),
    ('nulladd', 'high-blood-pressure', ['REF-5097']),
    ('note', 'high-blood-pressure', 'Garlic lowered blood pressure in people with hypertension in meta-analyses of randomized trials '
     '(aged garlic lowered systolic but not diastolic pressure); a 2009 systematic review judged most blood-pressure trials too '
     'poor in quality to confirm the effect'),
    ('add', 'blood-sugar', ['REF-5088', 'REF-5086']),
    ('add', 'metabolic-support', ['REF-5090', 'REF-5086']),
    ('add', 'cardiovascular-support', ['REF-5086']),
    ('add', 'inflammation', ['REF-5086']),
    ('nulladd', 'inflammation', ['REF-5096']),
    ('note', 'inflammation', 'Garlic lowered CRP and TNF-alpha in a 2026 meta-analysis of randomized trials (IL-6 unchanged); an '
     'earlier meta-analysis found no significant overall effect on these markers, only in longer or higher-dose subgroups'),
    ('refadd', ['REF-5099', 'REF-5100']),
]
POST['allium_sativum'] = [
    ('ciadd', 'Garlic is generally very safe', ['REF-5129', 'REF-5098', 'REF-5095']),
]
NOTES['allium_sativum'] = (
    'Searched PubMed (Allium sativum tiab; garlic/allicin/aged garlic ti; 5 families: 475 HT, 132 SR, 1,010 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (103) and OpenAlex. NEW pairs (inv. 12a): liver-support (two MAs: chronic liver disease 4 RCTs, '
    'NAFLD 4 RCTs), pms (double-blind RCT 2021), fatigue (single-blind RCT in MS 2025). Added 2026 CV-risk MA (Nutr Rev), aged '
    'garlic GRADE MA, glucose/lipid MA 2024, Ried 2013 lipid MA, MetS MA 2023. No-effect: Simons 2009 SR (BP effect cannot be '
    'ascertained, poor trial quality); 2021 inflammatory-mediator MA (overall NS). Safety: NCCIH garlic fact sheet (REF-5129; the '
    'caution already named NCCIH without citing it; POWO taxon page REF-0209 removed from both cautions), garlic-burn SR (39 cases), platelet-aggregation SR (6 of 12 RCTs reduced '
    'aggregation; inconclusive). Bucket: endometriosis-pain RCT (near-miss, inv. 12c: endometriosis pain is not ordinary period '
    'pain), topical garlic vs podophyllin genital-wart RCT (active comparator only, similar response; itching/burning in 22%). '
    'Not added: retracted aged-garlic BP MA 39437887 and retracted pregnancy trial (39471241 notice); garlic mouthwash caries MA '
    '(microbial counts only, and raw garlic on mucosa conflicts with the burn warning); dietary-intake cancer MAs (association, '
    'not treatment); onion+garlic, moringa+garlic, polyherbal and COVID combination products; preclinical MAs; animal '
    'interaction studies. Cardiovascular pairs were already 9-10.')

# ================================================================== aloe
PLAN['aloe_vera'] = [
    ('newpair', 'ibd', ['REF-5102'],
     'Oral aloe vera gel produced a clinical response more often than placebo (47% vs 14%) in a small 4-week double-blind '
     'randomized trial in active ulcerative colitis; remission rates did not differ significantly'),
    ('newpair', 'bruising', ['REF-5131'],
     'Aloe vera gel applied for 6 days reduced bruising (ecchymosis) at the leg vein harvest site after heart bypass surgery '
     'compared with the untreated leg and with cold/warm compresses, in a randomized trial'),
    ('nulladd', 'ibs', ['REF-5103', 'REF-5104']),
    ('note', 'ibs', 'Improved IBS symptoms vs placebo in a meta-analysis of three small randomized trials; two other randomized '
     'trials (2006, 2020) found no overall benefit over placebo'),
    ('add', 'blood-sugar', ['REF-5105']),
    ('note', 'blood-sugar', 'Lowered fasting blood glucose and HbA1c in meta-analyses of trials in prediabetes and type 2 diabetes '
     '(evidence limited, with signs of publication bias)'),
    ('add', 'skin-irritation', ['REF-5106']),
    ('nulladd', 'skin-irritation', ['REF-5107']),
    ('note', 'skin-irritation', 'Used on irritated and inflamed skin (reviews); a 2022 systematic review of 14 randomized trials found '
     'aloe lowered the risk of radiation skin reactions, while an earlier systematic review and a 2017 trial found no benefit'),
    ('add', 'wounds', ['REF-5108', 'REF-5109']),
    ('note', 'wounds', 'Aloe sped healing of second-degree burns in meta-analyses of randomized trials, aided diabetic foot ulcer '
     'healing in a double-blind trial and aided skin wound healing in a systematic review; a Cochrane review found no high-quality '
     'evidence for acute and chronic wounds'),
    ('add', 'oral-health', ['REF-5110', 'REF-5111']),
    ('note', 'oral-health', 'Aloe gel healed mouth ulcers faster and reduced severe chemotherapy or radiotherapy mouth sores '
     '(meta-analyses of randomized trials), and beat placebo for recurrent aphthous ulcers; a meta-analysis of natural '
     'oral-care products found aloe consistently improved gingival health'),
    ('refadd', ['REF-5118', 'REF-5119', 'REF-5120']),
]
POST['aloe_vera'] = [
    ('ciadd', 'Topical use of aloe gel is generally safe', ['REF-5130', 'REF-5117', 'REF-5115', 'REF-5116', 'REF-5112', 'REF-5113',
                                                           'REF-5114', 'REF-5105']),
    ('padd', 'Latex/dried juice', ['REF-5130', 'REF-5117']),
    ('dcinew', {'drug_class': 'cardiac-glycosides', 'severity': 'caution',
                'mechanism': 'NCCIH warns that overuse of aloe latex, a stimulant laxative, may increase the risk of adverse effects '
                             'from cardiac glycosides such as digoxin.',
                'reference_ids': ['REF-5130']}),
]
AL_CAUTION = ('Topical aloe gel is generally well tolerated, though burning, itching, rash and eczema are occasionally reported. '
              'Taken by mouth, aloe latex can cause abdominal pain, cramps and diarrhoea, and the US FDA removed it from '
              'over-the-counter laxatives in 2002 for lack of safety data. IARC classes non-decolorized whole-leaf aloe extract as '
              'possibly carcinogenic to humans, and the European Food Safety Authority regards the hydroxyanthracene derivatives '
              'in aloe latex and whole-leaf extracts (such as aloe-emodin) as genotoxic and carcinogenic unless shown otherwise. '
              'Acute hepatitis has been reported after oral aloe leaf extracts, while purified inner-leaf gel did not change liver '
              'tests in healthy volunteers over 60 days. Large amounts of the fibrous gel have caused bowel obstruction (bezoar). '
              'Oral aloe may lower blood sugar, so monitor glucose with diabetes medicines, and oral aloe in any form may be unsafe '
              'in pregnancy and while breastfeeding.')
AL_LATEX = ('The bitter yellow leaf exudate (latex), rich in anthraquinones such as aloin and aloe-emodin, acts as a stimulant '
            'laxative; the US FDA removed it from over-the-counter laxatives in 2002, and EFSA regards these compounds as a safety '
            'concern. Not for self-treatment.')
NOTES['aloe_vera'] = (
    'Searched PubMed ("Aloe vera" OR "Aloe barbadensis" tiab, aloe ti; 460 HT, 167 SR, 654 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (100) and OpenAlex. NEW pair ibd (Langmead 2004 double-blind RCT, ulcerative colitis, clinical response '
    'significant). IBS: Davis 2006 and Storsrud 2020 RCTs recorded as no-effect. Added: Dick 2016 glucose MA; 2022 radiation-'
    'dermatitis SR (14 RCTs, positive) + 2017 null RCT; diabetic-foot-ulcer RCT and Maenthaisong 2007 burn SR to wounds; '
    'three-arm placebo RCT for aphthous ulcers and 2026 gingival MA to oral-health. NEW pair bruising (2026 RCT, vein-harvest-site ecchymosis, found via Europe PMC). SAFETY: the oral-latex caution had NO source '
    '- now sourced to NCCIH (REF-5130, read 2026-11-24), EFSA 2018 hydroxyanthracene opinion, aloe gel food-tox review, '
    'aloe-emodin review, acute liver injury case, 60-day gel-juice liver study (PubMed lists the EFSA DOI on 33132775 by '
    'mistake; entry kept with PMID only), bezoar case; raised to warning; latex preparation sourced. Draft interaction: cardiac '
    'glycosides (caution, NCCIH). Bucket: 2021 umbrella review (phlebitis prevention best supported; no vocab condition), '
    'atrophic-vaginitis RCT and GERD pilot (active comparators only). Not added: retracted rat atopic-dermatitis paper; '
    'combination products (aloe+olive oil, aloe+chamomile+thyme, aloe+pineapple, polyherbal mouthwashes, colostrum+aloe); '
    'radiation proctitis RCTs (no vocab condition); hemorrhoidectomy-pain NMA (post-surgical pain, inconclusive); IBS trial '
    '24379854 (no abstract); periodontal adjunct trials vs active drugs.')

# ================================================================== lemon verbena
PLAN['aloysia_citrodora'] = [
    ('newpair', 'stress', ['REF-5122', 'REF-5121'],
     'Lemon verbena extract lowered perceived stress (with lower cortisol) vs placebo in two randomized trials, in adults and in '
     'adolescents'),
    ('add', 'insomnia', ['REF-5122', 'REF-5121']),
    ('note', 'insomnia', 'Improved sleep quality vs placebo in four randomized trials (people with insomnia, healthy adults, adults '
     'with stress, and adolescents with sleep and stress problems)'),
    ('add', 'anxiety', ['REF-5122', 'REF-5123']),
    ('nulladd', 'anxiety', ['REF-5124']),
    ('note', 'anxiety', 'Lemon verbena extract had an anxiolytic effect and lowered perceived stress vs placebo in a randomized '
     'trial, and inhaling its essential oil reduced anxiety before caesarean section; a single dose did not reduce anxiety before '
     'coronary angiography in another trial'),
    ('aadd', 'antioxidant', ['REF-5127']),
    ('refadd', ['REF-5128']),
]
POST['aloysia_citrodora'] = [
    ('ciadd', 'Safety in pregnancy and breastfeeding is not established', ['REF-5125', 'REF-5126']),
]
LV_PREG = ('Safety in pregnancy and breastfeeding is not established in people, so avoid medicinal doses; in mice, the leaf infusion '
           'and its main constituent verbascoside did not harm embryo development.')
NOTES['aloysia_citrodora'] = (
    'Searched PubMed ("Aloysia citrodora" / triphylla, "Lippia citriodora", "lemon verbena" tiab), Europe PMC, ClinicalTrials.gov '
    '(6) and OpenAlex. NEW pair stress (Nutrients 2022 RCT; adolescents double-blind RCT, Applied Sciences 2025, not in PubMed). '
    'Both also to insomnia. Anxiety: the 2022 RCT (anxiolytic effect) and a C-section aromatherapy RCT added; the lippia arm of a '
    'saffron/lippia RCT before coronary angiography recorded as no-effect. Funes 2011 exercise RCT to antioxidant (muscle-damage '
    'markers, not soreness). Mouse teratogenicity studies (no harm) added to the pregnancy caution. Bucket: 2026 cardiometabolic MA '
    '(pools combined hibiscus + lemon verbena formulations; benefit larger with combinations, so not attributed to lemon verbena '
    'alone). WRONG SPECIES rejected: 39286661 "Lemon Verbena (Cymbopogon citratus)" oral candidiasis SR - that is lemongrass. Not '
    'added: hibiscus + lemon verbena combination RCTs (appetite, weight, skin), lemon verbena + omega-3 joint RCT, Mother\'s Milk '
    'tea, ADHD-symptom RCT in children (no vocab condition).')


def text_edits():
    path = 'plants/alchemilla_vulgaris.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    b = d['botanical_description']
    b.update(text=LM_BOT, height='About a foot (30 cm)', leaves='Lower leaves 6-8 inches across, kidney-shaped, cut into seven or '
             'mostly nine broad shallow lobes, finely toothed; upper leaves stalkless or short-stalked',
             flowers='Numerous tiny (1/8 inch) yellow-green flowers without petals, four stamens, in loose clusters',
             root='Short, stout, black perennial rootstock', flowering_period='June-August', reference_ids=['REF-3192'])
    for k in ('fruit', 'stem'):
        b.pop(k, None)
    d['habitat'].update(text=LM_HAB, reference_ids=['REF-3192', 'REF-0208'])
    d['harvesting'].update(text=LM_HARV, season='June and July (in flower)', reference_ids=['REF-3192'], status='verified')
    d['traditional_uses'].update(text=LM_TRAD, reference_ids=['REF-3192', 'REF-0113'])
    p = [x for x in d['preparations'] if x['name'] == 'Infusion']; assert len(p) == 1
    p[0].update(text=LM_INF, reference_ids=['REF-3192', 'REF-0113'])
    ds = [x for x in d['dosage'] if x['name'] == 'Infusion']; assert len(ds) == 1
    ds[0].update(text=LM_DOSE, reference_ids=['REF-3192'], status='verified')
    c = [x for x in d['contraindications'] if x['note'].startswith('Generally considered very safe')]; assert len(c) == 1
    c[0]['reference_ids'] = [r for r in c[0]['reference_ids'] if r != 'REF-0208']; c[0]['status'] = 'needs-review'
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/allium_sativum.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'].startswith('Garlic is generally very safe')]; assert len(c) == 1
    assert '(National Center for Complementary and Integrative Health, 2021)' in c[0]['note']
    for x in d['contraindications']:   # REF-0209 is the POWO taxon page: it states nothing about safety
        x['reference_ids'] = [r for r in x['reference_ids'] if r != 'REF-0209']
    c[0]['note'] = c[0]['note'].replace('(National Center for Complementary and Integrative Health, 2021)',
                                        '(National Center for Complementary and Integrative Health, 2025)').replace('–', '-')
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/aloe_vera.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'].startswith('Topical use of aloe gel is generally safe')]; assert len(c) == 1
    c[0].update(note=AL_CAUTION, severity='warning', status='verified')
    p = [x for x in d['preparations'] if x['name'] == 'Latex/dried juice']; assert len(p) == 1
    p[0].update(text=AL_LATEX, status='verified')
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/aloysia_citrodora.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'].startswith('Safety in pregnancy and breastfeeding')]; assert len(c) == 1
    c[0]['note'] = LV_PREG
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})
    for s in (LM_BOT, LM_HARV, LM_HAB, LM_TRAD, LM_INF, LM_DOSE, AL_CAUTION, AL_LATEX, LV_PREG):
        assert '—' not in s and '–' not in s


def pubmed_urls():
    """Campaign entries (REF-5001+) with a pmid but no doi/url get the PubMed url."""
    lines = open('bibliography.bibtex', encoding='utf-8', newline='').read().split('\n')
    out, entry, n = [], [], 0
    for ln in lines:
        entry.append(ln)
        if ln == '}':
            body = '\n'.join(entry)
            m = re.search(r'note\s*=\s*\{REF-(\d+)\}', body)
            pm = re.search(r'pmid\s*=\s*\{(\d+)\}', body)
            if m and int(m.group(1)) >= 5001 and pm and not re.search(r'^\s*(doi|url)\s*=', body, re.M):
                i = next(k for k, x in enumerate(entry) if re.match(r'\s*pmid\s*=', x))
                entry.insert(i + 1, f'  url      = {{https://pubmed.ncbi.nlm.nih.gov/{pm.group(1)}/}},'); n += 1
            out.extend(entry); entry = []
    out.extend(entry)
    open('bibliography.bibtex', 'w', encoding='utf-8', newline='').write('\n'.join(out))
    return n


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r02_changes.tsv')
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
