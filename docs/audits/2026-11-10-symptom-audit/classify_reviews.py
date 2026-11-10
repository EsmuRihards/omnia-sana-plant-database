"""Split the `review` evidence tier into systematic vs narrative (owner decision 2026-11-10).

Reads every bibliography entry whose study_type maps to the `review` tier
(systematic-review / meta-analysis / review) and prints a proposed class:
  SYS  - title or abstract shows a systematic method (keep current study_type)
  NAR  - no systematic-method signal -> narrative-review
  CHK  - abstract mentions a systematic review / meta-analysis but the method is unclear
Usage: python classify_reviews.py <db_dir> <out.tsv>
"""
import os, re, sys

db, out = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(db, 'scripts'))
from build import parse_bibtex  # noqa: E402

TITLE_SYS = re.compile(r"systematic(ally)?\s+review|meta-?\s?analy|metaanaly|cochrane|umbrella review|pooled analysis|network meta", re.I)
ABS_METHOD = re.compile(
    r"prisma|random[- ]effects?|fixed[- ]effects?|standardi[sz]ed mean difference|weighted mean difference|"
    r"pooled (?:analysis|estimate|effect|data|results)|forest plot|heterogeneity \(|i\s?2\s?=|i\^2|"
    r"(?:this|a|our|we (?:performed|conducted|undertook)(?: a)?) (?:updated )?(?:systematic review|meta-analysis)|"
    r"systematic(?:ally)? search(?:ed)?|were systematically|risk of bias|grade approach|"
    r"(?:\d+|[a-z]+) (?:randomi[sz]ed )?(?:controlled )?(?:trials|rcts|studies) (?:were|was) included|met (?:the|our) inclusion criteria",
    re.I)
ABS_MENTION = re.compile(r"systematic review|meta-?analy", re.I)

ents = parse_bibtex(open(os.path.join(db, 'bibliography.bibtex'), encoding='utf-8').read())
rows = []
for e in ents:
    f = e['fields']
    st = (f.get('study_type') or '').strip().lower()
    if st not in ('systematic-review', 'meta-analysis', 'review'):
        continue
    t, a = f.get('title', ''), f.get('abstract', '')
    if TITLE_SYS.search(t) or ABS_METHOD.search(a):
        cls = 'SYS'
    elif ABS_MENTION.search(a):
        cls = 'CHK'
    else:
        cls = 'NAR'
    rows.append((e['ref_id'], st, cls, t.replace('\t', ' '), (a[:400] or '(no abstract)').replace('\t', ' ').replace('\n', ' ')))
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('ref\tstudy_type\tclass\ttitle\tabstract_head\n')
    for r in rows:
        fh.write('\t'.join(r) + '\n')
from collections import Counter
print(Counter((r[1], r[2]) for r in rows))
