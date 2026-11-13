"""Deep audit of batch 14 (prunus-serotina .. rubus-fruticosus). Run from the repo root.
Batches 14-19 never had the 2nd-pass audit, so this pass does both: the strict "does each direct card
name the symptom" check (dossier !NAME screen) plus the batch-13 deep checks.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3725..REF-3734 (Grieve x2 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3727', '17990195', 'rhodiolashr5depression', 'rct'),
    ('REF-3728', '25837277', 'rhodiolasertraline', 'rct'),
    ('REF-3729', '12725561', 'rhodiolashr5fatigue', 'rct'),
    ('REF-3730', '25268730', 'rhodiolanursing', 'rct'),
    ('REF-3731', '24055627', 'rhodiolamarathon', 'rct'),
    ('REF-3732', '42879451', 'rhodiolapms', 'rct'),
    ('REF-3733', '40873122', 'rhodioladigitaleye', 'rct'),
    ('REF-3734', '19818588', 'rosehiprheumatoid', 'rct'),
])
NEW['grieve1931wildcherry'] = ('REF-3725', [
    ('author', 'Grieve, M'), ('title', 'Cherry, Wild (Prunus serotina) - A Modern Herbal'), ('year', '1931'),
    ('url', 'https://www.botanical.com/botanical/mgmh/c/chewil56.html'), ('note', 'REF-3725'), ('study_type', 'traditional'),
    ('summary', 'Grieve, A Modern Herbal (1931), Wild Cherry (Prunus serotina) entry. Medicinal action: astringent tonic, pectoral, sedative; used for bronchitis, catarrh, nervous and whooping cough, and dyspepsia. Read 2026-11-13.')])
NEW['grieve1931blackberry'] = ('REF-3726', [
    ('author', 'Grieve, M'), ('title', 'Blackberry (Rubus fruticosus) - A Modern Herbal'), ('year', '1931'),
    ('url', 'https://www.botanical.com/botanical/mgmh/b/blaber49.html'), ('note', 'REF-3726'), ('study_type', 'traditional'),
    ('summary', 'Grieve, A Modern Herbal (1931), Blackberry (Rubus fruticosus) entry. Medicinal action: astringent and tonic, a remedy for dysentery and diarrhoea; historically for soreness of the mouth and throat, and the leaves for burns and scalds. Read 2026-11-13.')])

BIB = dict(
    retag={'REF-0999': 'narrative-review', 'REF-0479': 'preclinical',
           'REF-0979': 'narrative-review', 'REF-0981': 'narrative-review', 'REF-0983': 'narrative-review', 'REF-0984': 'narrative-review',
           'REF-1528': 'narrative-review', 'REF-1530': 'clinical', 'REF-0053': 'narrative-review',
           'REF-0097': 'narrative-review', 'REF-0302': 'rct',
           'REF-1005': 'narrative-review', 'REF-1006': 'narrative-review', 'REF-1013': 'narrative-review',
           'REF-2549': 'narrative-review'},
    sets={'REF-0053': {'pmid': '23352748', 'journal': 'Fitoterapia'}},
    delete=['REF-0311',    # "WHO Monographs on Selected Medicinal Plants" 2007, no volume/page: no knotweed monograph could be located
            'REF-0985',    # Citri Reticulatae Pericarpium + Reynoutria herb pair (two-herb mixture)
            'REF-0418'],   # honey enriched with Rubus spp. (mixture)
    new=NEW)

RHO_NONAME = ('arthritis', 'blood-sugar', 'cognitive-function', 'cold', 'immune-support', 'inflammation', 'memory', 'metabolic-support', 'muscle-soreness', 'skin-irritation')

PLAN = {
    'prunus_serotina': [
        ('drop', 'menstrual-cramps'), ('drop', 'muscle-spasm'),   # neither web source names cramps; airway antispasmodic is off-target
        ('drop', 'sore-throat'),                                  # neither web source nor Grieve names sore throat
        ('add', 'cough', ['REF-3725']), ('add', 'bronchitis', ['REF-3725']), ('aadd', 'antitussive', ['REF-3725']),
        ('note', 'cough', 'Traditional remedy for irritating dry cough and the persistent cough of chronic bronchitis (Herbal Reality; Grieve, A Modern Herbal; herbalist text)'),
        ('note', 'bronchitis', 'Traditionally used for bronchitis and its persistent cough (Herbal Reality; Grieve, A Modern Herbal; herbalist text)'),
        ('note', 'cancer', 'Wild cherry bark extract slowed colorectal cancer cells in the lab (preclinical)'),
    ],
    'psilocybe_cubensis': [
        ('note', 'depression', 'Psilocybin, the mushroom\'s active compound, given with psychological support reduced depression in randomized trials and meta-analyses (compound evidence; purified psilocybin in supervised settings, not the raw mushroom)'),
        ('note', 'anxiety', 'Psilocybin reduced anxiety in people with life-threatening cancer in a randomized trial (compound evidence); mushroom extracts reduced anxiety-like behaviour in rodents (preclinical)'),
    ],
    'pulmonaria_officinalis': [
        ('arm', 'demulcent', ['REF-0479']), ('arm', 'expectorant', ['REF-0479']),   # an in vitro COX-2 / oxidative-stress study
        ('rmk', 'arthritis', ['REF-0479']), ('rmk', 'inflammation', ['REF-0629']),
        ('rm', 'skin-irritation', ['REF-0479']),
        ('note', 'arthritis', 'inferred from anti-inflammatory action'),
        ('note', 'inflammation', 'Lungwort extract inhibited the inflammatory enzyme COX-2 and oxidative stress in the lab (preclinical)'),
        ('note', 'respiratory-support', 'Lungwort extract was active against Staphylococcus aureus from cystic fibrosis patients in lab tests (preclinical)'),
    ],
    'reynoutria_japonica': [
        ('purge', 'REF-0311'), ('purge', 'REF-0985'),
        ('arm', 'anti-inflammatory', ['REF-0980']), ('refadd', ['REF-0980']),   # SR of knotweed only as part of herbal mixtures for RTIs
        ('note', 'arthritis', 'Knotweed compounds were predicted to act on osteoarthritis targets in a computer study, and anti-inflammatory activity is reviewed (preclinical; reviews)'),
        ('note', 'cardiovascular-support', 'Traditionally used in Chinese medicine for high blood lipids (review)'),
        ('note', 'cancer', 'Knotweed compounds such as emodin and resveratrol slowed cancer cells in lab studies (reviews)'),
        ('note', 'inflammation', 'Anti-inflammatory activity of knotweed and its compounds is reviewed (reviews; preclinical)'),
    ],
    'rhodiola_rosea': [('rm', c, ['REF-0132']) for c in RHO_NONAME]
                      + [('rm', c, ['REF-1528']) for c in ('arthritis', 'cold', 'immune-support', 'inflammation', 'muscle-soreness', 'skin-irritation')]
                      + [('arm', a, ['REF-0055']) for a in ('anti-inflammatory', 'antidiabetic', 'antioxidant', 'immunomodulator')] + [
        ('null', 'fatigue', ['REF-1533']),   # SR: "efficacy is contradictory"
        ('add', 'fatigue', ['REF-3729']), ('nulladd', 'fatigue', ['REF-3730']),
        ('note', 'fatigue', 'Rhodiola (SHR-5 extract) reduced stress-related and burnout fatigue vs placebo in randomized trials; another trial found it worsened fatigue in shift-working students, and a systematic review called the evidence contradictory'),
        ('nulladd', 'muscle-soreness', ['REF-3731']),
        ('note', 'muscle-soreness', 'Exercise effects are reviewed with mixed findings (review); before a marathon it did not reduce muscle damage or soreness in a randomized trial'),
        ('note', 'cognitive-function', 'Rhodiola improved mental performance under stress and fatigue in randomized trials (review)'),
        ('note', 'memory', 'Rhodiola improved mental performance under stress and fatigue in randomized trials (review)'),
        ('note', 'inflammation', 'Anti-inflammatory effects of Rhodiola are reviewed and seen in lab studies (review; preclinical)'),
        ('note', 'blood-sugar', 'Antidiabetic effects are reviewed (review)'),
        ('note', 'metabolic-support', 'Metabolic effects are reviewed (review)'),
        ('newpair', 'depression', ['REF-3727'], 'Rhodiola extract SHR-5 reduced mild to moderate depression vs placebo in a randomized trial; in another, neither Rhodiola nor sertraline differed significantly from placebo'),
        ('nulladd', 'depression', ['REF-3728']),
        ('newpair', 'pms', ['REF-3732'], 'Short-term Rhodiola improved some premenstrual symptoms in female athletes in a small randomized trial'),
        ('newpair', 'eye-strain', ['REF-3733'], 'Rhodiola reduced one digital eye strain symptom and focusing variability vs placebo in a randomized trial'),
    ],
    'rhododendron_tomentosum': [
        ('purge', 'REF-0098'),   # Grieve's Labrador Tea entry is Ledum latifolium; for L. palustre it gives no medicinal use
        ('arm', 'diuretic', ['REF-0053']),
        ('rm', 'swelling', ['REF-0053']), ('rm', 'urinary-support', ['REF-0053']), ('rm', 'uti', ['REF-0053']),
        ('note', 'arthritis', 'Traditionally used for rheumatism (review of traditional use); its essential oil affected inflammatory cells from rheumatoid arthritis joints in the lab (preclinical)'),
        ('note', 'inflammation', 'Anti-inflammatory activity of its essential oil reported in lab and animal studies (review)'),
        ('note', 'respiratory-support', 'Traditionally used for cough and colds (review of traditional use)'),
        ('note', 'skin-irritation', 'Traditionally used for insect bites (review of traditional use)'),
        ('note', 'swelling', 'Its essential oil reduced inflammatory swelling in animals about as well as standard anti-inflammatory drugs (preclinical)'),
    ],
    'ribes_nigrum': [('rm', c, ['REF-0097']) for c in ('arthritis', 'cold', 'immune-support', 'skin-irritation', 'swelling', 'urinary-support', 'uti')]
                    + [('arm', a, ['REF-0302']) for a in ('anti-inflammatory', 'antioxidant', 'antiviral', 'diuretic', 'immunomodulator')] + [
        ('arm', 'diuretic', ['REF-0097']), ('refadd', ['REF-0302']),
        ('newpair', 'blood-sugar', ['REF-1247'], 'Blackcurrant lowered the blood sugar and insulin rise after a sugar drink in a randomized crossover trial'),
        ('note', 'cardiovascular-support', 'Blackcurrant extract lowered cholesterol in a small pilot study in women and protected blood vessels in animal studies; cardiovascular uses reviewed (review)'),
        ('note', 'eye-strain', 'Blackcurrant\'s use for eye conditions is reviewed (review)'),
        ('note', 'inflammation', 'Blackcurrant extract reduced inflammation in mice and immune cells (preclinical; review)'),
        ('note', 'infection', 'Antimicrobial effects of blackcurrant compounds are reviewed (review)'),
    ],
    'rosa_canina': [
        ('add', 'arthritis', ['REF-3734']),
        ('note', 'arthritis', 'Standardised rose hip powder reduced osteoarthritis pain and painkiller use in placebo-controlled trials and a meta-analysis, and helped rheumatoid arthritis as an add-on in a randomized trial'),
        ('note', 'inflammation', 'Rose hip reduced osteoarthritis symptoms in trials, and its compounds are anti-inflammatory in the lab (systematic reviews; preclinical)'),
        ('note', 'metabolic-support', 'Rose hip flesh and extracts reduced fat build-up and improved blood sugar in animal studies (preclinical); seed lipid-lowering effects reviewed (systematic review)'),
        ('note', 'skin-irritation', 'inferred from anti-inflammatory action'),
        ('note', 'cancer', 'Rose hip polyphenols slowed human cancer cells in the lab (preclinical)'),
    ],
    'rosa_rugosa': [
        ('purge', 'REF-0098'),   # Grieve mentions R. rugosa only as a parent of garden hybrids - no medicinal use
        ('note', 'cardiovascular-support', 'Rugosa rose flavonoids lowered triglycerides in mice (preclinical)'),
        ('note', 'skin-irritation', 'A rugosa rose polysaccharide eased psoriasis-like skin disease in mice (preclinical)'),
        ('note', 'cancer', 'Rugosa rose polysaccharides slowed colorectal and cervical cancer in lab and animal studies (preclinical)'),
    ],
    'rubus_fruticosus': [('rm', c, ['REF-2549']) for c in ('arthritis', 'inflammation', 'oral-health', 'skin-irritation', 'sore-throat')] + [
        ('purge', 'REF-0418'),
        ('add', 'diarrhea', ['REF-3726']), ('add', 'sore-throat', ['REF-3726']), ('add', 'oral-health', ['REF-3726']), ('add', 'wounds', ['REF-3726']),
        ('aadd', 'astringent', ['REF-3726']), ('aadd', 'antidiarrheal', ['REF-3726']),
        ('note', 'diarrhea', 'Traditional astringent remedy for diarrhoea and dysentery (Grieve, A Modern Herbal; review)'),
        ('note', 'sore-throat', 'Historically used for soreness of the mouth and throat (Grieve, A Modern Herbal)'),
        ('note', 'oral-health', 'Historically used for soreness of the mouth and throat (Grieve, A Modern Herbal)'),
        ('note', 'wounds', 'Leaves were traditionally applied to burns and scalds (Grieve, A Modern Herbal); blackberry polyphenols aided wound healing in lab studies (preclinical)'),
        ('note', 'inflammation', 'Blackberry fruit and leaf extracts reduced inflammatory signals in lab and animal studies (preclinical)'),
        ('note', 'infection', 'Blackberry is used as an antimicrobial in traditional medicine (review); fruit extracts were antimicrobial in the lab (preclinical)'),
        ('note', 'cancer', 'Blackberry fruit extract slowed cancer cells in the lab (preclinical)'),
    ],
}

NOTES = {
    'prunus_serotina': 'Deep audit (2nd pass + deep). Web sources checked 2026-11-13: Herbal Reality (references listed) names irritating cough, chronic bronchitis, nervous indigestion and appetite loss; The Herbal Medic (book bibliography) names coughs, bronchitis, asthma, nervous dyspepsia and smooth-muscle antispasmodic. Neither names sore throat or cramps -> sore-throat, menstrual-cramps and muscle-spasm dropped. Grieve REF-3725 (astringent tonic, pectoral, sedative; bronchitis, nervous and whooping cough, dyspepsia) added. REF-0999 retagged narrative-review. Gap: indigestion/appetite (traditional only, no pair).',
    'psilocybe_cubensis': 'Deep audit. Depression/anxiety evidence is purified psilocybin (the signature compound) - notes now label it as compound evidence (inv. 10).',
    'pulmonaria_officinalis': 'Deep audit. REF-0479 is an in vitro COX-2/peroxynitrite study (retagged preclinical, was traditional) - removed from the demulcent and expectorant actions and from skin-irritation (dropped: no source names skin). Grieve\'s "Lungwort" entry is the lichen Sticta pulmonaria, not this plant - not used. Gap: the traditional respiratory use has no checkable source here.',
    'reynoutria_japonica': 'Deep audit. REF-0311 ("WHO Monographs on Selected Medicinal Plants", 2007, no volume or page) - no WHO knotweed monograph could be located and WHO pages refuse automated access; purged and deleted as unverifiable. Herb-pair study REF-0985 purged and deleted (mixture). Mixture-only RTI SR REF-0980 removed from the anti-inflammatory action (kept in references). Four reviews retagged narrative-review.',
    'rhodiola_rosea': 'Deep audit (2nd pass + deep). Kelly 2001 review REF-0132 and Panossian 2010 review REF-1528 (retagged narrative-review) were cited on up to 11 pairs whose symptoms they never name - removed from those (kept for fatigue/cognition). Darbinyan 2000 RCT REF-0055 removed from four non-matching actions. Blood-sugar, metabolic-support, cold and immune-support dropped when no named evidence remained. Fatigue: SR REF-1533 ("contradictory") and nursing RCT REF-3730 (worsened fatigue) recorded as no-effect; SHR-5 RCT REF-3729 added. Marathon RCT REF-3731 no-effect for muscle soreness. New pairs (owner rule): depression (RCT REF-3727; sertraline RCT REF-3728 no-effect vs placebo), pms (RCT REF-3732), eye-strain (RCT REF-3733). REF-1530 retagged clinical (no placebo).',
    'rhododendron_tomentosum': 'Deep audit. Grieve REF-0098 purged: its Labrador Tea entry is Ledum latifolium and gives L. palustre no medicinal use (narcotic; used to strengthen beer). Dampc 2013 review REF-0053 (PMID 23352748, retagged narrative-review) names rheumatism, cough, cold and insect bites - removed from swelling, urinary-support and uti and from the diuretic action; urinary-support and uti dropped (no source names them).',
    'ribes_nigrum': 'Deep audit (2nd pass + deep). Gopalan 2012 review REF-0097 (tagged rct; retagged narrative-review) was on 11 pairs - removed from the seven whose symptoms it never names and from the diuretic action; swelling, urinary-support and uti dropped. REF-0302 (acute cognition RCT, retagged rct) removed from five actions. New pair (owner rule): blood-sugar (held RCT REF-1247). Gap: the EMA blackcurrant-leaf monograph (minor joint pain, urinary flushing) could not be fetched (EMA 429) - not used.',
    'rosa_canina': 'Deep audit. RA add-on RCT REF-3734 added to arthritis. Notes rewritten.',
    'rosa_rugosa': 'Deep audit. Grieve REF-0098 purged: Grieve mentions R. rugosa only as a parent of garden hybrids. Three reviews retagged narrative-review. Notes rewritten to the preclinical sources.',
    'rubus_fruticosus': 'Deep audit (2nd pass + deep). Verma 2014 review REF-2549 (retagged narrative-review) names antidiarrhoeal, antidysentery, antimicrobial uses only - removed from arthritis, inflammation, oral-health, skin-irritation and sore-throat. Honey-with-Rubus study REF-0418 purged and deleted (mixture). Grieve REF-3726 (diarrhoea, dysentery, astringent; mouth and throat soreness; leaves for burns) added.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 14', os.path.join(HERE, 'deep', 'd14_changes.tsv'), **BIB)
