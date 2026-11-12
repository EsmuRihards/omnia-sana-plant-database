"""Batch-13 fixes (2026-11-10 symptom audit): pimpinella-anisum .. prunus-africana. Run from the repo root.
Deeper pass (owner request 2026-11-12): beyond "does the source name the symptom", also checked mechanistic
plausibility, safety vs claims, species/part confusion, missing landmark and null trials, claim-note accuracy.
New owner policy (DATA_PRINCIPLES inv. 11, 2026-11-12): a mechanistic-only pair is dropped when the plant's own
evidence contradicts the mechanism or the action evidence concerns an unrelated target.
New refs REF-3397..REF-3402 (abstracts verbatim from PubMed efetch, italics kept: batch13_abstracts.json)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

HERE = os.path.dirname(__file__)
ABS = {k: v['abstract'] for k, v in json.load(open(os.path.join(HERE, 'batch13_abstracts.json'), encoding='utf-8')).items()}
UNVER = 'removed from every symptom as unverifiable'


def ref(key, rid, author, title, journal, year, vol, num, pages, doi, pmid, st):
    f = [('author', author), ('title', title), ('journal', journal), ('year', year)]
    f += [(k, v) for k, v in (('volume', vol), ('number', num), ('pages', pages)) if v]
    f += [('doi', doi), ('pmid', pmid), ('note', rid), ('study_type', st), ('abstract', ABS[pmid])]
    return key, (rid, f)


NEW = dict([
    ref('sarris2020kavagad', 'REF-3397',
        'Sarris, J., Byrne, G.J., Bousman, C.A., Cribb, L., Savage, K.M., Holmes, O., Murphy, J., Macdonald, P., '
        'Short, A., Nazareth, S., Jennings, E., Thomas, S.R., Ogden, E., Chamoli, S., Scholey, A. and Stough, C.',
        'Kava for generalised anxiety disorder: A 16-week double-blind, randomised, placebo-controlled study',
        'The Australian and New Zealand Journal of Psychiatry', '2020', '54', '3', '288--297',
        '10.1177/0004867419891246', '31813230', 'rct'),
    ref('sarris2013kavagad', 'REF-3398',
        'Sarris, J., Stough, C., Bousman, C.A., Wahid, Z.T., Murray, G., Teschke, R., Savage, K.M., Dowell, A., '
        'Ng, C. and Schweitzer, I.',
        'Kava in the treatment of generalized anxiety disorder: a double-blind, randomized, placebo-controlled study',
        'Journal of Clinical Psychopharmacology', '2013', '33', '5', '643--648',
        '10.1097/JCP.0b013e318291be67', '23635869', 'rct'),
    ref('dicks2020oyster', 'REF-3399', 'Dicks, L. and Ellinger, S.',
        'Effect of the Intake of Oyster Mushrooms (Pleurotus ostreatus) on Cardiometabolic Parameters-A Systematic '
        'Review of Clinical Trials', 'Nutrients', '2020', '12', '4', '1134',
        '10.3390/nu12041134', '32316680', 'systematic-review'),
    ref('bergendiova2011pleuran', 'REF-3400', 'Bergendiova, K., Tibenska, E. and Majtan, J.',
        'Pleuran (β-glucan from Pleurotus ostreatus) supplementation, cellular immune response and respiratory '
        'tract infections in athletes', 'European Journal of Applied Physiology', '2011', '111', '9', '2033--2040',
        '10.1007/s00421-011-1837-z', '21249381', 'rct'),
    ref('jesenak2013pleuran', 'REF-3401',
        'Jesenak, M., Majtan, J., Rennerova, Z., Kyselovic, J., Banovcin, P. and Hrubisko, M.',
        'Immunomodulatory effect of pleuran (β-glucan from Pleurotus ostreatus) in children with recurrent '
        'respiratory tract infections', 'International Immunopharmacology', '2013', '15', '2', '395--399',
        '10.1016/j.intimp.2012.11.020', '23261366', 'rct'),
    ref('huber2007tormentil', 'REF-3402',
        'Huber, R., Ditfurth, A.V., Amann, F., Güthlin, C., Rostock, M., Trittler, R., Kümmerer, K. and Merfort, I.',
        'Tormentil for active ulcerative colitis: an open-label, dose-escalating study',
        'Journal of Clinical Gastroenterology', '2007', '41', '9', '834--838',
        '10.1097/MCG.0b013e31804b2173', '17881930', 'clinical'),
])

BIB = dict(
    retag={'REF-0364': 'narrative-review', 'REF-0354': 'narrative-review', 'REF-0368': 'preclinical',
           'REF-0633': 'preclinical', 'REF-2597': 'narrative-review', 'REF-2598': 'narrative-review',
           'REF-0973': 'narrative-review', 'REF-0975': 'narrative-review', 'REF-0977': 'narrative-review',
           'REF-0978': 'preclinical', 'REF-0659': 'narrative-review', 'REF-1508': 'narrative-review'},
    # REF-2463 was the KADSS *protocol* paper (no results); repointed to the KADSS results paper (same trial).
    sets={'REF-2463': {'author': 'Sarris, J., Kavanagh, D.J., Byrne, G., Bone, K.M., Adams, J. and Deed, G.',
                       'title': 'The Kava Anxiety Depression Spectrum Study (KADSS): a randomized, placebo-controlled '
                                'crossover trial using an aqueous extract of Piper methysticum',
                       'journal': 'Psychopharmacology', 'volume': '205', 'number': '3', 'pages': '399--407',
                       'doi': '10.1007/s00213-009-1549-9', 'pmid': '19430766', 'abstract': ABS['19430766']}},
    delete=['REF-0102',   # edible-mushroom CVD review naming no species (purged)
            'REF-0306',   # "Wicke 2007" primula: no journal/DOI, not in PubMed, OpenAlex or Crossref
            'REF-0314',   # "Yang 2007" self-heal antiviral: no journal/DOI, not in PubMed, OpenAlex or Crossref
            'REF-0018',   # general essential-oil review naming no pine species (purged; orphaned)
            'REF-2882',   # PV-1, a multi-herb mixture containing self-heal
            'REF-0967',   # Balkan wound-plant review, never names ribwort
            'REF-0968',   # aucubin review naming Plantago asiatica, not ribwort
            'REF-2544',   # Pittler & Ernst 2000 MA, superseded by their Cochrane review REF-2462 (inv. 11)
            'REF-2592'],  # commentary on the Huber 2007 trial; replaced by the trial itself (REF-3402)
    new=NEW,
)

GRIEVE_PINE_RM = ('bronchitis', 'cough', 'uti', 'swelling', 'inflammation', 'wounds')
PRUN_GRIEVE_RM = ('arthritis', 'cold', 'immune-support', 'infection', 'inflammation', 'skin-irritation')
PRUN_PSOTOVA_RM = ('arthritis', 'bruising', 'cold', 'immune-support', 'skin-irritation', 'wounds')

PLAN = {
    'pimpinella_anisum': [
        ('rm', 'skin-irritation', ['REF-1408']),
        ('note', 'wounds', 'Topical seed extract sped wound healing in diabetic rats (preclinical)'),
        ('note', 'infection', 'Seed extract was active against the gut parasite Giardia in the lab (preclinical)'),
        ('note', 'cancer', 'Seed extract reduced chemically induced colorectal tumours in rats (preclinical)'),
    ],
    'pinus_sylvestris': [('purge', 'REF-0018'), ('purge', 'REF-1242')]
      + [('rm', c, ['REF-0098']) for c in GRIEVE_PINE_RM]
      + [('add', 'inflammation', ['REF-0633']), ('mexcl', 'inflammation', ['REF-1234']),
         ('nulladd', 'inflammation', ['REF-1242']), ('nulladd', 'wounds', ['REF-1242']),
         ('mexcl', 'wounds', ['REF-1233', 'REF-1241']),   # off-target: oil vs gonorrhoea / Cryptococcus (inv. 11)
         ('note', 'arthritis', 'Traditional remedy for rheumatic complaints (Grieve, A Modern Herbal)'),
         ('note', 'infection', 'Traditional antiseptic use of pine preparations (Grieve, A Modern Herbal)'),
         ('note', 'skin-irritation', 'Pine tar was used traditionally for eczema and other skin complaints (Grieve, A Modern Herbal)'),
         ('note', 'urinary-support', 'Traditional remedy for bladder and kidney complaints (Grieve, A Modern Herbal)'),
         ('note', 'inflammation', 'Needle extract reduced nitric oxide production by inflamed immune cells in the lab (preclinical); a study of the essential oil found no anti-inflammatory effect'),
         ('note', 'cancer', 'Needle extract and oil were selectively toxic to hormone-insensitive breast cancer cells in the lab (preclinical)')],
    'piper_methysticum': [
        ('merge', 'REF-2544', 'REF-2462'),
        ('add', 'anxiety', ['REF-3398']), ('nulladd', 'anxiety', ['REF-3397']),
        ('rm', 'stress', ['REF-2462', 'REF-2463']),
        ('rm', 'nervous-tension', ['REF-2462']),
        ('rm', 'insomnia', ['REF-2460']),
        ('note', 'anxiety', 'Reduced anxiety versus placebo in meta-analyses and short trials of kava extract; a larger 16-week trial in generalised anxiety disorder found no benefit'),
    ],
    'plantago_lanceolata': [('purge', 'REF-0968'), ('purge', 'REF-0967'),
        ('rm', 'arthritis', ['REF-0633']),
        ('rm', 'bronchitis', ['REF-0499']), ('add', 'bronchitis', ['REF-0358']),
        ('rm', 'bruising', ['REF-0500']),
        ('rm', 'cold', ['REF-0499', 'REF-0500']),
        ('rm', 'cough', ['REF-0500']), ('add', 'cough', ['REF-0358']),
        ('rm', 'immune-support', ['REF-0500']),
        ('rm', 'infection', ['REF-0500']),
        ('add', 'inflammation', ['REF-0500']),
        ('rm', 'skin-irritation', ['REF-0500']), ('add', 'skin-irritation', ['REF-0358']),
        ('rm', 'sore-throat', ['REF-0633']), ('add', 'sore-throat', ['REF-0500', 'REF-0358']),
        ('add', 'wounds', ['REF-0358']),
        ('note', 'infection', 'Leaf and root extracts were antibacterial in the lab, including against the Lyme disease bacterium (preclinical)'),
        ('note', 'skin-irritation', 'Traditionally applied to dry, inflamed rashes (Herbal Reality)')],
    'plantago_major': [('purge', 'REF-0309'), ('purge', 'REF-1762'),
        ('nulladd', 'inflammation', ['REF-1762']),
        ('rm', 'arthritis', ['REF-0364']),
        ('rm', 'bronchitis', ['REF-0364']),
        ('rm', 'bruising', ['REF-0364', 'REF-0368']),
        ('rm', 'constipation', ['REF-0358']), ('add', 'constipation', ['REF-1758']),
        ('add', 'cough', ['REF-1758']),
        ('add', 'diarrhea', ['REF-0354', 'REF-0098']),
        ('add', 'infection', ['REF-0358']),
        ('add', 'inflammation', ['REF-0354', 'REF-1758']),
        ('add', 'skin-irritation', ['REF-0358', 'REF-0098']),
        ('rm', 'sore-throat', ['REF-0358']),
        ('note', 'constipation', 'Traditional remedy for constipation in Persian medicine; laxative activity reported (narrative review)'),
        ('note', 'infection', 'Antibacterial and antiviral activity reported in lab studies; used traditionally for mild infections such as cystitis and sinusitis'),
        ('note', 'inflammation', 'Leaf extracts reduced inflammation in rodent and cell studies (preclinical; reviews); a mouth-rinse trial for chemotherapy mouth sores found no benefit'),
        ('note', 'respiratory-support', 'Traditional remedy for catarrh, coughs and other respiratory complaints'),
        ('note', 'skin-irritation', 'Traditional remedy for inflamed skin and rashes (Grieve; Herbal Reality; review of folk use)'),
        ('note', 'bronchitis', 'Traditionally used in mild bronchitis (Herbal Reality)'),
        ('note', 'bruising', 'Traditionally applied in salves for bruises and wounds (Herbal Reality)'),
        ('note', 'wounds', 'Traditional wound herb; leaf extracts aided cell migration and burn-wound healing in lab and rat studies (preclinical)'),
        ('note', 'cardiovascular-support', 'Plantamajoside, a signature compound of plantain, protected heart cells and reduced cardiac fibrosis in lab and mouse studies (compound evidence, preclinical)')],
    'pleurotus_ostreatus': [('purge', 'REF-0102'),
        ('add', 'blood-sugar', ['REF-3399']), ('add', 'metabolic-support', ['REF-3399']),
        ('add', 'cardiovascular-support', ['REF-3399']),
        ('rm', 'cancer', ['REF-2596']),
        ('add', 'cold', ['REF-3400', 'REF-3401']), ('add', 'immune-support', ['REF-3400', 'REF-3401']),
        ('note', 'blood-sugar', 'Eating oyster mushroom lowered fasting and after-meal blood glucose in clinical trials (systematic review; low-quality evidence)'),
        ('note', 'metabolic-support', 'Eating oyster mushroom improved blood glucose and blood lipids in clinical trials; body weight did not change (systematic review; low-quality evidence)'),
        ('note', 'cardiovascular-support', 'Eating oyster mushroom lowered cholesterol and triglycerides, and in some trials blood pressure (systematic review; low-quality evidence)'),
        ('note', 'cold', 'Pleuran, the beta-glucan from oyster mushroom, reduced respiratory infection symptoms in placebo-controlled trials in athletes and children (compound evidence)'),
        ('note', 'immune-support', 'Pleuran, the beta-glucan from oyster mushroom, raised natural killer cell counts and shifted immune markers in placebo-controlled trials (compound evidence)'),
        ('note', 'cancer', 'Oyster mushroom extracts and polysaccharides slowed cancer cell growth in lab studies (preclinical; reviews)')],
    'potentilla_erecta': [('merge', 'REF-2592', 'REF-3402'),
        ('rm', 'diarrhea', ['REF-0970']),
        ('rm', 'skin-irritation', ['REF-0521']), ('rm', 'wounds', ['REF-0521']),
        ('rm', 'sore-throat', ['REF-0976', 'REF-2594']),
        ('mexcl', 'arthritis', ['REF-0973']),   # contradicted: REF-3402 found tormentil tannins are not absorbed (inv. 11)
        ('note', 'skin-irritation', 'Topical extract showed anti-inflammatory and skin-blanching effects in lab tests; used in dermatology for atopic dermatitis and rosacea (preclinical; review)'),
        ('note', 'ibd', 'In a small open-label study in active ulcerative colitis, disease activity fell during tormentil extract treatment; ESCOP lists adjuvant use in colitis (limited evidence)')],
    'primula_veris': [('purge', 'REF-0306'), ('rm', 'respiratory-support', ['REF-0870']),
        ('note', 'respiratory-support', 'Traditional expectorant for cough associated with a cold (EU herbal monograph)')],
    'prunella_vulgaris': [('purge', 'REF-0314'), ('purge', 'REF-2882')]
      + [('rm', c, ['REF-0098']) for c in PRUN_GRIEVE_RM]
      + [('rm', c, ['REF-0200']) for c in PRUN_PSOTOVA_RM]
      + [('rmk', 'inflammation', ['REF-0200']),
         ('rm', 'bruising', ['REF-0659']), ('rm', 'skin-irritation', ['REF-0659']), ('rm', 'wounds', ['REF-0659']),
         ('add', 'cardiovascular-support', ['REF-0659']),
         ('rm', 'immune-support', ['REF-0658', 'REF-0660', 'REF-2887']),
         ('mexcl', 'cold', ['REF-2422']),   # off-target: self-heal antiviral work is herpes/HIV lab research (inv. 11)
         ('note', 'arthritis', 'Traditionally used as an anti-rheumatic (review of traditional uses)'),
         ('note', 'bruising', 'Traditional remedy for bruises and wounds (Grieve, A Modern Herbal)'),
         ('note', 'wounds', 'Traditional wound herb (Grieve); an extract sped wound healing in animal tests (preclinical)'),
         ('note', 'infection', 'Extracts showed antibacterial activity in lab studies (preclinical; review)'),
         ('note', 'inflammation', 'Extracts reduced inflammation in animal models of colitis, thyroiditis and uveitis (preclinical)'),
         ('note', 'immune-support', 'A self-heal polysaccharide strengthened the innate antiviral (interferon) response to herpes virus in lab and mouse studies (preclinical)'),
         ('note', 'cancer', 'Extracts and compounds slowed several cancer types in cell and animal studies (preclinical)')],
    'prunus_africana': [('null', 'prostate-support', ['REF-1508']), ('null', 'urinary-support', ['REF-1508']),
                        ('mexcl', 'inflammation', ['REF-1508'])],
}

NOTES = {
    'pimpinella_anisum': 'REF-1408 (wound healing in diabetic rats) names no skin irritation - removed; skin-irritation pair dropped. Claim notes on wounds/infection/cancer rewritten to describe their direct sources (they said "inferred"). Gap for owner: the EU anise monograph uses (bloating, flatulence, cough with cold) have no pairs.',
    'pinus_sylvestris': 'REF-0018 (general essential-oil review, no pine species) purged. REF-1242 (five Pinus oils: P. sylvestris oil "did not show any significant wound healing and anti-inflammatory activities") purged from actions and recorded as null for wounds and inflammation. Grieve REF-0098 (pine entry: rheumatic affections, respiratory complaints, antiseptic, tar in eczema, bladder/kidney) removed from bronchitis, cough, uti, swelling (rheumatic swelling is not fluid retention), inflammation, wounds - bronchitis, cough, uti and swelling dropped. REF-1234 (inhaled oil aggravated inflammatory markers) hidden from inflammation; REF-0633 (in vitro NO/iNOS, P. sylvestris) added. Wounds: remaining mechanistic cards were oil tests against N. gonorrhoeae and Cryptococcus (off-target, inv. 11) - pair dropped.',
    'piper_methysticum': 'Pittler & Ernst 2000 MA REF-2544 merged into their Cochrane review REF-2462 (superseded, inv. 11). REF-2463 was the KADSS protocol paper; repointed to the KADSS results paper (Psychopharmacology 2009, PubMed 19430766). Landmark GAD trials added: Sarris 2013 REF-3398 (positive, anxiety) and Sarris 2020 REF-3397 (16 weeks, 171 patients: no benefit vs placebo; more liver-test abnormalities on kava) recorded as null for anxiety. Anxiety RCTs/SRs removed from stress and nervous-tension (they measured anxiety). REF-2460 (herbal sedatives in cancer care: kava raised "disturbing toxicity concerns") removed from insomnia - pair dropped.',
    'plantago_lanceolata': 'REF-0968 (aucubin review naming P. asiatica) and REF-0967 (Balkan wound-plant review, ribwort not named) purged. EU monograph REF-0499 (demulcent for oral/pharyngeal irritation and dry cough) kept for cough and sore-throat only. ESCOP REF-0500 (catarrh of the respiratory tract, mild oral/pharyngeal inflammation, insect bites, wounds) kept for bronchitis and wounds, added to sore-throat and inflammation, removed from bruising, cold, cough, immune-support, infection, skin-irritation. REF-0633 (in vitro NO assay; retagged preclinical) kept for inflammation only. Herbal Reality plantain page REF-0358 (names ribwort for coughs and sore throats; both plantains for mild bronchitis, wounds, inflamed rashes) added. Arthritis, cold and immune-support dropped.',
    'plantago_major': 'REF-0309 ("WHO Monographs" 2002, vol. 2) purged: vol. 2 has no Plantago major monograph (table of contents runs Rhizoma Piperis methystici p.231 -> Cortex Pruni africanae p.246). REF-1762 (RCT: plantain rinse no better than bicarbonate for chemotherapy oral mucositis) purged from the demulcent action and recorded as null for inflammation. Herbal Reality REF-0358 names no constipation and gives sore throat to ribwort - removed there; sore-throat dropped. Samuelsen review REF-0364 (skin, respiratory, wounds, anti-inflammatory) removed from arthritis, bronchitis, bruising. Held sources that name the symptom added: Najafian review REF-1758 (constipation, coughs, anti-inflammatory), Adom review REF-0354 (antidiarrhoeal, anti-inflammatory), Grieve REF-0098 Common Plantain (inflammation of the skin; diarrhoea). Note: REF-3010 carries its journal\'s published abstract, which reads like a copy of earlier reviews, not the in-vitro study its title describes (left as mechanistic card).',
    'pleurotus_ostreatus': 'REF-0102 (edible mushrooms and CVD review; names no species) purged - it was the only source for blood-sugar, metabolic-support and cardiovascular-support. Landmark evidence added: Dicks & Ellinger 2020 SR REF-3399 (8 trials of P. ostreatus intake: lower glucose and lipids; low-quality evidence) for those three pairs; pleuran RCTs Bergendiova 2011 REF-3400 (athletes, fewer URTI symptoms, more NK cells) and Jesenak 2013 REF-3401 (children with recurrent RTIs; placebo arm got the same vitamin C) for cold and immune-support (pleuran = signature compound, labelled). REF-2596 (immune profile in breast-cancer survivors; no tumour outcome) removed from cancer.',
    'potentilla_erecta': 'Commentary REF-2592 replaced by the trial it discussed, Huber 2007 REF-3402 (open-label, 16 UC patients; disease activity fell on 2400 mg/day; tannins not detected in serum). ESCOP REF-0521 (acute diarrhoea, adjuvant in enteritis/colitis, slight irritations of mouth and throat mucosa) removed from skin-irritation and wounds. REF-0970 (campylobacteriosis mice: only the four-ingredient combination eased diarrhoea) removed from diarrhea. Dental-biofilm studies REF-0976 and REF-2594 removed from sore-throat. Arthritis was inferred from anti-inflammatory action, but tormentil tannins are not absorbed (REF-3402) - contradicted (inv. 11), pair dropped. EMA REF-0520 kept on its known indications (mild diarrhoea, minor oral-mucosa inflammation) - EMA 429, flagged.',
    'primula_veris': 'REF-0306 ("Wicke 2007", pages 109-116, no journal or DOI) not found in PubMed, OpenAlex or Crossref - purged as unverifiable. REF-0870 (SR of an ivy/primrose/thyme combination product; "studies on primrose were lacking") removed. Respiratory-support rests on the EU monograph REF-0075 (expectorant in cough associated with cold; EMA 429, flagged). Gap for owner: no cough pair and no expectorant action, though EMA and ESCOP (2021) both name cough with colds.',
    'prunella_vulgaris': 'REF-0314 ("Yang 2007", vol. 73(3) 157-162, no journal or DOI) not found in PubMed, OpenAlex or Crossref - purged as unverifiable. REF-2882 (PV-1, a multi-herb mixture) purged. Grieve REF-0098 Self-Heal (wounds, bruises, sore throat, ulcerated mouth, internal bleeding) kept for bruising and wounds only. Psotova REF-0200 (in vitro antioxidant, LTB4 inhibition, moderate antibacterial) kept for infection, kept as mechanistic card for inflammation. Mir review REF-0659 (anti-rheumatic, antimicrobial, anti-inflammatory, cardioprotective) kept for arthritis, infection, inflammation, added to cardiovascular-support. Immune-support: colitis, thyroiditis (Th1/Th17 suppression) and TLR-blocking studies are immune-suppressive, not support - removed; REF-0663 (innate antiviral response) remains. Cold: only a review\'s general antiviral mention remained; self-heal antiviral work is herpes/HIV lab research (off-target, inv. 11) - pair dropped.',
    'prunus_africana': 'Keehn & Lowe 2015 REF-1508 ("no evidence that phytotherapy significantly improves symptoms of BPH against placebo"; names Pygeum africanum) was cited as SUPPORT - moved to null_result_ids for prostate-support and urinary-support, hidden from inflammation; retagged narrative-review. Cochrane 2002 (REF-0547) remains the current version.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 13', os.path.join(HERE, 'batch13_changes.tsv'), **BIB)
