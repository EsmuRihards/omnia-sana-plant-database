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

Follow-up (same day, owner decision): the 46 refs with broken titles (e.g. ";13(13):2155.") were deleted
rather than repaired. 45 were removed from every plant field and from the bibliography. REF-0154 was kept,
because it had been repaired above. As a result, 34 indications lost all evidence and were dropped (mainly
bay laurel, anise, black seed and ashwagandha). 14 contraindications, 10 actions and 2 constituents are now
unsourced and set to needs-review; they stay visible pending re-sourcing. 5 dosage/preparation records are
now withheld by the build. Deleted: REF-0003, REF-0030, REF-0034, REF-0042, REF-0047, REF-0054, REF-0060, REF-0064, REF-0065, REF-0087, REF-0088, REF-0090, REF-0094, REF-0104, REF-0107, REF-0119, REF-0123, REF-0142, REF-0145, REF-0150, REF-0159, REF-0160, REF-0165, REF-0176, REF-0177, REF-0180, REF-0188, REF-0201, REF-0202, REF-0203, REF-0257, REF-0259, REF-0261, REF-0268, REF-0274, REF-0276, REF-0277, REF-0278, REF-0284, REF-0285, REF-0290, REF-0291, REF-0294, REF-0347, REF-0357.
