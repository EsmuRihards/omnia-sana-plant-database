"""Deep re-sweep of batch 7 (eschscholzia-californica .. gentiana-lutea) at batch-13 depth. Run from the repo root.
Owner rules 2026-11-12: new pair only when an SR/MA or RCT of this species names the symptom and finds benefit;
SRs of lab/animal studies keep SR scoring. New refs REF-3552..REF-3562 (PubMed efetch, deep/abstracts.json)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import fixlib, deep_lib

fixlib.DATE = '2026-11-12'
HERE = os.path.dirname(__file__)

NEW = deep_lib.newrefs([
    ('REF-3552', '12645832', 'cineoleasthma', 'rct'),
    ('REF-3553', '22978309', 'cineoleasthma2012', 'rct'),
    ('REF-3554', '15064633', 'cineolesinusitis', 'rct'),
    ('REF-3555', '19624838', 'cineolecopd', 'rct'),
    ('REF-3556', '28509813', 'fennelmenopause', 'rct'),
    ('REF-3557', '28891367', 'fenneldepression', 'rct'),
    ('REF-3558', '33182553', 'fenneldysmenorrhea', 'meta-analysis'),
    ('REF-3559', '25686270', 'ganodermacvcochrane', 'systematic-review'),
    ('REF-3560', '15857210', 'ganopolyneurasthenia', 'rct'),
    ('REF-3561', '22203880', 'ganodermacrf', 'rct'),
    ('REF-3562', '39241163', 'reishistress', 'rct'),
])

BIB = dict(delete=['REF-2352', 'REF-2353'],   # Galium mollugo studies (POWO: a separate species from G. album)
           new=NEW)

CINEOLE = 'compound evidence: 1,8-cineole (eucalyptol) is eucalyptus oil\'s main active compound'

PLAN = {
    'eschscholzia_californica': [
        ('note', 'pain', 'Its alkaloids act on calming GABA-A receptors, and an extract eased pain in mice (preclinical)'),
    ],
    'eucalyptus_globulus': [
        ('newpair', 'asthma', ['REF-3552', 'REF-3553'], 'Added to usual treatment, 1,8-cineole allowed steroid reduction and improved lung function in placebo-controlled asthma trials (' + CINEOLE + ')'),
        ('newpair', 'sinusitis', ['REF-3554'], 'Cineole relieved acute non-purulent sinusitis vs placebo in a randomized trial (' + CINEOLE + ')'),
        ('add', 'respiratory-support', ['REF-3555']),
        ('note', 'cold', 'Used for cough associated with colds (EU herbal monograph; WHO monograph)'),
        ('note', 'immune-support', 'Eucalyptus oil stimulated innate immune cells in lab studies (review)'),
        ('note', 'infection', 'Eucalyptus oil is antibacterial, antifungal and antiviral in lab studies (review)'),
        ('note', 'inflammation', 'Eucalyptus oil reduced inflammation in lab and animal studies (review)'),
        ('note', 'respiratory-support', 'Used for catarrh and cough of the upper airways (EU herbal monograph; WHO monograph); cineole, its main compound, reduced COPD flare-ups vs placebo in a randomized trial'),
    ],
    'euphrasia_officinalis': [
        ('note', 'allergy', 'Traditionally used for hay fever and allergic eye symptoms (Herbal Reality)'),
        ('note', 'cancer', 'Eyebright extracts slowed colon cancer cells in the lab (preclinical)'),
        ('note', 'infection', 'Traditionally used for eye and nasal infections (Herbal Reality); extracts were antibacterial in lab tests (preclinical)'),
        ('note', 'inflammation', 'Extracts reduced inflammatory markers in human corneal cells in the lab (preclinical); traditional use (Herbal Reality)'),
        ('note', 'respiratory-support', 'Traditionally used for catarrh and sinus congestion (Herbal Reality)'),
    ],
    'filipendula_ulmaria': [
        ('arm', 'analgesic', ['REF-0062']), ('arm', 'antimicrobial', ['REF-0062']), ('arm', 'antispasmodic', ['REF-0062']),
        ('arm', 'diuretic', ['REF-0062']), ('arm', 'gastroprotective', ['REF-0062']),   # a macrophage anti-inflammatory study
        ('note', 'inflammation', 'Meadowsweet polyphenols reduced inflammatory markers in immune cells, and extracts reduced inflammation in rats (preclinical)'),
        ('note', 'swelling', 'Traditional remedy for dropsy (fluid retention) (Grieve, A Modern Herbal)'),
        ('note', 'urinary-support', 'Traditional diuretic for urinary complaints (Grieve, A Modern Herbal)'),
        ('note', 'cancer', 'Meadowsweet tincture protected DNA and slowed liver cancer cells in the lab, and an extract reduced radiation-induced tumours in rats (preclinical)'),
    ],
    'filipendula_vulgaris': [
        ('arm', 'astringent', ['REF-2034']),   # a genotoxicity study
        ('note', 'cancer', 'Dropwort extract restrained mesothelioma cancer cells in the lab (preclinical)'),
        ('note', 'inflammation', 'Extracts reduced inflammation in animal models (preclinical)'),
        ('note', 'arthritis', 'inferred from anti-inflammatory action'),
        ('note', 'diarrhea', 'inferred from astringent action'),
        ('note', 'wounds', 'inferred from antimicrobial and astringent action'),
        ('note', 'infection', 'Extracts and essential oil were antimicrobial in lab tests (preclinical)'),
        ('note', 'cognitive-function', 'Extracts had nootropic (memory-supporting) effects in rats, comparable to piracetam (preclinical)'),
    ],
    'foeniculum_vulgare': [
        ('rm', 'muscle-spasm', ['REF-0537']),   # gut/uterine smooth-muscle antispasmodic is not muscle cramps (off-target, inv. 11)
        ('newpair', 'menopause', ['REF-1642', 'REF-3556'], 'Fennel improved menopausal symptoms vs placebo in a meta-analysis and a randomized trial'),
        ('newpair', 'anxiety', ['REF-3557'], 'Fennel reduced anxiety in postmenopausal women in a randomized trial; a meta-analysis found effects on psychological health unclear'),
        ('nulladd', 'anxiety', ['REF-1642']),
        ('newpair', 'depression', ['REF-3557'], 'Fennel reduced depression symptoms in postmenopausal women in a randomized trial; a meta-analysis found effects on psychological health unclear'),
        ('nulladd', 'depression', ['REF-1642']),
        ('add', 'menstrual-cramps', ['REF-3558']), ('add', 'pain', ['REF-3558']),
        ('note', 'infection', 'Antimicrobial activity reported in lab studies (review)'),
        ('note', 'respiratory-support', 'Expectorant for cough associated with colds (EU herbal monograph); expectorant activity reported (review)'),
    ],
    'galium_album': [('purge', 'REF-2352'), ('purge', 'REF-2353'), ('purge', 'REF-0818')],
    'galium_aparine': [
        ('note', 'cancer', 'Cleavers extracts slowed breast cancer and leukaemia cells in the lab (preclinical)'),
        ('note', 'infection', 'Extract was antimicrobial in lab tests (preclinical)'),
        ('note', 'wounds', 'Extract aided wound closure and was antimicrobial in lab tests; an 1883 medical report described its use on chronic ulcers'),
    ],
    'ganoderma_lingzhi': [('arm', a, ['REF-0019']) for a in ('anti-inflammatory', 'anticancer', 'antidiabetic', 'antioxidant', 'antiviral', 'sedative')] + [
        ('nulladd', 'blood-sugar', ['REF-3559']), ('nulladd', 'metabolic-support', ['REF-3559']),
        ('newpair', 'fatigue', ['REF-3560', 'REF-3561'], 'A reishi polysaccharide extract improved neurasthenia (fatigue-dominant) symptoms vs placebo, and spore powder eased cancer-related fatigue in a pilot trial (randomized trials)'),
        ('newpair', 'stress', ['REF-3562'], 'Reishi supplementation reduced psychological stress and improved anxiety, mood and vitality scores in a randomized trial'),
        ('note', 'blood-sugar', 'Antidiabetic effects reported, mostly in lab and animal studies (review); a Cochrane review found the trials do not support reishi for blood sugar or other cardiovascular risk factors in type 2 diabetes'),
        ('note', 'cancer', 'Reishi polysaccharides slowed tumours in lab and animal studies; a Cochrane review found it may improve tumour response and immune markers as an add-on to cancer treatment (low-quality evidence; no proven survival benefit)'),
        ('note', 'immune-support', 'Reishi polysaccharides stimulated immune cells in lab studies; as an add-on in cancer patients it may raise immune markers (Cochrane review; low-quality evidence)'),
        ('note', 'infection', 'Antiviral and antimicrobial activities reported (review)'),
        ('note', 'cold', 'inferred from immunomodulator action'),
    ],
    'gentiana_lutea': [
        ('arm', 'digestive', ['REF-0580']),   # genus-level Gentiana review (Chinese species, prose-only attribution); kept in references
    ],
}

NOTES = {
    'eschscholzia_californica': 'Deep re-sweep. Pain note rewritten to its lab sources. No single-herb trials on PubMed (only the excluded combination product).',
    'eucalyptus_globulus': 'Deep re-sweep. Landmark 1,8-cineole RCTs added (signature compound, labelled; inv. 10): asthma REF-3552/REF-3553 (new pair, owner rule), acute sinusitis REF-3554 (new pair), COPD exacerbations REF-3555 (respiratory-support). Notes rewritten. Not added: eucalyptus cough MA 35294302 ("efficacy minimal and of uncertain clinical importance") - no cough pair; recorded here as a negative finding for the owner.',
    'euphrasia_officinalis': 'Deep re-sweep. Notes rewritten to their sources (Herbal Reality; lab studies). No trials on PubMed beyond the purged homeopathic eye drops.',
    'filipendula_ulmaria': 'Deep re-sweep. REF-0062 (THP1 macrophage polyphenol study) removed from analgesic, antimicrobial, antispasmodic, diuretic and gastroprotective actions. Notes rewritten (Grieve: dropsy, diuretic). Gap: EU monograph REF-3072 also names supportive treatment of the common cold - no cold pair (no SR/RCT). Functional beverage RCT 24237191 not used (3-herb drink).',
    'filipendula_vulgaris': 'Deep re-sweep. Genotoxicity study REF-2034 removed from the astringent action. Mechanistic notes trimmed of unsourced claims ("salicylates", "traditional wound-wash use").',
    'foeniculum_vulgare': 'Deep re-sweep. Muscle-spasm dropped (REF-0537 antispasmodic = smooth muscle; off-target). New pairs (owner rule): menopause (held MA REF-1642 + RCT REF-3556); anxiety and depression (RCT REF-3557), each with REF-1642 recorded as no-effect (it found effects on psychological health unclear). Dysmenorrhoea MA REF-3558 added to menstrual-cramps and pain. Gap: EU monograph bloating/flatulence use has no pair (no SR/RCT; infantile colic RCT 12868253 is not bloating).',
    'galium_album': 'Deep re-sweep. REF-2352 and REF-2353 study Galium mollugo, a separate species (POWO) - purged and deleted. REF-0818 (Estonian Galium species; abstract names G. mollugo, not G. album) purged here, kept for G. aparine.',
    'galium_aparine': 'Deep re-sweep. Notes rewritten. No trials on PubMed.',
    'ganoderma_lingzhi': 'Deep re-sweep. Polysaccharide-structure study REF-0019 removed from six actions (kept for immunomodulator). Cochrane 2015 REF-3559 (does not support G. lucidum for cardiovascular risk factors in type 2 diabetes) recorded as no-effect for blood-sugar and metabolic-support. New pairs (owner rule): fatigue (Ganopoly neurasthenia RCT REF-3560; cancer-fatigue pilot REF-3561), stress (RCT REF-3562). "Ganoderma lucidum" literature counts for G. lingzhi (inv. 11).',
    'gentiana_lutea': 'Deep re-sweep. Genus review REF-0580 removed from the digestive action (kept in references). PubMed "gentian" trials are gentian violet (a synthetic dye) - not relevant.',
}

if __name__ == '__main__':
    fixlib.main_with_bib(PLAN, NOTES, 'deep re-sweep batch 7', os.path.join(HERE, 'deep', 'd07_changes.tsv'), **BIB)
