# Symptom-tool audit - batch 3 of 19 (2026-11-10) - FIXED

Plants 21-30: asclepias-tuberosa, astragalus-membranaceus, bacopa-monnieri, betula-pendula,
bistorta-officinalis, borago-officinalis, boswellia-serrata, calendula-officinalis,
camellia-sinensis, campanula-persicifolia. 92 pairs, 93 articles. The same commit applies the
no-effect and not-a-source flags from `truncated_abstracts.md` (9 other plants).

New owner rule this batch: **"may be effective / may benefit" reviews with low-quality evidence
count as support, as written** (e.g. REF-2261, astragalus post-stroke fatigue; REF-0584,
artichoke, stays as support).

Result: 149 changes. Site-wide: 1,521 pairs reduced to 1,487 and 185 plants in the tool reduced
to 184. 11 refs deleted. Log: `batch03_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Calendula / 6 pairs (5) | REF-0183, a "double-blind RCT" (Nicolaus 2017), is **not in PubMed** and has no DOI or journal. The author publishes only in-vitro work. **Phantom citation** | Purged. Wounds now rests on a real SR + burn RCT (8). The other pairs fall to 1 or drop |
| Tea / cancer (7) | Cochrane 2020 (REF-1961): "no conclusive evidence" | Moved to null_result_ids. Score 7 -> 2 |
| Astragalus / kidney support (7) | Cochrane CKD (REF-0586): "definitive conclusions could not be made" | Moved to null; pair dropped |
| Boswellia / asthma, IBD | Only source REF-0423 covers boswellic acids of *unnamed* Boswellia species | Purged; both pairs dropped |
| Peach-leaved bellflower / all 6 | Only source is a **genus-level** Campanula review that never names the species | Removed. Plant leaves the tool |
| Serenoa, hibiscus, lavender | No-effect trials/SRs (REF-1895, REF-1844, REF-0858) | Recorded in null_result_ids |
| Thyme, feverfew, evening primrose, willowherb | Multi-herb products cited as single-herb evidence (REF-0593, 1577, 2588, 0404) | Removed |
| Marsh tea | REF-0881 is homeopathic | Purged |

## Medium - does not match / cannot be verified

- **Unverifiable sources, removed from all pairs:**
  - "WHO Monographs" 2002 (REF-0309), cited for bacopa and borage. WHO has no monograph for
    either.
  - Herbs2000 (403) and WebMD bistort (404).
  - Lockwood 1848 and "Drake 2015", which can't be found anywhere.
  - Hoffmann (REF-0112), for calendula.
- **GLA review (REF-0129)** never names borage. Purged.
- **Generic reviews cited far beyond what they say:**
  - The green-tea review REF-0045 (PubMed abstract added) only covers cancer, heart and liver
    disease, obesity and diabetes.
  - REF-0402 (astragaloside IV) was cited for arthritis, fatigue, kidney, skin and stress.
- **Wrong condition:**
  - Rat wound and fibroblast studies were cited for skin irritation and bruising.
  - A GC-MS chemistry paper was cited for infection.
  - Birch's EMA summary was cited for UTI and swelling; it covers urinary flushing only.
- **Duplicate:** REF-0038 duplicates REF-0740 (the same bacopa RCT). Merged.

Validate 0 errors; refs 3215/3215.
