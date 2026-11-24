# Research-deepening batch 1 (2026-11-24)

Plants: yarrow, sweet flag, black cohosh, ground elder, horse chestnut.

Searched: PubMed (5 query families each), Europe PMC, ClinicalTrials.gov and OpenAlex. That is roughly 1,900
hits, about 200 abstracts or pages read, 82 references added (REF-5001..5082) and 1 deleted.
Symptom-tool pairs: 1,405 -> 1,409. Validate: 0 errors, refs cited 3,863 / declared 3,863.
Species audit: no flags on this batch. Change log: `r01_changes.tsv`; fixer: `../fix_r01.py`.

## Score changes (live Symptom tool)

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Horse chestnut | swelling, varicose veins | 7 | 10 | Diehm 1996 (Lancet) and 1992 RCTs, Siebert 2002 MA, open Aesculaforce study, EU monograph |
| Horse chestnut | haemorrhoids | 1 (inferred) | 6 | Two Thai RCTs adding escin (registered as "aescin in horse chestnut") to MPFF |
| Horse chestnut | bruising | new | 5 | Escin-gel haematoma RCT + EU monograph traditional topical use |
| Yarrow | heavy menstrual bleeding | 1 | 6 | Two triple-blind add-on RCTs (Iranian J Obstet Gynecol Infertil) |
| Yarrow | PMS | new | 5 | Double-blind placebo RCT 2026 (not in PubMed) |
| Yarrow | liver support, high cholesterol | new | 5 | Double-blind placebo RCT in type 2 diabetes (ALT/AST, LDL/TC/TG) |
| Yarrow | wounds, oral health | 5 | 6 | Nipple-fissure RCT; AML mucositis RCT |
| Black cohosh | hot flashes, menopause | 9 | 10 | NICE NMA, IMS 2026 SR, 5 RCTs; two more null RCTs recorded |

**No-effect studies recorded:**
- Horse chestnut: advanced chronic venous insufficiency (CVI) trial; open comparison with Pycnogenol.
- Yarrow: leishmaniasis gel; radiation dermatitis cream; venous-ulcer ointment.
- Black cohosh: Jacobson 2001 trial in breast cancer survivors; Frei-Kleiner 2005 (intention-to-treat result null).

## Safety and other tool data

- **Horse chestnut:**
  - EU monograph read from the PDF; its year was corrected to 2020.
  - Raw-conker poisoning note re-sourced to three poisoning reports and raised to `warning`.
  - New side-effects and liver-injury caution.
  - Kidney and heart caution and pregnancy line taken from the monograph; a bleeding case report added.
  - Dosage rewritten to the monograph plus the trial dose (now `verified`).
  - Bioavailability (PK) studies added to escin.
- **Yarrow:**
  - **Retracted paper removed** (REF-2085).
  - Rat pregnancy study added to the pregnancy caution.
  - Cosmetic safety review (Cosmetic Ingredient Review, CIR) and application-site reactions added to the allergy note.
  - New anticholinergic case-report caution.
  - New dosage entry with the capsule doses used in the trials.
- **Sweet flag:**
  - Serious warning re-sourced to the EMA/HMPC asarone statement: about 115 micrograms a day as a temporary limit, and asarone content by variety.
  - High asarone found in teas and supplements.
  - New `warning`: legal-high poisonings.
  - New caution: the rhizome oil is a skin sensitiser.
  - Description, habitat, harvesting, traditional uses and preparations had **no sources at all**. They are rewritten from Grieve. Harvesting no longer says to peel the rhizome; Grieve advises against peeling.
- **Black cohosh:**
  - Liver caution re-sourced: USP review of 30 cases, liver meta-analysis of 1,117 women, case reports, a 12-month study.
  - Breast and endometrium information re-sourced.
  - Pregnancy caution re-sourced (systematic review plus a case of low sodium in labour).
  - New side-effect caution: bradycardia, mania, serotonin toxicity.
  - Pharmacokinetics added to its triterpene glycosides.
- **Draft herb-drug interactions** (not public until the owner approves them):
  - Horse chestnut and sweet flag: CYP3A4, insufficient evidence (lab only).
  - Black cohosh: CYP3A4 likely safe, digoxin likely safe (both from human pharmacokinetic RCTs).
  - Black cohosh: serotonergic antidepressants, caution (one case).
  - Black cohosh: tamoxifen, insufficient evidence.

## Owner decisions needed

1. **Draft interactions** listed above: approve or adjust.
2. **Sweet flag / headache.** A pilot RCT of Vacha Taila nose drops for post-dural-puncture headache was
   positive. It meets the RCT rule, but the record carries a serious internal-use warning. The study is filed
   in the plant's general reference list, not as a headache pair. Add the pair or not?
3. **Black cohosh / fertility.** Several RCTs added black cohosh to clomiphene and were positive. However, one
   of them now has an Expression of Concern (2026), and a PCOS systematic review rated the evidence low
   quality. Not added.
4. **Black cohosh / depression.** A Chinese RCT adding Remifemin to paroxetine was positive, but the held 2023
   meta-analysis found no effect on depression. Not added.
5. **Horse chestnut / anticoagulant interaction (approved record).** The renal-bleeding case report (REF-5017)
   would support it. It was not attached, because that record is owner-signed.

## Still open (manual retrieval)

- Yarrow haemorrhoid RCT (J Herb Med 2023) and epistaxis RCT (J Herb Med 2021). There is no abstract anywhere
  machine-readable (Elsevier returns 403). If the owner can open them, both could be wired in.
- Yarrow knee-osteoarthritis topical oil RCT. The abstract gives only the effect over time, not yarrow versus
  placebo.

## Settled with no new sources

**Ground elder** has no human study in any of the five seams. The only candidates were rat and mouse papers in
journals from a publisher on Beall's list of possible predatory publishers. The search log is in its
`internal_notes`.
