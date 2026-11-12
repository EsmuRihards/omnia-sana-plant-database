"""Deep re-sweep of batch 6 (daucus-carota .. equisetum-sylvaticum) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3536..REF-3551 (PubMed efetch, deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3536', '40311928', 'echinaceachildrenma', 'meta-analysis'),
    ('REF-3537', '14748902', 'echinilincold', 'rct'),
    ('REF-3538', '33832544', 'echinaceachildrenrti', 'rct'),
    ('REF-3539', '15197051', 'echinaceacoldyale', 'rct'),
    ('REF-3540', '14657066', 'echinaceachildurti', 'rct'),
    ('REF-3541', '15156472', 'echinacearhinovirus', 'rct'),
    ('REF-3542', '18450126', 'echinaceaurtsymptoms', 'rct'),
    ('REF-3543', '38743584', 'echinaceaimmune', 'rct'),
    ('REF-3544', '28610718', 'echinaceaeczema', 'rct'),
    ('REF-3545', '38593657', 'cardamomcv', 'meta-analysis'),
    ('REF-3546', '36181264', 'cardamombp', 'meta-analysis'),
    ('REF-3547', '32359750', 'cardamomlipids', 'meta-analysis'),
    ('REF-3548', '31755188', 'cardamomlipidsma', 'meta-analysis'),
    ('REF-3549', '35581106', 'cardamomnausea', 'rct'),
    ('REF-3550', '28480505', 'cardamominflammation', 'rct'),
    ('REF-3551', '14971626', 'siberianginsengfatigue', 'rct'),
])

BIB = dict(new=NEW)

PLAN = {
    'daucus_carota': [
        ('note', 'cancer', 'Carrot compounds slowed cancer cells in lab studies (review)'),
        ('note', 'uti', 'Traditionally used for cystitis (review of wild-carrot uses)'),
        ('note', 'bloating', 'Traditional carminative for flatulence (review of wild-carrot uses)'),
        ('note', 'inflammation', 'Anti-inflammatory activity of wild carrot and of carrot polyacetylenes in lab studies (reviews)'),
        ('note', 'infection', 'Wild-carrot essential oil inhibited bacteria and fungi in lab tests (preclinical)'),
        ('note', 'blood-sugar', 'Insoluble fibre from carrots improved glucose tolerance in mice (preclinical)'),
        ('note', 'high-cholesterol', 'Insoluble fibre from carrots limited the rise in blood lipids after a fatty meal in mice (preclinical)'),
        ('note', 'indigestion', 'inferred from gastroprotective action: extracts reduced stomach acid and ulcers in rats (preclinical)'),
    ],
    'dioscorea_villosa': [
        ('arm', 'antispasmodic', ['REF-0528']),   # the study measured pain and inflammation, not spasm
        ('note', 'arthritis', 'Extract reduced pain and inflammation in rodent models (preclinical)'),
        ('note', 'inflammation', 'Extract reduced inflammation in rodent models (preclinical)'),
        ('note', 'pain', 'Extract reduced pain in rodent models (preclinical)'),
        ('note', 'cancer', 'Wild yam extract had cytostatic effects on triple-negative breast cancer cells in the lab (preclinical)'),
    ],
    'echinacea_purpurea': [
        ('arm', 'antimicrobial', ['REF-2017', 'REF-2014']), ('refadd', ['REF-2017']),
        ('add', 'cold', ['REF-3536', 'REF-3537', 'REF-3538', 'REF-2014']),
        ('nulladd', 'cold', ['REF-3539', 'REF-3540', 'REF-3541', 'REF-3542']),
        ('add', 'infection', ['REF-3538']),
        ('add', 'immune-support', ['REF-3543', 'REF-2013']),
        ('newpair', 'eczema', ['REF-3544'], 'A cream with Echinacea purpurea alkylamides eased atopic eczema symptoms and restored the skin barrier in a randomized trial'),
        ('note', 'cold', 'Results are mixed: E. purpurea reduced colds or their symptoms in some randomized trials and in a meta-analysis in children, but other trials and a Cochrane review found no clear benefit for treating colds'),
        ('note', 'immune-support', 'Improved immune markers vs placebo in randomized trials (healthy adults; athletes); traditional immunostimulant (WHO monograph)'),
        ('note', 'infection', 'Reduced respiratory infections and antibiotic use in children in a randomized trial; supportive use for respiratory and urinary infections (WHO monograph)'),
        ('note', 'skin-irritation', 'Applied externally for inflammatory skin conditions (WHO monograph)'),
        ('note', 'wounds', 'Applied externally to aid wound healing (WHO monograph)'),
    ],
    'elettaria_cardamomum': [
        ('arm', 'anti-inflammatory', ['REF-0292']), ('arm', 'antimicrobial', ['REF-0292', 'REF-1669']), ('arm', 'digestive', ['REF-0292']),
        ('add', 'cardiovascular-support', ['REF-3545']),
        ('newpair', 'high-blood-pressure', ['REF-3546'], 'Green cardamom lowered blood pressure in a meta-analysis of small randomized trials in metabolic syndrome'),
        ('add', 'inflammation', ['REF-3546', 'REF-3550']),
        ('newpair', 'high-cholesterol', ['REF-3547', 'REF-3548'], 'Cardamom lowered triglycerides (but not cholesterol) in meta-analyses of randomized trials'),
        ('newpair', 'nausea', ['REF-3549'], 'Inhaling cardamom aroma reduced nausea and retching during and after caesarean section in a randomized trial'),
        ('note', 'cardiovascular-support', 'Cardamom improved some cardiometabolic markers in a meta-analysis of randomized trials and lowered blood pressure in a small uncontrolled study; traditionally used for heart disorders (review)'),
        ('note', 'infection', 'Traditionally used for tooth and gum infections (review)'),
        ('note', 'respiratory-support', 'Traditionally used for asthma and other respiratory complaints (review)'),
        ('note', 'inflammation', 'Cardamom lowered inflammatory markers in a meta-analysis and in a randomized trial in pre-diabetic women'),
    ],
    'eleutherococcus_senticosus': [
        ('arm', 'ergogenic', ['REF-2291']),   # concludes no endurance benefit (inv. 7)
        ('nulladd', 'fatigue', ['REF-3551', 'REF-2291']),
        ('note', 'blood-sugar', 'Antidiabetic activity reported in lab and animal studies (review)'),
        ('note', 'cold', 'Russian clinical studies suggest it may help prevent respiratory infections (narrative review)'),
        ('note', 'cognitive-function', 'Improved mental performance in Russian clinical studies (narrative reviews)'),
        ('note', 'fatigue', 'Traditional adaptogen for fatigue (reviews); a randomized trial in chronic fatigue, a stress-management trial and a review of endurance studies found no overall benefit'),
        ('note', 'immune-support', 'Immunostimulant effects reported (reviews)'),
        ('note', 'memory', 'Memory-supporting activity reported in lab and animal studies (review)'),
        ('note', 'metabolic-support', 'Antidiabetic and metabolic activity reported in lab and animal studies (review)'),
        ('note', 'stress', 'Traditional adaptogen to improve resistance to stress (reviews); a randomized trial adding it to stress-management training found no benefit'),
    ],
    'elymus_repens': [
        ('note', 'urinary-support', 'Used to flush the urinary tract in minor urinary complaints and irritable bladder (EU herbal monograph; ESCOP); a rat study found no effect on kidney-stone risk factors'),
    ],
    'epilobium_parviflorum': [
        ('purge', 'REF-2301'),   # a review of Epilobium angustifolium (fireweed) - moved to Chamerion angustifolium
        ('mexcl', 'arthritis', ['REF-0803', 'REF-0618']), ('mexcl', 'inflammation', ['REF-0803', 'REF-0618']),
        ('mexcl', 'skin-irritation', ['REF-0803', 'REF-0618']),   # genus-level reviews, prose-only attribution (inv. 10)
        ('note', 'infection', 'Extract inhibited E. coli growth in the lab (preclinical)'),
        ('note', 'inflammation', 'Extract inhibited inflammatory COX enzymes in the lab (preclinical)'),
    ],
    'chamerion_angustifolium': [('aadd', 'antioxidant', ['REF-2301'])],
    'equisetum_arvense': [
        ('arm', 'anti-inflammatory', ['REF-0041', 'REF-0083']), ('arm', 'anti-rheumatic', ['REF-0041', 'REF-0083']),
        ('arm', 'antimicrobial', ['REF-0041', 'REF-0083']), ('arm', 'vulnerary', ['REF-0041']),
        ('note', 'arthritis', 'Among plants studied in humans for joint disorders (review)'),
        ('note', 'inflammation', 'Extract modulated inflammatory immune cells in the lab (preclinical)'),
        ('note', 'cancer', 'Extract was toxic to colon cancer cells but not to normal cells in the lab (preclinical)'),
        ('note', 'urinary-support', 'Increased urine output like hydrochlorothiazide in a randomized trial in healthy men; used to flush the urinary tract in minor urinary complaints (EU herbal monograph)'),
        ('note', 'wounds', 'Traditionally used for minor wounds (EU herbal monograph)'),
    ],
    'equisetum_pratense': [('arm', 'antioxidant', ['REF-2361']), ('refadd', ['REF-2361'])],
    'equisetum_sylvaticum': [('arm', 'antioxidant', ['REF-2361']), ('refadd', ['REF-2361'])],
}

NOTES = {
    'daucus_carota': 'Deep re-sweep. Notes rewritten to their sources. Not added (owner to decide): fertility pair from a carrot-seed RCT in hypoactive sexual desire disorder (33183662) - the record\'s own evidence REF-2724 reports estrogenic, pregnancy-interceptory effects of the seeds, so a "fertility" listing could mislead.',
    'dioscorea_villosa': 'Deep re-sweep. REF-0528 removed from the antispasmodic action (measured pain and inflammation only). Notes rewritten.',
    'echinacea_purpurea': 'Deep re-sweep. Cold now shows both sides: added MA in children REF-3536, Goel 2004 REF-3537, Ogal 2021 REF-3538 and the narrative REF-2014; Yale 2004 REF-3539, Taylor 2003 (JAMA, children) REF-3540, Sperber 2004 REF-3541 and O\'Neil 2008 REF-3542 recorded as no-effect (all E. purpurea). REF-2017 (pilot: "effectiveness could not be accurately assessed") and REF-2014 removed from the antimicrobial action. Immune RCT REF-3543 and held RCT REF-2013 to immune-support. New eczema pair from alkylamide cream RCT REF-3544 (owner rule).',
    'elettaria_cardamomum': 'Deep re-sweep. BP study REF-0292 removed from anti-inflammatory/antimicrobial/digestive actions; gastric-ulcer study REF-1669 from antimicrobial. Added CV MA REF-3545, BP/inflammation MA REF-3546, inflammation RCT REF-3550. New pairs (owner rule): high-blood-pressure REF-3546; high-cholesterol REF-3547/3548 (triglycerides only, labelled); nausea REF-3549 (aromatherapy RCT).',
    'eleutherococcus_senticosus': 'Deep re-sweep. Goulet 2005 REF-2291 (no endurance benefit) removed from the ergogenic action and recorded as no-effect for fatigue, with Hartz 2004 RCT REF-3551 ("overall efficacy was not demonstrated" in chronic fatigue). Notes rewritten; fatigue and stress notes state the null trials. REF-0506 kept as narrative-review (PubMed tags it MA, but it is a history/perspectives review).',
    'elymus_repens': 'Deep re-sweep. Urinary-support note rewritten. No trials on PubMed.',
    'epilobium_parviflorum': 'Deep re-sweep. REF-2301 (fireweed, E. angustifolium) moved to Chamerion angustifolium. Genus reviews REF-0803/REF-0618 hidden from arthritis, inflammation and skin-irritation mechanistic cards (prose-only genus attribution); REF-2302/REF-2298 (name E. parviflorum) remain.',
    'chamerion_angustifolium': 'Deep re-sweep (batch 6). REF-2301 (polyphenols of Epilobium angustifolium = fireweed) moved here from E. parviflorum, antioxidant action.',
    'equisetum_arvense': 'Deep re-sweep. Diuretic RCT REF-0041 and EU monograph REF-0083 removed from actions they do not support (anti-inflammatory, anti-rheumatic, antimicrobial; REF-0041 also vulnerary). Notes rewritten.',
    'equisetum_pratense': 'Deep re-sweep. REF-2361 (silver nanoparticles synthesised with Equisetum extracts) is not evidence of the plant\'s own antioxidant action - removed from it, kept in references.',
    'equisetum_sylvaticum': 'Deep re-sweep. REF-2361 (silver nanoparticles) removed from the antioxidant action, kept in references.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 6', os.path.join(HERE, 'deep', 'd06_changes.tsv'), **BIB)
