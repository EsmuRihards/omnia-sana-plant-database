"""Batch-6 fixes (2026-11-10 symptom audit): daucus .. equisetum-sylvaticum. Run from the repo root.
Owner decisions this batch (2026-11-11):
- a superseded review version is not cited; the current version is (Cochrane echinacea 2006 ->
  the 2014 update REF-0797, recorded as a no-effect result for cold);
- two landmark RCTs missing from the DB are added: Jawad 2012 (REF-3392, E. purpurea cold
  prevention, positive) and Schaffler 2013 (REF-3393, E. senticosus stress-related fatigue, null).
Bot-blocked monographs (EMA 429, WHO vol. 1) stay on the uses their known indication text names,
flagged for owner spot-check (batch-5 rule)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib

BIB = 'bibliography.bibtex'
UNVER = 'removed from every symptom as unverifiable'
LOCATE = 'could not be located (PubMed, Crossref, OpenAlex) - ' + UNVER

# ---------------------------------------------------------------- bibliography edits
RETAG = {
    'REF-0509': 'narrative-review', 'REF-0587': 'narrative-review', 'REF-0262': 'narrative-review',
    'REF-0727': 'narrative-review', 'REF-0618': 'narrative-review', 'REF-0803': 'narrative-review',
    'REF-0800': 'narrative-review', 'REF-0801': 'narrative-review', 'REF-2291': 'narrative-review',
    'REF-0403': 'preclinical', 'REF-0028': 'preclinical', 'REF-0292': 'clinical',
}
SET = {  # verified against PubMed 2026-11-11
    'REF-0041': {'year': '2014', 'journal': 'Evidence-Based Complementary and Alternative Medicine',
                 'volume': '2014', 'pages': '760683', 'pmid': '24723963'},
    'REF-0292': {'journal': 'Indian Journal of Biochemistry and Biophysics', 'pmid': '20361714'},
    'REF-0614': {'pmid': '11428178'},
    'REF-2362': {'pmid': '3009038'},
    'REF-0797': {'pmid': '24554461'},
}
DELETE = ['REF-0153',  # Cochrane 2006, superseded by the 2014 update REF-0797 (owner decision)
          'REF-0271']  # phantom: title, volume and pages match no paper by these authors

JAWAD_ABS = ("Objective. To investigate the safety (risk) and efficacy (benefit) of Echinacea purpurea extract in the "
             "prevention of common cold episodes in a large population over a 4-month period. Methods. 755 healthy "
             "subjects were allocated to receive either an alcohol extract from freshly harvested E. purpurea (95% herba "
             "and 5% root) or placebo. Participants were required to record adverse events and to rate cold-related "
             "issues in a diary throughout the investigation period. Nasal secretions were sampled at acute colds and "
             "screened for viruses. Results. A total of 293 adverse events occurred with Echinacea and 306 with placebo "
             "treatment. Nine and 10% of participants experienced adverse events, which were at least possibly related "
             "to the study drug (adverse drug reactions). Thus, the safety of Echinacea was noninferior to placebo. "
             "Echinacea reduced the total number of cold episodes, cumulated episode days within the group, and "
             "pain-killer medicated episodes. Echinacea inhibited virally confirmed colds and especially prevented "
             "enveloped virus infections (P < 0.05). Echinacea showed maximal effects on recurrent infections, and "
             "preventive effects increased with therapy compliance and adherence to the protocol. Conclusions. "
             "Compliant prophylactic intake of E. purpurea over a 4-month period appeared to provide a positive risk to "
             "benefit ratio.")
SCHAFFLER_ABS = ("Plant adaptogens are traditionally used for stress-related symptoms, but clinical evidence is "
                 "inconsistent. This trial explored the effects of 120 mg/day Eleutherococcus senticosus root extract "
                 "(ES), 2-day professional stress management training (SMT) and a combination of both (COM). 144 "
                 "participants suffering from asthenia and reduced working capacity related to chronic stress were "
                 "randomized to the treatments. Validated scales and tests were used to investigate cognitive "
                 "performance; feeling stressed; fatigue and exhaustion; alertness, restlessness and mood; quality of "
                 "life and sleep; physical complaints and activities; and physiological stress parameters including "
                 "cortisol awakening response (CAR), at baseline, after 2 and 8 weeks of treatment (German Clinical "
                 "Trials Register DRKS00000692). Almost all parameters improved significantly over time without group "
                 "differences. Significant differences were found in mental fatigue and restlessness, both in favor of "
                 "COM vs. ES. COM was not superior to SMT in any parameter at week 8. An attenuation of the CAR was seen "
                 "at week 2 without group differences. All treatments were well tolerated. Effects of adding ES to SMT "
                 "are, if any, negligible.")
NEW = {
    'jawad2012echinacea': ('REF-3392', [
        ('author', 'Jawad, M., Schoop, R., Suter, A., Klein, P. and Eccles, R.'),
        ('title', 'Safety and Efficacy Profile of Echinacea purpurea to Prevent Common Cold Episodes: '
                  'A Randomized, Double-Blind, Placebo-Controlled Trial'),
        ('journal', 'Evidence-Based Complementary and Alternative Medicine'), ('year', '2012'),
        ('volume', '2012'), ('pages', '841315'), ('doi', '10.1155/2012/841315'), ('pmid', '23024696'),
        ('note', 'REF-3392'), ('study_type', 'rct'), ('abstract', JAWAD_ABS)]),
    'schaffler2013eleutherococcus': ('REF-3393', [
        ('author', 'Schaffler, K., Wolf, O.T. and Burkart, M.'),
        ('title', 'No benefit adding Eleutherococcus senticosus to stress management training in stress-related '
                  'fatigue/weakness, impaired work or concentration, a randomized controlled study'),
        ('journal', 'Pharmacopsychiatry'), ('year', '2013'), ('volume', '46'), ('number', '5'),
        ('pages', '181--190'), ('doi', '10.1055/s-0033-1347178'), ('pmid', '23740477'),
        ('note', 'REF-3393'), ('study_type', 'rct'), ('abstract', SCHAFFLER_ABS)]),
}


def _span(lines, ref):
    """(start, end) line indexes of the entry whose note is `ref` (end = the closing '}' line)."""
    hit = [i for i, ln in enumerate(lines) if re.match(r'\s*note\s*=\s*\{' + ref + r'\}', ln)]
    assert len(hit) == 1, (ref, hit)
    s = hit[0]
    while not lines[s].startswith('@'):
        s -= 1
    e = hit[0]
    while lines[e] != '}':
        e += 1
    return s, e


def _field_line(k, v):
    return f'  {k:<8} = {{{v}}},' if len(k) <= 8 else f'  {k} = {{{v}}},'


def edit_bib():
    lines = open(BIB, encoding='utf-8', newline='').read().split('\n')
    for ref, st in RETAG.items():
        s, e = _span(lines, ref)
        idx = [i for i in range(s, e) if re.match(r'\s*study_type\s*=', lines[i])]
        assert len(idx) == 1, ref
        comma = ',' if lines[idx[0]].rstrip().endswith(',') else ''
        lines[idx[0]] = f'  study_type = {{{st}}}{comma}'
    for ref, fields in SET.items():
        for k, v in fields.items():
            s, e = _span(lines, ref)
            idx = [i for i in range(s, e) if re.match(r'\s*' + k + r'\s*=', lines[i])]
            if idx:
                comma = ',' if lines[idx[0]].rstrip().endswith(',') else ''
                lines[idx[0]] = _field_line(k, v)[:-1] + comma
            else:
                note = [i for i in range(s, e) if re.match(r'\s*note\s*=', lines[i])][0]
                lines.insert(note, _field_line(k, v))
    for ref in DELETE:
        s, e = _span(lines, ref)
        if e + 1 < len(lines) and lines[e + 1] == '':
            e += 1
        del lines[s:e + 1]
    for key, (ref, fields) in NEW.items():
        assert not any(re.match(r'\s*note\s*=\s*\{' + ref + r'\}', ln) for ln in lines), ref
        body = [f'@article{{{key},'] + [_field_line(k, v) for k, v in fields]
        body[-1] = body[-1][:-1]
        body += ['}', '']
        starts = [i for i, ln in enumerate(lines) if ln.startswith('@')]
        keys = [re.match(r'@\w+\{([^,]+),', lines[i]).group(1) for i in starts]
        pos = next((starts[j] for j, k in enumerate(keys) if k.lower() > key), len(lines))
        lines[pos:pos] = body
    open(BIB, 'w', encoding='utf-8', newline='').write('\n'.join(lines))


# ---------------------------------------------------------------- plant records
EQ_ALL = ('arthritis', 'back-pain', 'bruising', 'infection', 'inflammation', 'skin-irritation', 'swelling',
          'urinary-support', 'uti', 'wounds')
CARD_ALL = ('arthritis', 'bloating', 'cardiovascular-support', 'indigestion', 'infection', 'inflammation',
            'respiratory-support', 'skin-irritation', 'wounds')

PLAN = {
    'daucus_carota': [('rm', 'swelling', ['REF-2708']), ('rm', 'indigestion', ['REF-2708'])],
    'dioscorea_villosa': [('rm', c, ['REF-0528']) for c in ('back-pain', 'headache', 'skin-irritation')]
      + [('null', 'menopause', ['REF-0614'])],
    'echinacea_purpurea': [
        ('purge', 'REF-0153'), ('purge', 'REF-0271'),
        ('rm', 'arthritis', ['REF-0308']), ('rm', 'inflammation', ['REF-0308']),
        ('add', 'cold', ['REF-3392']), ('nulladd', 'cold', ['REF-0797']),
    ],
    'elettaria_cardamomum': [('rm', c, ['REF-0144']) for c in CARD_ALL]
      + [('rm', 'infection', ['REF-0028']), ('rm', 'wounds', ['REF-0028']),
         ('rm', 'bloating', ['REF-1669']), ('rm', 'indigestion', ['REF-1669']),
         ('rm', 'inflammation', ['REF-0292']),
         ('add', 'respiratory-support', ['REF-1668']), ('add', 'infection', ['REF-1668']),
         ('add', 'cardiovascular-support', ['REF-1668'])],
    'eleutherococcus_senticosus': [
        ('rm', 'cold', ['REF-0506', 'REF-0509', 'REF-0587']), ('add', 'cold', ['REF-2295']),
        ('rm', 'fatigue', ['REF-0509']), ('add', 'fatigue', ['REF-2295']),
        ('nulladd', 'fatigue', ['REF-3393']), ('mexcl', 'fatigue', ['REF-2291']),
        ('rm', 'immune-support', ['REF-0509']),
        ('rm', 'muscle-soreness', ['REF-0506', 'REF-0509', 'REF-0587']),
        ('mexcl', 'muscle-soreness', ['REF-2291', 'REF-2296']),
        ('add', 'stress', ['REF-2295']), ('nulladd', 'stress', ['REF-3393']),
        ('add', 'cognitive-function', ['REF-0587', 'REF-2295']),
    ],
    'elymus_repens': [('rm', 'swelling', ['REF-0437']), ('rm', 'uti', ['REF-0437', 'REF-0438']),
                      ('mexcl', 'urinary-support', ['REF-2563']), ('nulladd', 'urinary-support', ['REF-2563'])],
    'epilobium_parviflorum': [('rm', c, ['REF-0403']) for c in ('arthritis', 'skin-irritation', 'urinary-support', 'uti')]
      + [('rm', 'urinary-support', ['REF-0618']), ('rm', 'uti', ['REF-0618']),
         ('null', 'prostate-support', ['REF-0618']),
         ('add', 'prostate-support', ['REF-3075']), ('add', 'urinary-support', ['REF-3075'])],
    'equisetum_arvense': [('rm', c, ['REF-0262']) for c in EQ_ALL]
      + [('rm', 'swelling', ['REF-0041', 'REF-0083']), ('rm', 'uti', ['REF-0041', 'REF-0083'])],
}

NOTES = {
    'daucus_carota': 'REF-2708 (wild-carrot review) names antilithic, diuretic, carminative, antiseptic, anti-inflammatory uses and urinary calculus, cystitis, gout, prostatitis, cancer - removed from swelling (a diuretic is not swelling evidence) and indigestion (carminative = bloating; gastroprotective = ulcer models).',
    'dioscorea_villosa': 'REF-0614 (Komesaroff 2001 RCT, PubMed 11428178): wild yam cream showed no statistical difference from placebo and "little effect on menopausal symptoms" - moved to null_result_ids; menopause pair dropped. REF-0528 (rodent writhing/formalin/leukocyte models; background names joint pain and rheumatoid arthritis) kept for arthritis, pain, inflammation; removed from back-pain, headache, skin-irritation.',
    'echinacea_purpurea': 'REF-0153 (Cochrane 2006) purged: superseded by the 2014 update REF-0797 (owner decision 2026-11-11), which pools all Echinacea species and finds products "have not here been shown to provide benefits for treating colds" - recorded in null_result_ids for cold. REF-0271 purged as a phantom (title, volume and pages match no paper by Sharma/Schoop/Suter in PubMed, Crossref or OpenAlex). Jawad 2012 RCT (REF-3392, PubMed 23024696, 755 people, E. purpurea reduced cold episodes vs placebo) added to cold. REF-0308 (WHO vol. 1, Herba Echinaceae Purpureae) kept for cold, infection, immune-support, wounds, skin-irritation per its known Medicinal uses text (colds and respiratory/urinary infections via immune stimulation; externally wound healing and inflammatory skin conditions); removed from arthritis and inflammation. WHO PDF blocks automated reading - flagged for owner spot-check.',
    'elettaria_cardamomum': 'REF-0144 (Korikanthimath & Hiremath 2002, book chapter, likely agronomic) and REF-0028 (Bhilave 2013, no journal) ' + LOCATE + '. REF-1669 (rat gastric-ulcer models) names no bloating or indigestion. REF-0292 (Verma 2009, PubMed 20361714, stage-1 hypertension, 20 people, single arm) kept for cardiovascular only - it names no inflammation; retagged clinical. REF-1668 (Ashokkumar critical review) names asthma, teeth and gum infections and cardiac disorders as traditional uses - added to respiratory-support, infection, cardiovascular-support.',
    'eleutherococcus_senticosus': 'Full texts read (PMC): Todorova 2021 (REF-0506) names immune stimulation, memory, cognition, fatigue, stress; Kos 2025 (REF-0587) names stress resistance, fatigue, immunostimulation, antidiabetic, memory and cognitive function; Bleakney 2008 (REF-0509, abstract) names stressors only. None names colds or muscle soreness - removed there. REF-2295 (Russian clinical literature review) names fatigue (EMA asthenia), cognitive function, anti-stress effects and cold/influenza prophylaxis ("promising") - added to cold, fatigue, stress, cognitive-function. Schaffler 2013 RCT (REF-3393, PubMed 23740477: adding E. senticosus to stress training "negligible") recorded in null_result_ids for fatigue and stress. REF-2291 (Goulet 2005: rigorous studies show no endurance benefit) and REF-2296 (adipocyte lipolysis) hidden from muscle-soreness/fatigue mechanistic cards; muscle-soreness dropped.',
    'elymus_repens': 'EU monograph REF-0437 (EMA page 429 - known indication text: flushing of the urinary tract as an adjuvant in minor urinary complaints; flagged for owner spot-check) and ESCOP REF-0438 (page verified: "irritable bladder and other urinary tract disorders") kept for urinary-support only; removed from swelling and UTI (birch precedent). REF-2563 (rat study: A. repens infusion had no positive effect on urolithiasis risk factors) recorded in null_result_ids for urinary-support and hidden from its mechanistic cards.',
    'epilobium_parviflorum': 'REF-0403 (in vitro: E. coli growth, COX-1/2 inhibition; supports prostatitis/BPH use) kept for prostate-support, infection, inflammation; retagged preclinical. REF-0618 (genus review) concludes BPH in vivo studies are "not conclusive or too preliminary to draw a final conclusion" - moved to null_result_ids for prostate-support; removed from urinary-support and UTI. EU monograph REF-3075 (E. parviflorum named; lower urinary tract symptoms related to BPH - EMA page 429, flagged for owner spot-check) added to prostate-support and urinary-support.',
    'equisetum_arvense': 'REF-0262 (Sandhu 2010, Asian J Pharm Clin Res) - no abstract or text retrievable, ' + UNVER + '. REF-0041 (Carneiro 2014 RCT, PubMed 24723963; year corrected from 2016) shows a diuretic effect in healthy men - kept for urinary-support, removed from swelling and UTI. EU monograph REF-0083 (EMA page 429 - known indications: flushing of the urinary tract in minor urinary complaints; minor wounds) kept for urinary-support and wounds, removed from swelling and UTI; flagged for owner spot-check. REF-0727 (joint-disorders review naming E. arvense among plants tested in humans) kept for arthritis.',
}

if __name__ == '__main__':
    snap = open(BIB, 'rb').read()
    try:
        edit_bib()
        fixlib.main(PLAN, NOTES, 'batch 6', os.path.join(os.path.dirname(__file__), 'batch06_changes.tsv'))
    except BaseException:
        open(BIB, 'wb').write(snap)
        raise
