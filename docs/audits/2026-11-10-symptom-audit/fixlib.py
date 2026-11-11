"""Shared machinery for the 2026-11-10 symptom-audit batch fixers (see fix_batch01.py for
the first, self-contained version). Ops:
  ('rm',  cond, [refs])   remove direct ref; auto-exclude it from that condition's Mechanistic basis
  ('rmk', cond, [refs])   remove direct ref; keep it as a mechanistic card
  ('add', cond, [refs])   add a verified direct ref
  ('null', cond, [refs])  move a no-effect study to null_result_ids
  ('mexcl', cond, [refs]) hide an action ref from that condition's Mechanistic basis
  ('drop', cond)          remove the indication
  ('purge', ref)          remove ref from the whole record (wrong species, phantom, ...)
  ('merge', old, new)     replace a duplicate record id everywhere in the record
After the ops an indication with no direct ref keeps only valid mechanistic cards
(status needs-review) or is dropped. All files are written all-or-nothing.
"""
import copy, os, re, sys, textwrap, yaml
sys.path.insert(0, os.path.dirname(__file__))
import yamlsplice as Y

DATE = '2026-11-10'
VC = yaml.safe_load(open('vocabularies/conditions.yaml', encoding='utf-8'))
REL = {c['id']: c.get('related_actions', []) for c in VC}


def action_refs(d, cond):
    rel = set(REL.get(cond, []))
    return {r for a in d.get('actions', []) if a.get('action') in rel for r in (a.get('reference_ids') or [])}


def _walk_lists(node, fn):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'internal_notes':
                continue
            if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
                node[k] = fn(v)
            else:
                _walk_lists(v, fn)
    elif isinstance(node, list):
        for v in node:
            _walk_lists(v, fn)


def purge(d, ref):
    _walk_lists(d, lambda v: [x for x in v if x != ref])


def merge(d, old, new):
    def fn(v):
        out = []
        for x in v:
            x = new if x == old else x
            if x not in out:
                out.append(x)
        return out
    _walk_lists(d, fn)


def append_note(path, note):
    """Append to the single-quoted internal_notes scalar without reflowing its history."""
    text = open(path, encoding='utf-8', newline='').read()
    before = yaml.safe_load(text)['internal_notes']
    head, secs = Y.split_sections(text)
    chunk = dict(secs)['internal_notes']
    body = chunk.rstrip('\n'); trail = chunk[len(body):]
    assert body.startswith("internal_notes: '") and body.endswith("'"), path
    lines = textwrap.wrap(note.replace("'", "''"), 96, break_long_words=False, break_on_hyphens=False)
    new_chunk = body[:-1] + ''.join('\n  ' + ln for ln in lines) + "'" + trail
    text2 = text.replace(chunk, new_chunk, 1)
    assert yaml.safe_load(text2)['internal_notes'] == before + ' ' + note, path
    open(path, 'w', encoding='utf-8', newline='').write(text2)


def run(stem, ops, log, note, label):
    path = f'plants/{stem}.yaml'
    text, d = Y.load(path)
    orig = copy.deepcopy(d)
    ind = {i['condition']: i for i in d.get('indications', [])}
    for op in ops:
        kind = op[0]
        if kind == 'purge':
            purge(d, op[1]); log.append(f'{stem}\t*\t{op[1]}\tpurge'); continue
        if kind == 'merge':
            merge(d, op[1], op[2]); log.append(f'{stem}\t*\t{op[1]}->{op[2]}\tmerge'); continue
        cond = op[1]
        if cond not in ind:
            raise SystemExit(f'{stem}: no indication {cond}')
        i = ind[cond]
        if kind == 'note':  # ('note', cond, text): replace the indication note
            i['note'] = op[2]; log.append(f'{stem}\t{cond}\t-\tnote'); continue
        if kind == 'drop':
            d['indications'] = [x for x in d['indications'] if x['condition'] != cond]
            del ind[cond]; log.append(f'{stem}\t{cond}\t-\tdrop'); continue
        i.setdefault('reference_ids', [])
        for r in op[2]:
            if kind in ('rm', 'rmk', 'null'):
                if r not in i['reference_ids']:
                    raise SystemExit(f'{stem}/{cond}: {r} not cited')
                i['reference_ids'].remove(r)
                if kind == 'null':
                    i.setdefault('null_result_ids', []).append(r)
                elif kind == 'rm' and r in action_refs(d, cond):
                    mx = i.setdefault('mechanistic_exclude_ids', [])
                    if r not in mx: mx.append(r)
            elif kind == 'nulladd':  # record a no-effect study that is not cited as support
                if r in i['reference_ids']:
                    raise SystemExit(f'{stem}/{cond}: {r} is cited as support - use null')
                nr = i.setdefault('null_result_ids', [])
                if r not in nr: nr.append(r)
            elif kind == 'add':
                if r not in i['reference_ids']: i['reference_ids'].append(r)
                if r in (i.get('mechanistic_exclude_ids') or []): i['mechanistic_exclude_ids'].remove(r)
            elif kind == 'mexcl':
                if r in action_refs(d, cond) and r not in i['reference_ids']:
                    mx = i.setdefault('mechanistic_exclude_ids', [])
                    if r not in mx: mx.append(r)
            log.append(f'{stem}\t{cond}\t{r}\t{kind}')
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
    for a in d.get('actions', []):
        if not a.get('reference_ids') and a.get('status') == 'verified':
            a['status'] = 'needs-review'; log.append(f'{stem}\taction:{a["action"]}\t-\tneeds-review(unsourced)')
    changed = {k for k in set(d) | set(orig) if d.get(k) != orig.get(k)}
    Y.save(path, text, d, changed)
    append_note(path, f'| {DATE}: symptom-source audit {label} - ' + note)


