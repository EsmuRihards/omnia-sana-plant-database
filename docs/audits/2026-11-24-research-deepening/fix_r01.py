"""Research-deepening batch 1 (achillea-millefolium, acorus-calamus, actaea-racemosa, aegopodium-podagraria,
aesculus-hippocastanum). Run from the repo root (worktree). Report: batches/r01_report.md.
Owner rules applied: a new symptom pair needs an SR/MA or RCT of the species that names the symptom and finds benefit
(inv. 12a); no-effect studies go to null_result_ids (inv. 7); a plant's signature compound counts, labelled (inv. 10);
superseded review versions are not cited (inv. 11); a pair the plant's own safety note forbids is not added (inv. 12d);
new herb-drug interactions are DRAFT only (owner sign-off). Lab-only evidence goes to actions/constituents/safety, never
to a symptom pair (owner direction 2026-11-16: symptom pairs need human evidence).
New refs come from a reserved block REF-5001.. (a parallel session allocates REF-4029.., 4201.., 4301..).
PubMed abstracts are verbatim efetch (cache ../2026-11-10-symptom-audit/deep/abstracts.json); non-PubMed abstracts are
Crossref deposits or OpenAlex's reconstruction of the publisher abstract (batches/doi_cache.json)."""
import copy, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '2026-11-10-symptom-audit'))
import fixlib, deep_lib, rd_fix, rd_doi  # noqa: E402
import yamlsplice as Y  # noqa: E402

fixlib.DATE = '2026-11-24'
LABEL = 'research-deepening batch 1'

# ------------------------------------------------------------------ new bibliography entries (PubMed)
SPEC = [
    # horse chestnut
    ('REF-5001', '8569363', 'hcselancetcompression', 'rct'),
    ('REF-5002', '12518108', 'hcsecvima', 'meta-analysis'),
    ('REF-5003', '1621440', 'hcsedeepveinrct', 'rct'),
    ('REF-5004', '3527643', 'hcsefiltration', 'rct'),
    ('REF-5005', '15364642', 'hcseaesculaforceopen', 'clinical'),
    ('REF-5006', '11933130', 'hcsevspycnogenol', 'rct'),
    ('REF-5007', '11747472', 'hcseadvancedcvi', 'rct'),
    ('REF-5008', '16620045', 'hcselegulcer', 'rct'),
    ('REF-5009', '8255928', 'escingelhematoma', 'rct'),
    ('REF-5010', '42392851', 'escinhemorrhoidrecurrence', 'rct'),
    ('REF-5011', '39153932', 'aescinhemorrhoidbleeding', 'rct'),
    ('REF-5012', '33869100', 'horsechestnutdili', 'clinical'),
    ('REF-5013', '3699401', 'venoplanthepatic', 'clinical'),
    ('REF-5014', '35000361', 'horsechestnutseedpoisoning', 'clinical'),
    ('REF-5015', '25632792', 'horsechestnutsnuff', 'clinical'),
    ('REF-5016', '39728810', 'foodconfusionmarseille', 'clinical'),
    ('REF-5017', '21310579', 'hcserenalbleed', 'clinical'),
    ('REF-5018', '18331390', 'tradeherbscyp3a4pgp', 'preclinical'),
    ('REF-5019', '17214607', 'tradeherbscypinduction', 'preclinical'),
    ('REF-5020', '14964349', 'aescinbioavailability', 'rct'),
    ('REF-5021', '9748710', 'escinbioavailability', 'rct'),
    ('REF-5022', '37865870', 'betaescinreview', 'narrative-review'),
    ('REF-5023', '27366690', 'hcsethyroideye', 'rct'),
    # yarrow
    ('REF-5024', '39856724', 'yarrowt2dmliverlipids', 'rct'),
    ('REF-5025', '33874968', 'yarrowlivercompressfatigue', 'rct'),
    ('REF-5026', '24804185', 'yarrowleishmaniasis', 'rct'),
    ('REF-5027', '30599916', 'yarrowmultiplesclerosis', 'rct'),
    ('REF-5028', '21711463', 'yarrowskinrejuvenation', 'rct'),
    ('REF-5029', '27913788', 'yarrowcosmeticsafety', 'narrative-review'),
    ('REF-5030', '14745991', 'yarrowpregnantrat', 'preclinical'),
    ('REF-5031', '42316569', 'yarrowpharmreview2026', 'narrative-review'),
    # sweet flag
    ('REF-5041', '20040135', 'calamusoilintoxications', 'clinical'),
    ('REF-5042', '16159994', 'herbalhighsinternet', 'traditional'),
    ('REF-5043', '21062640', 'calamuscyp3a4cyp2d6', 'preclinical'),
    ('REF-5044', '41441227', 'calamusoilskinsensitiser', 'preclinical'),
    ('REF-5045', '23741157', 'vachashodhana', 'preclinical'),
    ('REF-5046', '33410326', 'asaronefoodproducts', 'preclinical'),
    # black cohosh
    ('REF-5049', '16432272', 'cohoshcyp3amidazolam', 'rct'),
    ('REF-5050', '16221754', 'cohoshdigoxin', 'rct'),
    ('REF-5051', '18214849', 'cohoshcyp2d6debrisoquine', 'clinical'),
    ('REF-5052', '38556373', 'cohoshserotonintoxicity', 'clinical'),
    ('REF-5053', '21827327', 'cohoshtamoxifeninvitro', 'preclinical'),
    ('REF-5054', '21228727', 'cohoshliverma', 'meta-analysis'),
    ('REF-5055', '18340277', 'cohoshuspliverreview', 'narrative-review'),
    ('REF-5056', '33962922', 'cohoshcholestaticdili', 'clinical'),
    ('REF-5057', '28203134', 'cohoshautoimmunehepatitis', 'clinical'),
    ('REF-5058', '19539907', 'cohoshhepaticperfusion', 'clinical'),
    ('REF-5059', '21660145', 'cohoshliverfollowup', 'clinical'),
    ('REF-5060', '18984078', 'cohoshadverseeventssr', 'systematic-review'),
    ('REF-5061', '38606233', 'cohoshbradycardia', 'clinical'),
    ('REF-5062', '32955954', 'cohoshmania', 'clinical'),
    ('REF-5063', '26989565', 'cohoshhyponatremialabour', 'clinical'),
    ('REF-5064', '17085773', 'cohoshpregnancylactation', 'systematic-review'),
    ('REF-5065', '11352967', 'cohoshbreastcancerhotflashes', 'rct'),
    ('REF-5066', '12609560', 'cohoshtamoxifenhotflushes', 'rct'),
    ('REF-5067', '16039414', 'cohoshethanolicextract', 'rct'),
    ('REF-5068', '12609561', 'cohoshbno1055conjugatedestrogens', 'rct'),
    ('REF-5069', '23346194', 'cohoshze450dose', 'rct'),
    ('REF-5070', '24499633', 'cohoshearlymenopause', 'rct'),
    ('REF-5071', '30935866', 'cohoshlhrhbreastcancer', 'rct'),
    ('REF-5072', '28276200', 'nicevasomotornma', 'meta-analysis'),
    ('REF-5073', '41498229', 'imscomplementarytherapies', 'systematic-review'),
    ('REF-5074', '19745648', 'cohoshanxietyrct', 'rct'),
    ('REF-5075', '17019374', 'cohoshbreastdensity', 'clinical'),
    ('REF-5076', '21958943', 'cohoshmammographicdensity', 'rct'),
    ('REF-5077', '17416109', 'cohoshbreastrecurrence', 'clinical'),
    ('REF-5078', '16837890', 'cohoshendometrialsafety', 'clinical'),
    ('REF-5079', '21231853', 'cohoshtamoxifenobservational', 'clinical'),
    ('REF-5080', '20032972', 'cohoshdeoxyacteinpk', 'clinical'),
    ('REF-5081', '36323641', 'cohoshgenotoxicitywomen', 'clinical'),
    ('REF-5082', '31691621', 'cohoshendothelialfunction', 'rct'),
]

