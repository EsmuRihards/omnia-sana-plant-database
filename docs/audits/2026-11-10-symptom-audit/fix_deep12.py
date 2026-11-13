"""Deep re-sweep of batch 12 (origanum-majorana .. petroselinum-crispum) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3705..REF-3724 (PubMed efetch, deep/abstracts.json).
Cross-batch carries closed here: REF-3434 (herbal cough MA) -> pelargonium cough; REF-2546 (herb NMA) -> passionflower no-effect."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3705', '11679026', 'passifloragad', 'rct'),
    ('REF-3706', '27918731', 'passifloradental', 'rct'),
    ('REF-3707', '39536249', 'guaranafatigue2024', 'meta-analysis'),
    ('REF-3708', '21612429', 'guaranabreastfatigue', 'rct'),
    ('REF-3709', '24237188', 'guaranapc18', 'rct'),
    ('REF-3710', '29190155', 'guaranapc18null', 'rct'),
    ('REF-3711', '19388866', 'guaranaradiation', 'rct'),
    ('REF-3712', '31014293', 'eps7630children', 'meta-analysis'),
    ('REF-3713', '28610802', 'herbalrtichildren', 'meta-analysis'),
    ('REF-3714', '29055287', 'pelargoniumcold', 'rct'),
    ('REF-3715', '22360575', 'eps7630bronchitis', 'rct'),
    ('REF-3716', '23478193', 'eps7630copd', 'rct'),
    ('REF-3717', '23142309', 'eps7630asthma', 'rct'),
    ('REF-3718', '21968667', 'oreganowound', 'rct'),
    ('REF-3719', '31315027', 'ginsenglipids2019', 'meta-analysis'),
    ('REF-3720', '38877862', 'ginsenglipids2024', 'meta-analysis'),
    ('REF-3721', '18754850', 'redginsenged', 'meta-analysis'),
    ('REF-3722', '34638031', 'fsdnaturalproducts', 'meta-analysis'),
    ('REF-3723', '22139546', 'redginsengdiabetes', 'meta-analysis'),
    ('REF-3724', '19584437', 'ginsengalzheimer', 'systematic-review'),
])

BIB = dict(
    retag={'REF-0020': 'narrative-review',   # carvacrol review tagged traditional
           'REF-1908': 'narrative-review',   # Passiflora ethnopharmacology review tagged SR
           'REF-1483': 'narrative-review',   # Petasites genus review tagged SR
           'REF-1875': 'preclinical',        # bronchial epithelial cell study tagged clinical
           'REF-0009': 'preclinical'},       # guarana toxicity/antioxidant lab study tagged traditional
    delete=['REF-2787',    # Oxalis corniculata polysaccharide - a different species
            'REF-2779'],   # ZnO nanoparticles synthesised with leaf extract - not the plant's activity
    new=NEW)

PLAN = {
    'origanum_majorana': [('arm', a, ['REF-0020']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive', 'sedative')] + [
        ('refadd', ['REF-0020']),   # carvacrol is oregano's signature compound, not marjoram's
        ('drop', 'muscle-spasm'),   # gut-hyperactivity calcium-channel study: off-target (inv. 11)
        ('note', 'infection', 'Marjoram essential oil protected against a fungal skin infection (sporotrichosis) in animals (preclinical)'),
    ],
    'origanum_vulgare': [
        ('add', 'wounds', ['REF-3718']), ('add', 'infection', ['REF-3718']),
        ('note', 'wounds', 'An oregano extract ointment reduced bacterial contamination and infection of surgical wounds vs petrolatum in a randomized trial, with similar scarring'),
        ('note', 'infection', 'Oregano oil and carvacrol are antibacterial and antifungal in lab studies (reviews); an oregano ointment reduced surgical-wound infection in a randomized trial, and emulsified oregano oil cleared intestinal parasites in a small uncontrolled study'),
    ],
    'oxalis_stricta': [('purge', 'REF-2787'), ('purge', 'REF-2779')],
    'oxycoccus_palustris': [
        ('note', 'urinary-support', 'Small cranberry\'s proanthocyanidins are reviewed for urinary tract protection (review)'),
        ('note', 'infection', 'Small cranberry extracts were antibacterial in lab tests (review; preclinical)'),
        ('note', 'inflammation', 'Small cranberry reduced inflammation in diabetic mice (preclinical)'),
    ],
    'panax_ginseng': [
        ('arm', 'ergogenic', ['REF-0137']),        # its own conclusion: ginseng does not appear to enhance physical performance
        ('arm', 'neuroprotective', ['REF-1475']),  # a null Cochrane review is not action evidence
        ('nulladd', 'memory', ['REF-1475', 'REF-3724']), ('nulladd', 'cognitive-function', ['REF-3724']),
        ('note', 'cognitive-function', 'Ginseng compounds protected nerve cells in lab and animal studies (review); a Cochrane review found no convincing evidence that ginseng improves cognition, and evidence in Alzheimer\'s disease is scarce and inconclusive'),
        ('note', 'memory', 'Ginseng compounds protected nerve cells in lab and animal studies (review); a Cochrane review and a systematic review found no convincing evidence of better memory or cognition'),
        ('nulladd', 'blood-sugar', ['REF-3723']),
        ('note', 'blood-sugar', 'Blood-sugar lowering effects reviewed (review); a systematic review of red ginseng trials in type 2 diabetes found the evidence not convincing'),
        ('newpair', 'high-cholesterol', ['REF-3719'], 'A 2019 meta-analysis found Panax ginseng lowered total and LDL cholesterol, but a 2024 GRADE-assessed meta-analysis found no significant effect on blood lipids'),
        ('nulladd', 'high-cholesterol', ['REF-3720']),
        ('newpair', 'low-libido', ['REF-3721', 'REF-3722'], 'Red ginseng improved erectile dysfunction in randomized trials (systematic review; suggestive evidence), and Panax ginseng helped female sexual dysfunction in a meta-analysis (preliminary evidence)'),
        ('note', 'fatigue', 'Asian and American ginseng reduced fatigue in people with chronic illness (systematic review)'),
        ('note', 'immune-support', 'Immune effects of ginseng are reviewed (review)'),
        ('note', 'metabolic-support', 'Metabolic effects of ginseng are reviewed (review)'),
        ('note', 'inflammation', 'Anti-inflammatory effects of ginseng are reviewed (review)'),
    ],
    'passiflora_incarnata': [
        ('add', 'anxiety', ['REF-3705', 'REF-3706', 'REF-1911']), ('nulladd', 'anxiety', ['REF-2546']),
        ('note', 'anxiety', 'Passionflower reduced anxiety before surgery and dental extraction in randomized trials (as well as midazolam in one) and matched oxazepam in a small trial in generalized anxiety; a network meta-analysis found no significant effect vs placebo'),
        ('add', 'insomnia', ['REF-1907']), ('add', 'stress', ['REF-1907']),
        ('note', 'insomnia', 'Passionflower improved subjective sleep quality and, on sleep studies, total sleep time vs placebo in randomized trials; traditional use to aid sleep (EU herbal monograph)'),
        ('note', 'stress', 'Traditional use for mild symptoms of mental stress (EU herbal monograph); an extract reduced stress and improved sleep vs placebo in a randomized trial'),
        ('note', 'nervous-tension', 'inferred from anxiolytic action'),
    ],
    'paullinia_cupana': [
        ('arm', 'ergogenic', ['REF-0009']), ('arm', 'neuroprotective', ['REF-0009']),   # a toxicity/antioxidant lab study
        ('arm', 'antioxidant', ['REF-0106']),                                            # an acute behavioural RCT
        ('newpair', 'fatigue', ['REF-3707', 'REF-3708', 'REF-3709'], 'Guarana reduced cancer-related fatigue in some randomized trials and a 2024 meta-analysis, but a 2021 meta-analysis and two other trials found it no better than placebo'),
        ('nulladd', 'fatigue', ['REF-0951', 'REF-3710', 'REF-3711']),
        ('note', 'cognitive-function', 'Guarana improved attention and some cognitive tests in randomized trials and a meta-analysis; how much is due to its caffeine is unknown'),
        ('note', 'memory', 'Guarana improved some memory and attention tasks in a randomized trial, and protected against amyloid toxicity in worms (preclinical)'),
        ('note', 'metabolic-support', 'Guarana reduced fat-cell formation and weight gain in lab and animal studies (preclinical; review)'),
    ],
    'pelargonium_sidoides': [
        ('newpair', 'cough', ['REF-3434'], 'Pelargonium sidoides was superior to placebo for cough frequency and severity (moderate evidence, systematic review and meta-analysis)'),
        ('add', 'bronchitis', ['REF-3715', 'REF-3712']),
        ('note', 'bronchitis', 'EPs 7630 reduced acute bronchitis symptoms and shortened illness in randomized trials and meta-analyses, including in children (Cochrane review: low-quality evidence)'),
        ('add', 'cold', ['REF-3714']),
        ('note', 'cold', 'A high-dose pelargonium extract reduced common cold symptoms and shortened illness in a randomized trial (Cochrane review: very low-quality evidence)'),
        ('add', 'sore-throat', ['REF-3712']),
        ('note', 'sore-throat', 'EPs 7630 eased acute tonsillopharyngitis and bronchitis in children in a meta-analysis of trials'),
        ('add', 'infection', ['REF-3713']),
        ('note', 'infection', 'Moderate evidence of efficacy for respiratory tract infections in children (meta-analysis); antiviral and immune effects in the lab (preclinical)'),
        ('newpair', 'respiratory-support', ['REF-3716'], 'Added to usual treatment, EPs 7630 prolonged time to COPD flare-ups and reduced their frequency vs placebo in a randomized trial'),
        ('newpair', 'asthma', ['REF-3717'], 'EPs 7630 reduced asthma attacks during viral upper respiratory infections in a randomized trial'),
    ],
    'petasites_hybridus': [
        ('arm', 'antihistaminic', ['REF-1483']), ('arm', 'antispasmodic', ['REF-1483']), ('refadd', ['REF-1483']),   # genus-level review
        ('drop', 'muscle-spasm'),   # smooth-muscle antispasmodic (airway, urinary): off-target
        ('note', 'asthma', 'An open, uncontrolled trial of butterbur extract reduced asthma attacks and medication use'),
        ('note', 'headache', 'Butterbur root extract prevented migraine headaches vs placebo in randomized trials'),
    ],
    'petroselinum_crispum': [
        ('note', 'kidney-support', 'Kidney-protective effects reported in animal studies (reviews)'),
        ('note', 'liver-support', 'Parsley extract protected the liver in rats with bile duct obstruction, diabetes or a fructose diet (preclinical; reviews)'),
        ('note', 'urinary-support', 'Parsley increased urine output in rats; traditional diuretic (reviews)'),
    ],
}

NOTES = {
    'origanum_majorana': 'Deep re-sweep. REF-0020 (carvacrol review; carvacrol is oregano\'s signature compound, not marjoram\'s) removed from all six actions, kept in references, retagged narrative-review. Muscle-spasm dropped (gut calcium-channel study; off-target). Not used: PCOS tea RCT REF-1227 (no matching condition); aromatherapy blend for dysmenorrhoea 22435409 (combination).',
    'origanum_vulgare': 'Deep re-sweep. Oregano ointment wound RCT REF-3718 added to wounds and infection. Notes rewritten (no "supports respiratory and gastrointestinal infections" claim without a source).',
    'oxalis_stricta': 'Deep re-sweep. REF-2787 studies Oxalis corniculata (different species) and REF-2779 studies zinc-oxide nanoparticles made with the extract - purged and deleted. No sourced activity remains.',
    'oxycoccus_palustris': 'Deep re-sweep. Notes rewritten. The large cranberry literature on PubMed is American cranberry (Vaccinium macrocarpon) - a different species, not used here (inv. 10).',
    'panax_ginseng': 'Deep re-sweep. REF-0137 removed from the ergogenic action (its conclusion: no enhanced physical performance); Cochrane REF-1475 removed from neuroprotective and recorded as no-effect for memory as well as cognition; AD SR REF-3724 no-effect. Red ginseng T2D SR REF-3723 no-effect for blood-sugar. New pairs (owner rule): high-cholesterol (2019 MA REF-3719; 2024 GRADE MA REF-3720 no-effect), low-libido (ED SR REF-3721, FSD MA REF-3722).',
    'passiflora_incarnata': 'Deep re-sweep. GAD RCT REF-3705, dental RCT REF-3706 and held spinal-anaesthesia RCT REF-1911 added to anxiety; herb NMA REF-2546 (passionflower not significant in the summary network) recorded as no-effect (batch-8 carry). Held stress/sleep RCT REF-1907 wired to insomnia and stress. REF-1908 retagged narrative-review.',
    'paullinia_cupana': 'Deep re-sweep. REF-0009 (toxicity/antioxidant lab study) retagged preclinical and removed from ergogenic/neuroprotective; REF-0106 removed from antioxidant. New pair (owner rule): fatigue (2024 MA REF-3707, RCTs REF-3708/REF-3709), with held 2021 MA REF-0951 and RCTs REF-3710/REF-3711 recorded as no-effect.',
    'pelargonium_sidoides': 'Deep re-sweep. New pairs (owner rule): cough (herbal cough MA REF-3434, batch-2 carry), respiratory-support (COPD RCT REF-3716), asthma (RCT REF-3717). Bronchitis RCT REF-3715 and children MA REF-3712, cold RCT REF-3714, children RTI MA REF-3713 added. REF-1875 retagged preclinical.',
    'petasites_hybridus': 'Deep re-sweep. Genus review REF-1483 retagged narrative-review and removed from both actions (kept in references). Muscle-spasm dropped (smooth-muscle antispasmodic; off-target). Notes rewritten.',
    'petroselinum_crispum': 'Deep re-sweep. Notes rewritten to their (preclinical/review) sources. No clinical trials found.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 12', os.path.join(HERE, 'deep', 'd12_changes.tsv'), **BIB)
