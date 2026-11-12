"""Helpers for the deep re-sweep fixers (fix_deepNN.py): build new bibliography entries from the PubMed cache
written by deep_efetch.py (verbatim abstract, authors, journal, ids)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = json.load(open(os.path.join(HERE, 'deep', 'abstracts.json'), encoding='utf-8'))
SMALL = {'of', 'and', 'the', 'in', 'on', 'for', 'a', 'an', 'to', 'with', 'de', 'des', 'et', 'la', 'le', 'y', 'du'}


def _journal(j):
    j = re.sub(r'\s*\(.*?\)\s*', ' ', j).split(' : ')[0].strip()
    words = j.split()
    return ' '.join(w if (k and w.lower() in SMALL) else (w[:1].upper() + w[1:]) for k, w in enumerate(words))


def _clean(s):
    return re.sub(r'\s+', ' ', s.replace('{', '(').replace('}', ')')).strip()


def autokey(pmid, slug):
    import unicodedata
    last = CACHE[pmid]['authors'][0].split(',')[0]
    last = unicodedata.normalize('NFKD', last).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z]', '', last) + CACHE[pmid]['year'] + slug


def newrefs(spec):
    """spec: [(rid, pmid, slug, study_type), ...] -> {key: (rid, fields)} for fixlib.bib_edit(new=...)."""
    return dict(newref(p, rid, autokey(p, slug), st) for rid, p, slug, st in spec)


def newref(pmid, rid, key, study_type):
    x = CACHE[pmid]
    au = x['authors']
    author = au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]
    f = [('author', _clean(author)), ('title', _clean(x['title']).rstrip('.')), ('journal', _clean(_journal(x['journal']))),
         ('year', x['year'])]
    f += [(k, x[k]) for k in ('volume', 'number', 'pages') if x.get(k)]
    if x.get('doi'):
        f.append(('doi', x['doi']))
    f += [('pmid', pmid), ('note', rid), ('study_type', study_type), ('abstract', _clean(x['abstract']))]
    assert x['abstract'], (pmid, 'no abstract')
    return key, (rid, f)
