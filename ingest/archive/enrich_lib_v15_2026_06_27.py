#!/usr/bin/env python3
"""
enrich_lib_v15_2026_06_27.py — shared, idempotent helper for the 2026-06-27
">=15 scientific publications" enrichment (user request: bring the six
identification-blog plants up to at least fifteen peer-reviewed @article
references, and create the three missing records).

Identical mechanics to enrich_lib_v10_2026_06_20.py (append @article bib entries
with dedup by citekey AND doi; weave each new REF-id into the matching
action/indication/constituent entry's reference_ids AND the plant-level
`references:` bucket; stamp provenance +pubmed). Only the date stamp and the
internal-notes marker differ, so re-runs of either pass remain idempotent and
the audit trail stays accurate.

Source dict shape (unchanged):
  {"citekey": str, "plant": "<plant_file_stem>", "study_type": str,
   "fields": {"author","title","journal","year","volume","number","pages","doi","url"},
   "abstract": str (optional),
   "actions": [action_id, ...] (optional), "indications": [condition_id, ...] (optional),
   "constituents": [constituent_name_substr, ...] (optional)}
study_type in {systematic-review, meta-analysis, rct, clinical, preclinical, traditional}
"""
import os, re, html, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIB = os.path.join(ROOT, "bibliography.bibtex")
PLANTS = os.path.join(ROOT, "plants")

FIELD_ORDER = ["author", "title", "journal", "year", "volume", "number", "pages", "doi", "url"]
NOTE_MARKER = "2026-06-27: enriched to >=15 scientific publications"
STAMP_DATE = "2026-06-27"


def clean_text(s):
    if not s:
        return ""
    s = html.unescape(s)
    s = s.replace("{", "(").replace("}", ")")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fmt_entry(citekey, ref_id, study_type, fields, abstract):
    lines = ["@article{%s," % citekey]
    body = []
    for k in FIELD_ORDER:
        v = clean_text(fields.get(k, ""))
        if v:
            body.append("  %s = {%s}" % (k.ljust(8), v))
    body.append("  %s = {%s}" % ("note".ljust(8), ref_id))
    body.append("  %s = {%s}" % ("study_type".ljust(8), study_type))
    ab = clean_text(abstract)
    if ab:
        body.append("  %s = {%s}" % ("abstract".ljust(8), ab))
    return lines[0] + "\n" + ",\n".join(body) + "\n}\n"


def existing_citekeys(text):
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", text))


def citekey_to_ref(text):
    out = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", text, re.S):
        r = re.search(r"REF-\d{4,}", m.group(2))
        if r:
            out[m.group(1)] = r.group(0)
    return out


def _norm_doi(d):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", (d or "").strip().lower())


def doi_to_ref(text):
    out = {}
    for m in re.finditer(r"@\w+\s*\{\s*[^,\s]+\s*,(.*?)(?=\n@|\Z)", text, re.S):
        body = m.group(1)
        dm = re.search(r"doi\s*=\s*\{([^}]*)\}", body)
        rm = re.search(r"REF-\d{4,}", body)
        if dm and rm and dm.group(1).strip():
            out[_norm_doi(dm.group(1))] = rm.group(0)
    return out


def max_ref(text):
    ids = [int(x) for x in re.findall(r"REF-(\d{4,})", text)]
    return max(ids) if ids else 0


def insert_before(d, newkey, newval, beforekey):
    out = {}
    inserted = False
    for k, v in d.items():
        if k == newkey:
            continue
        if k == beforekey and not inserted:
            out[newkey] = newval
            inserted = True
        out[k] = v
    if not inserted:
        out[newkey] = newval
    return out


def _weave(entries, match_key, target, ref_id):
    for e in entries or []:
        if str(e.get(match_key)) == str(target):
            rids = list(e.get("reference_ids", []))
            if ref_id not in rids:
                rids.append(ref_id)
                e["reference_ids"] = rids
            return True
    return False


