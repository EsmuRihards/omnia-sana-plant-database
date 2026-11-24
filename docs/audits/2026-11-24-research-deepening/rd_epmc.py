"""Re-run only the Europe PMC seams (Europe PMC returns 503 under load; this retries slowly and splits the
full-text query into smaller ones). Usage: python docs/audits/2026-11-24-research-deepening/rd_epmc.py <batch_no> [plant-id ...]
Writes batches/rNN_epmc.md. Same HELD / SEEN / new marking as rd_search.py."""
import os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rd_lib as L

n = int(sys.argv[1]); only = set(sys.argv[2:])
E = L.bib(); IDX = L.held_index(E); SEEN = L.seen_corpus()
SEEN_NUM = set(re.findall(r'(?<!\d)(\d{6,9})(?!\d)', SEEN))
SEEN_DOI = {d.lower().rstrip('.,;)') for d in re.findall(r'10\.\d{4,9}/[^\s|,;\]\)}\'"]+', SEEN)}


def mark(pmid='', doi='', title=''):
    h = L.is_held(IDX, pmid, doi, title)
    if h:
        return 'HELD ' + h
    return 'SEEN' if ((pmid and pmid in SEEN_NUM) or (doi and doi.lower() in SEEN_DOI)) else 'new'


def epmc(q, size=100):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode(
        {'query': q, 'format': 'json', 'pageSize': size, 'resultType': 'lite'})
    for attempt in range(6):
        r = L.http_json(url, tries=1)
        if r:
            return r.get('hitCount', '?'), r.get('resultList', {}).get('result', [])
        time.sleep(10 + 10 * attempt)
    return 'FAILED', []


md = [f'# Research-deepening batch {n} - Europe PMC']
for p in L.batch_plants(n):
    if only and p['id'] not in only:
        continue
    b = p['scientific_name']; cn = (p.get('common_names') or [''])[0]
    nm = f'(TITLE_ABS:"{b}"' + (f' OR TITLE:"{cn}")' if len(cn) > 4 else ')')
    qs = [
        ('non-MEDLINE, human-study wording', f'{nm} AND (randomized OR randomised OR placebo OR "clinical trial" OR patients OR volunteers) NOT SRC:MED'),
        ('non-MEDLINE, review / safety wording', f'{nm} AND ("systematic review" OR "meta-analysis" OR "case report" OR adverse OR toxicity OR poisoning OR interaction) NOT SRC:MED'),
        ('full text, trial in title', f'"{b}" AND (TITLE:randomized OR TITLE:randomised OR TITLE:placebo OR TITLE:trial)'),
        ('full text, patients/volunteers in title', f'"{b}" AND (TITLE:patients OR TITLE:volunteers OR TITLE:women OR TITLE:"clinical study")'),
    ]
    md.append(f"\n## {p['id']} ({b})")
    for lab, q in qs:
        cnt, rows = epmc(q)
        md.append(f'\n### {lab} - {cnt} hits')
        for x in sorted(rows, key=lambda x: x.get('pubYear', ''), reverse=True):
            m = mark(x.get('pmid', ''), x.get('doi', ''), x.get('title', ''))
            md.append(f"- {m} | {x.get('pubYear', '')} | {x.get('pmid') or x.get('id')} | {x.get('source', '')} | "
                      f"{x.get('title', '')[:170]} | {x.get('journalTitle', '')[:40]}" + (f" | doi {x['doi']}" if x.get('doi') else '')
                      + (f" | {x['pmcid']}" if x.get('pmcid') else ''))
        time.sleep(3)
    print(p['id'], 'done', file=sys.stderr, flush=True)
open(os.path.join(L.OUT, f'r{n:02d}_epmc.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('\n'.join(ln for ln in md if ln.startswith('#')))
