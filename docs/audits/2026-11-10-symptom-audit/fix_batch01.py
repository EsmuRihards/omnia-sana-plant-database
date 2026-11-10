"""Batch-1 fixes (2026-11-10 symptom audit). Owner rules applied:
  * a study that finds no effect is never evidence -> null_result_ids
  * a general source must name the symptom (or a close pharmacological equivalent)
  * multi-herb products, compound-only papers with no species named, and taxa POWO
    places in another species are not sources for this plant
Ops: rm (remove direct ref; auto-exclude from Mechanistic basis), rmk (remove, keep as
mechanistic card), add, null, mexcl, drop, purge (ref out of the whole record).
Run from the repo root: python docs/audits/2026-11-10-symptom-audit/fix_batch01.py
"""
import os, sys, yaml
sys.path.insert(0, os.path.dirname(__file__))
import yamlsplice as Y

DATE = '2026-11-10'
V = yaml.safe_load(open('vocabularies/conditions.yaml', encoding='utf-8'))
VC = V['conditions'] if isinstance(V, dict) and 'conditions' in V else V
REL = {c['id']: c.get('related_actions', []) for c in VC}

PLAN = {
    'achillea_millefolium': [
        ('purge', 'REF-2822'),  # genus-level review, its own experiments are A. coarctata
        ('rm', 'appetite-loss', ['REF-0369']),
        ('rm', 'arthritis', ['REF-0011']),
        ('rm', 'bloating', ['REF-0369']),
        ('rm', 'bruising', ['REF-0011', 'REF-0098', 'REF-0369', 'REF-0372']),
        ('rm', 'cold', ['REF-0369']), ('add', 'cold', ['REF-0098']),
        ('rm', 'diarrhea', ['REF-0369', 'REF-0373']),
        ('rm', 'fever', ['REF-0369']), ('add', 'fever', ['REF-0098']),
        ('rm', 'heavy-bleeding', ['REF-0369', 'REF-0381']), ('add', 'heavy-bleeding', ['REF-0098']),
        ('rm', 'indigestion', ['REF-0369']),
        ('rm', 'infection', ['REF-0098']),
        ('rm', 'inflammation', ['REF-0011', 'REF-0098']), ('add', 'inflammation', ['REF-0369']),
        ('rm', 'menstrual-cramps', ['REF-0011', 'REF-0098']),
        ('rm', 'muscle-spasm', ['REF-0011', 'REF-0098']),
        ('rm', 'skin-irritation', ['REF-0098']),
        ('rm', 'swelling', ['REF-0011', 'REF-0098']),
        ('rm', 'urinary-support', ['REF-0011', 'REF-0098']),
        ('rm', 'uti', ['REF-0011', 'REF-0098']),
    ],
    'acorus_calamus': [
        ('purge', 'REF-0516'), ('purge', 'REF-2825'), ('purge', 'REF-2827'),  # Acorus verus (POWO)
        ('purge', 'REF-2824'),  # beta-asarone only, no source species named
        ('rm', 'anxiety', ['REF-0624']),
        ('rm', 'cognitive-function', ['REF-0624']), ('add', 'cognitive-function', ['REF-0716']),
        ('rm', 'memory', ['REF-0624']), ('add', 'memory', ['REF-0716']),
        ('rm', 'nervous-tension', ['REF-0624']),
        ('rm', 'stress', ['REF-0624']),
    ],
    'actaea_racemosa': [
        ('purge', 'REF-0671'),  # 3-ingredient product (black cohosh + soy + SDG lignans)
        ('drop', 'anxiety'), ('drop', 'depression'),
        ('null', 'hot-flashes', ['REF-0623', 'REF-0672', 'REF-0673']),
        ('null', 'menopause', ['REF-0623', 'REF-0672', 'REF-0673']),
        ('rm', 'hot-flashes', ['REF-2400', 'REF-2589']),
        ('rm', 'menopause', ['REF-2400']),
        ('rm', 'cancer', ['REF-2830', 'REF-2831']),
    ],
    'aegopodium_podagraria': [
        ('purge', 'REF-0168'),  # Moerman's NAEB has no Aegopodium record
        ('rm', 'headache', ['REF-0098']),
        ('rm', 'skin-irritation', ['REF-0098']),
        ('rm', 'urinary-support', ['REF-0098']),
        ('rm', 'uti', ['REF-0098']),
    ],
    'aesculus_hippocastanum': [
        ('purge', 'REF-0678'),  # venoactive-drug review that never names horse chestnut
        ('purge', 'REF-2832'), ('purge', 'REF-2833'), ('purge', 'REF-2834'),  # escin, species unnamed
        ('rm', 'arthritis', ['REF-0590', 'REF-0676']),
        ('rm', 'hemorrhoids', ['REF-0590']),
        ('rm', 'skin-irritation', ['REF-0590']), ('mexcl', 'skin-irritation', ['REF-2405']),
    ],
    'agrimonia_eupatoria': [
        ('rm', 'appetite-loss', ['REF-0387', 'REF-0681']),
        ('rm', 'arthritis', ['REF-0386', 'REF-0387', 'REF-0680', 'REF-0681', 'REF-0683']),
        ('rm', 'bloating', ['REF-0387', 'REF-0681']),
        ('rm', 'bruising', ['REF-0386', 'REF-0681', 'REF-0682', 'REF-0683']),
        ('rm', 'diarrhea', ['REF-0681']),
        ('rm', 'indigestion', ['REF-0387', 'REF-0681']), ('rmk', 'indigestion', ['REF-0684']),
        ('rm', 'inflammation', ['REF-0680', 'REF-0682', 'REF-0683']),
        ('rm', 'skin-irritation', ['REF-0681']),
        ('rm', 'sore-throat', ['REF-0681', 'REF-0683']),
        ('rm', 'wounds', ['REF-0681']),
    ],
    'alchemilla_vulgaris': [
        ('rm', c, ['REF-0113']) for c in ('arthritis', 'bruising', 'inflammation', 'menstrual-cramps',
                                          'skin-irritation', 'wounds')
    ] + [('mexcl', c, ['REF-2227']) for c in ('arthritis', 'inflammation', 'skin-irritation')],
    'allium_sativum': [
        ('rm', c, ['REF-0166']) for c in ('arthritis', 'blood-sugar', 'cardiovascular-support', 'cold',
                                          'immune-support', 'infection', 'inflammation',
                                          'metabolic-support', 'skin-irritation', 'wounds')
    ] + [
        ('rm', 'metabolic-support', ['REF-0204']),
        ('rmk', 'wounds', ['REF-0650']), ('rm', 'wounds', ['REF-0651']),
    ],
    'aloe_vera': [
        ('purge', 'REF-2845'), ('purge', 'REF-2847'),  # aloe-emodin isolated from rhubarb
        ('purge', 'REF-2846'), ('purge', 'REF-2848'),  # aloe-emodin, no source species named
        ('add', 'wounds', ['REF-2241', 'REF-2238', 'REF-2243']),
        ('add', 'eczema', ['REF-2234']),
        ('add', 'skin-irritation', ['REF-2234', 'REF-2243']),
        ('drop', 'bruising'),  # only wound-healing papers, no bruising evidence
    ],
    'aloysia_citrodora': [
        ('rm', 'indigestion', ['REF-0474']),
        ('rm', 'inflammation', ['REF-0474']),
        ('rm', 'muscle-soreness', ['REF-0474']),
        ('rm', 'stress', ['REF-0474']),
        ('rm', 'skin-irritation', ['REF-0474']), ('rmk', 'skin-irritation', ['REF-0692']),
        ('rmk', 'arthritis', ['REF-0692']),
    ],
}

