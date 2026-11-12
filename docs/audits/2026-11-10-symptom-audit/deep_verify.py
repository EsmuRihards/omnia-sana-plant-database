"""Deep re-sweep integrity check for every ref in a batch dossier (run deep_dossier.py first). Run from repo root.
Usage: python docs/audits/2026-11-10-symptom-audit/deep_verify.py <batch_no>
PubMed (E-utilities) by PMID or DOI -> title similarity, publication types, retraction flag; DOIs PubMed lacks
-> Crossref title. Writes deep/dNN_verify.tsv and caches lookups in deep/verify_cache.json.
Flags: TITLE? (title similarity < 0.6), DEADDOI (Crossref 404), RETRACTED, NOID (article with neither id),
TAG? (PubMed type disagrees with study_type)."""
import difflib, json, os, re, sys, time, urllib.parse, urllib.request

b = int(sys.argv[1])
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deep')
R = json.load(open(os.path.join(HERE, f'd{b:02d}_refs.json'), encoding='utf-8'))
CP = os.path.join(HERE, 'verify_cache.json')
cache = json.load(open(CP, encoding='utf-8')) if os.path.exists(CP) else {}
EU = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
UA = {'User-Agent': 'osdb-audit/1.0 (citation integrity check)'}


def get(url, data=None):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode() if data else None, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(2 + attempt * 2)
        except Exception:
            time.sleep(2 + attempt * 2)
    return 'ERR'


def norm(t):
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'<[^>]+>', '', (t or '').lower()))


def summ(pmids):
    out = {}
    for k in range(0, len(pmids), 150):
        js = get(EU + 'esummary.fcgi', {'db': 'pubmed', 'id': ','.join(pmids[k:k + 150]), 'retmode': 'json'})
        time.sleep(0.4)
        if not js or js == 'ERR':
            continue
        res = json.loads(js).get('result', {})
        for pid in res.get('uids', []):
            x = res[pid]
            doi = next((a['value'] for a in x.get('articleids', []) if a['idtype'] == 'doi'), '')
            out[pid] = {'title': x.get('title', ''), 'pubtypes': x.get('pubtype', []), 'doi': doi.lower(), 'pmid': pid,
                        'source': x.get('source', ''), 'year': x.get('pubdate', '')[:4]}
    return out


todo_pmid = [f['pmid'] for r, f in R.items() if f.get('pmid') and 'pmid:' + f['pmid'] not in cache]
todo_doi = [f['doi'].lower() for r, f in R.items() if f.get('doi') and not f.get('pmid') and 'doi:' + f['doi'].lower() not in cache]
for pid, x in summ(todo_pmid).items():
    cache['pmid:' + pid] = x
# DOI -> PMID via esearch (one DOI per query term; batched with OR)
found = {}
for k in range(0, len(todo_doi), 12):
    chunk = todo_doi[k:k + 12]
    term = ' OR '.join(f'"{d}"[doi]' for d in chunk)
    js = get(EU + 'esearch.fcgi', {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': 50})
    time.sleep(0.4)
    if js and js != 'ERR':
        for pid, x in summ(json.loads(js)['esearchresult'].get('idlist', [])).items():
            if x['doi'] in chunk:
                found[x['doi']] = x
for d in todo_doi:
    if d in found:
        cache['doi:' + d] = found[d]
        continue
    js = get('https://api.crossref.org/works/' + urllib.parse.quote(d))
    time.sleep(0.3)
    if js is None:
        cache['doi:' + d] = {'dead': True}
    elif js == 'ERR':
        continue
    else:
        m = json.loads(js)['message']
        cache['doi:' + d] = {'title': (m.get('title') or [''])[0], 'pubtypes': [m.get('type', '')], 'crossref': True,
                             'source': (m.get('container-title') or [''])[0],
                             'year': str((m.get('issued', {}).get('date-parts') or [[None]])[0][0])}
json.dump(cache, open(CP, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

REV = {'Review', 'Systematic Review', 'Meta-Analysis'}
rows = ['ref\tstudy_type\tflags\tsim\tpubtypes\tbib_title\tfound_title']
for r, f in sorted(R.items()):
    st = f.get('study_type', ''); flags = []
    key = ('pmid:' + f['pmid']) if f.get('pmid') else ('doi:' + f['doi'].lower()) if f.get('doi') else None
    x = cache.get(key) if key else None
    if not key:
        if f.get('_type') == 'article':
            flags.append('NOID')
        rows.append(f"{r}\t{st}\t{' '.join(flags)}\t\t\t{f.get('title', '')[:120]}\t"); continue
    if x is None:
        rows.append(f"{r}\t{st}\tNOTCHECKED\t\t\t{f.get('title', '')[:120]}\t"); continue
    if x.get('dead'):
        rows.append(f"{r}\t{st}\tDEADDOI\t\t\t{f.get('title', '')[:120]}\t"); continue
    sim = difflib.SequenceMatcher(None, norm(f.get('title')), norm(x['title'])).ratio()
    if sim < 0.6: flags.append('TITLE?')
    pt = set(x.get('pubtypes', []))
    if 'Retracted Publication' in pt or 'Retraction of Publication' in pt: flags.append('RETRACTED')
    if not x.get('crossref'):
        if pt & {'Systematic Review', 'Meta-Analysis'} and st not in ('systematic-review', 'meta-analysis'):
            flags.append('TAG?SR')
        elif 'Review' in pt and st in ('rct', 'clinical', 'preclinical', 'systematic-review', 'meta-analysis') and not pt & {'Systematic Review', 'Meta-Analysis'}:
            flags.append('TAG?review')
        if 'Randomized Controlled Trial' in pt and st != 'rct':
            flags.append('TAG?rct')
        if st == 'rct' and not pt & {'Randomized Controlled Trial', 'Clinical Trial', 'Controlled Clinical Trial'} and pt:
            flags.append('TAG?not-rct')
    rows.append(f"{r}\t{st}\t{' '.join(flags)}\t{sim:.2f}\t{'|'.join(sorted(pt))}\t{f.get('title', '')[:120]}\t{x['title'][:120]}")
open(os.path.join(HERE, f'd{b:02d}_verify.tsv'), 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
bad = [ln for ln in rows[1:] if ln.split('\t')[2]]
print(f'batch {b}: {len(rows) - 1} refs, {len(bad)} flagged')
for ln in bad:
    c = ln.split('\t'); print(c[0], c[1], c[2], c[3], c[4][:50], '|', c[5][:80], '|', c[6][:80], sep='  ')
