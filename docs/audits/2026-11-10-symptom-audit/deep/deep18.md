# Deep audit - batch 18 (2026-11-13)

Plants 171-180: white clover, fenugreek, coltsfoot, nettle, cranberry, bilberry, valerian,
dense-flowered mullein, great mullein, vervain. 81 pairs before, 77 after.

Same two-part pass as batches 14-17: the strict `!NAME` check plus the deep checks.

Result:
- 217 changes.
- 33 refs added (REF-3817..3849); none deleted.
- Log: `d18_changes.tsv`. Fixer: `fix_deep18.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Fenugreek | Cited "WHO Monographs Vol 1 (1999)" on 6 pairs and 3 actions, but fenugreek is not in volume 1 | Purged from this record. The real evidence was added instead: glycaemia MAs, plus new pairs below |
| Bilberry / eye strain | Its only card was a night-vision SR that concludes there is no support | Moved to no-effect. Two placebo RCTs on screen-work eye fatigue added |
| White clover | Generic Grieve was cited on all 9 pairs and 5 actions, but Grieve has no white clover entry. A no-abstract review was pinned to 9 pairs | Grieve purged. The review is kept only where a checkable study agrees. Bruising, cold, cramps and muscle spasm dropped |
| Valerian | Hoffmann (unverifiable) was the only card for arthritis, inflammation, skin irritation and muscle spasm | Dropped |
| Valerian / insomnia | A null internet RCT and an inconclusive SR were cited as support. Two further nulls were missing: a 2024 umbrella review ("lacks empirical support") and the Barton cancer RCT | All four recorded as no-effect. A positive postmenopausal RCT added. The note now gives both sides |
| Nettle | Generic Grieve and two papers were cited for actions they do not address. Cold, immune support and UTI had nothing naming them | Grieve's nettle entry now used for what it names. Cold, immune support and UTI dropped. A combination study and an unnamed BPH review removed |
| Cranberry / UTI | A lingonberry (*V. vitis-idaea*) review and a dose-comparison trial (no placebo) were cited as support. A null MS placebo RCT was missing | First two removed. MS trial recorded as no-effect. The note now says where cranberry does not help |
| Mullein (dense-flowered) | Bronchitis, earache and pain rested on the EU monograph and ESCOP. Neither names them (EU: sore throat with dry cough and cold); the ear-drop RCTs were combinations | Dropped |
| Vervain | A 2020 review was cited on 11 pairs it never names | Moved to mechanistic. The notes now say the remaining evidence is animal studies |
| Coltsfoot | Insomnia rested on a review that never mentions sleep. Its own PA warning advises against home internal use | Dropped. A PA-content paper removed from two actions |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Fenugreek | high cholesterol | 3 MAs |
| Fenugreek | high blood pressure | MA (systolic only) |
| Fenugreek | hot flashes, menopause | placebo RCT |
| Nettle | prostate support | 3 RCTs (incl. placebo crossover) |
| Nettle | blood sugar | 2 MAs |
| Nettle | hot flashes | placebo RCT |
| Cranberry | oral health | gingivitis RCT |
| Valerian | hot flashes | triple-blind placebo RCT |
| Valerian | anxiety, depression | haemodialysis RCT. The Cochrane anxiety review and the internet RCT are recorded as no-effect |
| Great mullein | wounds | episiotomy placebo RCT |

Also added:
- Nettle: a nettle-sting RCT for thumb osteoarthritis. A knee-pain pilot recorded as no-effect.
- Valerian: a dysmenorrhoea MA and an RCT.
- Bilberry: an inflammation RCT. A 2025 MA (no cholesterol effect) recorded as no-effect.
- Cranberry: a men's lower-urinary-tract-symptoms RCT. An overactive-bladder RCT (ITT null) recorded as no-effect.
- Grieve entries: nettle, valerian, great mullein, vervain, coltsfoot, fenugreek.

## Other fixes

13 study_type retags. Most were reviews tagged rct or traditional.

## Gaps (not added)

- **Fenugreek:**
  - dysmenorrhoea MA (effect "highly uncertain");
  - lactation RCT (no significant difference);
  - Alzheimer's RCT (within-group only).
- **Cranberry:** rheumatoid-arthritis juice RCT (within-group only).
- **Coltsfoot:** no cough or bronchitis pair, despite the traditional use: there is no RCT, and PAs make it toxic.
- **Bilberry:** Grieve's entry names diarrhoea, scurvy, gravel and diabetes, which match no existing pair, so it was not added.
- **Mullein:** the EU monograph PDF could not be read (EMA 429); the EMA page summary was used.

Validate 0 errors; refs 3605/3605.
