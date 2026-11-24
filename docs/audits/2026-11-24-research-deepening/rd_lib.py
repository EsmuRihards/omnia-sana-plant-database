"""Shared helpers for the 2026-11-24 research-deepening campaign (batches of 5 plants, alphabetical by id).
Run every rd_*.py from the repo root. Batch N = plants sorted by id, slice [(N-1)*5, N*5)."""
import glob, json, os, re, sys, time, urllib.parse, urllib.request
sys.path.insert(0, 'scripts')
from build import parse_bibtex  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'batches')
os.makedirs(OUT, exist_ok=True)
UA = {'User-Agent': 'osdb-research/1.0 (literature audit)', 'Accept-Encoding': 'identity'}
BATCH = 5


def bib():
    return {e['ref_id']: dict(e['fields'], _type=e['type'], _key=e['key'])
            for e in parse_bibtex(open('bibliography.bibtex', encoding='utf-8').read())}


def norm_title(t):
    return re.sub(r'[^a-z0-9]', '', (t or '').lower())[:70]


def held_index(E):
    P, D, T = {}, {}, {}
    for rid, f in E.items():
        if f.get('pmid'):
            P[str(f['pmid']).strip()] = rid
        if f.get('doi'):
            D[f['doi'].strip().lower()] = rid
        nt = norm_title(f.get('title'))
        if len(nt) > 25:
            T[nt] = rid
    return P, D, T


def is_held(idx, pmid='', doi='', title=''):
    P, D, T = idx
    return P.get(str(pmid)) or D.get((doi or '').lower()) or (T.get(norm_title(title)) if len(norm_title(title)) > 25 else None)


def batch_plants(n):
    P = sorted(json.load(open('build/plants.json', encoding='utf-8'))['plants'], key=lambda p: p['id'])
    return P[(n - 1) * BATCH:n * BATCH]


def seen_corpus():
    """Every audit report + every plant's internal_notes, for 'was this candidate already judged?'."""
    txt = []
    for f in glob.glob('docs/audits/**/*.md', recursive=True) + glob.glob('docs/audits/**/*.tsv', recursive=True):
        g = f.replace('\\', '/')
        if ('2026-11-24-research-deepening' in g and '/batches/' in g) or g.endswith('_landmark.md'):
            continue  # raw hit lists, not judgements: being listed once is not being judged
        txt.append(open(f, encoding='utf-8', errors='ignore').read())
    for f in glob.glob('plants/*.yaml'):
        t = open(f, encoding='utf-8').read()
        i = t.find('internal_notes:')
        if i >= 0:
            txt.append(t[i:])
    return '\n'.join(txt)


def http_json(url, data=None, timeout=60, tries=4):
    for attempt in range(tries):
        try:
            if data is not None:
                req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(), headers=UA)
            else:
                req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as ex:  # noqa: BLE001
            err = ex
            time.sleep(2 + 3 * attempt)
    print('  !! request failed:', url[:120], err, file=sys.stderr)
    return {}
