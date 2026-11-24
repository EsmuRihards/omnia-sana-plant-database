"""Multi-seam literature search for a batch of 5 plants; marks every hit HELD (already in the bibliography, by
PMID / DOI / title), SEEN (its PMID or DOI appears in an earlier audit report or the plant's internal_notes, i.e.
already judged once - read that note before re-judging) or new.
Usage: python docs/audits/2026-11-24-research-deepening/rd_search.py <batch_no> [plant-id ...]
Seams and query families (name clause = binomial + 2-word synonyms in [tiab], first common name in [ti]):
  PubMed HT   human trials incl. untagged ones (randomized/placebo/double-blind/open-label/crossover/pilot...)
  PubMed SR   systematic reviews / meta-analyses (pt or wording)
  PubMed SAFE case reports, adverse events, toxicity, interactions, CYP/P-gp, pharmacokinetics, pregnancy
  PubMed OBS  cohort / case-control / cross-sectional human studies
  PubMed REV  narrative reviews (top 25 by relevance) - for constituents, actions, monograph blocks
  EuropePMC   non-MEDLINE records (PMC-only, preprints, Agricola, Chinese abstracts) with trial/review wording,
              plus full-text hits where the binomial is in the body and the title reads like a human study
  CT.gov      registered trials (status, has-results, linked result publications)
  OpenAlex    trial-worded works with no PMID (journals PubMed does not index)
Overrides: batches/names_override.json {plant-id: {"tiab": [...], "ti": [...]}} replaces the name clause
(for ambiguous common names). Writes batches/rNN_search.md + rNN_search.json."""
import json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rd_lib as L

n = int(sys.argv[1]); only = set(sys.argv[2:])
E = L.bib(); IDX = L.held_index(E); SEEN = L.seen_corpus()
EU = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
OVR_P = os.path.join(L.OUT, 'names_override.json')
OVR = json.load(open(OVR_P, encoding='utf-8')) if os.path.exists(OVR_P) else {}

FAM = {
    'HT': '(randomized[tiab] OR randomised[tiab] OR placebo[tiab] OR "double-blind"[tiab] OR "double blind"[tiab] OR '
          '"single-blind"[tiab] OR "clinical trial"[pt] OR "controlled clinical trial"[pt] OR "open-label"[tiab] OR '
          '"pilot study"[tiab] OR crossover[tiab] OR "cross-over"[tiab] OR "healthy volunteers"[tiab] OR '
          '"healthy subjects"[tiab] OR patients[ti] OR women[ti] OR children[ti]) NOT (animals[mh] NOT humans[mh])',
    'SR': '(systematic review[pt] OR meta-analysis[pt] OR "systematic review"[tiab] OR "meta-analysis"[tiab] OR '
          '"meta-analyses"[tiab] OR "scoping review"[tiab])',
    'SAFE': '("case reports"[pt] OR adverse[tiab] OR "side effect"[tiab] OR "side effects"[tiab] OR toxicity[ti] OR '
            'hepatotox*[tiab] OR "liver injury"[tiab] OR poisoning[tiab] OR intoxication[tiab] OR "drug interaction"[tiab] OR '
            '"drug interactions"[tiab] OR "herb-drug"[tiab] OR cytochrome[tiab] OR CYP3A4[tiab] OR CYP2D6[tiab] OR '
            'CYP2C9[tiab] OR CYP1A2[tiab] OR "P-glycoprotein"[tiab] OR pharmacokinetic*[tiab] OR allerg*[ti] OR '
            'dermatitis[ti] OR anaphyla*[tiab] OR pregnan*[ti] OR lactation[ti] OR genotox*[tiab] OR carcinogen*[tiab] OR '
            'teratogen*[tiab] OR "safety"[ti])',
    'OBS': '(cohort[tiab] OR "case-control"[tiab] OR "cross-sectional"[tiab] OR "prospective study"[tiab] OR '
           '"observational"[tiab]) NOT (animals[mh] NOT humans[mh])',
    'REV': '(review[pt] NOT systematic review[pt])',
}
LIMIT = {'HT': 200, 'SR': 100, 'SAFE': 200, 'OBS': 60, 'REV': 25}


def name_clause(p):
    if p['id'] in OVR:
        o = OVR[p['id']]
        return ' OR '.join([f'"{s}"[tiab]' for s in o.get('tiab', [])] + [f'"{s}"[ti]' for s in o.get('ti', [])]), o
    sci = [p['scientific_name']] + [s for s in p.get('synonyms', []) if isinstance(s, str) and len(s.split()) == 2][:5]
    cn = [c for c in (p.get('common_names') or [])[:1] if len(c) > 4]
    return ' OR '.join([f'"{s}"[tiab]' for s in sci] + [f'"{c}"[ti]' for c in cn]), {'tiab': sci, 'ti': cn}


