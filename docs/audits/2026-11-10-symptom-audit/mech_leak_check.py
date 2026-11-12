"""List refs that an audit batch REMOVED from a plant's pairs (rm op in batch*_changes.tsv) but that still show as
mechanistic cards on another pair of the same plant. A hit is only a problem when the ref was removed as
unverifiable / not a source (phantom, unlocatable, genus-level, compound-only, multi-herb, homeopathic, wrong
species) - refs removed only for not naming a symptom stay valid as mechanistic cards. Run from the repo root."""
import csv, glob, json, yaml
P = {p['id']: p for p in json.load(open('build/plants.json', encoding='utf-8'))['plants']}
V = {c['id']: c for c in yaml.safe_load(open('vocabularies/conditions.yaml', encoding='utf-8'))}
removed = {}
for f in sorted(glob.glob('docs/audits/2026-11-10-symptom-audit/batch*_changes.tsv')):
    for row in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        if row['op'] == 'rm':
            removed.setdefault(row['plant'].replace('_', '-'), set()).add(row['ref'])
for pid, p in P.items():
    acts = {a['action']: a.get('reference_ids', []) for a in p.get('actions', [])}
    for i in p.get('indications', []):
        c = i['condition']
        hide = set(i.get('reference_ids', [])) | set(i.get('mechanistic_exclude_ids', [])) | set(i.get('null_result_ids', []))
        mech = {r for a in (V.get(c, {}).get('related_actions') or []) for r in acts.get(a, [])} - hide
        bad = mech & removed.get(pid, set())
        if bad:
            print(pid, c, sorted(bad), sep='\t')
