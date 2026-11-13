"""Owner decisions 2026-11-13 (deep re-sweep follow-up). Run from the repo root.

1. Licorice: NO liver-support pair. The contraindication is rewritten to cite Health Canada's 2024
   NNHPD monograph (which lists "a kidney, liver or cardiovascular disorder", citing EMA 2012, ESCOP
   2003, Brinker 2010, Bradley 1992) and to give the mechanism (glycyrrhizin pseudoaldosteronism),
   so it no longer reads as a liver-toxicity warning.
2. Turmeric: NO liver-support pair; a rare-but-serious supplement liver-injury contraindication is added
   (Tuscany phytovigilance + SR of case reports; US DILIN series; 2025 histopathology series).
3. New condition `low-libido` split out of `fertility` (fertility's synonyms were libido/aphrodisiac).
   Fenugreek's only 'fertility' pair (a sexual-function RCT in men) is re-filed there; wild carrot gets
   a low-libido pair from its HSDD RCT, with the seed's anti-fertility warning in the note.
"""
import os, sys
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)

# ---- 1. vocabulary first (fixlib reads conditions.yaml at import) ----
VOC = 'vocabularies/conditions.yaml'
v = open(VOC, encoding='utf-8', newline='').read()
OLD = '''- id: fertility
  label: Fertility
  body_system: reproductive
  consumer_synonyms: ["libido", "aphrodisiac"]
'''
NEWV = '''- id: fertility
  label: Fertility
  body_system: reproductive
  consumer_synonyms: ["infertility", "trying to conceive", "conception"]
- id: low-libido
  related_actions: [aphrodisiac]
  label: Low libido
  body_system: reproductive
  consumer_synonyms: ["libido", "sexual desire", "low sex drive", "aphrodisiac", "sexual dysfunction"]
'''
if 'id: low-libido' not in v:
    assert OLD in v
    open(VOC, 'w', encoding='utf-8', newline='').write(v.replace(OLD, NEWV, 1))

import fixlib, deep_lib
import yamlsplice as Y
fixlib.DATE = '2026-11-13'

NEW = deep_lib.newrefs([
    ('REF-3649', '39079711', 'licoriceliverma', 'meta-analysis'),
    ('REF-3650', '11446888', 'glycyrrhizinpseudoaldo', 'clinical'),
    ('REF-3651', '32656820', 'turmerictuscanyliver', 'clinical'),       # phytovigilance cases + SR of case reports
    ('REF-3652', '36252717', 'turmericdilin', 'clinical'),
    ('REF-3653', '39381846', 'turmerichepatitisseries', 'clinical'),
    ('REF-3654', '33183662', 'carrotseedhsdd', 'rct'),
])
NEW['hclicorice2024'] = ('REF-3648', [
    ('author', 'Health Canada, Natural and Non-prescription Health Products Directorate'),
    ('title', 'Natural Health Product Monograph: Licorice - Glycyrrhiza glabra, Glycyrrhiza inflata, Glycyrrhiza uralensis'),
    ('year', '2024'),
    ('url', 'https://webprod.hc-sc.gc.ca/nhpid-bdipsn/dbImages/mono_licorice_english.pdf'),
    ('note', 'REF-3648'),
    ('study_type', 'traditional'),
    ('summary', 'Health Canada NNHPD single-ingredient monograph dated November 29, 2024. Uses: traditional expectorant for cough with upper respiratory infection/cold; relief of inflammatory conditions of the gastrointestinal tract such as gastritis. Contraindications: pregnancy; hypokalaemia, high blood pressure, or a kidney, liver or cardiovascular disorder (citing EMA 2012, Brinker 2010, ESCOP 2003, Bradley 1992); heart medications, corticosteroids, stimulant laxatives or other products contributing to electrolyte imbalance. Read 2026-11-13.'),
])
fixlib.bib_edit(new=NEW)


def edit(stem, fn, note):
    path = f'plants/{stem}.yaml'
    text, d = Y.load(path)
    import copy
    orig = copy.deepcopy(d)
    fn(d)
    changed = {k for k in set(d) | set(orig) if d.get(k) != orig.get(k)}
    Y.save(path, text, d, changed)
    fixlib.append_note(path, f'| {fixlib.DATE}: owner decisions (deep re-sweep) - ' + note)
    print(stem, sorted(changed))


LICORICE_CI = ('Glycyrrhizin in whole licorice root makes the body retain salt and water and lose potassium '
               '(pseudoaldosteronism), which can raise blood pressure and cause swelling and low potassium, '
               'especially with large doses or prolonged use. Do not use if you are pregnant or have low '
               'potassium, high blood pressure, or a kidney, liver or heart disorder, and do not combine with '
               'heart medicines, corticosteroids, stimulant laxatives or other products that can upset '
               'electrolytes (Health Canada; EMA). The liver warning is about these salt and potassium effects, '
               'not liver damage: in trials in liver disease the side effects were of this kind, and intravenous '
               'glycyrrhizin raised blood pressure in people with hepatitis C. Deglycyrrhizinated licorice (DGL) '
               'avoids this effect.')