SEEN_NUM = set(re.findall(r'(?<!\d)(\d{6,9})(?!\d)', SEEN))
SEEN_DOI = {d.lower().rstrip('.,;)') for d in re.findall(r'10\.\d{4,9}/[^\s|,;\]\)}\'"]+', SEEN)}


def seen(pmid, doi):
    return (pmid and str(pmid) in SEEN_NUM) or (doi and doi.lower() in SEEN_DOI)


def mark(pmid='', doi='', title=''):
    h = L.is_held(IDX, pmid, doi, title)
    if h:
        return 'HELD ' + h
    return 'SEEN' if seen(pmid, doi) else 'new'


def pubmed(term, retmax):
    r = L.http_json(EU + 'esearch.fcgi', {'db': 'pubmed', 'term': term, 'retmode': 'json', 'retmax': retmax, 'sort': 'relevance'})
    time.sleep(0.35)
    ids = r.get('esearchresult', {}).get('idlist', []); cnt = r.get('esearchresult', {}).get('count', '?')
    rows = []
    for k in range(0, len(ids), 150):
        s = L.http_json(EU + 'esummary.fcgi', {'db': 'pubmed', 'id': ','.join(ids[k:k + 150]), 'retmode': 'json'}).get('result', {})
        time.sleep(0.35)
        for pid in s.get('uids', []):
            x = s[pid]
            doi = next((a['value'] for a in x.get('articleids', []) if a['idtype'] == 'doi'), '')
            pts = [t for t in x.get('pubtype', []) if t not in ('Journal Article', 'English Abstract')]
            rows.append({'pmid': pid, 'doi': doi, 'year': x.get('pubdate', '')[:4], 'title': x.get('title', ''),
                         'journal': x.get('source', ''), 'pt': '/'.join(pts), 'lang': ','.join(x.get('lang', []))})
    return cnt, rows


def europepmc(q, size=100):
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode(
        {'query': q, 'format': 'json', 'pageSize': size, 'resultType': 'lite', 'sort': 'RELEVANCE'})
    r = L.http_json(url)
    rows = []
    for x in r.get('resultList', {}).get('result', []):
        rows.append({'pmid': x.get('pmid', ''), 'doi': x.get('doi', ''), 'year': x.get('pubYear', ''), 'title': x.get('title', ''),
                     'journal': x.get('journalTitle', '') or x.get('bookOrReportDetails', {}).get('publisher', ''),
                     'pt': x.get('source', '') + ('/' + x['pubType'] if x.get('pubType') else ''), 'src_id': x.get('id', ''),
                     'pmcid': x.get('pmcid', '')})
    return r.get('hitCount', '?'), rows


def ctgov(terms):
    rows, seen_ids = [], set()
    for t in terms:
        url = 'https://clinicaltrials.gov/api/v2/studies?' + urllib.parse.urlencode({'query.intr': t, 'pageSize': 100})
        r = L.http_json(url)
        for s in r.get('studies', []):
            ps = s.get('protocolSection', {})
            nct = ps.get('identificationModule', {}).get('nctId')
            if nct in seen_ids:
                continue
            seen_ids.add(nct)
            refs = ps.get('referencesModule', {}).get('references', []) or []
            res = [f"{x.get('pmid', '')}:{x.get('type', '')}" for x in refs if x.get('type') in ('RESULT', 'DERIVED')]
            rows.append({'nct': nct, 'title': ps.get('identificationModule', {}).get('briefTitle', ''),
                         'status': ps.get('statusModule', {}).get('overallStatus', ''), 'results': s.get('hasResults', False),
                         'conds': ', '.join(ps.get('conditionsModule', {}).get('conditions', [])[:4]),
                         'intr': ', '.join(i.get('name', '') for i in ps.get('armsInterventionsModule', {}).get('interventions', [])[:4]),
                         'pubs': res, 'phase': ','.join(ps.get('designModule', {}).get('phases', []) or [])})
        time.sleep(0.5)
    return rows


def openalex(binom):
    url = 'https://api.openalex.org/works?' + urllib.parse.urlencode({
        'search': f'"{binom}"', 'per-page': 100,
        'filter': 'title_and_abstract.search:randomized|randomised|placebo|trial|patients|volunteers'})
    r = L.http_json(url, timeout=90, tries=3)
    rows = []
    for w in r.get('results', []):
        ids = w.get('ids', {}) or {}
        if ids.get('pmid'):
            continue  # PubMed seams already cover it
        doi = (w.get('doi') or '').replace('https://doi.org/', '')
        src = ((w.get('primary_location') or {}).get('source') or {}).get('display_name', '')
        rows.append({'pmid': '', 'doi': doi, 'year': str(w.get('publication_year', '')), 'title': w.get('title') or '',
                     'journal': src, 'pt': w.get('type', ''), 'oa': w.get('id', '')})
    return r.get('meta', {}).get('count', '?'), rows


