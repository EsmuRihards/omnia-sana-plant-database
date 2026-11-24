"""Research-deepening batch 4 (arctium-minus, arctostaphylos-uva-ursi, arnica-montana, artemisia-absinthium,
artemisia-vulgaris) plus the batch-3 Europe PMC follow-up (andrographis safety). Run from the repo root (worktree).
Same rules as fix_r01.py. New refs REF-5169.. (reserved block)."""
import copy, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402
from fix_r01 import _initials, _ascii  # noqa: E402
from fix_r02 import pubmed_urls  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 4'

# The CIR report has no personal authors on PubMed; give it its corporate author (in memory only, cache untouched).
deep_lib.CACHE['11558636'] = dict(deep_lib.CACHE['11558636'], authors=['Cosmetic Ingredient Review Expert Panel'])

SPEC = [
    ('REF-5169', '30174700', 'andrographisplatelets', 'clinical'),
    ('REF-5170', '10925397', 'andrographolidephase1', 'clinical'),
    ('REF-5171', '15183807', 'uvaursimaculopathy', 'clinical'),
    ('REF-5172', '18066112', 'uvaursicyp', 'preclinical'),
    ('REF-5173', '26910697', 'arnicarhinoplasty', 'rct'),
    ('REF-5174', '37913818', 'arnicathirdmolar', 'rct'),
    ('REF-5175', '12539881', 'arnicakneeoa', 'clinical'),
    ('REF-5176', '11722485', 'arnicapatchtest', 'clinical'),
    ('REF-5177', '18154553', 'compositaeremedies', 'clinical'),
    ('REF-5178', '11558636', 'arnicasafety', 'narrative-review'),
    ('REF-5179', '43042214', 'wormwoodhepatitis', 'clinical'),
    ('REF-5180', '25823193', 'wormwoodinfant', 'clinical'),
    ('REF-5181', '23770559', 'wormwoodwarfarin', 'clinical'),
    ('REF-5182', '30044501', 'mugwortthujone', 'clinical'),
]
DOI_SPEC = [
    ('REF-5183', '10.21037/ajo-2025-1-97', 'arnicaseptorhinoplasty', 'rct', {'journal': 'Australian Journal of Otolaryngology'}),
    ('REF-5184', '10.22038/ijogi.2022.21058', 'wormwoodgeldepression', 'rct',
     {'journal': 'Iranian Journal of Obstetrics, Gynecology and Infertility'}),
    ('REF-5185', '10.1590/s0102-695x2007000100014', 'arctiumminusglicemia', 'preclinical', {}),
]
WEB = {'mskcc2022arnica': ('REF-5186', [
    ('author', 'Memorial Sloan Kettering Cancer Center'), ('title', 'Arnica (About Herbs)'), ('year', '2022'),
    ('url', 'https://www.mskcc.org/cancer-care/integrative-medicine/herbs/arnica'), ('note', 'REF-5186'), ('study_type', 'traditional'),
    ('summary', 'MSKCC About Herbs, last updated 19 October 2022, read 2026-11-24. Herb-drug interactions (clinical relevance not '
                'known): helenalin inhibits platelet aggregation in vitro; arnica may potentiate warfarin and other anticoagulants. '
                'Adverse reactions: oral raw herb causes gastrointestinal distress, internal bleeding, fast heartbeat, breathing '
                'difficulty and coma; a 9-day-old breastfed infant developed haemolytic anaemia 48 hours after the mother began '
                'drinking arnica flower tea; topical use can cause contact dermatitis. Contraindications: pregnancy and '
                'breastfeeding; people allergic to sunflowers, marigolds or ragweed are likely to be allergic to arnica.')])}


def bib_new():
    new = deep_lib.newrefs(SPEC)
    for rid, doi, slug, st, over in DOI_SPEC:
        _, (r, fields) = rd_doi.newref_doi(doi, rid, 'x', st)
        f = dict(fields)
        au = [_initials(a.strip()) for a in rd_doi.fetch(doi)['authors']]
        f['author'] = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
        f.update(over)
        order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'pmid', 'note', 'study_type', 'abstract']
        new[_ascii(f['author'].split(',')[0]) + f['year'] + slug] = (rid, [(k, f[k]) for k in order if k in f])
    new.update(WEB)
    return new


