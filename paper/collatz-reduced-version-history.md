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

Published 2026-08-03; version-specific DOI 10.5281/zenodo.21730505. After external
review, each definition, statement and scope word is brought back into line with the project record.
Source at `paper/collatz-reduced-v3.tex`.

*(One defect of the published artifact, recorded here because this file is the narrative home:
the PDF's own Version note carries its drafting-time self-description — "drafted; the
version-specific DOI on the title page is reserved and this version is not yet published" —
frozen at upload into the immutable file. The Zenodo record's publication date, 2026-08-03, is
authoritative. Found in the post-publication reconciliation, ours.)*

*(Zenodo metadata, 2026-09-04): the v3 Zenodo record's additional-notes field was updated to
explain the frozen "not yet published" Version-note self-description (the defect itself recorded
above, 2026-08-03); no change to the PDF file, which remains hash-identical to
`paper/collatz-reduced-v3.pdf`.)*

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

## v4 — [month] 2026

<!-- DRAFT section, written with the v4 source (branch paper1-v4-draft). At minting: fill the
month and the version-specific DOI, remove this comment, and check every item against the PDF
actually uploaded. -->

Version-specific DOI [v4 DOI]; concept DOI 10.5281/zenodo.21273547. Source at
`paper/collatz-reduced-v4.tex`. v4 collects into one version every item recorded against v3, from
the record's novelty refresh and register sweep (2026-10-18) and the checklist built on them.

### Attribution of the uniform trim (Section 4)

* Theorem 4.5 keeps its number and statement. Its header now carries the attribution — Rozier
  (*Singularité* 2 (1991), Lemme 4) and Simons–de Weger (*Acta Arith.* 117 (2005), Lemma 7, with
  Lemma 14 and Theorem 3(d) for the explicit bound) — and Brox (2000) is credited with finiteness at
  each period. The text presents the paper's proof as a rederivation by another route.
* The parameter is the same: a `p`-block cycle is an `m`-cycle of Simons–de Weger with `m = p`,
  and Rozier's number of local minima is the same count. The dictionary is stated once, with its
  one-line proof, after Theorem 4.4. Hercher's `m ≤ 91` therefore excludes every cycle with
  `p ≤ 91` blocks; no statement about the number of deep-entry blocks is made.
* The abstract and the Contributions no longer call the trim, or a "dichotomy", new; the phrase
  "our main new theorem" is gone. Related work gains a paragraph on the trim's lineage (Rozier,
  Brox, Simons–de Weger) and on the sharpness's antecedents: Rozier's optimality remark over real
  tuples (p. 11), Simons–de Weger's stated expectation (p. 69), and Halbeisen–Hungerbühler's proof
  in the cycle-length parameter (*Acta Arith.* 78 (1997), p. 238).

### The sharpness (Theorem 4.6), stated and proved

* Theorem 4.6 is **strengthened**, and its proof is printed. In v1–v3 it exhibited instances at
  `p ∈ {6, 7}` and set an `O(log p)` assessment beside them; v3 reported the all-period proof as
  established in the record and not reproduced. v4 states:
  (i) at every period `p ≥ 16` a size-passer with `3.683012 ≤ γ ≤ 5.140212`, the same bracket at
  `3 ≤ p ≤ 15` by finite check, and size-passers at `p ∈ {2, 4}` by exhibition — so a trim
  `γ + log_2 p > c_p n` needs `c_p < (5.140212 + log_2 p)(log_2 3)^{−p}`;
  (ii) at a size threshold `X_0`, every configuration has
  `γ − 1 ≤ log_2(x_min + 1) < γ + log_2 p`;
  (iii) for every `X_0 ≥ 1` and every `p ≥ p_1(X_0)`, a size-passer with every element at least
  `X_0`, `γ − κ_p n ∈ [λ_0, λ_0 + 1.5]` and `Λ > 0.054·2^{−κ_p n}`, realizing the minimax value
  of Rozier's optimality remark under every rotation's exact size condition;
  (iv) the v3 instances.
  The closing sentence ("Uniform cycle exclusion therefore requires the divisibility system …") is
  kept, so the theorem number stays citable, and is attributed to Halbeisen–Hungerbühler's
  conclusion in the cycle-length parameter.
