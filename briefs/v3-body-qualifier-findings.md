# Findings: the finite-window qualifier in the body, and the stage3 date

**Branch:** `v3-body-qualifier`.
**Base SHA cut from:** `cb0389f373392f86131ed4331bd6627b7dc8c902` — verified with `git rev-parse HEAD` against `main` before starting; working tree clean.
**Pushed:** nothing. **Merged:** nothing. Handed back checked out.

**Tracked files edited:** `paper/collatz-reduced-v3.tex`, the rebuilt `paper/collatz-reduced-v3.pdf`, `stage3.md` (one front-matter field), and this file — plus a one-line pointer into the previous round's findings, noted at the end.

**Why a new findings file rather than an append.** The repo's convention is one findings file per branch (`merle-la9-check-findings.md`, `staircase-allp-construction-findings.md`, …), and `briefs/v3-external-review-corrections-findings.md` is the record of a branch that is now **merged** — its contents are an accurate account of that round and rewriting them from a later branch would blur what was decided when. This round is a distinct branch with a distinct base, so it gets its own file. The one exception is a single pointer added to that file's stale open item, described at the end.

---

## Item 1 — the qualifier moved into the body. **Done.**

The author's reasoning ("relying on the abstract for key detail is unwise") reverses last round's ruling, which I had recorded as known-open at `briefs/v3-external-review-corrections-findings.md` §R2-3 and in its "Remaining drift" list, item 1.

### Site A — Contributions item (iv), the first encounter in the body (line 54)

**Before:**

```text
(iv) An exact low-order law for the anchor increment and an error-free
finite-window trichotomy for the next step, with a digit-budget accounting
(Theorems~\ref{thm:deltaM}--\ref{thm:onestep}, Heuristic~\ref{prop:budget}).
```

**After:**

```text
(iv) An exact low-order law for the anchor increment and an error-free
trichotomy deciding the next step from a finite residue window together with
the step's stratum labels, with a digit-budget accounting
(Theorems~\ref{thm:deltaM}--\ref{thm:onestep}, Heuristic~\ref{prop:budget}).
```

**As rendered:** "(iv) An exact low-order law for the anchor increment and an error-free trichotomy deciding the next step from a finite residue window together with the step's stratum labels, with a digit-budget accounting (Theorems 3.7–3.8, Heuristic 3.9)."

### Site B — the prose recap, one sentence later (line 56)

**Before:**

```text
A finite window of state digits then decides the next step in a trichotomy
that never errs, and an elementary accounting argument shows each decision
\emph{consumes} digits irreversibly, ...
```

**After:**

```text
A finite window of state digits and stratum labels then decides the next step
in a trichotomy that never errs, and an elementary accounting argument shows
each decision \emph{consumes} digits irreversibly, ...
```

**As rendered:** "A finite window of state digits and stratum labels then decides the next step in a trichotomy that never errs, …"

Three words added. Site A now carries the qualification properly, so Site B needs only to stop reading as a flat unqualified claim in its own right, which naming the second input does. No commas were added at Site B: the lighter noun-phrase form keeps the sentence's rhythm and avoids a second parenthetical in a paragraph that already runs long.

### Judgement made: words, not symbols

Both sites say **"stratum labels"** rather than **`(s, σ, a_+)`**, matching the abstract's register as instructed. This is also the only correct choice for §1 independently of the instruction: `σ` and `a_+` are first defined in **Definition 2.1** (`def:reduced`), so naming the triple in the introduction would forward-reference two undefined symbols. Item (iv)'s own parenthetical already points at Theorem 3.8, where the window is stated with the labels named in full. `s` is the one label that §1 does introduce (item (ii)), and nothing turns on singling it out.

### Scope held

`git diff --stat` on the `.tex` for this item: **2 insertions, 2 deletions**, both single-line, both inside §1's existing paragraphs. §1 is not restructured; nothing else in it — the opening framing, the related-work paragraph, items (i)–(iii) and (v)–(vi) — is touched.

### Version note: **not changed**, and why

