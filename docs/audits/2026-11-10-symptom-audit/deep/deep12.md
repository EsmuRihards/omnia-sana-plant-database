# Deep re-sweep - batch 12 (2026-11-13)

Plants 111-120: marjoram, oregano, yellow woodsorrel, small cranberry, Asian ginseng,
passionflower, guarana, pelargonium, butterbur, parsley. 79 pairs before, 83 after.

Method as in `deep01.md`. Result:
- 86 changes.
- 20 refs added (REF-3705..3724); 2 deleted.
- Log: `d12_changes.tsv`. Fixer: `fix_deep12.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Ginseng / memory | The Cochrane "no convincing evidence" review was shown as mechanistic support (it sat in the neuroprotective action) | Removed from the action. Recorded as no-effect for memory and cognition |
| Ginseng | A review concluding ginseng does not enhance physical performance supported the ergogenic action | Removed |
| Passionflower / anxiety | The herb network MA found it not significant vs placebo | Recorded as no-effect (batch-8 carry) |
| Marjoram | A carvacrol review (oregano's compound, not marjoram's) supported all six actions | Removed (kept as a reference) |
| Marjoram, butterbur / muscle spasm | Gut and airway smooth-muscle evidence. Off-target | Dropped |
| Yellow woodsorrel | Its two studies were a different *Oxalis* species and zinc-oxide nanoparticles | Deleted |
| Small cranberry | Most PubMed "cranberry" trials are American cranberry, a different species | Not used (inv. 10). Noted |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Pelargonium | cough | herbal cough MA (batch-2 carry) |
| Pelargonium | respiratory support (COPD) | RCT |
| Pelargonium | asthma | RCT |
| Guarana | fatigue | 2024 MA + 2 RCTs. A 2021 MA and 2 RCTs recorded as no-effect |
| Ginseng | high cholesterol | 2019 MA (2024 GRADE MA no-effect) |
| Ginseng | low libido | ED SR + female sexual dysfunction MA |

Also added:
- Passionflower: GAD and dental-anxiety RCTs, and held RCTs wired to anxiety, insomnia and stress.
- Pelargonium: a bronchitis RCT, children MAs, and a common-cold RCT.
- Oregano: a surgical-wound RCT.

Validate 0 errors; refs 3493/3493.