# ------------------------------------------------------------------ new bibliography entries (not in PubMed)
def _initials(name):
    """'Sara Abdoli' -> 'Abdoli, S.'; leaves 'Abdoli, S.' unchanged."""
    if ',' in name:
        return name
    parts = name.split()
    return f"{parts[-1]}, {''.join(p[0] + '.' for p in parts[:-1])}"


def _ascii(s):
    return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


DOI_SPEC = [  # (rid, doi, slug, study_type, field overrides)
    ('REF-5032', '10.1016/j.ctmp.2026.200287', 'yarrowpms', 'rct', {}),
    ('REF-5033', '10.22038/ijn.2020.40011.1647', 'yarrownipplefissure', 'rct',
     {'journal': 'Iranian Journal of Neonatology', 'volume': '11', 'number': '2', 'pages': '24--29'}),
    ('REF-5034', '10.22038/ijogi.2020.15965', 'yarrowmenorrhagia2020', 'rct',
     {'journal': 'Iranian Journal of Obstetrics, Gynecology and Infertility', 'volume': '23', 'number': '2', 'pages': '67--77'}),
    ('REF-5035', '10.22038/ijogi.2019.13200', 'yarrowmenorrhagia2019', 'rct',
     {'journal': 'Iranian Journal of Obstetrics, Gynecology and Infertility', 'volume': '22', 'number': '2', 'pages': '34--41'}),
    ('REF-5036', '10.5812/jjnpp.14077', 'yarrowamlmucositis', 'rct', {'volume': None, 'number': None}),
    ('REF-5037', '10.31557/apjcc.2016.1.1.9', 'yarrowradiationdermatitis', 'rct', {}),
    ('REF-5038', '10.17795/nmsjournal37268', 'yarrowgastroenteritis', 'rct', {}),
    ('REF-5039', '10.2478/v10249-011-0009-9', 'yarrowvenousulcers', 'clinical', {}),
    ('REF-5040', '10.5505/jaemcr.2013.55477', 'yarrowanticholinergic', 'clinical', {}),
    ('REF-5048', '10.7860/jcdr/2025/82584.22168', 'vachatailanasya', 'rct', {'journal': 'Journal of Clinical and Diagnostic Research'}),
]


