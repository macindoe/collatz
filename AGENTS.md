# Schema and Maintenance Workflows

This repository follows the LLM-wiki pattern: three layers with different mutation rules.

## Layers

1. **`sources/`** — immutable. Historical drafts (v000–v078), PDFs, residue data. Read for provenance; never edit, never delete. New monolith drafts are no longer created — the wiki pages are the live document.
2. **Wiki pages** (`index.md`, `spine.md`, `program.md`, `stage1.md`–`stage3.md`, `open-problems.md`, `archive/`) — evergreen. Each carries front matter (`status`, `scope`, `updated`) and a "Current state" paragraph. Pages are rewritten in place to carry the current best answer; history is git's job, not the page's.
3. **This file** — the schema. Update it when the structure or workflows change.

## Conventions

- Monolith section numbers (`11.8.6.3`, `9.8.3`, …) are the stable citation anchors. Do not renumber them. The resolver in `index.md` maps numbers to pages.
- Every fact lives in exactly one page. Other pages point to it; they do not restate it. (The staleness that motivated this wiki came from duplicated status claims.)
- Math statements are edited conservatively: never "improve" a proof while doing organizational work. Separate commits for content vs. structure.

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

- 2026-07-06 — wiki split from `sources/drafts/collatz_reduction_rewrite_v078.md`; concatenation of page bodies reproduces the monolith byte-identically.
- 2026-07-06 — independent numeric verification of: unified depth-side law (11.8.5.6.2), entry-depth law all six classes (11.8.6.3), orbit projection + fiber of (1,1) (9.8), 8,000 random states + orbit traces, zero failures.
