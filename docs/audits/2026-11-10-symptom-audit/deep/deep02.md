# Deep re-sweep - batch 2 (2026-11-12)

Plants 11-20: marshmallow, andrographis, dill, angelica, greater burdock, lesser burdock, bearberry,
arnica, wormwood, mugwort. 77 pairs before, 80 after.

Method as in `deep01.md`. Result:
- 84 changes.
- 23 refs added (REF-3426..3448); 2 deleted.
- Log: `d02_changes.tsv`. Fixer: `fix_deep02.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Arnica / wounds, skin irritation | Its own safety notes say "do not apply to broken or damaged skin, open wounds" and "prolonged topical use can also irritate the skin" | Both inferred pairs dropped (contradicted, inv. 11) |
| Arnica / bruising | Only traditional sources were shown. Three topical studies found **no benefit**: an arnica gel RCT, a 10% ointment RCT, and an arnica/bromelain SR ("insufficient data") | All three recorded as no-effect. Added the one positive RCT (20% ointment). The note now states the mixed result |
| Angelica / urinary support | The larger placebo-controlled trial of the leaf extract (SagaPro 2013: no overall benefit for nocturia) was missing | Recorded as no-effect. The note now gives both trials |
| Angelica / insomnia | Inferred only from an anxiety maze test filed under "sedative" | Ref removed from the sedative action. Pair dropped |
| Andrographis / cold | Its 2023 phase III trial found only a day-3 benefit | Recorded as no-effect. The 2004 SR and the KalmCold 2010 RCT (both positive) moved to direct |
| Dill / heart, cholesterol | A trial in people with high lipids found "no significant effect on lipid profile" | Recorded as no-effect. An updated SR (positive) added |

## Medium

- **Angelica.** REF-0397 is a columbianetin review that never names *A. archangelica*. It was
  purged and deleted.
- **Burdock.**
  - Purged from the actions: REF-0309, a WHO volume with no burdock monograph.
  - Also purged: REF-0313, unlocatable. It was deleted.
- **Bearberry.**
  - A bladder-cell toxicity study (hydroquinone "may exhibit negative properties") was cited as
    antimicrobial evidence. Removed from the actions.
  - Wounds dropped: the cards were off-target (acne bacterium; a monograph covering urinary use
    only).
- **Dill / wounds.** Inferred from an antimycobacterial lab screen. Off-target, so dropped.
- **Retags:** 2.
- **Claim notes:** 35 rewritten. One example: marshmallow's indigestion note claimed
  heartburn/reflux, but the EU monograph says mild gastric discomfort.

## Added under the owner rule (SR/RCT names the symptom and finds benefit)

| Plant | New pair | Source |
|---|---|---|
| Andrographis | ibd | Two HMPL-004 RCTs in ulcerative colitis |
| Andrographis | cough | Wagner 2015 MA ("strong evidence for A. paniculata") |
| Andrographis | fatigue | MS-fatigue pilot RCT |
| Andrographis | high-cholesterol | Triglyceride RCT (comparable to gemfibrozil) |
| Wormwood | ibd | Two placebo-controlled Crohn's RCTs |
| Marshmallow | infection | Held add-on RCT in vaginal thrush |
| Dill | high-cholesterol | SR + MA (with the null trial recorded) |
| Dill | anxiety | Labour-anxiety RCT |

Also wired to existing pairs:
- Andrographis: a knee-OA RCT (arthritis); a 1991 pharyngotonsillitis RCT (sore throat, fever).
- Burdock: a knee-OA RCT (inflammatory markers); a PCOS RCT.
- Arnica: a hand-OA RCT (gel non-inferior to ibuprofen).
- Dill: a candidiasis RCT.
- Garlic: Kojuri 2007, whose garlic arm lowered cholesterol.

## Gaps (no SR/RCT, not added)

- **Wormwood:** Commission E / EMA appetite-loss and dyspepsia uses have no appetite-loss pair.
- **Arnica:** topical arnica *increased* muscle pain after eccentric exercise (PMID 20807867). No
  muscle pair exists to record it on.
- **Moxibustion trials (mugwort):** not used. Moxibustion is a heat technique, not the plant's
  pharmacology.
- **Wagner 2015 MA:** it also gives "moderate evidence" for *P. sidoides*. To be wired in batch 12.

Validate 0 errors; refs 3237/3237.
