"""Deep re-sweep dossier (2026-11-12 re-sweep of batches 1-12 at batch-13 depth). Run from the repo root.
Usage: python docs/audits/2026-11-10-symptom-audit/deep_dossier.py <batch_no>
Writes deep/dNN_dossier.md (compact, for reading) and deep/dNN_refs.json (full fields of every ref shown).
Per pair: status, note, direct (D), no-effect (N), excluded (X) and mechanistic cards (M, ref<action).
Per ref: tag, year, journal, title, ids, the conclusion of its abstract, and screens:
  !NULL  a no-effect / uncertain-efficacy phrase anywhere in the abstract (inv. 7)
  !SP    neither the genus nor a common name appears in title+abstract (inv. 10)
  !TAG   title wording disagrees with study_type (review tagged rct, trial tagged preclinical, ...)
  !INF   note says "inferred" on a pair that has direct sources (batch-13 note rule)
Screens only flag; every call is made by hand."""
import json, os, re, sys
sys.path.insert(0, 'scripts')
from build import parse_bibtex  # noqa: E402

b = int(sys.argv[1]); start = (b - 1) * 10
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'deep'); os.makedirs(OUT, exist_ok=True)
E = {e['ref_id']: dict(e['fields'], _type=e['type'], _key=e['key']) for e in parse_bibtex(open('bibliography.bibtex', encoding='utf-8').read())}
P = sorted(json.load(open('build/plants.json', encoding='utf-8'))['plants'], key=lambda p: p['id'])[start:start + 10]
V = {c['id']: c for c in json.load(open('build/vocab.json', encoding='utf-8'))['conditions']}
S = {p['id']: {i['condition']: i for i in p['indications']} for p in json.load(open('build/symptoms.json', encoding='utf-8'))['plants']}

NULL = re.compile(r"[^.]*\b(no (statistically )?significant|not (statistically )?significant|non-?significant|did not (significantly )?"
                  r"(improve|reduce|differ|affect|show|change|alter|lower|decrease|increase|prevent|shorten)|no (clear |convincing |reliable |"
                  r"good |sufficient |conclusive |definitive |consistent )?(evidence|effect|difference|benefit|improvement)s?\b|insufficient evidence|"
                  r"inconclusive|lack of (convincing |good |reliable )?evidence|not (been )?(demonstrated|established|proven)|no better than|"
                  r"failed to|uncertain|does not support|not supported|cannot be recommended|not recommended|weak evidence|"
                  r"limited evidence|very low|not effective|ineffective|no more effective)[^.]*\.", re.I)
REVIEW_T = re.compile(r'\breview\b|overview|meta-analy|systematic', re.I)
TRIAL_T = re.compile(r'randomi[sz]ed|placebo|double-blind|clinical trial|\btrial\b|patients|volunteers|participants', re.I)
PRECL_T = re.compile(r'\bin vitro\b|\brats?\b|\bmice\b|\bmouse\b|cell line|\bcells\b|murine|in silico|zebrafish', re.I)


def tagflag(f):
    t, st = f.get('title', ''), f.get('study_type', '')
    if REVIEW_T.search(t) and st in ('rct', 'clinical', 'preclinical', 'traditional'):
        return f'!TAG review-title/{st}'
    if re.search(r'systematic review|meta-analy', t, re.I) and st == 'narrative-review':
        return '!TAG SR-title/narrative'
    if TRIAL_T.search(t) and not REVIEW_T.search(t) and st in ('preclinical', 'traditional', 'narrative-review'):
        return f'!TAG trial-title/{st}'
    if PRECL_T.search(t) and not TRIAL_T.search(t) and st in ('rct', 'clinical'):
        return f'!TAG lab-title/{st}'
    return ''


def conclusion(ab):
    ab = re.sub(r'\s+', ' ', ab or '').strip()
    m = re.search(r'(CONCLUSIONS?|Conclusions?|INTERPRETATION|Interpretation|SIGNIFICANCE)\s*:?\s*(.*)$', ab)
    if m and len(m.group(2)) > 40:
        return m.group(2)[:420]
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z])', ab)
    return ' '.join(sents[-2:])[:420]


