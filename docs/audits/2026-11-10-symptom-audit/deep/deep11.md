# Deep re-sweep - batch 11 (2026-11-13)

Plants 101-110: lemon balm, peppermint, bitter melon, noni, catnip, black seed, holy basil,
evening primrose, olive, field restharrow. 87 pairs before, 105 after.

Method as in `deep01.md`. Result:
- 158 changes.
- 50 refs added (REF-3655..3704); 4 deleted.
- Log: `d11_changes.tsv`. Fixer: `fix_deep11.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Black seed | Three held MAs (blood pressure; diabetes glucose and lipids) were never wired. Every pair was inferred only | Wired. Six new pairs from MAs |
| Peppermint | No IBS pair despite four positive MAs. Two recent RCTs (incl. PERSUADE) were null | IBS pair added. The nulls are recorded |
| Peppermint | "Fasciolosis in humans" and a rat kidney study were filed under all six actions | Removed (the fasciolosis paper deleted) |
| Lemon balm, peppermint / muscle spasm | Inferred from gut antispasmodic studies. Off-target | Dropped |
| Olive / blood sugar | Three MAs found no glycaemic effect (EVOO, olive leaf) | Recorded as no-effect. Note says so |
| Evening primrose / breast pain, PMS | A 2021 mastalgia MA found it no better than placebo; a PMS review found little value | Recorded as no-effect |
| Bitter melon / blood sugar | A 2023 SR found the effect cannot be determined | Recorded beside the Cochrane null |
| Field restharrow | Three refs are of *Ononis spinosa* | Deleted |
| Noni | A safety review was filed under seven actions | Removed |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Lemon balm | anxiety | MA + 2 RCTs |
| Lemon balm | stress | RCT + EU monograph |
| Lemon balm | high cholesterol | 2 held MAs + RCT |
| Lemon balm | high blood pressure | MA + RCT (a T2D RCT is no-effect) |
| Peppermint | IBS | 4 MAs + held SR (2 null RCTs recorded) |
| Peppermint | nausea | 2 postoperative RCTs |
| Bitter melon | high cholesterol | MA |
| Noni | high cholesterol | RCT (smokers) |
| Noni | nausea | postoperative RCT |
| Black seed | high blood pressure, high cholesterol, cardiovascular support | MAs |
| Black seed | asthma, allergy, liver support | MAs |
| Evening primrose | menopause, high cholesterol | MAs + RCT |
| Olive | menopause | held RCT (olive leaf) |
| Olive | oral health, cognitive function | MAs |

Also added:
- Peppermint: the tension-headache RCT (a foot-bath RCT is no-effect) and a nipple-pain MA.
- Lemon balm: sleep RCTs and a herpes labialis SR.
- Olive: CV MAs, an inflammation MA, a pressure-ulcer MA, and the herpes labialis SR.
- Holy basil: a diabetes RCT.
- Evening primrose: a hot-flash RCT and an atopic dermatitis RCT (beside the Cochrane null).
- Noni: a preclinical cancer SR. A URTI polysaccharide RCT is no-effect.
- Black seed: glycaemic, metabolic syndrome and inflammation MAs.

## Gaps (not added)

- **Lemon balm:** palpitations RCT (no matching condition). Psoriasis RCT (no between-group difference reported).
- **Olive cholesterol:** an MA found trivial effects.
- **Evening primrose:** cervical-ripening trials (pregnancy use).

Validate 0 errors; refs 3475/3475.
