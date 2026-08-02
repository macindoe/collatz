# Findings: the round-3 fix wave (v3 round 3, Wave 5b)

**Task:** `briefs/v3r3-fix-brief.md`. **Branch** `v3r3-review-round3`, from `df9e5e6` to `2e79417`.
Worked in the main working directory; no worktree, no push, no merge, no rebase, no branch switch.
Five commits, in the brief's order:

| commit | what |
|---|---|
| `d943d4d` | the tail bound (all four drop-ins) + `experiments/aeh_tailbound.py` + `13.6.4`(⇐) |
| `3dc4974` | D2, D3, D4, D7, D8 |
| `28647e1` | the two biased-protocol numbers |
| `677a76a` | D1, D10, PDF rebuilt |
| `2e79417` | the Appendix A pin, alone |

Everything was edited with the Write/Edit tools. `≤`, `—`, `ε`, `σ`, `π`, `B̂` all decode cleanly in every
edited file; no mojibake byte sequence (`â`, `Ã`, `Â`, `U+FFFD`) anywhere in them.

---

## 1. Disposition, item by item

### The tail bound (`briefs/v3r3-tailbound-findings.md` §4)

| drop-in | status |
|---|---|
| §4.1 `13.6.3`(iv), **required** | **landed**, verbatim |
| §4.2 `13.2`'s relocation clause, **required** | **landed**, verbatim |
| §4.3 `13.2.4`(e), *optional* | **landed**, verbatim |
| §4.4 `13.6.4`(⇒), *optional* (two substitutions) | **landed**, verbatim |

**The optional pair landed, together.** Both target strings matched the current text character for character
(`Choose the letter past-window \`W ≥ D\` with \`2L(0.93)^W < ε'/8\`,` at `13.2.4`(e); `off an exceptional
event of \`B\`-mass \`≤ 2L(0.93)^W\`` and `to within \`2L(0.93)^W + ε\`` at `13.6.4`(⇒)), so the
land-together-or-not-at-all condition never bound. After the edit, `git grep 0.93` over tracked
`*.md`/`*.py`/`*.tex` outside `briefs/`, `sources/`, `archive/` returns **nothing**: the page carries one
constant, `(1/3)(5/6)^(j−1)`, at all four sites.

**The verification script.** `experiments/aeh_tailbound.py` is Appendix A verbatim, plus the repository's
`Run: … (date: …)` docstring line and the header that names the page and results it supports
(`13.6.3`(iii)–(iv), `13.6.5`, `13.2.4`(e), `13.6.4`). **Run before committing: all checks pass, `FAILURES:
none`.** Output against §5's proposed verification line: exact rationals `1/3`, `2/63`, `1598/262143`,
`32767500859970/(2^54−1)` and `P(a=1) = 19/63`, `P(a=0) = 2/3` ✓; float-vs-exact `max |diff| = 7.8e-16` ✓;
both bounds hold at every `j ≤ 11` ✓; `P(a≥j)·3^j ∈ [0.1162, 0.1481]` for `6 ≤ j ≤ 11` ✓; `Q_11 = 7.13e-4`
against `(5/6)^11 = 0.1346` ✓; MC worst `z = 1.62` / `1.48` ✓; orbits `19,760` visits, worst `z = 1.61` ✓;
reconstruction `0/0/0` failures at `W = 2,3,4,6,8` with rates `3.14e-2, 5.72e-3, 1.77e-3, 1.01e-4, 0`
against `3.17e-2, 6.10e-3, 1.82e-3, 1.66e-4, 1.89e-5` ✓.

**Two deviations from §5's proposed line, both recorded here rather than absorbed silently:**

