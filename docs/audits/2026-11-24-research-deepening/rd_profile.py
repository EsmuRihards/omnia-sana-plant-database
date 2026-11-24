"""What a batch of plants already holds, field by field, with the study_type of every cited ref.
Usage: python docs/audits/2026-11-24-research-deepening/rd_profile.py <batch_no>
Writes batches/rNN_profile.md. Read it before searching: it shows which claims rest on weak tiers,
which fields are empty, and what earlier sessions already logged as dead ends."""
import collections, json, os, sys
import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rd_lib as L

n = int(sys.argv[1])
E = L.bib()
SYM = {p['id']: {i['condition']: i for i in p['indications']} for p in json.load(open('build/symptoms.json', encoding='utf-8'))['plants']}
HUMAN = {'rct', 'clinical', 'systematic-review', 'meta-analysis'}
out = [f'# Research-deepening batch {n} - profile']


def tag(r):
    f = E.get(r)
    if not f:
        return f'{r}(MISSING)'
    st = f.get('study_type', '?')
    short = {'preclinical': 'pre', 'traditional': 'trad', 'narrative-review': 'nrev', 'rct': 'RCT', 'clinical': 'CLIN',
             'systematic-review': 'SR', 'meta-analysis': 'MA', 'pharmacopoeial': 'pharm'}.get(st, st)
    return f'{r}:{short}'


for p in L.batch_plants(n):
    d = yaml.safe_load(open(f"plants/{p['id'].replace('-', '_')}.yaml", encoding='utf-8'))
    cited = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k != 'internal_notes':
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, str) and x.startswith('REF-'):
            cited.add(x)
    walk(d)
    c = collections.Counter(E.get(r, {}).get('study_type', '?') for r in cited)
    hum = sum(v for k, v in c.items() if k in HUMAN)
    out.append(f"\n## {p['id']} - {d['scientific_name']} - {', '.join(d.get('common_names', [])[:3])}")
    out.append(f"refs cited: {len(cited)} (human {hum}) | " + ', '.join(f'{k} {v}' for k, v in c.most_common()))
    out.append(f"parts_used: {d.get('parts_used')} | synonyms: {d.get('synonyms', [])}")
    out.append('\n**indications** (ev = live Symptom-tool score)')
    for i in d.get('indications', []) or []:
        sh = SYM.get(p['id'], {}).get(i['condition'])
        ev = f"ev{sh['evidence']}" if sh else 'not-shown'
        out.append(f"- {i['condition']} [{i.get('status')},{ev}] D={[tag(r) for r in i.get('reference_ids', []) or []]}"
                   + (f" N={i['null_result_ids']}" if i.get('null_result_ids') else '') + f" | {i.get('note', '')[:150]}")
    out.append('\n**actions**')
    for a in d.get('actions', []) or []:
        out.append(f"- {a['action']} [{a.get('status')}] {[tag(r) for r in a.get('reference_ids', []) or []]}")
    for sec in ('constituents', 'preparations', 'dosage', 'contraindications'):
        out.append(f'\n**{sec}**')
        for x in d.get(sec, []) or []:
            label = x.get('name') or x.get('severity') or ''
            out.append(f"- {label} [{x.get('status', '')}] {[tag(r) for r in x.get('reference_ids', []) or []]} | "
                       f"{(x.get('note') or x.get('text') or '')[:200]}")
    for sec in ('drug_class_interactions', 'pairings'):
        if d.get(sec):
            out.append(f'\n**{sec}**')
            for x in d[sec]:
                out.append(f"- {x.get('drug_class') or x.get('plant')} [{x.get('status')}] "
                           f"{[tag(r) for r in x.get('reference_ids', []) or []]} | {(x.get('note') or x.get('effect') or '')[:160]}")
    for sec in ('botanical_description', 'habitat', 'harvesting', 'traditional_uses'):
        v = d.get(sec) or {}
        if isinstance(v, dict):
            out.append(f"\n**{sec}** {[tag(r) for r in v.get('reference_ids', []) or []]} | {(v.get('text') or '')[:160]}")
    out.append(f"\n**references[] bucket** {[tag(r) for r in d.get('references', []) or []]}")
    hr = d.get('harvest_readiness') or []
    out.append(f"**harvest_readiness** {[(h.get('part'), h.get('status')) for h in hr]} | "
               f"lookalikes: {len(d.get('dangerous_lookalikes') or [])} ({(d.get('lookalikes_review') or {}).get('status') if isinstance(d.get('lookalikes_review'), dict) else d.get('lookalikes_review')})")
    notes = d.get('internal_notes', '') or ''
    out.append(f'**internal_notes** {len(notes)} chars; last 1200: ...{notes[-1200:]}')
path = os.path.join(L.OUT, f'r{n:02d}_profile.md')
open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(path, len('\n'.join(out)), 'chars')