def doi_entries():
    out = {}
    for rid, doi, slug, st, over in DOI_SPEC:
        key, (r, fields) = rd_doi.newref_doi(doi, rid, 'x', st)
        f = dict(fields)
        au = [_initials(a.strip()) for a in rd_doi.fetch(doi)['authors']]
        f['author'] = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
        for k, v in over.items():
            if v is None:
                f.pop(k, None)
            else:
                f[k] = v
        order = ['author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'note', 'study_type', 'abstract', 'summary']
        fl = [(k, f[k]) for k in order if k in f]
        first = _ascii(f['author'].split(',')[0])
        out[first + f['year'] + slug] = (rid, fl)
    return out


EMA_ASARONE = ('ema2005asarone', ('REF-5047', [
    ('author', 'European Medicines Agency (HMPC)'),
    ('title', 'Public statement on the use of herbal medicinal products containing asarone'),
    ('year', '2005'),
    ('url', 'https://www.ema.europa.eu/en/documents/scientific-guideline/public-statement-use-herbal-medicinal-products-containing-asarone_en.pdf'),
    ('note', 'REF-5047'), ('study_type', 'traditional'),
    ('summary', 'EMEA/HMPC/139215/2005, adopted November 2005 (read from the PDF 2026-11-24). Alpha- and beta-asarone are genotoxic '
                'and hepatocarcinogenic in rodents; their concentration in herbal medicinal products should be reduced to a '
                'minimum and diploid varieties should always be preferred; an exposure limit of approximately 115 micrograms a '
                'day (about 2 micrograms per kg body weight) could be accepted temporarily. Beta-asarone content: diploid '
                'Acorus calamus var. americanus not detected; triploid var. calamus rhizome essential oil 9-19% (dried rhizome '
                '0.3%); tetraploid var. angustatus rhizome oil 85-95% (dried rhizome 4.4-8.3%). Reported traditional uses of the '
                'rhizome: stomach cramps, dysentery, asthma, anthelmintic, insecticide, tonic, stimulant.')]))

BIB = dict(
    retag={'REF-0515': 'narrative-review'},     # Uebel 2021 J Appl Toxicol asarone toxicology review, was 'traditional'
    sets={'REF-3086': {'year': '2020'}},        # printed date of the PDF at its url: 15 January 2020
    delete=['REF-2085'],                        # retracted (Hepatol Forum retraction notice, PMID 43032310)
)

PLAN, POST, NOTES = {}, {}, {}

# ================================================================== horse chestnut
PLAN['aesculus_hippocastanum'] = [
    ('add', 'swelling', ['REF-5001', 'REF-5002', 'REF-5003', 'REF-5005', 'REF-3086']),
    ('nulladd', 'swelling', ['REF-5006', 'REF-5007']),
    ('note', 'swelling', 'Horse chestnut seed extract reduced lower-leg volume (oedema) vs placebo in chronic venous insufficiency in '
     'randomized trials and meta-analyses, and matched compression stockings in one trial; the EU monograph lists swollen legs '
     'among the venous symptoms it treats. A trial in advanced venous insufficiency and an open comparison with pine bark '
     'extract found no significant effect'),
    ('add', 'varicose-veins', ['REF-5001', 'REF-5002', 'REF-5003', 'REF-5005', 'REF-3086']),
    ('nulladd', 'varicose-veins', ['REF-5006', 'REF-5007']),
    ('note', 'varicose-veins', 'Chronic venous insufficiency (varicose veins, swollen, heavy and aching legs): horse chestnut seed '
     'extract improved leg swelling, pain and itching vs placebo in meta-analyses of randomized trials and is an EU '
     'well-established-use medicine for it; one trial in advanced venous insufficiency and one open comparison found no '
     'significant benefit'),
    ('add', 'pain', ['REF-3086']),
    ('note', 'pain', 'In chronic venous insufficiency, horse chestnut seed extract reduced leg pain vs placebo in six of seven '
     'placebo-controlled trials (Cochrane review); the EU monograph lists leg pain among the venous symptoms it treats'),
    ('newpair', 'bruising', ['REF-5009', 'REF-3086'],
     'A 2% escin gel (escin is the main saponin of horse chestnut seed; compound evidence) reduced the tenderness of '
     'experimentally induced bruises vs placebo in a double-blind randomized trial; the EU monograph lists traditional use on '
     'the skin for bruises (local swelling and haematoma)'),
    ('add', 'hemorrhoids', ['REF-5010', 'REF-5011']),
    ('note', 'hemorrhoids', 'Adding escin (the main saponin of horse chestnut seed, registered as "aescin in horse chestnut"; '
     'compound evidence) to a flavonoid haemorrhoid drug (MPFF) stopped bleeding haemorrhoids sooner than MPFF alone in two '
     'randomized trials, and in the double-blind one it also cut recurrence over 3 months'),
    ('status', 'hemorrhoids', 'verified'),
    ('aadd', 'anti-oedematous', ['REF-5004']),
    ('refadd', ['REF-5008', 'REF-5023']),
]
POST['aesculus_hippocastanum'] = [
    ('cadd', 'Triterpene saponins', ['REF-5020', 'REF-5022']),
    ('ciadd', 'Raw conkers', ['REF-5014', 'REF-5016', 'REF-5015']),
    ('ciadd', 'bleeding risk', ['REF-3086', 'REF-5017']),
    ('cinew', {'note': 'Reported side effects include stomach and gut complaints, headache, dizziness, itching and allergic '
                       'reactions, and itching or redness of the skin with gels and creams (EU monograph). Liver injury is rare '
                       'but has been reported: once with an oral horse chestnut supplement in a 70-year-old man (2021) and once '
                       'after an injected horse chestnut extract (1986). Stop and seek advice if jaundice, dark urine or '
                       'itching all over develops.',
               'severity': 'caution', 'reference_ids': ['REF-3086', 'REF-5012', 'REF-5013']}),
    ('dadd', 'Standardised oral extract', ['REF-3086', 'REF-5001', 'REF-5021']),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'In laboratory tests a commercial horse chestnut product inhibited the drug-clearing enzyme CYP3A4 and '
                             'the P-glycoprotein drug pump, and also lowered CYP activity in human liver cells; its authors '
                             'suggested possible interactions in the gut. No study in people has tested this, and the EU monograph '
                             'reports no interactions, so the evidence is insufficient to judge.',
                'reference_ids': ['REF-5018', 'REF-5019', 'REF-3086']}),
]
HC_RAW = ('Use only standardised, processed seed extract. Raw conkers are poisonous: people who ate them after mistaking them '
          'for edible sweet chestnuts developed stomach pain, nausea and vomiting, and in one case a temporary irregular '
          'heartbeat; snorting the powdered seeds has caused vomiting, breathing difficulty and fainting. Never eat raw horse '
          'chestnut.')
HC_CAUTION = ('The EU monograph advises seeing a doctor before use if you have heart or kidney failure, inflamed skin, '
              'thrombophlebitis, leg ulcers, severe pain or sudden swelling of one or both legs, and does not recommend use in '
              'pregnancy, while breastfeeding or under 18 years. One case of life-threatening kidney bleeding in a woman taking '
              'horse chestnut seed extract has been reported, and its authors advise caution with blood-thinning medicines.')
HC_DOSE = ('The EU herbal monograph (well-established use) gives a standardised dry extract corresponding to 21 mg triterpene '
           'glycosides, calculated as protoaescigenin (previously declared as 50 mg aescin), twice daily for adults and the '
           'elderly; at least 4 weeks may be needed before any benefit, and use under 18 is not recommended. The main '
           'placebo-controlled trial gave extract providing 50 mg aescin twice daily for 12 weeks. Educational reference only, '
           'not a prescription.')
