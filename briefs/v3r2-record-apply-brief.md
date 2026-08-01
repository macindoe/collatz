# Brief: apply round 2 to the record (v3 round 2, Phase 2 — wiki only)

**You edit wiki pages only.** A sibling delegate is editing `paper/collatz-reduced-v3.tex` in the same working tree at the same time. **Do not touch the `.tex` or the PDF**, and **run no `git` command of any kind** — no add, commit, branch, checkout, stash, or push. The main session handles all version control.

Files in your scope: `aeh.md`, `README.md`, `bridge.md`, `publication.md`, `itinerary.md`. Nothing else. **`reverse.md` is explicitly out of scope** — its §14.5.3 "measured stationary depth distribution" is the reverse tree's depth law, a different object, and previous sweeps have wrongly "corrected" it.

## Where the decisions live

Read these and use their drop-in text; do not re-derive their conclusions.

| file | supplies |
|---|---|
| `briefs/v3r2-aeh-formulation-findings.md` | §6.4 `13.2.1`; §6.5 `13.6.4`'s definition; §6.6 all of §13.3; §6.7 `13.6.6`; §6.8 `13.6.7` |
| `briefs/v3r2-syrac-identity-findings.md` | §9 — the attribution paragraph for `13.6.5` |
| `briefs/v3r2-wirsching-check-findings.md` | §4.1 — the replacement `publication.md` bullet |
| `briefs/v3r2-contraction-literature-findings.md` | what Inselmann/Korec/Tao subsume, for `publication.md`'s verdict |
| `briefs/v3r2-thomas-check-findings.md` | the Thomas result, which points the record's way |

## Decisions taken (authoritative)

1. **AEH takes the ensemble form** of `v3r2-aeh-formulation-findings.md` §3.
2. **The descent/contraction consequence is DROPPED**, and the drift rider with it — Inselmann proves the same thing unconditionally at natural density 1. `13.3.2`'s drift clause must stop asserting a deduction it does not have.
3. **`13.6.5`'s law is Tao's `Syrac(Z_3)/2`** — attribution owed, values unchanged.
4. **Wirsching and Thomas are cleared** and do not displace Tao.

## The work

**A. `aeh.md` — the main task.**

- **Front matter and Current state.** Both still describe `π_k`'s depth component as "the stationary law of the exact window chain", which `13.6.5` refutes. Rewrite both **directly around the exact convolution law** `d = m + a`, `m ~ geometric(1/2)`, `m ⊥ a`. Also bring the Current state into line with the new hypothesis form.
- **`13.2`'s `π_k` definition (L20).** Same repair: the depth component is the exact convolution law, stated here, not deferred. Keep the pointer to `13.6.5` for the values.
- **Hypothesis `13.2.1` (L22)** → §6.4's drop-in.
- **`13.6.4`'s bulk-frequency definition (L101)** → §6.5's drop-in. Statement and proof are otherwise unchanged.
- **`13.6.6` (L129)** → §6.7. Its "the bulk cut is precisely what makes the integer question nondegenerate" is wrong and is the sentence the paper's old L245 was written from.
- **`13.6.7` (L131)** → §6.8. It still describes the retired sample space.
- **§13.3.1–13.3.3** → §6.6. The ledger and `1/3` rate survive restated; the drift/contraction clause does not survive as a deduction.
- **`13.6.5`** — add the Tao attribution paragraph from `v3r2-syrac-identity-findings.md` §9. **Change no value.** The *contrast* finding (window chain `17/63`, `4/63` vs exact `19/63`, `2/63`) is internal to this record and stays.
- **The `(q2)` bullet in `13.6.4`.** It currently tells the reader to retroactively reinterpret `13.2`'s definition. Once `13.2` states the exact law directly, fold this into a plain forward reference. This is the AGENTS.md "current answer in one place" repair — the reviewer's finding 3.
- **`D_k` is never defined anywhere on the page** (`13.2` writes `min(d, D_k)`). You are rewriting that definition; define it, or remove the dependence.
- **Reconcile `13.4`'s methodology sentence (L36) with `13.5`'s standing rule (L53).** Per-orbit means are safe exactly when the denominator is deterministic, unsafe when it is the random count of qualifying visits. The quenched hypothesis needs per-orbit statistics, so this is now load-bearing.
- **Optional, flag if you skip it:** the statements say `x_exit > X` while the code cuts on `ω_+ > X` (`aeh_calibration.py` L361/L402). Harmless but the two should agree.

**B. `README.md` L40 and `bridge.md` L69.** Both say the conditional consequences hold "almost-everywhere". Replace with the density-of-starting-values form at a prescribed finite horizon. Keep both edits minimal — these are pointer pages.

**C. `publication.md`.** Three repairs.
- **L21** → the replacement bullet at `v3r2-wirsching-check-findings.md` §4.1. Two factual errors: they are **predecessor**-counting functions, not stopping-time; and the verdict was aimed only at `14.15.3`(c) and must now also name `13.6.3`(v)/`13.6.5`.
- **L28** lists Wirsching as "prior art for §13's product law". That is now established to be wrong. Remove the phrase.
- **The novelty verdict is stale**, and the page's `status: novelty sweep COMPLETE` overstates it. This round found that the AEH descent consequence is subsumed by Inselmann (2024) and that `13.6.5`'s law is Tao's (2019) — neither known when the sweep was written. Update the verdict for the statistical layer and the status line so the page states its current answer. **Do not write a change log** (AGENTS.md): state what is true now.

**D. `itinerary.md` L126.** Carries the same "stopping-time counting functions" error, plus a second: the `3`-adically completed variable is the predecessor tree's **root**, not the "starting value". Repair both. Touch nothing else on that page.

## Constraints

- **Wiki pages only. Not the `.tex`, not the PDF, not `experiments/`, not `reverse.md`.**
- **No `git` commands at all.**
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε` and will silently corrupt every page you touch. This is the single most likely way to ruin this task.
- **Do not renumber any monolith anchor.** `13.2.1`, `13.6.4`, `14.15.1.5` and the rest are stable citation targets that the paper and outside correspondence cite by number.
- **No change logs, no dated journals, no "was X, now Y" prose** in any tracked page (AGENTS.md). A page states the current answer; history is git's job. Front-matter `status:` is a short state word, not a diary.
- Change no numerical value or verification figure.
- Update `updated:` front matter on every page you edit.

## Report back

Site by site: what changed and which findings file supplied it. Flag anything you could not apply as printed, anything you skipped, and any page you found stating a claim about another page that no longer holds.
