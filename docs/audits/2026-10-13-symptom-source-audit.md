# Symptom-source audit, 2026-10-13

Every source card shown on the Symptom-tool "View Sources" pages (direct `reference_ids` plus the
"Mechanistic basis" action refs) was checked one by one for all 188 plants: 7,809 cards in total,
of which 1,962 were misclassified. `2026-10-13-symptom-source-audit.tsv` has one row per finding
(batch, plant, condition, ref, section, category, reason). `_systemic.tsv` lists the Kew POWO pages,
broken titles and duplicate records.

Applied in the same commit:
- Direct findings: the ref was removed from that indication's `reference_ids` (1,711 removals
  including POWO taxonomy pages). It was also added to `mechanistic_exclude_ids`, so it cannot
  resurface through a related action.
- Mechanistic findings: added to the indication's `mechanistic_exclude_ids`. The action itself is
  untouched, because the paper is still real evidence for the action, just not for that symptom.
- Wrong-species, chemistry-only and protocol-only refs: removed from the plant's indications
  and actions. Wrong-species refs were also removed from its `references[]`.
- Indications left with no valid card were dropped (98). Indications left with only mechanistic
  evidence were set to `needs-review` (inferred).
- Refs that were misfiled under the wrong symptom of the same plant were added as new
  indications: ginger nausea (REF-0295, REF-0635, REF-0077), St John's wort depression
  (REF-0154, REF-0842, REF-1797, REF-1798), saffron depression (REF-0005, REF-0172, REF-0789,
  REF-2001, REF-2002), lemon balm depression (REF-1194). REF-0634 (ginger CINV RCT) was NOT used:
  the trial reported no clinically meaningful effect on nausea.
- 47 duplicate bibliography records were merged (same DOI or same paper). Where the duplicates
  disagreed on study_type, the kept narrative reviews were set to `preclinical` (REF-1508,
  REF-1528, REF-2549, REF-1123, REF-0825).
- Wrong abstracts (belonging to other papers) were removed from REF-0146, REF-0317, REF-0190,
  REF-0349 and REF-0084. REF-0005, REF-0172 and REF-0154 had truncated titles and were
  completed from PubMed.
- 82 bibliography entries that were left cited by nothing were deleted.

Not addressed: 46 refs with broken titles (e.g. ";13(13):2155.") whose content could not be judged.
They remain linked and need metadata repair.