NOTES['aesculus_hippocastanum'] = (
    'Added human evidence (REF-5001..5023): Diehm 1996 Lancet RCT (HCSE 50 mg aescin twice daily = compression, both beat '
    'placebo on leg volume), Siebert 2002 MA (13 RCTs + 3 observational), Diehm 1992 RCT, Dickson 2004 open study '
    '(Aesculaforce) to swelling + varicose-veins; Ottillinger 2001 (advanced CVI: HCSE not superior to placebo) and Koch 2002 '
    '(open, Venostasin not significant vs Pycnogenol) recorded as no-effect. EU monograph REF-3086 (read from the PDF '
    '2026-11-24: printed 15 January 2020, EMA/HMPC/638242/2018; year corrected from 2023) names CVI swollen legs, varicose '
    'veins, pain; traditional cutaneous use for bruises (local oedema, haematoma); interactions none reported; '
    'pregnancy/lactation not recommended. NEW bruising pair: Calabrese 1993 RCT (2% escin gel, experimental haematoma, '
    'compound evidence) + EU monograph. Hemorrhoids now sourced: two Thai RCTs adding escin to MPFF (NCT06748014 registers the '
    'drug as "Aescin in Horse Chestnut"). Bisler 1986 crossover RCT (capillary filtration -22%) to anti-oedematous. Safety: '
    'DILI case 2021, Venoplant injection hepatic injury 1986, seed poisoning (Korean-chestnut confusion), snuff intoxication, '
    'Marseille PCC food confusion (A. hippocastanum 2.5% of 2,197 events), renal angiomyolipoma bleed. Raw-seed note '
    're-sourced (Cochrane states none of it; "esculin" wording dropped, the reports blame the seed/aescin) and raised to '
    'warning. Draft CYP3A4 interaction (insufficient; in vitro only). Not wired to the approved anticoagulant interaction '
    '(owner record): REF-5017 would support it. Bucket: Leach 2006 venous-ulcer RCT (healing NS; slough and dressing changes '
    'better), thyroid-eye-disease add-on RCT. Rejected: Pittler 1998 Arch Dermatol SR (earlier version of the held Cochrane '
    'review, superseded), Rehn 1996 (active comparator only), 1788677 (no abstract), Fang 2010 escin varicocele RCT (Chinese '
    'escin, species not named, all arms on composite medicines), escin/diethylamine-salicylate/heparin gels (Wetzel 2002, '
    '2001: combinations), aescin+heparin+PDC registry, F1000 third-molar aescin protocol (no results), sulodexide NMA (no '
    'HCSE-specific result), Aesculaforce 5-study product review, HAVLUT methods paper, cost-benefit companion, effusive '
    'pericarditis after "horse chestnut paste" (single case, product unclear), IV aescin renal-failure reports (parenteral, '
    'gentamicin co-therapy, no abstracts), contact urticaria / dermatitis / defensin-allergy letters (no abstracts), '
    'indinavir-crystallization escin trial (no symptom; plasma indinavir unchanged). Sweet chestnut (Castanea) is not a DB '
    'plant, so the conker/sweet-chestnut confusion is recorded as a safety note, not a dangerous_lookalikes entry.')

# ================================================================== yarrow
PLAN['achillea_millefolium'] = [
    ('purge', 'REF-2085'),
    ('newpair', 'liver-support', ['REF-5024'],
     'Yarrow capsules (500 mg a day for 3 months) lowered the liver enzymes ALT and AST vs placebo in a double-blind randomized '
     'trial in people with type 2 diabetes'),
    ('newpair', 'high-cholesterol', ['REF-5024'],
     'Yarrow capsules (500 mg a day for 3 months) lowered LDL and total cholesterol and triglycerides vs placebo in a '
     'double-blind randomized trial in people with type 2 diabetes'),
    ('newpair', 'pms', ['REF-5032'],
     'Yarrow capsules taken from day 21 of the cycle to day 3 of the next reduced premenstrual symptoms and abdominal pain vs '
     'placebo in a double-blind randomized trial (Unani medicine, India)'),
    ('add', 'heavy-bleeding', ['REF-5034', 'REF-5035']),
    ('note', 'heavy-bleeding', 'Yarrow capsules added to mefenamic acid reduced the amount and duration of heavy menstrual '
     'bleeding more than placebo in two triple-blind randomized trials; also a traditional styptic for heavy periods and '
     'nosebleeds (Herbal Reality; Grieve, A Modern Herbal)'),
    ('status', 'heavy-bleeding', 'verified'),
    ('add', 'wounds', ['REF-5033']),
    ('nulladd', 'wounds', ['REF-5039']),
    ('note', 'wounds', 'Traditional styptic for minor cuts; in randomized trials a yarrow ointment reduced pain, redness and '
     'swelling of episiotomy wounds and yarrow tea-bag compresses healed cracked nipples faster than breast milk; a small '
     'controlled study of a yarrow ointment for venous leg ulcers left its benefit uncertain'),
    ('add', 'oral-health', ['REF-5036']),
    ('note', 'oral-health', 'Yarrow mouthwashes eased chemotherapy mouth sores in two randomized trials (added to routine or '
     'chlorhexidine mouthwash); in one they did not prevent the sores from starting'),
    ('nulladd', 'infection', ['REF-5026']),
    ('note', 'infection', 'Traditionally used for respiratory infections (review of traditional uses); a yarrow gel added to '
     'standard injections did not improve cure of cutaneous leishmaniasis vs placebo in a randomized trial'),
    ('nulladd', 'skin-irritation', ['REF-5037']),
    ('note', 'skin-irritation', 'Traditionally used for skin conditions (review); yarrow oil extracts restored experimentally '
     'irritated skin in a randomized trial in volunteers; a yarrow cream did not significantly prevent radiation dermatitis vs '
     'placebo'),
    ('aadd', 'anti-inflammatory', ['REF-5031']), ('aadd', 'antioxidant', ['REF-5031']),
    ('aadd', 'antispasmodic', ['REF-5031']), ('aadd', 'antimicrobial', ['REF-5031']),
    ('refadd', ['REF-5025', 'REF-5027', 'REF-5028', 'REF-5038']),
]
POST['achillea_millefolium'] = [
    ('ciadd', 'Medicinal use is traditionally avoided in pregnancy', ['REF-5030']),
    ('ciadd', 'As a member of the daisy family', ['REF-5029', 'REF-5026']),
    ('cinew', {'note': 'One case of anticholinergic-type poisoning (blurred vision, dry mouth, facial flushing and palpitations) '
                       'was reported in a woman who drank five cups of yarrow tea a day for a week.',
               'severity': 'caution', 'reference_ids': ['REF-5040']}),
    ('dnew', {'name': 'Capsules (doses used in clinical trials)',
              'text': 'Clinical trials used yarrow capsules of different strengths: 500 mg a day for 3 months (type 2 '
                      'diabetes), two 500 mg capsules three times a day from day 21 of the cycle to day 3 of the next '
                      '(premenstrual syndrome), and 150 mg every 8 hours during menstruation alongside mefenamic acid (heavy '
                      'periods). The products were not standardised. Educational reference only, not a prescription.',
              'reference_ids': ['REF-5024', 'REF-5032', 'REF-5034']}),
]
NOTES['achillea_millefolium'] = (
    'Searched PubMed (human-trial, SR, safety, observational, review families; name clause "Achillea millefolium" OR yarrow '
    'tiab), Europe PMC (non-MEDLINE + full text), ClinicalTrials.gov and OpenAlex (no-PMID trial-worded works). RETRACTION: '
    'REF-2085 (Hepatol Forum, haemostatic effect in localized bleeding) was retracted (notice PMID 43032310) - purged from '
    'styptic, poultice and heavy-bleeding exclusions, entry deleted. NEW pairs (RCTs, inv. 12a): liver-support and '
    'high-cholesterol (REF-5024, T2DM double-blind RCT, ALT/AST and LDL/TC/TG down vs placebo), pms (REF-5032, double-blind '
    'RCT 2026, non-PubMed; abstract from OpenAlex). Wired: two triple-blind menorrhagia add-on RCTs (Iranian J Obstet Gynecol '
    'Infertil 2019, 2020; journal pages read 2026-11-24) to heavy-bleeding (now verified); nipple-fissure RCT (Iranian J '
    'Neonatol 2020) to wounds; AML mucositis RCT (Jundishapur J Nat Pharm Prod 2019) to oral-health. No-effect: '
    'leishmaniasis gel RCT (infection; also more application-site redness, wired to the allergy caution), radiation '
    'dermatitis RCT (skin-irritation; yarrow arm vs placebo NS), venous-ulcer ointment study (wounds; no statistics, authors '
    'call efficacy still to be investigated). Bucket (no vocab condition / not a symptom pair): liver-compress fatigue RCT '
    '(primary endpoint p=0.13), MS add-on RCT (relapse rate; cognitive tests secondary), wrinkle/pore cosmetic RCT, '
    'gastroenteritis distillate RCT (recovery time; gastroenteritis is not the diarrhea condition). Safety: CIR cosmetic '
    'safety assessment, rat pregnancy study (reduced fetal weight at 56x human dose), anticholinergic case report (J Acad '
    'Emerg Med Case Rep 2013). Rejected: 25699281 (same Kashan 56-patient trial as held REF-3410, duplicate publication), '
    'episiotomy SR 42817109 and dysmenorrhoea MA 41983255 (abstracts give no yarrow-specific result), haemorrhoid RCT '
    '(10.1016/j.hermed.2023.100657) and epistaxis RCT (10.1016/j.hermed.2021.100468) - promising but no abstract retrievable '
    '(Elsevier 403; Crossref, OpenAlex, Semantic Scholar have none), needs manual retrieval; knee OA topical oil RCT '
    '(10.1080/22311866.2025.2493088: abstract reports only the time effect, not yarrow vs placebo); harm SR in AJHNM 2020 (no '
    'abstract, only the journal blurb); vaginitis vagitories, Boswellia/ginger/yarrow IBS mixture, ginger+yarrow mouthwash, '
    'BNO 1030, Liv-52, atopic dermatitis combination (multi-herb); CKD nitrite RCT (non-significant, no symptom); HRV '
    'secondary of the liver-compress trial; CT.gov NCT06070571 (yarrow + moringa mixture, no results). Generic Grieve '
    'REF-0098 left for the locatorless-ref audit (owner session 2026-11-24).')

