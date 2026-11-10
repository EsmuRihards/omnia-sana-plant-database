"""Pre-flag direct refs whose title+abstract never name their symptom (DATA_PRINCIPLES inv. 9).
A hit is only a screen: every flag is then judged by hand (books have no abstract).
Usage: python mention_check.py <db_dir> <start> <count>
"""
import json, os, re, sys

db, start, count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
sys.path.insert(0, os.path.join(db, 'scripts'))
from build import parse_bibtex  # noqa: E402

E = {e['ref_id']: e['fields'] for e in parse_bibtex(open(os.path.join(db, 'bibliography.bibtex'), encoding='utf-8').read())}
V = {c['id']: c for c in json.load(open(os.path.join(db, 'build/vocab.json'), encoding='utf-8'))['conditions']}
P = sorted(json.load(open(os.path.join(db, 'build/plants.json'), encoding='utf-8'))['plants'], key=lambda p: p['id'])[start:start + count]

# condition id -> extra words (close pharmacological equivalents, owner-approved 2026-11-10)
KW = {
    'arthritis': 'arthrit|rheumat|joint|gout|osteoarth', 'bruising': 'bruis|contusion|haematoma|hematoma|ecchymo',
    'cancer': 'cancer|tumo|carcinom|antiprolif|leuk|neoplas|antineoplas', 'inflammation': 'inflamm',
    'skin-irritation': 'skin|dermat|eczem|pruri|itch|rash', 'wounds': 'wound|vulner|ulcer|burn',
    'infection': 'infect|antimicrob|antibacter|antifung|antivir|bacteri|pathogen', 'urinary-support': 'urin|bladder|lower urinary',
    'uti': 'urinary tract infection|\\buti\\b|cystitis|bladder infect', 'menstrual-cramps': 'menstru|dysmenor|period pain',
    'muscle-spasm': 'spasm|cramp', 'swelling': 'swell|oedem|edem|fluid retention', 'cold': 'common cold|\\bcolds?\\b|influenza|\\bflu\\b|respiratory infection',
    'fever': 'fever|febri|antipyr|diaphor', 'diarrhea': 'diarrh|dysenter', 'indigestion': 'indigest|dyspeps|upset stomach',
    'bloating': 'bloat|flatul|carminat', 'appetite-loss': 'appetite|anorex', 'heavy-bleeding': 'menorrhag|heavy menstrua|nosebleed|epistaxis',
    'anxiety': 'anxi', 'depression': 'depress', 'stress': 'stress(?! response)|adaptogen', 'nervous-tension': 'nervous|tension|anxiolyt|restless',
    'cognitive-function': 'cogni|alzheim|dementia|learning', 'memory': 'memory|amnes|alzheim|dementia', 'insomnia': 'insomn|sleep|sedat|hypnot',
    'muscle-soreness': 'muscle sore|soreness|muscle damage', 'hot-flashes': 'hot fl|vasomotor|flush', 'menopause': 'menopaus|climacter',
    'pain': 'pain|analges|antinocic|ache', 'back-pain': 'back pain|lumbar|sciatic|lumbago', 'headache': 'headache|migraine|cephal',
    'hemorrhoids': 'haemorrhoid|hemorrhoid|piles', 'varicose-veins': 'varicose|venous insuff|chronic venous',
    'blood-sugar': 'glucose|glyc|diabet|insulin', 'cardiovascular-support': 'cardio|blood pressure|hypertens|cholesterol|heart|lipid',
    'immune-support': 'immun|resistance to colds', 'metabolic-support': 'metabolic syndrome|obes|weight|diabet',
    'sore-throat': 'throat|pharyn|tonsil|gargle', 'eczema': 'eczema|atopic', 'cough': 'cough|antituss|expector',
    'bronchitis': 'bronch', 'respiratory-support': 'respirat|bronch|airway|lung|cough|expector', 'nausea': 'nause|vomit|emesis|antiemet',
    'acid-reflux': 'reflux|heartburn|gerd|gastroesoph', 'constipation': 'constipat|laxat|purgat', 'ibs': 'irritable bowel|\\bibs\\b',
    'liver-support': 'liver|hepat', 'detox': 'detox|depurat|alterative', 'high-cholesterol': 'cholesterol|lipid|hyperlipid',
    'oral-health': 'oral|mouth|gingiv|dental|periodont|stomatit', 'psoriasis': 'psoria', 'acne': 'acne', 'allergy': 'allerg|hay fever|rhinit',
    'asthma': 'asthma', 'fatigue': 'fatigue|tired|energy|exhaust', 'eye-strain': 'eye|vision|retin|ocular', 'parasites': 'parasit|anthelmin|worm|helminth',
}

for p in P:
    for i in p['indications']:
        c = i['condition']
        words = KW.get(c, re.escape(c))
        syn = '|'.join(re.escape(s) for s in V.get(c, {}).get('consumer_synonyms', []))
        kw = re.compile(words + ('|' + syn if syn else ''), re.I)
        for r in i['reference_ids']:
            f = E.get(r, {})
            if not kw.search(f.get('title', '') + ' ' + f.get('abstract', '')):
                print(f"{p['id']}\t{c}\t{r}\t{f.get('study_type')}\t{f.get('title', '')[:90]}\t{'abs' if f.get('abstract') else 'NO-ABS'}")
