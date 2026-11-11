"""Batch-7 fixes (2026-11-10 symptom audit): eschscholzia .. gentiana. Run from the repo root.
Owner decision this batch (2026-11-11): "Ganoderma lucidum" in reishi/lingzhi literature counts for
Ganoderma lingzhi (the name was misapplied to the East Asian species; same logic as the cinnamon rule).
Standing rules applied: invariant 11 (superseded Cochrane Jin 2012 -> 2016 update), homeopathic
potencies are not evidence (Weleda/Wala Euphrasia D3 eye drops), multi-herb products are not sources,
"no consistent evidence" = null, bot-blocked monographs kept on their known indication text (flagged)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'

DRUMMOND_ABS = ("Antiinflammatory compounds in the diet can alleviate excessive inflammation, a factor in the pathogenesis "
                "of common diseases such as rheumatoid arthritis, atherosclerosis and diabetes. This study examined three "
                "European herbs, chamomile (Matricaria chamomilla), meadowsweet (Filipendula ulmaria L.) and willow bark "
                "(Salix alba L.), which have been traditionally used to treat inflammation and their potential for use as "
                "antiinflammatory agents. Aqueous herbal extracts and isolated polyphenolic compounds (apigenin, quercetin "
                "and salicylic acid, 0-100 μM) were incubated with THP1 macrophages, and interleukin (IL)-1β, IL-6 and "
                "tumour necrosis factor-alpha (TNF-α) were measured. At concentrations of 10 μM, both apigenin and quercetin "
                "reduced IL-6 significantly (p < 0.05). Apigenin at 10 μM and quercetin at 25 μM reduced TNF-α "
                "significantly (p < 0.05). Amongst the herbal extracts, willow bark had the greatest antiinflammatory "
                "activity at reducing IL-6 and TNF-α production. This was followed by meadowsweet and then chamomile. The "
                "lowest effective antiinflammatory concentrations were noncytotoxic (MTT mitochondrial activity assay). The "
                "Comet assay, which was used to study the protective effect of the isolated phenols against oxidative "
                "damage, showed positive results for all three polyphenols. These are the first findings that demonstrate "
                "the antiinflammatory capacity of these herbal extracts.")
BAO_ABS = ("Three polysaccharides, two heteroglycans (PL-1 and PL-4) and one glucan (PL-3), were solubilized from the fruit "
           "bodies of Ganoderma lucidum and isolated by anion-exchange and gel-filtration chromatography. Their structural "
           "features were elucidated by glycosyl residue and glycosyl linkage composition analyses, partial acid "
           "hydrolysis, acetolysis, periodate oxidation, 1D and 2D NMR spectroscopy, and ESI-MS experiments. The data "
           "obtained indicated that PL-1 had a backbone consisting of 1,4-linked alpha-D-glucopyranosyl residues and "
           "1,6-linked beta-D-galactopyranosyl residues with branches at O-6 of glucose residues and O-2 of galactose "
           "residues, composed of terminal glucose, 1,6-linked glucosyl residues and terminal rhamnose. PL-3 was a highly "
           "branched glucan composed of 1,3-linked beta-D-glucopyranosyl residues substituted at O-6 with 1,6-linked "
           "glucosyl residues. PL-4 was comprised of 1,3-, 1,4-, 1,6-linked beta-D-glucopyranosyl residues and 1,6-linked "
           "beta-D-mannopyranosyl residues. These polysaccharides enhanced the proliferation of T- and B-lymphocytes in "
           "vitro to varying contents and PL-1 exhibited an immune-stimulating activity in mice.")
WACHTEL_ABS = ("In Chinese, the name lingzhi represents a combination of spiritual potency and essence of immortality, and is "
               "regarded as the “herb of spiritual potency,” symbolizing success, well-being, divine power, and longevity. "
               "Among cultivated mushrooms, G. lucidum is unique in that its pharmaceutical rather than nutritional value "
               "is paramount. A variety of commercial G. lucidum products are available in various forms, such as "
               "powders, dietary supplements, and tea. These are produced from different parts of the mushroom, including "
               "mycelia, spores, and fruit body. The specific applications and attributed health benefits of lingzhi "
               "include control of blood glucose levels, modulation of the immune system, hepatoprotection, "
               "bacteriostasis, and more. The various beliefs regarding the health benefits of G. lucidum (Figure 9.2) are "
               "based largely on anecdotal evidence, traditional use, and cultural mores. However, recent reports provide "
               "scientific support to some of the ancient claims of the health benefits of lingzhi.")
JIN_ABS = ("Ganoderma lucidum is a natural medicine that is widely used and recommended by Asian physicians and naturopaths "
           "for its supporting effects on immune system. Laboratory research and a handful of preclinical trials have "
           "suggested that G. lucidum carries promising anticancer and immunomodulatory properties. The popularity of "
           "taking G. lucidum as an alternative medicine has been increasing in cancer patients. However, there is no "
           "systematic review that has been conducted to evaluate the actual benefits of G. lucidum in cancer treatment. "
           "To evaluate the clinical effects of G. lucidum on long-term survival, tumour response, host immune functions "
           "and quality of life in cancer patients, as well as adverse events associated with its use. We searched an "
           "extensive set of databases including the Cochrane Central Register of Controlled Trials (CENTRAL), MEDLINE, "
           "EMBASE, NIH, AMED, CBM, CNKI, CMCC and VIP Information/Chinese Scientific Journals Database was searched for "
           "randomised controlled trials (RCTs) in October 2011. Other strategies used were scanning the references of "
           "articles retrieved, handsearching of the International Journal of Medicinal Mushrooms and contact with herbal "
           "medicine experts and manufacturers of G. lucidum. For this update we updated the searches in February 2016. "
           "To be eligible for being included in this review, studies had to be RCTs comparing the efficacy of G. lucidum "
           "medications to active or placebo control in patients with cancer that had been diagnosed by pathology. All "
           "types and stages of cancer were eligible for inclusion. Trials were not restricted on the basis of language. "
           "Five RCTs met the inclusion criteria and were included in this review. Two independent review authors "
           "assessed the methodological quality of individual trials. Common primary outcomes were tumour response "
           "evaluated according to the World Health Organization (WHO) criteria, immune function parameters such as "
           "natural killer (NK)-cell activity and T-lymphocyte co-receptor subsets, and quality of life measured by the "
           "Karnofsky scale score. No trial had recorded long-term survival rates. Associated adverse events were reported "
           "in one study. A meta-analysis was performed to pool available data from the primary trials. Results were "
           "gauged using relative risks (RR) and standard mean differences (SMD) for dichotomous and continuous data "
           "respectively, with a 95% confidence interval (CI). The methodological quality of primary studies was "
           "generally unsatisfying and the results were reported inadequately in many aspects. Additional information was "
           "not available from primary trialists. The meta-analysis results showed that patients who had been given G. "
           "lucidum alongside with chemo/radiotherapy were more likely to respond positively compared to "
           "chemo/radiotherapy alone (RR 1.50; 95% CI 0.90 to 2.51, P = 0.02). G. lucidum treatment alone did not "
           "demonstrate the same regression rate as that seen in combined therapy. The results for host immune function "
           "indicators suggested that G. lucidum simultaneously increases the percentage of CD3, CD4 and CD8 by 3.91% (95% "
           "CI 1.92% to 5.90%, P < 0.01), 3.05% (95% CI 1.00% to 5.11%, P < 0.01) and 2.02% (95% CI 0.21% to 3.84%, P = "
           "0.03), respectively. In addition, leukocyte, NK-cell activity and CD4/CD8 ratio were marginally elevated. Four "
           "studies showed that patients in the G. lucidum group had relatively improved quality of life in comparison to "
           "controls. One study recorded minimal side effects, including nausea and insomnia. No significant "
           "haematological or hepatological toxicity was reported. Our review did not find sufficient evidence to justify "
           "the use of G. lucidum as a first-line treatment for cancer. It remains uncertain whether G. lucidum helps "
           "prolong long-term cancer survival. However, G. lucidum could be administered as an alternative adjunct to "
           "conventional treatment in consideration of its potential of enhancing tumour response and stimulating host "
           "immunity. G. lucidum was generally well tolerated by most participants with only a scattered number of minor "
           "adverse events. No major toxicity was observed across the studies. Although there were few reports of harmful "
           "effect of G. lucidum, the use of its extract should be judicious, especially after thorough consideration of "
           "cost-benefit and patient preference. Future studies should put emphasis on the improvement in methodological "
           "quality and further clinical research on the effect of G. lucidum on cancer long-term survival are needed. An "
           "update to this review will be performed every two years.")

BIB = dict(
    retag={'REF-0256': 'narrative-review', 'REF-0448': 'preclinical', 'REF-0062': 'preclinical',
           'REF-0537': 'narrative-review', 'REF-0298': 'narrative-review', 'REF-0019': 'preclinical',
           'REF-0580': 'narrative-review'},
    sets={  # verified against PubMed 2026-11-11
        'REF-0062': {'journal': 'Phytotherapy Research', 'doi': '10.1002/ptr.4753', 'pmid': '22711544',
                     'abstract': DRUMMOND_ABS},
        'REF-0019': {'author': 'Bao, X.F., Wang, X.S., Dong, Q., Fang, J.N. and Li, X.Y.',
                     'title': 'Structural features of immunologically active polysaccharides from Ganoderma lucidum',
                     'journal': 'Phytochemistry', 'year': '2002', 'volume': '59', 'number': '2', 'pages': '175--181',
                     'doi': '10.1016/s0031-9422(01)00450-2', 'pmid': '11809453', 'abstract': BAO_ABS},
        'REF-0298': {'url': 'https://www.ncbi.nlm.nih.gov/books/NBK92757/', 'pmid': '22593926',
                     'abstract': WACHTEL_ABS},
    },
    delete=['REF-0606',   # fixed combination (Crataegus + Eschscholzia + magnesium)
            'REF-0613',   # anthroposophic Euphrasia D3 eye drops (potentized = homeopathic)
            'REF-2173',   # Weleda Euphrasia D3 eye drops (homeopathic); primary outcome null anyway
            'REF-0125'],  # Cochrane 2012, superseded by the 2016 update REF-3394 (invariant 11)
    new={'jin2016ganoderma': ('REF-3394', [
        ('author', 'Jin, X., Ruiz Beguerie, J., Sze, D.M. and Chan, G.C.'),
        ('title', 'Ganoderma lucidum (Reishi mushroom) for cancer treatment'),
        ('journal', 'Cochrane Database of Systematic Reviews'), ('year', '2016'), ('volume', '4'),
        ('pages', 'CD007731'), ('doi', '10.1002/14651858.CD007731.pub3'), ('pmid', '27045603'),
        ('note', 'REF-3394'), ('study_type', 'systematic-review'), ('abstract', JIN_ABS)])},
)

FU_ALL = ('acid-reflux', 'arthritis', 'back-pain', 'headache', 'indigestion', 'infection', 'inflammation',
          'menstrual-cramps', 'muscle-spasm', 'pain', 'skin-irritation', 'swelling', 'urinary-support', 'uti', 'wounds')
GA_ALL = ('bruising', 'eczema', 'infection', 'skin-irritation', 'swelling', 'urinary-support', 'uti', 'wounds')

PLAN = {
    'eschscholzia_californica': [('purge', 'REF-0606')]
      + [('rm', c, ['REF-0427']) for c in ('back-pain', 'headache', 'stress')]
      + [('add', 'stress', ['REF-3099']), ('add', 'insomnia', ['REF-3099'])],
    'eucalyptus_globulus': [('rm', c, ['REF-0309']) for c in ('arthritis', 'immune-support', 'infection', 'inflammation',
                                                             'skin-irritation', 'wounds')]
      + [('rm', 'cold', ['REF-0256']), ('rm', 'wounds', ['REF-0256']),
         ('add', 'cold', ['REF-3083']), ('add', 'respiratory-support', ['REF-3083'])],
    'euphrasia_officinalis': [('purge', 'REF-2173'), ('purge', 'REF-0613')]
      + [('rm', c, ['REF-0449']) for c in ('arthritis', 'cough', 'diarrhea', 'fever', 'skin-irritation', 'wounds')]
      + [('rm', 'inflammation', ['REF-2581']), ('nulladd', 'eye-strain', ['REF-3084'])],
    'filipendula_ulmaria': [('rm', c, ['REF-0033']) for c in FU_ALL]
      + [('rm', c, ['REF-0098']) for c in FU_ALL if c not in ('swelling', 'urinary-support')]
      + [('rm', c, ['REF-0062']) for c in ('arthritis', 'back-pain', 'headache', 'pain', 'skin-irritation')]
      + [('add', 'arthritis', ['REF-3072']), ('add', 'pain', ['REF-3072'])],
    'filipendula_vulgaris': [('rm', 'arthritis', ['REF-2031']), ('rm', 'indigestion', ['REF-0815']),
                             ('rm', 'wounds', ['REF-2730', 'REF-2734']), ('rm', 'cognitive-function', ['REF-2738'])],
    'foeniculum_vulgare': [('rm', c, ['REF-0537']) for c in ('bronchitis', 'cough', 'wounds')]
      + [('null', 'menstrual-cramps', ['REF-2586']),
         ('add', 'menstrual-cramps', ['REF-3080']), ('add', 'cough', ['REF-3080']),
         ('add', 'respiratory-support', ['REF-3080'])],
    'galium_aparine': [('rm', c, ['REF-0035', 'REF-0113']) for c in GA_ALL]
      + [('add', 'wounds', ['REF-1720', 'REF-1725']), ('add', 'infection', ['REF-1720']),
         ('mexcl', 'bruising', ['REF-1720', 'REF-1725'])],
    'ganoderma_lingzhi': [('purge', 'REF-0125')]
      + [('rm', c, ['REF-0298']) for c in ('arthritis', 'cardiovascular-support', 'cold', 'inflammation', 'insomnia',
                                          'metabolic-support', 'skin-irritation')]
      + [('rm', 'cold', ['REF-0019']), ('rm', 'infection', ['REF-0019']),
         ('add', 'cancer', ['REF-3394']), ('add', 'immune-support', ['REF-3394'])],
    'gentiana_lutea': [('rm', 'bloating', ['REF-0453', 'REF-0580']), ('rm', 'indigestion', ['REF-0580'])],
}

NOTES = {
    'eschscholzia_californica': 'REF-0606 purged: the RCT tested a fixed combination (Crataegus + Eschscholzia + magnesium), not California poppy alone. REF-0427 (in vitro GABA-A) names sedative, anxiolytic and analgesic effects - removed from back-pain, headache, stress. EU monograph REF-3099 (relief of mild symptoms of mental stress and to aid sleep; EMA page 429 - flagged for owner spot-check) added to stress and insomnia.',
    'eucalyptus_globulus': 'REF-0309 (WHO vol. 2, Folium/Aetheroleum Eucalypti) kept for cold and respiratory-support per its known pharmacopoeial uses (symptomatic treatment of respiratory-tract catarrh/colds); WHO PDF blocks automated reading - flagged for owner spot-check; removed from 6 other pairs. REF-0256 (Sadlon 2010 review of eucalyptus oil, the E. globulus oil per invariant 10) names antimicrobial, immune-stimulatory, anti-inflammatory effects and bronchitis/asthma/COPD - removed from cold and wounds; retagged narrative-review. EU leaf monograph REF-3083 (relief of cough associated with cold; EMA page 429, flagged) added to cold and respiratory-support.',
    'euphrasia_officinalis': 'REF-2173 (Weleda Euphrasia eye drops = Euphrasia D3, cited as such in the trial references; primary outcome null, p=0.85) and REF-0613 (anthroposophic Euphrasia single-dose eye drops, a potentized preparation; E. rostkoviana) purged: homeopathic potencies are not evidence. EMA public statement REF-3084 (no monograph possible; efficacy undocumented, home eye applications not safe) recorded in null_result_ids for eye-strain. Herbal Reality REF-0449 (page read) names allergy/hay fever, catarrh/sinusitis, asthma, common cold, eye conditions incl. eyestrain, eye/nasal inflammation and infections - removed from arthritis, cough, diarrhea, fever, skin, wounds. REF-2581 (E. officinalis subsp. pratensis) names antimicrobial and antiproliferative activity only - removed from inflammation.',
    'filipendula_ulmaria': 'REF-0033 (Bridge 2008, The Herbal Remedy Handbook) ' + UNVER + '. Grieve (REF-0098, page read) names diarrhoea, stomach, strangury and dropsy, fevers - kept for urinary-support (strangury) and swelling (dropsy) only. REF-0062 (Drummond, PubMed 22711544, THP1 macrophages) names inflammation only; retagged preclinical, abstract and DOI added. EU monograph REF-3072 (supportive treatment of common cold; relief of minor articular pain - EMA page 429, flagged for owner spot-check) added to arthritis and pain.',
    'filipendula_vulgaris': 'F. hexapetala Gilib. = F. vulgaris (POWO synonym). REF-2031 (rat hyperalgesia) names pain only - removed from arthritis. REF-0815 (gastric-ulcer/anti-inflammatory models) is not indigestion evidence. REF-2730/REF-2734 (antimicrobial) removed from wounds. REF-2738 (brain mitochondria after hypoxia) removed from cognitive-function; REF-2736 (nootropic) remains.',
    'foeniculum_vulgare': 'REF-2586 (Cochrane 2016 dietary supplements for dysmenorrhoea): "no consistent evidence of effectiveness" for fennel vs placebo (MD -0.34, 95% CI -0.74 to 0.06) and no difference vs NSAIDs - moved to null_result_ids for menstrual-cramps. REF-0605 reports a fennel-specific positive estimate and stays. REF-0537 (Badgujar review; retagged narrative-review) names respiratory ailments, antimicrobial and antispasmodic activity - removed from bronchitis, cough, wounds. EU monograph REF-3080 (bitter fennel fruit: minor spasm with menstrual periods; expectorant in cough associated with cold - EMA page 429, flagged) added to menstrual-cramps, cough, respiratory-support.',
    'galium_aparine': 'REF-0035 (British Herbal Pharmacopoeia 1983, not available online) and REF-0113 (Hoffmann, Medical Herbalism; unverifiable per batches 2-3) ' + UNVER + '. REF-1720 (in vitro wound healing + antimicrobial) and REF-1725 (Quinlan 1883 BMJ, chronic ulcers) wired directly to wounds; REF-1720 to infection. Wound/ulcer papers are not bruise evidence (mechanistic cards hidden).',
    'ganoderma_lingzhi': 'Owner decision 2026-11-11: "Ganoderma lucidum" in reishi/lingzhi literature is the name long misapplied to East Asian G. lingzhi, so it counts for this record. REF-0125 (Cochrane 2012) purged - superseded by the 2016 update REF-3394 (PubMed 27045603; "could be administered as an alternative adjunct ... enhancing tumour response and stimulating host immunity"), added to cancer and immune-support. REF-0298 (Wachtel-Galor 2011 chapter; full text behind a reCAPTCHA, abstract read) names blood glucose control, immune modulation, hepatoprotection and bacteriostasis - kept for blood-sugar, immune-support, infection; removed from 7 pairs. REF-0019 metadata corrected to Bao 2002 Phytochemistry (PubMed 11809453; in vitro/mouse immune stimulation) - kept for immune-support only.',
    'gentiana_lutea': 'EU monograph REF-0453 (known indications: temporary loss of appetite; mild dyspeptic/gastrointestinal disorders - EMA page 429, flagged for owner spot-check) kept for appetite-loss and indigestion, removed from bloating. REF-0580 is a genus-level Gentiana review (Chinese species, prose-only attribution) - removed from bloating and indigestion; retagged narrative-review.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 7', os.path.join(os.path.dirname(__file__), 'batch07_changes.tsv'), **BIB)