def main(plan, notes, label, out_tsv):
    log = []
    snap = {stem: open(f'plants/{stem}.yaml', 'rb').read() for stem in plan}
    try:
        for stem, ops in plan.items():
            run(stem, ops, log, notes[stem], label)
    except BaseException:
        for stem, b in snap.items():
            open(f'plants/{stem}.yaml', 'wb').write(b)
        raise
    open(out_tsv, 'w', encoding='utf-8').write('plant\tcondition\tref\top\n' + '\n'.join(log) + '\n')
    print(len(log), 'changes')


# ---------------------------------------------------------------- bibliography edits (batch 7+)
BIB = 'bibliography.bibtex'


def _bib_span(lines, ref):
    """(start, end) line indexes of the entry whose note is `ref` (end = its closing '}' line)."""
    hit = [i for i, ln in enumerate(lines) if re.match(r'\s*note\s*=\s*\{' + ref + r'\}', ln)]
    assert len(hit) == 1, (ref, hit)
    s = hit[0]
    while not lines[s].startswith('@'):
        s -= 1
    e = hit[0]
    while lines[e] != '}':
        e += 1
    return s, e


def _bib_line(k, v):
    return f'  {k:<8} = {{{v}}},' if len(k) <= 8 else f'  {k} = {{{v}}},'


def bib_edit(retag=None, sets=None, delete=(), new=None):
    """retag {ref: study_type}; sets {ref: {field: value}} (replace or insert before note);
    delete [ref] (whole entry); new {key: (ref, [(field, value), ...])} inserted in key order.
    Values must already be single-line with no braces."""
    lines = open(BIB, encoding='utf-8', newline='').read().split('\n')
    for ref, st in (retag or {}).items():
        (sets := sets or {}).setdefault(ref, {})['study_type'] = st
    for ref, fields in (sets or {}).items():
        for k, v in fields.items():
            assert '{' not in v and '}' not in v and '\n' not in v, (ref, k)
            s, e = _bib_span(lines, ref)
            idx = [i for i in range(s, e) if re.match(r'\s*' + k + r'\s*=', lines[i])]
            if idx:
                comma = ',' if lines[idx[0]].rstrip().endswith(',') else ''
                lines[idx[0]] = _bib_line(k, v)[:-1] + comma
            else:
                note = [i for i in range(s, e) if re.match(r'\s*note\s*=', lines[i])][0]
                lines.insert(note, _bib_line(k, v))
    for ref in delete:
        s, e = _bib_span(lines, ref)
        if e + 1 < len(lines) and lines[e + 1] == '':
            e += 1
        del lines[s:e + 1]
    for key, (ref, fields) in (new or {}).items():
        assert not any(re.match(r'\s*note\s*=\s*\{' + ref + r'\}', ln) for ln in lines), ref
        body = [f'@article{{{key},'] + [_bib_line(k, v) for k, v in fields]
        body[-1] = body[-1][:-1]
        body += ['}', '']
        starts = [i for i, ln in enumerate(lines) if ln.startswith('@')]
        keys = [re.match(r'@\w+\{([^,]+),', lines[i]).group(1) for i in starts]
        pos = next((starts[j] for j, k in enumerate(keys) if k.lower() > key), len(lines))
        lines[pos:pos] = body
    open(BIB, 'w', encoding='utf-8', newline='').write('\n'.join(lines))


def main_with_bib(plan, notes, label, out_tsv, **bib):
    """bib_edit + main, all-or-nothing across the bibliography and the plant files."""
    snap = open(BIB, 'rb').read()
    try:
        bib_edit(**bib)
        main(plan, notes, label, out_tsv)
    except BaseException:
        open(BIB, 'wb').write(snap)
        raise
