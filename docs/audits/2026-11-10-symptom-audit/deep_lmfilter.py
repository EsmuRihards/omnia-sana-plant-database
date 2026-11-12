"""Filter a landmark list to single-plant human SR/MA/RCTs. Usage: python deep_lmfilter.py dNN_landmark.md plant-prefix [plant-prefix ...] [--max N]"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
args = sys.argv[2:]; mx = 45
if '--max' in args:
    i = args.index('--max'); mx = int(args[i + 1]); args = args[:i] + args[i + 2:]
txt = open(sys.argv[1], encoding='utf-8').read().split('\n## ')
BAD = re.compile(r'decoction|formula|granule|containing|compound|\btang\b|powder\b|capsule|patent|combination|broiler|chicken|\bpigs?\b|piglet|calves|cattle|dairy|goat|sheep|fish|rabbit|quail|\bmice\b|\brats?\b|in vitro|animal (model|stud)|preclinical|Yupingfeng|Shenqi|injection|network pharmacology|mastitis|weaned|laying hens|poultry', re.I)
for blk in txt[1:]:
    lines = blk.split('\n'); head = lines[0][:95]
    if any(head.startswith(a) for a in args):
        keep = [l for l in lines[1:] if l.startswith('- ') and not BAD.search(l)]
        print('##', head, len(keep))
        for l in keep[:mx]:
            print(l[:178])
