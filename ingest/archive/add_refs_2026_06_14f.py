#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 6.

Targets six more records that carried only two references each:

    Foeniculum vulgare (Fennel), Eschscholzia californica (California Poppy),
    Rubus idaeus (Raspberry Leaf), Capsella bursa-pastoris (Shepherd's Purse),
    Viola odorata (Sweet Violet), Viburnum opulus (Cramp Bark).

New sources from PubMed/PMC are added as REF-0604..REF-0610 and cited from the
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
    "shahrahmani2021fennel": """@article{shahrahmani2021fennel,
  author  = {Shahrahmani, H., Ghazanfarpour, M., Shahrahmani, N., Abdi, F., Sewell, R.D.E. and Rafieian-Kopaei, M.},
  title   = {Effect of fennel on primary dysmenorrhea: a systematic review and meta-analysis},
  journal = {Journal of Complementary & Integrative Medicine},
  note    = {REF-0604},
  year    = {2021},
  doi     = {10.1515/jcim-2019-0212},
  annote  = {Shahrahmani, H., Ghazanfarpour, M., Shahrahmani, N., Abdi, F., Sewell, R.D.E. and Rafieian-Kopaei, M. (2021) 'Effect of fennel on primary dysmenorrhea: a systematic review and meta-analysis', Journal of Complementary & Integrative Medicine, 18(2), pp. 261-269. doi:10.1515/jcim-2019-0212.}
}

""",
    "xu2020dysmenorrhea": """@article{xu2020dysmenorrhea,
  author  = {Xu, Y., Yang, Q. and Wang, X.},
  title   = {Efficacy of herbal medicine (cinnamon/fennel/ginger) for primary dysmenorrhea: a systematic review and meta-analysis of randomized controlled trials},
  journal = {Journal of International Medical Research},
  note    = {REF-0605},
  year    = {2020},
  doi     = {10.1177/0300060520936179},
  annote  = {Xu, Y., Yang, Q. and Wang, X. (2020) 'Efficacy of herbal medicine (cinnamon/fennel/ginger) for primary dysmenorrhea: a systematic review and meta-analysis of randomized controlled trials', Journal of International Medical Research, 48(6), 300060520936179. doi:10.1177/0300060520936179.}
}

""",
    "hanus2004eschscholzia": """@article{hanus2004eschscholzia,
  author  = {Hanus, M., Lafon, J. and Mathieu, M.},
  title   = {Double-blind, randomised, placebo-controlled study to evaluate the efficacy and safety of a fixed combination containing two plant extracts (Crataegus oxyacantha and Eschscholtzia californica) and magnesium in mild-to-moderate anxiety disorders},
  journal = {Current Medical Research and Opinion},
  note    = {REF-0606},
  year    = {2004},
  doi     = {10.1185/030079903125002603},
  annote  = {Hanus, M., Lafon, J. and Mathieu, M. (2004) 'Double-blind, randomised, placebo-controlled study to evaluate the efficacy and safety of a fixed combination containing two plant extracts (Crataegus oxyacantha and Eschscholtzia californica) and magnesium in mild-to-moderate anxiety disorders', Current Medical Research and Opinion, 20(1), pp. 63-71. doi:10.1185/030079903125002603.}
}

""",
    "simpson2001raspberry": """@article{simpson2001raspberry,
  author  = {Simpson, M., Parsons, M., Greenwood, J. and Wade, K.},
  title   = {Raspberry leaf in pregnancy: its safety and efficacy in labor},
  journal = {Journal of Midwifery & Women's Health},
  note    = {REF-0607},
  year    = {2001},
  doi     = {10.1016/s1526-9523(01)00095-2},
  annote  = {Simpson, M., Parsons, M., Greenwood, J. and Wade, K. (2001) 'Raspberry leaf in pregnancy: its safety and efficacy in labor', Journal of Midwifery & Women's Health, 46(2), pp. 51-59. doi:10.1016/s1526-9523(01)00095-2.}
}

""",
    "naafe2018capsella": """@article{naafe2018capsella,
  author  = {Naafe, M., Kariman, N., Keshavarz, Z., Khademi, N., Mojab, F. and Mohammadbeigi, A.},
  title   = {Effect of Hydroalcoholic Extracts of Capsella Bursa-Pastoris on Heavy Menstrual Bleeding: A Randomized Clinical Trial},
  journal = {Journal of Alternative and Complementary Medicine},
  note    = {REF-0608},
  year    = {2018},
  doi     = {10.1089/acm.2017.0267},
  annote  = {Naafe, M., Kariman, N., Keshavarz, Z., Khademi, N., Mojab, F. and Mohammadbeigi, A. (2018) 'Effect of Hydroalcoholic Extracts of Capsella Bursa-Pastoris on Heavy Menstrual Bleeding: A Randomized Clinical Trial', Journal of Alternative and Complementary Medicine, 24(7), pp. 694-700. doi:10.1089/acm.2017.0267.}
}

""",
    "qasemzadeh2015viola": """@article{qasemzadeh2015viola,
  author  = {Qasemzadeh, M.J., Sharifi, H., Hamedanian, M., Gharehbeglou, M., Heydari, M., Sardari, M., Akhlaghdoust, M. and Minae, M.B.},
  title   = {The Effect of Viola odorata Flower Syrup on the Cough of Children With Asthma: A Double-Blind, Randomized Controlled Trial},
  journal = {Journal of Evidence-Based Complementary & Alternative Medicine},
  note    = {REF-0609},
  year    = {2015},
  doi     = {10.1177/2156587215584862},
  annote  = {Qasemzadeh, M.J., Sharifi, H., Hamedanian, M., Gharehbeglou, M., Heydari, M., Sardari, M., Akhlaghdoust, M. and Minae, M.B. (2015) 'The Effect of Viola odorata Flower Syrup on the Cough of Children With Asthma: A Double-Blind, Randomized Controlled Trial', Journal of Evidence-Based Complementary & Alternative Medicine, 20(4), pp. 287-291. doi:10.1177/2156587215584862.}
}

""",
    "kajszczak2020viburnum": """@article{kajszczak2020viburnum,
  author  = {Kajszczak, D., Zaklos-Szyda, M. and Podsedek, A.},
  title   = {Viburnum opulus L. - A Review of Phytochemistry and Biological Effects},
  journal = {Nutrients},
  note    = {REF-0610},
  year    = {2020},
  doi     = {10.3390/nu12113398},
  annote  = {Kajszczak, D., Zaklos-Szyda, M. and Podsedek, A. (2020) 'Viburnum opulus L. - A Review of Phytochemistry and Biological Effects', Nutrients, 12(11), 3398. doi:10.3390/nu12113398.}
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
