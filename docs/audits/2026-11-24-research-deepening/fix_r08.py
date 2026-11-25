"""Research-deepening batch 8 (centella-asiatica, chamerion-angustifolium, chelidonium-majus, cinnamomum-cassia,
cinnamomum-verum). Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5250.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-25'
LABEL = 'research-deepening batch 8'

SPEC = [
    # gotu kola
    ('REF-5250', '20677602', 'centellagad', 'clinical'),
    ('REF-5251', '31080345', 'centellatriterpenesneuropathy', 'rct'),
    ('REF-5252', '40253389', 'eca233tmdpain', 'rct'),
    ('REF-5253', '11666125', 'ttfcavenousedema', 'rct'),
    ('REF-5254', '11666121', 'ttfcaflightedema', 'rct'),
    ('REF-5255', '36420467', 'gotukolaexercisemci', 'rct'),
    # greater celandine
    ('REF-5256', '21893153', 'celandinecausality22', 'clinical'),
    ('REF-5257', '22189691', 'celandinecausalityeurope', 'clinical'),
    ('REF-5258', '28379595', 'celandinehepatotoxicityreview', 'narrative-review'),
    ('REF-5259', '38682076', 'celandineushepatitis', 'clinical'),
    ('REF-5260', '42359199', 'celandinehepatitiscase', 'clinical'),
    ('REF-5261', '2291149', 'celandinehaemolyticanaemia', 'clinical'),
    # cassia (unnamed "cinnamon" trials go to cassia, inv. 10)
    ('REF-5262', '30396627', 'cinnamondysmenorrhoea', 'rct'),
    ('REF-5263', '26023350', 'cinnamonmenstrualbleeding', 'rct'),
    ('REF-5264', '25074885', 'cinnamonepisiotomy', 'rct'),
    ('REF-5265', '31617744', 'cinnamonbloodpressuredose', 'meta-analysis'),
    ('REF-5266', '32220351', 'cinnamonbloodpressure', 'meta-analysis'),
    ('REF-5267', '39299867', 'cinnamonbpumbrella', 'systematic-review'),
    ('REF-5268', '26839630', 'cinnamonaerosolanaphylaxis', 'clinical'),
    # true cinnamon
    ('REF-5269', '31780001', 'cinnamonbarknasalspray', 'rct'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== gotu kola
PLAN['centella_asiatica'] = [
    ('add', 'anxiety', ['REF-5250']),
    ('note', 'anxiety', 'Gotu kola blunted the acoustic startle response (a measure of anxiety) vs placebo in healthy '
     'volunteers, and a hydro-ethanolic extract reduced anxiety, stress and related low mood in a clinical study in '
     'generalized anxiety disorder; anti-anxiety activity of its triterpenes in animal studies (review)'),
    ('add', 'swelling', ['REF-5253', 'REF-5254']),
    ('note', 'swelling', 'Improves venous tone and microcirculation - supports chronic venous insufficiency / varicose veins and '
     'reduces leg swelling; in randomized trials, its total triterpenic fraction reduced ankle swelling in venous hypertension '
     'and swelling during long flights'),
    ('nulladd', 'cognitive-function', ['REF-5255']),
    ('note', 'cognitive-function', 'Improved cognition and mood in healthy older volunteers and after stroke in small randomized '
     'trials; a meta-analysis found no significant effect on any cognitive domain, and added to exercise it gave no extra '
     'cognitive benefit in mild cognitive impairment'),
    ('newpair', 'pain', ['REF-5251', 'REF-5252'],
     'In placebo-controlled randomized trials, Centella triterpenes reduced the severity of diabetic neuropathy symptoms, and a '
     'standardized extract (ECa 233) gave fast, short-term relief of jaw (temporomandibular) pain'),
]
NOTES['centella_asiatica'] = (
    'Searched PubMed (Centella asiatica / gotu kola / Hydrocotyle asiatica tiab; centella, asiaticoside, madecassoside ti), '
    'Europe PMC, ClinicalTrials.gov (61) and OpenAlex. Added: GAD clinical study (Nepal 2010) to anxiety; two TTFCA RCTs '
    '(venous-hypertension oedema; flight oedema) to swelling; Gotu kola + exercise vs exercise RCT (no extra cognitive '
    'effect) as no-effect for cognitive-function; NEW pain pair (CAST triterpenes diabetic-neuropathy placebo RCT; ECa 233 '
    'TMD placebo pilot RCT). Dead end: 2025 Thai placebo RCT in type 2 diabetes found no glycaemic or lipid effect (no '
    'blood-sugar pair exists). Considered, not added: cosmetics and creams combining Centella with panthenol, ceramides, '
    'mandelic acid, aloe or other actives; Centella vs flavonoids for haemorrhoids and anal fissure (active comparators); '
    'scar-cream RCT (pigmentation only); skin-ageing, macular-pigment and elderly strength trials (no vocab condition); '
    'contact-dermatitis case (no abstract); Medhya Rasayana and other formulas.')

# ================================================================== fireweed
PLAN['chamerion_angustifolium'] = []
NOTES['chamerion_angustifolium'] = (
    'Searched PubMed (Chamerion / Epilobium angustifolium / fireweed / rosebay willowherb / Ivan chai tiab; oenothein B ti), '
    'Europe PMC, ClinicalTrials.gov (0) and OpenAlex. No usable human study: the prostate and nocturia products combine '
    'Epilobium with other herbs, and the one single-extract nocturia food study is in a SCIRP journal (Beall\'s list, not '
    'used); the rest is lab work, oenothein B from other plants, and fire ecology. Settled.')

# ================================================================== greater celandine
PLAN['chelidonium_majus'] = []
POST['chelidonium_majus'] = [
    ('ciadd', 'SERIOUS: oral greater celandine', ['REF-5256', 'REF-5257', 'REF-5258', 'REF-5259', 'REF-5260']),
    ('cinew', {'note': 'Blood: a patient developed severe haemolytic anaemia, with kidney failure and low platelets, after '
                       'taking a greater celandine extract by mouth; it resolved with hospital treatment (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5261']}),
]
NOTES['chelidonium_majus'] = (
    'Searched PubMed (Chelidonium majus / greater celandine tiab; celandine, chelidonium ti), Europe PMC, ClinicalTrials.gov '
    '(1) and OpenAlex. No efficacy trial of the plant itself: Ukrain (NSC-631570) is a semisynthetic thiophosphoric alkaloid '
    'derivative, not the herb, so its cancer trials and the 2005 Ukrain SR are not used; chelidonium + turmeric for '
    'abdominal pain is a combination. SAFETY: added to the serious liver warning the CIOMS causality reanalyses of 22 German '
    'spontaneous reports (2011) and 21 European published cases (2012), a 2017 literature review, the first US case (2024) '
    'and a 2026 case; new caution for a haemolytic anaemia case (1990). Not added: contact dermatitis and balanoposthitis '
    'letters (no abstract), COVID-19 case series, lesser celandine case (a different plant).')

# ================================================================== cassia cinnamon
PLAN['cinnamomum_cassia'] = [
    ('newpair', 'menstrual-cramps', ['REF-5262', 'REF-5263'],
     'Cinnamon capsules reduced period pain more than placebo in two double-blind randomized trials, one of which also found '
     'less nausea and vomiting (cinnamon species not stated)'),
    ('newpair', 'wounds', ['REF-5264'],
     'A cinnamon ointment reduced perineal pain and improved healing of episiotomy wounds more than placebo in a double-blind '
     'randomized trial (cinnamon species not stated)'),
    ('newpair', 'high-blood-pressure', ['REF-5265', 'REF-5266', 'REF-5267'],
     'Cinnamon supplements modestly lowered systolic and diastolic blood pressure in meta-analyses of randomized trials, '
     'confirmed by a 2024 umbrella review (cinnamon species often not stated)'),
]
POST['cinnamomum_cassia'] = [
    ('cinew', {'note': 'Allergy: cinnamon (cinnamaldehyde) can cause immediate allergic reactions; in reported cases, people '
                       'first sensitised by inhaling heated, cinnamon-flavoured fog-machine or shisha vapour later had severe '
                       'reactions, including anaphylaxis, to spiced food.',
               'severity': 'caution', 'reference_ids': ['REF-5268']}),
]
NOTES['cinnamomum_cassia'] = (
    'Searched PubMed (Cinnamomum cassia / C. aromaticum / cassia / Chinese cinnamon tiab, cinnamon ti), Europe PMC, '
    'ClinicalTrials.gov (112) and OpenAlex. Trials and reviews that say only "cinnamon" are assigned here (inv. 10). The '
    'metabolic pairs are already at 10 and were not padded. NEW pairs: menstrual-cramps (Jahangirifar 2018 and Jaafarpour '
    '2015 placebo RCTs), wounds (Mohammadi 2014 episiotomy placebo RCT, ointment), high-blood-pressure (two 2020 MAs and a '
    '2024 umbrella review). New allergy caution (aerosol-primed cinnamaldehyde anaphylaxis cases, 2016). NOT ADDED: '
    'liver-support (two liver-enzyme MAs) because the record warns that cassia coumarin can damage the liver (inv. 12d); '
    'heavy-bleeding from the dysmenorrhoea trial (women with period pain, not heavy bleeding: near-miss, inv. 12c); '
    'cinnamon vs ibuprofen or chlorhexidine (active comparators); PCOS and fertility-hormone trials (surrogates, mixed); '
    'combinations with berberine, sumac, chromium, probiotics, marjoram and other spices; the 2021 safety umbrella review '
    '(no claim it would change).')

# ================================================================== true cinnamon
PLAN['cinnamomum_verum'] = [
    ('newpair', 'allergy', ['REF-5269'],
     'A Ceylon cinnamon bark extract nasal spray reduced seasonal hay-fever symptoms and improved quality of life more than '
     'placebo over 7 days in a double-blind randomized trial'),
]
NOTES['cinnamomum_verum'] = (
    'Searched PubMed (Cinnamomum verum / C. zeylanicum / Ceylon cinnamon / true cinnamon tiab), Europe PMC, '
    'ClinicalTrials.gov (100) and OpenAlex. NEW allergy pair: 2019 placebo RCT of a C. zeylanicum bark extract nasal spray '
    '(IND02) in seasonal allergic rhinitis. Not added: the 2025 Sri Lankan T2DM trial report (SLCTR/2017/010; same trial as '
    'REF-2413, and its abstract reports within-group changes) and its 2017 protocol; C. zeylanicum essential oil vs nystatin '
    'for oral candidiasis (active comparator only); trials naming only "cinnamon" (assigned to cassia, inv. 10).')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r08_changes.tsv')
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