PLAN, POST, NOTES = {}, {}, {}

# ================================================================== andrographis (batch-3 Europe PMC follow-up)
PLAN['andrographis_paniculata'] = []
AP_OLD = ('May lower blood pressure and blood sugar and may interact with anticoagulant/antiplatelet, antihypertensive and '
          'immunosuppressant medicines; allergic reactions can occur.')
AP_NEW = ('May lower blood pressure and blood sugar and may interact with anticoagulant/antiplatelet, antihypertensive and '
          'immunosuppressant medicines; allergic reactions can occur, including an anaphylactic reaction in one person in a '
          'dose-escalating trial of purified andrographolide, which was stopped early because of side effects. In 10 healthy '
          'volunteers, one day of andrographis did not significantly change platelet function.')
NOTES['andrographis_paniculata'] = (
    'Batch-3 Europe PMC sweep (read after the batch-3 commit): added the platelet study in 10 healthy Thai volunteers (no '
    'significant change in platelet aggregation, COX-1, TXB2 or P-selectin) and the Calabrese 2000 phase I andrographolide '
    'trial (stopped at 6 weeks for adverse events including one anaphylactic reaction) to the BP/sugar/interaction caution, '
    'whose text now says so. Not added: oesophageal cancer phase II (compares completers with non-completers, so survival '
    'bias), malaria open trial, AS201-01 4-day safety RCT (no new claim), prediabetes GLP-1 preprint (not peer reviewed), '
    'Kan Jang and other combinations.')

# ================================================================== lesser burdock
PLAN['arctium_minus'] = [('refadd', ['REF-5185'])]
AM_OLD = 'May lower blood sugar (caution with antidiabetic medicines) and add to diuretics; avoid medicinal doses in pregnancy.'
AM_SUGAR = ('May lower blood sugar: root and leaf extracts lowered blood glucose in diabetic rats, the root extract about as '
            'much as the drug glibenclamide, so take care if using diabetes medicines (animal evidence only).')
AM_REST = 'May add to diuretics; avoid medicinal doses in pregnancy.'
NOTES['arctium_minus'] = (
    'Searched PubMed ("Arctium minus" OR "lesser burdock" tiab: 0 HT, 0 SR, 3 SAFE hits), Europe PMC, ClinicalTrials.gov (4, '
    'none on this species) and OpenAlex (49 no-PMID works, mostly ecology). No human study of A. minus exists. Added: Cavalli '
    '2007 Rev Bras Farmacogn (alloxan-diabetic rats; root extract -34.6% glycaemia, leaf -22.9%, glibenclamide -34.5%) as the '
    'source for a new antidiabetic action and for the blood-sugar part of the caution, which is split off and verified; the '
    'diuretic and pregnancy parts stay needs-review (no A. minus source; the EU monograph REF-3088 is for A. lappa). No '
    'blood-sugar pair (animal evidence only; owner rule 2026-11-16). Considered, not added: Turkish herbal genotoxicity screen '
    '1996 (A. minus extract increased comet-assay DNA breaks in lymphocytes in vitro, Ames negative; authors say the hazard '
    'for people cannot be judged), Amish burn-dressing qualitative study (caregiver experiences, not an outcome study), silver '
    'nanoparticle and in vitro antidiabetic papers.')

