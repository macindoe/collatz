# Version history: *Reduced coordinates for the Collatz map*

**What this is.** The per-version record of the paper whose sources are in this directory: what each
released version says, and what changed between them, item by item. Each version's Zenodo release
description carries the same text.

**Why it is a file and not the commit log.** Released versions are frozen at their DOIs. A reader
holding one PDF cannot recover from it what an earlier or a later version claims, and the commit
stream is organised by commit, not by version. This is therefore the one place in the repository
where a change history is kept by hand (`AGENTS.md`, Layers): a wiki page states the current answer
and leaves its history to git, because any past state of it can be read back at a commit; a published
PDF in someone else's hands cannot be.

**What it is not.** It records what the *paper* says at each version. Where a claim's standing has
moved past what a version printed, the project record is the authority — `cycles.md` §12.8.6 for the
staircase, `aeh.md` §13 for the hypothesis and its calibration — and the pointers below name it.

---

## v1 — July 2026

Original publication. DOI 10.5281/zenodo.21273548. Source frozen at
`sources/paper/collatz-reduced-v1.tex`.

## v2 — July 2026

Version-specific DOI 10.5281/zenodo.21421120. Source at `paper/collatz-reduced-v2.tex`.

* The subtitle of the `merle` citation restored — *…a conditional formal proof in Lean 4, with
  documented structural obstructions* — which v1 printed without its second clause.
* A *Note added in v2* added to Section 4, evidencing the sharpness hedge of Theorem 4.6 (the
  staircase) and prompted by correspondence with Eric Merle. It reported a single
  period-parametrized construction procedure — semiconvergents of `log_2 3` select the exponent `n`,
  a rounded geometric profile builds the climb, a bounded correction closes the last bits, applied
  separately at each period — verified by exact big-integer arithmetic to produce a passing
  size-condition witness (`q <= R_r` at every rotation) at every period `p ∈ {2,...,23}`, with
  `γ / log_2 p ∈ [1.828, 3.643]`: a contiguous range, extending the two isolated instances the
  theorem exhibits.
* The note recorded that the recipe's own candidate chain initially left `p = 22` unresolved.
  Correspondence with Eric Merle identified the cause as a gap in that chain's coverage at the
  required scale rather than a failure of the correction step, and at two candidates outside the
  chain — `n = 25217` and `n = 31202` — the same profile-and-correction procedure resolves it, in
  `13` and `8` correction moves, closing the range.
* The note named its remaining gap: no proved closed-form bound on the multiplicative gap between
  consecutive correctly-signed semiconvergent runs — the bound that would certify no period is
  skipped.
* No theorem or universal claim strengthened, and Theorem 4.6's hedge sentence unchanged. v2 adds a
  finite computational evidence record.
* Record of the v2 note: `cycles.md` §12.8.6 at commit `72ec88e`.

The gap sentence of that note is the one published sentence v3 supersedes; see the staircase items
below. The route it names is kept in the current record, at `cycles.md` §12.8.6.1 (*Superseded
formulation*) and §12.8.6.3, precisely because the published note names it.

## v3 — August 2026

Drafted and not yet published; version-specific DOI 10.5281/zenodo.21730505 reserved. After external
review, each definition, statement and scope word is brought back into line with the project record.
Source at `paper/collatz-reduced-v3.tex`.

### The staircase (Section 4)

* The gap the v2 note named is closed, and closed by replacing the route rather than by completing
  it. Candidate availability needs no continued-fraction input at all:
  `8 − 5·log_2 3 = 0.0751874964...` is positive and shorter than the target arc, so any `66`
  consecutive integers contain an `n` whose `⌈n·log_2 3⌉ − n·log_2 3` lies in
  `[0.0415, 0.1169390665...]`, and the scale window at period `p` holds `0.05·(log_2 3)^p`
  integers — `79` at `p = 16` — so `p = 16` is the first period supplying `66` consecutive integers.
* The bound the v2 note asked for is not needed and, as posed, is a dead end: those multiplicative
  gaps are the partial quotients of `log_2 3`, so a uniform bound on them is exactly the assertion
  that `log_2 3` is badly approximable.
* The `p = 22` episode was a property of the candidate list used, not of `log_2 3`: under the
  availability statement it does not arise — from `p = 8` upward not one working witness is a
  convergent or semiconvergent denominator.
* The construction half is closed independently. A corrected profile — the geometric climb with a
  fixed additive offset `1/(log_2 3 − 1) = 1.70951` per block, absent from the v2 profile —
  satisfies all `p` size conditions by construction, with no correction step. The bounded correction
  is removed from the argument rather than bounded.
* The two halves compose to a proof for every period `p >= 16`, at `γ` between the absolute
  constants `3.683012` and `5.140212` — no `p`-dependence at all — with `3 <= p <= 15` meeting the
  same bracket by finite check, and `p ∈ {2, 4}`, which lie outside the construction's reach,
  covered by direct exhibition. Two independent evaluators reproduce the composition end to end over
  the periods from `3` to `26` (apart from `p = 4`), and the construction itself is verified through
  `p = 32`.
* The proof is established in the project record and is **not** reproduced in the paper. Theorem 4.6
  claims exactly what it claimed in v1 and v2: it is neither strengthened nor weakened, and its
  statement is not restated. Every constructed configuration remains a size-passer only and fails
  the divisibility conditions `q | R_r` — sharper evidence that counting cannot do better, and no
  evidence about exclusion.
* Current record: `cycles.md` §12.8.6 at commit `9d9d1ec`.

### Definitions and statements brought back into line with the record