# ================================================================== sweet flag
PLAN['acorus_calamus'] = [
    ('refadd', ['REF-5048']),
]
POST['acorus_calamus'] = [
    ('ciadd', 'SERIOUS: beta-asarone', ['REF-5047', 'REF-5046']),
    ('ciadd', 'Do not use in pregnancy', ['REF-5047']),
    ('cinew', {'note': 'Calamus products sold online as "legal highs" have caused poisonings: the Swedish Poisons Information '
                       'Centre was consulted about 30 intentional intoxications in 2003-2006, mainly with prolonged vomiting '
                       'lasting up to 15 hours.',
               'severity': 'warning', 'reference_ids': ['REF-5041', 'REF-5042']}),
    ('cinew', {'note': 'In laboratory skin-safety tests, sweet flag rhizome oil (about 41% beta-asarone) was a moderate skin '
                       'sensitiser and irritant; its authors give safe concentrations of about 0.13-0.78% for leave-on '
                       'products.',
               'severity': 'caution', 'reference_ids': ['REF-5044']}),
    ('cadd', 'Phenylpropanoid asarones', ['REF-5047', 'REF-5046']),
    ('dadd', 'All preparations', ['REF-5047']),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'insufficient',
                'mechanism': 'In laboratory tests a standardised sweet flag extract and its alpha-asarone moderately inhibited the '
                             'drug-clearing enzymes CYP3A4 and CYP2D6; this has not been studied in people.',
                'reference_ids': ['REF-5043']}),
    ('madd', 'botanical_description', ['REF-3186']), ('madd', 'habitat', ['REF-3186']),
    ('madd', 'harvesting', ['REF-3186']), ('madd', 'traditional_uses', ['REF-3186', 'REF-5045', 'REF-5047']),
]
AC_SERIOUS = ('SERIOUS: alpha- and beta-asarone, the main aromatic compounds of the rhizome, are genotoxic and cause liver cancer '
              'in rodents. The EU herbal committee (EMA/HMPC) advises keeping asarone in herbal medicines to a minimum and '
              'always preferring the beta-asarone-free diploid variety, with a provisional exposure limit of about 115 '
              'micrograms a day (about 2 micrograms per kg body weight); herbal teas and food supplements made from calamus '
              'have been found to contain high asarone levels. It is banned as a food additive in the USA. Avoid internal use '
              'except properly characterised beta-asarone-free preparations.')
AC_DOSE = ('Because alpha- and beta-asarone are genotoxic and carcinogenic in animal studies and their content varies widely '
           'between varieties, no general dose is given here. The EU herbal committee\'s provisional limit for asarone '
           'exposure from herbal medicines is about 115 micrograms a day (about 2 micrograms per kg body weight). Internal use '
           'should be restricted to properly characterised, beta-asarone-free preparations under professional guidance. '
           'Educational reference only, not a prescription.')