# ================================================================== bearberry
PLAN['arctostaphylos_uva_ursi'] = []
POST['arctostaphylos_uva_ursi'] = [
    ('cinew', {'note': 'Long-term use: a woman who took uva ursi for 3 years developed bull\'s-eye maculopathy (damage to the '
                       'centre of the retina) in both eyes; the report\'s authors link it to the herb, which blocks melanin '
                       'production (single case report).',
               'severity': 'caution', 'reference_ids': ['REF-5171']}),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'In laboratory tests, water extracts of five uva-ursi products strongly inhibited several '
                             'drug-metabolising enzymes, including CYP3A4, 3A5, 3A7 and 2C19, and affected the P-glycoprotein drug pump; whether this '
                             'matters in people has not been studied.',
                'reference_ids': ['REF-5172']}),
]
NOTES['arctostaphylos_uva_ursi'] = (
    'Searched PubMed (Arctostaphylos uva-ursi / uva-ursi / uva ursi / bearberry / Uvae ursi folium tiab), Europe PMC, '
    'ClinicalTrials.gov and OpenAlex. No new efficacy trial: REGATTA and ATAFUTI results are held (REF-0700, REF-0701, both '
    'no-effect); their 2017-2018 protocols are not cited; the BRUMI bearberry vs placebo cystitis trial (protocol 2022, '
    'NCT05055544) has no published results (status unknown) - check again later. Added: bull\'s-eye maculopathy case after '
    '3 years of use (new caution); in vitro CYP3A4/3A5/3A7/2C19 and P-gp inhibition (new DRAFT interaction, insufficient, needs '
    'owner sign-off). Considered, not added: UGT1A1 inhibition in vitro that did not carry over to rats (no human claim), '
    'arbutin urinary-excretion PK studies (no new claim), "herbal detox" hyponatraemia case (multi-herb tea plus over a '
    'gallon of fluid daily), Ciurol N and D-mannose combinations, Dwyer 2020 AJHNM systematic review of harm (no abstract '
    'retrievable), LiverTox and LactMed Uva Ursi pages (NCBI bot check blocked the fetch), MSKCC (no uva ursi page, 404).')

# ================================================================== arnica
SWELLING = ('Arnica cream reduced swelling around the eyes after nose surgery in two small randomized trials compared with no '
            'treatment; after wisdom-tooth surgery, topical arnica did not reduce swelling')
PLAN['arnica_montana'] = [
    ('add', 'bruising', ['REF-5173', 'REF-5183']),
    ('note', 'bruising', 'Traditional topical remedy for bruises (EU herbal monograph, summarised in a review); a 20% arnica '
     'ointment sped bruise healing in one randomized trial and arnica cream reduced bruising after nose surgery in two small '
     'randomized trials with untreated comparison, but arnica gel, a 10% ointment and a systematic review found no clear benefit'),
    ('add', 'arthritis', ['REF-5175']),
    ('note', 'arthritis', 'An arnica gel was as effective as ibuprofen gel for hand osteoarthritis in a randomized trial, and '
     'knee osteoarthritis scores improved with an arnica gel in an open trial without a comparison group; applied for rheumatic '
     'muscle and joint complaints (EU herbal monograph)'),
    ('newpair', 'swelling', ['REF-5173', 'REF-5183'], SWELLING),
    ('nulladd', 'swelling', ['REF-5174']),
    ('newpair', 'pain', ['REF-5174'],
     'Added to standard pain relief, topical arnica reduced pain for the first 5 days after wisdom-tooth surgery in a randomized '
     'trial without placebo'),
    ('refadd', ['REF-5186']),
]
POST['arnica_montana'] = [
    ('ciadd', 'EXTERNAL USE ONLY on unbroken skin', ['REF-5178', 'REF-5186']),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'insufficient',
                'mechanism': 'Arnica\'s helenalin inhibits platelets in laboratory tests, and Memorial Sloan Kettering notes that '
                             'arnica may add to the effect of warfarin and other blood thinners; the clinical relevance is not '
                             'known, and arnica is meant for use on unbroken skin only.',
                'reference_ids': ['REF-5186']}),
]
AR_ALLERGY_OLD = ('As a member of the daisy family (Asteraceae) it can cause allergic contact dermatitis; prolonged topical use '
                  'can also irritate the skin.')
AR_ALLERGY_NEW = ('As a member of the daisy family (Asteraceae) it can cause allergic contact dermatitis; prolonged topical use '
                  'can also irritate the skin. About 1 in 100 people in a clinic series of 443 patch tests reacted to arnica, '
                  'and 5 of 6 people already sensitised to arnica reacted to arnica-based products; people allergic to '
                  'sunflowers, marigolds or ragweed are likely to react.')
AR_PREG_OLD = 'Avoid medicinal use during pregnancy and breastfeeding.'
AR_PREG_NEW = ('Avoid medicinal use during pregnancy and breastfeeding. A 9-day-old breastfed baby developed haemolytic anaemia '
               '(breakdown of red blood cells) 48 hours after the mother began drinking arnica flower tea (case cited by '
               'Memorial Sloan Kettering).')
