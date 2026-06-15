#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 4.

Targets six more records that carried only two references each:

    Salix alba (Willow Bark), Thymus vulgaris (Thyme), Vaccinium myrtillus
    (Bilberry), Ruscus aculeatus (Butcher's Broom), Ocimum tenuiflorum (Holy
    Basil / Tulsi), Origanum vulgare (Oregano).

New sources from PubMed/PMC are added as REF-0592..REF-0597 and cited from the
relevant actions / constituents in the plant YAML files (edited alongside this
script, provenance in each record's internal_notes).

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "chrubasik2000willow": """@article{chrubasik2000willow,
  author  = {Chrubasik, S., Eisenberg, E., Balan, E., Weinberger, T., Luzzati, R. and Conradt, C.},
  title   = {Treatment of low back pain exacerbations with willow bark extract: a randomized double-blind study},
  journal = {The American Journal of Medicine},
  note    = {REF-0592},
  year    = {2000},
  doi     = {10.1016/S0002-9343(00)00442-3},
  annote  = {Chrubasik, S., Eisenberg, E., Balan, E., Weinberger, T., Luzzati, R. and Conradt, C. (2000) 'Treatment of low back pain exacerbations with willow bark extract: a randomized double-blind study', The American Journal of Medicine, 109(1), pp. 9-14. doi:10.1016/S0002-9343(00)00442-3.}
}

""",
    "kemmerich2006thyme": """@article{kemmerich2006thyme,
  author  = {Kemmerich, B., Eberhardt, R. and Stammer, H.},
  title   = {Efficacy and tolerability of a fluid extract combination of thyme herb and ivy leaves and matched placebo in adults suffering from acute bronchitis with productive cough},
  journal = {Arzneimittel-Forschung},
  note    = {REF-0593},
  year    = {2006},
  doi     = {10.1055/s-0031-1296767},
  annote  = {Kemmerich, B., Eberhardt, R. and Stammer, H. (2006) 'Efficacy and tolerability of a fluid extract combination of thyme herb and ivy leaves and matched placebo in adults suffering from acute bronchitis with productive cough. A prospective, double-blind, placebo-controlled clinical trial', Arzneimittel-Forschung, 56(9), pp. 652-660. doi:10.1055/s-0031-1296767.}
}

""",
    "kopcekova2022bilberry": """@article{kopcekova2022bilberry,
  author  = {Kopcekova, J. and Mrazova, J.},
  title   = {Phytonutrients of bilberry fruit and saskatoon berry in the prevention and treatment of dyslipidemia},
  journal = {Roczniki Panstwowego Zakladu Higieny},
  note    = {REF-0594},
  year    = {2022},
  doi     = {10.32394/rpzh.2022.0216},
  annote  = {Kopcekova, J. and Mrazova, J. (2022) 'Phytonutrients of bilberry fruit and saskatoon berry in the prevention and treatment of dyslipidemia', Roczniki Panstwowego Zakladu Higieny, 73(3), pp. 265-274. doi:10.32394/rpzh.2022.0216.}
}

""",
    "boyle2003ruscus": """@article{boyle2003ruscus,
  author  = {Boyle, P., Diehm, C. and Robertson, C.},
  title   = {Meta-analysis of clinical trials of Cyclo 3 Fort in the treatment of chronic venous insufficiency},
  journal = {International Angiology},
  note    = {REF-0595},
  year    = {2003},
  annote  = {Boyle, P., Diehm, C. and Robertson, C. (2003) 'Meta-analysis of clinical trials of Cyclo 3 Fort in the treatment of chronic venous insufficiency', International Angiology, 22(3), pp. 250-262. [Cyclo 3 Fort = Ruscus aculeatus root extract + hesperidin methyl chalcone + ascorbic acid.]}
}

""",
    "sampath2015ocimum": """@article{sampath2015ocimum,
  author  = {Sampath, S., Mahapatra, S.C., Padhi, M.M., Sharma, R. and Talwar, A.},
  title   = {Holy basil (Ocimum sanctum Linn.) leaf extract enhances specific cognitive parameters in healthy adult volunteers: A placebo controlled study},
  journal = {Indian Journal of Physiology and Pharmacology},
  note    = {REF-0596},
  year    = {2015},
  annote  = {Sampath, S., Mahapatra, S.C., Padhi, M.M., Sharma, R. and Talwar, A. (2015) 'Holy basil (Ocimum sanctum Linn.) leaf extract enhances specific cognitive parameters in healthy adult volunteers: A placebo controlled study', Indian Journal of Physiology and Pharmacology, 59(1), pp. 69-77.}
}

""",
    "force2000oregano": """@article{force2000oregano,
  author  = {Force, M., Sparks, W.S. and Ronzio, R.A.},
  title   = {Inhibition of enteric parasites by emulsified oil of oregano in vivo},
  journal = {Phytotherapy Research},
  note    = {REF-0597},
  year    = {2000},
  doi     = {10.1002/(SICI)1099-1573(200005)14:3<213::AID-PTR583>3.0.CO;2-U},
  annote  = {Force, M., Sparks, W.S. and Ronzio, R.A. (2000) 'Inhibition of enteric parasites by emulsified oil of oregano in vivo', Phytotherapy Research, 14(3), pp. 213-214. doi:10.1002/(SICI)1099-1573(200005)14:3<213::AID-PTR583>3.0.CO;2-U.}
}

""",
}


def citation_key(entry_text):
    m = re.match(r"@\w+\{([^,]+),", entry_text)
    return m.group(1) if m else ""


def main():
    with open(BIB, encoding="utf-8") as fh:
        text = fh.read()

    parts = re.split(r"(?m)^(?=@)", text)
    preamble, entries = parts[0], parts[1:]
    keys = [citation_key(e) for e in entries]
    existing_notes = set(re.findall(r"REF-\d+", text))

    added = 0
    for key in sorted(NEW_ENTRIES):
        block = NEW_ENTRIES[key]
        ref_id = re.search(r"REF-\d+", block).group(0)
        if ref_id in existing_notes or key in keys:
            continue
        pos = len(entries)
        for i, k in enumerate(keys):
            if k > key:
                pos = i
                break
        entries.insert(pos, block)
        keys.insert(pos, key)
        existing_notes.add(ref_id)
        added += 1

    with open(BIB, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(preamble + "".join(entries))

    print(f"Added {added} new reference(s); bibliography now has {len(entries)} entries.")


if __name__ == "__main__":
    main()
