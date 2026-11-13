"""Deep audit of batch 17 (tanacetum-parthenium .. trifolium-pratense): 2nd-pass strict-match + deep checks. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3791..REF-3816 (Grieve x6 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib
import yamlsplice as Y

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3791', '16232154', 'feverfewmig99', 'rct'),
    ('REF-3792', '2673080', 'feverfewra', 'rct'),
    ('REF-3793', '28439881', 'cocoabpcochrane', 'systematic-review'),
    ('REF-3794', '42679502', 'cocoaflavanolbp', 'meta-analysis'),
    ('REF-3795', '37211619', 'chocolatecognition', 'meta-analysis'),
    ('REF-3796', '42930530', 'wildthymegi', 'rct'),
    ('REF-3797', '38186189', 'thymeasthmacough', 'rct'),
    ('REF-3798', '24778782', 'thymedysmenorrhea', 'rct'),
    ('REF-3799', '38039009', 'thymestudents', 'rct'),
    ('REF-3800', '36760146', 'thymehalitosis', 'rct'),
    ('REF-3801', '40989143', 'ajwaindentalpain', 'rct'),
    ('REF-3802', '38633679', 'ajwaincipn', 'rct'),
    ('REF-3803', '17374344', 'ajwainasthma', 'clinical'),
    ('REF-3804', '22185453', 'yunzhisurvival', 'meta-analysis'),
    ('REF-3805', '12851275', 'redcloverice', 'rct'),
    ('REF-3806', '24323914', 'phytoestrogencochrane2013', 'systematic-review'),
    ('REF-3807', '42269521', 'redcloverhotflashgrade', 'meta-analysis'),
    ('REF-3808', '28160855', 'promensilma', 'meta-analysis'),
    ('REF-3809', '30269660', 'redcloverlipids', 'meta-analysis'),
    ('REF-3810', '15259285', 'redclovercognition', 'rct'),
])


def grieve(key, rid, name, url, summary):
    NEW[key] = (rid, [('author', 'Grieve, M'), ('title', f'{name} - A Modern Herbal'), ('year', '1931'), ('url', url),
                      ('note', rid), ('study_type', 'traditional'),
                      ('summary', f'Grieve, A Modern Herbal (1931). {summary} Read 2026-11-13.')])


grieve('grieve1931tansy', 'REF-3811', 'Tansy (Tanacetum vulgare)', 'https://www.botanical.com/botanical/mgmh/t/tansy-05.html',
       'Anthelmintic, tonic, stimulant and emmenagogue; for worms, hysteria, kidney weakness, low fevers and gout; stomachic and anti-flatulent in moderate doses; externally for eruptive skin diseases, sprains, swellings and rheumatic parts. Warns that large doses are a violent irritant.')
grieve('grieve1931dandelion', 'REF-3812', 'Dandelion (Taraxacum officinale)', 'https://www.botanical.com/botanical/mgmh/d/dandel08.html',
       'Diuretic, tonic and slightly aperient; chiefly for kidney and liver disorders: sluggish or congested liver, jaundice, gall stones, kidney gravel and stone, dropsy; a bitter tonic for atonic dyspepsia and appetite; mild laxative for constipation; for eczema and eruptions of the skin.')
grieve('grieve1931thyme', 'REF-3813', 'Thyme, Garden (Thymus vulgaris)', 'https://www.botanical.com/botanical/mgmh/t/thygar16.html',
       'Antiseptic, antispasmodic, tonic and carminative; for whooping and convulsive cough, catarrh, sore throat, wind and colic, and taken at the start of a cold; thymol for bronchial affections, laryngitis and septic sore throat, and in dressings for wounds.')
grieve('grieve1931wildthyme', 'REF-3814', 'Thyme, Wild (Thymus serpyllum)', 'https://www.botanical.com/botanical/mgmh/t/thywil17.html',
       'Aromatic, antiseptic, antispasmodic, diuretic and emmenagogue; for chest maladies, weak digestion and flatulence, whooping cough, catarrh and sore throat, and headache and nervous affections.')
grieve('grieve1931lime', 'REF-3815', 'Lime Tree (Tilia europaea, syn. T. cordata)', 'https://www.botanical.com/botanical/mgmh/l/limtre28.html',
       'Lime (linden) flower tea for indigestion, hysteria, nervous vomiting and palpitation, and for spasms; baths of the flowers for hysteria. Warns that tea made from old flowers may produce narcotic intoxication.')
grieve('grieve1931redclover', 'REF-3816', 'Clover, Red (Trifolium pratense)', 'https://www.botanical.com/botanical/mgmh/c/clovrd75.html',
       'The fluid extract is alterative and antispasmodic; an infusion is used for bronchial and whooping cough; fomentations were applied externally to cancerous growths.')

BIB = dict(
    retag={'REF-0552': 'preclinical', 'REF-1574': 'narrative-review', 'REF-0326': 'narrative-review', 'REF-0329': 'narrative-review',
           'REF-0338': 'narrative-review', 'REF-0333': 'narrative-review', 'REF-2962': 'narrative-review', 'REF-0321': 'clinical',
           'REF-0131': 'narrative-review', 'REF-1094': 'systematic-review', 'REF-1303': 'narrative-review',
           'REF-0017': 'narrative-review', 'REF-0031': 'narrative-review', 'REF-0275': 'preclinical',
           'REF-0052': 'narrative-review', 'REF-0282': 'narrative-review'},
    delete=['REF-1573',    # 2000 Cochrane feverfew, superseded by the 2015 update REF-0450
            'REF-2345',    # 2007 Cochrane phytoestrogens, superseded by the 2013 update REF-3806
            'REF-0015',    # ajwain review: dead DOI, no abstract, cannot be read
            'REF-0139',    # "The 1879 Beal seed viability experiment" - irrelevant to tansy's actions
            'REF-0167'],   # chocolate confectionery technology book cited for four pharmacological actions
    new=NEW)

PLAN = {
    'tanacetum_parthenium': [
        ('purge', 'REF-1573'),
        ('null', 'migraine', ['REF-1576', 'REF-1575']),   # MIG-99 dose-finding trial failed overall; 2020 SR "mixed"
        ('add', 'migraine', ['REF-3791']),
        ('nulladd', 'arthritis', ['REF-3792']),
        ('rm', 'pain', ['REF-0450']), ('add', 'pain', ['REF-1574']),
        ('arm', 'anti-inflammatory', ['REF-0450']),
        ('add', 'skin-irritation', ['REF-1578']),
        ('note', 'migraine', 'Feverfew modestly reduced migraine frequency in the 2015 Cochrane review (low-quality evidence) and in a randomized trial of a CO2 extract (MIG-99); a smaller dose-finding trial and a 2020 systematic review found mixed results'),
        ('note', 'headache', 'Feverfew modestly reduced migraine headaches in a Cochrane review (low-quality evidence)'),
        ('note', 'arthritis', 'Traditionally used for rheumatoid arthritis (review); a placebo-controlled trial in rheumatoid arthritis found no benefit'),
        ('note', 'fever', 'Traditional use for fevers (review)'),
        ('note', 'pain', 'Traditionally used for toothache and stomach ache (review)'),
        ('note', 'inflammation', 'A parthenolide-depleted feverfew extract had anti-inflammatory activity in the lab (preclinical)'),
        ('note', 'skin-irritation', 'A parthenolide-depleted feverfew extract reduced chemically induced skin redness in a clinical model and inflammation in the lab'),
    ],
    'tanacetum_vulgare': [('purge', 'REF-0139')] + [('rm', c, ['REF-0098']) for c in ('arthritis', 'bloating', 'indigestion', 'infection', 'inflammation', 'menstrual-cramps', 'muscle-spasm', 'skin-irritation', 'wounds')]
                         + [('arm', a, ['REF-0098']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'digestive')] + [
        ('drop', 'bloating'), ('drop', 'indigestion'),   # own safety note: not recommended for internal use (thujone)
        ('drop', 'menstrual-cramps'), ('drop', 'muscle-spasm'),   # an emmenagogue, not an antispasmodic for cramps; nothing names them
        ('add', 'arthritis', ['REF-3811']), ('add', 'skin-irritation', ['REF-3811']),
        ('aadd', 'digestive', ['REF-3811']), ('aadd', 'antispasmodic', ['REF-3811']),
        ('arm', 'antimicrobial', ['REF-1297']), ('refadd', ['REF-1297']),   # fish parasite
        ('note', 'arthritis', 'Hot tansy fomentations were traditionally applied to rheumatic joints, and it was taken for gout (Grieve, A Modern Herbal); not recommended internally because of thujone toxicity'),
        ('note', 'skin-irritation', 'Traditionally applied to eruptive skin diseases (Grieve, A Modern Herbal)'),
        ('note', 'infection', 'Tansy essential oil was active against multidrug-resistant bacteria in the lab (preclinical)'),
    ],
    'taraxacum_officinale': [('rmk', c, ['REF-0326']) for c in ('appetite-loss', 'arthritis', 'bloating', 'constipation', 'indigestion', 'skin-irritation')] + [
        ('rm', 'bloating', ['REF-0328']),
        ('add', 'appetite-loss', ['REF-3812']), ('add', 'indigestion', ['REF-3812']), ('add', 'constipation', ['REF-3812']),
        ('add', 'liver-support', ['REF-3812', 'REF-0328']), ('add', 'skin-irritation', ['REF-3812', 'REF-0328']),
        ('add', 'swelling', ['REF-3812', 'REF-0328']), ('add', 'urinary-support', ['REF-3812', 'REF-0328']), ('add', 'arthritis', ['REF-0328']),
        ('rmk', 'detox', ['REF-0329', 'REF-0338']), ('rmk', 'liver-support', ['REF-0338']), ('rmk', 'swelling', ['REF-0338']),
        ('rmk', 'urinary-support', ['REF-0338']), ('rmk', 'uti', ['REF-0321', 'REF-0338']), ('add', 'uti', ['REF-2953']),
        ('rm', 'infection', ['REF-0333']), ('add', 'infection', ['REF-2953']), ('rm', 'wounds', ['REF-0333']),
        ('arm', 'anti-inflammatory', ['REF-0333']), ('arm', 'antimicrobial', ['REF-0333']), ('arm', 'antioxidant', ['REF-0333']), ('refadd', ['REF-0333']),   # genus-level
        ('arm', 'diuretic', ['REF-2968']), ('nulladd', 'swelling', ['REF-2968']), ('nulladd', 'urinary-support', ['REF-2968']),
        ('rmk', 'immune-support', ['REF-2964']),
        ('aadd', 'diuretic', ['REF-3812']), ('aadd', 'laxative', ['REF-3812']), ('aadd', 'digestive', ['REF-3812']),
        ('note', 'appetite-loss', 'Traditional bitter tonic for poor appetite and weak digestion (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'indigestion', 'Traditional bitter tonic for dyspepsia (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'constipation', 'Traditional mild laxative (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'liver-support', 'Traditional remedy for a sluggish liver, jaundice and gallstones (Grieve, A Modern Herbal; Herbal Reality); dandelion protected the liver in animal studies (reviews; preclinical)'),
        ('note', 'skin-irritation', 'Traditionally used for eczema and skin eruptions (Grieve, A Modern Herbal; Herbal Reality)'),
        ('note', 'swelling', 'Traditional diuretic for dropsy and fluid retention (Grieve, A Modern Herbal; Herbal Reality); a leaf extract raised urine output in a small one-day pilot study in people, but a mouse study found no diuretic effect'),
        ('note', 'urinary-support', 'Traditional diuretic for kidney gravel and stones (Grieve, A Modern Herbal; Herbal Reality); a leaf extract raised urine frequency in a small pilot study in people'),
        ('note', 'uti', 'Dandelion extract was active against urinary-tract bacteria in the lab (preclinical)'),
        ('note', 'arthritis', 'Traditionally used for arthritis and gout (Herbal Reality)'),
        ('note', 'infection', 'Dandelion extract was active against Staphylococcus aureus and other bacteria in the lab (preclinical)'),
        ('note', 'detox', 'Traditional "cleansing" herb for the liver (review)'),
        ('note', 'inflammation', 'Dandelion extracts reduced inflammation in lab and animal studies (reviews; preclinical)'),
        ('note', 'cancer', 'Dandelion extracts slowed or killed cancer cells in lab and animal studies (preclinical)'),
        ('note', 'immune-support', 'Dandelion fractions stimulated immune cells in the lab (preclinical)'),
    ],
    'theobroma_cacao': [
        ('purge', 'REF-0167'),
        ('rm', 'cardiovascular-support', ['REF-1092']), ('refadd', ['REF-1092']),   # cell-line apolipoprotein study
        ('null', 'cardiovascular-support', ['REF-1084', 'REF-1085']),   # SR: no BP/lipid effect in healthy people; COSMOS: primary endpoint null
        ('add', 'cardiovascular-support', ['REF-3793']),
        ('newpair', 'high-blood-pressure', ['REF-3793', 'REF-3794'], 'Cocoa flavanols slightly lowered blood pressure in a Cochrane review and a 2026 meta-analysis of randomized trials, more in people with high blood pressure'),
        ('add', 'cognitive-function', ['REF-3795']), ('add', 'memory', ['REF-3795']),
        ('note', 'cardiovascular-support', 'Cocoa flavanols slightly lowered blood pressure in a Cochrane review; the large COSMOS trial found no reduction in total cardiovascular events (fewer cardiovascular deaths was a secondary finding), and a 2021 systematic review found no effect on blood pressure or lipids in healthy people'),
        ('note', 'cognitive-function', 'Regular chocolate or cocoa improved executive function in a meta-analysis of trials in healthy adults'),
        ('note', 'memory', 'Daily cocoa improved learning, memory and attention in young adults in a meta-analysis of trials'),
        ('note', 'inflammation', 'Cocoa polyphenols had anti-inflammatory effects (reviews; mostly preclinical)'),
        ('note', 'skin-irritation', 'Cacao extract eased atopic-dermatitis-like skin symptoms in mice (preclinical)'),
    ],
    'thymus_serpyllum': [('arm', a, ['REF-0133']) for a in ('anti-inflammatory', 'antioxidant', 'gastroprotective')] + [
        ('newpair', 'indigestion', ['REF-3796'], 'A wild thyme extract reduced digestive discomfort and improved quality of life vs placebo in a randomized trial in adults with persistent digestive complaints; traditional remedy for weak digestion and flatulence (Grieve, A Modern Herbal)'),
        ('add', 'indigestion', ['REF-3814']),
        ('note', 'infection', 'Wild thyme was active against mouth bacteria in the lab (preclinical)'),
        ('note', 'cancer', 'Wild thyme extract slowed breast cancer cell growth in the lab (preclinical)'),
    ],
    'thymus_vulgaris': [
        ('add', 'cough', ['REF-3797', 'REF-3813']), ('add', 'cold', ['REF-3813']), ('add', 'bronchitis', ['REF-3813']),
        ('add', 'respiratory-support', ['REF-3797', 'REF-3813']),
        ('add', 'menstrual-cramps', ['REF-3798']), ('status', 'menstrual-cramps', 'verified'),
        ('drop', 'muscle-spasm'),   # airway/gut smooth-muscle antispasmodic: off-target
        ('aadd', 'antispasmodic', ['REF-3813']), ('aadd', 'antimicrobial', ['REF-3813']),
        ('newpair', 'anxiety', ['REF-3799'], 'Dried thyme leaves reduced anxiety scores vs control in university students in a randomized trial'),
        ('newpair', 'depression', ['REF-3799'], 'Dried thyme leaves reduced depression scores vs control in university students in a randomized trial'),
        ('newpair', 'insomnia', ['REF-3799'], 'Dried thyme leaves improved overall sleep quality (not time to fall asleep or sleep length) vs control in university students in a randomized trial'),
        ('newpair', 'memory', ['REF-3799'], 'Dried thyme leaves improved prospective and retrospective memory vs control in university students in a randomized trial'),
        ('newpair', 'oral-health', ['REF-3800'], 'A thyme mouthwash reduced bad breath and gum inflammation after periodontal treatment in a randomized trial'),
        ('note', 'bronchitis', 'Traditional remedy for coughs and bronchial complaints (Grieve, A Modern Herbal); traditional expectorant for productive cough (EU herbal monograph)'),
        ('note', 'cold', 'Traditional expectorant for productive cough with a cold (EU herbal monograph); traditionally taken at the start of a cold (Grieve, A Modern Herbal)'),
        ('note', 'cough', 'Thyme syrup reduced cough vs placebo in children with asthma attacks in a randomized trial; traditional expectorant for productive cough with a cold (EU herbal monograph) and for whooping cough (Grieve, A Modern Herbal)'),
        ('note', 'respiratory-support', 'Traditional expectorant for coughs and chest complaints (EU herbal monograph; Grieve, A Modern Herbal); thyme syrup eased cough in children with asthma in a randomized trial'),
        ('note', 'menstrual-cramps', 'Thyme reduced period pain as much as ibuprofen and more than placebo in a triple-blind randomized trial'),
        ('note', 'infection', 'Thymol and carvacrol, the main compounds of thyme, are antimicrobial in the lab (reviews; preclinical)'),
        ('note', 'wounds', 'Thymol and carvacrol, the main compounds of thyme, are antimicrobial and were reviewed for wound healing (preclinical)'),
        ('note', 'cancer', 'A thyme oil nanoemulsion killed cancer cells in the lab (preclinical)'),
    ],
    'tilia_cordata': [
        ('rmk', 'anxiety', ['REF-0478']),   # EU monograph covers mild mental stress, not anxiety
        ('add', 'nervous-tension', ['REF-3815']),
        ('note', 'cold', 'Traditional use for the symptoms of the common cold (EU herbal monograph)'),
        ('note', 'cough', 'Traditional use for the symptoms of the common cold (EU herbal monograph)'),
        ('note', 'fever', 'Traditional use for the symptoms of the common cold (EU herbal monograph)'),
        ('note', 'stress', 'Traditional use for relief of mild symptoms of mental stress (EU herbal monograph)'),
        ('note', 'nervous-tension', 'Traditional use for mild mental stress (EU herbal monograph) and for hysteria and palpitations (Grieve, A Modern Herbal)'),
        ('note', 'cancer', 'Linden flower extracts killed pancreatic cancer cells in the lab (preclinical)'),
    ],
    'trachyspermum_ammi': [
        ('purge', 'REF-0015'),
        ('rm', 'menstrual-cramps', ['REF-0017', 'REF-0031']),
        ('rm', 'oral-health', ['REF-0017', 'REF-0031', 'REF-0275']), ('arm', 'digestive', ['REF-0275']), ('refadd', ['REF-0275']),
        ('rm', 'indigestion', ['REF-0031']),
        ('add', 'respiratory-support', ['REF-3803']),
        ('newpair', 'pain', ['REF-1920', 'REF-3801'], 'An ajwain cream reduced neuropathic burning feet vs placebo in a randomized trial, and ajwain oil eased dental injection pain in children better than an anaesthetic spray; it did not help chemotherapy nerve pain in a pilot trial'),
        ('nulladd', 'pain', ['REF-3802']),
        ('status', 'oral-health', 'needs-review'),
        ('note', 'bloating', 'Traditional carminative for flatulence and bloating (reviews)'),
        ('note', 'indigestion', 'Traditional digestive (review); ajwain essential oil healed stomach ulcers in rats (preclinical)'),
        ('note', 'oral-health', 'Ajwain oil killed mouth bacteria in the lab (preclinical)'),
        ('note', 'respiratory-support', 'Boiled ajwain extract widened the airways of people with asthma, comparable to theophylline, in a placebo-controlled study; traditional respiratory remedy (reviews)'),
    ],
    'trametes_versicolor': [('arm', a, ['REF-0282']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antiviral')]
                           + [('arm', a, ['REF-0300']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antiviral')] + [
        ('drop', 'cold'),   # nothing names colds
        ('add', 'cancer', ['REF-3804']),
        ('note', 'cancer', 'Turkey tail extracts (PSK, PSP) improved survival as add-ons to cancer treatment in a meta-analysis, most clearly in breast, gastric and colorectal cancer; a Cochrane review in colorectal cancer found low-certainty evidence of a small survival benefit'),
        ('note', 'immune-support', 'Turkey tail polysaccharides (PSK, PSP) supported immune function, especially during cancer treatment (reviews)'),
        ('note', 'infection', 'Reviewed as antimicrobial and antiviral (review; mostly preclinical)'),
    ],
    'trifolium_pratense': [('purge', 'REF-2345')] + [('arm', a, ['REF-0013']) for a in ('anti-inflammatory', 'antioxidant', 'antispasmodic', 'expectorant')] + [
        ('rm', 'hot-flashes', ['REF-2344']),
        ('nulladd', 'hot-flashes', ['REF-3406', 'REF-3805', 'REF-3806']), ('nulladd', 'menopause', ['REF-3406', 'REF-3805', 'REF-3806']),
        ('add', 'hot-flashes', ['REF-3807', 'REF-3808']), ('add', 'menopause', ['REF-3807']),
        ('rm', 'menopause', ['REF-2347']), ('refadd', ['REF-2347']),   # osteoporosis in rats
        ('rm', 'high-cholesterol', ['REF-1108']), ('add', 'high-cholesterol', ['REF-3809', 'REF-1105']),
        ('rm', 'cardiovascular-support', ['REF-0013', 'REF-0036', 'REF-0112', 'REF-1113']), ('rmk', 'cardiovascular-support', ['REF-2928']), ('refadd', ['REF-1113']),
        ('rm', 'arthritis', ['REF-0036', 'REF-0112']), ('rm', 'inflammation', ['REF-0036', 'REF-0112']), ('rm', 'skin-irritation', ['REF-0036', 'REF-0112']),
        ('drop', 'menstrual-cramps'), ('drop', 'muscle-spasm'),
        ('add', 'cough', ['REF-3816']), ('add', 'bronchitis', ['REF-3816']), ('add', 'respiratory-support', ['REF-3816']),
        ('arm', 'antispasmodic', ['REF-1111']), ('refadd', ['REF-1111']), ('aadd', 'antispasmodic', ['REF-3816']),
        ('rm', 'wounds', ['REF-2934', 'REF-2890']), ('arm', 'vulnerary', ['REF-2934', 'REF-2890']), ('refadd', ['REF-2934']),   # red clover + basil combinations
        ('nulladd', 'cognitive-function', ['REF-3810']),
        ('status', 'blood-sugar', 'needs-review'),
        ('note', 'hot-flashes', 'Red clover isoflavones modestly reduced hot flashes vs placebo in meta-analyses (a 2026 GRADE review; Promensil 80 mg), but the 2013 Cochrane review found no conclusive evidence for phytoestrogens and two large US trials (ICE 2003; Geller 2009) found no clinically important benefit'),
        ('note', 'menopause', 'Red clover isoflavones modestly reduced hot flashes and some menopausal symptoms in meta-analyses, but the 2013 Cochrane review found no conclusive evidence for phytoestrogens and two large US trials found no clinically important benefit'),
        ('note', 'high-cholesterol', 'Red clover isoflavones lowered total and LDL cholesterol and triglycerides in perimenopausal and postmenopausal women in meta-analyses of trials'),
        ('note', 'cardiovascular-support', 'Red clover isoflavones improved blood lipids in menopausal women (meta-analyses); its compounds protected the heart in animal studies (preclinical)'),
        ('note', 'cough', 'Traditional remedy for bronchial and whooping cough (Grieve, A Modern Herbal; British Herbal Pharmacopoeia)'),
        ('note', 'bronchitis', 'Traditional remedy for bronchial and whooping cough (Grieve, A Modern Herbal; British Herbal Pharmacopoeia)'),
        ('note', 'respiratory-support', 'Traditional remedy for bronchial and whooping cough (Grieve, A Modern Herbal; British Herbal Pharmacopoeia)'),
        ('note', 'arthritis', 'Biochanin A, a red clover isoflavone, eased arthritis in mice (preclinical)'),
        ('note', 'inflammation', 'Red clover anthocyanins reduced inflammation in immune cells in the lab (preclinical)'),
        ('note', 'cancer', 'Red clover extract slowed breast and other cancer cells in lab and animal studies (preclinical); its safety in breast or womb cancer is not established'),
        ('note', 'blood-sugar', 'Red clover polysaccharides and extracts lowered blood sugar in lab and animal studies (preclinical)'),
        ('note', 'cognitive-function', 'Red clover isoflavones protected nerve cells in lab and animal studies (preclinical); a randomized trial in postmenopausal women found no major effect on cognition'),
    ],
}

NOTES = {
    'tanacetum_parthenium': 'Deep audit (2nd pass + deep). 2000 Cochrane REF-1573 purged and deleted (superseded by the 2015 update REF-0450). MIG-99 dose-finding RCT REF-1576 (no overall effect) and the 2020 herbal-migraine SR REF-1575 ("mixed") moved to no-effect; the positive 2005 MIG-99 RCT REF-3791 added. Pattrick 1989 RA RCT REF-3792 recorded as no-effect. Cochrane REF-0450 removed from pain (never names it) and the anti-inflammatory action; review REF-1574 (retagged narrative-review) names toothache/stomach ache. REF-0552 retagged preclinical (rat migraine model).',
    'tanacetum_vulgare': 'Deep audit. REF-0139 "The 1879 Beal seed viability experiment" was cited for 5 actions: purged and deleted. Generic Grieve REF-0098 was pinned to all 9 pairs; the tansy entry (REF-3811, read 2026-11-13) names gout, rheumatic parts (external), eruptive skin disease, flatulence, worms - used where it fits. Bloating and indigestion dropped: the record\'s own safety note says tansy is not recommended internally (thujone). Menstrual-cramps and muscle-spasm dropped (Grieve: emmenagogue; nothing names cramps). Fish-parasite study REF-1297 removed from the antimicrobial action.',
    'taraxacum_officinale': 'Deep audit. 2024 review REF-0326 (retagged narrative-review) was pinned to 13 pairs; moved to mechanistic on the 6 it never names. Review REF-0338 and REF-0329 likewise on detox/liver/urinary/swelling/uti. Herbal Reality REF-0328 (has a reference list; says clinical evidence is minimal) kept for what it names; Grieve REF-3812 added (liver, gravel, dropsy, dyspepsia, appetite, constipation, eczema). Genus-level review REF-0333 removed from pairs and actions; wounds dropped. Diuretic screen REF-2968 (no increase in urine volume) moved from the diuretic action to no-effect. REF-0321 retagged clinical (single-arm pilot, not an RCT).',
    'theobroma_cacao': 'Deep audit. Confectionery technology book REF-0167 cited for four pharmacological actions: purged and deleted. Cell study REF-1092 removed from cardiovascular-support. 2021 SR REF-1084 (no BP/lipid effect in healthy people) and COSMOS REF-1085 (primary endpoint null) moved to no-effect. Cochrane BP review REF-3793 added. New pair (owner rule): high-blood-pressure (Cochrane + 2026 MA). Chocolate-cognition MA REF-3795 added. REF-0131 retagged narrative-review.',
    'thymus_serpyllum': 'Deep audit. Oral-pathogen study REF-0133 (by title) removed from the anti-inflammatory, antioxidant and gastroprotective actions. New pair (owner rule): indigestion (2026 multicentre placebo RCT REF-3796) plus Grieve REF-3814. REF-1094 retagged systematic-review (PubMed type).',
    'thymus_vulgaris': 'Deep audit. Cough/cold/bronchitis notes cited a thyme-ivy combination trial that is not referenced and is a combination: rewritten to the EU monograph and Grieve REF-3813. Thyme-syrup asthma-cough RCT REF-3797 and the thyme vs ibuprofen vs placebo dysmenorrhoea RCT REF-3798 added. Muscle-spasm dropped (off-target). New pairs (owner rule): anxiety, depression, insomnia, memory (student RCT REF-3799), oral-health (halitosis/gingivitis RCT REF-3800). Gap: thyme-honey RCTs (combination), Shirazi thyme (different species).',
    'tilia_cordata': 'Deep audit. EU monograph REF-0478 covers common-cold symptoms and mild mental stress: moved to mechanistic for anxiety; the stress note no longer cites T. americana animal data. Grieve REF-3815 added to nervous-tension, and its warning about stale flowers added as a safety note. Gap: the only linden RCT is a four-ingredient sleep combination.',
    'trachyspermum_ammi': 'Deep audit. Review REF-0015 (dead DOI, no abstract) purged and deleted. Reviews REF-0017/REF-0031 (retagged narrative-review) removed from menstrual-cramps (dropped), oral-health and indigestion (never named). GC-MS antibacterial study REF-0275 removed from oral-health and the digestive action. Asthma bronchodilator study REF-3803 added. New pair (owner rule): pain (held placebo RCT REF-1920; dental-injection RCT REF-3801; CIPN pilot REF-3802 no-effect). Gap: functional dyspepsia RCT 29299438 used an Apium + ajwain combination.',
    'trametes_versicolor': 'Deep audit. Cold dropped: its only card (2002 review REF-0052) never names colds. Breast-cancer review REF-0282 and a general medicinal-mushroom review REF-0300 removed from four actions they never address. Yun Zhi survival MA REF-3804 added to cancer. REF-0052/REF-0282 retagged narrative-review. Gap: HPV RCTs used mushroom combinations.',
    'trifolium_pratense': 'Deep audit. 2007 Cochrane REF-2345 purged and deleted (superseded by the 2013 update REF-3806, which found no conclusive evidence - recorded as no-effect with the ICE trial REF-3805 and Geller 2009 REF-3406). Positive hot-flash MAs REF-3807/REF-3808 added. Bone-density RCT REF-0013 removed from 4 actions and cardiovascular-support. British Herbal Pharmacopoeia REF-0036 and Hoffmann REF-0112 (unverifiable books) kept only where Grieve REF-3816 agrees (cough, bronchitis, respiratory); menstrual-cramps and muscle-spasm dropped. Broiler-chicken study REF-1113 and two red clover + basil combination studies removed; wounds dropped. Lipid MA REF-3809 added; Howes 2004 cognition RCT REF-3810 no-effect. Blood-sugar is preclinical only (verified -> needs-review). Gap: glucose RCT 33761143 (primary outcome not different).',
}


def post():
    path = 'plants/tilia_cordata.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    d['contraindications'].append({'note': 'Tea made from old, stale lime flowers may cause narcotic intoxication; use fresh-dried flowers (Grieve, A Modern Herbal).',
                                   'severity': 'info', 'reference_ids': ['REF-3815'], 'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 17', os.path.join(HERE, 'deep', 'd17_changes.tsv'), **BIB)
    post()
