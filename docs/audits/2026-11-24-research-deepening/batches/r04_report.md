# Research-deepening batch 4 (2026-11-24)

**Plants:** lesser burdock, bearberry, arnica, wormwood, mugwort. Also a follow-up on andrographis from the batch 3 Europe PMC results, which arrived after batch 3 was committed.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov, OpenAlex and the Memorial Sloan Kettering (MSKCC) "About Herbs" pages.

**Outcome:**
- **Search volume:** about 1,300 PubMed hits (mugwort alone: 937, nearly all pollen allergy or moxibustion) and about 70 abstracts or pages read.
- **New references:** 18 (REF-5169..5186).
- **Symptom-tool pairs:** 1,417 -> 1,420.
- **Checks:** validate passes, with refs cited 3,961 / declared 3,961. The species audit raised only false positives ("Arnica cream", "Arnica group").
- **Files:** change log `r04_changes.tsv`; fixer `../fix_r04.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Arnica | bruising | 5 | 7 | Two small randomized trials after nose surgery: arnica cream vs no treatment (2016), and split-face (2026, found via OpenAlex) |
| Arnica | swelling | new | 6 | The same two trials (less swelling around the eyes); a wisdom-tooth trial found no effect on swelling and is recorded as no-effect |
| Arnica | pain | new | 5 | Wisdom-tooth surgery trial: topical arnica added to standard pain relief lowered pain to day 5 (open, no placebo) |
| Arnica | arthritis | 5 | 6 | Open multicentre knee-osteoarthritis gel trial (79 patients) |
| Wormwood | depression | new | 5 | Triple-blind placebo RCT of a wormwood vaginal gel in women with sexual dysfunction (Mashhad 2022, not in PubMed) |

**Homeopathic trials:** most arnica trials use homeopathic dilutions (12CH, D4, D12, D30, pellets, SinEcch). None were used (owner rule). Topical creams, gels and ointments count as plant evidence under the mother-tincture rule (invariant 11).

## Safety and other tool data

**Arnica:**
- The allergy note now carries two patch-test studies:
  - about 1% of 443 people tested reacted to arnica;
  - 5 of 6 people already sensitised to arnica reacted to arnica products.
- The oral-toxicity note is now also sourced to the 2001 CIR safety assessment and the MSKCC page.
- The pregnancy and breastfeeding caution now cites an MSKCC case: a breastfed newborn developed haemolytic anaemia after the mother drank arnica flower tea.

**Wormwood:**
- New **warning** on liver injury: two toxic-hepatitis cases (2026), one fatal after a liver transplant.
- New caution not to give it to babies or children: an infant was poisoned by a home-made extract.

**Mugwort:** new caution on thujone poisoning. A man drank 1 L of mugwort infusion and was admitted in a manic state; thujone was confirmed in his blood.

**Bearberry:** new caution on long-term use: bull's-eye maculopathy (retinal damage) after 3 years of uva ursi.

**Lesser burdock:**
- A diabetic-rat study is now the source for a new antidiabetic action and for the blood-sugar part of its caution.
- The diuretic and pregnancy parts of that caution have no source for this species and stay `needs-review`.

**Andrographis (batch 3 follow-up):** the interaction caution now states two things:
- one anaphylactic reaction in a dose-escalating andrographolide trial, which was stopped early;
- no significant platelet change in 10 healthy volunteers.

**Draft herb-drug interactions (need owner sign-off):**
- **Wormwood × anticoagulants (caution):** a case of gut bleeding on warfarin, with the link rated "probable".
- **Arnica × anticoagulants (insufficient):** lab platelet data plus MSKCC; clinical relevance unknown, and arnica is for use on the skin only.
- **Bearberry × CYP3A4 substrates (insufficient):** lab inhibition of CYP3A4, 3A5, 3A7, 2C19 and P-gp only.

## For the owner

1. **The three draft interactions above** need sign-off.
2. **Arnica muscle soreness was not added.** The two trials conflict:
   - after downhill running, a small RCT (n=20) found less pain at 72 h;
   - a larger RCT (n=53) found that arnica cream **increased** leg pain at 24 h.

   The scoring does not subtract no-effect studies, so a pair would show 5/10. Add it only if you want conflicting pairs shown.
3. **Wormwood depression (5)** rests on one small trial of a vaginal gel in women with sexual dysfunction. It is labelled that way, but it is a narrow basis for "depression".
4. **Arnica pain (5)** rests on one open-label trial; patients knew whether they got arnica.

## Rejected or not added (main reasons)

- **Conflicts with a safety note (invariant 12d):** arnica tincture healed cutaneous leishmaniasis in 12 of 12 completers, but it is applied to ulcers, and the record forbids broken skin.
- **Active comparator only:** wormwood ointment vs piroxicam for knee osteoarthritis; *Artemisia* vaginal cream vs clotrimazole.
- **Uncontrolled or below the new-pair bar:**
  - wormwood for IgA nephropathy (10 patients, no control);
  - andrographis in oesophageal cancer (compares completers with non-completers).
- **Mixed homeopathic and topical forms:** three 2025-2026 arnica systematic reviews.
- **Not about taking the herb:**
  - mugwort moxibustion trials (burning moxa on acupoints, often *Artemisia argyi*);
  - mugwort pollen-allergy studies.
- **Combinations:**
  - arnica + hydroxyethyl salicylate spray;
  - Arnica-Echinacea umbilical powder;
  - a three-herb mixture in a kidney-injury case;
  - Kan Jang;
  - a multi-herb detox tea.
- **Unreadable:**
  - Sharbat-e-Afsanteen liver-enzyme RCT (no abstract);
  - Dwyer 2020 harm systematic review (no abstract);
  - mugwort lotion letter (no abstract).
- **Blocked or missing pages:** LiverTox and LactMed pages for arnica and uva ursi sit behind an NCBI bot check. MSKCC has no uva ursi, wormwood or mugwort page (404).
- **Still pending:** the BRUMI bearberry-vs-placebo cystitis trial (NCT05055544) has a protocol but no results yet.
- **Lesser burdock:** no human study of *Arctium minus* exists. Settled apart from the animal blood-sugar source above.
