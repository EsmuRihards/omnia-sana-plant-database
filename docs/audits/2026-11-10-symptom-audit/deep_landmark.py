"""Deep re-sweep: PubMed search for each plant's systematic reviews, meta-analyses and RCTs, marking which the DB
already holds (by PMID or DOI). Run from the repo root.
Usage: python docs/audits/2026-11-10-symptom-audit/deep_landmark.py <batch_no> [plant-id ...]
Query per plant: binomial (and listed synonyms) in title/abstract, or the main common name in the title, restricted
to SR / MA / RCT publication types (CT added when the plant has under 40 hits). Writes deep/dNN_landmark.md;
the abstracts of candidates are fetched later, by hand, only for the ones that matter."""
import json, os, re, sys, time, urllib.parse, urllib.request
sys.path.insert(0, 'scripts')
from build import parse_bibtex  # noqa: E402

b = int(sys.argv[1]); only = set(sys.argv[2:])
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deep')
EU = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
UA = {'User-Agent': 'osdb-audit/1.0 (landmark search)'}
E = [e['fields'] for e in parse_bibtex(open('bibliography.bibtex', encoding='utf-8').read())]
HELD_P = {f['pmid']: f['note'] for f in E if f.get('pmid')}
HELD_D = {f['doi'].lower(): f['note'] for f in E if f.get('doi')}
P = sorted(json.load(open('build/plants.json', encoding='utf-8'))['plants'], key=lambda p: p['id'])[(b - 1) * 10:(b - 1) * 10 + 10]


def get(url, data):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(), headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception:
            time.sleep(2 + 2 * attempt)
    return {}


PT_HI = '(systematic review[pt] OR meta-analysis[pt] OR randomized controlled trial[pt])'
out = [f'# Landmark search batch {b}']
for p in P:
    if only and p['id'] not in only:
        continue
    sci = [p['scientific_name']] + [s for s in p.get('synonyms', []) if isinstance(s, str) and len(s.split()) == 2][:4]
    cn = (p.get('common_names') or [''])[0]
    q = ' OR '.join(f'"{s}"[tiab]' for s in sci)
    if cn and len(cn) > 4:
        q += f' OR "{cn}"[ti]'
    term = f'({q}) AND {PT_HI}'
    r = get(EU + 'esearch.fcgi', {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': 200, 'sort': 'relevance'})
    time.sleep(0.4)
    ids = r.get('esearchresult', {}).get('idlist', [])
    n = r.get('esearchresult', {}).get('count', '?')
    if len(ids) < 40:
        term2 = f'({q}) AND (clinical trial[pt] OR {PT_HI})'
        r2 = get(EU + 'esearch.fcgi', {'db': 'pubmed', 'term': term2, 'retmode': 'json', 'retmax': 200, 'sort': 'relevance'})
        time.sleep(0.4)
        ids = r2.get('esearchresult', {}).get('idlist', ids); n = r2.get('esearchresult', {}).get('count', n) + ' (+CT)'
    out.append(f"\n## {p['id']} ({p['scientific_name']}; {cn}) - {n} hits; query: {term}")
    rows = []
    for k in range(0, len(ids), 150):
        s = get(EU + 'esummary.fcgi', {'db': 'pubmed', 'id': ','.join(ids[k:k + 150]), 'retmode': 'json'}).get('result', {})
        time.sleep(0.4)
        for pid in s.get('uids', []):
            x = s[pid]
            doi = next((a['value'].lower() for a in x.get('articleids', []) if a['idtype'] == 'doi'), '')
            held = HELD_P.get(pid) or HELD_D.get(doi)
            pts = [t for t in x.get('pubtype', []) if t in ('Systematic Review', 'Meta-Analysis', 'Randomized Controlled Trial', 'Clinical Trial', 'Review', 'Retracted Publication')]
            rows.append((x.get('pubdate', '')[:4], pid, held, '/'.join(t.replace('Randomized Controlled Trial', 'RCT').replace('Systematic Review', 'SR').replace('Meta-Analysis', 'MA') for t in pts), x.get('title', '')))
    rows.sort(key=lambda t: t[0], reverse=True)
    for y, pid, held, pts, t in rows:
        out.append(f"- {'HELD ' + held if held else 'new'} | {y} | {pid} | {pts} | {t[:170]}")
open(os.path.join(HERE, f'd{b:02d}_landmark.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(ln for ln in out if ln.startswith('##')))
