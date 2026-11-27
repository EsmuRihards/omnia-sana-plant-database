# Research-deepening batch 29 (2026-11-27)

**Plants:** blackberry, raspberry leaf, sorrel, butcher's broom, white willow.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Species and compound traps avoided:**
  - Bare "sorrel" (Jamaican sorrel is hibiscus).
  - Black raspberry and raspberry ketone.
  - Black mulberry labelled "blackberry".
  - BlackBerry devices.
  - Cyclo 3 Fort, a combination product.

**Outcome:**
- **Search volume:** about 640 PubMed hits (raspberry about 280) and about 40 abstracts read.
- **New references:** 8 (REF-5636..5643).
- **Symptom-tool pairs:** 1,519 (unchanged; this batch added safety data only).
- **Checks:** validate passes, with refs cited 4,418 / declared 4,418. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r29_changes.tsv`; fixer `../fix_r29.py`.

## Score changes

None. No new trial met the bar for a pair. The strong willow pairs (pain and back pain 9, arthritis 8) were not padded.

## Safety and other tool data

- **Sorrel:** new foraging **warning**. A woman mistook foxglove for common sorrel in a wild-plant smoothie and developed foxglove poisoning (persistent vomiting, ECG changes). A normal digoxin test does not rule this out.
- **Butcher's broom:**
  - New diabetes caution: diabetic ketoacidosis 5 days after starting butcher's broom.
  - New bowel caution: chronic watery diarrhoea and lymphocytic colitis with long-term Cyclo 3 Fort (the combination product is named). It resolved when the product was stopped.
- **White willow:**
  - The bleeding caution now cites a randomised platelet study (much weaker than aspirin, but above placebo) and the 2019 USP safety review.
  - The aspirin-allergy caution now cites the USP review and an anaphylaxis case.
  - New info note: no DNA damage in mice.

**Draft interactions:** none new. Ten are still pending.

## For the owner (queued for the end-of-campaign review)

1. **Foxglove as a Dangerous Lookalike for sorrel.** The case is documented, and the sorrel record lists only lords-and-ladies. A formal lookalike entry (with distinguishing features) would need your approval. For now, the warning is in the safety notes.
2. **The sorrel foraging note uses severity "warning",** because foxglove poisoning can be fatal.

## Gaps and settled plants

- **Blackberry leaf and raspberry leaf:** settled.
  - The only blackberry trial used the fruit, species not stated.
  - The raspberry-fruit meta-analyses are not leaf evidence and were mostly null.
  - The raspberry-in-pregnancy review pools the labour RCT already cited.
- **Butcher's broom:** varicose veins and swelling stay at 5. Nearly every trial is Cyclo 3 Fort or Phlebodril (combinations), and the one butcher's-broom-only RCT measured vein diameter only.
- **Sorrel:** settled for efficacy.

## Rejected or not added (main reasons)

- **No abstract:** raspberry leaf tea pregnancy toxicity letter, sorrel nephritis letter, ruscogenin dermatitis letters, the infant liver-failure case (willow tea + paracetamol).
- **Other species:** *Morus nigra* "blackberry", black raspberry, a *Salix pentandra* CYP study.
- **Combinations:** xylitol + blackberry gum, phlebotonic blends, fat-burner cases.
