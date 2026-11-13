# Deep audit - batch 16 (2026-11-13)

Plants 151-160: figwort, skullcap, saw palmetto, milk thistle, Canadian goldenrod,
European goldenrod, wood betony, chickweed, comfrey, clove. 75 pairs before, 72 after.

Same two-part pass as batches 14-15: the strict `!NAME` check plus the deep checks.

Result:
- 195 changes.
- 27 refs added (REF-3764..3790); 4 deleted.
- Log: `d16_changes.tsv`. Fixer: `fix_deep16.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Saw palmetto / prostate, urinary | The 2023 Cochrane review ("little to no benefit"), a 2021 MA and a CAM review all found no benefit, yet were cited as support. The superseded 2012 Cochrane (and its journal version) was still cited | The three moved to no-effect. The 2012 versions were purged and deleted. The two large US placebo trials (CAMUS 2011 at up to triple dose; Bent 2006, NEJM) added as no-effect. Note rewritten |
| Comfrey / wounds, skin irritation | The record's own safety note says "do not apply to broken skin (open wounds, damaged/irritated skin)" | Both dropped (organ-of-own-warning rule) |
| Comfrey | Five placebo or diclofenac RCTs were never wired; pain and swelling had empty notes | Added: acute back pain, knee osteoarthritis, ankle sprain vs placebo, and vs diclofenac. Also an injection-bruise RCT and the 2014 Cochrane LBP review (names comfrey). Arthritis, back pain and bruising are now verified |
| Milk thistle / liver | Cochrane 2007 (alcoholic and viral hepatitis: "question the beneficial effects") and the large SyNCH hepatitis C trial (no benefit) were missing. A safety review (tagged RCT) was cited as liver and detox evidence | Both nulls added. NAFLD meta-analyses, the 2025 Cochrane MASLD review (low certainty) and an anti-TB liver-injury RCT added. Safety review retagged and removed from detox and three actions |
| Wood betony | The Naturopathic Herbalist page has no references. It was the only source for bloating, cramps, muscle spasm, a safety note and four actions | Purged and deleted. Cramps and muscle spasm dropped. PeaceHealth (5 references) and Grieve now carry the remaining traditional uses. The unsourced "may lower blood pressure" warning was removed |
| Figwort | The WebMD page returns 404. The cramps and muscle-spasm pairs rested on a rabbit-gut antispasmodic study | WebMD purged and deleted. Cramps, muscle spasm and UTI (diuretic only) dropped. Grieve added |
| Clove | A 2012 Indian review and a generic "WHO Monographs" citation were pinned to all 11 pairs. Neither could be read (404; 403) | Kept only where Grieve or an RCT agrees: pain, oral health, indigestion, bloating. Removed elsewhere |
| European goldenrod | A 1990 saponin chemistry paper (no abstract) was pinned to 6 pairs. The EU monograph was cited for swelling and UTI, but it covers only flushing the urinary tract in minor complaints | Removed from those pairs. Grieve added for gravel and stone |
| Chickweed | Chevallier and Grieve were pinned to all 4 pairs. Grieve's entry names inflammation, itch and skin complaints, not rheumatism or eczema | Removed from arthritis. Eczema is now mechanistic only. The entry-specific Grieve ref added |
| Skullcap / anxiety | The 2014 crossover RCT found no anxiety difference vs placebo (only overall mood improved) but was cited as support | Moved to no-effect for anxiety. Kept for mood, stress and nervous tension |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Milk thistle | hot flashes | placebo RCT |
| Milk thistle | menopause | placebo RCT |
| Milk thistle | wounds | RCT (episiotomy ointment) |
| Milk thistle | skin irritation | placebo RCT (radiation dermatitis gel) |

Also added:
- Saw palmetto: three small Japanese placebo RCTs on mild urinary frequency (urinary support).
- Milk thistle: a type 2 diabetes RCT (blood sugar).
- Clove: the clove gel vs benzocaine vs placebo RCT (pain, oral health).
- Grieve entries: figwort, wood betony, chickweed, cloves, skullcap, golden rod.

## New safety notes

- **European goldenrod:** in lab tests the extract weakened amikacin and ciprofloxacin against urinary E. coli (caution).
- **Wood betony:** caused some DNA damage in human blood cells in vitro but was not mutagenic in the Ames test (info). Its two older notes were re-sourced to PeaceHealth.

## Other fixes

- Canadian goldenrod: cell, enzyme and plant-pathogen studies were removed from liver, infection, cancer, arthritis and swelling (none names the symptom). The empty notes are now filled.
- Six study_type retags.

## Gaps (not added)

- **Saw palmetto:** three hair-loss RCTs (no hair-loss condition in the vocabulary).
- **Milk thistle:** OCD vs fluoxetine, melasma and mucositis RCTs (no matching condition).
- **Clove:** anal fissure cream RCT (no condition). Not added because the evidence falls short:
  - open-label blood-sugar study;
  - chronic itch trial (between-group P > .05);
  - post-spinal headache aromatherapy (not significant).
- **Clove:** the WHO Flos Caryophylli monograph could not be fetched (403), so the WHO citation could not be checked per use.
- **Comfrey:** the abrasion-wound RCT used Russian comfrey (*S. x uplandicum*), a different species. Two RCTs combined comfrey with other actives.

Validate 0 errors; refs 3551/3551.
