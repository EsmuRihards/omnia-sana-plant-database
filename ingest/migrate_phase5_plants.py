#!/usr/bin/env python3
"""
migrate_phase5_plants.py — architecture migration, Phase 5 (the core rewrite).

Rewrites every plants/*.yaml from the old embedded-free-text schema to the new
entity schema:
  * medicinal_actions[].action (free text) -> actions[].action (vocab id) + parts
    + indications[].condition (vocab id) + evidence, with the ORIGINAL string kept
    verbatim as a `note` (nothing is lost).
  * constituents[].name kept verbatim + compounds:[ids] linked from compound synonyms.
  * reference_ids become claim-level (union of refs from the strings that map to
    each id) — as claim-level as the source allows; book-derived records (where all
    actions shared one ref set) are flagged provenance: book.
  * indication evidence (1-5) is seeded from the curated Symptom-to-Plant Lookup
    scores where available, else derived from the source string + status.

Usage:  python ingest/migrate_phase5_plants.py            # DRY RUN (report only)
        python ingest/migrate_phase5_plants.py --apply     # rewrite the files
"""
import os, re, sys, glob, json, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
COMPDIR = os.path.join(ROOT, "compounds")
SYMPTOM = os.path.join(ROOT, "ingest", "archive", "sources", "symptom_lookup.json")

STATUS_RANK = {"verified": 0, "draft": 1, "needs-review": 2}


def clean_label(lbl):
    return lbl.split("/")[0].split("(")[0].strip().lower()


def load_keyword_index(path_glob_or_file, kind):
    """Return list of (keyword, id) sorted longest-first, from a vocab list file."""
    if kind == "compound":
        items = []
        for f in glob.glob(os.path.join(COMPDIR, "*.yaml")):
            items.append(yaml.safe_load(open(f, encoding="utf-8")))
    else:
        items = yaml.safe_load(open(path_glob_or_file, encoding="utf-8"))
    kw = {}
    for it in items:
        cid = it["id"]
        keys = set(it.get("synonyms", []) or []) | set(it.get("consumer_synonyms", []) or [])
        keys.add(cid.replace("-", " "))
        if it.get("label"):
            keys.add(clean_label(it["label"]))
        if kind != "compound":
            keys.add(cid)  # the slug/abbrev itself (e.g. uti, pms, ibs)
        for k in keys:
            k = k.strip().lower()
            if len(k) >= 3:
                kw.setdefault(k, cid)
    return sorted(kw.items(), key=lambda x: -len(x[0]))


def matches(text, kw_index):
    """Distinct ids whose keyword occurs in text (word-boundary)."""
    out = []
    for k, cid in kw_index:
        if cid in out:
            continue
        if re.search(r"\b" + re.escape(k) + r"(?:e?s)?\b", text):
            out.append(cid)
    return out


def split_parts(name):
    return [p.strip() for p in str(name).split("/") if p.strip()]


def is_rich(s):
    sl = s.lower()
    return len(s) > 26 or any(c in s for c in "(),") or " for " in sl or " - " in s


def evidence_from(s, status):
    sl = s.lower()
    if any(k in sl for k in ["meta-analysis", "meta analysis", "systematic review", "cochrane",
                              "randomi", "rct", "double-blind", "placebo-controlled", "clinical trial"]):
        base = 4
    elif "tradition" in sl:
        base = 2
    else:
        base = 3
    if status == "needs-review":
        base = min(base, 2)
    return base


def worst(statuses):
    return max(statuses, key=lambda s: STATUS_RANK.get(s, 0)) if statuses else "verified"


def severity_from(note):
    n = note.lower()
    if any(k in n for k in ["carcinogen", "hepatotox", "mutagen", "banned", "genotoxic"]):
        return "serious"
    if any(k in n for k in ["avoid", "contraindicat", "should not", "do not", "pregnan",
                            "interact", "caution", "anticoagulant", "surgery", "not be used"]):
        return "caution"
    return "info"


def provenance_from(internal):
    inl = (internal or "").lower()
    prov = []
    if "book manuscript" in inl or "koffetablbok" in inl:
        prov.append("book")
    if "omniasana.bio" in inl or "materia medica" in inl:
        prov.append("website")
    if "pubmed" in inl:
        prov.append("pubmed")
    if "symptom-to-plant" in inl or "symptom lookup" in inl or "symptom tool" in inl:
        prov.append("symptom-tool")
    return "+".join(dict.fromkeys(prov)) or "unknown"


def find_refs(node):
    out = set()
    if isinstance(node, dict):
        for v in node.values():
            out |= find_refs(v)
    elif isinstance(node, list):
        for v in node:
            out |= find_refs(v)
    elif isinstance(node, str):
        out |= set(re.findall(r"REF-\d{4,}", node))
    return out