md, js = [f'# Research-deepening batch {n} - search'], {}
for p in L.batch_plants(n):
    if only and p['id'] not in only:
        continue
    nc, names = name_clause(p)
    md.append(f"\n## {p['id']} ({p['scientific_name']}) - name clause: {nc}")
    js[p['id']] = {}
    allp = set()
    for fam, filt in FAM.items():
        cnt, rows = pubmed(f'({nc}) AND {filt}', LIMIT[fam])
        new = [r for r in rows if r['pmid'] not in allp]
        allp |= {r['pmid'] for r in rows}
        for r in new:
            r['mark'] = mark(r['pmid'], r['doi'], r['title'])
        js[p["id"]][fam] = new; print("  ", p["id"], fam, cnt, file=sys.stderr, flush=True)
        nn = sum(1 for r in new if r['mark'] == 'new')
        md.append(f"\n### PubMed {fam} - {cnt} hits, {len(new)} not already listed above, {nn} new")
        for r in sorted(new, key=lambda r: r['year'], reverse=True):
            md.append(f"- {r['mark']} | {r['year']} | {r['pmid']} | {r['pt']} | {r['title'][:180]} | {r['journal'][:40]}"
                      + (f" [{r['lang']}]" if r['lang'] and r['lang'] != 'eng' else ''))
    tiab = names['tiab']; ti = names['ti']
    nm = ' OR '.join([f'TITLE_ABS:"{s}"' for s in tiab] + [f'TITLE:"{c}"' for c in ti])
    q1 = (f'({nm}) AND (randomized OR randomised OR placebo OR "clinical trial" OR "double-blind" OR patients OR volunteers '
          f'OR "systematic review" OR "meta-analysis" OR "case report" OR adverse OR toxicity OR interaction) NOT SRC:MED')
    q2 = (f'"{tiab[0]}" AND (TITLE:randomized OR TITLE:randomised OR TITLE:placebo OR TITLE:trial OR TITLE:patients '
          f'OR TITLE:volunteers OR TITLE:"clinical study")')
    for lab, q in ((() if os.environ.get('NO_EPMC') else (('EuropePMC non-MEDLINE', q1), ('EuropePMC full-text', q2)))):
        cnt, rows = europepmc(q)
        rows = [r for r in rows if not r['pmid'] or r['pmid'] not in allp]
        for r in rows:
            r['mark'] = mark(r['pmid'], r['doi'], r['title'])
        js[p['id']][lab] = rows
        md.append(f"\n### {lab} - {cnt} hits, {len(rows)} not in the PubMed lists, {sum(1 for r in rows if r['mark'] == 'new')} new")
        for r in sorted(rows, key=lambda r: r['year'], reverse=True):
            md.append(f"- {r['mark']} | {r['year']} | {r['pmid'] or r['src_id']} | {r['pt']} | {r['title'][:180]} | {r['journal'][:40]}"
                      + (f" | doi {r['doi']}" if r['doi'] else '') + (f" | {r['pmcid']}" if r['pmcid'] else ''))
    rows = ctgov(tiab[:1] + ti)
    js[p['id']]['CT.gov'] = rows
    md.append(f'\n### ClinicalTrials.gov - {len(rows)} registered studies')
    for r in rows:
        pubs = [f"{x} ({mark(x.split(':')[0]) if x.split(':')[0] else '-'})" for x in r['pubs']]
        md.append(f"- {r['nct']} | {r['status']} | results={r['results']} | {r['phase']} | {r['title'][:140]} | conds: {r['conds']} | "
                  f"intr: {r['intr'][:100]}" + (f" | pubs: {pubs}" if pubs else ''))
    cnt, rows = openalex(tiab[0])
    for r in rows:
        r['mark'] = mark('', r['doi'], r['title'])
    js[p['id']]['OpenAlex'] = rows
    md.append(f"\n### OpenAlex no-PMID trial-worded - {cnt} hits, {len(rows)} without PMID, {sum(1 for r in rows if r['mark'] == 'new')} new")
    for r in sorted(rows, key=lambda r: r['year'], reverse=True):
        md.append(f"- {r['mark']} | {r['year']} | {r['doi'] or r['oa']} | {r['pt']} | {r['title'][:180]} | {r['journal'][:40]}")
    print(p['id'], 'done', file=sys.stderr)

suffix = ('_' + '_'.join(sorted(only))) if only else ''
open(os.path.join(L.OUT, f'r{n:02d}_search{suffix}.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
json.dump(js, open(os.path.join(L.OUT, f'r{n:02d}_search{suffix}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('\n'.join(ln for ln in md if ln.startswith('##')))
