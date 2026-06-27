#!/usr/bin/env python3
"""2026-06-27 >=15-publications pass — matricaria_chamomilla (German chamomile) 11 -> 15.
4 genuine Matricaria chamomilla clinical trials verified via PubMed MCP (real
authors/titles/DOIs). Adds the well-evidenced anxiety/depression/arthritis
indications and the matching anxiolytic/antidepressant/analgesic actions."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v15_2026_06_27 import apply, add_facts

add_facts("matricaria_chamomilla",
          actions=["anxiolytic", "antidepressant", "analgesic", "antidiabetic", "antispasmodic"],
          indications=["anxiety", "depression", "arthritis", "blood-sugar", "menstrual-cramps"])

SOURCES = [
    {"citekey": "mao2016chamomile", "plant": "matricaria_chamomilla", "study_type": "rct",
     "fields": {"author": "Mao, J.J., Xie, S.X., Keefe, J.R., Soeller, I., Li, Q.S. and Amsterdam, J.D.",
                "title": "Long-term chamomile (Matricaria chamomilla L.) treatment for generalized anxiety disorder: a randomized clinical trial",
                "journal": "Phytomedicine", "year": "2016", "volume": "23", "number": "14", "pages": "1735-1742",
                "doi": "10.1016/j.phymed.2016.10.012"},
     "abstract": "In a randomized clinical trial, long-term chamomile extract treatment was safe and maintained significantly lower generalized anxiety disorder symptoms than placebo, with reductions in body weight and mean arterial pressure.",
     "actions": ["anxiolytic"], "indications": ["anxiety"]},
    {"citekey": "amsterdam2009chamomile", "plant": "matricaria_chamomilla", "study_type": "rct",
     "fields": {"author": "Amsterdam, J.D., Li, Y., Soeller, I., Rockwell, K., Mao, J.J. and Shults, J.",
                "title": "A randomized, double-blind, placebo-controlled trial of oral Matricaria recutita (chamomile) extract therapy for generalized anxiety disorder",
                "journal": "Journal of Clinical Psychopharmacology", "year": "2009", "volume": "29", "number": "4", "pages": "378-382",
                "doi": "10.1097/JCP.0b013e3181ac935c"},
     "abstract": "The first controlled clinical trial of chamomile extract for generalized anxiety disorder found a significantly greater reduction in Hamilton Anxiety scores than placebo, suggesting modest anxiolytic activity.",
     "actions": ["anxiolytic"], "indications": ["anxiety"]},
    {"citekey": "amsterdam2012chamomile", "plant": "matricaria_chamomilla", "study_type": "rct",
     "fields": {"author": "Amsterdam, J.D., Shults, J., Soeller, I., Mao, J.J., Rockwell, K. and Newberg, A.B.",
                "title": "Chamomile (Matricaria recutita) may provide antidepressant activity in anxious, depressed humans: an exploratory study",
                "journal": "Alternative Therapies in Health and Medicine", "year": "2012", "volume": "18", "number": "5", "pages": "44-49"},
     "abstract": "An analysis of a randomized double-blind placebo-controlled chamomile trial found a significantly greater reduction in Hamilton Depression scores for chamomile than placebo, suggesting clinically meaningful antidepressant activity in addition to its anxiolytic effect.",
     "actions": ["antidepressant"], "indications": ["depression"]},
    {"citekey": "shoara2015chamomile", "plant": "matricaria_chamomilla", "study_type": "rct",
     "fields": {"author": "Shoara, R., Hashempur, M.H., Ashraf, A., Salehi, A., Dehshahri, S. and Habibagahi, Z.",
                "title": "Efficacy and safety of topical Matricaria chamomilla L. (chamomile) oil for knee osteoarthritis: a randomized controlled clinical trial",
                "journal": "Complementary Therapies in Clinical Practice", "year": "2015", "volume": "21", "number": "3", "pages": "181-187",
                "doi": "10.1016/j.ctcp.2015.06.003"},
     "abstract": "In a randomized controlled trial, topical chamomile oil significantly reduced analgesic (acetaminophen) demand in patients with knee osteoarthritis compared with diclofenac and placebo, with no adverse events reported.",
     "actions": ["analgesic", "anti-inflammatory"], "indications": ["arthritis"]},
    {"citekey": "zemestani2015chamomile", "plant": "matricaria_chamomilla", "study_type": "rct",
     "fields": {"author": "Zemestani, M., Rafraf, M. and Asghari-Jafarabadi, M.",
                "title": "Chamomile tea improves glycemic indices and antioxidants status in patients with type 2 diabetes mellitus",
                "journal": "Nutrition", "year": "2016", "volume": "32", "number": "1", "pages": "66-72",
                "doi": "10.1016/j.nut.2015.07.011"},
     "abstract": "In a randomized controlled trial, eight weeks of chamomile tea significantly lowered glycated haemoglobin, serum insulin and insulin resistance and raised antioxidant enzyme activity in patients with type 2 diabetes mellitus.",
     "actions": ["antidiabetic", "antioxidant"], "indications": ["blood-sugar"]},
    {"citekey": "niazi2021chamomile", "plant": "matricaria_chamomilla", "study_type": "systematic-review",
     "fields": {"author": "Niazi, A. and Moradi, M.",
                "title": "The effect of chamomile on pain and menstrual bleeding in primary dysmenorrhea: a systematic review",
                "journal": "International Journal of Community Based Nursing and Midwifery", "year": "2021", "volume": "9", "number": "3", "pages": "174-186",
                "doi": "10.30476/ijcbnm.2021.87219.1417"},
     "abstract": "A systematic review of seven clinical trials concluded that chamomile, which inhibits prostaglandin and leukotriene production, can be an effective treatment for the pain of primary dysmenorrhea and for reducing menstrual bleeding.",
     "actions": ["antispasmodic", "analgesic"], "indications": ["menstrual-cramps"]},
]

if __name__ == "__main__":
    apply(SOURCES)
