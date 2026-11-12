# Deep re-sweep - batch 4 (2026-11-12)

Plants 31-40: hemp, shepherd's purse, chili, caraway, centaury, gotu kola, fireweed,
greater celandine, cassia, true cinnamon. 73 pairs before, 71 after.

Method as in `deep01.md`. Result:
- 83 changes.
- 22 refs added (REF-3485..3506); 3 refs corrected (DOI, year, PMID).
- Log: `d04_changes.tsv`. Fixer: `fix_deep04.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Cassia / blood sugar (10/10) | The Cochrane review ("insufficient evidence") and two null trials of *C. cassia* were missing | All three recorded as no-effect. The note now says the evidence is mixed |
| Cassia / heart, cholesterol | A cassia trial found no change in BP, lipids or arterial stiffness; another found no lipid change | Recorded as no-effect |
| Chili / pain | Only positive reviews were shown. The Cochrane review of low-concentration capsaicin creams (the OTC kind) found **no meaningful effect** | Recorded as no-effect. The note separates high-dose patches from creams |
| Chili / skin irritation, wounds | Its own safety note: topical preparations "may cause skin irritation" | Both inferred pairs dropped (contradicted) |
| Greater celandine / skin irritation, wounds | Its own safety note: the latex is "irritant and caustic - keep it away from broken skin" | Both dropped. Warts kept (intact skin) |
| Hemp | A CBD trial in Dravet-syndrome seizures was filed as evidence for four actions (analgesic, anti-inflammatory, antioxidant, sedative) | Removed from all four |
| True cinnamon / blood sugar | A trial of Ceylon cinnamon found no effect on after-meal glucose | Recorded as no-effect |

## Medium

- **Fireweed / bruising.** The only card was a wound-healing study, and a wound is not a bruise.
  Dropped.
- **Caraway.** Its EU monograph (bloating only) was removed from the antimicrobial and
  appetite-stimulant actions.
- **Metadata fixes.**
  - The Cochrane capsaicin DOI was malformed (`10.1002/http://...`).
  - REF-0169's DOI was dead; corrected to PMID 10363839.
  - REF-0022 corrected: Farmaco 2001 (bib said 2014), PMID 11482755.
- **Claim notes:** 39 rewritten. Gotu kola notes now label triterpene evidence as compound
  evidence.

## Added

| Plant | Pair | Source |
|---|---|---|
| Hemp | back-pain, pain | VER-01 phase 3 RCT (820 patients) |
| Hemp | arthritis | Topical hemp-seed-oil knee-OA RCT |
| Chili | arthritis | Topical capsaicin OA MA (compound evidence) |
| Chili | indigestion | Red-pepper dyspepsia RCT |
| Chili | **new** high-cholesterol | 2 MAs |
| Caraway | **new** ibs | Poultice RCT |
| Cassia | **new** diarrhea | RCT |
| Gotu kola | anxiety | Startle RCT |
| Gotu kola | cognition, memory | 2 RCTs |
| Gotu kola | wounds | Held SR + 2 RCTs |
| Gotu kola | psoriasis, skin irritation | Held studies, now direct |
| True cinnamon | blood-sugar | Ranasinghe SR (preclinical SR; owner: scores as SR) |

## Checked, not used

- Cannabinoid reviews pooling synthetic THC drugs.
- The Cochrane herbal low-back-pain plasters, which use *C. frutescens*.
- Menthacarin (a peppermint + caraway combination).
- A shepherd's purse postpartum-haemorrhage trial (no matching condition).

Validate 0 errors; refs 3292/3292.
