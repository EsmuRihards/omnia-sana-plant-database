"""Deep audit of batch 15 (rubus-idaeus .. schisandra-chinensis): 2nd-pass strict-match + deep checks. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3735..REF-3762 (Grieve x2 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib
import yamlsplice as Y

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3735', '33563275', 'raspberrypregnancysr', 'systematic-review'),
    ('REF-3736', '11406860', 'willowoa2001', 'rct'),
    ('REF-3737', '15517622', 'willowoara2004', 'rct'),
    ('REF-3738', '11752510', 'willowrofecoxib', 'rct'),
    ('REF-3739', '39672763', 'chiabp2025', 'meta-analysis'),
    ('REF-3740', '39299654', 'chiacardiometabolic', 'meta-analysis'),
    ('REF-3741', '25403867', 'chiabp2014', 'rct'),
    ('REF-3742', '33530854', 'chiat2dbp', 'rct'),
    ('REF-3743', '19628108', 'chiaweight2009', 'rct'),
    ('REF-3744', '37489230', 'sagehotflashes', 'meta-analysis'),
    ('REF-3745', '30572339', 'sagepms', 'rct'),
    ('REF-3746', '21506190', 'sagehyperlipidemia', 'rct'),
    ('REF-3747', '24050577', 'saget2d', 'rct'),
    ('REF-3748', '18350281', 'sagememoryolder', 'rct'),
    ('REF-3749', '16205785', 'sagemood', 'rct'),
    ('REF-3750', '16504956', 'sagepharyngitis', 'rct'),
    ('REF-3751', '12605619', 'sagealzheimer', 'rct'),
    ('REF-3752', '17713873', 'sageuverythema', 'rct'),
    ('REF-3753', '36343423', 'rosemarymdd', 'rct'),
    ('REF-3754', '37758539', 'rosemarycopdcognition', 'rct'),
    ('REF-3755', '36028878', 'rosemaryepisiotomy', 'rct'),
    ('REF-3756', '30970057', 'rosemarytoothpaste', 'rct'),
    ('REF-3757', '38242798', 'rosemaryanxietysurgery', 'rct'),
    ('REF-3758', '33827515', 'elderberrysr', 'systematic-review'),
    ('REF-3759', '32929634', 'elderberryinfluenza', 'rct'),
    ('REF-3760', '27023596', 'elderberrytravellers', 'rct'),
])
NEW['grieve1931sorrel'] = ('REF-3761', [
    ('author', 'Grieve, M'), ('title', 'Sorrel, Common (Rumex acetosa) - A Modern Herbal'), ('year', '1931'),
    ('url', 'https://www.botanical.com/botanical/mgmh/s/sorcom64.html'), ('note', 'REF-3761'), ('study_type', 'traditional'),
    ('summary', 'Grieve, A Modern Herbal (1931), Common Sorrel entry. Medicinal action: refrigerant and diuretic, a cooling drink in febrile disorders; for scurvy; the juice with vinegar for ringworm; root and seed formerly esteemed as astringent. Read 2026-11-13.')])
NEW['grieve1931soapwort'] = ('REF-3762', [
    ('author', 'Grieve, M'), ('title', 'Soapwort (Saponaria officinalis) - A Modern Herbal'), ('year', '1931'),
    ('url', 'https://www.botanical.com/botanical/mgmh/s/soawor61.html'), ('note', 'REF-3762'), ('study_type', 'traditional'),
    ('summary', 'Grieve, A Modern Herbal (1931), Soapwort entry. Medicinal action: tonic, diaphoretic and alterative; a decoction for the itch; for rheumatism and skin troubles, jaundice and visceral obstructions. Read 2026-11-13.')])

NEW['national2024elderberry'] = ('REF-3763', [
    ('author', 'National Center for Complementary and Integrative Health (NCCIH)'), ('title', 'Elderberry: Usefulness and Safety'),
    ('year', '2024'), ('url', 'https://www.nccih.nih.gov/health/elderberry'), ('note', 'REF-3763'), ('study_type', 'traditional'),
    ('summary', 'NCCIH fact sheet (last updated November 2024). Raw or unripe elderberries and other parts of the elder tree such as the leaves and stem contain cyanide-producing substances that can cause nausea, vomiting and severe diarrhoea; cooking eliminates the toxin. Little is known about safety in pregnancy or breastfeeding. Preliminary research suggests elderberry may relieve flu, cold or other upper respiratory symptoms. Read 2026-11-13.')])

ELDER_CI = ('Raw or unripe elderberries and the leaves and stems contain cyanide-producing substances that can cause nausea, '
            'vomiting and severe diarrhoea; cooking the berries eliminates the toxin, and large amounts may cause serious illness (NCCIH). '
            'Use in pregnancy and breastfeeding is not recommended because safety has not been established (EU herbal monograph; NCCIH). '
            'Do not use if allergic to elder. If you take any medicine, talk with your health care provider first, as some herbs and medicines interact (NCCIH).')

BIB = dict(
    retag={'REF-0497': 'clinical', 'REF-0498': 'clinical', 'REF-2574': 'narrative-review',
           'REF-0897': 'narrative-review', 'REF-0898': 'narrative-review',
           'REF-0424': 'narrative-review', 'REF-0425': 'narrative-review', 'REF-2590': 'narrative-review', 'REF-2591': 'narrative-review',
           'REF-0503': 'narrative-review', 'REF-0173': 'rct', 'REF-1286': 'narrative-review',
           'REF-1015': 'narrative-review', 'REF-1018': 'narrative-review', 'REF-1020': 'narrative-review', 'REF-1021': 'narrative-review',
           'REF-0505': 'narrative-review', 'REF-0583': 'narrative-review', 'REF-0506': 'systematic-review'},
    delete=['REF-1260'],   # 2006 Cochrane LBP review, superseded by the 2014 update REF-1261 (withdrawn/superseded rule)
    new=NEW)

PLAN = {
    'rubus_idaeus': [
        ('rm', 'menstrual-cramps', ['REF-1541', 'REF-2575']),   # guinea-pig ileum relaxation; endometriosis rats - neither names cramps
        ('arm', 'antidiarrheal', ['REF-0497']), ('arm', 'astringent', ['REF-0497']),
        ('arm', 'emmenagogue', ['REF-0498', 'REF-0607', 'REF-1541']), ('refadd', ['REF-0498', 'REF-1541', 'REF-2575']),
        ('nulladd', 'pregnancy-support', ['REF-0607', 'REF-3735']),
        ('note', 'pregnancy-support', 'Widely used to prepare for labour: an observational study linked it to less labour augmentation, but a randomized trial found it did not shorten labour, and reviews judge the evidence weak, with a possible negative effect on cervical ripening'),
        ('newpair', 'arthritis', ['REF-1538'], 'A raspberry leaf extract relieved knee osteoarthritis pain vs placebo in a randomized trial'),
    ],
    'rumex_acetosa': [('arm', a, ['REF-0897']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant')]
                     + [('arm', a, ['REF-0898']) for a in ('anti-inflammatory', 'antioxidant', 'digestive')] + [
        ('refadd', ['REF-0897', 'REF-0898']),   # genus-level Rumex reviews
        ('rm', 'wounds', ['REF-0897']),
        ('rm', 'arthritis', ['REF-0048', 'REF-0098']), ('rm', 'bloating', ['REF-0048', 'REF-0098']), ('rm', 'indigestion', ['REF-0048', 'REF-0098']),
        ('rm', 'uti', ['REF-0048', 'REF-0098']), ('rm', 'wounds', ['REF-0048', 'REF-0098']),
        ('drop', 'urinary-support'),   # Grieve's "gravel and stone in the kidneys" vs the record's own oxalate / kidney-stone warning
        ('add', 'infection', ['REF-3761']), ('add', 'skin-irritation', ['REF-3761']), ('add', 'swelling', ['REF-3761']),
        ('note', 'infection', 'Juice with vinegar was a traditional cure for ringworm (Grieve, A Modern Herbal); its compounds were active against stomach Helicobacter pylori in the lab (preclinical)'),
        ('note', 'skin-irritation', 'Traditionally applied for ringworm and skin complaints (Grieve, A Modern Herbal)'),
        ('note', 'swelling', 'Traditional diuretic (Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Traditionally used to cool inflammation (old herbal quoted in Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Its compounds were active against stomach Helicobacter pylori in the lab (preclinical)'),
    ],
    'ruscus_aculeatus': [
        ('rm', 'pain', ['REF-0424', 'REF-0425', 'REF-0595']), ('rm', 'varicose-veins', ['REF-0595']), ('rm', 'swelling', ['REF-0424']),
        ('arm', 'venotonic', ['REF-0595', 'REF-1555', 'REF-1556', 'REF-1560']), ('arm', 'anti-oedematous', ['REF-1556']),
        ('refadd', ['REF-0595', 'REF-1555', 'REF-1556', 'REF-1560']),   # Ruscus + hesperidin + vitamin C (or other) combinations
        ('add', 'varicose-veins', ['REF-1554']), ('add', 'swelling', ['REF-1554']),
        ('note', 'varicose-veins', 'Butcher\'s broom extract reduced leg volume and swelling vs placebo in women with chronic venous insufficiency in a randomized trial; used for venous insufficiency and varicose veins (reviews)'),
        ('note', 'swelling', 'Butcher\'s broom extract reduced lower-leg volume and ankle swelling vs placebo in chronic venous insufficiency in a randomized trial'),
        ('note', 'hemorrhoids', 'Used for haemorrhoid symptoms (reviews)'),
    ],
    'salix_alba': [
        ('rm', 'inflammation', ['REF-0529', 'REF-0592', 'REF-0530']),
        ('arm', 'anti-inflammatory', ['REF-1256']), ('refadd', ['REF-1256']),   # calves: ineffective on PGE2
        ('purge', 'REF-1260'),
        ('add', 'arthritis', ['REF-3736']), ('nulladd', 'arthritis', ['REF-3737']),
        ('add', 'back-pain', ['REF-3738']), ('add', 'pain', ['REF-3738']),
        ('note', 'arthritis', 'Willow bark extract eased osteoarthritis pain moderately vs placebo in one randomized trial but showed no relevant effect in another; traditional use for minor joint pain (EU herbal monograph)'),
        ('note', 'back-pain', 'Willow bark extract (about 240 mg salicin daily) relieved low back pain vs placebo and matched rofecoxib in randomized trials (moderate evidence; Cochrane review)'),
        ('note', 'pain', 'Willow bark relieved low back pain in randomized trials (moderate evidence) and eased osteoarthritis pain in some trials; traditional use for minor joint pain and headache (EU herbal monograph)'),
        ('note', 'headache', 'Traditional use for headache (EU herbal monograph)'),
        ('note', 'inflammation', 'inferred from anti-inflammatory action'),
    ],
    'salvia_hispanica': [('arm', a, ['REF-0297']) for a in ('anti-inflammatory', 'antioxidant', 'digestive')] + [
        ('null', 'cardiovascular-support', ['REF-1267', 'REF-1268']),
        ('add', 'cardiovascular-support', ['REF-3739', 'REF-3740']),
        ('note', 'cardiovascular-support', 'Chia lowered blood pressure in meta-analyses of trials; earlier reviews found no significant effect on most cardiovascular risk factors'),
        ('newpair', 'high-blood-pressure', ['REF-3739', 'REF-3740', 'REF-3741', 'REF-3742'], 'Chia lowered systolic and diastolic blood pressure in meta-analyses and in randomized trials in people with hypertension or type 2 diabetes'),
        ('nulladd', 'metabolic-support', ['REF-3743', 'REF-3739']),
        ('note', 'metabolic-support', 'Chia reduced the blood sugar rise after a meal and prolonged fullness in a randomized trial; it did not reduce body weight in trials or a meta-analysis'),
    ],
    'salvia_officinalis': [
        ('rm', 'cognitive-function', ['REF-1274']), ('rm', 'memory', ['REF-1274']),
        ('arm', 'neuroprotective', ['REF-1274']), ('refadd', ['REF-1274']),   # S. officinalis + S. lavandulaefolia mixture, mice
        ('add', 'cognitive-function', ['REF-3748', 'REF-3749', 'REF-3751']), ('add', 'memory', ['REF-3748', 'REF-3751']),
        ('note', 'cognitive-function', 'Sage extract improved cognition in mild to moderate Alzheimer\'s disease and memory, attention and mood in healthy people in randomized trials; a systematic review notes methodological weaknesses'),
        ('note', 'memory', 'Sage extract improved memory in healthy older adults and cognition in mild to moderate Alzheimer\'s disease in randomized trials'),
        ('add', 'hot-flashes', ['REF-3744']), ('add', 'menopause', ['REF-3744']),
        ('note', 'hot-flashes', 'Sage reduced hot flash frequency in a meta-analysis of trials; traditional use for excessive sweating (EU herbal monograph)'),
        ('note', 'menopause', 'Sage reduced menopausal hot flashes in a meta-analysis of trials; its extract had estrogen-like effects in rats (preclinical)'),
        ('add', 'sore-throat', ['REF-3750']),
        ('note', 'sore-throat', 'A 15% sage spray relieved acute pharyngitis vs placebo in a randomized trial; traditional gargle for mouth and throat inflammation (EU herbal monograph)'),
        ('newpair', 'pms', ['REF-3745'], 'Sage reduced the psychological and physical symptoms of PMS in a randomized trial'),
        ('newpair', 'high-cholesterol', ['REF-3746', 'REF-3747'], 'Sage leaf extract lowered total and LDL cholesterol and raised HDL vs placebo in randomized trials'),
        ('newpair', 'blood-sugar', ['REF-3747'], 'Sage leaves improved blood sugar control in hyperlipidaemic type 2 diabetes in a randomized trial'),
        ('newpair', 'skin-irritation', ['REF-3752'], 'A sage extract cream reduced UV-induced skin redness as much as hydrocortisone vs placebo in a randomized trial'),
    ],
    'salvia_rosmarinus': [('arm', a, ['REF-0173']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive')] + [
        ('drop', 'muscle-spasm'),   # smooth-muscle antispasmodic: off-target
        ('newpair', 'anxiety', ['REF-1291', 'REF-3753', 'REF-3757'], 'Rosemary reduced anxiety in randomized trials in students, in major depression as an add-on, and before surgery (aromatherapy)'),
        ('newpair', 'depression', ['REF-1291', 'REF-3753'], 'Rosemary reduced depression scores in randomized trials in students and as an add-on in major depression'),
        ('newpair', 'insomnia', ['REF-1291'], 'Rosemary improved sleep quality in university students in a randomized trial'),
        ('add', 'cognitive-function', ['REF-3754']),
        ('note', 'cognitive-function', 'Rosemary extract improved cognitive function in COPD patients in a randomized trial and memory in students; it improved cognition in animal studies (meta-analysis)'),
        ('note', 'memory', 'Rosemary improved prospective and retrospective memory in university students in a randomized trial; rosemary aroma improved memory quality; cognition improved in animal studies (meta-analysis)'),
        ('add', 'wounds', ['REF-3755']),
        ('note', 'wounds', 'A rosemary cream improved episiotomy wound healing in a randomized trial'),
        ('newpair', 'oral-health', ['REF-3756'], 'A rosemary toothpaste reduced gum bleeding and plaque vs conventional toothpaste in a randomized trial'),
        ('note', 'cardiovascular-support', 'Traditional use (Medical Herbalism)'),
    ],
    'sambucus_nigra': [
        ('rm', 'respiratory-support', ['REF-1018']),   # COVID pros/cons review warning of cytokine-storm risk - not evidence of benefit
        ('add', 'cold', ['REF-3760']), ('nulladd', 'cold', ['REF-3758', 'REF-3759']),
        ('nulladd', 'infection', ['REF-3759']), ('nulladd', 'respiratory-support', ['REF-3759']),
        ('note', 'cold', 'Traditional use for the early symptoms of colds (EU herbal monograph, elder flower); elderberry shortened colds in air travellers and eased flu symptoms in small trials and a meta-analysis, but a larger 2020 trial found no benefit in influenza and a systematic review called the evidence uncertain'),
        ('note', 'infection', 'Elderberry extract eased influenza symptoms in a small randomized trial, but a larger 2020 trial found no benefit; antiviral activity reviewed'),
        ('note', 'respiratory-support', 'Black elderberry reduced upper respiratory symptoms in a meta-analysis of small trials; a larger 2020 influenza trial found no benefit'),
        ('note', 'inflammation', 'Elderberry extracts reduced inflammatory and oxidative markers in cells (preclinical)'),
    ],
    'saponaria_officinalis': [
        ('drop', 'detox'),   # note described topical skin cleansing, not detox; re-added below on Grieve's 'alterative'
        ('newpair', 'detox', ['REF-3762'], 'Traditional alterative ("blood-cleansing") remedy (Grieve, A Modern Herbal)'),
        ('note', 'cough', 'Traditional expectorant for cough and bronchitis, now largely outdated; no scientific studies support it (MedicineNet; Drugs.com)'),
        ('note', 'bronchitis', 'Traditional expectorant for cough and bronchitis, now largely outdated; no scientific studies support it (MedicineNet; Drugs.com)'),
        ('note', 'respiratory-support', 'Traditional expectorant for respiratory complaints, now largely outdated; no scientific studies support it (MedicineNet; Drugs.com)'),
        ('note', 'eczema', 'Traditionally applied to eczema and other skin conditions; no scientific studies support it (MedicineNet)'),
    ],
    'schisandra_chinensis': [('rm', c, ['REF-0505']) for c in ('arthritis', 'cognitive-function', 'fatigue', 'muscle-soreness', 'stress')] + [
        ('rm', 'muscle-soreness', ['REF-0506']),
        ('note', 'cognitive-function', 'Adaptogens including schisandra improved cognition in a review with meta-analysis'),
        ('note', 'fatigue', 'Adaptogens including schisandra helped chronic fatigue in a review with meta-analysis; Russian studies report greater stamina (review)'),
        ('note', 'stress', 'Adaptogen for stress (review with meta-analysis; review of Russian research)'),
        ('note', 'liver-support', 'Schisandra protected the liver in animal and cell studies (reviews; preclinical)'),
        ('note', 'arthritis', 'Schisandra extract eased osteoarthritis in rats (preclinical)'),
    ],
}

NOTES = {
    'rubus_idaeus': 'Deep audit (2nd pass + deep). Menstrual-cramps dropped: its two cards (guinea-pig ileum relaxation; rat endometriosis) never name cramps. Pregnancy observational study REF-0497 (tagged rct; retagged clinical) removed from antidiarrheal/astringent; survey REF-0498 (retagged clinical), labour RCT REF-0607 (null) and REF-1541 removed from the emmenagogue action. REF-0607 and the 2021 SR REF-3735 ("evidence base weak") recorded as no-effect for pregnancy-support; REF-2574 retagged narrative-review. New pair (owner rule): arthritis (held knee OA RCT REF-1538).',
    'rumex_acetosa': 'Deep audit (2nd pass + deep). Chevallier REF-0048 and Grieve REF-0098 were pinned to all 10 pairs. Grieve\'s Sorrel entry (REF-3761, read 2026-11-13) names diuretic, febrile, scurvy, ringworm, kidney gravel - not rheumatism, bloating, indigestion, UTI or wounds; both refs removed from those pairs (Chevallier could not be checked). Arthritis, bloating, uti and wounds dropped. Urinary-support dropped: the record\'s own oxalate warning covers kidney and bladder stones. Genus reviews REF-0897/REF-0898 removed from actions. Not used: periodontal mouth-rinse RCT REF-0894 (no improvement in periodontal health).',
    'ruscus_aculeatus': 'Deep audit. Cyclo 3 Fort MA REF-0595 and two combination reviews (Ruscus + hesperidin methyl chalcone + vitamin C) and a four-ingredient preparation REF-1560 removed from pairs/actions (kept in references) - combinations. The Ruscus-only placebo RCT REF-1554 (Vanscheidt 2002) wired to varicose-veins and swelling. Pain dropped: its only cards were the genus review, a Polish review and the combination MA, none naming pain for Ruscus alone. Four reviews retagged narrative-review.',
    'salix_alba': 'Deep audit. Superseded 2006 Cochrane REF-1260 purged and deleted (2014 update REF-1261 kept). OA RCT REF-3736 added; OA/RA RCT REF-3737 (no relevant efficacy) recorded as no-effect; rofecoxib-comparison LBP RCT REF-3738 added. Inflammation now mechanistic (none of its cards names inflammation); calf PGE2 study REF-1256 removed from the action.',
    'salvia_hispanica': 'Deep audit. Glycaemia RCT REF-0297 removed from three non-matching actions. Chia MA REF-1267 and SR REF-1268 (no significant CV-risk effect) moved to no-effect; BP MAs REF-3739/REF-3740 added. New pair (owner rule): high-blood-pressure (2 MAs, 2 RCTs). Weight RCT REF-3743 and MA REF-3739 (no BMI/weight effect) no-effect for metabolic-support.',
    'salvia_officinalis': 'Deep audit. Two-species mouse study REF-1274 removed. Cognition RCTs REF-3748/REF-3749/REF-3751 and hot-flash MA REF-3744 added; pharyngitis spray RCT REF-3750 added to sore-throat. REF-0503 retagged narrative-review (tagged rct). New pairs (owner rule): pms (RCT), high-cholesterol (2 RCTs), blood-sugar (RCT), skin-irritation (UV-erythema RCT). Not used: palliative mouth-rinse RCT 33586003 (no difference vs saline).',
    'salvia_rosmarinus': 'Deep audit. Aroma-cognition RCT REF-0173 (retagged rct) removed from five non-matching actions. Muscle-spasm dropped (off-target). New pairs (owner rule): anxiety, depression, insomnia (student RCT REF-1291; MDD add-on RCT REF-3753; surgical aromatherapy RCT REF-3757), oral-health (toothpaste RCT REF-3756). COPD cognition RCT REF-3754 and episiotomy RCT REF-3755 added.',
    'sambucus_nigra': 'Deep audit. COVID pros/cons review REF-1018 removed from respiratory-support. Air-traveller RCT REF-3760 added to cold; Macknin 2020 influenza RCT REF-3759 (no benefit) and Wieland 2021 SR REF-3758 (evidence uncertain) recorded as no-effect. Four reviews retagged narrative-review. Safety note #1 was pasted Wikipedia text full of link fragments, cited to Kew POWO and an influenza RCT (neither states toxicity); rewritten from the NCCIH elderberry page REF-3763 (read 2026-11-13) and the EU flos monograph REF-0085 - NCCIH says little is known about pregnancy safety, so the old "should not be consumed during pregnancy" and the unsourced "gastrointestinal disease" line were not kept. Safety note #2: unsupported sentence "clinical use for colds, bronchitis and fever is well-supported" removed (contradicted by REF-3758/REF-3759); dose dash normalised.',
    'saponaria_officinalis': 'Deep audit. Web sources checked 2026-11-13: MedicineNet (cites five web pages) names cough, bronchitis, expectorant and topical eczema and says no scientific studies support most uses; Drugs.com refused automated access. Detox re-sourced to Grieve REF-3762 (tonic, diaphoretic, alterative; itch, rheumatism, jaundice) - the old note described skin cleansing. Safety note severity info -> serious (its own text reads "SERIOUS").',
    'schisandra_chinensis': 'Deep audit. Antioxidant review REF-0505 (retagged narrative-review) removed from five pairs it never names; adaptogen review REF-0506 (retagged systematic-review: PubMed SR/MA) removed from muscle-soreness. REF-0583 retagged narrative-review. Not used: muscle-strength RCTs 32260466/33710261 (strength, not soreness); Omija mixture RCT 35956334.',
}


def post():
    """Two safety-note fixes fixlib has no op for."""
    path = 'plants/sambucus_nigra.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    ci = d['contraindications'][0]
    assert 'wikipedia.org' in ci['note']
    ci['note'] = ELDER_CI   # pasted Wikipedia text; rewritten from the sources that actually state it
    ci['reference_ids'] = ['REF-3763', 'REF-0085']   # was Kew POWO (taxonomy) + an influenza RCT, neither states toxicity
    ci2 = d['contraindications'][1]
    assert 'well-supported' in ci2['note'] and '3–5 g' in ci2['note']
    ci2['note'] = ci2['note'].replace(' Clinical use for\n    colds, bronchitis, and fever is well-supported.', '').replace(
        ' Clinical use for colds, bronchitis, and fever is well-supported.', '').replace('3–5 g', '3-5 g')
    assert 'well-supported' not in ci2['note']
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})
    path = 'plants/saponaria_officinalis.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    ci = d['contraindications'][0]
    assert ci['note'].startswith('SERIOUS') and ci['severity'] == 'info'
    ci['severity'] = 'serious'
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 15', os.path.join(HERE, 'deep', 'd15_changes.tsv'), **BIB)
    post()
