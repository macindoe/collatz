# Schema and Maintenance Workflows

This repository follows the LLM-wiki pattern: three layers with different mutation rules.

## Layers

1. **`sources/`** — immutable. Historical drafts (v000–v078), PDFs, residue data. Read for provenance; never edit, never delete. New monolith drafts are no longer created — the wiki pages are the live document.
2. **Wiki pages** (`index.md`, `spine.md`, `program.md`, `stage1.md`–`stage3.md`, `open-problems.md`, `archive/`) — evergreen. Each carries front matter (`status`, `scope`, `updated`) and a "Current state" paragraph. Pages are rewritten in place to carry the current best answer; history is git's job, not the page's.
3. **`experiments/`** — verification and pilot code. Each script states which page/result it supports. Scripts are kept runnable; results (counts, ranges, dates) are quoted in the owning page.
4. **`README.md`** — the human-facing map, including the program's strategy and stopping rules. Those rules are binding on agents too: check them before opening new computational fronts (in particular: no per-period cycle searches unless they serve the uniform trim lemma).
5. **This file** — the schema. Update it when the structure or workflows change.

## Conventions

- Monolith section numbers (`11.8.6.3`, `9.8.3`, …) are the stable citation anchors. Do not renumber them. The resolver in `index.md` maps numbers to pages.
- Every fact lives in exactly one page. Other pages point to it; they do not restate it. (The staleness that motivated this wiki came from duplicated status claims.)
- Math statements are edited conservatively: never "improve" a proof while doing organizational work. Separate commits for content vs. structure.
- **No change logs in tracked files.** History is git's job (see Layers) — that is the point of a version-controlled repo, and it is not an agent's job to duplicate it by hand. Do not keep running session journals, dated "verification records", branch-by-branch narration, or "was X, now Y" prose in any page or in this file. A page states the *current* answer; how it got there is the commit log (`git log`, per-commit messages). The `status:` and `source:` front-matter fields are metadata, not a diary: `status:` is a short state word or phrase (plus at most a pointer), `source:` names where the page originated. When a result is verified, record the *current* verification inline per the proved-claim workflow below — what was checked, the range, the date, one line — and overwrite it next time rather than appending a new entry.

## Workflows

### When a result's status changes (proved / refuted / dissolved)

1. Update the owning page: front matter `status` + `updated`, the "Current state" paragraph, and the statement itself.
2. Update the compact ledger (stage1.md 11.8.4.5).
3. Sweep `open-problems.md` for entries that posed the question as open; add a calibration note pointing to the closure.
4. If stage-level, update `program.md` and the status summary in `index.md`.
5. Refuted claims are not deleted: move the claim + refutation evidence to `archive/`, leave a pointer.

### When adding a new result

- Proved structural material about the formalism itself → `spine.md`.
- Stage results → the owning stage page.
- New open questions → `open-problems.md`, phrased so that closure is checkable.

### Before marking anything "proved"

Run an independent numerical check (not the one quoted in the text — a fresh implementation), and record what was checked, the range, and the date in the page. Precedent: the v077 laws were re-verified with independent code over 8,000 random states and orbit traces, zero discrepancies (2026-07-06).

### Periodic status pass

Occasionally diff every page's claims about *other* pages against those pages' own front matter. Any mismatch is a bug. This is the wiki's replacement for the monolith-era problem of §11.1–11.6 rotting while §11.8 moved on.

## Verification record

History lives in the git log, not here — `git log --oneline` for the change stream, individual commit messages for what each change checked and why. This file is the schema; it carries no running journal. Per-result verification (what was checked, the range, the date) lives inline in the owning page, per "Before marking anything proved" above, as a single current line that is overwritten on re-verification rather than appended to.
