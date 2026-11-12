"""Batch-11 fixes (2026-11-10 symptom audit): melissa .. ononis. Run from the repo root.
No new owner policy this batch; standing rules applied (null results incl. Cochrane, landmark null review
added per invariant 11, unverifiable books, compound papers, multi-product reviews, an RCT is cited only
for the outcome it measured, claim notes must match their sources)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

UNVER = 'removed from every symptom as unverifiable'
OOI_ABS = ("Momordica charantia (bitter gourd) is not only a nutritious vegetable but it is also used in traditional medical "
           "practices to treat type 2 diabetes mellitus. Experimental studies with animals and humans suggested that the "
           "vegetable has a possible role in glycaemic control. To assess the effects of mormodica charantia for type 2 "
           "diabetes mellitus. Several electronic databases were searched, among these were The Cochrane Library (Issue 1, "
           "2012), MEDLINE, EMBASE, CINAHL, SIGLE and LILACS (all up to February 2012), combined with handsearches. No "
           "language restriction was used. We included randomised controlled trials (RCTs) that compared momordica charantia "
           "with placebo or a control intervention, with or without pharmacological or non-pharmacological interventions. "
           "Two authors independently extracted data. Risk of bias of the trials was evaluated using the parameters of "
           "randomisation, allocation concealment, blinding, completeness of outcome data, selective reporting and other "
           "potential sources of bias. A meta-analysis was not performed given the quality of data and the variability of "
           "preparations of momordica charantia used in the interventions (no similar preparation was tested twice). Four "
           "randomised controlled trials with up to three months duration and investigating 479 participants met the "
           "inclusion criteria. Risk of bias of these trials (only two studies were published as a full peer-reviewed "
           "publication) was generally high. Two RCTs compared the effects of preparations from different parts of the "
           "momordica charantia plant with placebo on glycaemic control in type 2 diabetes mellitus. There was no "
           "statistically significant difference in the glycaemic control with momordica charantia preparations compared to "
           "placebo. When momordica charantia was compared to metformin or glibenclamide, there was also no significant "
           "change in reliable parameters of glycaemic control. No serious adverse effects were reported in any trial. No "
           "trial investigated death from any cause, morbidity, health-related quality of life or costs. There is "
           "insufficient evidence on the effects of momordica charantia for type 2 diabetes mellitus. Further studies are "
           "therefore required to address the issues of standardization and the quality control of preparations. For "
           "medical nutritional therapy, further observational trials evaluating the effects of momordica charantia are "
           "needed before RCTs are established to guide any recommendations in clinical practice.")

BIB = dict(
    retag={'REF-0100': 'systematic-review', 'REF-0413': 'narrative-review', 'REF-0412': 'narrative-review',
           'REF-0197': 'narrative-review', 'REF-0095': 'preclinical', 'REF-0032': 'narrative-review',
           'REF-0301': 'narrative-review', 'REF-1430': 'narrative-review', 'REF-0467': 'narrative-review'},
    new={'ooi2012momordica': ('REF-3396', [
        ('author', 'Ooi, C.P., Yassin, Z. and Hamid, T.A.'),
        ('title', 'Momordica charantia for type 2 diabetes mellitus'),
        ('journal', 'Cochrane Database of Systematic Reviews'), ('year', '2012'), ('number', '8'),
        ('pages', 'CD007845'), ('doi', '10.1002/14651858.CD007845.pub3'), ('pmid', '22895968'),
        ('note', 'REF-3396'), ('study_type', 'systematic-review'), ('abstract', OOI_ABS)])},
)

MEL10 = ('arthritis', 'bloating', 'cold', 'indigestion', 'infection', 'inflammation', 'insomnia', 'menstrual-cramps',
         'muscle-spasm', 'skin-irritation')
NONI12 = ('arthritis', 'back-pain', 'blood-sugar', 'cold', 'headache', 'immune-support', 'infection', 'inflammation',
          'metabolic-support', 'pain', 'skin-irritation', 'wounds')
NEP9 = ('arthritis', 'bloating', 'indigestion', 'infection', 'inflammation', 'insomnia', 'respiratory-support',
        'skin-irritation', 'wounds')

PLAN = {
    'melissa_officinalis': [('rm', c, ['REF-0112']) for c in MEL10]
      + [('rm', c, ['REF-0194']) for c in ('arthritis', 'cold', 'infection', 'inflammation', 'skin-irritation')]
      + [('rm', 'insomnia', ['REF-0134'])]
      + [('add', c, ['REF-3078']) for c in ('insomnia', 'bloating', 'indigestion')],
    'mentha_piperita': [('rm', c, ['REF-0100']) for c in ('bloating', 'indigestion', 'muscle-spasm')]
      + [('rm', 'cognitive-function', ['REF-3047', 'REF-3050']),
         ('note', 'pain', 'Enteric-coated peppermint oil relieved abdominal pain in irritable bowel syndrome and recurrent abdominal pain (review of 16 trials)'),
         ('note', 'cognitive-function', 'Peppermint extract inhibited acetylcholinesterase in vitro, a target in Alzheimer\'s disease (preclinical)')],
    'momordica_charantia': [('nulladd', 'blood-sugar', ['REF-3396']), ('nulladd', 'metabolic-support', ['REF-3396'])],
    'morinda_citrifolia': [('rm', c, ['REF-0197']) for c in NONI12]
      + [('rm', 'cold', ['REF-0110']), ('rm', 'infection', ['REF-0110']), ('add', 'cancer', ['REF-0110'])],
    'nepeta_cataria': [('rm', c, ['REF-0035']) for c in NEP9]
      + [('rm', 'bloating', ['REF-0095']), ('rm', 'indigestion', ['REF-0095', 'REF-0938'])],
    'ocimum_tenuiflorum': [('rm', 'anxiety', ['REF-0466', 'REF-1427']), ('rm', 'cold', ['REF-0466']),
                           ('rm', 'fatigue', ['REF-0466']), ('rm', 'memory', ['REF-0596']),
                           ('note', 'stress', 'Adaptogen for stress - a systematic review of human studies and an 8-week RCT (lower stress scores, better sleep quality)')],
    'oenothera_biennis': [('null', 'eczema', ['REF-0447', 'REF-1458', 'REF-2587']),
                          ('null', 'pms', ['REF-0446']), ('rm', 'pain', ['REF-1463']),
                          ('rm', 'skin-irritation', ['REF-0446']),
                          ('note', 'pain', 'Cyclical breast pain (mastalgia) - evening primrose oil reduced pain severity versus placebo in a trial; a 2024 review reports some benefit'),
                          ('note', 'pms', 'Cyclical breast pain (mastalgia) improved versus placebo in a trial; a 2024 review found no effect on premenstrual syndrome itself')],
    'olea_europaea': [('rm', c, ['REF-0032']) for c in ('cardiovascular-support', 'skin-irritation')]
      + [('rm', 'cardiovascular-support', ['REF-0299'])]
      + [('rm', c, ['REF-0301']) for c in ('arthritis', 'blood-sugar', 'inflammation', 'metabolic-support',
                                          'skin-irritation', 'wounds')]
      + [('add', 'metabolic-support', ['REF-1443'])],
    'ononis_arvensis': [('rm', c, ['REF-2748']) for c in ('urinary-support', 'kidney-support', 'skin-irritation')]
      + [('note', 'cardiovascular-support', 'An Ononis arvensis isoflavone glucoside inhibited platelet activation in vitro; its flavonoids were predicted to lower lipids in silico (preclinical)')],
}

NOTES = {
    'melissa_officinalis': 'REF-0112 (Hoffmann; unverifiable since batch 2) removed from 10 pairs. REF-0194 (Petersen 2003, "Rosmarinic acid" - a compound found across many Lamiaceae, not a lemon balm source) removed from 5 pairs. REF-0134 (Kennedy 2002 RCT) measured mood and cognition, not sleep - removed from insomnia (an RCT is cited only for what it measured). EU leaf monograph REF-3078 (mild symptoms of mental stress and to aid sleep; mild GI complaints including bloating and flatulence - EMA page 429, flagged for owner spot-check) added to insomnia, bloating, indigestion.',
    'mentha_piperita': 'REF-0100 (Grigoleit 2005, review of 16 IBS trials; retagged systematic-review) names IBS and recurrent abdominal pain only - removed from bloating, indigestion, muscle-spasm; kept for pain. REF-3047 (six Algerian Mentha species; M. arvensis the active one) and REF-3050 (CNS assays, no cognition named) removed from cognitive-function; REF-3049 (names Alzheimer\'s) kept. Note: no IBS pair exists for peppermint although IBS is its best-evidenced use (follow-up for the owner).',
    'momordica_charantia': 'Cochrane review REF-3396 (Ooi 2012, PubMed 22895968: no significant difference in glycaemic control vs placebo; "insufficient evidence") added and recorded in null_result_ids for blood-sugar and metabolic-support (landmark null review, invariant 11). REF-0413 (multi-plant diabetes review) is not an RCT - retagged.',
    'morinda_citrifolia': 'REF-0197 (Potterat 2007 Noni review; retagged) names no specific condition ("clinical data are essentially lacking") - removed from all 12 pairs. REF-0110 (noni polysaccharide, immunomodulatory antitumour activity in mice) removed from cold and infection, added to cancer.',
    'nepeta_cataria': 'REF-0035 (British Herbal Pharmacopoeia 1983, not available online) ' + UNVER + '. REF-0095 (spasmolytic and bronchodilatory oil; retagged preclinical) kept for respiratory-support only ("gastrointestinal disorders" is vague). REF-0938 (pharmacognosy: carminative, infantile colic) kept for bloating, removed from indigestion.',
    'ocimum_tenuiflorum': 'REF-0466 (Jamshidi 2017 SR) names metabolic, cardiovascular, immunity, neurocognition and psychological stress - removed from anxiety, cold and fatigue. REF-1427 (Holixer RCT) measured stress, mood and sleep, not anxiety - removed from anxiety. REF-0596 (cognition RCT) names no memory outcome - removed from memory.',
    'oenothera_biennis': 'Eczema: Cochrane REF-0447 ("further studies on EPO ... for eczema would be hard to justify"), Williams 2003 BMJ editorial REF-1458 and EAACI MA REF-2587 (evidence "remains limited") were cited AS SUPPORT - all moved to null_result_ids; pair dropped. REF-0446 (2024 SR) found EPO did not demonstrate effectiveness in premenstrual syndrome - moved to null for pms; it reports some results for mastalgia and hot flushes (kept). REF-1463 (EPO and borage oil, essential fatty acids in rheumatology) removed from pain. Claim notes rewritten.',
    'olea_europaea': 'REF-0032 (oleocanthal, olive-specific phenolic; compound evidence) kept for arthritis and inflammation only. REF-0299 (olive leaf RCT in T2D) names no cardiovascular outcome. REF-0301 (Waterman 2007 review) names blood pressure, LDL and antimicrobial activity against intestinal/respiratory pathogens - kept for cardiovascular, infection, cold; removed from 6 pairs. REF-1443 (RCT: insulin sensitivity in men at risk of metabolic syndrome) added to metabolic-support.',
    'ononis_arvensis': 'REF-2748 (Rezacova 1978, Czech pharmacognostic study; no abstract or text) ' + UNVER + '. Cardiovascular note corrected: it described PPAR-gamma anti-adipogenic work that neither cited study reports.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'batch 11', os.path.join(os.path.dirname(__file__), 'batch11_changes.tsv'), **BIB)

# Follow-up (2026-11-12): a source removed as UNVERIFIABLE must not survive as a mechanistic card on other pairs
# (mech_leak_check.py lists candidates; refs removed only for not naming a symptom stay valid as mechanistic cards).
FOLLOWUP = {
    'ononis_arvensis': [('mexcl', 'uti', ['REF-2748']), ('mexcl', 'swelling', ['REF-2748']),
                        ('note', 'wounds', 'inferred from antimicrobial action')],
    'lentinula_edodes': [('mexcl', 'cancer', ['REF-0293'])],
    'oenothera_biennis': [('note', 'eczema', 'inferred from emollient action; oral evening primrose oil showed no benefit for eczema in trials (see the no-effect studies)')],
}
FOLLOWUP_NOTES = {k: 'unverifiable source hidden from remaining mechanistic cards / claim note reset.' for k in FOLLOWUP}
