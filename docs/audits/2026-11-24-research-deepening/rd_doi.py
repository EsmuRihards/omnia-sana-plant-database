"""Fetch records that PubMed does not index (OpenAlex / Europe PMC hits) by DOI: title, authors, journal, year,
volume/issue/pages and the abstract, preferring the publisher abstract deposited with Crossref (verbatim JATS text)
over OpenAlex's reconstructed inverted index. Cache: batches/doi_cache.json.
Usage: python docs/audits/2026-11-24-research-deepening/rd_doi.py DOI [DOI ...]   (prints each for reading)
newref_doi(doi, rid, key, study_type) builds a bibliography entry for fixlib.bib_edit(new=...)."""
import html, json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rd_lib as L

CP = os.path.join(L.OUT, 'doi_cache.json')
cache = json.load(open(CP, encoding='utf-8')) if os.path.exists(CP) else {}


def _jats(s):
    s = re.sub(r'<jats:title>.*?</jats:title>', '', s or '', flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def _inv(ix):
    if not ix:
        return ''
    pos = sorted((p, w) for w, ps in ix.items() for p in ps)
    return ' '.join(w for _, w in pos)


def fetch(doi):
    doi = doi.lower().strip()
    if doi in cache:
        return cache[doi]
    cr = L.http_json('https://api.crossref.org/works/' + urllib.parse.quote(doi), timeout=40, tries=2).get('message', {})
    time.sleep(0.5)
    oa = L.http_json('https://api.openalex.org/works/doi:' + urllib.parse.quote(doi), timeout=60, tries=2)
    time.sleep(0.5)
    au = [f"{a.get('family', '')}, {''.join(x[0] + '.' for x in a.get('given', '').replace('-', ' ').split() if x)}".strip(', ')
          for a in cr.get('author', []) if a.get('family')]
    if not au:
        au = [a['author']['display_name'] for a in oa.get('authorships', [])]
    rec = {
        'doi': doi, 'title': _jats((cr.get('title') or [oa.get('title') or ''])[0]),
        'authors': au, 'journal': (cr.get('container-title') or [((oa.get('primary_location') or {}).get('source') or {}).get('display_name', '')])[0],
        'year': str((cr.get('issued', {}).get('date-parts') or [[oa.get('publication_year', '')]])[0][0]),
        'volume': cr.get('volume', ''), 'number': cr.get('issue', ''), 'pages': (cr.get('page') or '').replace('-', '--'),
        'abstract_crossref': _jats(cr.get('abstract', '')), 'abstract_openalex': _inv(oa.get('abstract_inverted_index')),
        'type': cr.get('type', oa.get('type', '')), 'pmid': ((oa.get('ids') or {}).get('pmid') or '').rsplit('/', 1)[-1],
        'retracted': bool(oa.get('is_retracted')), 'oa_url': (oa.get('best_oa_location') or {}).get('landing_page_url') or '',
    }
    cache[doi] = rec
    json.dump(cache, open(CP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return rec


def newref_doi(doi, rid, key, study_type, abstract=None, summary=None):
    """abstract: pass the verbatim text explicitly when neither cached abstract is usable; summary for editorial notes."""
    x = fetch(doi)
    ab = abstract if abstract is not None else (x['abstract_crossref'] or x['abstract_openalex'])
    au = x['authors']
    author = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
    clean = lambda s: re.sub(r'\s+', ' ', str(s).replace('{', '(').replace('}', ')')).strip()  # noqa: E731
    f = [('author', clean(author)), ('title', clean(x['title']).rstrip('.')), ('journal', clean(x['journal'])), ('year', x['year'])]
    f += [(k, clean(x[k])) for k in ('volume', 'number', 'pages') if x.get(k)]
    f.append(('doi', doi))
    f += [('note', rid), ('study_type', study_type)]
    if ab:
        f.append(('abstract', clean(ab)))
    if summary:
        f.append(('summary', clean(summary)))
    return key, (rid, f)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for d in sys.argv[1:]:
        x = fetch(d)
        print(f"== {d} | {x['year']} | {x['journal'][:50]} | {x['type']} | pmid {x['pmid'] or '-'} | retracted {x['retracted']}")
        print('   T:', x['title']); print('   AU:', '; '.join(x['authors'][:4]))
        print('   A(crossref):', x['abstract_crossref'][:2500] or '(none)')
        if not x['abstract_crossref']:
            print('   A(openalex):', x['abstract_openalex'][:2500] or '(none)')