AC_BOT = ('Aromatic, reed-like aquatic perennial with a long, branched, cylindrical rhizome about the thickness of a finger, '
          'creeping in the mud and sending out numerous roots. The few erect leaves are yellowish-green, 2-3 feet long, '
          'sword-shaped, narrow and flat, sheathing and pink at the base, with entire but wavy or crimped edges and an aromatic '
          'smell when bruised. From the side of a leaf-like stem a solid, cylindrical, blunt flower spike (spadix) 2-4 inches '
          'long projects at an angle, densely crowded with very small greenish-yellow flowers, in June and July. All parts of '
          'the plant have a peculiar, agreeable fragrance.')
AC_HAB = ('Grows in ditches, at the margins of lakes, ponds and streams and in marshy places, often with reeds, bulrushes and '
          'bur-reed. Thought to be native to eastern Asia (the mountain marshes of India) and apparently also to the northern '
          'United States; now found wild in most European countries except Spain, including most English counties.')
AC_HARV = ('The rhizomes are dug in late autumn or early spring, once large enough (generally after two or three years) and '
           'before they lose their firmness and become hollow, then washed, cleared of rootlets and dried, losing 70-75% of '
           'their weight. Peeling is discouraged because the aromatic oil lies in the outer layer. The crimped leaf edges and '
           'the aromatic smell of the bruised leaves distinguish it from the non-aromatic yellow flag iris.')
AC_TRAD = ('Sweet flag rhizome was esteemed as an aromatic stimulant and mild tonic: used to increase the appetite and help '
           'digestion, as a carminative for flatulence, chewed or infused for dyspepsia, for ague and low fevers, and (by older '
           'writers) for nervous complaints, vertigo and headaches; in Oriental medicine for dyspepsia and bronchitis, and '
           'chewed as a cough lozenge. Ayurvedic practitioners used it for weak memory and against worms, after a traditional '
           'detoxifying process (shodhana) prescribed because of its toxic beta-asarone. Other reported traditional uses '
           'include stomach cramps, dysentery and asthma.')
AC_PREP = {
    'Decoction': ('Infusion', 'Historically an infusion of 1 oz (about 28 g) of the dried rhizome to 1 pint of boiling water was '
                  'taken by the teacupful for dyspepsia. Shown for history only: see the serious safety warning about asarone.'),
    'Tincture': ('Tincture', 'Historically made by macerating the finely cut rhizome in alcohol for seven days and filtering, and '
                 'used as a stomachic and flavouring. Shown for history only: see the serious safety warning about asarone.'),
    'Powder': ('Powder', 'The powdered rhizome was historically given in small doses (12 grains to half a drachm, about 0.8-1.9 g), '
               'and the dried root was chewed for dyspepsia and to clear the voice. Shown for history only: see the serious '
               'safety warning about asarone.'),
}
NOTES['acorus_calamus'] = (
    'Searched PubMed (name clause "Acorus calamus" OR "sweet flag" OR "calamus rhizome" OR "calamus oil" OR "Acorus '
    'americanus" tiab, Vacha ti; human-trial, SR, safety, observational, review families), Europe PMC, ClinicalTrials.gov '
    '(10 records, all multi-herb Chinese formulas) and OpenAlex. No usable human efficacy trial: oral Vacha powder trials '
    '(memory in children, AYUSHDHARA 2023; hyperlipidaemia, single-group open, JAIMS 2023) conflict with the record\'s own '
    'serious internal-use warning (inv. 12d) and are uncontrolled or without between-group statistics; homeopathic '
    'verification study (inv. 10); polyherbal Ayurvedic formulas (Brahmighruta, Kushmand Avaleha, Ashtamangal ghrita, Abhaya '
    'ghrita, Murvadhya churna); white-spot-lesion bioadhesive (no effect attributable to calamus); T2DM paper (mice). OWNER '
    'DECISION: Vacha Taila Nasya pilot RCT for post-dural-puncture headache (REF-5048, open-label, blinded assessor, VAS fell '
    'more vs routine care) would meet inv. 12a for a headache pair, but it is intranasal medicated oil for 3 days against a '
    'serious internal-use warning - bucketed, not paired, pending owner call. Safety re-sourced: EMA/HMPC public statement on '
    'asarone (REF-5047, read from the PDF 2026-11-24: genotoxic hepatocarcinogen in rodents, temporary limit ~115 micrograms '
    'a day, prefer diploid, beta-asarone by variety) and Hermes 2021 asarone content of teas/supplements to the serious '
    'warning, variety caution, dose and constituents; Swedish Poisons Centre intoxications + internet "herbal highs" survey '
    '(new warning); OECD in-vitro skin sensitiser/irritant (new caution); draft CYP3A4 interaction (in vitro). REF-0515 '
    'retagged narrative-review (a toxicology review, was traditional). Monograph blocks (description, habitat, harvesting, '
    'traditional uses) and preparations had no sources - rewritten from Grieve Sweet Sedge (REF-3186, read 2026-11-24 by the '
    'web-fetch agent), the EMA statement and the shodhana paper; harvesting no longer says "peeled" (Grieve advises against '
    'peeling) and the unsourced decoction is now Grieve\'s infusion.')

