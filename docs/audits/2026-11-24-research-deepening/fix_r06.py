"""Research-deepening batch 6 (borago-officinalis, boswellia-serrata, calendula-officinalis, camellia-sinensis,
campanula-persicifolia). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5205.. (reserved)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 6'

SPEC = [
    ('REF-5205', '21328257', 'cochraneherbalra', 'systematic-review'),
    ('REF-5206', '10233322', 'borageoileczemamulticentre', 'rct'),
    ('REF-5207', '9244815', 'borageoilchildreneczema', 'rct'),
    ('REF-5208', '17513402', 'glaweightregain', 'rct'),
    ('REF-5209', '33534427', 'borageoilpostmenopausal', 'rct'),
    ('REF-5210', '21387119', 'borageoilstatusepilepticus', 'clinical'),
    ('REF-5211', '35342437', 'olibanumaphthous', 'rct'),
    ('REF-5212', '16364338', 'frankincensecyp', 'preclinical'),
    ('REF-5213', '38922237', 'boswelliasiadh', 'clinical'),
    ('REF-5214', '25233607', 'warfarinherbs', 'narrative-review'),
    ('REF-5215', '23497687', 'calendulamucositis', 'rct'),
    ('REF-5216', '23245940', 'calendulavsaqueouscream', 'rct'),
    ('REF-5217', '32460565', 'calendulaepisiotomy', 'rct'),
    ('REF-5218', '30598929', 'calendulacesarean', 'rct'),
    ('REF-5219', '21164072', 'cirmarigold', 'narrative-review'),
    ('REF-5220', '29580974', 'greenteasafety', 'systematic-review'),
    ('REF-5221', '18484782', 'uspgreenteaextracts', 'systematic-review'),
    ('REF-5222', '32812270', 'greenteaacne', 'meta-analysis'),
    ('REF-5223', '34209247', 'catechinsinfluenza', 'meta-analysis'),
    ('REF-5224', '39809182', 'greenteat2dm', 'meta-analysis'),
    ('REF-5225', '32670385', 'greenteaglycaemic', 'meta-analysis'),
    ('REF-5226', '40314930', 'teatheaninecognition', 'meta-analysis'),
]


def _mskcc(rid, herb, slug, year, updated, summary):
    return (rid, [('author', 'Memorial Sloan Kettering Cancer Center'), ('title', f'{herb} (About Herbs)'), ('year', year),
                  ('url', f'https://www.mskcc.org/cancer-care/integrative-medicine/herbs/{slug}'), ('note', rid),
                  ('study_type', 'traditional'),
                  ('summary', f'MSKCC About Herbs, last updated {updated}, read 2026-11-24. ' + summary)])


WEB = {
    'mskcc2023borage': _mskcc('REF-5227', 'Borage', 'borage', '2023', '26 September 2023',
        'Contains small amounts of hepatotoxic unsaturated pyrrolizidine alkaloids; the oil should be certified free of them; '
        'chronic use should be avoided, especially in liver disease, pregnancy and breastfeeding; possible liver damage with '
        'prolonged use; status epilepticus reported in a woman after one week of borage oil; may increase bleeding risk with '
        'anticoagulants such as warfarin (extrapolated from a small evening primrose GLA study); may cause birth defects, '
        'premature labour or infant methaemoglobinaemia.'),
    'mskcc2026boswellia': _mskcc('REF-5228', 'Boswellia', 'boswellia', '2026', '3 September 2026',
        'Generally well tolerated. Herb-drug interactions: extracts can inhibit platelet aggregation and may increase bleeding '
        'risk with anticoagulant or antiplatelet drugs (clinical significance not determined); in vitro, boswellic acids '
        'modulate the OATP1B3 and MRP2 transporters and inhibit P-glycoprotein (clinical relevance not known). Adverse '
        'reactions: allergic contact dermatitis from oil and cream, a gastric bezoar after excessive frankincense intake.'),
    'mskcc2025calendula': _mskcc('REF-5229', 'Calendula', 'calendula', '2025', '23 May 2025',
        'Avoid during pregnancy and lactation because safety data are lacking; calendula is known to cause allergic '
        'reactions; do not take if allergic to plants in the daisy family; generally safe in food and tea; no herb-drug '
        'interactions listed.'),
    'mskcc2026greentea': _mskcc('REF-5230', 'Green Tea', 'green-tea', '2026', '12 August 2026',
        'Adverse reactions: elevated liver enzymes with green tea extract 800 mg or EGCG 843-1600 mg daily and hepatotoxicity '
        'with high-EGCG extracts (USP: do not use with a liver problem; stop if signs of liver trouble). Herb-drug '
        'interactions: very large amounts (0.5-1 gallon a day) may supply enough vitamin K to antagonise anticoagulants; '
        'EGCG can inhibit the effect of bortezomib; extract inhibits CYP3A4; lowered rosuvastatin exposure in healthy '
        'volunteers; reduces nadolol absorption (OATP1A2); case reports with ziprasidone and nadolol.'),
}


def bib_new():
    new = deep_lib.newrefs(SPEC)
    new.update(WEB)
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== borage
PLAN['borago_officinalis'] = [
    ('add', 'arthritis', ['REF-5205']),
    ('note', 'arthritis', 'Borage seed oil (gamma-linolenic acid) reduced rheumatoid arthritis signs and symptoms vs placebo '
     'in a 24-week randomized trial; a Cochrane review found moderate evidence that GLA-containing oils, including borage oil, '
     'relieve rheumatoid arthritis symptoms'),
    ('nulladd', 'eczema', ['REF-5206', 'REF-5207']),
    ('note', 'eczema', 'Undershirts coated with borage oil eased itch and redness of mild atopic dermatitis in a small '
     'placebo-controlled trial; oral borage oil did not help eczema (Cochrane review and three placebo-controlled trials)'),
    ('newpair', 'high-blood-pressure', ['REF-5209'],
     'Borage oil (1 g a day, with vitamin E) lowered systolic and diastolic blood pressure more than vitamin E alone over 6 '
     'months in a double-blind randomized trial in postmenopausal women with hypertension'),
    ('newpair', 'metabolic-support', ['REF-5208', 'REF-5209'],
     'Borage oil reduced weight regain after major weight loss over a year in a double-blind randomized trial and reduced '
     'waist-to-hip ratio in postmenopausal women with hypertension; it did not change metabolic rate in overweight young adults'),
    ('nulladd', 'metabolic-support', ['REF-3461']),
]
POST['borago_officinalis'] = [
    ('ciadd', 'Pyrrolizidine alkaloids (PAs)', ['REF-5227']),
    ('cinew', {'note': 'Seizures: a previously healthy woman developed status epilepticus (continuous seizures) after taking '
                       'borage oil for one week (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5210', 'REF-5227']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'insufficient',
                'mechanism': 'Memorial Sloan Kettering notes that borage oil may increase bleeding risk with blood thinners '
                             'such as warfarin; this is extrapolated from a small study of gamma-linolenic acid from evening '
                             'primrose, not from studies of borage itself.',
                'reference_ids': ['REF-5227']}),
]
NOTES['borago_officinalis'] = (
    'Searched PubMed (Borago officinalis / borage oil / borage seed oil tiab, borage ti), Europe PMC, ClinicalTrials.gov (17) '
    'and OpenAlex. Added: Cochrane 2011 herbal therapy for RA (moderate evidence for GLA oils incl. borage) to arthritis; '
    'Henz 1999 multicentre RCT and a 1997 children RCT (both no effect) as no-effect for eczema; NEW high-blood-pressure pair '
    '(2021 Menopause RCT, borage oil + vitamin E vs vitamin E, 96 women, BP and waist-hip ratio fell); NEW metabolic-support '
    'pair (Schwartz 2007 J Nutr double-blind RCT vs olive oil, weight regain 2.2 vs 8.8 kg at 1 year; plus the 2021 trial), '
    'with REF-3461 (no effect on metabolic rate) recorded as no-effect. Safety: status epilepticus case (new caution); MSKCC '
    'About Herbs (REF-5227) added to the PA warning; new DRAFT anticoagulant interaction (insufficient, extrapolated from '
    'evening primrose GLA; needs owner sign-off). Considered, not added: Cochrane 2012 dietary supplements for eczema '
    '(excludes borage), GLA prophylaxis trial (only a trend), functional-textile MA (erythema only), acne RCT (abstract does '
    'not give the comparison with the control group), flax/borage skin study (within-group changes), borage + green tea + '
    'purslane and other combinations, Borage plus syrup (COVID), platelet study 1997 (no abstract), LactMed (bot check).')

# ================================================================== boswellia
PLAN['boswellia_serrata'] = [
    ('newpair', 'oral-health', ['REF-5211'],
     'Frankincense (Boswellia serrata resin) extract tablets shrank mouth ulcers and eased their pain more than placebo in a '
     'double-blind randomized trial'),
]
BS_OLD = ('Boswellic acids can affect drug-metabolising enzymes, so caution is advised when taking other medicines; safety in '
          'pregnancy and breastfeeding is not established, so avoid medicinal doses.')
BS_CYP = ('In laboratory tests, Boswellia serrata resin extract inhibited the main drug-metabolising enzymes (CYP1A2, 2C8, '
          '2C9, 2C19, 2D6 and 3A4), and boswellic acids affected drug transporters such as P-glycoprotein, so caution is '
          'advised when taking other medicines.')
BS_PREG = 'Safety in pregnancy and breastfeeding is not established, so avoid medicinal doses.'
POST['boswellia_serrata'] = [
    ('cinew', {'note': 'High doses: a woman taking 1,000 mg a day of Boswellia serrata capsules for 3 weeks had a seizure caused '
                       'by very low blood sodium (inappropriate antidiuretic hormone secretion), which resolved after stopping '
                       '(case report).',
               'severity': 'caution', 'reference_ids': ['REF-5213']}),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'In laboratory tests, Boswellia serrata resin extract inhibited CYP3A4 and the other main '
                             'drug-metabolising enzymes; no human study has tested whether this changes drug levels.',
                'reference_ids': ['REF-5212']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'Boswellia extracts inhibit platelets in laboratory tests and may increase bleeding risk with '
                             'blood thinners (Memorial Sloan Kettering); a 2014 review of warfarin interactions lists Boswellia '
                             'serrata among herbs linked to serious adverse events in case reports. The clinical significance '
                             'is not established.',
                'reference_ids': ['REF-5228', 'REF-5214']}),
]
NOTES['boswellia_serrata'] = (
    'Searched PubMed (Boswellia serrata / Indian frankincense / Indian olibanum tiab; Boswellia, boswellic acid(s), AKBA ti), '
    'Europe PMC, ClinicalTrials.gov (65), OpenAlex, and a targeted PubMed search for CYP / P-gp / interaction studies. Arthritis '
    'and pain are already at 10; further OA RCTs and the 2024 Aflapin MA were not added (no change). NEW oral-health pair: '
    '2022 Isfahan placebo RCT of olibanum orally disintegrating tablets for aphthous ulcers. SAFETY: the drug-enzyme caution '
    'had no source; split into a verified CYP/P-gp note (Frank & Unger 2006 in vitro CYP panel, REF-5212; MSKCC REF-5228) and '
    'the unsourced pregnancy line (stays needs-review); SIADH/seizure case at 1,000 mg/day (new caution); two DRAFT '
    'interactions (CYP3A4 insufficient; anticoagulants caution, MSKCC + 2014 warfarin review), need owner sign-off. '
    'Considered, not added: gingivitis RCT 2011 (frankincense alone not better than scaling alone), Memowell (K-Vie plus '
    'other ingredients) Alzheimer trial, Inflawell COVID syrup (formulation), collagenous colitis Cochrane (near-miss for '
    'IBD), B. carteri burn and episiotomy trials (other species, combinations), curcumin + boswellia and other mixtures, '
    'photoaged-skin, stroke and Parkinson trials (no vocab condition).')

# ================================================================== calendula
PLAN['calendula_officinalis'] = [
    ('newpair', 'oral-health', ['REF-5215', 'REF-3065'],
     'A calendula flower extract mouthwash reduced radiotherapy-induced mouth and throat inflammation (mucositis) more than '
     'placebo in a randomized trial; traditionally used for minor inflammations of the mouth and throat (EU herbal monograph)'),
    ('add', 'wounds', ['REF-5217', 'REF-5218']),
    ('note', 'wounds', 'Calendula sped healing of hand wounds, episiotomy and caesarean wounds and, taken orally, of '
     'second-degree burns in randomized trials; a systematic review found some benefit, though trials in burns and diabetic '
     'ulcers did not'),
    ('nulladd', 'skin-irritation', ['REF-5216']),
    ('note', 'skin-irritation', 'Calendula cream prevented radiation dermatitis better than trolamine and essential fatty acids '
     'in randomized trials and helped diaper and contact dermatitis; two trials found no difference from a standard '
     'moisturiser'),
    ('refadd', ['REF-5229']),
]
CO_OLD = ('Generally very safe for topical use. May cause contact dermatitis in rare cases (Asteraceae family allergy). Internal '
          'use is safe in normal doses. Avoid during pregnancy at therapeutic doses (uterine stimulant potential). Generally safe '
          'during breastfeeding for topical use.')
CO_NEW = ('Do not use if allergic to plants of the daisy family (Asteraceae); skin sensitisation (contact allergy) has been '
          'reported, and about 2 in 100 people in a clinic series of patch tests reacted to marigold. Not recommended in '
          'pregnancy or breastfeeding because safety has not been established, nor as a medicine for children under 6 '
          '(on the skin) or under 12 (mouth and throat) (EU herbal monograph). Calendula in food and tea is generally '
          'considered safe, and cosmetic ingredients from the flower were not irritating or sensitising in tests.')
NOTES['calendula_officinalis'] = (
    'Searched PubMed (Calendula officinalis / pot marigold tiab, calendula ti), Europe PMC, ClinicalTrials.gov (27) and '
    'OpenAlex. Added: NEW oral-health pair (Babaee 2013 placebo RCT, radiation oropharyngeal mucositis; EU monograph '
    'REF-3065 traditional indication 2); episiotomy (2022) and caesarean (2018) RCTs to wounds; Sharp 2013 RCT (Weleda '
    'calendula vs Essex aqueous cream, no difference) recorded as no-effect for skin irritation. SAFETY: the main caution '
    'rested on Hoffmann (REF-0112, unreadable) and a rat wound study (REF-0199) and said "internal use is safe", "uterine '
    'stimulant" and "safe in breastfeeding", none of which a readable source states. Rewritten from the EU monograph '
    '(EMA/HMPC/437450/2017 PDF read 2026-11-24: Asteraceae contraindication, skin sensitisation, pregnancy and lactation not '
    'recommended, children), MSKCC About Herbs (REF-5229), the CIR 2010 amended safety assessment (REF-5219) and Reider '
    '2001 patch tests (REF-5176, 2.03% reacted to marigold); REF-0112/REF-0199 removed from both safety notes. Considered, '
    'not added: Leach 2008 wound SR (superseded by the 2019 SR REF-0752), calendula vs metronidazole, lycopene, bentonite, '
    'olive oil and Bao Yuan Gao (active comparators only), combinations (Ayurvedic gel, suppositories, mouthwashes, COPD '
    'mix), 1974 anaphylaxis after gargling (no abstract), CIR 2001 (superseded by the 2010 amended report).')

# ================================================================== tea
PLAN['camellia_sinensis'] = [
    ('add', 'blood-sugar', ['REF-5224', 'REF-5225']),
    ('note', 'blood-sugar', 'Green tea lowered fasting glucose and HbA1c in a meta-analysis of 17 trials and in a 2024 '
     'meta-analysis in type 2 diabetes; a 2020 meta-analysis found lower fasting glucose but no change in HbA1c, and a 2021 '
     'meta-analysis limited to type 2 diabetes found no significant effect'),
    ('add', 'cognitive-function', ['REF-5226']),
    ('note', 'cognitive-function', 'L-theanine, an amino acid found in tea, increased brain alpha activity linked to relaxed '
     'alertness in a small trial, and a 2025 meta-analysis found that L-theanine, alone or with caffeine, could benefit '
     'cognition and mood (compound evidence)'),
    ('newpair', 'acne', ['REF-5222'],
     'Green tea extract applied to the skin reduced acne lesions in a meta-analysis of randomized trials; taken by mouth it had '
     'little effect'),
    ('newpair', 'cold', ['REF-5223'],
     'Green tea catechins, gargled or taken by mouth, lowered the risk of catching influenza in a meta-analysis of studies'),
]
CS_OLD = ('Generally safe in moderate consumption. High caffeine intake may cause insomnia, anxiety, palpitations, or dependence. '
          'Large amounts of green tea extract supplements may be hepatotoxic (rare). May reduce iron absorption if consumed with '
          'meals. Avoid very high supplement doses during pregnancy.')
CS_NEW = ('Generally safe in moderate consumption. High caffeine intake may cause insomnia, anxiety, palpitations, or dependence. '
          'May reduce iron absorption if consumed with meals. Avoid very high supplement doses during pregnancy.')
POST['camellia_sinensis'] = [
    ('cinew', {'note': 'Liver injury: concentrated, catechin-rich green tea extracts taken as large single doses (tablets or '
                       'capsules, especially on an empty stomach) have caused liver injury in a dose-dependent way, while '
                       'brewed tea and tea in food or drinks did not. A safe intake of 338 mg EGCG a day has been proposed '
                       'for such supplements. Do not use extracts with a liver problem, and stop if signs of liver trouble '
                       'appear.',
               'severity': 'warning', 'reference_ids': ['REF-5220', 'REF-5221', 'REF-5230']}),
    ('dcinew', {'drug_class': 'chemotherapy-agents', 'severity': 'caution',
                'mechanism': 'EGCG and other green tea polyphenols can block the anticancer effect of bortezomib '
                             '(Memorial Sloan Kettering), so concentrated green tea products are best avoided during treatment '
                             'with it.',
                'reference_ids': ['REF-5230']}),
    ('dcinew', {'drug_class': 'statins', 'severity': 'caution',
                'mechanism': 'Green tea significantly lowered blood levels of rosuvastatin in healthy volunteers (Memorial '
                             'Sloan Kettering), which could weaken its cholesterol-lowering effect.',
                'reference_ids': ['REF-5230']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'insufficient',
                'mechanism': 'Very large amounts of green tea (about half to one gallon a day) may supply enough vitamin K to '
                             'weaken warfarin-type blood thinners (Memorial Sloan Kettering), and a 2014 review of warfarin '
                             'interactions lists Camellia sinensis among herbs in case reports of serious adverse events.',
                'reference_ids': ['REF-5230', 'REF-5214']}),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'Green tea extract inhibits the drug-metabolising enzyme CYP3A4 (Memorial Sloan Kettering); '
                             'whether ordinary tea drinking changes the levels of CYP3A4 medicines is not established.',
                'reference_ids': ['REF-5230']}),
]
NOTES['camellia_sinensis'] = (
    'Searched PubMed (Camellia sinensis tiab; green tea, black tea, tea extract, tea catechins, EGCG ti: 1,006 HT, 240 SR, '
    '1,798 SAFE hits; only SR/MA and safety were read in depth), Europe PMC, ClinicalTrials.gov (292) and OpenAlex. Added: '
    'two glycaemic MAs (2024 T2DM positive, 2020 fasting glucose only) to blood-sugar; 2025 tea / L-theanine cognition MA to '
    'cognitive-function (compound evidence); NEW acne pair (2021 MA: topical extract effective, oral not); NEW cold pair '
    '(2021 catechin influenza-prevention MA, RR 0.62). SAFETY: the extract hepatotoxicity sentence cited only a 2010 benefits '
    'review and an L-theanine RCT (REF-0184, which states nothing on safety); moved to a new liver-injury warning sourced to '
    'Hu 2018 SR (338 mg EGCG/day), USP 2008 SR and MSKCC Green Tea (REF-5230); REF-0184 removed from both safety notes. Four '
    'DRAFT interactions from MSKCC (bortezomib, rosuvastatin, vitamin K / warfarin with the 2014 review, CYP3A4), need owner '
    'sign-off. NOT ADDED as pairs because they conflict with the record\'s own cautions (inv. 12d): insomnia and '
    'stress/anxiety (L-theanine SRs; tea caffeine causes insomnia and anxiety), liver support (2024 MA improved liver enzymes; '
    'extracts cause liver injury). Also not added: periodontitis MAs (very low certainty / insufficient), halitosis SR (two '
    'studies, before-after only), inflammatory-marker MA (TNF-alpha only, CRP and IL-6 unchanged), observational cancer, '
    'stroke and depression MAs (associations, not treatment), black-tea cholesterol MAs (already covered at 8).')

# ================================================================== peach-leaved bellflower
PLAN['campanula_persicifolia'] = []
NOTES['campanula_persicifolia'] = (
    'Searched PubMed (Campanula persicifolia / peach-leaved / peach-leaf bellflower tiab): 0 hits in every family; Europe '
    'PMC, ClinicalTrials.gov (0) and OpenAlex (26 works, all ecology, pollination and horticulture). No medicinal study of '
    'this species exists. Settled.')


def _swap(d, old, new, drop=(), add=(), **upd):
    c = [x for x in d['contraindications'] if x['note'] == old]
    assert len(c) == 1, old[:50]
    assert '—' not in new and '–' not in new
    c[0]['note'] = new
    c[0]['reference_ids'] = [r for r in c[0]['reference_ids'] if r not in drop] + [r for r in add if r not in c[0]['reference_ids']]
    c[0].update(upd)
    return c[0]


def text_edits():
    path = 'plants/boswellia_serrata.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'] == BS_OLD]; assert len(c) == 1
    i = d['contraindications'].index(c[0])
    c[0]['note'] = BS_PREG
    d['contraindications'].insert(i, {'note': BS_CYP, 'severity': 'caution', 'reference_ids': ['REF-5212', 'REF-5228'],
                                      'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/calendula_officinalis.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    _swap(d, CO_OLD, CO_NEW, drop=('REF-0112', 'REF-0199'), add=('REF-3065', 'REF-5229', 'REF-5219', 'REF-5176'),
          status='verified')
    duke = [x for x in d['contraindications'] if x['note'].startswith('Duke (2002) rates calendula')]; assert len(duke) == 1
    duke[0]['reference_ids'] = [r for r in duke[0]['reference_ids'] if r not in ('REF-0112', 'REF-0199')]
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/camellia_sinensis.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    _swap(d, CS_OLD, CS_NEW, drop=('REF-0184',))
    duke = [x for x in d['contraindications'] if x['note'].startswith('Duke (2002) rates tea')]; assert len(duke) == 1
    duke[0]['reference_ids'] = [r for r in duke[0]['reference_ids'] if r != 'REF-0184']
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r06_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
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
