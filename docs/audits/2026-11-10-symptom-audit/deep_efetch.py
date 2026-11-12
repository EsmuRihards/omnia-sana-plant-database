"""Fetch PubMed records (verbatim abstract, inline-markup text kept, tags dropped) into deep/abstracts.json.
Usage: python docs/audits/2026-11-10-symptom-audit/deep_efetch.py [--quiet] PMID [PMID ...]
Prints title, type, journal/year, DOI and the full abstract for reading; the cache feeds new bib entries
(deep_newref() in deep_lib.py). Run from the repo root."""
import json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deep')
CP = os.path.join(HERE, 'abstracts.json')
cache = json.load(open(CP, encoding='utf-8')) if os.path.exists(CP) else {}
args = [a for a in sys.argv[1:] if a != '--quiet']; quiet = '--quiet' in sys.argv
todo = [p for p in args if p not in cache]


def text(el):
    return re.sub(r'\s+', ' ', ''.join(el.itertext())).strip() if el is not None else ''


for k in range(0, len(todo), 100):
    url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    data = urllib.parse.urlencode({'db': 'pubmed', 'id': ','.join(todo[k:k + 100]), 'retmode': 'xml'}).encode()
    for attempt in range(4):
        try:
            xml = urllib.request.urlopen(urllib.request.Request(url, data=data, headers={'User-Agent': 'osdb-audit/1.0'}), timeout=60).read()
            break
        except Exception:
            time.sleep(3 + 3 * attempt)
    time.sleep(0.4)
    for art in ET.fromstring(xml).findall('.//PubmedArticle'):
        pmid = art.findtext('.//MedlineCitation/PMID')
        a = art.find('.//Article')
        parts = []
        for t in a.findall('./Abstract/AbstractText'):
            lab = t.get('Label')
            s = text(t)
            parts.append(f'{lab}: {s}' if lab and lab.upper() != 'UNLABELLED' else s)
        auth = []
        for au in a.findall('./AuthorList/Author'):
            ln, ini = au.findtext('LastName'), au.findtext('Initials')
            if ln:
                auth.append(f"{ln}, {'.'.join(ini) + '.' if ini else ''}")
            elif au.findtext('CollectiveName'):
                auth.append(au.findtext('CollectiveName'))
        ji = a.find('./Journal/JournalIssue')
        year = ji.findtext('./PubDate/Year') or (ji.findtext('./PubDate/MedlineDate') or '')[:4]
        doi = next((e.text for e in art.findall('.//ArticleIdList/ArticleId') if e.get('IdType') == 'doi'), '') or \
              next((e.text for e in a.findall('./ELocationID') if e.get('EIdType') == 'doi'), '')
        cache[pmid] = {
            'title': text(a.find('./ArticleTitle')), 'abstract': ' '.join(parts),
            'authors': auth, 'journal': a.findtext('./Journal/Title') or '', 'year': year,
            'volume': ji.findtext('./Volume') or '', 'number': ji.findtext('./Issue') or '',
            'pages': (a.findtext('./Pagination/MedlinePgn') or '').replace('-', '--'),
            'doi': doi or '', 'pubtypes': [text(p) for p in a.findall('./PublicationTypeList/PublicationType')],
        }
json.dump(cache, open(CP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if not quiet:
    for p in args:
        x = cache.get(p)
        if not x:
            print(f'== {p}: NOT FOUND'); continue
        print(f"== {p} | {x['year']} | {x['journal'][:50]} | {'/'.join(t for t in x['pubtypes'] if t != 'Journal Article')} | doi {x['doi']}")
        print('   T:', x['title'])
        print('   A:', x['abstract'] or '(no abstract)')
