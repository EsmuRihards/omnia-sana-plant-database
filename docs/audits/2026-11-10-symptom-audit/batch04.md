# Symptom-tool audit - batch 4 of 19 (2026-11-11) - FIXED

Plants 31-40: cannabis-sativa, capsella-bursa-pastoris, capsicum-annuum, carum-carvi,
centaurium-erythraea, centella-asiatica, chamerion-angustifolium, chelidonium-majus,
cinnamomum-cassia, cinnamomum-verum. 93 pairs, 93 articles.

Owner decisions this batch (now DATA_PRINCIPLES invariant 10):
- Clinical evidence on unnamed "cinnamon" goes to **Cassia only**.
- A plant's **signature compound** (capsaicin) counts as evidence, labelled in the note.
- A plant is **never listed for the organ its own serious warning is about**.

Result: 113 changes; site-wide pairs 1,487 -> 1,467; 3 phantom refs deleted. Log: `batch04_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| True cinnamon / blood sugar (10), cardiovascular (10), metabolic (9) | 7 "cinnamon" studies never name the species. Khan 2003 and Akilen 2010 used cassia | Moved to Cassia. True cinnamon keeps its one C. zeylanicum RCT: blood sugar 5. Its LDL result was null, so cardiovascular is dropped |
| Fireweed / 8 pairs | REF-0146 and REF-0317 are **phantoms**: their DOIs resolve to a tomato-virus paper and a yeast-media paper, and neither title exists | Purged; only *E. angustifolium* studies remain |
| Chili / 11 pairs | REF-0021 is a **phantom** (dead DOI, title not found) | Purged |
| Gotu kola / cognitive function (7) | Its SR (REF-0568) says "not strong evidence ... cognitive function" | Moved to null_result_ids. Score 7 -> 2 |
| Greater celandine / liver support | Its own serious warning is liver injury | Dropped |
| Gotu kola / hemorrhoids (8) | Sources were a CVI review and a Cochrane review pooling 10 phlebotonics | Removed; score 1 |

## Medium

- **Chili.** Capsaicin-patch evidence is about neuropathic pain, so it was removed from arthritis
  and back pain. The "spicy foods" cohort names no plant.
- **Caraway.** The EU monograph covers bloating and flatulence only.
- **Centaury.** The EU monograph covers indigestion and loss of appetite only. The other pairs
  keep the Herbal Reality page, which names them.
- **Hemp.** The food review names none of its 3 pairs.
- **Greater celandine.** Its review names anti-inflammatory, antimicrobial and analgesic uses only.
  The HPV/warts latex paper was added for warts.
- **True cinnamon.** "Body into Balance" (a book) is unverifiable.
- **Retags.** 15 refs were retagged, among them two cinnamon RCTs tagged "clinical" or "traditional"
  and a Cochrane review tagged "rct".

Validate 0 errors; refs 3212/3212.
