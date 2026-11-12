"""Deep re-sweep of batch 4 (cannabis-sativa .. cinnamomum-verum) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: a new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep scoring as SRs. New refs REF-3485..REF-3506 (PubMed efetch, deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3485', '41023483', 'ver01backpain', 'rct'),
    ('REF-3486', '39256070', 'hempseedoiloa', 'rct'),
    ('REF-3487', '22972149', 'capsaicinlowcochrane', 'systematic-review'),
    ('REF-3488', '38761115', 'capsaicinoa', 'meta-analysis'),
    ('REF-3489', '12030948', 'redpepperdyspepsia', 'rct'),
    ('REF-3490', '33262398', 'capsicummets', 'meta-analysis'),
    ('REF-3491', '37344950', 'capsicumlipids', 'meta-analysis'),
    ('REF-3492', '26044145', 'carawayibs', 'rct'),
    ('REF-3493', '11106141', 'gotukolastartle', 'rct'),
    ('REF-3494', '18191355', 'centellaelderly', 'rct'),
    ('REF-3495', '27340413', 'gotukolastroke', 'rct'),
    ('REF-3496', '32310680', 'centellalaser', 'rct'),
    ('REF-3497', '21298840', 'centelladiabeticwound', 'rct'),
    ('REF-3498', '22972104', 'cinnamoncochrane', 'systematic-review'),
    ('REF-3499', '22579946', 'cinnamonglycaemic', 'meta-analysis'),
    ('REF-3500', '25249415', 'cassiaigt', 'rct'),
    ('REF-3501', '16549460', 'cinnamonpostmenopausal', 'rct'),
    ('REF-3502', '37262194', 'cassiaarterial', 'rct'),
    ('REF-3503', '36655542', 'cassiadiarrhea', 'rct'),
    ('REF-3504', '22671971', 'truecinnamonsr', 'systematic-review'),
    ('REF-3505', '21929834', 'ceyloncinnamonigt', 'rct'),
    ('REF-3506', '40667904', 'cinnamonanthropometric', 'rct'),
])

BIB = dict(
    sets={'REF-0057': {'doi': '10.1002/14651858.CD007393.pub4'},   # was malformed "10.1002/http://..."
          'REF-0169': {'year': '1999', 'doi': '10.1016/s0378-8741(98)00134-2', 'pmid': '10363839'},   # old DOI dead
          'REF-0022': {'title': 'Antimicrobial activity of Epilobium spp. extracts', 'journal': 'Farmaco', 'year': '2001',
                       'volume': '56', 'pages': '345--348', 'doi': '10.1016/s0014-827x(01)01047-3', 'pmid': '11482755'}},
    new=NEW,
)

PLAN = {
    'cannabis_sativa': [('arm', a, ['REF-0058']) for a in ('analgesic', 'anti-inflammatory', 'antioxidant', 'sedative')] + [
        ('refadd', ['REF-0058']),
        ('add', 'back-pain', ['REF-3485']), ('add', 'pain', ['REF-3485', 'REF-3486']), ('add', 'arthritis', ['REF-3486']),
        ('note', 'back-pain', 'A full-spectrum cannabis extract (VER-01) reduced chronic low back pain more than placebo in a large phase 3 trial (modest effect; more side effects)'),
        ('note', 'pain', 'A full-spectrum cannabis extract reduced chronic low back pain in a phase 3 trial, and topical hemp seed oil reduced knee osteoarthritis pain (randomized trials)'),
        ('note', 'arthritis', 'Topical hemp seed oil reduced knee osteoarthritis pain vs placebo, comparable to diclofenac gel, in a randomized trial'),
    ],
    'capsella_bursa_pastoris': [
        ('note', 'diarrhea', 'Traditional astringent remedy for diarrhoea (Herbal Reality)'),
        ('note', 'menstrual-cramps', 'Traditionally used for period pain (Herbal Reality)'),
        ('note', 'pms', 'Traditionally used for premenstrual complaints (Herbal Reality)'),
    ],
    'capsicum_annuum': [
        ('nulladd', 'pain', ['REF-3487']), ('add', 'arthritis', ['REF-3488']), ('add', 'indigestion', ['REF-3489']),
        ('newpair', 'high-cholesterol', ['REF-3490', 'REF-3491'], 'Capsicum supplements lowered LDL or total cholesterol in meta-analyses of small trials in metabolic syndrome; other blood lipids did not change'),
        ('drop', 'skin-irritation'), ('drop', 'wounds'),   # own safety note: topical preparations may cause skin irritation
        ('note', 'pain', 'High-concentration capsaicin patches (capsaicin is chili\'s signature compound) relieved chronic neuropathic pain in some patients; low-concentration capsaicin creams showed no meaningful effect (Cochrane reviews; compound evidence)'),
        ('note', 'arthritis', 'Topical capsaicin, chili\'s signature compound, may reduce osteoarthritis pain for up to 3 months (meta-analysis; compound evidence)'),
        ('note', 'indigestion', 'Red pepper powder reduced functional dyspepsia symptoms vs placebo in a randomized trial'),
        ('note', 'infection', 'Capsaicin inhibited some bacteria in lab tests (compound evidence, preclinical)'),
    ],
    'carum_carvi': [
        ('newpair', 'ibs', ['REF-3492'], 'Hot caraway-oil poultices eased IBS symptoms in a randomized crossover trial; part of the effect may be due to the heat'),
        ('arm', 'antimicrobial', ['REF-0078']), ('arm', 'appetite-stimulant', ['REF-0078']),   # EU monograph: bloating/flatulence only
        ('note', 'bloating', 'Traditionally used for bloating and flatulence (EU herbal monograph)'),
        ('note', 'cancer', 'Caraway reduced markers of chemically induced colon cancer in rats (preclinical)'),
    ],
    'centaurium_erythraea': [
        ('note', 'acid-reflux', 'Traditionally used for heartburn (Herbal Reality)'),
        ('note', 'arthritis', 'Traditionally used for joint pain (Herbal Reality)'),
        ('note', 'detox', 'Traditional bitter "blood-cleansing" tonic (Herbal Reality)'),
        ('note', 'inflammation', 'Anti-inflammatory activity in lab and animal studies (review); traditional use (Herbal Reality)'),
        ('note', 'liver-support', 'Liver-protective activity in animal studies (review); traditional liver tonic (Herbal Reality)'),
        ('note', 'skin-irritation', 'Traditionally used for skin complaints (Herbal Reality)'),
    ],
    'centella_asiatica': [
        ('add', 'anxiety', ['REF-3493']),
        ('add', 'cognitive-function', ['REF-3494', 'REF-3495']),
        ('add', 'memory', ['REF-3494', 'REF-3495']), ('nulladd', 'memory', ['REF-0568']),
        ('add', 'wounds', ['REF-2091', 'REF-3496', 'REF-3497']),
        ('add', 'psoriasis', ['REF-2092']), ('add', 'skin-irritation', ['REF-2093']),
        ('note', 'anxiety', 'Gotu kola blunted the acoustic startle response (a measure of anxiety) vs placebo in healthy volunteers; anti-anxiety activity of its triterpenes in animal studies (review)'),
        ('note', 'arthritis', 'Its triterpenes asiaticoside and madecassoside reduced arthritis in animal models (review; compound evidence)'),
        ('note', 'cognitive-function', 'Improved cognition and mood in healthy older volunteers and after stroke in small randomized trials; a meta-analysis found no significant effect on any cognitive domain'),
        ('note', 'memory', 'Improved memory in small randomized trials (healthy older adults; after stroke); a meta-analysis found no significant effect on cognitive domains'),
        ('note', 'inflammation', 'Its triterpenes and a standardised extract (TECA) reduced inflammation in lab and animal studies (reviews)'),
        ('note', 'nervous-tension', 'Anti-anxiety activity of its triterpenes in animal studies (review; compound evidence)'),
        ('note', 'psoriasis', 'Extracts reduced psoriasis-like skin inflammation in lab and animal studies (preclinical; review)'),
        ('note', 'skin-irritation', 'A 5% Centella cream reduced experimentally induced skin micro-inflammation in volunteers; anti-inflammatory activity in lab studies (reviews)'),
        ('note', 'wounds', 'Centella extract sped healing of diabetic wounds and of facial laser wounds in randomized trials; a systematic review found improved wound healing'),
    ],
    'chamerion_angustifolium': [
        ('mexcl', 'bruising', ['REF-1658']),   # wound-healing enzyme study; a wound is not a bruise (batch-1 rule)
        ('note', 'infection', 'Fireweed extract was active against bacteria, yeasts and fungi in lab tests (preclinical)'),
    ],
    'chelidonium_majus': [
        ('drop', 'skin-irritation'), ('drop', 'wounds'),   # own safety note: latex irritant and caustic, keep from broken skin
        ('note', 'cancer', 'Celandine extracts killed ovarian and other cancer cells and reduced metastases in mice (preclinical)'),
        ('note', 'infection', 'Antimicrobial activity reported in lab studies (integrative review)'),
        ('note', 'inflammation', 'Anti-inflammatory activity reported in lab and animal studies (integrative review)'),
        ('note', 'pain', 'Traditionally used for pain; analgesic activity reported (integrative review)'),
        ('note', 'warts', 'Fresh orange latex is traditionally dabbed on warts; latex components were active against the wart virus (HPV) in lab studies (preclinical)'),
    ],
    'cinnamomum_cassia': [
        ('add', 'blood-sugar', ['REF-3499']), ('nulladd', 'blood-sugar', ['REF-3498', 'REF-3500', 'REF-3501']),
        ('nulladd', 'high-cholesterol', ['REF-3501']), ('nulladd', 'cardiovascular-support', ['REF-3502']),
        ('add', 'metabolic-support', ['REF-3502']),
        ('newpair', 'diarrhea', ['REF-3503'], 'A cassia cinnamon water extract eased diarrhoea symptoms vs placebo in a randomized trial'),
        ('note', 'blood-sugar', 'Cinnamon (mostly cassia) lowered fasting glucose in several meta-analyses, but a Cochrane review judged the evidence insufficient and some trials found no effect on glucose control or insulin sensitivity'),
        ('note', 'cardiovascular-support', 'Cinnamon improved blood pressure and blood lipids in some meta-analyses and trials, mostly in type 2 diabetes; a trial of cassia found no change in arterial stiffness, blood pressure or lipids'),
        ('note', 'high-cholesterol', 'Cinnamon lowered total cholesterol and triglycerides (LDL less consistently) in meta-analyses of trials, mostly in type 2 diabetes; some trials found no change'),
        ('note', 'metabolic-support', 'Cinnamon improved glucose, lipids and body weight in people with type 2 diabetes (meta-analyses; randomized trials)'),
    ],
    'cinnamomum_verum': [
        ('add', 'blood-sugar', ['REF-3504']), ('nulladd', 'blood-sugar', ['REF-3505']),
        ('nulladd', 'metabolic-support', ['REF-3506']),
        ('note', 'blood-sugar', 'Ceylon cinnamon extract lowered fasting blood sugar in type 2 diabetes in a randomized trial and showed antidiabetic effects in lab and animal studies (systematic review); it did not lower after-meal glucose in people with impaired glucose tolerance'),
        ('note', 'cancer', 'Ceylon cinnamon extract and cinnamaldehyde slowed cancer cells in lab and animal studies (preclinical)'),
    ],
}

NOTES = {
    'cannabis_sativa': 'Deep re-sweep. REF-0058 (CBD trial in Dravet-syndrome seizures) was filed as evidence for the analgesic, anti-inflammatory, antioxidant and sedative actions - removed from all four, kept in references. Added VER-01 phase 3 RCT REF-3485 (full-spectrum C. sativa extract; chronic low back pain, primary endpoint met) to back-pain and pain, and topical hemp-seed-oil knee-OA RCT REF-3486 to arthritis and pain. Not used: cannabinoid reviews pooling synthetic THC analogues (compound/drug, not the plant).',
    'capsella_bursa_pastoris': 'Deep re-sweep. Notes rewritten to Herbal Reality wording. REF-0508 is an ESCOP news summary of the REF-0608 RCT (kept). Postpartum-haemorrhage trial 28590768 not added (no matching condition).',
    'capsicum_annuum': 'Deep re-sweep. Cochrane low-concentration capsaicin review REF-3487 ("without meaningful effect beyond placebo") recorded as no-effect for pain. Capsaicin-OA MA REF-3488 (arthritis), Bortolotti 2002 red-pepper dyspepsia RCT REF-3489 (indigestion) added; new high-cholesterol pair from two lipid MAs (REF-3490/3491; owner rule). Skin-irritation and wounds dropped: contradicted by the record\'s own note (topical preparations may cause skin irritation; inv. 11). DOIs fixed: REF-0057 (malformed), REF-0169 (dead; now PMID 10363839). Not used: Cochrane herbal low-back-pain plasters (Capsicum frutescens, other species).',
    'carum_carvi': 'Deep re-sweep. New ibs pair from caraway-oil poultice RCT REF-3492 (owner rule; authors note heat may contribute). EU monograph REF-0078 removed from the antimicrobial and appetite-stimulant actions (it covers bloating/flatulence only). Menthacarin (peppermint + caraway) trials not used (combination).',
    'centaurium_erythraea': 'Deep re-sweep. Notes rewritten from "inferred" to their sources (Herbal Reality names all nine uses, batch 4; review REF-0619). No trials on PubMed.',
    'centella_asiatica': 'Deep re-sweep. Added: Bradwejn 2000 startle RCT REF-3493 (anxiety), Wattanathorn 2008 REF-3494 and Farhana 2016 REF-3495 RCTs (cognition, memory); Cochrane-style null REF-0568 now also recorded for memory. Held SR REF-2091 plus RCTs REF-3496 (post-laser) and REF-3497 (diabetic wounds) to wounds; held REF-2092 (psoriasis model) and REF-2093 (human skin micro-inflammation) wired to psoriasis and skin-irritation. Notes label asiaticoside/madecassoside evidence as compound evidence.',
    'chamerion_angustifolium': 'Deep re-sweep. REF-0022 corrected: Battinelli et al., Farmaco 2001;56:345-8 (PMID 11482755; old DOI dead, year was 2014). Bruising dropped: its only card was a wound-healing enzyme study (batch-1 rule: a wound is not a bruise).',
    'chelidonium_majus': 'Deep re-sweep. Skin-irritation and wounds dropped: contradicted by the record\'s own note (latex "irritant and caustic - keep it away from ... broken skin"; inv. 11). Warts kept (traditional external use on intact skin). Notes rewritten.',
    'cinnamomum_cassia': 'Deep re-sweep. Cochrane "Cinnamon for diabetes mellitus" 2012 REF-3498 ("insufficient evidence"), cassia IGT RCT REF-3500 and Vanschoonbeek 2006 RCT REF-3501 (no glycaemic or lipid effect) recorded as no-effect; positive 2012 MA REF-3499 added. Arterial-stiffness RCT REF-3502: no BP/lipid/vascular change (no-effect for cardiovascular-support) but lower weight and HbA1c (metabolic-support). New diarrhea pair from RCT REF-3503 (owner rule). Notes now state the mixed evidence.',
    'cinnamomum_verum': 'Deep re-sweep. Ranasinghe 2012 SR/MA REF-3504 (C. zeylanicum antidiabetic effects in vitro and in vivo) added to blood-sugar (owner: SRs of preclinical work keep SR scoring). Wickenberg 2012 RCT REF-3505 (no effect on postprandial glucose in IGT) and 2025 RCT REF-3506 (anthropometrics not significant) recorded as no-effect.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 4', os.path.join(HERE, 'deep', 'd04_changes.tsv'), **BIB)