# !NAME: a DIRECT card whose title+abstract never names the symptom (2nd-pass strict-match screen, added
# 2026-11-13 for batches 14-19 which never had the 2nd pass). Refs with no abstract are not judged (?).
STEMS = {
    'arthritis': 'arthrit|osteoarth|rheumat|joint|gout', 'blood-sugar': 'glucose|glyc|diabet|insulin|sugar',
    'metabolic-support': 'metabolic|obes|weight|diabet|insulin|lipid|glyc', 'high-cholesterol': 'cholesterol|lipid|triglycer|LDL',
    'high-blood-pressure': 'blood pressure|hypertens|antihypertens', 'cardiovascular-support': 'cardi|heart|vascular|blood pressure|atheroscl|coronary|lipid|platelet',
    'inflammation': 'inflamm', 'infection': 'infect|antimicrob|antibacter|antifung|antivir|bacteri|fung|virus|viral|microb',
    'wounds': 'wound|heal|ulcer|burn|cut', 'skin-irritation': 'skin|derma|eczema|pruri|itch|cutane|topical',
    'cancer': 'cancer|tumo|carcino|neoplas|leuk|lymphom|melanom|apopto|antiprolif', 'cold': 'cold|influenza|respiratory infect|URTI|rhinovirus|flu',
    'immune-support': 'immun', 'cognitive-function': 'cogni|memory|dementia|alzheimer|neuroprot|learning', 'memory': 'memory|cogni|dementia|alzheimer|learning',
    'anxiety': 'anxi|anxiolytic', 'depression': 'depress', 'stress': 'stress', 'insomnia': 'sleep|insomn|sedat|hypnot', 'nervous-tension': 'nervous|tension|anxi|restless|calm',
    'fatigue': 'fatigue|tired|energy|vitality|exhaust', 'headache': 'headache|migraine|cephal', 'migraine': 'migraine',
    'pain': 'pain|analges|antinocicep|ache', 'back-pain': 'back pain|low back|lumbar|backache', 'muscle-spasm': 'muscle|spasm|cramp|myorelax',
    'menstrual-cramps': 'menstru|dysmenor|period pain', 'pms': 'premenstru|PMS|mastalgia|breast pain', 'menopause': 'menopaus|climacter|hot flash|hot flush',
    'hot-flashes': 'hot flash|hot flush|vasomotor', 'indigestion': 'dyspeps|indigest|digest|gastr|stomach', 'bloating': 'bloat|flatul|carminat|gas|colic|meteoris',
    'nausea': 'nause|vomit|emesis|antiemet', 'constipation': 'constipat|laxat|bowel', 'diarrhea': 'diarrh|dysenter|antidiarr', 'ibs': 'irritable bowel|IBS',
    'ibd': 'colitis|crohn|inflammatory bowel|IBD', 'acid-reflux': 'reflux|heartburn|GERD|dyspeps', 'liver-support': 'liver|hepat|NAFLD',
    'kidney-support': 'kidney|renal|nephr', 'urinary-support': 'urin|bladder|diure', 'uti': 'urinary tract|UTI|cystitis|bladder infect',
    'prostate-support': 'prostat|BPH|urinary', 'cough': 'cough|antituss|expector', 'bronchitis': 'bronch', 'asthma': 'asthm|bronchodil',
    'respiratory-support': 'respirat|lung|airway|bronch|pulmon|cough|catarrh|COPD', 'sinusitis': 'sinus|rhinosinus', 'sore-throat': 'throat|pharyn|tonsil',
    'allergy': 'allerg|histamin|rhinitis|hay fever', 'eczema': 'eczema|dermatitis|atopic', 'psoriasis': 'psoria', 'acne': 'acne',
    'oral-health': 'oral|gingiv|periodont|dental|mouth|plaque|mucositis|stomatit|caries', 'bad-breath': 'halitos|breath|oral',
    'hemorrhoids': 'hemorrhoid|haemorrhoid|piles', 'varicose-veins': 'varicose|venous|vein', 'bruising': 'bruis|hematoma|haematoma|contusion',
    'swelling': 'oedema|edema|swelling|diure', 'fever': 'fever|antipyret|pyrex', 'earache': 'ear|otitis', 'eye-strain': 'eye|ocular|vision|retin',
    'appetite-loss': 'appetit|anorex|bitter', 'detox': 'detox|liver|hepat', 'heavy-bleeding': 'menorrh|bleed|haemostat|hemostat',
    'fertility': 'fertil|concept|ovulat|sperm', 'low-libido': 'libido|sexual|erectile|aphrodis', 'lactation-support': 'lactat|milk|galactag|breastfeed',
    'pregnancy-support': 'pregnan|labou?r|nausea', 'muscle-soreness': 'muscle|sore|DOMS|exercise', 'warts': 'wart|verruc|papilloma',
}
def names_symptom(r, cond):
    f = E.get(r) or {}
    txt = ' '.join(str(f.get(k, '')) for k in ('title', 'abstract', 'summary'))
    if not f.get('abstract') and not f.get('summary'):
        return None
    pat = STEMS.get(cond) or re.escape(V.get(cond, {}).get('label', cond).split()[0])
    return bool(re.search(pat, txt, re.I))