Concluded that it needs no word, agreeing with the coordinator's read, on two grounds.

1. **It already carries the substance, at the grade the register uses.** Its v3 entry states: "Theorem~\ref{thm:onestep} states its depth-$k$ window as the residues of Theorem~\ref{thm:deltaM} *together with* the stratum labels $(s,\sigma,a_+)$, matching its own proof, with Theorem~\ref{thm:deltaM} unchanged". The §1 edits do not add a substantive change; they propagate that one into the prose that summarises it.
2. **The note does not enumerate echo sites, and never did.** It does not mention the abstract clause either, though that was the same correction reaching the same kind of prose. Adding "and §1 was updated to match" would make it a change log of edit locations — the register `AGENTS.md` forbids in tracked files, and which the note has so far avoided.

Had the note been silent on `thm:onestep` the conclusion would be the opposite; it is not.

---

## Item 2 — `stage3.md` front-matter date. **Done.**

`updated: 2026-07-23` → `updated: 2026-08-01`. It records the verification line added to §11.8.6.2 in the previous round, which is why the field was stale — the front matter was out of bounds then and I flagged it rather than bumping it.

**That one field only.** `git diff -U1 stage3.md` shows a single line changed:

```text
 scope: monolith 11.8.6
-updated: 2026-07-23
+updated: 2026-08-01
 source: sources/drafts/collatz_reduction_rewrite_v078.md (last monolith)
```

`status:`, `scope:` and `source:` are byte-identical, and nothing in the body moves. Note that `status:` correctly needed no change: this was a verification record, not a status change, and §11.8.6.2's status ("closed at the valuation level, per reduced step, all residue classes") is unaffected by re-verifying it.

---

## Gates

- **Build:** rebuilt from a clean sandbox directory. `pdflatex -interaction=nonstopmode -halt-on-error` exits **0 on two consecutive runs**; **0 overfull boxes**, 0 undefined or multiply-defined references. Title/author metadata still populated, DOI target `https://doi.org/10.5281/zenodo.21730505` unchanged, **12 pages — unchanged**, both edits absorbed within existing lines. PDF built in the sandbox and copied back as the artifact only.
- **Encoding scan:** `python experiments/encoding_scan.py` → `RESULT: CLEAN` (0 non-UTF-8, 0 BOMs, 0 double-encoding signatures). Both edits made with the file-editing tools; no `Get-Content`/`Set-Content` touched a tracked file.
- **Rendered text checked**, not just the source: both sentences were read back out of the built PDF with `pdftotext` and are quoted above as rendered.

---

## Pointer added to the previous round's findings

`briefs/v3-external-review-corrections-findings.md` closed with a "Remaining drift noticed, out of scope to fix" list whose **item 1** is precisely what this branch fixed. Left as written it would read as an open item forever. `AGENTS.md`'s own diagnosis of what the wiki is for — *"the staleness that motivated this wiki came from duplicated status claims"* — argues for a pointer rather than silence, so that item now carries a one-line note that it is closed here.

Nothing else in that file was altered: §R2-3 records a decision that was correct for its round, and remains a true account of it.

## What remains open

Nothing from this round. The items still standing from the previous one, unchanged and recorded there:

1. **The `llmcollatz` bibliography entry** (arXiv:2603.11066) has no authors in our record; none were invented. Author-side lookup.
2. **The three Yu volume/page numbers** were supplied from outside this repository and should be confirmed before publication.
3. **`thm:onestep`'s undecided rate** is attributed to "the product law of Section 5", but `stage4.md`'s derivation of `≈ 2^{-(k+1)}` runs under a *uniformity* heuristic, which item 1 of the previous round established is not `π_k`'s depth marginal. The measured rates are unaffected and the figure is stated as an approximation, so nothing is false — but the provenance is wrong, and it is a wiki-side question as much as a paper-side one.
4. **`hyp:aeh` and `aeh.md` `13.2.1`/`13.6.4`** share a residual imprecision about the inner limit on a convergent orbit. The paper now says this out loud; the two wiki statements do not.
