"""Deep re-sweep of batch 10 (laurus-nobilis .. matricaria-chamomilla) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3609..REF-3647 (PubMed efetch, deep/abstracts.json).
Cross-batch: St John's wort bruising dropped here (batch 9 plant; same 'a wound is not a bruise' rule as bay)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3609', '31743795', 'lavenderanxiety2019', 'meta-analysis'),
    ('REF-3610', '34775136', 'lavenderanxietydepression', 'meta-analysis'),
    ('REF-3611', '35262795', 'silexandepressive', 'meta-analysis'),
    ('REF-3612', '38558147', 'silexanmdd', 'rct'),
    ('REF-3613', '35429599', 'lavenderstress', 'meta-analysis'),
    ('REF-3614', '40600743', 'lavendersleep2026', 'meta-analysis'),
    ('REF-3615', '41057090', 'lavendersleepolder', 'meta-analysis'),
    ('REF-3616', '40187937', 'lavenderpostoppain', 'systematic-review'),
    ('REF-3617', '33066851', 'lavenderepisiotomy', 'systematic-review'),
    ('REF-3618', '36622248', 'flaxbpdoseresponse', 'meta-analysis'),
    ('REF-3619', '25740909', 'flaxbp2015', 'meta-analysis'),
    ('REF-3620', '31899314', 'flaxlipids2020', 'meta-analysis'),
    ('REF-3621', '34384619', 'flaxlipids2022', 'meta-analysis'),
    ('REF-3622', '35843472', 'flaxglycemic2022', 'meta-analysis'),
    ('REF-3623', '36640581', 'flaxhba1c', 'meta-analysis'),
    ('REF-3624', '29228348', 'flaxglucose2018', 'meta-analysis'),
    ('REF-3625', '38971216', 'flaxinflammation2024', 'meta-analysis'),
    ('REF-3626', '26959052', 'flaxcrp2016', 'meta-analysis'),
    ('REF-3627', '32229443', 'flaxconstipation', 'rct'),
    ('REF-3628', '30661699', 'flaxpsyllium', 'rct'),
    ('REF-3629', '31006899', 'chamomileanxietysleep', 'meta-analysis'),
    ('REF-3630', '40665590', 'chamomileinflammation', 'meta-analysis'),
    ('REF-3631', '39836709', 'chamomilemenopause', 'rct'),
    ('REF-3632', '41761999', 'chamomilevasomotor', 'rct'),
    ('REF-3633', '24439651', 'chamomilepms', 'rct'),
    ('REF-3634', '29808331', 'chamomilemigraine', 'rct'),
    ('REF-3635', '28025442', 'chamomilegingivitis', 'rct'),
    ('REF-3636', '33290635', 'chamomilemucositis', 'rct'),
    ('REF-3637', '35129844', 'chamomilemucositissr', 'systematic-review'),
    ('REF-3638', '25194428', 'chamomileteaglycemic', 'rct'),
    ('REF-3639', '35787809', 'chamomileoillbp', 'rct'),
    ('REF-3640', '25866155', 'shiitakeimmunity', 'rct'),
    ('REF-3641', '42648714', 'lentinulacancer', 'meta-analysis'),
    ('REF-3642', '31030752', 'lentinanchina', 'systematic-review'),
    ('REF-3643', '23909714', 'psoriasisplantextracts', 'meta-analysis'),
    ('REF-3644', '17890932', 'relievaatopic', 'clinical'),
    ('REF-3645', '33100212', 'malvaatopic', 'rct'),
    ('REF-3646', '41184820', 'malvastomatitis', 'rct'),
    ('REF-3647', '39173823', 'malvamouthwash', 'rct'),
])

BIB = dict(
    retag={'REF-1156': 'rct'},   # chamomile GAD+depression analysis: randomized controlled (PubMed pubtype)
    sets={'REF-0868': {'title': 'Hepatoprotection of Mentha aquatica L., Lavandula dentata L. and Leonurus cardiaca L.'}},  # title did not match its DOI/PubMed record
    delete=['REF-2805',          # Lysimachia foenum-graecum, a different species
            'REF-0105'],         # stearidonic acid (soybean/echium) paper, not flax
    new=NEW)

CHAM_EU = 'EU herbal monograph'

PLAN = {
    'laurus_nobilis': [
        ('drop', 'bruising'),   # only card: a rabbit wound-healing study; a wound is not a bruise (batch-1 rule)
        ('note', 'cancer', 'Bay seed extract killed multidrug-resistant tumour cells in the lab (preclinical)'),
    ],
    'hypericum_perforatum': [
        ('drop', 'bruising'),   # inferred from the vulnerary action (wound-healing review); a wound is not a bruise
    ],
    'lavandula_angustifolia': [('arm', a, ['REF-0265']) for a in ('anti-inflammatory', 'antimicrobial', 'antioxidant', 'antispasmodic', 'emollient')] + [
        ('newpair', 'anxiety', ['REF-2531', 'REF-2546', 'REF-3609', 'REF-3610'], 'Oral lavender oil (Silexan) reduced anxiety vs placebo in meta-analyses of randomized trials, and lavender aromatherapy reduced anxiety in meta-analyses'),
        ('newpair', 'depression', ['REF-3611', 'REF-3612', 'REF-3610'], 'Silexan lavender oil reduced depressive symptoms vs placebo in a meta-analysis and in a randomized trial in mild-to-moderate major depression; an earlier systematic review judged the evidence insufficient'),
        ('nulladd', 'depression', ['REF-2212']),
        ('newpair', 'stress', ['REF-3613'], 'Lavender reduced stress in a meta-analysis of trials'),
        ('newpair', 'pain', ['REF-3616', 'REF-3617'], 'Inhaled lavender reduced postoperative pain (systematic review of randomized trials), and lavender eased episiotomy pain (systematic review)'),
        ('add', 'insomnia', ['REF-3614', 'REF-3615']),
        ('note', 'insomnia', 'Lavender essential oil improved sleep quality in meta-analyses of trials; traditional use to aid sleep (EU herbal monograph); a trial in postmenopausal women with insomnia found no significant effect'),
        ('add', 'wounds', ['REF-3617']),
        ('note', 'wounds', 'Lavender aided episiotomy wound healing in trials (systematic review); the oil is antimicrobial in the lab (preclinical)'),
        ('note', 'cancer', 'Lavender extract slowed breast cancer cells and tumours in lab and animal studies (preclinical)'),
    ],
    'lentinula_edodes': [('arm', a, ['REF-0315']) for a in ('anticancer', 'antidiabetic', 'antimicrobial', 'antioxidant', 'antiviral', 'immunomodulator')]
                        + [('arm', a, ['REF-0293']) for a in ('antidiabetic', 'antimicrobial', 'antioxidant', 'antiviral')] + [
        ('refadd', ['REF-0315']),   # eritadenine anti-obesity observation: no evidence for any of the six actions
        ('add', 'immune-support', ['REF-3640']),
        ('note', 'immune-support', 'Eating shiitake daily improved immune cell function and raised secretory IgA in healthy adults in a randomized trial'),
        ('add', 'cancer', ['REF-3641', 'REF-3642']),
        ('note', 'cancer', 'Lentinan and shiitake extracts given with chemotherapy improved tumour response and quality of life in clinical studies (meta-analysis; systematic review), without proven survival benefit'),
    ],
    'leonurus_cardiaca': [
        ('rm', 'cardiovascular-support', ['REF-0867']),   # PPAR-delta / anti-obesity cell study
        ('rm', 'skin-irritation', ['REF-0861']),          # pharmacology review that does not name skin
        ('note', 'cardiovascular-support', 'Traditional remedy for nervous heart complaints (review of the EMA assessment); lower blood pressure reported in clinical studies (review); extracts reduced platelet activation in the lab (preclinical)'),
        ('note', 'menstrual-cramps', 'Traditionally used for gynaecological complaints including painful periods (review of the EMA assessment)'),
        ('note', 'insomnia', 'Sedative activity reported in clinical studies (review)'),
        ('note', 'inflammation', 'Anti-inflammatory activity reported in pharmacological studies (review)'),
    ],
    'linum_usitatissimum': [
        ('purge', 'REF-0105'),
        ('newpair', 'high-blood-pressure', ['REF-3618', 'REF-3619', 'REF-3395'], 'Flaxseed lowered blood pressure in meta-analyses of trials, more with whole seed, longer use and in hypertension; ground flaxseed strongly lowered blood pressure in hypertensive patients in a randomized trial'),
        ('newpair', 'high-cholesterol', ['REF-3620', 'REF-3621'], 'Flaxseed lowered total and LDL cholesterol and triglycerides in meta-analyses of randomized trials, mainly in people with high blood lipids'),
        ('newpair', 'blood-sugar', ['REF-3622', 'REF-3623', 'REF-3624'], 'Flaxseed improved blood sugar control and HbA1c in prediabetes and type 2 diabetes in meta-analyses; whole flaxseed worked, flaxseed oil and lignan extracts did not'),
        ('newpair', 'constipation', ['REF-3627', 'REF-3628'], 'Flaxseed eased chronic constipation in randomized trials, more than lactulose in one and psyllium in another'),
        ('add', 'inflammation', ['REF-3625']), ('nulladd', 'inflammation', ['REF-3626']),
        ('note', 'inflammation', 'Flaxseed lowered the inflammation markers CRP and IL-6 in a 2024 meta-analysis; an earlier meta-analysis found no overall effect on CRP except in obese people'),
        ('note', 'cancer', 'Dietary flaxseed reduced tumour growth markers in postmenopausal breast cancer patients in a randomized trial; anticancer compounds reviewed (review)'),
        ('note', 'metabolic-support', 'Flaxseed reduced body weight, BMI and waist size in a meta-analysis of trials; a flaxseed lignan supplement modestly improved HbA1c in type 2 diabetes (randomized trial)'),
    ],
    'lysimachia_vulgaris': [
        ('purge', 'REF-2805'),
        ('note', 'liver-support', 'Yellow loosestrife extract eased liver fibrosis in mice with fatty liver disease, and its compounds reduced fat production in liver cells (preclinical)'),
        ('note', 'high-cholesterol', 'Root compounds inhibited PCSK9, a cholesterol-regulating protein, in liver cells (preclinical)'),
        ('note', 'diarrhea', 'Used for diarrhoea in folk medicine (as stated in a lab study); an extract acted on a gut serotonin receptor linked to diarrhoea-type IBS in lab tests (var. davurica; preclinical)'),
        ('note', 'ibs', 'An extract acted on a gut serotonin receptor (5-HT3) linked to diarrhoea-type IBS in lab tests (var. davurica; preclinical)'),
        ('note', 'inflammation', 'Folk anti-inflammatory use is noted in a lab study (preclinical)'),
        ('note', 'infection', 'Extracts were antibacterial in lab tests (preclinical)'),
        ('note', 'wounds', 'Used for wounds in folk medicine (as stated in a lab study)'),
        ('note', 'cancer', 'Extracts slowed tumour growth in lab tests (preclinical)'),
    ],
    'mahonia_aquifolium': [
        ('add', 'psoriasis', ['REF-3643']), ('add', 'eczema', ['REF-3644']),
        ('note', 'psoriasis', 'Topical 10% Mahonia aquifolium cream reduced plaque severity in mild-to-moderate psoriasis (placebo-controlled RCT and other trials; a meta-analysis found benefit from small, weak studies). The cream is registered in the US as a homeopathic product but is a 10% plant extract'),
        ('note', 'eczema', 'Topical Mahonia cream improved atopic eczema in clinical studies (systematic review; open-label trial)'),
        ('note', 'arthritis', 'Traditionally used for gout, rheumatism and arthritis (Herbal Reality)'),
        ('note', 'infection', 'Traditionally used for skin, mouth and intestinal infections (Herbal Reality); the extract and its alkaloids were antibacterial and antifungal in lab tests (preclinical)'),
        ('note', 'wounds', 'Traditionally used topically for infected wounds (Herbal Reality); extracts were antimicrobial in the lab (preclinical)'),
        ('note', 'inflammation', 'Topical Mahonia relieved inflammatory skin disease (psoriasis, atopic eczema) in clinical studies (systematic review); some of its alkaloids reduced inflammatory signals in immune cells (preclinical)'),
        ('note', 'cancer', 'Extracts boosted doxorubicin against lung cancer cells in the lab (preclinical)'),
    ],
    'malva_sylvestris': [
        ('newpair', 'eczema', ['REF-3645'], 'A Malva sylvestris cream reduced atopic eczema symptoms in children in a randomized double-blind trial'),
        ('newpair', 'oral-health', ['REF-3646', 'REF-3647', 'REF-0480'], 'A mallow mouthwash eased chemotherapy mouth sores and their pain in a randomized trial, and reduced plaque as well as chlorhexidine (with less effect on gum inflammation); traditional use for mouth and throat irritation (EU herbal monograph)'),
        ('add', 'pain', ['REF-3646']),
        ('note', 'pain', 'A mallow mouthwash eased chemotherapy mouth-sore pain in a randomized trial, but a cream did not ease episiotomy pain; analgesic effects reported in lab and animal studies (reviews)'),
        ('note', 'sore-throat', 'Traditional demulcent for mouth and throat irritation (EU herbal monograph)'),
        ('note', 'infection', 'Antibacterial activity reported (reviews)'),
        ('note', 'inflammation', 'Extracts reduced inflammation in lab and animal studies (reviews; preclinical)'),
        ('note', 'wounds', 'Wound healing reported in lab and animal studies (review); a cream did not improve episiotomy healing in a randomized trial'),
        ('note', 'cancer', 'Anticancer activity of its compounds reviewed (review)'),
    ],
    'marrubium_vulgare': [
        ('arm', 'expectorant', ['REF-0926']),                                # rat lung-fibrosis study, not expectoration
        ('arm', 'antispasmodic', ['REF-0925']), ('refadd', ['REF-0925']),     # antinociception study, not antispasmodic
        ('note', 'respiratory-support', 'Traditional expectorant for cough associated with colds (EU herbal monograph); protected the lungs of rats with lung fibrosis (preclinical)'),
        ('note', 'cancer', 'Horehound leaf extract slowed colorectal cancer cells in the lab (preclinical)'),
    ],
    'matricaria_chamomilla': [
        ('drop', 'muscle-spasm'),   # EU monograph 'minor spasms' are gastrointestinal; gut antispasmodic is not muscle cramps (inv. 11)
        ('add', 'anxiety', ['REF-3629']), ('nulladd', 'anxiety', ['REF-2546']),
        ('note', 'anxiety', 'Chamomile extract reduced generalized anxiety symptoms in randomized trials and a meta-analysis; in a network meta-analysis it did not differ significantly from placebo'),
        ('add', 'depression', ['REF-1156']),
        ('note', 'depression', 'Chamomile extract reduced depression scores in people with generalized anxiety and depression in randomized trial analyses (exploratory)'),
        ('add', 'insomnia', ['REF-3629']),
        ('note', 'insomnia', 'Chamomile improved sleep quality, mainly fewer night awakenings, in meta-analyses of trials; sleep duration and efficiency did not improve'),
        ('add', 'inflammation', ['REF-3630']), ('nulladd', 'inflammation', ['REF-3527']), ('nulladd', 'skin-irritation', ['REF-3527']),
        ('note', 'inflammation', 'Traditional use for minor skin and mouth inflammation (' + CHAM_EU + '); a meta-analysis of randomized trials found anti-inflammatory effects; an extract was no better than its base cream for UV skin redness in one trial'),
        ('note', 'skin-irritation', 'Traditional use for minor skin inflammation such as sunburn (' + CHAM_EU + '); an extract was no better than its base cream for UV skin redness in a randomized trial'),
        ('add', 'pain', ['REF-2349', 'REF-2351']),
        ('note', 'pain', 'Chamomile eased period pain in trials (systematic review) and topical oil reduced painkiller use in knee osteoarthritis in a randomized trial'),
        ('add', 'blood-sugar', ['REF-3638']),
        ('note', 'blood-sugar', 'Chamomile tea improved blood sugar control in type 2 diabetes in randomized trials'),
        ('note', 'menstrual-cramps', 'Chamomile eased primary dysmenorrhoea pain in trials (systematic review)'),
        ('note', 'arthritis', 'Topical chamomile oil reduced painkiller use in knee osteoarthritis in a randomized trial, without improving WOMAC scores'),
        ('note', 'bloating', 'Traditional use for minor stomach and gut complaints such as bloating (' + CHAM_EU + ')'),
        ('note', 'indigestion', 'Traditional use for minor gastrointestinal complaints (' + CHAM_EU + ')'),
        ('note', 'wounds', 'Traditional use for superficial wounds (' + CHAM_EU + '); antimicrobial activity reported (review)'),
        ('newpair', 'menopause', ['REF-3631', 'REF-3632'], 'Chamomile eased menopausal symptoms vs placebo in two randomized trials (side effects were noted in one)'),
        ('newpair', 'hot-flashes', ['REF-3632'], 'Chamomile reduced hot flashes and other vasomotor symptoms in postmenopausal women in a randomized trial'),
        ('newpair', 'pms', ['REF-3633'], 'Chamomile extract relieved the emotional symptoms of PMS more than mefenamic acid in a randomized trial (physical symptoms did not differ)'),
        ('newpair', 'migraine', ['REF-3634'], 'A topical chamomile oleogel eased migraine pain, nausea and light sensitivity vs placebo in a randomized trial'),
        ('newpair', 'oral-health', ['REF-3635', 'REF-3636', 'REF-3637'], 'A chamomile mouthwash reduced plaque and gum bleeding vs placebo in gingivitis, and a chamomile gel reduced chemotherapy mouth sores (randomized trials; systematic review)'),
        ('newpair', 'back-pain', ['REF-3639'], 'Topical chamomile oil reduced non-specific low back pain in a randomized trial'),
    ],
}

NOTES = {
    'laurus_nobilis': 'Deep re-sweep. Bruising dropped: its only card was a rabbit wound-healing study (a wound is not a bruise; batch-1 rule). No trials on PubMed.',
    'hypericum_perforatum': 'Deep re-sweep batch 10 (cross-batch). Bruising dropped: inferred only from the vulnerary action (wound-healing review REF-1789, which does not name bruises) - a wound is not a bruise.',
    'lavandula_angustifolia': 'Deep re-sweep. REF-0265 (VOCC anxiolytic mechanism study) removed from five non-sedative actions. Held Silexan MA REF-2531 and herb NMA REF-2546 were never wired to a pair: new pairs (owner rule) anxiety (+ MAs REF-3609, REF-3610), depression (MA REF-3611, RCT REF-3612; inconclusive SR REF-2212 recorded as no-effect), stress (MA REF-3613), pain (SRs REF-3616, REF-3617). Sleep MAs REF-3614/REF-3615 added to insomnia; episiotomy SR REF-3617 to wounds. Not used: retracted burn-patient MA 36651329; underpowered post-dural-puncture headache RCT 33245709.',
    'lentinula_edodes': 'Deep re-sweep. REF-0315 (eritadenine anti-obesity observation, 1989) removed from all six actions (kept in references); REF-0293 (lentinan immunomodulator title) removed from antidiabetic, antimicrobial, antioxidant and antiviral. Daily-shiitake RCT REF-3640 added to immune-support; lentinan cancer MA REF-3641 and SR REF-3642 added to cancer.',
    'leonurus_cardiaca': 'Deep re-sweep. REF-0867 (PPAR-delta anti-obesity cell study) removed from cardiovascular-support; REF-0861 (pharmacology review, no skin claim) removed from skin-irritation. REF-0868 title corrected to its DOI/PubMed record (Mentha aquatica, Lavandula dentata and L. cardiaca). Not used: melatonin vs motherwort tincture study 17209457 (no placebo; motherwort effects "less pronounced"); postpartum haemorrhage MA 40527062 (Chinese motherwort injection, L. japonicus).',
    'linum_usitatissimum': 'Deep re-sweep. REF-0105 (stearidonic acid as an EPA surrogate - not flax) purged and deleted. New pairs (owner rule): high-blood-pressure (MAs REF-3618, REF-3619 + held RCT REF-3395), high-cholesterol (MAs REF-3620, REF-3621), blood-sugar (MAs REF-3622-REF-3624), constipation (RCTs REF-3627, REF-3628). Inflammation: 2024 MA REF-3625 support, 2016 CRP MA REF-3626 no-effect. Gap: hot flashes - flaxseed RCTs 21900849 and 20007337 were null and there is no hot-flash pair.',
    'lysimachia_vulgaris': 'Deep re-sweep. REF-2805 studies Lysimachia foenum-graecum, a different species - purged and deleted. Notes rewritten to their lab sources (all preclinical; REF-2796 states folk use for fever, ulcer, diarrhoea and wounds). No trials on PubMed.',
    'mahonia_aquifolium': 'Deep re-sweep. Herbal Reality REF-0488 page (herb/oregon-grape) checked 2026-11-12: names gout/rheumatism/arthritis, skin, mouth and intestinal infections, infected wounds, psoriasis, eczema and digestive support; lists references. Topical psoriasis MA REF-3643 and open-label atopic dermatitis trial REF-3644 added. Notes rewritten. Gap: digestion (traditional only, no pair).',
    'malva_sylvestris': 'Deep re-sweep. New pairs (owner rule): eczema (paediatric RCT REF-3645), oral-health (stomatitis RCT REF-3646, mouthwash RCT REF-3647, EU monograph oral irritation). Stomatitis RCT also added to pain. Notes state the null episiotomy RCT REF-1190. Gap: constipation - placebo-controlled flower-extract trial 25801702 does not state randomisation.',
    'marrubium_vulgare': 'Deep re-sweep. REF-0926 (rat lung fibrosis) removed from the expectorant action (still cited for respiratory-support); REF-0925 (antinociception) removed from antispasmodic (kept in references). Not used: Cecropia/Marrubium glucose trial 15636168 (no blood-sugar pair).',
    'matricaria_chamomilla': 'Deep re-sweep. Muscle-spasm dropped (EU monograph spasms are gastrointestinal; off-target). Anxiety: MA REF-3629 added, herb NMA REF-2546 (chamomile not significant vs placebo) no-effect. REF-1156 retagged rct and added to depression. UV-erythema RCT REF-3527 no-effect for inflammation and skin-irritation (batch-7 carry). Anti-inflammatory MA REF-3630, chamomile-tea RCT REF-3638 added. New pairs (owner rule): menopause (RCTs REF-3631, REF-3632), hot-flashes (REF-3632), pms (RCT vs mefenamic acid REF-3633), migraine (RCT REF-3634), oral-health (RCTs REF-3635, REF-3636 + SR REF-3637), back-pain (RCT REF-3639). Not used: saffron+chamomile combination 37427624; ginger/chamomile CINV trial 27644672 (conclusion is about ginger).',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 10', os.path.join(HERE, 'deep', 'd10_changes.tsv'), **BIB)
