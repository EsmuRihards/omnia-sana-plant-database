"""Deep audit of batch 16 (scrophularia-nodosa .. syzygium-aromaticum): 2nd-pass strict-match + deep checks. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit.
New refs REF-3764..REF-3790 (Grieve x6 read 2026-11-13 by the web-fetch agent; rest PubMed efetch)."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib
import yamlsplice as Y

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3764', '21954478', 'sawpalmettocamus', 'rct'),
    ('REF-3765', '16467543', 'sawpalmettobent', 'rct'),
    ('REF-3766', '39042923', 'sawpalmettojpadults', 'rct'),
    ('REF-3767', '35334848', 'sawpalmettowomen', 'rct'),
    ('REF-3768', '32884683', 'sawpalmettojpmen', 'rct'),
    ('REF-3769', '38579127', 'silymarinnafld2024', 'meta-analysis'),
    ('REF-3770', '29245314', 'silymarinnafld2017', 'meta-analysis'),
    ('REF-3771', '40552569', 'silymarincochranemasld', 'systematic-review'),
    ('REF-3772', '37351038', 'silymarinantitb', 'rct'),
    ('REF-3773', '17943794', 'milkthistlecochrane2007', 'systematic-review'),
    ('REF-3774', '22797645', 'silymarinhcv', 'rct'),
    ('REF-3775', '17072885', 'silymarint2d', 'rct'),
    ('REF-3776', '32762030', 'milkthistlemenopause', 'rct'),
    ('REF-3777', '34620153', 'milkthistleepisiotomy', 'rct'),
    ('REF-3778', '30479044', 'silymarinradiodermatitis', 'rct'),
    ('REF-3779', '19460762', 'comfreybackpain', 'rct'),
    ('REF-3780', '17169543', 'comfreykneeoa', 'rct'),
    ('REF-3781', '15500257', 'comfreyankle', 'rct'),
    ('REF-3782', '16323288', 'comfreydiclofenac', 'rct'),
    ('REF-3783', '35028171', 'comfreybruise', 'rct'),
    ('REF-3784', '16530911', 'clovegel', 'rct'),
])


def grieve(key, rid, name, url, summary):
    NEW[key] = (rid, [('author', 'Grieve, M'), ('title', f'{name} - A Modern Herbal'), ('year', '1931'), ('url', url),
                      ('note', rid), ('study_type', 'traditional'),
                      ('summary', f'Grieve, A Modern Herbal (1931). {summary} Read 2026-11-13.')])


grieve('grieve1931figwort', 'REF-3785', 'Figwort, Knotted (Scrophularia nodosa)', 'https://www.botanical.com/botanical/mgmh/f/figkno13.html',
       'Diuretic and anodyne; used mainly externally, as a fomentation or ointment for sprains, swellings, inflammations, wounds, cutaneous eruptions, abscesses, scrofulous sores and burns.')
grieve('grieve1931betony', 'REF-3786', 'Betony, Wood (Stachys officinalis)', 'https://www.botanical.com/botanical/mgmh/b/betowo35.html',
       'Used for maladies of the head, nervous headaches, pain in the head and face, neuralgia and nervous affections; as a tonic in dyspepsia; as an alterative for rheumatism and scrofula; also gout, colds and coughs; applied externally to wounds, ulcers, boils and bruises.')
grieve('grieve1931chickweed', 'REF-3787', 'Chickweed (Stellaria media)', 'https://www.botanical.com/botanical/mgmh/c/chickw60.html',
       'Used mostly as an ointment or poultice: for inflammation, indolent ulcers, abscesses, piles, cutaneous diseases, redness, itch and wheals; internally for constipation, coughs and hoarseness.')
grieve('grieve1931cloves', 'REF-3788', 'Cloves (Syzygium aromaticum)', 'https://www.botanical.com/botanical/mgmh/c/cloves76.html',
       'Taken in powder or infusion for nausea, vomiting, flatulence and languid indigestion or dyspepsia; applied to decayed teeth as a feeble local anaesthetic; germicide and antiseptic; stimulating expectorant.')
grieve('grieve1931skullcap', 'REF-3789', 'Scullcap, Virginian (Scutellaria lateriflora)', 'https://www.botanical.com/botanical/mgmh/s/scullc34.html',
       'Taken internally for hysteria, convulsions, St Vitus\'s dance, nervous headaches, neuralgia and "all disorders of the nervous system".')
grieve('grieve1931goldenrod', 'REF-3790', 'Golden Rod (Solidago virgaurea)', 'https://www.botanical.com/botanical/mgmh/g/golrod26.html',
       'Diuretic; used for stone in the bladder, gravel and urinary obstruction; for sickness from weak digestion, painful or absent periods and diphtheria; the powder applied to old ulcers.')

BIB = dict(
    retag={'REF-0630': 'preclinical', 'REF-0510': 'preclinical', 'REF-0483': 'narrative-review', 'REF-0484': 'narrative-review',
           'REF-0281': 'narrative-review', 'REF-3174': 'narrative-review'},
    delete=['REF-0451',    # WebMD figwort page: 404, content cannot be checked
            'REF-0535',    # Naturopathic Herbalist betony page: no references (web-page rule)
            'REF-0504', 'REF-1892'],   # 2012 Cochrane saw palmetto review + its BJU version, superseded by the 2023 update REF-1887
    new=NEW)

PLAN = {
    'scrophularia_nodosa': [
        ('purge', 'REF-0451'),
        ('rm', 'menstrual-cramps', ['REF-0630']), ('rm', 'muscle-spasm', ['REF-0630']),   # rabbit gut antispasmodic: off-target
        ('drop', 'uti'),   # diuretic only; nothing names infection
        ('rm', 'skin-irritation', ['REF-1035']), ('refadd', ['REF-1035']),   # wound-healing iridoids: a wound is not skin irritation
        ('rmk', 'acne', ['REF-0452']),
        ('add', 'skin-irritation', ['REF-3785']), ('add', 'swelling', ['REF-3785']), ('add', 'inflammation', ['REF-3785']),
        ('add', 'urinary-support', ['REF-3785']),
        ('aadd', 'diuretic', ['REF-3785']), ('aadd', 'anti-inflammatory', ['REF-3785']),
        ('note', 'arthritis', 'Traditionally used for rheumatic problems and joint pain (Medicinal Herbals)'),
        ('note', 'detox', 'Traditional "alterative" or blood-cleansing herb (Medicinal Herbals)'),
        ('note', 'inflammation', 'Traditionally applied as a fomentation to inflammations and swellings (Grieve, A Modern Herbal); figwort reduced inflammatory signals in mouse immune cells (preclinical)'),
        ('note', 'swelling', 'Traditionally applied as a fomentation to swellings and sprains (Grieve, A Modern Herbal)'),
        ('note', 'skin-irritation', 'Traditionally used for skin eruptions and rashes, applied as an ointment or wash (Grieve, A Modern Herbal; Medicinal Herbals)'),
        ('note', 'urinary-support', 'Traditional diuretic (Grieve, A Modern Herbal; Medicinal Herbals)'),
    ],
    'scutellaria_lateriflora': [
        ('null', 'anxiety', ['REF-0551']),   # BAI no different from placebo
        ('rm', 'stress', ['REF-0510']),
        ('add', 'nervous-tension', ['REF-3789']),
        ('note', 'anxiety', 'Skullcap reduced anxiety in a small placebo-controlled trial in healthy volunteers and in rats; a 2014 crossover trial in mostly non-anxious volunteers found no difference in anxiety vs placebo but improved overall mood'),
        ('note', 'insomnia', 'A skullcap extract supplement improved sleep quality, time to fall asleep and total sleep vs placebo in primary insomnia in a randomized crossover trial; traditional sedative'),
        ('note', 'stress', 'Traditional remedy for stress and nervous disorders; skullcap improved overall mood vs placebo in a randomized crossover trial'),
        ('note', 'nervous-tension', 'Traditional remedy for nervous disorders (Grieve, A Modern Herbal); skullcap improved overall mood without loss of energy or cognition vs placebo in a randomized crossover trial; its flavonoids bind the benzodiazepine site of the GABA-A receptor (preclinical)'),
    ],
    'serenoa_repens': [
        ('purge', 'REF-0504'), ('purge', 'REF-1892'),
        ('rm', 'prostate-support', ['REF-1893']), ('refadd', ['REF-1893']),   # Serenoa + lycopene + selenium combination
        ('null', 'prostate-support', ['REF-1887', 'REF-1890', 'REF-1508']), ('null', 'urinary-support', ['REF-1887', 'REF-1890', 'REF-1508']),
        ('nulladd', 'prostate-support', ['REF-3764', 'REF-3765']), ('nulladd', 'urinary-support', ['REF-3764', 'REF-3765']),
        ('add', 'urinary-support', ['REF-3766', 'REF-3767', 'REF-3768']),
        ('note', 'prostate-support', 'Urinary symptoms of an enlarged prostate (BPH): the 2023 Cochrane review found saw palmetto alone gives little to no benefit over placebo, and two large US trials (one at double and triple doses) found none; meta-analyses of one hexane extract (Permixon) report fewer night-time urinations and better flow, similar to tamsulosin'),
        ('note', 'urinary-support', 'Saw palmetto fruit extract eased mild urinary frequency vs placebo in three small Japanese randomized trials (women, men and healthy adults); in men with an enlarged prostate the 2023 Cochrane review found little to no benefit'),
    ],
    'silybum_marianum': [('arm', a, ['REF-0483']) for a in ('anti-inflammatory', 'antioxidant', 'digestive')] + [
        ('rmk', 'detox', ['REF-0483']), ('rmk', 'liver-support', ['REF-0484', 'REF-0560']),
        ('add', 'liver-support', ['REF-3769', 'REF-3770', 'REF-3771', 'REF-3772']), ('nulladd', 'liver-support', ['REF-3773', 'REF-3774']),
        ('note', 'liver-support', 'Silymarin lowered liver enzymes and improved liver fat in meta-analyses of trials in non-alcoholic fatty liver disease (a 2025 Cochrane review rates this evidence low to very low certainty) and reduced anti-tuberculosis drug liver injury in a small trial; for alcoholic and viral hepatitis a Cochrane review questioned any benefit, and a large hepatitis C trial found none'),
        ('add', 'blood-sugar', ['REF-3775']),
        ('note', 'blood-sugar', 'Silymarin lowered fasting blood sugar and HbA1c in type 2 diabetes in a randomized trial and a meta-analysis of trials (low-quality evidence)'),
        ('note', 'metabolic-support', 'Silymarin improved blood sugar control in type 2 diabetes in a meta-analysis of trials but had no effect on blood lipids'),
        ('note', 'cancer', 'Reviews describe anticancer effects of silymarin in lab and animal studies and its possible use alongside chemotherapy; clinical evidence is limited'),
        ('note', 'inflammation', 'Silymarin had anti-inflammatory effects in lab and animal studies (reviews; preclinical)'),
        ('newpair', 'hot-flashes', ['REF-3776'], 'Milk thistle extract reduced the frequency and severity of hot flashes vs placebo in a randomized trial'),
        ('newpair', 'menopause', ['REF-3776'], 'Milk thistle extract reduced hot flashes and menopausal symptom scores vs placebo in a randomized trial'),
        ('newpair', 'wounds', ['REF-3777'], 'A milk thistle ointment sped episiotomy wound healing and reduced pain in a randomized trial'),
        ('newpair', 'skin-irritation', ['REF-3778'], 'A silymarin gel reduced and delayed radiation skin reactions vs placebo during breast cancer radiotherapy in a randomized trial'),
    ],
    'solidago_canadensis': [
        ('rm', 'liver-support', ['REF-3165']), ('arm', 'hepatoprotective', ['REF-3165']), ('refadd', ['REF-3165']),   # GST enzyme activity in vitro
        ('rm', 'infection', ['REF-3170']),   # essential oil vs plant pathogens
        ('rm', 'uti', ['REF-3180']),
        ('rmk', 'cancer', ['REF-3163', 'REF-3164', 'REF-3166']),
        ('rmk', 'arthritis', ['REF-3161', 'REF-3160']), ('rmk', 'swelling', ['REF-3158']),
        ('note', 'inflammation', 'Canadian goldenrod extract and its compounds reduced inflammation in cell and mouse studies (preclinical)'),
        ('note', 'liver-support', 'Canadian goldenrod extract protected the liver from toxic injury in animal studies (preclinical)'),
        ('note', 'cancer', 'Canadian goldenrod essential oil slowed cancer cell growth in the lab (preclinical)'),
        ('note', 'infection', 'Canadian goldenrod extracts and essential oil were active against bacteria and Candida in the lab (preclinical)'),
        ('note', 'uti', 'Traditionally used for kidney and urinary tract diseases; its extract had antimicrobial activity in the lab (preclinical)'),
    ],
    'solidago_virgaurea': [('rm', c, ['REF-0016']) for c in ('arthritis', 'inflammation', 'skin-irritation', 'swelling', 'urinary-support', 'uti')]
                          + [('arm', a, ['REF-0016']) for a in ('anti-inflammatory', 'antioxidant', 'diuretic')] + [
        ('refadd', ['REF-0016']),   # 1990 saponin chemistry paper, no abstract - cannot support a use
        ('rm', 'swelling', ['REF-0069']), ('rm', 'uti', ['REF-0069']),   # EU monograph: flushing the urinary tract in minor urinary complaints only
        ('arm', 'diuretic', ['REF-1048']),
        ('arm', 'anti-inflammatory', ['REF-1047', 'REF-1050']), ('refadd', ['REF-1047']),
        ('add', 'urinary-support', ['REF-3790']), ('aadd', 'diuretic', ['REF-3790']),
        ('note', 'urinary-support', 'Traditional use to increase urine and flush the urinary tract in minor urinary complaints (EU herbal monograph); for gravel and bladder stone (Grieve, A Modern Herbal)'),
        ('note', 'uti', 'Goldenrod extract reduced the survival and biofilm of urinary E. coli in the lab, but weakened the effect of two antibiotics (preclinical)'),
        ('note', 'inflammation', 'Goldenrod compounds reduced inflammation in rats (preclinical)'),
        ('note', 'cancer', 'Goldenrod extract suppressed prostate tumour growth in mice (preclinical)'),
    ],
    'stachys_officinalis': [
        ('purge', 'REF-0535'),
        ('rmk', 'stress', ['REF-0534']),
        ('add', 'indigestion', ['REF-0534', 'REF-3786']), ('add', 'headache', ['REF-3786']), ('add', 'nervous-tension', ['REF-3786']),
        ('add', 'arthritis', ['REF-3786']),
        ('aadd', 'digestive', ['REF-3786']),
        ('arm', 'antioxidant', ['REF-1055']),   # a genotoxicity study, not antioxidant evidence; now a safety note
        ('note', 'anxiety', 'Traditional calming herb for anxiety, with minimal scientific evidence (PeaceHealth)'),
        ('note', 'headache', 'Traditional remedy for headaches and nerve pain in the head and face (PeaceHealth; Grieve, A Modern Herbal)'),
        ('note', 'nervous-tension', 'Traditional nerve tonic for nervous complaints (PeaceHealth; Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Used in European herbal medicine for heartburn and gastritis, and as a tonic for indigestion (PeaceHealth; Grieve, A Modern Herbal)'),
        ('note', 'arthritis', 'Traditionally used for rheumatism and gout (Grieve, A Modern Herbal)'),
        ('note', 'inflammation', 'Wood betony extract reduced inflammation in rats (preclinical)'),
    ],
    'stellaria_media': [
        ('rm', 'arthritis', ['REF-0048', 'REF-0098']), ('rmk', 'arthritis', ['REF-0906']),
        ('rmk', 'eczema', ['REF-0048', 'REF-0098']),
        ('rm', 'inflammation', ['REF-0098']), ('add', 'inflammation', ['REF-3787']),
        ('rm', 'skin-irritation', ['REF-0098']), ('add', 'skin-irritation', ['REF-3787']),
        ('arm', 'antioxidant', ['REF-0048', 'REF-0098']), ('aadd', 'anti-inflammatory', ['REF-3787']),
        ('note', 'inflammation', 'Traditionally applied as an ointment or poultice to inflammation (Grieve, A Modern Herbal); chickweed extract inhibited COX inflammatory enzymes in the lab (preclinical)'),
        ('note', 'skin-irritation', 'Traditionally applied to itching, redness and skin complaints as an ointment or wash (Grieve, A Modern Herbal)'),
    ],
    'symphytum_officinale': [
        ('drop', 'wounds'), ('drop', 'skin-irritation'),   # own safety note: do not apply to broken, damaged or irritated skin
        ('rm', 'bruising', ['REF-1070']), ('rm', 'pain', ['REF-1070']),
        ('arm', 'analgesic', ['REF-1070']), ('arm', 'anti-inflammatory', ['REF-1070']), ('refadd', ['REF-1070']),   # genus-level scoping review
        ('arm', 'vulnerary', ['REF-1072']), ('refadd', ['REF-1072']),   # homeopathic mother tincture, osteoblasts in vitro
        ('add', 'pain', ['REF-3779', 'REF-3780', 'REF-3781', 'REF-3782']), ('add', 'swelling', ['REF-3781']),
        ('add', 'arthritis', ['REF-3780']), ('add', 'back-pain', ['REF-3779', 'REF-1261']), ('add', 'bruising', ['REF-3783']),
        ('status', 'arthritis', 'verified'), ('status', 'back-pain', 'verified'), ('status', 'bruising', 'verified'),
        ('note', 'pain', 'Comfrey root ointment relieved pain vs placebo in randomized trials of acute back pain, knee osteoarthritis and ankle sprains, and matched diclofenac gel for ankle sprains; topical use only'),
        ('note', 'swelling', 'Comfrey root ointment reduced ankle swelling vs placebo after sprains in a randomized trial; EU herbal use for bruises and sprains'),
        ('note', 'bruising', 'Comfrey ointment sped the healing of injection bruises vs placebo in a randomized trial; EU herbal use for bruises and sprains'),
        ('note', 'back-pain', 'Comfrey root ointment reduced acute back pain vs placebo in a randomized trial (moderate-quality evidence, Cochrane review)'),
        ('note', 'arthritis', 'Comfrey root ointment reduced knee osteoarthritis pain and improved mobility vs placebo in a randomized trial'),
        ('note', 'inflammation', 'Topical comfrey relieves pain, inflammation and swelling of muscles and joints (clinical overview); comfrey compounds reduced inflammatory cytokines in the lab (preclinical)'),
    ],
    'syzygium_aromaticum': [('rm', c, ['REF-0029', 'REF-0309']) for c in ('arthritis', 'back-pain', 'headache', 'infection', 'inflammation', 'skin-irritation', 'wounds')] + [
        ('add', 'pain', ['REF-3784', 'REF-3788']), ('add', 'oral-health', ['REF-3784', 'REF-3788']),
        ('add', 'indigestion', ['REF-3788']), ('add', 'bloating', ['REF-3788']),
        ('aadd', 'digestive', ['REF-3788']), ('aadd', 'analgesic', ['REF-3788']), ('aadd', 'antimicrobial', ['REF-3788']),
        ('note', 'pain', 'Clove gel reduced needle-stick pain in the mouth vs placebo, as much as benzocaine, in a randomized trial; traditional toothache remedy (Grieve, A Modern Herbal)'),
        ('note', 'oral-health', 'Clove gel numbed the gums as well as benzocaine and better than placebo before needle insertion in a randomized trial; traditionally applied to decayed teeth as a mild local anaesthetic (Grieve, A Modern Herbal)'),
        ('note', 'indigestion', 'Traditionally taken for indigestion, nausea and flatulence (Grieve, A Modern Herbal)'),
        ('note', 'bloating', 'Traditionally taken for flatulence and indigestion (Grieve, A Modern Herbal)'),
        ('note', 'arthritis', 'Nanostructured clove oil reduced arthritis in rats (preclinical)'),
        ('note', 'cancer', 'Clove infusion showed chemopreventive effects against lung cancer in mice (preclinical)'),
        ('note', 'infection', 'Clove extract was active against vaginal Candida in the lab (preclinical)'),
    ],
}

NOTES = {
    'scrophularia_nodosa': 'Deep audit (2nd pass + deep). WebMD figwort page REF-0451 returns 404 (2026-11-13): purged and deleted. Medicinal Herbals blog REF-0452 has a short reference list, kept only for what it names (skin conditions, rheumatic and joint pain, cleansing, diuretic, swellings). Grieve REF-3785 (external use for sprains, swellings, inflammations, eruptions; diuretic) added. Menstrual-cramps and muscle-spasm dropped (rabbit gut antispasmodic REF-0630, retagged preclinical). UTI dropped (diuretic only). Wound-healing iridoid study REF-1035 removed from skin-irritation.',
    'scutellaria_lateriflora': 'Deep audit. Brock 2014 crossover RCT REF-0551 found no anxiety (BAI) difference vs placebo: moved to no-effect for anxiety, kept for mood/stress/nervous tension. REF-0510 retagged preclinical (rat behaviour + phytochemistry) and removed from stress (never names it). Grieve REF-3789 added to nervous-tension. REF-1562 (insomnia RCT, single-herb extract) checked and kept.',
    'serenoa_repens': 'Deep audit. 2012 Cochrane REF-0504 and its BJU version REF-1892 purged and deleted (superseded by the 2023 update REF-1887). The 2023 Cochrane, the 2021 MA REF-1890 and the CAM review REF-1508 all conclude no benefit and were cited as support: moved to no-effect. CAMUS 2011 REF-3764 and Bent 2006 REF-3765 (NEJM) added as no-effect. Lycopene/selenium combination review REF-1893 removed. Three Japanese placebo RCTs on mild urinary symptoms added to urinary-support. Gap: hair-loss RCTs (no hair-loss condition in the vocabulary).',
    'silybum_marianum': 'Deep audit. Safety review REF-0483 (tagged rct; retagged narrative-review) removed from anti-inflammatory/antioxidant/digestive actions and detox. GI-cancer review REF-0484 (retagged narrative-review) and the NAFLD network MA REF-0560 (reports no silymarin result) moved to mechanistic for liver-support. Added NAFLD MAs REF-3769/REF-3770, the 2025 Cochrane MASLD review REF-3771 (low to very low certainty) and an anti-TB DILI RCT REF-3772; Cochrane 2007 REF-3773 (alcoholic/viral hepatitis, benefit questioned) and the SyNCH HCV RCT REF-3774 recorded as no-effect. New pairs (owner rule): hot-flashes, menopause (placebo RCT), wounds (episiotomy RCT), skin-irritation (radiodermatitis RCT). Gaps: OCD vs fluoxetine RCT, melasma, mucositis.',
    'solidago_canadensis': 'Deep audit. In vitro GST study REF-3165 removed from liver-support and the hepatoprotective action. Essential-oil study against plant pathogens REF-3170 removed from infection. Haudenosaunee screen REF-3180 removed from uti (tested E. coli/Salmonella/S. aureus, not urinary infection). Cell-line and enzyme studies on cancer, and LPS/colitis and aquaretic studies on arthritis/swelling, moved to mechanistic (they never name those symptoms). Empty notes filled. REF-3174 retagged narrative-review.',
    'solidago_virgaurea': 'Deep audit. 1990 saponin chemistry paper REF-0016 (no abstract) was pinned to 6 pairs and 3 actions: removed. EU monograph REF-0069 covers flushing the urinary tract in minor urinary complaints only: removed from swelling and uti. Grieve REF-3790 (gravel, bladder stone, urinary obstruction) added to urinary-support. UPEC study REF-1048 removed from the diuretic action and its antibiotic antagonism finding added as a safety note. Oral-Candida toothpaste RCT REF-1047 and prostate-tumour study REF-1050 removed from the anti-inflammatory action.',
    'stachys_officinalis': 'Deep audit. Naturopathic Herbalist page REF-0535 (no references) purged and deleted; it was the only source for bloating, menstrual cramps and muscle spasm (dropped) and for safety note #1. PeaceHealth REF-0534 (5 references; 1-star traditional ratings) kept for anxiety, nervous tension, headache and added to indigestion (heartburn, gastritis). Grieve REF-3786 added (head maladies, neuralgia, dyspepsia, rheumatism). Safety notes re-sourced to PeaceHealth; the unsourced "may lower blood pressure" line removed. Genotoxicity study REF-1055 moved from the antioxidant action to a new info safety note.',
    'stellaria_media': 'Deep audit. Chevallier REF-0048 and Grieve REF-0098 were pinned to all 4 pairs. Grieve\'s chickweed entry (REF-3787, read 2026-11-13) names inflammation, itch, cutaneous diseases, redness - not rheumatism or eczema by name: removed from arthritis, kept as mechanistic for eczema; REF-0098 replaced by the entry-specific REF-3787. COX in vitro study REF-0906 moved to mechanistic for arthritis.',
    'symphytum_officinale': 'Deep audit. Wounds and skin-irritation dropped: the record\'s own safety note says do not apply to broken, damaged or irritated skin. Five held-back Kytta RCTs added (acute back pain REF-3779, knee OA REF-3780, ankle sprain vs placebo REF-3781, vs diclofenac REF-3782; the 2007 diclofenac re-analysis 18193693 not added as duplicate data) plus an injection-bruise RCT REF-3783 and the 2014 Cochrane LBP review REF-1261 (names comfrey). Genus-level scoping review REF-1070 and the homeopathic osteoblast study REF-1072 removed from pairs/actions. REF-0281 retagged narrative-review. Combination RCTs (with methyl nicotinate; with tannic acid) not used.',
    'syzygium_aromaticum': 'Deep audit. Bhowmik 2012 review REF-0029 and the generic WHO monographs citation REF-0309 were pinned to all 11 pairs; neither could be read (journal archive 404; WHO PDF 403). Kept only where Grieve REF-3788 (read 2026-11-13: nausea, flatulence, dyspepsia, toothache, antiseptic) or an RCT corroborates: pain, oral health, indigestion, bloating. Clove-gel vs benzocaine vs placebo RCT REF-3784 added. Gaps: anal fissure cream RCT, open-label blood-sugar study, chronic pruritus trial (between-group P > .05), post-spinal headache aromatherapy (not significant).',
}


def ci(note, severity, refs):
    return {'note': note, 'severity': severity, 'reference_ids': refs, 'status': 'verified'}


def post():
    """Safety-note edits fixlib has no op for."""
    path = 'plants/stachys_officinalis.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c1, c2 = d['contraindications'][0], d['contraindications'][1]
    assert c1['note'].startswith('Generally well tolerated') and c1['reference_ids'] == []
    c1['reference_ids'] = ['REF-0534']
    assert 'blood pressure' in c2['note']
    c2['note'] = 'Safety during pregnancy and breastfeeding is unknown (PeaceHealth), so avoid it then.'
    c2['reference_ids'] = ['REF-0534']; c2['status'] = 'verified'
    d['contraindications'].append(ci('In lab tests on human white blood cells, wood betony extract caused some DNA damage (comet assay) but was not mutagenic in the Ames test; what this means for people is unknown (preclinical).', 'info', ['REF-1055']))
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/solidago_virgaurea.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    d['contraindications'].append(ci('In lab tests, goldenrod extract weakened the antibacterial effect of amikacin and ciprofloxacin against urinary E. coli; tell your doctor before combining it with these antibiotics for a urinary infection (preclinical).', 'caution', ['REF-1048']))
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep audit batch 16', os.path.join(HERE, 'deep', 'd16_changes.tsv'), **BIB)
    post()
