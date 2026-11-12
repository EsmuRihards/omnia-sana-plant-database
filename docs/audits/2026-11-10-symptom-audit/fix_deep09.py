"""Deep re-sweep of batch 9 (humulus-lupulus .. lamium-album) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3594..REF-3608 (PubMed efetch, deep/abstracts.json;
REF-3608 = Grieve's Hyssop entry, read 2026-11-12 by the web-fetch agent)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3594', '25982391', 'hopmenopause', 'rct'),
    ('REF-3595', '16321485', 'hopextractmenopause', 'rct'),
    ('REF-3596', '11939866', 'hdtsg2002', 'rct'),
    ('REF-3597', '11308434', 'sheltonsjw2001', 'rct'),
    ('REF-3598', '31331546', 'hypericummenopause', 'rct'),
    ('REF-3599', '19194342', 'hypericumhotflashes', 'rct'),
    ('REF-3600', '20155996', 'hypericumpms', 'rct'),
    ('REF-3601', '20064022', 'hypericumcesarean', 'rct'),
    ('REF-3602', '40717256', 'hypericumpressure', 'rct'),
    ('REF-3603', '12807340', 'hypericumatopic', 'rct'),
    ('REF-3604', '22571563', 'hypericumpsoriasis', 'rct'),
    ('REF-3605', '38242739', 'hypericumkneeoa', 'rct'),
    ('REF-3606', '41240546', 'rolecajuniper', 'rct'),
    ('REF-3607', '39842749', 'abhaljuniper', 'rct'),
])
NEW['grieve1931hyssop'] = ('REF-3608', [
    ('author', 'Grieve, M'),
    ('title', 'Hyssop (Hyssopus officinalis) - A Modern Herbal'),
    ('year', '1931'),
    ('url', 'https://www.botanical.com/botanical/mgmh/h/hyssop48.html'),
    ('note', 'REF-3608'),
    ('study_type', 'traditional'),
    ('summary', 'Grieve, A Modern Herbal (1931), Hyssop entry. Medicinal action: expectorant, diaphoretic, stimulant, pectoral, carminative; said to promote expectoration and used for chronic catarrh and pulmonary complaints, sometimes for asthma; externally for bruises and rheumatism. Read 2026-11-12.'),
])

BIB = dict(
    retag={'REF-1729': 'rct',                 # hop cream: randomized placebo-controlled UVB-erythema trial in 40 volunteers
           'REF-0843': 'narrative-review',    # SJW neurotransmitter review tagged traditional
           'REF-0849': 'narrative-review'},   # chaga polysaccharide review tagged traditional
    delete=['REF-2814'],                      # Scabiosa species (Turkey) - not Knautia arvensis
    new=NEW)

PLAN = {
    'humulus_lupulus': [
        ('add', 'skin-irritation', ['REF-1729']), ('add', 'inflammation', ['REF-1729']),
        ('newpair', 'anxiety', ['REF-1732'], 'A hop dry extract lowered anxiety scores vs placebo in a randomized crossover trial in young adults with mild symptoms'),
        ('newpair', 'depression', ['REF-1732'], 'A hop dry extract lowered depression scores vs placebo in a randomized crossover trial in young adults with mild symptoms'),
        ('newpair', 'stress', ['REF-1732', 'REF-3077'], 'A hop dry extract lowered stress scores vs placebo in a randomized crossover trial; traditional use for mild symptoms of mental stress (EU herbal monograph)'),
        ('newpair', 'menopause', ['REF-3594', 'REF-3595'], 'Hop extracts reduced menopausal symptoms vs placebo in two randomized trials'),
        ('newpair', 'hot-flashes', ['REF-3594', 'REF-3595'], 'Hop extracts reduced hot flashes vs placebo in two randomized trials'),
        ('note', 'insomnia', 'Traditional use to aid sleep (EU herbal monograph)'),
        ('note', 'skin-irritation', 'A 1% hop extract cream reduced UV-induced skin redness as much as 1% hydrocortisone in a randomized placebo-controlled trial (in one cream base only)'),
        ('note', 'inflammation', 'A 1% hop extract cream reduced UV-induced skin inflammation as much as 1% hydrocortisone in a randomized placebo-controlled trial; extracts reduced inflammatory markers in immune cells (preclinical)'),
    ],
    'hydrastis_canadensis': [
        ('note', 'infection', 'Traditionally used for skin and eye infections (review); leaf extracts were active against MRSA in the lab (preclinical)'),
        ('note', 'inflammation', 'Traditional remedy whose anti-inflammatory activity is reviewed (review)'),
        ('note', 'skin-irritation', 'Traditionally used for skin ailments (review)'),
        ('note', 'wounds', 'Traditionally used for wounds (review); extracts were antibacterial in the lab (preclinical)'),
    ],
    'hypericum_perforatum': [('arm', a, ['REF-0154']) for a in ('anti-inflammatory', 'antioxidant', 'antiviral', 'emollient', 'vulnerary')] + [
        ('drop', 'insomnia'),   # inferred from 'sedative' refs that are all antidepressant literature (off-target, inv. 11)
        ('nulladd', 'depression', ['REF-3596', 'REF-3597']),
        ('note', 'depression', 'Hypericum extracts beat placebo in major depression and matched standard antidepressants with fewer side effects (Cochrane review; meta-analysis in mild-to-moderate depression); two large US trials in moderately severe major depression found no benefit over placebo'),
        ('add', 'wounds', ['REF-3409', 'REF-3601']), ('nulladd', 'wounds', ['REF-3602']),
        ('note', 'wounds', 'St John\'s wort ointments aided healing of episiotomy and caesarean wounds in randomized trials; the oil did no better than saline for early pressure injuries'),
        ('newpair', 'menopause', ['REF-1795', 'REF-3598', 'REF-3599'], 'St John\'s wort improved menopausal symptoms vs placebo in a meta-analysis and randomized trials'),
        ('newpair', 'hot-flashes', ['REF-3598'], 'St John\'s wort reduced hot flashes in a randomized trial; a pilot trial found no significant effect on hot flash frequency'),
        ('nulladd', 'hot-flashes', ['REF-3599']),
        ('newpair', 'pms', ['REF-3600'], 'St John\'s wort eased the common physical and behavioural premenstrual symptoms vs placebo in a randomized trial; mood and pain symptoms did not clearly improve'),
        ('newpair', 'eczema', ['REF-3603'], 'A St John\'s wort cream outperformed its base cream in mild to moderate atopic eczema in a randomized half-side trial'),
        ('newpair', 'psoriasis', ['REF-3604'], 'A St John\'s wort ointment lowered psoriasis severity scores vs its base in a small single-blind half-side randomized trial'),
        ('newpair', 'arthritis', ['REF-3605'], 'St John\'s wort oil eased knee osteoarthritis pain vs control in a randomized trial'),
    ],
    'hyssopus_officinalis': [
        ('aadd', 'expectorant', ['REF-3608']),
        ('arm', 'expectorant', ['REF-1803', 'REF-1804']),   # TLR/interferon cell study; asthmatic-mouse airway inflammation - neither tests expectoration
        ('refadd', ['REF-1803']),
        ('add', 'respiratory-support', ['REF-3608']),
        ('note', 'respiratory-support', 'Traditional expectorant for chronic catarrh and lung complaints (Grieve, A Modern Herbal); extract reduced airway inflammation in asthmatic mice (preclinical)'),
        ('note', 'inflammation', 'Hyssop extract reduced airway inflammation in asthmatic mice (preclinical)'),
        ('note', 'cancer', 'Hyssop extract reduced brain tumour (glioblastoma) growth in rats (preclinical)'),
    ],
    'inonotus_obliquus': [
        ('note', 'cancer', 'Chaga extracts and polysaccharides slowed tumours in lab and animal studies (preclinical)'),
        ('note', 'immune-support', 'Chaga polysaccharides activated immune cells in lab studies (preclinical)'),
        ('note', 'metabolic-support', 'Chaga polysaccharides and extracts lowered blood sugar and improved insulin sensitivity in diabetic mice (preclinical)'),
        ('note', 'cardiovascular-support', 'A chaga polysaccharide lowered blood lipids in mice and cells (preclinical)'),
    ],
    'inula_helenium': [
        ('add', 'respiratory-support', ['REF-0445']),
        ('note', 'respiratory-support', 'Traditionally used for respiratory ailments in Irish folk medicine (as stated in a lab study); its root compounds were antibacterial in the lab (preclinical)'),
        ('note', 'arthritis', 'Elecampane sesquiterpene lactones eased arthritis in animal models (preclinical)'),
        ('note', 'inflammation', 'Elecampane sesquiterpene lactones reduced inflammation in arthritis models and human immune cells (preclinical)'),
        ('note', 'cancer', 'Elecampane sesquiterpene lactones slowed breast and pancreatic cancer cells in the lab (preclinical)'),
        ('note', 'infection', 'Elecampane root oil and its compounds were active against staphylococci and tuberculosis bacteria in the lab (preclinical)'),
    ],
    'juniperus_communis': [
        ('add', 'indigestion', ['REF-3606']),
        ('newpair', 'menstrual-cramps', ['REF-3607'], 'Juniper reduced menstrual cramp pain in primary dysmenorrhoea in a randomized trial'),
        ('note', 'indigestion', 'A juniper preparation relieved functional dyspepsia vs placebo in a randomized trial; traditional use for digestive complaints (EU herbal monograph)'),
        ('note', 'bloating', 'Traditional use for digestive complaints such as bloating and flatulence (EU herbal monograph)'),
        ('note', 'urinary-support', 'Traditional use to increase urine flow and flush the urinary tract in minor urinary complaints (EU herbal monograph)'),
        ('note', 'cancer', 'Juniper extracts slowed melanoma, liver and colorectal cancers in lab and animal studies (preclinical)'),
    ],
    'knautia_arvensis': [('purge', 'REF-2814')],
    'lactuca_virosa': [
        ('add', 'cough', ['REF-2059']),
        ('arm', 'sedative', ['REF-2061', 'REF-2062']), ('refadd', ['REF-2061', 'REF-2062']),   # abuse report; NPS analytical review
        ('note', 'cough', 'Traditionally used for persistent and whooping cough (Herbal Reality; RxList; 1815 medical report)'),
        ('note', 'anxiety', 'Traditionally used for anxiety (Herbal Reality)'),
        ('note', 'insomnia', 'Traditionally used for insomnia and restlessness (Herbal Reality; RxList); lactucin and lactucopicrin were sedative in mice (preclinical)'),
        ('note', 'nervous-tension', 'Traditionally used for restlessness and tension (Herbal Reality)'),
        ('note', 'pain', 'Historically used as a painkiller (Herbal Reality; RxList, which rates the evidence insufficient); lactucin and lactucopicrin relieved pain in mice (preclinical)'),
    ],
    'lamium_album': [
        ('arm', 'antioxidant', ['REF-0342']), ('refadd', ['REF-0342']),                  # phytochemistry paper, no activity tested
        ('arm', 'expectorant', ['REF-1753']), ('refadd', ['REF-1753']),                  # tracheal smooth-muscle relaxation, not expectoration
        ('aadd', 'expectorant', ['REF-1746']),                                              # states the traditional mucolytic use
        ('note', 'arthritis', 'Historically used for gout, sciatica and joint aches (Herbal Reality)'),
        ('note', 'bronchitis', 'Traditionally used for chronic bronchitis and pharyngitis (as stated in a lab study); extracts calmed human immune cells in the lab (preclinical)'),
        ('note', 'bruising', 'Historically used for bruises (Herbal Reality)'),
        ('note', 'diarrhea', 'Traditionally used for diarrhoea (Herbal Reality)'),
        ('note', 'inflammation', 'Traditional anti-inflammatory (Herbal Reality); extracts reduced inflammatory responses of human immune cells in the lab (preclinical)'),
        ('note', 'respiratory-support', 'Traditionally used for catarrh of the upper airways (Herbal Reality)'),
        ('note', 'skin-irritation', 'Traditionally used for skin inflammation (as stated in a lab study); extracts calmed human immune cells in the lab (preclinical)'),
    ],
}

NOTES = {
    'humulus_lupulus': 'Deep re-sweep. REF-1729 retagged rct (randomized placebo-controlled UVB-erythema trial, 40 volunteers) and wired to skin-irritation/inflammation. New pairs (owner rule): anxiety, depression, stress (RCT REF-1732; stress also EU monograph REF-3077), menopause and hot-flashes (RCTs REF-3594, REF-3595). Not used: Lactium/Zizyphus and sleep-supplement combinations, non-alcoholic beer study, xanthohumol Crohn trials (compound, safety endpoint).',
    'hydrastis_canadensis': 'Deep re-sweep. Notes rewritten to what the review REF-0455 names (traditional use for wounds, skin and eye infections, digestive disorders) and the lab studies. PubMed trials are pharmacokinetic only.',
    'hypericum_perforatum': 'Deep re-sweep. Cochrane depression review REF-0154 removed from five non-depression actions. Insomnia dropped: inferred from the sedative action, whose refs are antidepressant literature (off-target, inv. 11); the polysomnogram RCT 9784087 showed only longer REM latency. Landmark null RCTs HDTSG 2002 REF-3596 and Shelton 2001 REF-3597 recorded as no-effect for depression. Wounds: episiotomy RCT REF-3409 and caesarean RCT REF-3601 added, pressure-injury RCT REF-3602 no-effect. New pairs (owner rule): menopause (held MA REF-1795 + RCTs REF-3598, REF-3599), hot-flashes (REF-3598; pilot REF-3599 no-effect on frequency), pms (RCT REF-3600), eczema (REF-3603; 12634994 is the same trial in German), psoriasis (REF-3604), arthritis (knee OA RCT REF-3605). Homeopathic Hypericum trials (HYPOS 35171041, LBP 39951699) excluded.',
    'hyssopus_officinalis': 'Deep re-sweep. The expectorant action rested on a TLR/interferon cell study (REF-1803) and an asthmatic-mouse study (REF-1804), neither of which tests expectoration - both removed from it (REF-1803 kept in references). Grieve REF-3608 (Hyssop: expectorant, promotes expectoration, chronic catarrh, pulmonary complaints) added to expectorant and respiratory-support. Gaps (traditional only): Grieve also names asthma and bruises - no pairs. No trials on PubMed.',
    'inonotus_obliquus': 'Deep re-sweep. Notes rewritten to their lab sources. REF-0849 retagged narrative-review. No human trials on PubMed. REF-2981 DOI 10.5897/jmpr.9000346 does not resolve (left; preclinical action ref only).',
    'inula_helenium': 'Deep re-sweep. REF-0445 (states Irish ethnomedical use for respiratory ailments) wired to respiratory-support. Notes rewritten. Grieve elecampane page URL tried 2026-11-12 returned 404 - bronchitis/cough stay inferred from expectorant. Only PubMed trial is a multi-herb syrup (excluded).',
    'juniperus_communis': 'Deep re-sweep. Functional dyspepsia RCT REF-3606 (Roleca juniper, J. communis) added to indigestion. New pair (owner rule): menstrual-cramps (abhal = J. communis RCT REF-3607). Notes rewritten to the EU monograph REF-3066.',
    'knautia_arvensis': 'Deep re-sweep. REF-2814 studies Turkish Scabiosa species (S. columbaria, S. triniifolia), not Knautia arvensis - purged and deleted. No sourced activity remains.',
    'lactuca_virosa': 'Deep re-sweep. Web sources checked 2026-11-12: Herbal Reality names anxiety, restlessness/tension, insomnia, cough and historical painkiller use; RxList lists cough, insomnia, restlessness and muscle/joint pain (insufficient evidence; references are five reference books). 1815 whooping-cough report REF-2059 added to cough. Abuse report REF-2061 and NPS review REF-2062 removed from the sedative action (kept in references).',
    'lamium_album': 'Deep re-sweep. Herbal Reality page checked 2026-11-12: names respiratory catarrh, diarrhoea, inflammation, wounds, menorrhagia and historical use for bruises and joint aches. REF-0342 (phytochemistry, no activity) removed from antioxidant; REF-1753 (tracheal smooth-muscle relaxation) removed from expectorant; REF-1746 (states traditional mucolytic use for chronic bronchitis) added to expectorant. Gap: heavy menstrual bleeding (Herbal Reality) - traditional only, no pair.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 9', os.path.join(HERE, 'deep', 'd09_changes.tsv'), **BIB)