# ================================================================== black cohosh
PLAN['actaea_racemosa'] = [
    ('add', 'hot-flashes', ['REF-5066', 'REF-5070', 'REF-5072', 'REF-5073', 'REF-5079']),
    ('nulladd', 'hot-flashes', ['REF-5065', 'REF-5067']),
    ('note', 'hot-flashes', 'Reduced hot flushes vs placebo in meta-analyses (including the NICE guideline network meta-analysis) '
     'and in several randomized trials, and the 2026 International Menopause Society review rated this moderate-certainty '
     'evidence; a Cochrane review and several other trials, one in breast cancer survivors, found no difference from placebo'),
    ('add', 'menopause', ['REF-5068', 'REF-5069', 'REF-5070', 'REF-5071', 'REF-5072', 'REF-5073', 'REF-5079']),
    ('nulladd', 'menopause', ['REF-5065', 'REF-5067']),
    ('note', 'menopause', 'Improved overall menopausal symptom scores vs placebo in meta-analyses and several randomized trials, '
     'including menopausal symptoms caused by breast cancer treatment; a Cochrane review and several trials found no benefit '
     'over placebo; no effect on menopausal anxiety'),
    ('refadd', ['REF-5074', 'REF-5081', 'REF-5082']),
]
POST['actaea_racemosa'] = [
    ('ciadd', 'Rare reports of liver injury', ['REF-5054', 'REF-5055', 'REF-5056', 'REF-5057', 'REF-5058', 'REF-5059']),
    ('ciadd', 'Current evidence does not show an increased risk of breast cancer', ['REF-5075', 'REF-5076', 'REF-5077', 'REF-5078']),
    ('ciadd', 'Not recommended during pregnancy', ['REF-5064', 'REF-5063']),
    ('cinew', {'note': 'Side effects in clinical trials are usually mild, but isolated case reports describe a very slow heart '
                       'rate in an older woman taking it for years, mania in a woman with depression, and serotonin toxicity '
                       'with muscle breakdown in a woman also taking two antidepressants; use cautiously with a history of '
                       'depression or bipolar disorder.',
               'severity': 'caution', 'reference_ids': ['REF-5060', 'REF-5061', 'REF-5062', 'REF-5052']}),
    ('cadd', 'Triterpene glycosides', ['REF-5080']),
    ('dcinew', {'drug_class': 'cyp3a4-substrates', 'severity': 'likely-safe',
                'mechanism': 'In healthy volunteers, 14-28 days of black cohosh did not change midazolam levels (a CYP3A4 test '
                             'drug), so clinically relevant CYP3A4 interactions are unlikely, although extracts inhibited CYP3A4 '
                             'in laboratory tests.',
                'reference_ids': ['REF-5049', 'REF-2503', 'REF-5053']}),
    ('dcinew', {'drug_class': 'cardiac-glycosides', 'severity': 'likely-safe',
                'mechanism': 'In a randomized study in healthy volunteers, 14 days of black cohosh did not change digoxin blood '
                             'levels, so it is unlikely to affect digoxin through the P-glycoprotein drug pump.',
                'reference_ids': ['REF-5050']}),
    ('dcinew', {'drug_class': 'antidepressants-serotonergic', 'severity': 'caution',
                'mechanism': 'Black cohosh contains serotonin-like compounds. One woman on two long-term antidepressants '
                             'developed serotonin toxicity and muscle breakdown soon after starting black cohosh; this rests on a '
                             'single case report, with no controlled study.',
                'reference_ids': ['REF-5052']}),
    ('dcinew', {'drug_class': 'hormonal-therapies', 'severity': 'insufficient',
                'mechanism': 'In laboratory tests a black cohosh extract blocked the enzymes (CYP2D6, CYP3A4) that turn tamoxifen '
                             'into its active forms, which could in theory weaken tamoxifen. In healthy volunteers black cohosh '
                             'had no or only a weak, clinically irrelevant effect on CYP2D6, and an observational study in '
                             'tamoxifen-treated women reported no related adverse events. Whether it affects tamoxifen\'s '
                             'anticancer effect has not been tested.',
                'reference_ids': ['REF-5053', 'REF-5051', 'REF-2503', 'REF-5079']}),
]
BC_LIVER = ('Rare cases of liver injury, including cholestatic and autoimmune-type hepatitis, have been reported; a US '
            'Pharmacopeia review of 30 reports judged all of them possibly related and recommended a cautionary label. Pooled '
            'data from five trials of the isopropanolic extract (1,117 women) and a 12-month study found no effect on liver '
            'tests. Stop use and seek advice if signs of liver problems occur (jaundice, dark urine, upper-abdominal pain).')
BC_PREG = ('Not recommended during pregnancy or breastfeeding. Midwives have used it to stimulate the womb and induce labour; a '
           'systematic review advises caution in pregnancy, especially the first trimester, and while breastfeeding, and '
           'severe low blood sodium was reported in a woman who took it to induce labour.')
NOTES['actaea_racemosa'] = (
    'Searched PubMed with "Actaea racemosa" OR "Cimicifuga racemosa" OR "black cohosh" tiab (the earlier landmark search used '
    'only the accepted binomial + title common name and missed most of this literature), Cimicifuga/Remifemin ti; Europe '
    'PMC, ClinicalTrials.gov (35 records), OpenAlex. Added: Wuttke 2003 (BNO 1055 = conjugated oestrogens, > placebo), '
    'Schellenberg 2012 (Ze 450 dose-dependent), Iranian 2013 double-blind RCT (Chin Med), LHRH-a breast-cancer RCT 2019, '
    'Hernandez Munoz 2003 (tamoxifen hot flushes, open RCT), NICE 2017 NMA, IMS 2026 SR (moderate certainty), tamoxifen '
    'observational 2011 (clinical) to hot-flashes/menopause; no-effect: Jacobson 2001 (breast cancer survivors) and '
    'Frei-Kleiner 2005 (ITT null, subgroup only). Safety: Naser 2011 liver MA, USP 2008 case review, cholestatic and AIH case '
    'reports, 12-month hepatic perfusion study, 107-patient follow-up; breast density (RCT + open), recurrence cohort, '
    'endometrial safety; pregnancy SR (Dugoua 2006) + labour hyponatraemia case; AE SR + bradycardia, mania, serotonin '
    'toxicity cases; PK of 23-epi-26-deoxyactein. Draft interactions: CYP3A4 likely-safe (midazolam RCT), digoxin '
    'likely-safe, serotonergic antidepressants caution (single case), tamoxifen insufficient (in vitro vs human CYP2D6 data). '
    'Bucket: Amsterdam 2009 anxiety RCT (no anxiolytic effect; no anxiety pair exists), genotoxicity cross-sectional study (no '
    'excess micronuclei), endothelial-function RCT (surrogate in healthy women, not used for a cardiovascular pair). Not '
    'added: 25276716 (J Caring Sci 2013, 84 women, 8 weeks - very likely the same trial as REF-5070, duplicate publication), '
    'active-comparator-only trials (vs tibolone, low-dose estradiol, fluoxetine), combinations (with St John\'s wort, soy '
    'isoflavones, rhodiola, dong quai, Menohelp, BRN-01, Phyto-Female), Nutrients 2026 SR (black cohosh result ambiguous), '
    'Shams 2010 MA (black cohosh-containing preparations), older SRs (Borrelli 2008 held as REF-0623), hypertension study '
    '(Wiad Lek, add-on, not stated randomized), homeopathic Actaea potencies. OWNER DECISIONS: (1) fertility - clomiphene '
    'add-on RCTs (Shahin 2008, 2009; Kamel 2014; 2022 PCOS trial) would meet inv. 12a, but the 2009 trial now carries an '
    'Expression of Concern (Reprod Biomed Online 2026) and the PCOS SR found low-quality evidence; (2) depression - a Chinese '
    'add-on RCT (Remifemin + paroxetine) is positive while the held 2023 MA found no effect on depression.')

