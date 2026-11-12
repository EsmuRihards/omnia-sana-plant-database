"""Deep re-sweep of batch 1 (achillea-millefolium .. aloysia-citrodora) at batch-13 depth. Run from the repo root.
Owner request 2026-11-12: re-sweep batches 1-12 with the batch-13 checks (mechanistic plausibility, safety vs claims,
species/part confusion, missing landmark and null trials, claim-note accuracy). Owner rule 2026-11-12: a new pair is
added only when a systematic review or RCT of this species names the symptom and finds benefit.
New refs REF-3403..REF-3425 (abstracts verbatim from PubMed efetch, cached in deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3403', '22972105', 'cohoshcochrane', 'systematic-review'),
    ('REF-3404', '37192826', 'cohoshma', 'meta-analysis'),
    ('REF-3405', '17179056', 'haltcohosh', 'rct'),
    ('REF-3406', '19609225', 'cohoshredclover', 'rct'),
    ('REF-3407', '15863547', 'cohoshicr', 'rct'),
    ('REF-3408', '26000551', 'cohoshsleep', 'rct'),
    ('REF-3409', '28027682', 'yarrowepisiotomy', 'rct'),
    ('REF-3410', '25667123', 'yarrowmucositis', 'rct'),
    ('REF-3411', '28163113', 'yarrowskin', 'rct'),
    ('REF-3412', '29486131', 'agrimonyliver', 'rct'),
    ('REF-3413', '25386977', 'garliccoldcochrane', 'systematic-review'),
    ('REF-3414', '40602379', 'garlicrheum', 'systematic-review'),
    ('REF-3415', '24681077', 'garliccrc', 'meta-analysis'),
    ('REF-3416', '35402472', 'alliumcancer', 'meta-analysis'),
    ('REF-3417', '26693740', 'garlicglucose', 'meta-analysis'),
    ('REF-3418', '37517570', 'garlicmets', 'meta-analysis'),
    ('REF-3419', '22336851', 'aloewoundscochrane', 'systematic-review'),
    ('REF-3420', '38605441', 'aloeburns', 'meta-analysis'),
    ('REF-3421', '36504087', 'aloeoralulcers', 'meta-analysis'),
    ('REF-3422', '39909775', 'aloemucositis', 'meta-analysis'),
    ('REF-3423', '16149293', 'aloeradiation', 'systematic-review'),
    ('REF-3424', '30153721', 'aloeibs', 'meta-analysis'),
    ('REF-3425', '34104096', 'lemonverbenamuscle', 'rct'),
])

BIB = dict(
    retag={'REF-2401': 'narrative-review',   # Beer 2013: structured but not a reproducible search (PubMed: Review)
           'REF-0719': 'narrative-review',   # goutweed review tagged traditional
           'REF-0686': 'preclinical',        # in vitro antitumour study tagged traditional
           'REF-2839': 'narrative-review',   # ajoene editorial/review tagged preclinical
           'REF-0296': 'preclinical'},       # essential-oil chemistry study tagged traditional
    sets={'REF-0296': {'title': 'Chemical Composition and Antioxidant Activity Achillea millefolium L. Essential Oils',
                       'journal': 'Journal of Essential Oil Bearing Plants', 'doi': '10.1080/0972060x.2016.1238323'}},
    delete=['REF-2446',            # Cochrane 2006 HCSE, superseded by its 2012 update REF-0470 (merged)
            'REF-2228', 'REF-2230'],  # Alchemilla caucasica / Alchemilla acutiloba studies (wrong species, purged)
    new=NEW,
)

GARLIC_312 = ['anti-inflammatory', 'antidiabetic', 'antifungal', 'antimicrobial', 'antioxidant', 'immunomodulator']

PLAN = {
    'achillea_millefolium': [
        ('add', 'menstrual-cramps', ['REF-0374']),
        ('add', 'wounds', ['REF-3409']),
        ('newpair', 'oral-health', ['REF-3410'], 'A yarrow distillate mouthwash healed chemotherapy mouth sores faster than the routine mouthwash in a randomized trial'),
        ('add', 'skin-irritation', ['REF-3411']), ('add', 'inflammation', ['REF-3411']),
        ('add', 'arthritis', ['REF-2077']), ('add', 'indigestion', ['REF-2077']),
        ('add', 'fever', ['REF-2077']), ('add', 'cold', ['REF-2077']),
        ('mexcl', 'muscle-spasm', ['REF-2078']),   # off-target (inv. 11): gut smooth-muscle antispasmodic work, not muscle cramps
        ('note', 'appetite-loss', 'Traditional bitter used to stimulate appetite (Herbal Reality)'),
        ('note', 'arthritis', 'Traditional remedy for rheumatism, gout and arthritis (Grieve, A Modern Herbal; review of traditional uses)'),
        ('note', 'bloating', 'Traditionally used for flatulence (Herbal Reality)'),
        ('note', 'cold', 'Diaphoretic, used traditionally at the start of colds and flu (Grieve; Herbal Reality; review of traditional uses)'),
        ('note', 'fever', 'Diaphoretic, used traditionally to break fevers (Grieve; Herbal Reality; review of traditional uses)'),
        ('note', 'heavy-bleeding', 'Traditional styptic for heavy menstrual bleeding and nosebleeds (Herbal Reality; Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Traditional bitter for indigestion and dyspepsia (Herbal Reality; review of traditional uses)'),
        ('note', 'infection', 'Traditionally used for respiratory infections (review of traditional uses)'),
        ('note', 'inflammation', 'Yarrow oil extracts calmed experimentally irritated skin in volunteers (randomized trial); extracts and sesquiterpene lactones reduced inflammatory markers in lab studies (preclinical)'),
        ('note', 'menstrual-cramps', 'Yarrow tea reduced period pain vs placebo in a randomized trial in primary dysmenorrhoea'),
        ('note', 'skin-irritation', 'Traditionally used for skin conditions (review); yarrow oil extracts restored experimentally irritated skin in a randomized trial in volunteers'),
        ('note', 'wounds', 'Traditional styptic for minor cuts; a yarrow ointment reduced pain, redness and swelling of episiotomy wounds in a randomized trial'),
    ],
    'acorus_calamus': [
        ('drop', 'cancer'),   # its own serious warning: beta-asarone (the compound studied here) is carcinogenic
        ('note', 'depression', 'Antidepressant-like activity in animal studies (narrative review; preclinical)'),
    ],
    'actaea_racemosa': [
        ('add', 'hot-flashes', ['REF-3404', 'REF-3407']), ('add', 'menopause', ['REF-3404', 'REF-3407']),
        ('nulladd', 'hot-flashes', ['REF-3403', 'REF-3405', 'REF-3406']),
        ('nulladd', 'menopause', ['REF-3403', 'REF-3405', 'REF-3406']),
        ('newpair', 'insomnia', ['REF-3408'], 'Improved objective sleep (sleep efficiency, time awake at night) vs placebo in a randomized trial in postmenopausal women with sleep problems'),
        ('note', 'hot-flashes', 'Reduced hot flushes in meta-analyses and in a large trial of the isopropanolic extract; a Cochrane review and several large trials found no difference from placebo'),
        ('note', 'menopause', 'Improved overall menopausal symptom scores in meta-analyses and in a large trial of the isopropanolic extract; a Cochrane review and several trials found no benefit over placebo; no effect on menopausal anxiety'),
    ],
    'aegopodium_podagraria': [
        ('rmk', 'swelling', ['REF-0098']),   # Grieve: diuretic, gout/joint/sciatic pain; names no fluid retention
        ('note', 'arthritis', 'Traditional remedy for gout and aching joints (Grieve, A Modern Herbal)'),
        ('note', 'back-pain', 'Traditional remedy for sciatic pain (Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Applied traditionally as a fomentation for inflamed parts (Grieve, A Modern Herbal)'),
        ('note', 'pain', 'Traditional remedy for joint, gouty and sciatic pain (Grieve, A Modern Herbal)'),
    ],
    'aesculus_hippocastanum': [
        ('merge', 'REF-2446', 'REF-0470'),
        ('rmk', 'arthritis', ['REF-2405']),   # credits a 5-ingredient product (Flonat Fast); escin alone not reported
        ('note', 'inflammation', 'Escin, horse chestnut\'s main active compound, reduced inflammation and swelling in lab and animal studies and in trials of escin gel for blunt injuries (compound evidence; reviews)'),
        ('note', 'hemorrhoids', 'inferred from venotonic action'),
        ('note', 'cancer', 'Escin, horse chestnut\'s main active compound, slowed breast, liver, lung and pancreatic cancer cells and made them more sensitive to chemotherapy in lab studies (compound evidence, preclinical)'),
    ],
    'agrimonia_eupatoria': [
        ('newpair', 'liver-support', ['REF-3412'], 'Lowered the liver enzyme ALT and blood triglycerides vs placebo in adults with mildly raised ALT (one randomized trial)'),
        ('note', 'skin-irritation', 'Applied for minor skin inflammation (EU herbal monograph; Herbal Reality)'),
        ('note', 'indigestion', 'inferred from gastroprotective action: leaf extract protected the stomach lining from alcohol damage in rats (preclinical)'),
    ],
    'alchemilla_vulgaris': [
        ('purge', 'REF-2228'), ('purge', 'REF-2230'),
        ('note', 'inflammation', 'Extract reduced inflammatory and oxidative-stress markers in a rat model of heart injury (preclinical)'),
    ],
    'allium_sativum': [('arm', a, ['REF-0312']) for a in GARLIC_312] + [
        ('nulladd', 'cold', ['REF-3413']),
        ('add', 'arthritis', ['REF-3414']),
        ('nulladd', 'cancer', ['REF-3415', 'REF-3416']),
        ('add', 'blood-sugar', ['REF-3417', 'REF-2536', 'REF-3418']),
        ('add', 'metabolic-support', ['REF-3418']),
        ('add', 'inflammation', ['REF-3418']),
        ('newpair', 'high-cholesterol', ['REF-0204', 'REF-2536', 'REF-3418', 'REF-0648'], 'Garlic lowered total and LDL cholesterol in meta-analyses of randomized trials, by about 10% in people with mildly raised cholesterol'),
        ('newpair', 'high-blood-pressure', ['REF-0204', 'REF-3418', 'REF-0649', 'REF-0648'], 'Garlic lowered blood pressure in people with hypertension in meta-analyses of randomized trials'),
        ('drop', 'skin-irritation'), ('drop', 'wounds'),   # contradicted (inv. 11): raw garlic on skin causes chemical burns
        ('note', 'arthritis', 'Garlic extract improved pain and disease activity in small trials in rheumatoid arthritis and knee osteoarthritis (systematic review of 4 trials)'),
        ('note', 'blood-sugar', 'Garlic lowered fasting blood glucose in meta-analyses of randomized trials, including in people with diabetes'),
        ('note', 'cancer', 'Garlic compounds slowed cancer cells in lab studies; in the Shandong trial, 7 years of garlic supplements were linked to fewer gastric-cancer deaths over 22 years. Meta-analyses of prospective studies found no lower overall or colorectal cancer risk with garlic supplements'),
        ('note', 'cardiovascular-support', 'Garlic lowered blood pressure and cholesterol in meta-analyses of randomized trials'),
        ('note', 'cold', 'An allicin garlic supplement reduced the number of colds vs placebo in one randomized trial; a Cochrane review judged the evidence insufficient'),
        ('note', 'immune-support', 'Garlic stimulated immune cells and reduced the number and severity of respiratory infections in trials (meta-analysis and review)'),
        ('note', 'infection', 'An allicin supplement reduced colds in a placebo-controlled trial; allicin is antibacterial and antifungal in lab studies (review)'),
        ('note', 'inflammation', 'Garlic lowered inflammatory markers (CRP, TNF-alpha, IL-6) in meta-analyses of randomized trials'),
        ('note', 'metabolic-support', 'Garlic improved waist size, blood lipids, blood pressure and blood glucose in a meta-analysis of randomized trials'),
    ],
    'aloe_vera': [
        ('nulladd', 'wounds', ['REF-3419']), ('add', 'wounds', ['REF-3420']),
        ('newpair', 'oral-health', ['REF-3421', 'REF-3422'], 'Aloe gel healed mouth ulcers faster and reduced severe chemotherapy or radiotherapy mouth sores (meta-analyses of randomized trials)'),
        ('newpair', 'blood-sugar', ['REF-2456'], 'May improve blood glucose (HbA1c) in prediabetes and type 2 diabetes (meta-analysis; evidence limited)'),
        ('newpair', 'ibs', ['REF-3424'], 'Improved IBS symptoms vs placebo in a meta-analysis of three small randomized trials'),
        ('nulladd', 'skin-irritation', ['REF-3423']),
        ('note', 'wounds', 'Aloe sped healing of second-degree burns in a meta-analysis of randomized trials and aided skin wound healing in a systematic review; a Cochrane review found no high-quality evidence for acute and chronic wounds'),
        ('note', 'skin-irritation', 'Used on irritated and inflamed skin (reviews); a systematic review found no evidence that it prevents radiation skin reactions'),
        ('note', 'eczema', 'Moisturising (emollient) gel used for dry, inflamed skin (pharmacology review)'),
    ],
    'aloysia_citrodora': [
        ('add', 'muscle-soreness', ['REF-3425']),
        ('note', 'anxiety', 'Calming (anxiolytic) activity reported in the pharmacology literature (narrative review)'),
        ('note', 'arthritis', 'Traditional use for rheumatism (narrative review)'),
        ('note', 'inflammation', 'Leaf extract and essential oil showed anti-inflammatory activity in lab assays (preclinical)'),
        ('note', 'nervous-tension', 'Calming (anxiolytic) activity reported in the pharmacology literature (narrative review)'),
        ('note', 'insomnia', 'Improved sleep quality vs placebo in two randomized trials (people with insomnia; healthy adults with sleep problems)'),
        ('note', 'muscle-soreness', 'Lemon verbena extract reduced muscle damage and soreness after exhausting exercise vs placebo in two randomized trials'),
    ],
}

NOTES = {
    'achillea_millefolium': 'Deep re-sweep. Held RCT REF-0374 (dysmenorrhoea, positive) wired to menstrual-cramps. Landmark RCTs added: REF-3409 (episiotomy wound ointment) to wounds; REF-3410 (chemotherapy mucositis mouthwash) as a new oral-health pair (owner rule: RCT names the symptom and finds benefit); REF-3411 (SLS-irritated skin, double-blind) to skin-irritation and inflammation. Minireview REF-2077 (names RA/gout/OA, indigestion, dyspepsia, fever, influenza) moved from mechanistic to direct for those pairs. Muscle-spasm dropped: its only card REF-2078 is gut smooth-muscle antispasmodic work (off-target for muscle cramps, inv. 11). REF-0296 identified (J Essent Oil Bear Plants 2017, doi added; retagged preclinical). Sacred Plant Co page REF-0381 checked 2026-11-12: has a 10-item reference list - kept for wounds. Notes rewritten from "inferred" to their real sources. Not added: candidiasis RCT 32951733 (yarrow cream inferior to clotrimazole).',
    'acorus_calamus': 'Deep re-sweep. Cancer pair dropped: the record\'s own serious warning is that beta-asarone is carcinogenic, and the anticancer evidence was largely beta-asarone itself (DATA_PRINCIPLES inv. 10, organ/system of its own serious warning). Depression note rewritten. 2026 "systematic review" on cognition (PMID 42929295) summarises preclinical work only - not added.',
    'actaea_racemosa': 'Deep re-sweep. Landmark evidence added: Cochrane 2012 REF-3403 (16 RCTs: no significant difference from placebo in hot flushes; insufficient evidence), HALT trial 2006 REF-3405 and Geller 2009 REF-3406 (no difference from placebo) recorded as no-effect for hot-flashes and menopause. Positive: Sadahiro 2023 MA REF-3404 (overall symptoms and hot flashes improved; anxiety and depression not) and Osmers 2005 RCT REF-3407 (isopropanolic extract, 304 women) added to both. New insomnia pair from Jiang 2015 RCT REF-3408 (owner rule). REF-2401 retagged narrative-review (structured review, no reproducible search). Notes now state the mixed result. Not added: PCOS-infertility SR 33926292 ("lack of high-quality evidence").',
    'aegopodium_podagraria': 'Deep re-sweep. Grieve REF-0098 (diuretic; gout, joint and sciatic pain; fomentation for inflamed parts) names no fluid retention - kept as a mechanistic (diuretic) card for swelling only. REF-0719 retagged narrative-review. Notes rewritten to their Grieve source. No trials found on PubMed.',
    'aesculus_hippocastanum': 'Deep re-sweep. Cochrane 2006 REF-2446 merged into its 2012 update REF-0470 (superseded, inv. 11). REF-2405 credits the 5-ingredient product Flonat Fast (escin alone not reported in the abstract) - removed from arthritis, kept as a mechanistic card; arthritis is now inferred only. Inflammation and cancer notes labelled as escin (signature compound) evidence.',
    'agrimonia_eupatoria': 'Deep re-sweep. New liver-support pair from RCT REF-3412 (2018, double-blind; ALT and TG fell vs placebo in adults with raised ALT) under the owner rule. Indigestion note now states its inference (gastroprotection in rats). Skin-irritation note now credits the EU monograph.',
    'alchemilla_vulgaris': 'Deep re-sweep. Wrong-species refs purged and deleted: REF-2228 (Alchemilla caucasica gastric ulcer study), REF-2230 (Alchemilla acutiloba phenolics). REF-0686 retagged preclinical (in vitro). Inflammation note rewritten. Only an in vitro/rat wound study found on PubMed (no SR/RCT).',
    'allium_sativum': 'Deep re-sweep. Cochrane "Garlic for the common cold" 2014 REF-3413 (insufficient evidence; one trial) recorded as no-effect for cold. Cancer: meta-analyses REF-3415 (garlic supplements, colorectal cancer: no reduction, possible increase) and REF-3416 (no lower cancer risk) recorded as no-effect. Added: SR of garlic in RA/OA REF-3414 (arthritis), glucose MAs REF-3417 and held REF-2536 (blood-sugar), metabolic-syndrome MA REF-3418. New pairs from held meta-analyses (owner rule): high-cholesterol and high-blood-pressure. Skin-irritation and wounds dropped: contradicted by the record\'s own safety note (topical raw garlic causes chemical burns; SR of garlic burn injuries 33571752) - inv. 11. WCRF report REF-0312 removed from six non-cancer actions. REF-2839 retagged narrative-review (editorial/review).',
    'aloe_vera': 'Deep re-sweep. Cochrane 2012 REF-3419 ("absence of high quality clinical trial evidence" for acute and chronic wounds) recorded as no-effect for wounds; burns MA 2024 REF-3420 added. Radiation-dermatitis SR REF-3423 ("no evidence" topical aloe prevents radiation skin reactions) recorded as no-effect for skin-irritation. New pairs (owner rule, MA-backed): oral-health (REF-3421 oral ulcers, REF-3422 mucositis), blood-sugar (held MA REF-2456), ibs (Hong 2018 MA REF-3424). Not added: gingivitis SR 30829440 ("inconclusive"), prediabetes MA 27347994 ("results are inconclusive"), psoriasis (mixed RCTs).',
    'aloysia_citrodora': 'Deep re-sweep. Anxiety note claimed support from a trial of Aloysia polystachya (another species) - removed (inv. 10). Planox RCT 2021 REF-3425 (less muscle pain and damage after exhaustive exercise) added to muscle-soreness. Notes rewritten from "inferred" to their real sources.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 1', os.path.join(HERE, 'deep', 'd01_changes.tsv'), **BIB)
