# Research-deepening batch 32 (2026-11-27)

**Plants:** Canadian goldenrod, European goldenrod, wood betony, chickweed, comfrey.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Species traps avoided:**
  - Iranian "wood betony" (*Stachys lavandulifolia*).
  - Russian comfrey (*Symphytum × uplandicum*, the Traumaplant cream).
  - Rayless goldenrod (*Isocoma*).
  - Mouse-ear chickweed.

**Outcome:**
- **Search volume:** about 230 PubMed hits (comfrey about 160) and about 15 abstracts read.
- **New references:** 3 (REF-5667..5669).
- **Symptom-tool pairs:** 1,523 (unchanged; this batch added safety data only).
- **Checks:** validate passes, with refs cited 4,444 / declared 4,444. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r32_changes.tsv`; fixer `../fix_r32.py`.

## Score changes

None. Comfrey arthritis stays at 5. The 2013 Cochrane topical-herb review bases its comfrey result on the one knee trial already cited, so it was not counted twice.

## Safety and other tool data

- **Comfrey:**
  - New foraging **warning**: a woman died after drinking tea made from foxglove she had mistaken for comfrey. The approved foxglove lookalike entry cites only non-fatal cases.
  - New info note: only 0.04-0.22% of the main comfrey alkaloid passed through human skin from an ointment (lab study). Internal use stays unsafe.
- **Chickweed:** new skin caution. Recurrent erythema multiforme after weeding, with patch-test reactions to fresh chickweed leaves.

**Draft interactions:** none new. Eleven are still pending.

## For the owner (queued for the end-of-campaign review)

1. **The comfrey foraging note uses severity "warning"** (a fatal foxglove confusion), as for sorrel in batch 29. You may also want the fatal case added to the approved foxglove lookalike entry itself.

## Gaps and settled plants

- **Canadian goldenrod:** settled; no human study.
- **European goldenrod:** settled; only combinations (Phytodolor) and unrelated *Isocoma*.
- **Wood betony:** settled; the only RCT used *S. lavandulifolia*.
- **Chickweed:** settled for efficacy.
- **Comfrey:** back pain (8) and pain (7) were not padded. The myalgia, wound and sprain cream trials used Russian comfrey.

## Rejected or not added (main reasons)

- **Combinations:** comfrey + tannic acid, comfrey + methyl nicotinate, 4Jointz, Phytodolor, Traumeel (homeopathic).
- **Other species:** *Symphytum × uplandicum*, *Stachys lavandulifolia*, *Isocoma pluriflora*.
- **No abstract:** a goldenrod dermatitis case, a betony lactation study.