def main():
    apply = "--apply" in sys.argv
    A = load_keyword_index(os.path.join(VOCAB, "actions.yaml"), "action")
    C = load_keyword_index(os.path.join(VOCAB, "conditions.yaml"), "condition")
    K = load_keyword_index(None, "compound")
    actions_meta = {a["id"]: a for a in yaml.safe_load(open(os.path.join(VOCAB, "actions.yaml"), encoding="utf-8"))}

    symptom = {}
    for p in json.load(open(SYMPTOM, encoding="utf-8")):
        symptom[p["l"].strip().lower()] = p["s"]

    unmapped, stats = [], dict(plants=0, actions_in=0, act_ids=0, ind_ids=0, comp_links=0)

    for path in sorted(glob.glob(os.path.join(PLANTS, "*.yaml"))):
        d = yaml.safe_load(open(path, encoding="utf-8"))
        stats["plants"] += 1
        pid = re.sub(r"\s+", "-", d["scientific_name"].strip().lower())
        pid = re.sub(r"[^a-z0-9-]", "", pid)

        actions, indications, all_parts, plant_unmapped = {}, {}, [], []
        for pu in (d.get("parts_used") or []):
            parts = split_parts(pu.get("name", ""))
            all_parts += parts
            for ma in (pu.get("medicinal_actions") or []):
                s = str(ma.get("action", "")).strip()
                refs = ma.get("reference_ids", []) or []
                st = ma.get("status", "verified")
                stats["actions_in"] += 1
                low = s.lower()
                aids = matches(low, A)
                cids = matches(low, C)
                rich = is_rich(s)
                for aid in aids:
                    a = actions.setdefault(aid, dict(refs=set(), parts=set(), st=[], notes=set()))
                    a["refs"].update(refs); a["parts"].update(parts); a["st"].append(st)
                    if rich: a["notes"].add(s)
                ev = evidence_from(s, st)
                for cid in cids:
                    g = indications.setdefault(cid, dict(refs=set(), st=[], ev=0, notes=set()))
                    g["refs"].update(refs); g["st"].append(st); g["ev"] = max(g["ev"], ev)
                    if rich: g["notes"].add(s)
                if not aids and not cids:
                    unmapped.append((os.path.basename(path), s))
                    plant_unmapped.append(s)

        # mechanism-inferred indications from each mapped action's related_conditions
        # (low-confidence: evidence 2, needs-review, sourced to the action's own refs)
        for aid, a in actions.items():
            for rc in (actions_meta.get(aid, {}).get("related_conditions") or []):
                if rc not in indications:
                    indications[rc] = dict(refs=set(a["refs"]), st=["needs-review"], ev=2,
                                           notes={"inferred from %s action" % aid})

        # seed/raise indication evidence from the curated Symptom-tool scores
        for cid, score in symptom.get(d.get("scientific_name", "").strip().lower(), {}).items():
            g = indications.setdefault(cid, dict(refs=set(), st=["needs-review"], ev=0, notes=set()))
            g["ev"] = max(g["ev"], int(score))

        # ---- build new record ----
        rec = {}
        rec["id"] = pid
        rec["scientific_name"] = d["scientific_name"]
        rec["common_names"] = d.get("common_names", [])
        rec["family"] = d.get("family", "")
        seen = set(); parts_list = [p for p in all_parts if not (p in seen or seen.add(p))]
        if parts_list:
            rec["parts_used"] = parts_list

        new_const = []
        for c in (d.get("constituents") or []):
            name = c.get("name", "")
            text = (name + " " + (c.get("note", "") or "")).lower()
            cmps = matches(text, K)
            stats["comp_links"] += len(cmps)
            nc = {"name": name}
            if cmps: nc["compounds"] = cmps
            if c.get("note"): nc["note"] = c["note"]
            if c.get("reference_ids"): nc["reference_ids"] = c["reference_ids"]
            new_const.append(nc)
        if new_const:
            rec["constituents"] = new_const

        rec_actions = []
        for aid in sorted(actions):
            a = actions[aid]
            stats["act_ids"] += 1
            e = {"action": aid}
            pl = [p for p in parts_list if p in a["parts"]]
            if pl and len(pl) < len(parts_list):
                e["parts"] = pl
            notes = sorted(n for n in a["notes"] if n.lower() != aid.replace("-", " "))
            if notes:
                e["note"] = "; ".join(notes)
            e["reference_ids"] = sorted(a["refs"])
            e["status"] = worst(a["st"])
            rec_actions.append(e)
        if rec_actions:
            rec["actions"] = rec_actions

        rec_ind = []
        for cid in sorted(indications):
            g = indications[cid]
            stats["ind_ids"] += 1
            e = {"condition": cid, "evidence": g["ev"] or 2}
            if g["notes"]:
                e["note"] = "; ".join(sorted(g["notes"]))
            e["reference_ids"] = sorted(g["refs"])
            e["status"] = worst(g["st"]) if g["st"] else "needs-review"
            rec_ind.append(e)
        if rec_ind:
            rec["indications"] = rec_ind

        new_contra = []
        for c in (d.get("contraindications") or []):
            nc = {"note": c.get("note", ""), "severity": severity_from(c.get("note", ""))}
            if c.get("reference_ids"): nc["reference_ids"] = c["reference_ids"]
            nc["status"] = c.get("status", "verified")
            new_contra.append(nc)
        if new_contra:
            rec["contraindications"] = new_contra

        extra = sorted(find_refs(d) - find_refs(rec))   # any ref not re-cited on a claim
        if extra:
            rec["references"] = extra

        rec["provenance"] = provenance_from(d.get("internal_notes", ""))
        rec["status"] = d.get("status", "verified")
        rec["last_updated"] = d.get("last_updated", "")
        note = d.get("internal_notes", "") or ""
        add = "2026-06-15: migrated to entity schema (actions->vocab ids, indications split out, constituents linked to compounds)."
        if plant_unmapped:
            add += " Unmapped uses kept for reference: " + " | ".join(plant_unmapped) + "."
        rec["internal_notes"] = (note + " | " + add) if note else add

        if apply:
            with open(path, "w", encoding="utf-8") as fh:
                yaml.safe_dump(rec, fh, allow_unicode=True, sort_keys=False, width=100)

    print(("APPLIED" if apply else "DRY RUN") + " — Phase 5 plant rewrite")
    for k, v in stats.items():
        print(f"  {k:12s}: {v}")
    print(f"  unmapped strings: {len(unmapped)}")
    if unmapped:
        from collections import Counter
        common = Counter(s for _, s in unmapped).most_common(25)
        print("  --- top unmapped action strings ---")
        for s, n in common:
            print(f"    {n:3d}x  {s[:90]}")


if __name__ == "__main__":
    main()
