"""Deep re-sweep of batch 2 (althaea-officinalis .. artemisia-vulgaris) at batch-13 depth. Run from the repo root.
Owner rule 2026-11-12: a new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3426..REF-3448 (abstracts verbatim from PubMed efetch, cached in deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3426', '30968986', 'andrographisoa', 'rct'),
    ('REF-3427', '23044768', 'andrographisuc', 'rct'),
    ('REF-3428', '21114791', 'andrographisucmesalazine', 'rct'),
    ('REF-3429', '20092985', 'kalmcold', 'rct'),
    ('REF-3430', '36842634', 'kalmcoldphase3', 'rct'),
    ('REF-3431', '27215274', 'andrographisms', 'rct'),
    ('REF-3432', '26434249', 'andrographistg', 'rct'),
    ('REF-3433', '1797953', 'andrographispharyngitis', 'rct'),
    ('REF-3434', '26840418', 'herbalcoughma', 'meta-analysis'),
    ('REF-3435', '34838903', 'dilllipids', 'systematic-review'),
    ('REF-3436', '17328819', 'dillgarliclipids', 'rct'),
    ('REF-3437', '29553834', 'dillcandida', 'rct'),
    ('REF-3438', '31705450', 'dilllabouranxiety', 'rct'),
    ('REF-3439', '23323790', 'sagapronocturia', 'rct'),
    ('REF-3440', '25350500', 'burdockoa', 'rct'),
    ('REF-3441', '41757842', 'burdockpcos', 'rct'),
    ('REF-3442', '20412090', 'arnicabruising', 'rct'),
    ('REF-3443', '12174058', 'arnicagellaser', 'rct'),
    ('REF-3444', '27348641', 'arnicablepharoplasty', 'rct'),
    ('REF-3445', '27035499', 'arnicabromelainsr', 'systematic-review'),
    ('REF-3446', '17318618', 'arnicahandoa', 'rct'),
    ('REF-3447', '17240130', 'wormwoodcrohn', 'rct'),
    ('REF-3448', '19962291', 'wormwoodcrohntnf', 'rct'),
])

BIB = dict(
    retag={'REF-0707': 'narrative-review',   # burdock diabetes "review" tagged preclinical
           'REF-0406': 'preclinical'},       # bladder-cell proteome study tagged traditional
    delete=['REF-0313',   # "Arctium lappa L.: a review..." 2008 - unlocatable (batch 2), purged from actions too
            'REF-0397'],  # columbianetin review that never names Angelica archangelica (compound paper, no species)
    new=NEW,
)

PLAN = {
    'althaea_officinalis': [
        ('newpair', 'infection', ['REF-1376'], 'Adding marshmallow extract to clotrimazole vaginal cream improved thrush symptoms more than clotrimazole alone in a randomized trial'),
        ('note', 'eczema', 'A 1% marshmallow ointment reduced atopic dermatitis severity more than 1% hydrocortisone in a small double-blind trial in children'),
        ('note', 'skin-irritation', 'Soothing (emollient) for irritated skin; a marshmallow ointment eased atopic dermatitis in a small trial in children'),
        ('note', 'indigestion', 'Mucilage eases mild stomach discomfort (EU herbal monograph; ESCOP)'),
        ('note', 'sore-throat', 'Demulcent for irritation of the mouth and throat (EU herbal monograph; ESCOP)'),
    ],
    'andrographis_paniculata': [
        ('add', 'arthritis', ['REF-3426']),
        ('newpair', 'ibd', ['REF-3427', 'REF-3428'], 'An Andrographis extract (HMPL-004) gave more clinical responses than placebo in mild-to-moderate ulcerative colitis and was comparable to mesalazine in a second trial'),
        ('add', 'cold', ['REF-1622', 'REF-3429']), ('nulladd', 'cold', ['REF-3430']),
        ('add', 'infection', ['REF-1622']),
        ('newpair', 'fatigue', ['REF-3431'], 'Reduced fatigue vs placebo in a 12-month pilot trial in people with relapsing-remitting multiple sclerosis'),
        ('newpair', 'high-cholesterol', ['REF-3432'], 'Lowered triglycerides about as much as gemfibrozil in a randomized trial in people with raised triglycerides'),
        ('add', 'sore-throat', ['REF-3433']), ('add', 'fever', ['REF-3433']),
        ('newpair', 'cough', ['REF-3434'], 'Reduced cough frequency and severity vs placebo in acute respiratory infections (meta-analysis of randomized trials)'),
        ('note', 'arthritis', 'A standardised Andrographis extract reduced knee osteoarthritis pain vs placebo in a randomized trial'),
        ('note', 'cold', 'Reduced symptoms of colds and acute respiratory infections in systematic reviews and placebo-controlled trials; a recent phase III trial found only a short-lived early benefit'),
        ('note', 'fever', 'Antipyretic; in a randomized trial a high dose relieved fever and sore throat as well as paracetamol'),
        ('note', 'inflammation', 'Andrographolide reduced inflammation in lab and animal studies (review); listed for inflammation by MSKCC About Herbs'),
        ('note', 'sore-throat', 'An Andrographis spray relieved acute viral sore throat faster than a comparator spray, and the oral herb matched paracetamol for sore throat in an older trial (randomized trials)'),
    ],
    'anethum_graveolens': [
        ('add', 'cardiovascular-support', ['REF-3435']), ('nulladd', 'cardiovascular-support', ['REF-3436']),
        ('newpair', 'high-cholesterol', ['REF-0174', 'REF-3435'], 'Dill lowered LDL cholesterol (and triglycerides in some analyses) in systematic reviews of trials; one trial in people with high lipids found no effect'),
        ('nulladd', 'high-cholesterol', ['REF-3436']),
        ('add', 'infection', ['REF-3437']),
        ('mexcl', 'wounds', ['REF-1394']),   # off-target (inv. 11): antimycobacterial lab screen offered for wounds
        ('newpair', 'anxiety', ['REF-3438'], 'Boiled dill seed reduced anxiety during labour in a randomized trial'),
        ('note', 'bloating', 'Traditional remedy for flatulence (WHO monograph)'),
        ('note', 'indigestion', 'Traditional remedy for dyspepsia and stomach ache (WHO monograph)'),
        ('note', 'urinary-support', 'Traditionally used for painful urination (WHO monograph)'),
        ('note', 'inflammation', 'Anti-inflammatory activity in experimental studies (WHO monograph); in a trial in type 2 diabetes, dill powder did not lower the inflammatory marker hs-CRP'),
        ('note', 'cardiovascular-support', 'Dill lowered LDL cholesterol and insulin resistance in meta-analyses of trials; one trial in people with high lipids found no effect on lipids'),
        ('note', 'metabolic-support', 'Dill improved insulin resistance and LDL cholesterol in a meta-analysis of randomized trials, and glycaemic control in a trial in type 2 diabetes'),
        ('note', 'infection', 'A 2% dill vaginal suppository was as effective as clotrimazole for vaginal thrush in a randomized trial'),
    ],
    'angelica_archangelica': [
        ('purge', 'REF-0397'),
        ('arm', 'sedative', ['REF-2410']),   # an elevated-plus-maze anxiety test; no sedation measured
        ('nulladd', 'urinary-support', ['REF-3439']),
        ('note', 'anxiety', 'Anti-anxiety activity in animal studies (narrative review; preclinical)'),
        ('note', 'nervous-tension', 'Anti-anxiety activity in animal studies (narrative review; preclinical)'),
        ('note', 'cognitive-function', 'Cognition-enhancing activity reported in animal studies (narrative review)'),
        ('note', 'inflammation', 'Extracts reduced inflammation in lab and animal models, including a fibromyalgia model (narrative review; preclinical)'),
        ('note', 'urinary-support', 'A leaf extract reduced daytime urination and bladder-storage symptoms in a pilot trial in overactive bladder; a larger placebo-controlled trial of a leaf extract found no overall benefit for night-time urination'),
    ],
    'arctium_lappa': [
        ('purge', 'REF-0309'), ('purge', 'REF-0313'),   # WHO 2002 has no burdock monograph; Xu 2008 unlocatable
        ('add', 'arthritis', ['REF-2339', 'REF-3440']),
        ('add', 'inflammation', ['REF-3440', 'REF-3441']),
        ('note', 'arthritis', 'Burdock root tea lowered inflammatory markers (not pain) in a randomized trial in knee osteoarthritis; anti-rheumatic activity reported for the root (review)'),
        ('note', 'inflammation', 'Burdock root lowered inflammatory markers in randomized trials (knee osteoarthritis; polycystic ovary syndrome); anti-inflammatory activity in lab studies (reviews)'),
    ],
    'arctium_minus': [
        ('add', 'arthritis', ['REF-1924']), ('add', 'inflammation', ['REF-1925']),
        ('note', 'arthritis', 'Seed extract reduced pain in a mouse model of acute gout (preclinical)'),
        ('note', 'inflammation', 'Anti-inflammatory and pain-relieving activity in animal tests (preclinical)'),
    ],
    'arctostaphylos_uva_ursi': [
        ('arm', 'antimicrobial', ['REF-0406']), ('arm', 'urinary-antiseptic', ['REF-0406']),
        ('mexcl', 'wounds', ['REF-2370', 'REF-0407']),   # off-target: acne bacterium; ESCOP covers urinary use only
        ('note', 'uti', 'Urinary antiseptic for mild cystitis (EU herbal monograph; ESCOP); in two randomized trials in women with UTI, uva-ursi did not ease symptoms and led to more symptom burden than an antibiotic'),
        ('note', 'infection', 'Urinary antiseptic for mild cystitis (EU herbal monograph; ESCOP); two randomized trials found no symptom benefit'),
        ('note', 'urinary-support', 'Used short-term for mild lower urinary tract infection symptoms (EU herbal monograph); two randomized trials found no symptom benefit'),
    ],
    'arnica_montana': [
        ('add', 'bruising', ['REF-3442']), ('nulladd', 'bruising', ['REF-3443', 'REF-3444', 'REF-3445']),
        ('add', 'arthritis', ['REF-3446']),
        ('drop', 'wounds'), ('drop', 'skin-irritation'),   # own safety notes: not on broken skin; can irritate skin
        ('note', 'bruising', 'Traditional topical remedy for bruises (EU herbal monograph, summarised in a review); a 20% arnica ointment sped bruise healing in one randomized trial, but arnica gel, a 10% ointment and a systematic review found no clear benefit'),
        ('note', 'arthritis', 'An arnica gel was as effective as ibuprofen gel for hand osteoarthritis in a randomized trial; applied for rheumatic muscle and joint complaints (EU herbal monograph)'),
        ('note', 'infection', 'Antibacterial activity reported in lab studies (narrative review)'),
        ('note', 'inflammation', 'Applied for inflammation after blunt injuries (EU herbal monograph, summarised in a review); anti-inflammatory activity in lab and animal studies'),
    ],
    'artemisia_absinthium': [
        ('newpair', 'ibd', ['REF-3447', 'REF-3448'], 'In two small placebo-controlled trials in Crohn\'s disease, wormwood allowed steroid tapering and improved symptoms and mood'),
        ('note', 'bloating', 'Traditional bitter for flatulence (Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Traditional bitter for weak digestion (Grieve, A Modern Herbal)'),
        ('note', 'infection', 'Traditional antiseptic use (Grieve, A Modern Herbal)'),
    ],
    'artemisia_vulgaris': [
        ('note', 'arthritis', 'Burned as moxa for rheumatism in traditional practice (Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Traditional remedy for stomach disorders (Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Traditionally used for swollen tonsils (Grieve, A Modern Herbal)'),
    ],
    'allium_sativum': [('add', 'high-cholesterol', ['REF-3436'])],   # Kojuri 2007: garlic arm lowered TC/LDL
}

NOTES = {
    'althaea_officinalis': 'Deep re-sweep. Held add-on RCT REF-1376 (marshmallow + clotrimazole vs clotrimazole in vulvovaginal candidiasis; better symptom relief) wired as a new infection pair (owner rule). Eczema/skin notes now describe REF-1373 (1% ointment beat 1% hydrocortisone, pilot trial in children). Indigestion note no longer claims heartburn/reflux (EU monograph: mild gastric discomfort only). BNO 1030 (Imupret) trial not added (multi-herb).',
    'andrographis_paniculata': 'Deep re-sweep. SR REF-1622 (Coon & Ernst 2004) moved from mechanistic to direct for cold/infection. Landmark trials added: ParActin knee-OA RCT REF-3426 (arthritis), HMPL-004 UC RCTs REF-3427/3428 (new ibd pair), KalmCold RCT 2010 REF-3429 (cold) and its 2023 phase III REF-3430 (benefit on day 3 only - recorded as no-effect), MS fatigue RCT REF-3431 (new fatigue pair), hypertriglyceridaemia RCT REF-3432 (new high-cholesterol pair), 1991 pharyngotonsillitis RCT REF-3433 (sore-throat, fever), Wagner 2015 herbal-cough MA REF-3434 (new cough pair; "strong evidence for A. paniculata"). Not added: Kan Jang/ImmunoGuard trials (fixed combination with Eleutherococcus), 2009 RA trial 19408036 (within-group changes only).',
    'anethum_graveolens': 'Deep re-sweep. Lipid evidence: updated SR REF-3435 (LDL, TG, TC improved) added; Kojuri 2007 RCT REF-3436 ("no significant effect on lipid profile") recorded as no-effect; new high-cholesterol pair (owner rule; REF-0174 + REF-3435). Candidiasis RCT REF-3437 (2% suppository = clotrimazole) wired to infection. New anxiety pair from labour-anxiety RCT REF-3438. Wounds dropped: its only card was an antimycobacterial lab screen (off-target, inv. 11). Notes rewritten to the WHO monograph wording. Not added: Apiaceae dysmenorrhoea MA 41653970 (no dill-specific result in the abstract).',
    'angelica_archangelica': 'Deep re-sweep. REF-0397 (columbianetin review; never names A. archangelica) purged and deleted. REF-2410 (elevated-plus-maze anxiety test) removed from the sedative action - insomnia, inferred only from it, dropped. SagaPro RCT REF-3439 (A. archangelica leaf extract; no overall benefit for nocturia vs placebo) recorded as no-effect for urinary-support. Notes rewritten.',
    'arctium_lappa': 'Deep re-sweep. REF-0309 (WHO 2002 vol. 2: no burdock monograph) and REF-0313 (unlocatable; deleted) purged from the actions too. Held review REF-2339 (anti-rheumatic) moved to direct for arthritis. Knee-OA RCT REF-3440 (root tea lowered CRP/IL-6; no pain outcome) added to arthritis and inflammation; PCOS RCT REF-3441 to inflammation. REF-0707 retagged narrative-review.',
    'arctium_minus': 'Deep re-sweep. A. minus studies moved from mechanistic to direct where they name the symptom: REF-1924 (acute gout model) for arthritis, REF-1925 (anti-inflammatory in vivo) for inflammation. No trials on PubMed.',
    'arctostaphylos_uva_ursi': 'Deep re-sweep. REF-0406 (hydroquinone changed bladder-cell proteins: "may exhibit negative properties") removed from the antimicrobial and urinary-antiseptic actions (kept in references), retagged preclinical. Wounds dropped: off-target cards (C. acnes acne study; ESCOP limited to urinary use). Notes now state the two null trials.',
    'arnica_montana': 'Deep re-sweep. Wounds and skin-irritation dropped: contradicted by the record\'s own safety notes ("do not apply to broken or damaged skin, open wounds"; "prolonged topical use can also irritate the skin"; inv. 11). Bruising: 20% ointment RCT REF-3442 added; topical arnica gel RCT REF-3443, 10% ointment blepharoplasty RCT REF-3444 and the arnica/bromelain SR REF-3445 ("insufficient data") recorded as no-effect. Hand-OA RCT REF-3446 (arnica gel non-inferior to ibuprofen gel) added to arthritis. Homeopathic arnica trials not used (owner rule). Gap: topical arnica increased muscle pain after eccentric exercise (20807867) - no muscle pair exists.',
    'artemisia_absinthium': 'Deep re-sweep. New ibd pair from two placebo-controlled Crohn\'s disease RCTs (REF-3447 steroid-sparing; REF-3448 TNF-alpha, remission) under the owner rule. Notes rewritten to Grieve. Gap for owner: Commission E/EMA appetite-loss and dyspepsia uses have no appetite-loss pair (no SR/RCT).',
    'artemisia_vulgaris': 'Deep re-sweep. Notes rewritten to Grieve (moxa for rheumatism; stomach disorders; swollen tonsils). Moxibustion trials not used (a heat technique, not the plant\'s pharmacology).',
    'allium_sativum': 'Deep re-sweep (batch 2 follow-up). Kojuri 2007 RCT REF-3436 (garlic tablets improved cholesterol, LDL and HDL) added to high-cholesterol.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 2', os.path.join(HERE, 'deep', 'd02_changes.tsv'), **BIB)
