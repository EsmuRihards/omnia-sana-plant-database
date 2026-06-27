#!/usr/bin/env python3
"""2026-06-27 >=15-publications pass — trifolium_pratense (red clover) 11 -> 15.
Adds the well-evidenced menopause/hot-flush + lipid indications the record lacked,
then 4 genuine Trifolium pratense @article sources verified via PubMed MCP
(real authors/titles/DOIs extracted from get_article_metadata).
Species-care: all four are red-clover-specific menopause/lipid clinical literature."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enrich_lib_v15_2026_06_27 import apply, add_facts

add_facts("trifolium_pratense",
          actions=["lipid-lowering"],
          indications=["menopause", "hot-flashes", "high-cholesterol"])

SOURCES = [
    {"citekey": "kanadys2021trifolium", "plant": "trifolium_pratense", "study_type": "meta-analysis",
     "fields": {"author": "Kanadys, W., Baranska, A., Blaszczuk, A., Polz-Dacewicz, M., Drop, B., Kanecki, K. and Malm, M.",
                "title": "Evaluation of clinical meaningfulness of red clover (Trifolium pratense L.) extract to relieve hot flushes and menopausal symptoms in peri- and post-menopausal women: a systematic review and meta-analysis of randomized controlled trials",
                "journal": "Nutrients", "year": "2021", "volume": "13", "number": "4", "pages": "1258",
                "doi": "10.3390/nu13041258"},
     "abstract": "A meta-analysis of eight randomized controlled trials found that red clover isoflavone extract produced a statistically significant reduction in the daily frequency of hot flushes in peri- and post-menopausal women compared with placebo.",
     "indications": ["hot-flashes", "menopause"]},
    {"citekey": "yigit2024trifolium", "plant": "trifolium_pratense", "study_type": "rct",
     "fields": {"author": "Yigit, E. and Unsal, S.",
                "title": "Isoflavones obtained from red clover improve both dyslipidemia and menopausal symptoms in menopausal women: a prospective randomized placebo-controlled trial",
                "journal": "Climacteric", "year": "2024", "volume": "27", "number": "6", "pages": "548-554",
                "doi": "10.1080/13697137.2024.2393121"},
     "abstract": "In a randomized placebo-controlled trial, six months of red clover isoflavones significantly improved menopausal symptom scores and the lipid profile (lower total cholesterol, LDL-C and triglycerides, higher HDL-C) in postmenopausal women with dyslipidemia.",
     "indications": ["hot-flashes", "menopause", "high-cholesterol"], "actions": ["lipid-lowering"]},
    {"citekey": "lethaby2007phytoestrogens", "plant": "trifolium_pratense", "study_type": "systematic-review",
     "fields": {"author": "Lethaby, A.E., Brown, J., Marjoribanks, J., Kronenberg, F., Roberts, H. and Eden, J.",
                "title": "Phytoestrogens for vasomotor menopausal symptoms",
                "journal": "Cochrane Database of Systematic Reviews", "year": "2007", "number": "4", "pages": "CD001395",
                "doi": "10.1002/14651858.CD001395.pub3"},
     "abstract": "A Cochrane systematic review of phytoestrogens for vasomotor menopausal symptoms pooled five trials of the red clover extract Promensil, finding no significant overall difference from placebo in hot-flush frequency and no oestrogenic stimulation of the endometrium over up to two years.",
     "indications": ["hot-flashes", "menopause"]},
    {"citekey": "geller2006soy", "plant": "trifolium_pratense", "study_type": "systematic-review",
     "fields": {"author": "Geller, S.E. and Studee, L.",
                "title": "Soy and red clover for mid-life and aging",
                "journal": "Climacteric", "year": "2006", "volume": "9", "number": "4", "pages": "245-263",
                "doi": "10.1080/13697130600736934"},
     "abstract": "This review of randomized controlled trials concluded that red clover isoflavones have a small but positive effect on plasma lipids, reducing triglycerides and increasing HDL cholesterol, with promising but less convincing effects on bone mass density and cognition in peri- and post-menopausal women.",
     "actions": ["lipid-lowering"], "indications": ["high-cholesterol", "cardiovascular-support"]},
    {"citekey": "atkinson2004phytoestrogen", "plant": "trifolium_pratense", "study_type": "rct",
     "fields": {"author": "Atkinson, C., Compston, J.E., Day, N.E., Dowsett, M. and Bingham, S.A.",
                "title": "The effects of phytoestrogen isoflavones on bone density in women: a double-blind, randomized, placebo-controlled trial",
                "journal": "The American Journal of Clinical Nutrition", "year": "2004", "volume": "79", "number": "2", "pages": "326-333",
                "doi": "10.1093/ajcn/79.2.326"},
     "abstract": "In a one-year double-blind randomized placebo-controlled trial of 205 women, a red clover-derived isoflavone supplement significantly attenuated loss of lumbar spine bone mineral density and increased bone-formation markers, suggesting a protective effect on the spine."},
    {"citekey": "booth2006clinical", "plant": "trifolium_pratense", "study_type": "systematic-review",
     "fields": {"author": "Booth, N.L., Piersen, C.E., Banuvar, S., Geller, S.E., Shulman, L.P. and Farnsworth, N.R.",
                "title": "Clinical studies of red clover (Trifolium pratense) dietary supplements in menopause: a literature review",
                "journal": "Menopause", "year": "2006", "volume": "13", "number": "2", "pages": "251-264",
                "doi": "10.1097/01.gme.0000198297.40269.f7"},
     "abstract": "This review of clinical studies of red clover (Trifolium pratense) dietary supplements in menopause found limited evidence for vasomotor-symptom relief or LDL reduction but possible benefit for maintenance of bone health and arterial compliance.",
     "indications": ["menopause", "hot-flashes", "high-cholesterol"], "actions": ["lipid-lowering"]},
    {"citekey": "quah2022trifolium", "plant": "trifolium_pratense", "study_type": "preclinical",
     "fields": {"author": "Quah, Y., Yi-Le, J.C., Park, N.H., Lee, Y.Y., Lee, E.B., Jang, S.H., Kim, M.J., Rhee, M.H., Lee, S.J. and Park, S.C.",
                "title": "Serum biomarker-based osteoporosis risk prediction and the systemic effects of Trifolium pratense ethanolic extract in a postmenopausal model",
                "journal": "Chinese Medicine", "year": "2022", "volume": "17", "number": "1", "pages": "70",
                "doi": "10.1186/s13020-022-00622-7"},
     "abstract": "In ovariectomized rats, a Trifolium pratense ethanolic extract showed anti-osteoporosis and estrogenic activity, down-regulating RANK ligand and alkaline phosphatase and up-regulating estrogen receptor beta, supporting traditional use for postmenopausal complaints.",
     "indications": ["menopause"]},
]

if __name__ == "__main__":
    apply(SOURCES)
