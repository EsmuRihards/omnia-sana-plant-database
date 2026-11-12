"""Batch-10 fixes (2026-11-10 symptom audit): laurus .. matricaria. Run from the repo root.
Owner decision this batch (2026-11-12): a 10% Mahonia aquifolium cream (Releva) counts as plant
evidence even though it is registered as a homeopathic product - a 10% extract is mother-tincture
strength, not a serial dilution; labelled in the note. Standing rules otherwise."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'
PAN_ABS = ("Flaxseed consumption has been shown to improve blood lipids in humans and flaxseed-derived lignan has been shown "
           "to enhance glycemic control in animals. The study aimed to investigate the effect of a flaxseed-derived lignan "
           "supplement on glycemic control, lipid profiles and insulin sensitivity in type 2 diabetic patients. This was a "
           "randomized, double-blind, placebo-controlled, cross-over trial and it was conducted between April and December "
           "2006 in Shanghai, China. Seventy-three type 2 diabetic patients with mild hypercholesterolemia were enrolled into "
           "the study. Patients were randomized to supplementation with flaxseed-derived lignan capsules (360 mg lignan per "
           "day) or placebo for 12 weeks, separated by an 8-week wash-out period. HbA1c, lipid profiles, insulin resistance "
           "index and inflammatory factors were measured. Sixty-eight completed the study and were included in the analyses. "
           "The lignan supplement significantly improved glycemic control as measured by HbA(1c) (-0.10+/-0.65 % vs. "
           "0.09+/-0.52 %, P = 0.001) compared to placebo; however, no significant changes were observed in fasting glucose "
           "and insulin concentrations, insulin resistance and blood lipid profiles. Urinary excretion of lignan metabolites "
           "(enterodiol and enterolactone) was significantly higher after the lignan supplement intervention compared to "
           "baseline (14.2+/-18.1 vs. 1.2+/-2.4 microg/mL, P<0.001). Data also suggested minimal competition between lignan "
           "and isoflavones for bioavailability when measured by the excretion concentrations. Daily lignan supplementation "
           "resulted in modest, yet statistically significant improvements in glycemic control in type 2 diabetic patients "
           "without apparently affecting fasting glucose, lipid profiles and insulin sensitivity. Further studies are needed "
           "to validate these findings and explore the efficacy of lignans on type 2 diabetes. ClinicalTrials.gov NCT00363233.")

BIB = dict(
    retag={'REF-0043': 'narrative-review', 'REF-0265': 'preclinical', 'REF-0860': 'narrative-review',
           'REF-0861': 'narrative-review', 'REF-0001': 'narrative-review', 'REF-0039': 'narrative-review',
           'REF-0541': 'narrative-review', 'REF-0542': 'narrative-review', 'REF-0921': 'narrative-review',
           'REF-0280': 'narrative-review', 'REF-0300': 'narrative-review'},
    sets={'REF-0190': {'year': '2007', 'journal': 'PLoS One', 'volume': '2', 'number': '11', 'pages': 'e1148',
                       'doi': '10.1371/journal.pone.0001148', 'pmid': '17987126', 'abstract': PAN_ABS}},
)

LAV9 = ('arthritis', 'eczema', 'infection', 'inflammation', 'insomnia', 'menstrual-cramps', 'muscle-spasm',
        'skin-irritation', 'wounds')
LEO7 = ('arthritis', 'cardiovascular-support', 'inflammation', 'insomnia', 'menstrual-cramps', 'muscle-spasm',
        'skin-irritation')
CHA15 = ('arthritis', 'back-pain', 'bloating', 'bruising', 'eczema', 'headache', 'indigestion', 'infection',
         'inflammation', 'insomnia', 'menstrual-cramps', 'muscle-spasm', 'pain', 'skin-irritation', 'wounds')

PLAN = {
    'lavandula_angustifolia': [('rm', c, ['REF-0043', 'REF-0155']) for c in LAV9]
      + [('rm', 'insomnia', ['REF-0265']), ('add', 'insomnia', ['REF-3071']),
         ('note', 'insomnia', 'EU traditional use to aid sleep and relieve mild mental stress and exhaustion')],
    'lentinula_edodes': [('rm', c, ['REF-0293']) for c in ('cold', 'immune-support', 'infection')]
      + [('rm', c, ['REF-0315']) for c in ('cardiovascular-support', 'metabolic-support')],
    'leonurus_cardiaca': [('rm', c, ['REF-0198', 'REF-0270']) for c in LEO7]
      + [('rm', 'insomnia', ['REF-0864']), ('add', 'menstrual-cramps', ['REF-0860'])]
      + [('add', c, ['REF-0861']) for c in ('insomnia', 'inflammation', 'skin-irritation')],
    'linum_usitatissimum': [
        ('note', 'cardiovascular-support', 'Flaxseed lowered blood pressure in people with hypertension (review of trials); its lignan SDG is linked to lower lipids and blood pressure'),
        ('note', 'metabolic-support', 'A flaxseed lignan (SDG) supplement modestly improved HbA1c in type 2 diabetes (RCT); lignan reviews report lower lipids and glucose - compound evidence'),
        ('note', 'inflammation', 'Flax lignan (SDG) metabolites reduce oxidative stress and inflammation (review) - compound evidence')],
    'lysimachia_vulgaris': [('add', 'wounds', ['REF-2796']), ('rm', 'inflammation', ['REF-2795']),
                            ('add', 'inflammation', ['REF-2796']), ('rm', 'high-cholesterol', ['REF-2797']),
                            ('rm', 'metabolic-support', ['REF-2794', 'REF-2797']), ('add', 'liver-support', ['REF-2797'])],
    'mahonia_aquifolium': [('add', 'arthritis', ['REF-0488']),
        ('note', 'psoriasis', 'Topical 10% Mahonia aquifolium cream reduced plaque severity in mild-to-moderate psoriasis (double-blind placebo-controlled RCT and other trials; the cream is registered in the US as a homeopathic product but is a 10% plant extract)')],
    'malva_sylvestris': [('rm', c, ['REF-0541', 'REF-0542']) for c in ('arthritis', 'back-pain', 'bruising', 'headache')]
      + [('rm', 'wounds', ['REF-0542']), ('null', 'pain', ['REF-1190']), ('null', 'wounds', ['REF-1190']),
         ('rm', 'skin-irritation', ['REF-0480']), ('add', 'cough', ['REF-0542'])],
    'marrubium_vulgare': [('rm', 'bronchitis', ['REF-0468', 'REF-0469']), ('rm', 'cough', ['REF-0469', 'REF-0921'])]
      + [('add', c, ['REF-0469']) for c in ('bloating', 'appetite-loss', 'indigestion')]
      + [('note', 'cough', 'EU traditional use as an expectorant in cough associated with a cold')],
    'matricaria_chamomilla': [('rm', c, ['REF-0112', 'REF-0189']) for c in CHA15]
      + [('rm', c, ['REF-0280']) for c in ('back-pain', 'bloating', 'bruising', 'eczema', 'headache', 'indigestion',
                                          'infection', 'skin-irritation', 'menstrual-cramps')]
      + [('rm', 'eczema', ['REF-0079']), ('rm', 'infection', ['REF-0079'])],
}

NOTES = {
    'lavandula_angustifolia': 'REF-0043 (Cavanagh 2002, oils of four Lavandula species, "data still inconclusive") is a genus-level review and REF-0155 (Lis-Balchin, Lavender: The Genus Lavandula, book) is unverifiable and genus-level - both removed from all 9 pairs. REF-0265 (Schuwald 2013) is a mechanism study of anxiolytic action, not an RCT (retagged preclinical) - removed from insomnia. EU flower monograph REF-3071 (relief of mild symptoms of mental stress and exhaustion and to aid sleep - EMA page 429, flagged for owner spot-check) added to insomnia; REF-0858 stays in null_result_ids.',
    'lentinula_edodes': 'REF-0293 (Vethanayagam 1996, "Lentinan - a novel immunomodulator") and REF-0315 (Yokota 1989, eritadenine observatory trial) could not be located in PubMed - ' + UNVER + '. REF-0300 (multi-mushroom review) retagged narrative-review.',
    'leonurus_cardiaca': 'REF-0198 (Prajapati, A Handbook of Medicinal Plants) ' + UNVER + '; REF-0270 (Shang 2014, "The genus Leonurus", mostly L. japonicus) is genus-level - both removed. L. cardiaca reviews wired where they name the use: REF-0860 (cardiotonic; dysmenorrhoea, amenorrhoea) -> menstrual-cramps; REF-0861 (nervous heart conditions; sedative effects in clinical trials; wounds and skin inflammations) -> insomnia, inflammation, skin-irritation. REF-0864 (anxiolytic in animals) removed from insomnia.',
    'linum_usitatissimum': 'REF-0190 metadata corrected: it is Pan 2007 PLoS One 2:e1148 (PubMed 17987126); the stored DOI pointed to an unrelated nucleosome paper. Lignan (SDG) evidence labelled as compound evidence in the notes. REF-0001 and REF-0039 are narrative reviews (were tagged clinical/rct).',
    'lysimachia_vulgaris': 'var. davurica is listed as a synonym on this record. REF-2796 (Turkish L. vulgaris: folk use for fever, ulcer, diarrhoea and wounds; anti-inflammatory activity; antibacterial) added to wounds and inflammation. REF-2795 (IBS-D mouse model) names no inflammation. REF-2797 (hepatic lipogenesis, fatty liver) moved from high-cholesterol/metabolic to liver-support; REF-2794 (NASH) removed from metabolic-support.',
    'mahonia_aquifolium': 'Owner decision 2026-11-12: Releva (10% M. aquifolium cream, US homeopathic registration) counts as plant evidence - labelled in the psoriasis note. Herbal Reality REF-0488 (page read) names gout, rheumatism and arthritis - added to arthritis.',
    'malva_sylvestris': 'REF-1190 (episiotomy RCT): "No significant statistical differences ... in perineal healing (P=0.89) and pain scores (P=0.56)" - moved to null_result_ids for pain and wounds. REF-0541 (names inflammation, menstrual pains, analgesic and wound-healing activity) and REF-0542 (names cough, cold, diarrhoea, antinociceptive, anti-inflammatory, antimicrobial) removed from arthritis, back-pain, bruising, headache; REF-0542 removed from wounds, added to cough. EU monograph REF-0480 (oral or pharyngeal irritation and associated dry cough; mild gastrointestinal discomfort - EMA page 429, flagged) removed from skin-irritation.',
    'marrubium_vulgare': 'EU monograph REF-0468 (expectorant in cough associated with cold; mild dyspeptic complaints such as bloating and flatulence; temporary loss of appetite - EMA page 429, flagged) removed from bronchitis. ESCOP REF-0469 (page read: dyspeptic complaints such as bloating and flatulence, lack of appetite, catarrh of the upper respiratory tract) removed from bronchitis and cough, added to bloating, appetite-loss, indigestion. REF-0921 (critical review "More of a myth than a reality?") names bronchitis, colds, asthma, lack of appetite and dyspepsia as traditional uses - removed from cough; retagged.',
    'matricaria_chamomilla': 'REF-0112 (Hoffmann, Medical Herbalism; unverifiable since batch 2) and REF-0189 (Padula 2006, "Chamomile: industrial profiles"; not locatable) ' + UNVER + '. REF-0280 (Srivastava 2010 review; lumps German and Roman chamomile, counts for M. chamomilla per the type-species rule) names hay fever, inflammation, muscle spasms, insomnia, ulcers, wounds, rheumatic pain, haemorrhoids - removed from 9 pairs (incl. menstrual-cramps: "menstrual disorders" is vague) and retagged. EU monograph REF-0079 (minor GI complaints such as bloating and minor spasms; common cold; mouth and throat inflammation; minor skin inflammation, superficial wounds - EMA page 429, flagged) removed from eczema and infection.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 10', os.path.join(os.path.dirname(__file__), 'batch10_changes.tsv'), **BIB)

# Follow-up (2026-11-12): flaxseed. The Natural Standard review REF-2217 concludes the literature "does not support
# recommendation for any condition" (null); two positive sources already in the DB were not cited; the FLAX-PAD RCT
# (landmark, invariant 11) was missing.
RODRIGUEZ_ABS = ("Flaxseed contains ω-3 fatty acids, lignans, and fiber that together may provide benefits to patients with "
                 "cardiovascular disease. Animal work identified that patients with peripheral artery disease may particularly "
                 "benefit from dietary supplementation with flaxseed. Hypertension is commonly associated with peripheral "
                 "artery disease. The purpose of the study was to examine the effects of daily ingestion of flaxseed on "
                 "systolic (SBP) and diastolic blood pressure (DBP) in peripheral artery disease patients. In this "
                 "prospective, double-blinded, placebo-controlled, randomized trial, patients (110 in total) ingested a variety "
                 "of foods that contained 30 g of milled flaxseed or placebo each day over 6 months. Plasma levels of the ω-3 "
                 "fatty acid α-linolenic acid and enterolignans increased 2- to 50-fold in the flaxseed-fed group but did not "
                 "increase significantly in the placebo group. Patient body weights were not significantly different between "
                 "the 2 groups at any time. SBP was ≈ 10 mm Hg lower, and DBP was ≈ 7 mm Hg lower in the flaxseed group "
                 "compared with placebo after 6 months. Patients who entered the trial with a SBP ≥ 140 mm Hg at baseline "
                 "obtained a significant reduction of 15 mm Hg in SBP and 7 mm Hg in DBP from flaxseed ingestion. The "
                 "antihypertensive effect was achieved selectively in hypertensive patients. Circulating α-linolenic acid "
                 "levels correlated with SBP and DBP, and lignan levels correlated with changes in DBP. In summary, flaxseed "
                 "induced one of the most potent antihypertensive effects achieved by a dietary intervention.")
FOLLOWUP_BIB = dict(new={'rodriguezleyva2013flaxseed': ('REF-3395', [
    ('author', 'Rodriguez-Leyva, D., Weighell, W., Edel, A.L., LaVallee, R., Dibrov, E., Pinneker, R. and others'),
    ('title', 'Potent antihypertensive action of dietary flaxseed in hypertensive patients'),
    ('journal', 'Hypertension'), ('year', '2013'), ('volume', '62'), ('number', '6'), ('pages', '1081--1089'),
    ('doi', '10.1161/HYPERTENSIONAHA.113.02094'), ('pmid', '24126178'), ('note', 'REF-3395'),
    ('study_type', 'rct'), ('abstract', RODRIGUEZ_ABS)])})
FOLLOWUP = {'linum_usitatissimum': [
    ('nulladd', 'cardiovascular-support', ['REF-2217']), ('nulladd', 'metabolic-support', ['REF-2217'])]
    + [('mexcl', c, ['REF-2217']) for c in ('arthritis', 'bloating', 'indigestion', 'inflammation', 'skin-irritation')]
    + [('add', 'cardiovascular-support', ['REF-3395']), ('add', 'metabolic-support', ['REF-2221']),
       ('add', 'cancer', ['REF-0288'])]}
FOLLOWUP_NOTES = {'linum_usitatissimum': 'REF-2217 (Natural Standard 2007: the literature "does not support recommendation for any condition at this time") recorded in null_result_ids for cardiovascular- and metabolic-support and hidden from other mechanistic cards. FLAX-PAD RCT (Rodriguez-Leyva 2013, REF-3395, PubMed 24126178: 30 g milled flaxseed lowered SBP ~10 mmHg vs placebo over 6 months) added to cardiovascular-support. Already-held positive sources wired: REF-2221 (2024 MA: body weight, BMI, waist) -> metabolic-support; REF-0288 (RCT: tumour markers in breast cancer) -> cancer.'}
# run: python -c "import sys; sys.path.insert(0,'docs/audits/2026-11-10-symptom-audit'); import fix_batch10 as f, fixlib; fixlib.main_with_bib(f.FOLLOWUP, f.FOLLOWUP_NOTES, 'batch 10', 'docs/audits/2026-11-10-symptom-audit/batch10_followup_changes.tsv', **f.FOLLOWUP_BIB)"
