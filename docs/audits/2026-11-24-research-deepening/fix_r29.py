"""Research-deepening batch 29 (rubus-fruticosus, rubus-idaeus, rumex-acetosa, ruscus-aculeatus, salix-alba).
Run from the repo root (worktree). Same rules as fix_r01.py. New refs REF-5636.. (reserved)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-27'
LABEL = 'research-deepening batch 29'

SPEC = [
    # butcher's broom
    ('REF-5636', '23849361', 'butchersbroomdka', 'clinical'),
    ('REF-5637', '8150360', 'cyclo3fortcolitis', 'clinical'),
    ('REF-5638', '8378650', 'cyclo3fortdiarrhoea', 'clinical'),
    # sorrel
    ('REF-5639', '33331728', 'foxglovesorrelconfusion', 'clinical'),
    # white willow
    ('REF-5640', '11345689', 'willowplatelets', 'rct'),
    ('REF-5641', '31604354', 'willowuspsafety', 'narrative-review'),
    ('REF-5642', '12773073', 'willowanaphylaxis', 'clinical'),
    ('REF-5643', '34674609', 'salixalbagenotoxicity', 'preclinical'),
]


def bib_new():
    return deep_lib.newrefs(SPEC)


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== blackberry
PLAN['rubus_fruticosus'] = []
NOTES['rubus_fruticosus'] = (
    'Searched PubMed (Rubus fruticosus / blackberry leaf or leaves / bramble / European blackberry tiab, "blackberry" in '
    'titles: 12 HT, 1 SR, 37 SAFE hits; many were about BlackBerry devices or "bramble" as a surname or descriptor), '
    'Europe PMC, ClinicalTrials.gov (27, none of the leaf) and OpenAlex. Nothing new for the leaf: a 2018 '
    'blackberry-feeding trial in overweight men (fat oxidation and insulin sensitivity; cultivated blackberry, species '
    'not stated, fruit), xylitol + blackberry chewing gum and blackberry + dill skin cream (combinations), a 2015 '
    '"blackberry" lipid study that used Morus nigra (black mulberry, a different plant), a sunitinib hand-foot reaction '
    'case caused by BlackBerry phone use, pharmacokinetic studies. Settled.')

# ================================================================== raspberry leaf
PLAN['rubus_idaeus'] = []
NOTES['rubus_idaeus'] = (
    'Searched PubMed (Rubus idaeus / raspberry leaf or leaves / red raspberry tiab, "raspberry" in titles; black '
    'raspberry, Rubus occidentalis, and raspberry ketone are not this record: 63 HT, 8 SR, 142 SAFE hits), Europe PMC, '
    'ClinicalTrials.gov (86) and OpenAlex. This record covers the leaf. Nothing new: the 2024 raspberry-fruit '
    'meta-analyses (glycaemic control, lipids and blood pressure, body weight and liver tests) concern the fruit and were '
    'mostly null; a 2025 raspberry leaf tea study measured one sugar drink in healthy adults (acute, surrogate); the 2013 '
    'systematic review of herbs in pregnancy pools the labour RCT the record already cites (not cited twice); the 2023 '
    'letter on raspberry leaf tea toxicity in pregnancy has no abstract; raspberry-fruit anaphylaxis and raspberry ketone '
    'cardiac cases are not leaf exposures. Settled.')

# ================================================================== sorrel
PLAN['rumex_acetosa'] = []
POST['rumex_acetosa'] = [
    ('cinew', {'note': 'Foraging: a woman who made a smoothie from wild plants picked in the woods mistook foxglove '
                       '(Digitalis purpurea) for common sorrel and developed foxglove poisoning, with persistent vomiting and '
                       'ECG changes; a normal digoxin blood test does not rule this out (case report).',
               'severity': 'warning', 'reference_ids': ['REF-5639']}),
]
NOTES['rumex_acetosa'] = (
    'Searched PubMed (Rumex acetosa / garden sorrel / common sorrel tiab; bare "sorrel" was not searched because it also '
    'means Jamaican sorrel, Hibiscus sabdariffa: 2 HT, 1 SR, 10 SAFE hits), Europe PMC, ClinicalTrials.gov (1) and '
    'OpenAlex. Added: 2020 Dutch case of foxglove mistaken for common sorrel as a foraging WARNING (owner flag: a formal '
    'Dangerous Lookalikes entry for foxglove is queued). Not added: 2015 acute tubulointerstitial nephritis after a large '
    'sorrel intake (letter, no abstract), periodontal proanthocyanidin extract RCT (held), veterinary and plant-genetics '
    'studies. Settled for human efficacy evidence.')

# ================================================================== butcher's broom
PLAN['ruscus_aculeatus'] = []
POST['ruscus_aculeatus'] = [
    ('cinew', {'note': 'Diabetes: a 39-year-old woman with diabetes developed diabetic ketoacidosis 5 days after starting '
                       'butcher\'s broom for mild ankle swelling; butcher\'s broom contains substances with alpha-adrenergic '
                       'stimulating effects (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5636']}),
    ('cinew', {'note': 'Bowel: long-term use of Cyclo 3 Fort, a product combining butcher\'s broom extract with hesperidin '
                       'methyl chalcone and vitamin C, has been linked to chronic watery diarrhoea and lymphocytic colitis '
                       'starting 1 to 3 months after the first dose, with weight loss and low potassium in some people; it '
                       'resolved when the product was stopped (case series).',
               'severity': 'caution', 'reference_ids': ['REF-5637', 'REF-5638']}),
]
NOTES['ruscus_aculeatus'] = (
    'Searched PubMed (Ruscus aculeatus / butcher\'s broom / ruscogenin(s) / Cyclo 3 Fort tiab, "Ruscus" in titles: 27 HT, '
    '8 SR, 39 SAFE hits), Europe PMC, ClinicalTrials.gov (7) and OpenAlex. Varicose-veins and swelling (5) were not '
    'raised: nearly all trials and the 2017 meta-analysis test Cyclo 3 Fort or Phlebodril (butcher\'s broom + hesperidin '
    'methyl chalcone + vitamin C, combinations), and the one butcher\'s-broom-only RCT here (1990 topical cream in 18 '
    'healthy volunteers) measured vein diameter only (surrogate). Added: 2013 diabetic ketoacidosis case and the Cyclo 3 '
    'Fort lymphocytic colitis / chronic diarrhoea case series as cautions (the colitis caution names the combination '
    'product). Not added: ruscogenin contact-dermatitis letters (no abstracts), diosmin + Ruscus + Melilotus + grape and '
    'other phlebotonic blends, ruscogenin from Ophiopogon or Liriope (other plants).')

# ================================================================== white willow
PLAN['salix_alba'] = []
POST['salix_alba'] = [
    ('ciadd', 'Avoid with anticoagulant/antiplatelet medicines (bleeding risk)', ['REF-5640', 'REF-5641']),
    ('ciadd', 'avoid willow bark if you are allergic to aspirin or salicylates', ['REF-5641', 'REF-5642']),
    ('cinew', {'note': 'Lab safety: white willow bark extract given to mice at up to 2,000 mg/kg daily for 7 days caused no '
                       'DNA damage or chromosome changes in blood, liver, bone marrow, heart or testis cells (animal study).',
               'severity': 'info', 'reference_ids': ['REF-5643']}),
]
NOTES['salix_alba'] = (
    'Searched PubMed (Salix alba / white willow / willow bark / Salicis cortex tiab: 36 HT, 10 SR, 66 SAFE hits), Europe '
    'PMC, ClinicalTrials.gov (6) and OpenAlex. Back-pain and pain (9) and arthritis (8) were not padded (2023 Salix spp. '
    'arthritis meta-analysis of six RCTs, 2007/2016 Cochrane back-pain reviews, STW 33-I long-term and 2008 multicentre '
    'studies). '
    'Added: 2001 randomized platelet study (willow bark with 240 mg salicin inhibited platelets far less than aspirin '
    'but more than placebo) and the 2019 USP safety review to the bleeding caution; the USP review and a 2003 '
    'anaphylaxis case (willow-bark-containing supplement in a woman with aspirin allergy) to the aspirin-allergy caution; '
    '2022 mouse genotoxicity study as an info note. Not added: 2017 fatal infant liver failure after willow bark tea + '
    'acetaminophen (no abstract), 2021 HepaRG CYP study (Salix pentandra and an unspecified reference extract), fat-burner '
    'and weight-loss supplement cases (multi-ingredient), willow pollen allergy (not related to use), topical and '
    'cosmetic blends.')


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r29_changes.tsv')
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