* The threshold form (iii) is new to the paper; it entered the record on 2026-10-19
  (`cycles.md` §12.8.7). What the paper does not say: that the trim is new; that Rozier's Lemme 4
  inequality is attained (the minimax value is); that Simons–de Weger's "at best a constant" is
  settled (the `log_2 p` gap between (ii) and (iii) is open); that the unit-crash staircase works at
  the threshold scale (Remark 4.8, new, shows it does not wherever the stated condition holds);
  anything about exclusion.
* The proof composes the record's availability theorem (§12.8.6.1) with the construction under the
  weaker hypothesis of §12.8.7.2. The *Sharpness evidence and assessment* paragraph and the
  *Status of the assessment* paragraph are removed; a *Verification and record* paragraph names the
  scripts and their counts. The v2 note's route is no longer pointed at from the body; it stays in
  this file and at `cycles.md` §12.8.6.1 and §12.8.6.3.

### Coordinates and provenance

* The provenance sentence is restated as a statement of authorship, not priority. The clause "any
  overlap with contemporary work lies in that layer, not in the coordinate system" is deleted: it
  had been false since 2 July 2026.
* The block cascade is cited as classical (Steiner 1977; Rozier 1990; LaDue 2018). The states
  `(ω, d)` are cited as the skeleton rows `(λ, k)` of J. Williams, arXiv:2607.01718 (2 July 2026),
  one week before v1, with her Proposition 3.3, Theorem 3.6 and Proposition 3.10 matched to
  Proposition 2.2. One sentence says that Section 3 answers her open problem (1) in part — where a
  trajectory leaving a row lands — and not which skeleton it enters.
* Proposition 4.1 is identified as the Böhm–Sontacchi cycle equation (1978) in block coordinates,
  and in integer form as Tao's `n`-Syracuse offset.

### Corrections

* Theorem 3.3's unconditional bound is attributed to Baker theory for `ω ≠ 1` only (Bugeaud–Laurent,
  Corollaire 2). At `ω = 1` the pair `(9, 1)` is multiplicatively dependent; the bound holds there
  exactly, `s = 2 + v_2(d)`, by the isometry. No inequality printed in v3 was false.
* `T` is identified as Tao's `Syr`, and Section 5's "from `T`-time to Syracuse time" (a clash: the
  paper's `T` is the Syracuse map) reads "from one-division-map time to Syracuse time".

### Bibliography

* Added: Rozier 1990 and 1991, Böhm–Sontacchi 1978, Halbeisen–Hungerbühler 1997, Brox 2000,
  LaDue 2018, Williams 2026, Sós 1958 and Świerczkowski 1958 (the three-distance theorem used in the
  proof of Theorem 4.6(iii)).
* Updated: Simons–de Weger and Terras gain DOIs; Steiner gains "and Computing" and *Congr. Numer.*
  20; Hercher gains its corrigendum of 14 June 2026 (a derivation repaired, no statement changed);
  Bařina gains its issue number; Merle is cited at its version-specific DOI with the concept DOI
  beside it.

### Presentation and scope of v4

* The Version note is one paragraph and contains no drafting-time self-description. The title
  page gives the version DOI and the concept DOI.
* The Author's note is unchanged from v3; the sentences the record's findings bear on are the
  author's to reword.
* No statement is renumbered. Theorem 4.6 is strengthened and proved; Theorem 4.5 is attributed,
  unchanged in statement; Remark 4.8 is new and numbered after every existing statement of Section 4. The
  document grows from 15 pages to 20, the growth being the proof of Theorem 4.6.