# ================================================================== ground elder
PLAN['aegopodium_podagraria'] = []
NOTES['aegopodium_podagraria'] = (
    'Searched PubMed ("Aegopodium podagraria" OR goutweed OR "ground elder" OR Aegopodium tiab: 0 human-trial, 0 SR, 2 '
    'off-topic safety hits), Europe PMC, ClinicalTrials.gov (0 records) and OpenAlex (89 trial-worded works, all ecology or '
    'agronomy except below). No human study exists. Not added: Tovchiga et al. rat/mouse studies (J Adv Med Pharm Sci 2018 '
    'renal/uric-acid effects with hydrochlorothiazide; Int J Biochem Res Rev 2014 hypouricaemic effect; Asian J Res Med Pharm '
    'Sci 2018 behaviour) - preclinical only and published by SCIENCEDOMAIN/Journal Repository, on Beall\'s list of '
    'potentially predatory publishers; Jurczak 2016 gout-plants overview (Nauka Przyroda Technologie, names goutweed in one '
    'sentence). Settled: no new sources this pass.')


def text_edits():
    """Notes and monograph text rewritten from the sources now cited (fixlib/rd_fix ops do not rewrite text)."""
    path = 'plants/aesculus_hippocastanum.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    ci = [c for c in d['contraindications'] if 'Raw conkers' in c['note']]; assert len(ci) == 1
    ci[0].update(note=HC_RAW, severity='warning'); ci[0]['reference_ids'] = [r for r in ci[0]['reference_ids'] if r != 'REF-0470']
    cb = [c for c in d['contraindications'] if 'bleeding risk' in c['note']]; assert len(cb) == 1
    cb[0].update(note=HC_CAUTION, status='verified'); cb[0]['reference_ids'] = [r for r in cb[0]['reference_ids'] if r != 'REF-0470']
    ds = [x for x in d['dosage'] if x['name'] == 'Standardised oral extract']; assert len(ds) == 1
    ds[0].update(text=HC_DOSE, status='verified'); ds[0]['reference_ids'] = [r for r in ds[0]['reference_ids'] if r != 'REF-0590']
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/acorus_calamus.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    cs = [c for c in d['contraindications'] if c['note'].startswith('SERIOUS: beta-asarone')]; assert len(cs) == 1
    cs[0]['note'] = AC_SERIOUS
    ds = [x for x in d['dosage'] if x['name'] == 'All preparations']; assert len(ds) == 1
    ds[0].update(text=AC_DOSE, status='verified')
    b = d['botanical_description']
    b.update(text=AC_BOT, height='Leaves 2-3 feet (about 60-90 cm)',
             leaves='Few, erect, yellowish-green, sword-shaped, sheathing and pink at the base, with wavy or crimped edges; '
                    'aromatic when bruised',
             flowers='Very small greenish-yellow flowers crowded on a blunt, cylindrical spadix 2-4 inches long, projecting at '
                     'an angle from the side of a leaf-like stem',
             root='Long, branched, cylindrical rhizome about the thickness of a finger, creeping in mud, with numerous roots',
             flowering_period='June and July')
    b.pop('fruit', None)
    d['habitat']['text'] = AC_HAB
    d['harvesting'].update(text=AC_HARV, season='Late autumn or early spring')
    d['traditional_uses']['text'] = AC_TRAD
    for p in d['preparations']:
        if p['name'] in AC_PREP:
            p['name'], p['text'] = AC_PREP[p['name']]
            p['reference_ids'] = ['REF-3186']; p['status'] = 'verified'
    assert sum(1 for p in d['preparations'] if p.get('reference_ids') == ['REF-3186']) == 3
    for s in (AC_SERIOUS, AC_DOSE, AC_BOT, AC_HAB, AC_HARV, AC_TRAD, *[v[1] for v in AC_PREP.values()]):
        assert '—' not in s and '–' not in s
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})

    path = 'plants/actaea_racemosa.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    cl = [c for c in d['contraindications'] if c['note'].startswith('Rare reports of liver injury')]; assert len(cl) == 1
    cl[0]['note'] = BC_LIVER
    cp = [c for c in d['contraindications'] if c['note'].startswith('Not recommended during pregnancy')]; assert len(cp) == 1
    cp[0]['note'] = BC_PREG
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


def bib_new():
    new = deep_lib.newrefs(SPEC)
    new.update(doi_entries())
    new[EMA_ASARONE[0]] = EMA_ASARONE[1]
    return new


if __name__ == '__main__':
    log = []
    tsv = os.path.join(HERE, 'batches', 'r01_changes.tsv')
    snap = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in PLAN]}
    try:
        fixlib.main_with_bib(PLAN, NOTES, LABEL, tsv, new=bib_new(), **BIB)
        bib = open('bibliography.bibtex', encoding='utf-8', newline='').read()
        assert bib.count('@article{ema2005asarone,') == 1
        open('bibliography.bibtex', 'w', encoding='utf-8', newline='').write(bib.replace('@article{ema2005asarone,', '@misc{ema2005asarone,'))
        for stem, ops in POST.items():
            rd_fix.apply(stem, ops, log)
        text_edits()
    except BaseException:
        for p, b in snap.items():
            open(p, 'wb').write(b)
        raise
    open(tsv, 'a', encoding='utf-8').write('\n'.join(log) + '\n')
    print(len(log), 'post ops')
