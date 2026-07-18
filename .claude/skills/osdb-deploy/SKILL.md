---
name: osdb-deploy
description: "Publish plant-database changes to omniasana.bio — validate, build, commit, push to the osdb remote, then force the WordPress sync and verify the change is actually live. Use whenever DB work needs to reach the site, or when a change was pushed but the site still shows old data."
---

# Getting a change live

Data reaching `osdb/main` is not data reaching the website. There are two more
hops — CI, then the WordPress pull — and each has a way of silently not happening.
Verify at the end; do not assume.

## 1. Validate and build

```bash
python scripts/validate.py     # exit 0 required — hard gate
python scripts/build.py
```

Commit the regenerated `build/*.json` alongside the data. CI skips the rebuild
when your outputs already match (`git diff --quiet -- build/`), which keeps this a
single clean push.

`build/*.draft.json` is gitignored on purpose — those are unreviewed safety-record
twins. `build/` ships approved-only. Never commit a draft twin.

## 2. Push

```bash
git push osdb main
```

**`osdb`** = `github.com/EsmuRihards/omnia-sana-plant-database` — canonical, push here.
**`origin`** = `github.com/EsmuRihards/OmniaSana` — the old website-export monorepo,
unrelated history. **Never push DB work there.** It would be rejected or clobber.

Never force-push. History here is an audit trail for published health claims.

Auth goes through the Windows credential manager; `gh` is not installed.

CI `build-and-publish.yml` fires on changes to `plants/**`, `names/**`,
`vocabularies/**`, `compounds/**`, `bibliography.bibtex`, `schema/**`, `scripts/**`.
It verifies vernacular names for any *new* plant, re-validates, rebuilds, and
commits back in one push. An actor guard skips the bot's own commits — if you see
CI not running, check whether the last commit was the bot's. `build/` is
deliberately not a trigger path.

## 3. Pull it into WordPress

The site syncs from `osdb/main` raw files via the sandbox plugins — hourly WP-cron,
lazy-on-request, plus a GitHub push webhook. To force it immediately, call the
sync function for each surface the change touches (via novamira execute-php):

| Surface | Function |
| --- | --- |
| Knowledge Finder (citations) | `os_kf_do_sync(true)` |
| Plant pages / Materia Medica | `os_pe_sync(true)` |
| Symptom-to-Plant Lookup | `os_sym_do_sync(true)` |
| Herb-drug + herb-herb safety | `os_safety_sync(true)` |
| Dangerous Lookalikes | `os_lk_sync(true)` |
| Plant-name dictionary | `os_pp_sync(true)` |

Call the ones your change actually affects. A citation-only change needs
`os_kf_do_sync`; a new indication needs `os_sym_do_sync` too.

### Expected non-errors

- **`os_sym_do_sync` returning "data block not matched" is normal.** The symptom
  tool's data no longer lives inline in page 201 — it lives in
  `uploads/os-tools/os-sym.js`, and `os_sym_cache` is authoritative. The
  page-write path is dead; the cache was still updated. Do not chase this.
  `os-sym-jsbake.php` rebakes `os-sym.js` when the cache changes.
- **`os_safety_sync` output looks stale for ~5 minutes** — CDN caching. Trust the
  sha reported by `os_kf_do_sync` rather than re-running it.

## 4. Verify it is actually live

Do not report success from a green sync call. Check the public surface:

- Knowledge Finder record count moved, or the new `REF-` is findable.
- The plant page shows the new field.
- The condition appears in the Symptom tool.

If the site still shows old data after a successful sync, purge the page cache
(`\SpeedyCache\Delete::all_cache()`).

## Front-end caveats when a data change needs a JS change

- **Knowledge Finder JS is manually versioned** `?v=kfN` in page 208. Editing the
  JS without bumping that serves the old file from cache. Bump it.
- **`os-cards.php` generates `os-cards.css`** — bump `OS_CARDS_VER` and call
  `os_cards_maybe_write()`, or the CSS never regenerates.
- **novamira write-file / edit-file refuse PHP outside the sandbox.** To edit theme
  PHP, use execute-php + `file_put_contents`. Lint first
  (`shell_exec(PHP_BINARY.' -l')`) and back the original up into the sandbox.

## If the site breaks after a sandbox PHP edit

A PHP fatal in `wp-content/novamira-sandbox/` makes the loader write a `.crashed`
marker, and **safe mode then disables every sandbox file site-wide** — map, tools,
carousel, account, comments all dead at once. Deleting the bad file does **not**
recover it.

```php
unlink('wp-content/novamira-sandbox/.crashed');   // hidden dotfile — this is the fix
```

## Rollback

`git revert` the data commit, re-run validate + build, push, re-sync. Do not
hand-edit live data to patch over a bad push — the database is the backbone, and
a divergent live copy means the next sync silently reintroduces the bug.
