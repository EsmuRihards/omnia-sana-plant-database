"""Extract every source card the Symptom tool shows for a batch of plants.

Mirrors os-symptom-sources.php: DIRECT = indication.reference_ids;
MECH = refs of plant actions in condition.related_actions, minus direct, minus
indication.mechanistic_exclude_ids.
Usage: python extract_batch.py <db_dir> <start> <count> <out.md>
"""
import json, sys, os

db, start, count, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
P = json.load(open(os.path.join(db, 'build/plants.json'), encoding='utf-8'))['plants']
C = {c['ref_id']: c for c in json.load(open(os.path.join(db, 'build/citations.json'), encoding='utf-8'))['citations']}
S = json.load(open(os.path.join(db, 'build/symptoms.json'), encoding='utf-8'))
conds = {c['id']: c for c in S['conditions']}
shown = {p['id']: {i['condition']: i for i in p['indications']} for p in S['plants']}

P.sort(key=lambda p: p['id'])
batch = P[start:start + count]
lines = []
for p in batch:
    pid = p['id']
    acts = {a['action']: a for a in p.get('actions', [])}
    sh = shown.get(pid, {})
    lines.append(f"\n# {pid} ({p['scientific_name']}) - {p['common_names'][0] if p.get('common_names') else ''}")
    lines.append(f"tool indications: {len(sh)} / yaml indications: {len(p.get('indications', []))}")
    use = {}  # ref -> list of tags
    for ind in p.get('indications', []):
        cid = ind['condition']
        s = sh.get(cid)
        tag_ev = f"ev{s['evidence']}{'/inf' if s.get('inferred') else ''}" if s else 'NOT-SHOWN'
        lines.append(f"- {cid} [{ind.get('status')}, {tag_ev}] D={ind.get('reference_ids', [])} X={ind.get('mechanistic_exclude_ids', [])}")
        direct = list(ind.get('reference_ids', []))
        for r in direct:
            use.setdefault(r, []).append(f"D:{cid}")
        excl = set(ind.get('mechanistic_exclude_ids', []))
        for act in conds.get(cid, {}).get('related_actions', []):
            if act in acts:
                for r in acts[act].get('reference_ids', []):
                    if r in direct or r in excl:
                        continue
                    use.setdefault(r, []).append(f"M:{cid}<{act}")
    lines.append("")
    for r in sorted(use):
        c = C.get(r)
        if not c:
            lines.append(f"!! {r} MISSING FROM CITATIONS -> {use[r]}")
            continue
        ab = (c.get('abstract') or '').replace('\n', ' ')
        lines.append(f"## {r} [{c.get('tier')}] {c.get('year')} | {c.get('title')}")
        lines.append(f"   USED: {', '.join(use[r])}")
        lines.append(f"   ABS: {ab[:700] if ab else '(none)'}")
open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print('plants:', [p['id'] for p in batch])
