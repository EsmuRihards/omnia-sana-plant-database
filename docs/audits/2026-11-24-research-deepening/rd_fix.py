"""Edit ops for the research-deepening batches that fixlib (symptom-audit) has no op for: constituents, contraindications,
dosage, preparations, drug-class interactions and monograph blocks. Indication/action ops still go through fixlib.run.
Every op asserts what it expects to find, so a stale plan fails loudly instead of editing the wrong entry.
  ('cadd', name_substr, [refs])        add refs to the constituent whose name contains name_substr
  ('cnew', {name, compounds?, note, reference_ids})
  ('ciadd', note_substr, [refs])       add refs to the contraindication whose note contains note_substr
  ('cinew', {note, severity, reference_ids})            status 'verified' (a sourced caution, not an approval)
  ('dadd', name_substr, [refs]) / ('dnew', {name, text, reference_ids})   dosage
  ('padd', name_substr, [refs]) / ('pnew', {name, text, reference_ids})   preparations
  ('dcinew', {drug_class, severity, mechanism, reference_ids})            ALWAYS status draft (owner sign-off needed)
  ('dciadd', drug_class, [refs])       add refs to an existing interaction (status untouched)
  ('madd', block, [refs])              add refs to a monograph block (botanical_description/habitat/harvesting/traditional_uses)
Notes must be dash-free (no em/en dashes, owner rule)."""
import copy, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2026-11-10-symptom-audit'))
import yamlsplice as Y  # noqa: E402

DASH = ('—', '–')


def _nodash(*s):
    for x in s:
        assert not any(c in str(x) for c in DASH), ('em/en dash', x)


def _one(lst, key, sub, what):
    hit = [x for x in lst if sub.lower() in (x.get(key) or '').lower()]
    assert len(hit) == 1, (what, sub, len(hit))
    return hit[0]


def _addrefs(entry, refs):
    lst = entry.setdefault('reference_ids', [])
    for r in refs:
        if r not in lst:
            lst.append(r)


def apply(stem, ops, log):
    path = f'plants/{stem}.yaml'
    text, d = Y.load(path)
    orig = copy.deepcopy(d)
    for op in ops:
        k = op[0]
        if k == 'cadd':
            _addrefs(_one(d['constituents'], 'name', op[1], 'constituent'), op[2])
        elif k == 'cnew':
            _nodash(op[1].get('note', ''), op[1]['name'])
            d.setdefault('constituents', []).append(dict(op[1]))
        elif k == 'ciadd':
            _addrefs(_one(d['contraindications'], 'note', op[1], 'contraindication'), op[2])
        elif k == 'cinew':
            _nodash(op[1]['note'])
            e = dict(op[1]); e.setdefault('status', 'verified')
            d.setdefault('contraindications', []).append(e)
        elif k == 'dadd':
            _addrefs(_one(d['dosage'], 'name', op[1], 'dosage'), op[2])
        elif k == 'dnew':
            _nodash(op[1]['text'], op[1]['name'])
            e = dict(op[1]); e.setdefault('status', 'verified')
            d.setdefault('dosage', []).append(e)
        elif k == 'padd':
            _addrefs(_one(d['preparations'], 'name', op[1], 'preparation'), op[2])
        elif k == 'pnew':
            _nodash(op[1]['text'], op[1]['name'])
            e = dict(op[1]); e.setdefault('status', 'verified')
            d.setdefault('preparations', []).append(e)
        elif k == 'dcinew':
            _nodash(op[1].get('mechanism', ''))
            assert not any(x['drug_class'] == op[1]['drug_class'] for x in d.get('drug_class_interactions', []) or []), op
            e = dict(op[1]); e['status'] = 'draft'
            d.setdefault('drug_class_interactions', []).append(e)
        elif k == 'dciadd':
            _addrefs(_one(d['drug_class_interactions'], 'drug_class', op[1], 'interaction'), op[2])
        elif k == 'madd':
            assert op[1] in ('botanical_description', 'habitat', 'harvesting', 'traditional_uses'), op
            _addrefs(d[op[1]], op[2])
        else:
            raise SystemExit(f'unknown op {k}')
        log.append(f"{stem}\t{k}\t{op[1] if isinstance(op[1], str) else op[1].get('name') or op[1].get('drug_class') or op[1].get('note', '')[:40]}"
                   f"\t{','.join(op[2]) if len(op) > 2 else ','.join(op[1].get('reference_ids', []))}")
    changed = {key for key in set(d) | set(orig) if d.get(key) != orig.get(key)}
    if changed:
        Y.save(path, text, d, changed)