def licorice(d):
    ci = d['contraindications'][0]
    assert ci['note'].startswith('Avoid prolonged use of whole licorice root'), ci['note'][:60]
    ci['note'] = LICORICE_CI
    ci['severity'] = 'warning'
    ci['reference_ids'] = ['REF-3648', 'REF-3649', 'REF-3650', 'REF-0308', 'REF-0012']


TURMERIC_CI = {
    'note': ('Rare but serious liver injury (acute hepatitis) has been reported with turmeric and curcumin '
             'supplements, mostly high-dose or high-absorption products, some combined with black pepper '
             '(piperine). Case series from Italy and the US describe dozens of cases; one US patient died, and '
             'most US cases carried the gene variant HLA-B*35:01. Liver tests usually returned to normal after '
             'the supplement was stopped. Culinary use has not been implicated.'),
    'severity': 'serious',
    'reference_ids': ['REF-3651', 'REF-3652', 'REF-3653'],
    'status': 'verified',
}


def turmeric(d):
    assert not any('HLA-B' in str(c.get('note', '')) for c in d['contraindications'])
    d['contraindications'].insert(0, TURMERIC_CI)


def fenugreek(d):
    i = [x for x in d['indications'] if x['condition'] == 'fertility']
    assert len(i) == 1
    i = i[0]
    i['condition'] = 'low-libido'
    i['reference_ids'] = ['REF-1116']
    i['note'] = 'A fenugreek seed extract (Testofen) improved sexual function and raised testosterone in healthy older men in a randomized trial'
    keys = list(i.keys())
    d['indications'][d['indications'].index(i)] = {k: i[k] for k in ['condition', 'note', 'reference_ids', 'status'] if k in i}


def carrot(d):
    assert not any(x['condition'] == 'low-libido' for x in d['indications'])
    d['indications'].append({
        'condition': 'low-libido',
        'note': ('Carrot seed improved sexual desire and function vs placebo in women with low sexual desire in a '
                 'randomized trial. The seed blocks pregnancy in animal studies and is a folk contraceptive - '
                 'avoid it when trying to conceive'),
        'reference_ids': ['REF-3654'],
        'status': 'verified',
    })


if __name__ == '__main__':
    snaps = {p: open(p, 'rb').read() for p in ['bibliography.bibtex'] + [f'plants/{s}.yaml' for s in
             ('glycyrrhiza_glabra', 'curcuma_longa', 'trigonella_foenum_graecum', 'daucus_carota')]}
    try:
        edit('glycyrrhiza_glabra', licorice,
             'Licorice liver-support NOT added (owner, 2026-11-13). The liver contraindication is real but is about '
             'pseudoaldosteronism, not hepatotoxicity: Health Canada 2024 NNHPD monograph REF-3648 ("kidney, liver or '
             'cardiovascular disorder", citing EMA 2012, ESCOP 2003, Brinker 2010, Bradley 1992); Duke 2002 says liver '
             'cirrhosis. Benefit evidence documented here only: NAFLD RCTs 22308054, 35785498; MA of 15 RCTs in liver disease '
             'REF-3649 (ALT -15.6, AST -7.4 U/L, mostly purified glycyrrhizic acid; side effects mineralocorticoid). '
             'Contraindication rewritten (severity caution -> warning), REF-0089 (history paper) dropped from it.')
        edit('curcuma_longa', turmeric,
             'Turmeric liver-support NOT added (owner, 2026-11-13): 2023 GRADE MA 37178581 (31 RCTs; ALT -4.1, AST -3.8 U/L; '
             'GGT ns; low/very-low certainty; authors: not necessarily clinically meaningful) and 2025 NAFLD MA 38213188 '
             '(ALT -4.1) vs rare idiosyncratic supplement hepatotoxicity. NEW serious contraindication: Tuscany '
             'phytovigilance 7 cases + SR of 23 case reports REF-3651; US DILIN 10 cases, 1 death, HLA-B*35:01 in 7 REF-3652; '
             '2025 histopathology series of 11 REF-3653. The record previously carried no liver-injury warning.')
        edit('trigonella_foenum_graecum', fenugreek,
             'Fertility pair re-filed to the new low-libido condition (owner, 2026-11-13: libido split out of fertility). '
             'Its evidence is a sexual-function RCT in men (Testofen, REF-1116). REF-0308 (WHO Monographs vol. 1) dropped from '
             'this pair: vol. 1 has no fenugreek monograph (fenugreek is in vol. 3) - the record\'s other REF-0308 citations '
             'are left for its deep re-sweep batch.')
        edit('daucus_carota', carrot,
             'New low-libido pair (owner, 2026-11-13): carrot-seed RCT in women with hypoactive sexual desire disorder REF-3654 '
             '(500 mg x3/day, 12 weeks; FSFI desire, arousal, lubrication, orgasm, satisfaction and pain improved vs placebo). '
             'Note carries the seed\'s anti-fertility / folk-contraceptive warning (REF-2724). Not filed under fertility.')
    except BaseException:
        for p, b in snaps.items():
            open(p, 'wb').write(b)
        raise
