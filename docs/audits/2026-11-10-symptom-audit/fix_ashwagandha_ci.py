"""Source ashwagandha's general safety note (owner request 2026-11-13). Run from the repo root.
The old note had no references; it is rewritten to what NCCIH (2023) and two 2026 reviews state.
New refs REF-3878 (NCCIH page, read 2026-11-13 by the web-fetch agent), REF-3879..3880 (PubMed efetch)."""
import os, sys, copy
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib
import yamlsplice as Y

fixlib.DATE = '2026-11-13'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3879', '41502355', 'ashwagandhaadverseeffects', 'narrative-review'),
    ('REF-3880', '40887707', 'ashwagandhateratogenic', 'systematic-review'),
])
NEW['national2023ashwagandha'] = ('REF-3878', [
    ('author', 'National Center for Complementary and Integrative Health (NCCIH)'), ('title', 'Ashwagandha: Usefulness and Safety'),
    ('year', '2023'), ('url', 'https://www.nccih.nih.gov/health/ashwagandha'), ('note', 'REF-3878'), ('study_type', 'traditional'),
    ('summary', 'NCCIH fact sheet (last updated March 2023; 11 key references). May be safe short term (up to 3 months); long-term safety unknown. May cause drowsiness, stomach upset, diarrhoea and vomiting; rare liver injury. Avoid in pregnancy and breastfeeding; not recommended before surgery or with autoimmune or thyroid disorders; avoid with hormone-sensitive prostate cancer (may raise testosterone). May interact with diabetes and blood-pressure medicines, immunosuppressants, sedatives, anticonvulsants and thyroid hormone. Read 2026-11-13.')])

NOTE = ('Ashwagandha may be safe short term (up to 3 months); its long-term safety is unknown. It can cause drowsiness, stomach upset, '
        'diarrhoea and vomiting (NCCIH). Avoid it in pregnancy and while breastfeeding (NCCIH); evidence that it causes miscarriage or '
        'birth defects is inconclusive (systematic review). It is not recommended before surgery or for people with autoimmune or thyroid '
        'disorders, and it has been linked to an overactive thyroid and to allergic reactions (NCCIH; review). People with hormone-sensitive '
        'prostate cancer should avoid it because it may raise testosterone. It may interact with medicines for diabetes and high blood '
        'pressure, immunosuppressants, sedatives, anti-seizure medicines and thyroid hormone (NCCIH).')

PLAN = {'withania_somnifera': [('refadd', ['REF-3878'])]}
NOTES = {'withania_somnifera': 'Safety note #1 had no references (needs-review). Rewritten to what NCCIH REF-3878 (read 2026-11-13), the 2026 adverse-effects review REF-3879 and the 2026 teratogenicity SR REF-3880 state. Dropped as unsourced: "doses up to 600 mg/day for up to 12 weeks" and "not recommended for children without medical supervision"; "contraindicated due to potential abortifacient effects" replaced by NCCIH\'s "avoid in pregnancy" plus the SR finding that abortifacient evidence is inconclusive. Status needs-review -> verified.'}


def post():
    path = 'plants/withania_somnifera.yaml'
    text, d = Y.load(path); orig = copy.deepcopy(d)
    ci = d['contraindications'][0]
    assert ci['note'].startswith('Generally well-tolerated') and ci['reference_ids'] == []
    ci['note'] = NOTE
    ci['reference_ids'] = ['REF-3878', 'REF-3879', 'REF-3880']
    ci['status'] = 'verified'
    Y.save(path, text, d, {k for k in d if d[k] != orig.get(k)})


if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'ashwagandha safety note sourced', os.path.join(HERE, 'deep', 'ashwagandha_ci_changes.tsv'), new=NEW)
    post()