1. **Two decimals in §5 are wrong and were corrected against the run.** §5 prints `P(a ≥ 3) = 1598/262143 =
   0.00609593…` and `P(a ≥ 4) = 32767500859970/(2^54 − 1) = 0.00181897…`. In exact rationals the values are
   `0.006095909485…` and `0.001818961696…`. The landed line prints `0.0060959…` and `0.0018190…`. (§2.3 of
   the verify findings has the first one right; only §5's copy is off.)
2. **The clause "and its induction step in exact rationals to `t = 59` with slack exactly `(1/3)2^{−t}`" was
   dropped.** That result comes from the tail-bound delegate's second scratch script `deriv_audit.py`, whose
   source is not in Appendix A and which therefore does not land. A `**Verified**` line names the script that
   produced everything in it (`AGENTS.md`); leaving the clause in would have named a fact no landed script
   checks. The claim itself is not in doubt — the identity it audits, `(2/3)[(3/2)(5/6)^t(1 − (3/5)^{t−1}) +
   2^{−(t−1)}] = (5/6)^t − (1/3)2^{−t}`, is printed inside `13.6.3`(iv)'s own proof — but it is now carried by
   the proof rather than by the verification record.

### D5 — the `13.6.4`(⇐) parenthetical, completed

Landed. The parenthetical stays (it is true and the proof is worse without it); the cap-to-infinity step is
added after it, mirroring (⇒).

**One correction to verify's suggested bound.** Verify's §4 proposes `freq({min(s_n, D) = D}) →
π_{k,D}({s ≥ D}) = 2^{−(D−1)}`. That cell alone is not enough: letter `n = (σ_n − s_n, s_{n+1})` needs
`σ_n` exactly as well, and `σ_n` can saturate while `s_n` does not (`σ_n ≥ s_n`, so the `s`-cell is contained
in the `σ`-cell, not conversely). The landed clause therefore uses `{σ_n ≥ D} ∪ {s_{n+1} ≥ D}`, of
`π_{k,D}`-mass `(D+1)·2^{−(D−1)}`: under `13.6.3`(v) the letters are iid, so `σ_n = s_n + m_n` is a sum of
two independent geometric(1/2) variables and `P(σ ≥ D) = D·2^{−(D−1)}` (checked at `D = 2, 3`: `1` and
`0.75`, against `1 − P(σ=2) = 0.75`), while `P(s ≥ D) = 2^{−(D−1)}` is the cell `13.3.1` already prints. An
`L`-letter pattern spans `L+1` window states, hence the `L(D+1)·2^{−(D−1)}` in the text. It vanishes as
`D → ∞`, which is what the definition's quantifier over every `D` consumes.

### D1 — the Tao footnote locator. **Landed, both sites.**

* `paper/collatz-reduced-v3.tex` L246: `\cite[Remark~1.13, footnote~4]{tao}` →
  `\cite[Remark~1.13, footnote~4 of arXiv~v7]{tao}`.
* `aeh.md` `13.6.5` **Attribution**: the locator now reads "Remark 1.13's **footnote 4** in arXiv v7", with a
  parenthetical recording that the numbering inside Remark 1.13 is version-dependent, that arXiv v5 (which
  matches the *Forum Math. Pi* publication by date and content) carries a single footnote there and it is the
  Wirsching/Thomas pointer, and that the pointer is therefore fixed by content as much as by number.

**What the fix assumes.** (a) That arXiv v7's Remark 1.13 numbers the negative-time-indexing footnote `4` —
verify extracted the text of v4, v5 and v7 and reports this directly; I did not re-download the sources. (b)
That the *published Cambridge text* was **not** consulted by anyone in this round: verify says so in terms
(§9 item 1). The fix is written so that (b) does not matter — the locator now names a version whose
numbering is on record, and the record page says the numbering is version-dependent, so a reader holding the
journal PDF is told to expect a different number rather than being sent to a footnote that is not there. If
the Cambridge text turns out to carry the ancient-iteration footnote as footnote 4, nothing landed becomes
false; the locator is merely more specific than it needed to be.

The paper's Related-work sentence ("Tao's paper carries a footnote to two further `3`-adic studies") gives no
number and is consistent with the pinned version; it was not touched.

### D2 — `README.md` L40. **Landed.** All three headline corrections:

* "every tested statistic matches the **exact product law**" → "matches the exact capped-window law
  `π_{k,D}`, whose word 'product' names two proved clauses and no others (aeh.md 13.2, 13.6.3(v))".
* "Bulk uniformity stands unqualified at all tested depths." → "unqualified at every tested depth and cell,
  at block lengths `L ≤ 2`, which is as far as the campaign reaches (aeh.md 13.5), and what it pools is the
  across-orbit average rather than the per-start statement itself (aeh.md 13.4)" — both ceilings, each
  pointing at the owning page rather than restating it.
* "a **density-zero set of starting values** over a prescribed finite horizon" → "a vanishing density of
  *starting values* of each size over a prescribed finite horizon, converted to almost every integer only at
  dyadic-shell scale".

### D3 — `bridge.md` §16.4.3. **Landed, both sentences.**

L71's "where uniformity stands unqualified" now carries the `L ≤ 2` ceiling and the pointer to `13.5`; L69's
"density-zero set of starting values over a prescribed finite horizon" now reads "a vanishing density of
starting values of each size … density zero in the integers only at dyadic-shell scale (aeh.md 13.2.5)".
Verify's D3 names both; the brief's D3 line names the first. Both are the same defect and both landed.

### D4 — the proved-claim workflow, steps 2–4. **All three landed.**

* **Step 2, `stage1.md` 11.8.4.5.** The frequency ledger and the `3`-gain rate move out of `heuristic,
  empirically sharp` into a new group, `formal inside the digit budget (aeh.md 13.2.4(d)-(e), 13.2.4.1; every
  horizon rate theta < 1/4 block per bit, for all but a vanishing density of starting values of each size)`,
  with a parenthetical recording that they are marginals of `π_{k,D}`, exact below the cap, and
  AEH-conditional past the budget. `drift log(3/4) per odd step (classical)` stays where it was — it is a
  measurement on `13.4`, not a consequence of the base case.
* **Step 3, `open-problems.md` §11.3.** The entry is kept verbatim and a **Calibration note (2026-08-02,
  aeh.md 13.2.4)** is added after it, per the workflow: what closed (every `θ < 1/4`, at every block length,
  for all but a vanishing density of starts, density zero at shell scale), and what did not (the range past
  the budget, and the derivation along an individual orbit, which no density statement supplies).
* **Step 4, `index.md` L46.** The AEH clause now records the unconditional base case, its range, its
  every-block-length scope, the shell-scale exceptional set, and that the hypothesis is what lies past the
  budget.

`updated:` bumped to `2026-08-02` on `open-problems.md` and `stage1.md` (the other pages were already there;
`README.md` has no front matter).

### D7 — "23 of its 30 tallied blocks". **Landed as `22`, verified two ways.**

*Arithmetic, from the page's own numbers:* the flagship run is `10` burn-in + `30` tallied blocks from
`70`-bit starts, at a measured `4.0017` of exponent per block, so one budget (`70`) is spent at block
`70/4.0017 = 17.49`; the tallied blocks past it are indices `18…39`, which is **22** of 30.
*Direct measurement*, re-running the protocol (`aeh_symbolic.F_step`, seed `31005`, starts `[2^70, 2^71)`,
`d` uniform on `1..12`, burn-in `10`, horizon `30`, no cut): mean total exponent over the 40 blocks
`160.070` (`τ = 2.2867`, so the page's `≈ 2.29` stands), mean exponent per tallied block `4.0018` (the
page's `4.0017` stands), and the mean number of tallied blocks with `S_n ≥ 70` is **`22.003`** under
`13.2.3`'s state-time accounting and **`22.009`** under its letter-time accounting — the one-letter offset
does not move the count. Verify's `22.006` reproduces.

### D8 — the complement slip. **Landed, both sites.**

A Syracuse step **ends** a block exactly when its exponent is `≥ 2`; in the `T_1`-parity word a Syracuse step
of exponent `a` writes `1` followed by `a−1` zeros, so exponent `= 1` writes `11` (the block continues) and
exponent `≥ 2` writes `10` (the block ends). `aeh.md` `13.3.2` and `publication.md` landscape item 4 now name
`10`, with "an odd step whose successor is even" spelled out so the naming cannot invert again. Both
probabilities are `1/2` and both are pair statistics, so no argument moved. Checked that no third site
carries the claim: the paper's own sentence (p. 15) says "a two-letter statistic of the parity word" and
names no pattern.

### D9 — the version note. **No prose changed; the record of it is corrected here.**

`briefs/v3r3-paper-apply-findings.md` §5 item 2 says of the version note: "It is a description, not a change
log: no 'was X, now Y'." **That self-assessment is false.** The note contains at least four such
constructions (`previously carried several`, `previously the theorem's closing clause`, `retiring both …`,
`is replaced by`). **The text is right and the self-assessment was wrong:** a DOI'd paper's version note is
precisely the genre in which "was X, now Y" belongs, and `AGENTS.md`'s no-change-log rule governs wiki pages.
Nothing was edited on this account.

### D10 — the paper's two unqualified calibration numbers. **Landed.**

Section 5's Calibration paragraph now opens "(per-orbit statistics over each cell's own conditional counts,
$1{,}600$–$2{,}600$ independent orbits per cell, under an altitude cut on the core)" and identifies the
bottom regime, where `z = 41` is read, as "that cut's own complement". The paragraph after Lemma 5.2 gains a
third recorded qualifier: the guard cuts on the core rather than the door, censors `s`, `m_+` and `a_+` at
once, binds at finite size (`2.6 %` of visits in the adjudicating run) and moves the reported statistics at
the third decimal — with the pointer to `aeh.md` §13.4 — closing with the fact that Hypothesis 5.1 itself
carries no cut and tallies within the exponent budget. Every number in the addition is one the record already
carries and verify independently reproduced (§2.4).

### D6 — the pin. **Landed as the separate final commit** (§4 below).

### D11, D12 — informational, no action. The layout is clean (rebuild report in §3); the round adds five
anchors and renumbers none, and this wave adds none.

---

## 2. The cut-free re-run

**What I ran.** A scratchpad driver importing `experiments/aeh_symbolic.py` **unmodified** (the repository
script was not edited; the import runs no `__main__` block), calling `check_b_side_laws`,
`check_depth_comparison`, then `check_orbit_texture(seed=31005)` twice — once at `CUT = 1 << 30` as printed,
once at `CUT = 0`.

**What I got.** Both columns reproduce verify's §2.5 exactly:

| | core cut, as printed | cut-free |
|---|---|---|
| tallied visits | `154,389` | `158,580` |
| `P(d=2)` | `0.31919` | `0.31854` |
| `L1` over `d ≤ 5` vs the exact law | `0.00517` | `0.00241` |
| `L1` vs the chain law | `0.03117` | `0.02763` |
| chain offset at `P(d=2)` | `0.01760` | `0.01695` |
| `P(ω_+ ≡ 1 mod 3 \| a_+ = 0)` | `0.6662` (`0.3σ` from `2/3`, `112.0σ` from `1/2`) | `0.6651` (`1.1σ`, `113.4σ`) |

(One number of verify's that does not reproduce as stated: verify estimated the cut-free deviation from `1/2`
at "`~110σ`"; the run reports `113.4σ`. Nothing on any page quotes it, and both verdicts are unmoved.)

**What I changed.** Exactly the two entries the brief names, in `13.6.5`'s adjudication clause:

* the visit count now reads "`154,389` tallied visits of the run's `158,580`";
* `P(d=2)` now reads "`0.3192`, and `0.3185` on the same seed with the cut removed, against `20/63 =
  0.31746` — the cut bias reaches the fourth decimal at this cell, which is why both are printed".

**What I did not change, and why.** The clause names its protocol (core cut, which binds, `13.4`) and the
remaining figures are true *of that protocol*: `L1 ≤ 0.006` (cut `0.0052`, and cut-free `0.0024`, so the
printed bound holds either way), `off by 0.018, ≈ 14 pooled standard errors` (cut `0.0176` at `15.1` SE;
cut-free `0.0170` at `14.5` SE — the `≈ 14` is if anything better cut-free), and `0.6662 ± 0.0015` with its
two verdicts. Rewriting the whole clause under the cut-free protocol would have moved `0.018 → 0.017`,
`0.6662 → 0.6651` and `112σ → 113σ` as well — four or five measured values rather than two, on a run the
`aeh_symbolic.py` docstring deliberately freezes because `13.6.5`'s recorded values were produced by it.
Verify's own recommendation for these two entries was "neither needs a re-run, only a footnote"; reporting
both protocols where the bias reaches the printed precision is that footnote, in the form `13.4` already uses
for the mean-`s` triple. **No other measured value on any page changed in this wave.**

---

## 3. Build report

Three `pdflatex -halt-on-error -interaction=nonstopmode` passes per build, MiKTeX-pdfTeX.

**Build 1 (the D1/D10 commit, `677a76a`):** exit `0 / 0 / 0`. **17 pages, 432,819 bytes.** `0` overfull
boxes; `1` underfull (`badness 1067`, tex lines `470--471` — the pre-existing `rhin` bibliography entry,
exactly the one verify reports); `0` `LaTeX Warning` lines; `0` undefined references or citations.

**Build 2 (the pin commit, `2e79417`):** exit `0 / 0 / 0`. **17 pages, 432,863 bytes.** Same box profile:
`0` overfull, the same single underfull at `470--471`, `0` warnings, `0` undefined references.

**Page count: unchanged at 17** (committed PDF before this wave: 17 pages, 432,124 bytes). No content was
cut. The only layout movement is that §6 *Discussion* now opens at the top of p. 16 rather than at the foot
of p. 15, which removes the two-lines-under-the-heading tightness verify flagged as cosmetic on p. 15.
Rendered p. 12, p. 15 and p. 16 and read them: the locator sets as "[4, Remark 1.13, footnote 4 of arXiv
v7]", the calibration paragraph and its new qualifier set cleanly across the p. 15/16 break, Appendix A and
the References are clean, and the pin renders as `677a76a`.

---

## 4. The pin commit, and the verification of its claim

`2e79417`, alone: `paper/collatz-reduced-v3.tex` (one token) and the rebuilt `paper/collatz-reduced-v3.pdf`.
Appendix A now reads "every wiki section and script named in this paper is cited at commit `677a76a`."

**Is the claim true at `677a76a`?** Checked mechanically against that tree (`git show 677a76a:<page>`,
`git ls-tree -r 677a76a`), for every wiki section and every script the `.tex` names:

* `aeh.md` — `13.1`, `13.2.4`, `13.2.5`, `13.3`, `13.3.2`, `13.4`, `13.5`, `13.6.3`, `13.6.4`, `13.6.5`:
  all present.
* `cycles.md` — `12.2.3`, `12.5.2`, `12.5.3`, `12.6.1`, `12.6.2`, `12.7.4`, `12.7.5`, `12.8.6`: all present.
* `stage3.md` `11.8.6.3`, `itinerary.md` `14.15.1.5`: present.
* Scripts named in the `.tex`: `experiments/absorption_law.py`, `anchor_increment.py`,
  `one_step_propagation.py`, `period1_cycles.py`, `period2_cycles.py`, `period3_cycles.py`: all present.
  (`aeh_tailbound.py`, `aeh_basecase.py`, `aeh_symbolic.py`, `aeh_calibration.py`, `aeh_anomaly.py` and
  `merle_aeh_key_check.py` are present too; the paper names them only through the wiki.)

**And it is honest in the sense the repository has always meant.** `677a76a` is this round's last content
commit: its `aeh.md` is the round-3 record, its `paper/collatz-reduced-v3.tex` is this paper, and its
`experiments/` contains the script `13.6.3`'s verification line names. The single residue is the one both
precedents (`643e864`, `3511a0d`) accepted and cannot be removed by any one commit: at `677a76a` Appendix A
still prints the *previous* pin, because the token can only be updated by a later commit than the one it
names.

**The risk verify names is unchanged and is the author's to weigh:** `677a76a` is a branch commit. If
`v3r3-review-round3` is squashed or rebased at merge, the pin dangles and must be re-pointed at the merge
commit, exactly as `3511a0d` re-pointed the last one.

---

## 5. Found and not fixed

Reported, per the brief's rule against unscoped edits.

1. **`anchor-digit-search.md` L139 still writes `aeh.md`'s law as `π_k`.** The round renamed the object
   `π_k → π_{k,D}` everywhere else; a `git grep` for `π_k` outside `π_{k,D}` over tracked pages returns this
   one site ("the routine check that Haar, read in the block/anchor coordinates, equals aeh.md's `π_k`").
   The sentence's content is unaffected — it is about the Haar/product identification, which is `13.6.3`(v) —
   but the symbol is the retired one, on a page `a1e1701` did edit. One token.
2. **`stage1.md` 11.8.4.4's first status remark still opens "First, it is a heuristic".** The workflow step
   the brief named is 11.8.4.5's compact ledger, which is done; 11.8.4.4's prose discussion of the same
   ledger now sits one step behind it. It is not wrong as written (it is a heuristic past the budget, which
   is where that passage's `10^18`-start measurements live), but a reader comparing the two subsections finds
   the snapshot stronger than the discussion it summarises.
3. **`13.6.5`'s "`≈ 14` pooled standard errors" understates under the printed protocol.** Verify's §2.5 notes
   it (`15.1` under the cut) and I reproduce it; cut-free it is `14.5`. Left alone: it is inside "`≈`", it is
   not on the fix list, and it is the one figure that is *more* accurate under the cut-free reading the same
   sentence now also quotes.
4. **The `13.6.4`(⇒) and `13.2.4`(e) index nits** (tail-bound findings §1(4), U5) remain unlanded, as that
   findings file recommends: `13.2.4`(e)'s `P` over-counts by one in the safe direction, and `13.6.4`(⇒)'s
   window supplies past depth `W−1` where `W` is universally quantified. Both are no-ops for the conclusions.
5. **U1–U4 of the tail-bound findings and items 1–11 of verify §9 are untouched** — in particular the true
   decay rate (`≈ 3^{−j}` measured, `5/6` proved), `13.2.4`(e)'s `ε'`/`Λ`/union-bound bookkeeping, and the
   composite five-coordinate reconstruction. None is a fix-wave item.
6. **`briefs/v3r3-fix-brief.md`, `briefs/v3r3-tailbound-findings.md` and this file are left untracked.** The
   round has committed each wave's brief-and-findings as its own `briefs:` commit, and committing them here
   would have put a tracked-file commit after the pin, which the brief requires to be the final one.