NOTES = {
    'achillea_millefolium': 'removed refs that do not name the symptom (REF-0011 abstract: wounds, digestive problems, respiratory infections, skin conditions; Grieve: colds, fevers, rheumatism, kidney, styptic/nosebleeds, wounds; Herbal Reality: appetite, flatulence, colds, fever, menorrhagia, dyspepsia, wounds); added Grieve to cold/fever/heavy-bleeding and REF-0369 to inflammation; REF-2822 purged (genus review, experiments on A. coarctata). Full text of REF-0011 not retrieved - re-check its uses list before re-adding it anywhere.',
    'acorus_calamus': 'REF-0516/REF-2825/REF-2827 purged: A. calamus var. angustatus / A. tatarinowii = Acorus verus in POWO (owner decision: wrong species). REF-2824 purged (beta-asarone, no species named). REF-0624 kept only for depression (the only symptom its abstract names); REF-0716 (memory/intellect) wired to memory + cognitive-function.',
    'actaea_racemosa': 'anxiety + depression dropped: REF-0674 found NO significant effect of black cohosh on anxiety; REF-0670 covers only psychological menopausal symptoms (menopause indication keeps both). Null RCT/SR REF-0623, REF-0672, REF-0673 moved to null_result_ids (never evidence). REF-0671 purged (3-ingredient product). REF-2400 removed (reporting-quality review, not efficacy). REF-2830/2831 removed from cancer (rat liver transcriptomics, not cancer studies).',
    'aegopodium_podagraria': "REF-0168 (Moerman, Native American Ethnobotany) purged: the NAEB database has no Aegopodium record (searched naeb.brit.org 2026-11-10). Grieve supports joint/gout/sciatic pain, 'swelling and inflammation' (Gerard) only - removed from headache, skin-irritation, urinary-support, uti.",
    'aesculus_hippocastanum': 'REF-0678 purged (venoactive-drug review never names horse chestnut). REF-2832/2833/2834 purged (escin papers, no source species named). REF-0590/REF-0676 removed from arthritis/hemorrhoids/skin-irritation (abstracts do not name them).',
    'agrimonia_eupatoria': 'EU monograph REF-0386 covers mild diarrhoea, mouth/throat inflammation, minor skin inflammation and superficial wounds only - removed from arthritis/bruising. REF-0680 (neuropathic pain model) removed from arthritis/inflammation. General refs that do not name the symptom removed; REF-0684 (gastric ulcer) kept as mechanistic only.',
    'alchemilla_vulgaris': "REF-0113 (Hoffmann, Medical Herbalism) removed from every symptom: its text could not be verified (owner rule: unverifiable general source = drop). Re-sourcing candidate: ESCOP monograph Alchemillae herba. REF-2227 (genus review, prose-only attribution) excluded from Mechanistic basis.",
    'allium_sativum': 'REF-0166 (garlic + shallot review, abstract names no condition) removed from all symptoms. REF-0204 removed from metabolic-support (BP/cholesterol/immunity only). REF-0651 (allicin vapour vs lung pathogens) removed from wounds; REF-0650 kept as mechanistic only.',
    'aloe_vera': 'REF-2845/REF-2847 purged (aloe-emodin from Rheum), REF-2846/REF-2848 purged (aloe-emodin, source species not named). Wound evidence moved to direct: REF-2241 (SR of clinical trials), REF-2238, REF-2243; REF-2234 to eczema + skin-irritation, REF-2243 to skin-irritation. bruising dropped (wound papers only).',
    'aloysia_citrodora': 'REF-0474 (narrative review) kept only where its abstract names the use (anxiolytic, rheumatism, flatulence, insomnia/sedative, anticancer); removed from indigestion, inflammation, muscle-soreness, skin-irritation, stress. REF-0692 (in vitro) kept as mechanistic only for arthritis/skin-irritation.',
}