NOTES['arnica_montana'] = (
    'Searched PubMed (Arnica montana tiab, arnica ti), Europe PMC, ClinicalTrials.gov (33) and OpenAlex. Most arnica trials '
    'are homeopathic dilutions (12CH, D4, D12, D30, Boiron/Alpine pellets, SinEcch) and are not used (owner rule); topical '
    'creams, gels and ointments count as plant evidence (inv. 11 mother-tincture rule). Added: Simsek 2016 rhinoplasty RCT '
    '(arnica cream vs no treatment, less ecchymosis and faster oedema regression) and Grigg 2026 split-face septorhinoplasty '
    'RCT (Aust J Otolaryngol, found via OpenAlex) to bruising; both make a NEW swelling pair, with Akay 2024 (third-molar RCT, '
    'arnica did not reduce oedema) recorded as no-effect; Akay 2024 also makes a NEW pain pair (lower VAS to day 5 vs '
    'standard therapy alone; open, no placebo). Knuesel 2002 open knee-OA gel trial to arthritis. Safety: Reider 2001 patch '
    'tests (1.13% of 443) and Paulsen 2008 (5/6 arnica-sensitive positive to arnica products) to the Asteraceae allergy note; '
    'CIR 2001 safety assessment (ingestion: gastroenteritis, fast heart rate, muscular weakness, death) and MSKCC About Herbs '
    '(REF-5186, read 2026-11-24) to the oral-toxicity note; MSKCC neonatal haemolysis case to the pregnancy/breastfeeding '
    'caution; new DRAFT interaction with anticoagulants/antiplatelets (insufficient, needs owner sign-off). NOT ADDED - '
    'muscle-soreness: Pumpa 2014 RCT (n=20, less pain 72 h after downhill running) conflicts with Adkison 2010 RCT (n=53, '
    'arnica cream INCREASED leg pain at 24 h); left out as conflicting, flagged for owner. Infection: Robledo 2025 phase Ib/II '
    'arnica tincture healed cutaneous leishmaniasis in 12/12 completers, but it is applied to ulcers and the record forbids '
    'broken skin (inv. 12d). Also not added: 2026 Cureus SR and 2026 facial-surgery SR (pool homeopathic and topical forms), '
    '2025 eyelid-surgery SR (same mix; no benefit), arnica + hydroxyethyl salicylate spray (arnica-alone arm not tested '
    'against placebo in the abstract), carpal-tunnel trial (homeopathic tablets plus ointment), umbilical Arnica-Echinacea '
    'powder, menthol mud pack and other combinations, LiverTox and LactMed arnica pages (NCBI bot check blocked the fetch).')

# ================================================================== wormwood
PLAN['artemisia_absinthium'] = [
    ('newpair', 'depression', ['REF-5184'],
     'A wormwood vaginal gel reduced depression scores more than placebo in a triple-blind randomized trial in women with '
     'sexual dysfunction and mild to moderate depression'),
]
POST['artemisia_absinthium'] = [
    ('cinew', {'note': 'Liver injury: two people developed toxic hepatitis after taking wormwood (5 g daily for 6 days to help '
                       'breastfeeding; about 10 g twice daily for a week for urinary complaints). One recovered; the other '
                       'developed acute liver failure, had a liver transplant and died (case reports).',
               'severity': 'warning', 'reference_ids': ['REF-5179']}),
    ('cinew', {'note': 'Not for babies or children: a 10-month-old baby given a home-made wormwood extract for a cold developed '
                       'severe diarrhoea and persistent metabolic acidosis (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5180']}),
    ('dcinew', {'drug_class': 'anticoagulants-antiplatelets', 'severity': 'caution',
                'mechanism': 'An 82-year-old woman on warfarin was admitted with stomach and gut bleeding and a very high INR '
                             'after taking wormwood; the link was rated probable. This rests on a single case report.',
                'reference_ids': ['REF-5181']}),
]
NOTES['artemisia_absinthium'] = (
    'Searched PubMed (Artemisia absinthium tiab; absinthium, absinthe ti), Europe PMC, ClinicalTrials.gov (3, none on '
    'wormwood alone) and OpenAlex. NEW pair depression: Hajatpour 2022 (Mashhad, triple-blind placebo RCT, 76 women with sexual '
    'dysfunction, DASS-21 depression fell; IJOGI, not in PubMed, abstract via OpenAlex). Safety: two toxic-hepatitis cases '
    '2026, one fatal after liver transplant (new warning); infant poisoning case (new caution); warfarin GI-bleeding case, '
    'Naranjo 6 (new DRAFT interaction, caution, needs owner sign-off). Considered, not added: knee-OA ointment/liniment RCT '
    '(vs piroxicam only, no placebo), IgA nephropathy pilot (uncontrolled, 10 patients; kidney-support would be a new pair '
    'and needs an RCT), Sharbat-e-Afsanteen liver-enzyme RCT in alcoholics (J Herb Med 2023; no abstract retrievable), eye '
    'cream for dark circles (no vocab condition), afsanteen + qust hepatitis B (combination), AKI case (three-herb mixture), '
    'absinthe thujone attention study (spiked drinks), 13-week rat NOAEL study (no new claim), MSKCC (no wormwood page, 404).')