lines, refs_out = [f'# Deep dossier batch {b}'], {}
for p in P:
    pid = p['id']; genus = p['scientific_name'].split()[0]
    names = [genus] + [n for n in p.get('common_names', []) if len(n) > 3]
    namepat = re.compile('|'.join(re.escape(n.split()[-1] if ' ' in n and n != genus else n) for n in names), re.I)
    acts = {a['action']: a for a in p.get('actions', [])}
    serious = [c.get('note', '')[:160] for c in p.get('contraindications', []) if (c.get('severity') or '') == 'serious']
    lines.append(f"\n## {pid} - {p['scientific_name']} - {', '.join(p.get('common_names', [])[:3])}")
    if serious:
        lines.append('SERIOUS: ' + ' || '.join(serious))
    lines.append('actions: ' + '; '.join(f"{a}={acts[a].get('reference_ids', [])}" for a in acts))
    used = {}
    for i in p.get('indications', []):
        c = i['condition']; D = i.get('reference_ids', []); X = i.get('mechanistic_exclude_ids', []); N = i.get('null_result_ids', [])
        M = []
        for a in V.get(c, {}).get('related_actions', []):
            for r in (acts.get(a, {}).get('reference_ids') or []):
                if r not in D and r not in X and r not in N:
                    M.append(f'{r}<{a}')
        sh = S.get(pid, {}).get(c)
        ev = f"ev{sh['evidence']}" if sh else 'NOT-SHOWN'
        note = i.get('note', '')
        fl = ' !INF' if D and 'inferred' in note.lower() else ''
        nn = [r for r in D if names_symptom(r, c) is False]
        if nn:
            fl += ' !NAME' + str(nn)
        lines.append(f"- **{c}** [{i.get('status')},{ev}]{fl} note=\"{note}\"")
        lines.append(f"    D={D} N={N} X={X} M={M}")
        for r in D: used.setdefault(r, []).append('D:' + c)
        for r in N: used.setdefault(r, []).append('N:' + c)
        for m in M: used.setdefault(m.split('<')[0], []).append('M:' + c)
    for a in acts:  # action refs not shown anywhere still matter (nulls hiding in actions)
        for r in acts[a].get('reference_ids') or []:
            used.setdefault(r, []).append('A:' + a)
    for r in sorted(used):
        f = E.get(r)
        if not f:
            lines.append(f'  !! {r} NOT IN BIB'); continue
        refs_out[r] = f
        ab = f.get('abstract', '')
        ids = ' '.join(x for x in (f"pmid:{f['pmid']}" if f.get('pmid') else '', f"doi:{f['doi']}" if f.get('doi') else '') if x) or 'NO-ID'
        flags = [tagflag(f)]
        if ab and not namepat.search(f.get('title', '') + ' ' + ab):
            flags.append('!SP')
        uses = sorted(set(used[r]))
        lines.append(f"  {r} [{f.get('study_type')}] {f.get('year', '')} {f.get('journal', f.get('publisher', ''))[:40]} | "
                     f"{f.get('title', '')[:150]} | {ids} {' '.join(x for x in flags if x)}")
        lines.append(f"     used: {', '.join(uses)}")
        if ab:
            lines.append(f"     C: {conclusion(ab)}")
            nulls = [m.group(0).strip() for m in NULL.finditer(ab)]
            for s in nulls[:3]:
                lines.append(f"     !NULL: {s[:300]}")
        else:
            lines.append('     (no abstract)')
open(os.path.join(OUT, f'd{b:02d}_dossier.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
json.dump(refs_out, open(os.path.join(OUT, f'd{b:02d}_refs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('plants:', [p['id'] for p in P], 'refs:', len(refs_out), 'chars:', len('\n'.join(lines)))