def apply(sources):
    bib = open(BIB, encoding="utf-8").read()
    have = existing_citekeys(bib)
    c2r = citekey_to_ref(bib)
    d2r = doi_to_ref(bib)
    nextid = max_ref(bib) + 1

    appended = []
    warnings = []
    plant_data = {}
    for s in sources:
        ck = s["citekey"]
        doi = _norm_doi(s.get("fields", {}).get("doi", ""))
        if ck in have:
            ref_id = c2r.get(ck)
            warnings.append("citekey already in bib (reused, NOT new): %s -> %s" % (ck, ref_id))
        elif doi and doi in d2r:
            ref_id = d2r[doi]
            warnings.append("DOI already in bib (reused, NOT new): %s -> %s [%s]" % (doi, ref_id, ck))
        else:
            ref_id = "REF-%04d" % nextid
            nextid += 1
            appended.append(fmt_entry(ck, ref_id, s["study_type"], s["fields"], s.get("abstract", "")))
            have.add(ck)
            c2r[ck] = ref_id
            if doi:
                d2r[doi] = ref_id
        pd = plant_data.setdefault(s["plant"], {"refs": [], "weave": []})
        if ref_id not in pd["refs"]:
            pd["refs"].append(ref_id)
        for a in s.get("actions", []) or []:
            pd["weave"].append((ref_id, "action", a))
        for i in s.get("indications", []) or []:
            pd["weave"].append((ref_id, "condition", i))
        for c in s.get("constituents", []) or []:
            pd["weave"].append((ref_id, "constituent", c))

    if appended:
        bib = bib.rstrip("\n") + "\n\n" + "\n".join(appended)
        open(BIB, "w", encoding="utf-8").write(bib)

    changed = []
    for stem, pd in plant_data.items():
        path = os.path.join(PLANTS, stem + ".yaml")
        d = yaml.safe_load(open(path, encoding="utf-8"))
        woven = 0
        missed = []
        for ref_id, kind, target in pd["weave"]:
            ok = False
            if kind == "action":
                ok = _weave(d.get("actions"), "action", target, ref_id)
            elif kind == "condition":
                ok = _weave(d.get("indications"), "condition", target, ref_id)
            elif kind == "constituent":
                for e in d.get("constituents", []) or []:
                    if target.lower() in str(e.get("name", "")).lower():
                        rids = list(e.get("reference_ids", []))
                        if ref_id not in rids:
                            rids.append(ref_id)
                            e["reference_ids"] = rids
                        ok = True
                        break
            woven += 1 if ok else 0
            if not ok:
                missed.append("%s->%s:%s" % (ref_id, kind, target))
        bucket = list(d.get("references", []))
        for r in pd["refs"]:
            if r not in bucket:
                bucket.append(r)
        d = insert_before(d, "references", bucket, "provenance")
        prov = str(d.get("provenance", "")).strip()
        if "pubmed" not in prov:
            d["provenance"] = (prov + "+pubmed") if prov else "pubmed"
        d["last_updated"] = STAMP_DATE
        notes = d.get("internal_notes", "") or ""
        if NOTE_MARKER not in notes:
            sentence = (" | %s: added %d PubMed-verified @article sources (%s) — woven into "
                        "relevant actions/indications and the plant-level references bucket." %
                        (NOTE_MARKER, len(pd["refs"]), ", ".join(pd["refs"])))
            d["internal_notes"] = (notes.rstrip() + sentence) if notes else sentence.lstrip(" |").strip()
        out = yaml.safe_dump(d, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
        open(path, "w", encoding="utf-8").write(out)
        changed.append((stem, pd["refs"], woven, missed))

    print("bibliography: %d new entries appended (next id now REF-%04d)" % (len(appended), nextid))
    for stem, refs, woven, missed in changed:
        print("  %-30s +%d refs, %d woven into facts" % (stem, len(refs), woven))
        if missed:
            print("      UNWOVEN (target not found, bucket-only): %s" % "; ".join(missed))
    if warnings:
        print("WARNINGS (%d) — NOT newly added:" % len(warnings))
        for w in warnings:
            print("  ! " + w)
    return changed


def add_facts(stem, actions=None, indications=None):
    """Pre-create vocab-id action/indication entries (empty reference_ids) on a
    plant so apply()'s weaver has a target to fill. Idempotent: skips ids already
    present. Inserts actions before any existing 'indications'/'contraindications'
    key and indications before 'contraindications'/'references' to keep order sane.
    """
    path = os.path.join(PLANTS, stem + ".yaml")
    d = yaml.safe_load(open(path, encoding="utf-8"))
    if actions:
        have = {a.get("action") for a in d.get("actions", [])}
        lst = list(d.get("actions", []))
        for aid in actions:
            if aid not in have:
                lst.append({"action": aid, "reference_ids": [], "status": "verified"})
        d["actions"] = lst
    if indications:
        have = {i.get("condition") for i in d.get("indications", [])}
        lst = list(d.get("indications", []))
        for cid in indications:
            if cid not in have:
                lst.append({"condition": cid, "reference_ids": [], "status": "verified"})
        d["indications"] = lst
    out = yaml.safe_dump(d, sort_keys=False, allow_unicode=True, default_flow_style=False, width=100)
    open(path, "w", encoding="utf-8").write(out)