* Definition 2.1 requires `ω` positive, without which the state `(−1, 1)` leaves `F` undefined:
  there `A = 3ω − 1 = −4`, `s = v_2(A) = 2`, `C = A + 2^s = 0`, and `σ = v_2(C)` does not exist.
* Theorem 3.3's unconditional bound reads `C(ω)(1 + log d)^2`. The printed `(log d)^2` was imported
  from a record statement carrying a `d >= 2` guard which the paper had dropped, and is false at
  `d = 1`.
* Theorem 3.8 states its depth-`k` window as the residues of Theorem 3.7 **together with** the
  stratum labels `(s, σ, a_+)`, matching its own proof. Theorem 3.7 is unchanged.
* Theorem 4.5's `n_0(p)` is defined — as the solution of the displayed equation — rather than named
  only inside the order estimate `O(p·(log_2 3)^p)`.
* The digit budget is labelled a heuristic, as its own text always said; no part of it is claimed as
  proved. It carried a proposition environment in v1 and v2.
* Proposition 4.1 defines `σ_j` at its point of use (`σ_j = s_j + m_{j+1}`, as in Definition 2.1),
  and distinguishes `M_t`, a partial sum of entry depths, from the anchor `M(ω)` of Section 3.

### Section 5 — one object, one clock, one hypothesis

* The section carries one object where it previously carried several. The observable is the capped
  window `W_{k,D}`, at a depth `k` and a cap `D` quantified together, the cap bounding the stratum
  labels as well as the depth.
* The comparison law `π_{k,D}` is the law of that window under the two-sided Bernoulli measure, its
  depth component the exact convolution rather than the window chain's stationary law. "Product"
  names its two proved clauses and no others — in particular the window process is stationary but
  not independent across time.
* Hypothesis 5.1 is stated in ensemble form — uniformly sampled starts, a horizon linked to the
  sampling scale, every block counted once, a single limit — in letter coordinates and at every
  finite block length. This retires both the single-orbit reading, which is empty on a convergent
  orbit, and the single-visit reading, which is strictly weaker. The distance is total variation on
  the finite window alphabet, named where it is used.
* The bulk cut is replaced by an exponent budget whose admissibility is defined and whose protection
  is a deterministic identity rather than an assumption.
* The section states **no** descent or contraction consequence of Hypothesis 5.1: that conclusion is
  a theorem without the hypothesis, and a stronger one, so the section is framed onto what the
  hypothesis alone supplies, which is distributional.
* The unconditional base case is given with the exact rate at which it holds and the exact horizon
  at which that rate vanishes. It is about the **extended** `(n+1)`-letter word — the start's own
  letter followed by the `n` sampled letters — and not about a word beginning at the sampled start;
  the displayed bound is a marginal of that word's law.
* The density conclusion is stated at dyadic-shell scale, where it is exact; the union over all
  sampling scales is a triangular array that no per-scale statement controls.
* Section 5 does not claim that Hypothesis 5.1 supplies `E_B[m + r] = 4`, or the empirical exponent
  mean, past the digit budget; and the reading of any step-time horizon in reduced blocks is a
  theorem of the cylinder count inside the digit budget and, past it, neither a theorem nor a
  consequence of the hypothesis.

### Attributions and citations

* The stationary `3`-adic law governing the absorption is Tao's Syracuse random variable (*Forum
  Math. Pi* 10 (2022) e12, Lemma 1.12 and Remark 1.13), in the present normalisation; the block
  coordinate's `3`-adic past-limit has the law of `Syrac(Z_3)/2`.
* Its negative-time reading is Tao's own alternative to his positive-time indexing, at Remark 1.13,
  footnote 4 of arXiv v7.
* The unconditional density line the hypothesis does not add to — Terras, Everett, Korec,
  Inselmann, Tao — is cited in Related work, with the horizons given in the step units in which they
  are proved.
* The two further `3`-adic studies a reader of Tao's footnote will reach (Wirsching, Thomas) are
  cited and distinguished from the object appearing here.
* The bibliography was audited against the external sources: `llmcollatz` gains its author,
  and `terras`, `steiner`, `hercher` and `barina` each gain a locator verified in the audit. None of
  those four entries was wrong as printed.

### Calibration

* The record is reported with the limits it does not reach past: block length `L <= 2`, pooled
  adjudicating estimates, and an altitude guard on the core that binds at finite size — removing
  `2.6%` of visits in the adjudicating run and moving the reported statistics at the third decimal.

### Presentation

* The sharpness assessment, in v1 and v2 the closing clause of Theorem 4.6, is set out beside the
  theorem under *Sharpness evidence and assessment*, so the theorem environment carries only what
  the paper proves.
* The *Note added in v2* and the correction paragraph that followed it are replaced by a single
  *Status of the assessment* paragraph, which states what was proved, where, and at what scope. The
  narrative of how the route changed is what this file carries.
* The document is shortened from 18 pages to 15: the version note reduced to a paragraph, the
  abstract and the introduction's roadmap compressed, Remark 3.6's verification counts pointed at
  `stage3.md` §11.8.6.3, and Section 5's derivations and its repeated qualifications pointed at
  `aeh.md` §13. No numbered statement is removed and no qualification is dropped; every passage cut
  is one the record carries.

### Scope of v3

* No numbered theorem's claim is strengthened, weakened, or renumbered, and nothing new is proved in
  the paper. v3 reports two results established in the project record and not reproduced there: the
  sharpness construction of Section 4 and the base-case assembly of Section 5.
* Verification pointers and script names are concrete throughout. The complete record is public at
  <https://github.com/macindoe/collatz>; Appendix A pins the commit at which every wiki section and
  script named in the paper is cited.