# ================================================================== mugwort
PLAN['artemisia_vulgaris'] = []
POST['artemisia_vulgaris'] = [
    ('cinew', {'note': 'Thujone poisoning: a man was taken to hospital in a manic state after drinking 1 litre of mugwort '
                       'infusion, and thujone was found in his blood (case report).',
               'severity': 'caution', 'reference_ids': ['REF-5182']}),
]
NOTES['artemisia_vulgaris'] = (
    'Searched PubMed (Artemisia vulgaris / mugwort tiab: 208 HT, 592 SAFE hits), Europe PMC, ClinicalTrials.gov (6) and '
    'OpenAlex. Almost all hits are mugwort-pollen allergy (Art v 1, mugwort-celery-spice syndrome, food cross-reactivity) '
    'or moxibustion. Neither is used: pollen sensitisation is not evidence about taking the herb, and moxibustion trials test '
    'burning moxa on acupoints (often Artemisia argyi), a procedure rather than the plant. Added: thujone poisoning after '
    '1 L of mugwort infusion, serum thujone confirmed (new caution). Considered, not added: mugwort lotion for burn scars '
    '(letter, no abstract), EFSA 2019/2020 feed-additive opinions (animal feed; no consumer concern), herbs-in-epilepsy '
    'review (no mugwort-specific statement in the abstract), Artemisia vaginal cream vs clotrimazole (species not stated, '
    'active comparator only), MSKCC (no mugwort page, 404).')


def _swap_note(d, old, new, extra_refs=(), **upd):
    c = [x for x in d['contraindications'] if x['note'] == old]
    assert len(c) == 1, old[:40]
    assert '—' not in new and '–' not in new
    c[0]['note'] = new
    for r in extra_refs:
        if r not in c[0]['reference_ids']:
            c[0]['reference_ids'].append(r)
    c[0].update(upd)
    return c[0]


def text_edits():
    path = 'plants/andrographis_paniculata.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    _swap_note(d, AP_OLD, AP_NEW, ['REF-5169', 'REF-5170'])
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/arctium_minus.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    c = [x for x in d['contraindications'] if x['note'] == AM_OLD]; assert len(c) == 1
    i = d['contraindications'].index(c[0])
    c[0]['note'] = AM_REST
    d['contraindications'].insert(i, {'note': AM_SUGAR, 'severity': 'caution', 'reference_ids': ['REF-5185'],
                                      'status': 'verified'})
    assert 'antidiabetic' not in {a['action'] for a in d['actions']}
    d['actions'].append({'action': 'antidiabetic', 'reference_ids': ['REF-5185'], 'status': 'verified'})
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/arnica_montana.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    _swap_note(d, AR_ALLERGY_OLD, AR_ALLERGY_NEW, ['REF-5176', 'REF-5177', 'REF-5186'])
    _swap_note(d, AR_PREG_OLD, AR_PREG_NEW, ['REF-5186'])
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r04_changes.tsv')
    stems = set(PLAN) | set(POST)
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in stems]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new())
        bib = open('bibliography.bibtex', encoding='utf-8', newline='').read()
        for k in WEB:
            assert bib.count('@article{' + k + ',') == 1
            bib = bib.replace('@article{' + k + ',', '@misc{' + k + ',')
        open('bibliography.bibtex', 'w', encoding='utf-8', newline='').write(bib)
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        text_edits()
        print('pubmed urls added:', pubmed_urls())
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