def action_refs(d, cond):
    rel = set(REL.get(cond, []))
    return {r for a in d.get('actions', []) if a.get('action') in rel for r in (a.get('reference_ids') or [])}


def purge(node, ref):
    """Remove ref from every list in the record except internal_notes."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'internal_notes':
                continue
            if isinstance(v, list) and ref in v and all(isinstance(x, str) for x in v):
                v[:] = [x for x in v if x != ref]
            else:
                purge(v, ref)
    elif isinstance(node, list):
        for v in node:
            purge(v, ref)


def run(stem, ops, log):
    path = f'plants/{stem}.yaml'
    text, d = Y.load(path)
    import copy
    orig = copy.deepcopy(d)
    ind = {i['condition']: i for i in d.get('indications', [])}
    changed = {'indications'}
    for op in ops:
        kind = op[0]
        if kind == 'purge':
            purge(d, op[1]); changed |= {'actions', 'references', 'constituents', 'contraindications',
                                         'preparations', 'dosage', 'traditional_uses'}
            log.append(f'{stem}\t*\t{op[1]}\tpurge')
            continue
        cond = op[1]
        if cond not in ind:
            raise SystemExit(f'{stem}: no indication {cond}')
        i = ind[cond]
        if kind == 'drop':
            d['indications'] = [x for x in d['indications'] if x['condition'] != cond]
            del ind[cond]; log.append(f'{stem}\t{cond}\t-\tdrop'); continue
        refs = op[2]
        i.setdefault('reference_ids', [])
        if kind in ('rm', 'rmk', 'null'):
            for r in refs:
                if r not in i['reference_ids']:
                    raise SystemExit(f'{stem}/{cond}: {r} not cited')
                i['reference_ids'].remove(r)
                if kind == 'null':
                    i.setdefault('null_result_ids', []).append(r)
                elif kind == 'rm' and r in action_refs(d, cond):
                    mx = i.setdefault('mechanistic_exclude_ids', [])
                    if r not in mx: mx.append(r)
                log.append(f'{stem}\t{cond}\t{r}\t{kind}')
        elif kind == 'add':
            for r in refs:
                if r not in i['reference_ids']: i['reference_ids'].append(r)
                if r in (i.get('mechanistic_exclude_ids') or []): i['mechanistic_exclude_ids'].remove(r)
                log.append(f'{stem}\t{cond}\t{r}\tadd')
        elif kind == 'mexcl':
            mx = i.setdefault('mechanistic_exclude_ids', [])
            for r in refs:
                if r in action_refs(d, cond) and r not in mx and r not in i['reference_ids']:
                    mx.append(r); log.append(f'{stem}\t{cond}\t{r}\tmexcl')
    # tidy: stale exclusions, empty lists, then drop / downgrade evidence-less pairs
    keep = []
    for i in d.get('indications', []):
        cond = i['condition']; ar = action_refs(d, cond)
        if 'mechanistic_exclude_ids' in i:
            i['mechanistic_exclude_ids'] = [r for r in i['mechanistic_exclude_ids'] if r in ar]
            if not i['mechanistic_exclude_ids']: del i['mechanistic_exclude_ids']
        if 'null_result_ids' in i and not i['null_result_ids']: del i['null_result_ids']
        if not i.get('reference_ids'):
            mech = ar - set(i.get('mechanistic_exclude_ids', [])) - set(i.get('null_result_ids', []))
            if not mech:
                log.append(f'{stem}\t{cond}\t-\tdrop(no evidence left)'); continue
            if i.get('status') != 'needs-review':
                i['status'] = 'needs-review'; log.append(f'{stem}\t{cond}\t-\tneeds-review(mechanistic only)')
        keep.append(i)
    d['indications'] = keep
    # actions left with no reference: flag, never silently publish as verified
    for a in d.get('actions', []):
        if not a.get('reference_ids') and a.get('status') == 'verified':
            a['status'] = 'needs-review'; log.append(f'{stem}\taction:{a["action"]}\t-\tneeds-review(unsourced)')
    changed = {k for k in set(d) | set(orig) if d.get(k) != orig.get(k)}
    Y.save(path, text, d, changed)
    append_note(path, f'| {DATE}: symptom-source audit batch 1 - ' + NOTES[stem])


def append_note(path, note):
    """Append to the single-quoted internal_notes scalar without reflowing its history."""
    import textwrap
    text = open(path, encoding='utf-8', newline='').read()
    before = yaml.safe_load(text)['internal_notes']
    head, secs = Y.split_sections(text)
    chunk = dict(secs)['internal_notes']
    body = chunk.rstrip('\n'); trail = chunk[len(body):]
    assert body.startswith("internal_notes: '") and body.endswith("'"), path
    lines = textwrap.wrap(note.replace("'", "''"), 96, break_long_words=False, break_on_hyphens=False)
    new_chunk = body[:-1] + ''.join('\n  ' + ln for ln in lines) + "'" + trail
    text2 = text.replace(chunk, new_chunk, 1)
    after = yaml.safe_load(text2)['internal_notes']
    assert after == before + ' ' + note, (path, after[-200:])
    open(path, 'w', encoding='utf-8', newline='').write(text2)


if __name__ == '__main__':
    log = []
    snap = {stem: open(f'plants/{stem}.yaml', 'rb').read() for stem in PLAN}
    try:
        for stem, ops in PLAN.items():
            run(stem, ops, log)
    except BaseException:
        for stem, b in snap.items():  # all-or-nothing: put every file back
            open(f'plants/{stem}.yaml', 'wb').write(b)
        raise
    open(os.path.join(os.path.dirname(__file__), 'batch01_changes.tsv'), 'w', encoding='utf-8').write(
        'plant\tcondition\tref\top\n' + '\n'.join(log) + '\n')
    print(len(log), 'changes')
