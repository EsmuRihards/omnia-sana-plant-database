"""Research-deepening batch 11 (daucus-carota, dioscorea-villosa, echinacea-purpurea, elettaria-cardamomum,
eleutherococcus-senticosus). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5315.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 11'

SPEC = [
    # wild carrot
    ('REF-5315', '11496252', 'carrotallergydbpcfc', 'clinical'),
    ('REF-5316', '24102077', 'apiaceaerootdermatitis', 'clinical'),
    ('REF-5317', '23746205', 'purplecarrotquench', 'rct'),
    # wild yam
    ('REF-5318', '15513824', 'wildyamcirsafety', 'narrative-review'),
    # echinacea
    ('REF-5319', '38667040', 'echinaceaeraprima', 'meta-analysis'),
    ('REF-5320', '35559249', 'echinaforcecovidprevention', 'rct'),
    ('REF-5321', '11231867', 'echinaceagenitalherpes', 'clinical'),
    ('REF-5322', '18831749', 'echinaceaotitischildren', 'rct'),
    ('REF-5323', '16177972', 'echinilincoldimmune', 'clinical'),
    ('REF-5324', '12218779', 'echinaceajuiceimmune', 'clinical'),
    ('REF-5325', '16194048', 'echinaceajuicelymphocytes', 'clinical'),
    ('REF-5326', '42951292', 'echinaceasafetyma', 'meta-analysis'),
    ('REF-5327', '15853441', 'echinaceasafetysr', 'systematic-review'),
    ('REF-5328', '28846157', 'vigibaseherbalallergychildren', 'clinical'),
    ('REF-5329', '23701184', 'echinaceadocetaxel', 'clinical'),
    ('REF-5330', '21078942', 'echinaceadarunavir', 'clinical'),
    ('REF-5331', '22869560', 'echinaceaetravirine', 'clinical'),
    ('REF-5332', '15536458', 'botanicalcypphenotypes', 'clinical'),
    # cardamom
    ('REF-5333', '35691204', 'cardamomglycemicma', 'meta-analysis'),
    ('REF-5334', '30701554', 'cardamomt2dmrct', 'rct'),
    ('REF-5335', '29026804', 'cardamomprediabetesrct', 'rct'),
    ('REF-5336', '30263038', 'cardamomnafldrct', 'rct'),
    ('REF-5337', '38268891', 'cardamominflammationbpma', 'meta-analysis'),
    # eleuthero
    ('REF-5338', '2963645', 'eleutherococcusimmunecells', 'clinical'),
    ('REF-5339', '11798012', 'eleutherococcusathletes', 'clinical'),
    ('REF-5340', '12695337', 'siberianginsengcyp', 'clinical'),
    ('REF-5341', '26587397', 'acanthopanaxinjectionanaphylaxis', 'clinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== wild carrot
PLAN['daucus_carota'] = [
    ('nulladd', 'high-cholesterol', ['REF-5317']),
    ('note', 'high-cholesterol', 'Insoluble fibre from carrots limited the rise in blood lipids after a fatty meal in mice '
     '(preclinical); in people, dried purple carrot did not lower cholesterol in a small placebo-controlled trial'),
]
POST['daucus_carota'] = [
    ('cinew', {'note': 'Allergy: carrot (the cultivated form of the same species) can cause food allergy, mostly in people '
                       'allergic to birch pollen; in a placebo-controlled food-challenge study, 20 of 26 people with suspected '
                       'carrot allergy reacted, most to the birch-related allergen Dau c 1. A delayed allergic skin reaction to '
                       'carrot and other carrot-family roots has also been reported (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5315', 'REF-5316']}),
]
NOTES['daucus_carota'] = (
    'Searched PubMed (Daucus carota / wild carrot / Queen Anne\'s lace / carrot seed tiab: 18 HT, 2 SR, 92 SAFE hits, mostly '
    'crop science), Europe PMC, ClinicalTrials.gov (34, all dietary-carrot studies) and OpenAlex. Added: carrot-allergy '
    'caution (2001 double-blind placebo-controlled food challenge, Dau c 1; 2014 systemic contact dermatitis case); 2013 '
    'QUENCH placebo RCT of dried purple carrot (no change in cholesterol, BP or CRP) as no-effect for high-cholesterol. Not '
    'added: carrot seed + clomiphene + lifestyle RCT in male infertility (2025; carrot effect not isolated, and the seed is a '
    'folk contraceptive, see the owner note of 2026-11-12), Jazar (Vitex + fennel + carrot seed) and wild-carrot halva '
    '(multi-herb), phytophotodermatitis letter 2011 and 2013 threshold-dose letter (no abstract), gastric-cancer intake MA '
    '(dietary, risk-only), Dau c 1 lab characterisation.')

# ================================================================== wild yam
PLAN['dioscorea_villosa'] = []
POST['dioscorea_villosa'] = [
    ('cinew', {'note': 'Skin products: a 2004 Cosmetic Ingredient Review safety assessment concluded that wild yam root extract '
                       'is safe as used in cosmetics; the tested extract showed no oestrogen-like activity in young rats, and '
                       'undiluted extract irritated rabbit skin while a 10% dilution did not.',
               'severity': 'info', 'reference_ids': ['REF-5318']}),
]
NOTES['dioscorea_villosa'] = (
    'Searched PubMed (Dioscorea villosa / wild yam / Mexican wild yam tiab, diosgenin ti: 15 HT, 3 SR, 113 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (3) and OpenAlex. Still no human trial of oral wild yam. Added: 2004 CIR cosmetic safety '
    'assessment as an info note. Not added: diosgenin-rich yam extract cognition RCT 2017 (Japanese "yam", species not '
    'stated), Dioscorea + Vitex + Turnera phyto-progestin pilot and Dioscorea comp. ovules (combinations), diosgenin + vitamin '
    'D + lactalbumin in PCOS (combination), the 2010 OTC hot-flash review (no wild yam pair to attach; consistent with the '
    'null cream RCT REF-0614), diosgenin lab and animal work (other Dioscorea species or isolated compound).')

# ================================================================== echinacea
PLAN['echinacea_purpurea'] = [
    ('add', 'infection', ['REF-5319', 'REF-5320']),
    ('nulladd', 'infection', ['REF-5321', 'REF-5322']),
    ('note', 'infection', 'Echinacea extracts reduced respiratory infections, their complications and antibiotic use in a 2024 '
     'meta-analysis of clinical trials (strongest for fresh E. purpurea alcoholic extracts); E. purpurea reduced respiratory '
     'infections and antibiotic use in children in a randomized trial, and an open randomized trial in adults found fewer '
     'SARS-CoV-2 infections; it did not reduce recurrences of genital herpes or prevent ear infections in otitis-prone '
     'children (placebo-controlled trials); supportive use for respiratory and urinary infections (WHO monograph)'),
    ('add', 'immune-support', ['REF-5323']),
    ('nulladd', 'immune-support', ['REF-5324', 'REF-5325']),
    ('note', 'immune-support', 'Improved immune markers vs placebo in randomized trials (healthy adults; athletes) and raised '
     'white-cell and natural-killer-cell counts during a cold (placebo-controlled study); the pressed juice of the herb did '
     'not stimulate immune cells in two placebo-controlled crossover trials in healthy men; traditional immunostimulant (WHO '
     'monograph)'),
]
POST['echinacea_purpurea'] = [
    ('ciadd', 'Generally considered safe, but caution', ['REF-5326']),
    ('cinew', {'note': 'Allergy: echinacea, a daisy-family plant, can rarely cause allergic reactions, sometimes severe; people '
                       'with allergies or asthma should take care. E. purpurea was among the herbal medicines most often linked '
                       'to allergy-like reactions in children in the WHO safety database.',
               'severity': 'caution', 'reference_ids': ['REF-5327', 'REF-5328']}),
    ('cinew', {'note': 'Pregnancy and breastfeeding: there are too few data on echinacea in pregnancy and breastfeeding to '
                       'judge its safety, and a systematic review of its safety advised against use in these periods.',
               'severity': 'caution', 'reference_ids': ['REF-5327']}),
    ('cinew', {'note': 'Medicines: in clinical studies, E. purpurea did not meaningfully change blood levels of the cancer drug '
                       'docetaxel or the HIV drugs darunavir-ritonavir and etravirine, and had only minor, non-significant '
                       'effects on the liver enzymes CYP1A2, CYP2D6, CYP2E1 and CYP3A4 in healthy volunteers.',
               'severity': 'info', 'reference_ids': ['REF-5329', 'REF-5330', 'REF-5331', 'REF-5332']}),
]
NOTES['echinacea_purpurea'] = (
    'Searched PubMed (Echinacea purpurea / purple coneflower tiab, echinacea ti: 140 HT, 30 SR, 206 SAFE hits; SR/MA, '
    'safety and E. purpurea trials read in depth), Europe PMC, ClinicalTrials.gov (42) and OpenAlex. Species rule: only '
    'E. purpurea products, or reviews pooling Echinacea products with E. purpurea named as the leading preparation. Added: '
    'ERA-PRIMA MA 2024 and the 2022 Echinaforce open RCT to infection, with E. purpurea placebo trials in genital herpes '
    '(2001) and otitis-prone children (2008) as no-effect; Echinilin cold study 2005 to immune-support with the two pressed-'
    'juice crossover trials (2002, 2005) as no-effect; 2026 safety MA (48 trials, adverse events no higher than control) to '
    'the safety note; new allergy and pregnancy cautions (2005 safety SR, 2017 VigiBase children); human interaction studies '
    '(docetaxel, darunavir-ritonavir, etravirine, CYP phenotyping) as an info note. Not added: the cold pair (already 9 with '
    'five no-effect trials) was not padded either way - positive (Schulten 2001, Brinkeborn 1999, air travellers 2012, 2019 '
    'URTI MA) and null (Barrett 2002, Grimm 1999, Turner 2000) trials logged here only; 2015 recurrent-RTI MA (superseded by '
    'ERA-PRIMA); anxiety trials (EP107 is E. angustifolia root); oral lichen planus RCT 2022, tonsillitis add-on study 2020 '
    'and COVID syrup RCT 2024 (species not stated); warfarin and digoxin interaction studies (species not stated in the '
    'abstract); athletic VO2max/EPO trials and MA (no vocab condition); combinations (Kan Jang, Imupret, echinacea + zinc / '
    'propolis / ginger / sage); homeopathic products.')

# ================================================================== cardamom
PLAN['elettaria_cardamomum'] = [
    ('newpair', 'blood-sugar', ['REF-5333', 'REF-5334'],
     'Green cardamom (3 g a day) lowered HbA1c and insulin resistance, though not fasting blood sugar, in a 2022 meta-analysis '
     'of randomized trials and in a placebo-controlled trial in type 2 diabetes; a trial in pre-diabetic women found no '
     'difference from placebo'),
    ('nulladd', 'blood-sugar', ['REF-5335']),
    ('newpair', 'liver-support', ['REF-5336'],
     'Green cardamom capsules (3 g a day) reduced the degree of fatty liver, the liver enzyme ALT and inflammatory markers vs '
     'placebo in overweight people with non-alcoholic fatty liver disease (randomized trial)'),
    ('add', 'high-blood-pressure', ['REF-5337']),
    ('note', 'high-blood-pressure', 'Green cardamom lowered blood pressure in meta-analyses of small randomized trials, in '
     'metabolic syndrome and in adults generally, though the falls were very small (under 1 mmHg in the 2024 analysis)'),
]
NOTES['elettaria_cardamomum'] = (
    'Searched PubMed (Elettaria cardamomum / cardamom tiab: 42 HT, 19 SR, 77 SAFE hits), Europe PMC, ClinicalTrials.gov (13) '
    'and OpenAlex; black cardamom (Amomum subulatum) hits excluded as another species. Added: NEW blood-sugar pair (2022 '
    'glycaemic MA: HbA1c and HOMA-IR fell, fasting glucose did not; 2019 T2DM placebo RCT) with the 2017 pre-diabetes RCT as '
    'no-effect; NEW liver-support pair (2018 NAFLD placebo RCT, IRCT2015121317254N4; its 2019 companion paper 30871514 '
    'reports the same trial and was not added as a second source); 2024 inflammation/BP MA to high-blood-pressure with its '
    'tiny effect size stated. Not added: inflammation (already 8), peppermint vs cardamom ice cubes for post-operative '
    'nausea 2025 (abstract does not state a significant difference from placebo), PCOS gene-expression trials (surrogates), '
    'Arabic coffee, compound honey syrup and other combinations, two trial protocols, cardamom allergy protein study 2024 '
    '(no abstract), hematuria letter 2011 and contact dermatitis case 1975 (no abstract).')

# ================================================================== eleuthero
PLAN['eleutherococcus_senticosus'] = [
    ('add', 'immune-support', ['REF-5338']),
    ('nulladd', 'immune-support', ['REF-5339']),
    ('note', 'immune-support', 'Immunostimulant effects reported (reviews); an ethanolic root extract raised T-cell and '
     'natural-killer-cell counts vs placebo in healthy volunteers (1987 double-blind study), but an extract did not change '
     'immune cells in endurance athletes (2001 placebo-controlled trial)'),
    ('nulladd', 'stress', ['REF-5339']),
    ('note', 'stress', 'Traditional adaptogen to improve resistance to stress (reviews); a randomized trial adding it to '
     'stress-management training found no benefit, and in endurance athletes it raised rather than lowered hormonal markers '
     'of stress (placebo-controlled trial)'),
]
POST['eleutherococcus_senticosus'] = [
    ('cinew', {'note': 'Medicines: a standardised extract (485 mg twice daily for 14 days) did not change CYP2D6 or CYP3A4 '
                       'activity in healthy volunteers, so interactions with drugs cleared by these liver enzymes are unlikely '
                       '(clinical study).',
               'severity': 'info', 'reference_ids': ['REF-5340']}),
    ('cinew', {'note': 'Injections: eleuthero (Acanthopanax) injections used in Chinese hospitals have caused anaphylactic '
                       'shock, sometimes fatal; in a review of 57 Chinese cases almost all followed an infusion (literature '
                       'analysis).',
               'severity': 'caution', 'reference_ids': ['REF-5341']}),
]
NOTES['eleutherococcus_senticosus'] = (
    'Searched PubMed (Eleutherococcus senticosus / Acanthopanax senticosus / Siberian ginseng / eleuthero tiab; '
    'eleutherococcus, acanthopanax ti: 72 HT, 15 SR, 135 SAFE hits), Europe PMC, ClinicalTrials.gov (25) and OpenAlex. '
    'Added: 1987 double-blind flow-cytometry study to immune-support, with the 2001 endurance-athlete placebo trial as '
    'no-effect for immune-support and stress (its testosterone-to-cortisol ratio fell); 2003 CYP2D6/CYP3A4 phenotyping study '
    'and a 2015 analysis of injection anaphylaxis as notes. Not added: fruit extract BP RCT 2020 (the record cautions about '
    'uncontrolled high blood pressure, inv. 12d), postmenopausal lipid RCT 2008 (calcium control; abstract reports '
    'within-group changes only), elderly quality-of-life RCT 2004 and endurance RCT 2010 (no vocab condition), hangover RCT '
    '2015, bone-density RCT 2009, cancer-fatigue feasibility study 2024 (single arm), Siberian ginseng vs fluoxetine add-on in '
    'bipolar adolescents (active comparator), Acanthopanax injections for stroke and Aidi / Shugan Jieyu / ADAPT-232 / Kan '
    'Jang / ImmunoGuard and other combinations, subarachnoid haemorrhage case (red clover + dong quai + Siberian ginseng '
    'product), other Acanthopanax and Eleutherococcus species.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r11_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
