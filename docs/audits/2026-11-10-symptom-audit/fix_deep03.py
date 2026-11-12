"""Deep re-sweep of batch 3 (asclepias-tuberosa .. campanula-persicifolia) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: a new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
systematic reviews of lab/animal studies keep scoring as systematic reviews (owner answer, batch 3).
New refs REF-3449..REF-3484 (abstracts verbatim from PubMed efetch, cached in deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3449', '40302232', 'astragaluscrf', 'meta-analysis'),
    ('REF-3450', '38834234', 'astragaluscovidfatigue', 'rct'),
    ('REF-3451', '39465324', 'astragaluspg2fatigue', 'rct'),
    ('REF-3452', '37952511', 'astragalusimmunema', 'meta-analysis'),
    ('REF-3453', '34271953', 'astragalusathletes', 'rct'),
    ('REF-3454', '42197058', 'astragalusresistance', 'rct'),
    ('REF-3455', '37433206', 'astragalust2dm', 'meta-analysis'),
    ('REF-3456', '22747190', 'bacopasr', 'systematic-review'),
    ('REF-3457', '20590480', 'bacopamemory', 'rct'),
    ('REF-3458', '12093601', 'brahmimemory', 'rct'),
    ('REF-3459', '18078406', 'borageundershirts', 'rct'),
    ('REF-3460', '14670885', 'borageeczema', 'rct'),
    ('REF-3461', '34606560', 'borageoillipids', 'rct'),
    ('REF-3462', '8214997', 'boragegla', 'rct'),
    ('REF-3463', '39314013', 'boswelliama', 'meta-analysis'),
    ('REF-3464', '39449720', 'boswelliat2dm', 'meta-analysis'),
    ('REF-3465', '30676012', 'casperomeibs', 'rct'),
    ('REF-3466', '26502867', 'casperomeasthma', 'rct'),
    ('REF-3467', '35565826', 'casperomediarrhea', 'rct'),
    ('REF-3468', '30670277', 'frankincensehmb', 'rct'),
    ('REF-3469', '35751891', 'kundurvvc', 'rct'),
    ('REF-3470', '35385330', 'kvietbi', 'rct'),
    ('REF-3471', '25967706', 'boswelliacream', 'rct'),
    ('REF-3472', '15084618', 'calendularadiation', 'rct'),
    ('REF-3473', '25992820', 'calendularadiodermatitis', 'rct'),
    ('REF-3474', '41527980', 'calendulacontact', 'rct'),
    ('REF-3475', '22606064', 'calenduladiaper', 'rct'),
    ('REF-3476', '32965030', 'calendulasorbolene', 'rct'),
    ('REF-3477', '34674610', 'calendulahandwounds', 'rct'),
    ('REF-3478', '23803878', 'greenteaglucose', 'meta-analysis'),
    ('REF-3479', '33285391', 'greenteat2dm', 'meta-analysis'),
    ('REF-3480', '23780706', 'teacvdcochrane', 'systematic-review'),
    ('REF-3481', '22027055', 'greenteacholesterol', 'meta-analysis'),
    ('REF-3482', '40497293', 'greenteabp', 'meta-analysis'),
    ('REF-3483', '23235664', 'greenteaweightcochrane', 'systematic-review'),
    ('REF-3484', '32372444', 'greenteaobesity', 'meta-analysis'),
])

BIB = dict(
    retag={'REF-2262': 'narrative-review'},   # Astragalus polysaccharide review tagged preclinical
    delete=['REF-0494',   # Naturopathic Herbalist page: no checkable references (batch-9 rule); replaced by Grieve
            'REF-0411',   # WebMD bistort page, 404 since batch 3 - purged from the actions too
            'REF-2817'],  # Campanula alliariifolia study - wrong species
    new=NEW,
)

BIRCH_0080 = ['anti-inflammatory', 'anti-rheumatic', 'anticancer', 'antidiabetic', 'antimicrobial', 'antioxidant',
              'antiviral', 'emollient', 'gastroprotective']

PLAN = {
    'asclepias_tuberosa': [
        ('add', 'respiratory-support', ['REF-0098']),
        ('purge', 'REF-0494'),
        ('aadd', 'diaphoretic', ['REF-0098']), ('aadd', 'expectorant', ['REF-0098']),
        ('note', 'respiratory-support', 'Traditional remedy for chest complaints and pulmonary catarrh, aiding expectoration (Grieve, A Modern Herbal)'),
    ],
    'astragalus_membranaceus': [
        ('add', 'fatigue', ['REF-3449', 'REF-3450']), ('nulladd', 'fatigue', ['REF-3451']),
        ('add', 'immune-support', ['REF-3452', 'REF-3453']),
        ('add', 'inflammation', ['REF-3452', 'REF-3454']),
        ('newpair', 'blood-sugar', ['REF-3455'], 'Add-on Astragalus lowered fasting and after-meal glucose and HbA1c in type 2 diabetes (meta-analysis of randomized trials; evidence of limited certainty)'),
        ('arm', 'nephroprotective', ['REF-0586']), ('refadd', ['REF-0586']),
        ('note', 'cold', 'inferred from immunomodulator action'),
        ('note', 'fatigue', 'Reduced fatigue after stroke and in cancer patients in meta-analyses of trials (low-quality evidence) and in a trial in nurses with post-COVID fatigue; an Astragalus polysaccharide infusion did not reduce chemotherapy fatigue overall'),
        ('note', 'immune-support', 'Strengthened cellular immune markers in a meta-analysis of human studies and limited exercise-induced immune suppression in athletes (randomized trial)'),
        ('note', 'infection', 'Astragalus polysaccharide\'s immune effects are studied for infections (review of lab and animal studies)'),
        ('note', 'inflammation', 'Lowered pro-inflammatory cytokines in a meta-analysis of human studies and during intensive training in a randomized trial'),
    ],
    'bacopa_monnieri': [
        ('purge', 'REF-0309'),   # WHO 2002 vol. 2 has no Bacopa monograph
        ('add', 'cognitive-function', ['REF-2107']),
        ('add', 'memory', ['REF-3456', 'REF-3457', 'REF-3458']),
        ('newpair', 'anxiety', ['REF-0740'], 'Anxiety scores fell in older adults taking Bacopa for 12 weeks (and rose on placebo) in a randomized trial; another trial found no change in anxiety'),
        ('nulladd', 'anxiety', ['REF-3458']),
        ('newpair', 'depression', ['REF-0740'], 'Depression scores fell in older adults taking Bacopa for 12 weeks (and rose on placebo) in a randomized trial'),
        ('note', 'cognitive-function', 'Improved attention and processing speed in a meta-analysis of randomized trials, and cognitive performance in older adults in placebo-controlled trials'),
        ('note', 'memory', 'Improved memory recall and retention in randomized trials in healthy adults and older people (systematic review)'),
    ],
    'betula_pendula': [('arm', a, ['REF-0080']) for a in BIRCH_0080] + [
        ('add', 'arthritis', ['REF-0743', 'REF-1692']), ('add', 'inflammation', ['REF-1692']),
        ('mexcl', 'back-pain', ['REF-1692']),   # off-target: rheumatoid-arthritis lymphocyte study offered for back pain
        ('mexcl', 'infection', ['REF-0743']), ('mexcl', 'wounds', ['REF-0743']),   # genus-level, prose-only attribution
        ('mexcl', 'inflammation', ['REF-0743']), ('mexcl', 'skin-irritation', ['REF-0743']),
        ('note', 'urinary-support', 'Used to increase urine flow and flush the urinary tract in minor urinary complaints (EMA summary)'),
        ('note', 'cancer', 'Compounds from birch buds induced apoptosis in digestive-system cancer cells (preclinical)'),
        ('note', 'arthritis', 'Leaf extract slowed inflammatory lymphocytes (a rationale for rheumatoid arthritis) and birch has been studied for degenerative joint disease (preclinical; genus review)'),
        ('note', 'inflammation', 'Leaf extract slowed the growth of inflammatory lymphocytes in the lab (preclinical)'),
    ],
    'bistorta_officinalis': [
        ('purge', 'REF-0411'),
        ('arm', 'antimicrobial', ['REF-0627']),   # GC-MS chemistry only
        ('note', 'infection', 'Root infusion was antibacterial in lab tests (preclinical)'),
        ('note', 'skin-irritation', 'Root infusion showed antibacterial and anti-inflammatory activity relevant to inflamed skin, supporting traditional topical use (preclinical)'),
        ('note', 'inflammation', 'Root infusion reduced inflammatory mediators in lab tests (preclinical)'),
        ('note', 'wounds', 'inferred from antimicrobial action: an extract reduced the virulence of the wound pathogen Pseudomonas in the lab (preclinical)'),
    ],
    'borago_officinalis': [
        ('purge', 'REF-0309'),   # WHO 2002 vol. 2 has no borage monograph
        ('add', 'eczema', ['REF-3459']), ('nulladd', 'eczema', ['REF-0447', 'REF-3460']),
        ('newpair', 'high-cholesterol', ['REF-3461'], 'Borage oil lowered triglycerides and raised HDL cholesterol in a randomized trial in overweight young adults; total and LDL cholesterol did not change'),
        ('add', 'arthritis', ['REF-3462']),
        ('newpair', 'asthma', ['REF-1952'], 'Borage extract improved asthma symptoms (but not airway inflammation markers) in a phase II placebo-controlled trial'),
        ('arm', 'anti-inflammatory', ['REF-1952']), ('nulladd', 'inflammation', ['REF-1952']),
        ('mexcl', 'immune-support', ['REF-1958']),   # the study showed inflammasome suppression, not immune support
        ('note', 'arthritis', 'Borage seed oil (gamma-linolenic acid) reduced rheumatoid arthritis signs and symptoms vs placebo in a 24-week randomized trial'),
        ('note', 'eczema', 'Undershirts coated with borage oil eased itch and redness of mild atopic dermatitis in a small placebo-controlled trial; oral borage oil did not help eczema (Cochrane review; large trial)'),
        ('note', 'cold', 'Traditional remedy for colds and influenza (narrative review)'),
        ('note', 'inflammation', 'Anti-inflammatory activity in lab and animal studies (narrative review); in an asthma trial borage did not lower airway inflammation markers'),
        ('note', 'respiratory-support', 'Traditionally used for respiratory disorders (narrative review)'),
        ('note', 'cancer', 'Borage extracts protected DNA and showed anticarcinogenic effects in lab studies (preclinical)'),
    ],
    'boswellia_serrata': [
        ('add', 'arthritis', ['REF-1810', 'REF-3463']), ('add', 'pain', ['REF-1810', 'REF-3463']),
        ('newpair', 'blood-sugar', ['REF-3464'], 'Boswellia improved blood glucose markers and blood lipids in type 2 diabetes (meta-analysis of randomized trials)'),
        ('newpair', 'ibs', ['REF-3465'], 'A lecithin form of Boswellia extract (Casperome) improved IBS symptoms in a randomized study'),
        ('newpair', 'asthma', ['REF-3466'], 'A lecithin form of Boswellia extract (Casperome) reduced the need for inhaled asthma medication in a randomized add-on study'),
        ('newpair', 'diarrhea', ['REF-3467'], 'A lecithin form of Boswellia extract (Casperome) shortened acute diarrhoea and reduced stool frequency in a randomized study'),
        ('newpair', 'heavy-bleeding', ['REF-3468'], 'Frankincense (Boswellia serrata resin) reduced heavy menstrual bleeding vs placebo in a randomized trial'),
        ('newpair', 'infection', ['REF-3469'], 'Boswellia serrata vaginal preparation improved thrush symptoms as much as clotrimazole in a randomized trial'),
        ('newpair', 'cognitive-function', ['REF-3470'], 'A Boswellia extract improved memory and processing-speed tests vs placebo in a pilot trial after traumatic brain injury'),
        ('add', 'skin-irritation', ['REF-3471']),
        ('note', 'arthritis', 'Reduced osteoarthritis pain and stiffness and improved function in meta-analyses and randomized trials (from about 4 weeks of use)'),
        ('note', 'pain', 'Relieved osteoarthritis joint pain in meta-analyses and randomized trials'),
        ('note', 'inflammation', 'Boswellia extract reduced inflammatory markers and knee osteoarthritis symptoms in a placebo-controlled trial; boswellic acids inhibit inflammatory enzymes in lab studies'),
        ('note', 'skin-irritation', 'A Boswellia cream reduced radiotherapy skin redness and the need for steroid creams in a randomized trial in breast cancer'),
    ],
    'calendula_officinalis': [
        ('add', 'skin-irritation', ['REF-3472', 'REF-3473', 'REF-3474', 'REF-3475']), ('nulladd', 'skin-irritation', ['REF-3476']),
        ('add', 'wounds', ['REF-3477']),
        ('add', 'infection', ['REF-0754']),
        ('note', 'skin-irritation', 'Calendula cream prevented radiation dermatitis better than trolamine and essential fatty acids in randomized trials and helped diaper and contact dermatitis; one trial found no difference from a standard moisturiser'),
        ('note', 'wounds', 'Calendula sped healing of hand wounds and, taken orally, of second-degree burns in randomized trials; a systematic review found some benefit, though trials in burns and diabetic ulcers did not'),
        ('note', 'infection', 'Calendula vaginal cream cleared thrush less often than clotrimazole at 2 weeks but more often at 1 month in a randomized trial'),
    ],
    'camellia_sinensis': [
        ('add', 'blood-sugar', ['REF-3478']), ('nulladd', 'blood-sugar', ['REF-3479']),
        ('add', 'cardiovascular-support', ['REF-3480']),
        ('newpair', 'high-cholesterol', ['REF-3481', 'REF-3480'], 'Green tea catechins lowered total and LDL cholesterol in meta-analyses of randomized trials'),
        ('newpair', 'high-blood-pressure', ['REF-3482', 'REF-3480'], 'Green tea modestly lowered blood pressure in meta-analyses of randomized trials'),
        ('add', 'metabolic-support', ['REF-3484']), ('nulladd', 'metabolic-support', ['REF-3483']),
        ('note', 'blood-sugar', 'Green tea lowered fasting glucose and HbA1c in a meta-analysis of 17 trials; a meta-analysis limited to type 2 diabetes found no significant effect'),
        ('note', 'cancer', 'Tea compounds slowed bladder cancer cells in lab studies (review); a Cochrane review found inconsistent, limited evidence that drinking green tea lowers cancer risk'),
        ('note', 'cardiovascular-support', 'Green tea lowered LDL cholesterol and blood pressure in a Cochrane review of short trials; long-term heart outcomes are unstudied'),
        ('note', 'cognitive-function', 'L-theanine, an amino acid found in tea, increased brain alpha activity linked to relaxed alertness in a small trial (compound evidence)'),
        ('note', 'metabolic-support', 'Green tea improved weight and waist measures in a 2020 meta-analysis, but a Cochrane review found only a small, non-significant weight loss'),
    ],
    'campanula_persicifolia': [
        ('purge', 'REF-2817'),
        ('arm', 'anti-inflammatory', ['REF-2816']), ('arm', 'antimicrobial', ['REF-2816']), ('arm', 'antioxidant', ['REF-2816']),
        ('refadd', ['REF-2816']),
    ],
}

NOTES = {
    'asclepias_tuberosa': 'Deep re-sweep. The Naturopathic Herbalist page REF-0494 (checked 2026-11-12) cites no checkable references (only a pointer to the author\'s unnamed textbook) - not a source (batch-9 rule); purged and deleted. Replaced by Grieve REF-0098 (Pleurisy Root, botanical.com/botanical/mgmh/p/pleuri52.html: chest complaints, pulmonary catarrh, assisting expectoration, perspiration in fever and pleurisy, diarrhoea, dysentery, rheumatism, eczema) for respiratory-support and the diaphoretic/expectorant actions. Bronchitis and cold kept as inferred-only pairs (Grieve names expectoration and perspiration, not these conditions). Gap: Grieve\'s diarrhoea/rheumatism/eczema uses have no pairs (traditional only, no SR/RCT).',
    'astragalus_membranaceus': 'Deep re-sweep. Added: cancer-related-fatigue MA REF-3449 ("supportive", low quality), post-COVID fatigue RCT REF-3450; PG2 (Astragalus polysaccharide) chemotherapy-fatigue RCT REF-3451 (no significant difference overall) recorded as no-effect. Human-studies immune MA REF-3452 (immune-support, inflammation), athlete RCT REF-3453 (immune-support), resistance-training RCT REF-3454 (TNF-alpha, IL-6; inflammation). New blood-sugar pair from adjuvant-T2DM MA REF-3455 (owner rule). Cochrane CKD REF-0586 ("definitive conclusions could not be made") removed from the nephroprotective action (inv. 7) and kept in references. REF-2262 retagged narrative-review. Cold note now states its inference.',
    'bacopa_monnieri': 'Deep re-sweep. REF-0309 (WHO 2002 vol. 2, no Bacopa monograph) purged from the actions. MA REF-2107 moved to direct for cognitive-function. Memory: Pase 2012 SR REF-3456, Morgan 2010 RCT REF-3457, Roodenrys 2002 RCT REF-3458 added. New anxiety and depression pairs from Calabrese 2008 REF-0740 (STAI and CESD-10 fell vs placebo; owner rule); Roodenrys 2002 (anxiety unaffected) recorded as no-effect for anxiety. Not added: Bacumen 2025 RCT (no cognitive benefit; stress/fatigue secondary), MCI sleep RCT (no effect on sleep - no insomnia pair exists).',
    'betula_pendula': 'Deep re-sweep. EMA public summary REF-0080 (urinary flushing only) was filed under 10 actions - removed from all but diuretic. Genus review REF-0743 names B. pendula only for degenerative joint disease: direct for arthritis, hidden elsewhere (prose-only genus claims) - infection and wounds dropped. REF-1692 (inflammatory lymphocytes; rationale for RA) direct for arthritis and inflammation; back-pain dropped (off-target, inv. 11). REF-1695 is B. pendula subsp. mandshurica (accepted infraspecific taxon) - kept.',
    'bistorta_officinalis': 'Deep re-sweep. WebMD page REF-0411 (404) purged from the actions and deleted. GC-MS study REF-0627 removed from the antimicrobial action (chemistry only; kept in references). Notes rewritten; wounds is inferred from anti-virulence activity against Pseudomonas (REF-0747). No trials on PubMed.',
    'borago_officinalis': 'Deep re-sweep. REF-0309 (WHO 2002 vol. 2, no borage monograph) purged. Eczema: undershirt RCT REF-3459 (topical, positive) added; Cochrane REF-0447 and Takwale 2003 RCT REF-3460 (oral borage oil, no benefit) recorded as no-effect. Arthritis: Leventhal 1993 RCT REF-3462 (GLA in borage seed oil, RA) added. New pairs (owner rule): high-cholesterol (REF-3461, TG and HDL only), asthma (REF-1952). REF-1952 also found no fall in airway inflammation - removed from the anti-inflammatory action, recorded as no-effect for inflammation. Immune-support dropped: its only card REF-1958 showed inflammasome suppression. Not added: Zurier 1996 GLA RA trial (abstract names no source plant).',
    'boswellia_serrata': 'Deep re-sweep. Aflapin RCT REF-1810 moved to direct and 2024 MA REF-3463 added for arthritis and pain; the note no longer claims rheumatoid arthritis (no RA source). Radiotherapy-cream RCT REF-3471 added to skin-irritation. New pairs (owner rule, RCT/MA with benefit): blood-sugar REF-3464, ibs REF-3465, asthma REF-3466, diarrhea REF-3467 (Casperome studies), heavy-bleeding REF-3468, infection REF-3469 (VVC), cognitive-function REF-3470 (TBI pilot). Not added: collagenous-colitis Cochrane 29127772 ("uncertain"), B. carteri episiotomy trial (other species).',
    'calendula_officinalis': 'Deep re-sweep. Skin-irritation was inferred only although trials exist: Pommier 2004 phase III REF-3472, 2015 RCT REF-3473, 2025 contact-dermatitis RCT REF-3474 and diaper-dermatitis RCT REF-3475 added; 2021 radiation RCT REF-3476 (no difference from sorbolene) recorded as no-effect. Hand-wound RCT REF-3477 added to wounds. Held VVC RCT REF-0754 wired to infection. Owner answer (batch 3): systematic reviews of lab/animal studies keep scoring as SRs - REF-2124 (cancer) left as tagged.',
    'camellia_sinensis': 'Deep re-sweep (targeted "green tea" title searches; the binomial search misses most trials). Added: Liu 2013 glucose MA REF-3478 (blood-sugar; T2DM-only MA REF-3479 null recorded), Cochrane 2013 tea/CVD REF-3480, cholesterol MA REF-3481 and BP MA REF-3482 (new high-cholesterol and high-blood-pressure pairs, owner rule), obesity MA REF-3484 (metabolic-support); Cochrane 2012 weight-loss review REF-3483 ("small, statistically non-significant") recorded as no-effect. Cognitive note labels L-theanine as compound evidence.',
    'campanula_persicifolia': 'Deep re-sweep. REF-2817 (Campanula alliariifolia antioxidant study) purged and deleted as wrong species. Genus review REF-2816 never names C. persicifolia - removed from the three actions (prose-only genus claims), kept in references as background. The plant now has no species-level action evidence.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 3', os.path.join(HERE, 'deep', 'd03_changes.tsv'), **BIB)
