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

## v4 — October 2026

Version-specific DOI 10.5281/zenodo.23501162 (minted 2026-10-21); concept DOI
10.5281/zenodo.21273547. Source and PDF at `paper/collatz-reduced-v4.tex` and `.pdf`, released at
commit `9a29035`; the record commit cited inside the paper (Appendices A and D) is `110f8b6`. 46
pages. v4 collects every item recorded against v3 — the attribution of the trim, the sharpness
proved, the provenance and the corrections — and is rewritten for a reader without training in
mathematics. Statement numbers below are v4's; Appendix H of the paper maps v3's to them.

### Rewritten for a non-specialist reader; statements renumbered

* The main text (Sections 1–8, pp. 4–12) tells the paper in words, with only short formulas, each
  explained. The abstract is in plain language; the technical abstract opens the appendices as a
  *Technical summary*. A *Symbols at a glance* page precedes Section 1, and Appendix I indexes every
  symbol of the paper.
* The orbit of `7` runs through Sections 2–4 and returns in Section 6. Section 2 gives it as a
  table — `x` and `x + 1` in binary, `x + 1` factored with every exponent written, a ruled cascade
  row for the even number `26` (half of `3·17 + 1`, with `26 + 1 = 2^0·3^3·1`), and the trailing
  1s of `x` and trailing 0s of `x + 1` in bold.
* Sections 4, 5 and 6 are one page each — what is claimed, why it matters, one worked example, where
  the full account lives — and each of Appendices C, D and E opens with *A guided account* in plain
  words before its formal statements. Section 4 introduces the exit valuation through
  `3^d·ω − 1`, of which `s` counts the trailing zeros, and lists the eight kinds in three groups: one
  extra halving, two, and the two lifting kinds, where the anchor enters.
* Every formal statement moves, in v3's order, into Appendices B–E, so a v3 number becomes a v4 number
  by changing the leading section number to a letter (Theorem 4.6 is Theorem D.6). Related work in
  detail is Appendix F, a verification index Appendix G, the concordance Appendix H. Symbols that
  carried two meanings in v3 are renamed (Appendix H lists them; no meaning changed). For outside
  citations of this paper's statements by number, v3 remains the pinned citation.
* Section 7 closes with a pointer to the mirror paper (DOI 10.5281/zenodo.21303918) as the place to
  start for work from the backward direction.

### Attribution of the uniform trim

* Theorem D.5 (v3's 4.5) keeps its statement and names Rozier and Simons–de Weger in its header.
  The paragraph after it gives the locators: the first display is Rozier's Lemme 4 (*Singularité* 2
  (1991), p. 11) and Simons–de Weger's Lemma 7 (*Acta Arith.* 117 (2005), p. 58), up to an additive
  constant; the second, with Rhin's bound, is their Lemma 14 and Theorem 3(d). Finiteness at each period is credited to
  Rozier's Théorème (1991, p. 8) and also to Brox (2000). The paper's proof — rotation numerators
  and a max-plus recursion — is presented as a rederivation by another route, chosen because it
  identifies the extremal profile the staircase realizes.
* The dictionary with `m`-cycles is stated once, after Theorem D.4, with its proof: a `p`-block
  cycle is an `m`-cycle of Simons–de Weger with `m = p`, and Rozier's number of local minima is the
  same count. Hercher's theorem therefore excludes every nontrivial cycle with `p ≤ 91` blocks; such
  exclusions say nothing about how many blocks are deep.
* The abstract, the introduction and the Author's note no longer call the trim new or a main
  contribution of the paper (v3's "main new theorem" is gone; the Author's note's contributions
  sentence is in the author's own wording). Appendix F gives the trim's lineage and the sharpness's
  antecedents: Rozier's optimality remark over real tuples (p. 11), Simons–de Weger's stated
  expectation (p. 69), and Halbeisen–Hungerbühler's proof in the cycle-length parameter (*Acta
  Arith.* 78 (1997), p. 238).

### The sharpness (Theorem D.6), stated and proved

* v1–v3 exhibited instances at `p ∈ {6, 7}` and set an `O(log p)` assessment beside them; v3
  reported the all-period proof as established in the record and not reproduced. In v4 the theorem
  is strengthened and its proof is printed. It states:
  (i) for every `p ≥ 16`, an `n ∈ [(log_2 3)^p, 1.05·(log_2 3)^p]` and a size-passer with
  `K = ⌈n·log_2 3⌉` and `3.683012 ≤ γ ≤ 5.140212`; the same bracket at `3 ≤ p ≤ 15` by finite
  check; size-passers at `p ∈ {2, 4}` by exhibition; hence a trim `γ + log_2 p > c_p·n` at
  `p ≥ 16` needs `c_p < (5.140212 + log_2 p)(log_2 3)^{−p}`;
  (ii) every configuration has `γ − 1 ≤ log_2(x_min + 1) < γ + log_2 p`, so a size-passer whose
  elements are all at least `X_0` has `γ > max(κ_p·n, log_2(X_0 + 1)) − log_2 p`;
  (iii) for every real `X_0 ≥ 1` and every `p ≥ p_1(X_0)`, a size-passer with every element at
  least `X_0`, `λ_0 ≤ γ − κ_p·n ≤ λ_0 + 1.5` (`λ_0 = 2.7095122...`), Rozier's quantity between
  `κ_p·n` and `γ`, and `Λ > 0.054·2^{−κ_p n}`;
  (iv) v3's instances, the `84` at `p = 6` now described as from a seeded random search, each
  clearing the period-3 constant by at least `0.698`.
* The proof of (i) is the availability argument (`8 − 5·log_2 3`; any `66` consecutive integers
  contain a good `n`) composed with the construction under the weaker hypothesis of `cycles.md`
  §12.8.7.2; that of (iii) uses the convergents of `log_2 3` and the three-distance theorem
  (Sós; Świerczkowski). `p_1(X_0)` is given at sample values — `10` for `X_0 ≤ 16`, `98` at
  Simons–de Weger's `5·2^60`, `110` at `2^71`, `309` at `2^200` — with
  `p_1 − log_{log_2 3} X_0 ∈ [2.783, 10.630]` over `X_0 = 2^j`, `j ≤ 200`. No formula uniform in
  `X_0` is claimed, and nothing below `p_1(X_0)`.
* At the threshold scale the staircases realize the minimax value of Rozier's optimality remark
  under every rotation's exact size condition — that value, not the inequality of his Lemme 4 — and
  show that the prefactor in Simons–de Weger's Lemma 7 cannot be lowered below `0.054`. Whether it
  can be lowered to a constant (the `log_2 p` between (ii) and (iii)) is left open. The closing
  sentence — uniform exclusion needs the divisibility conditions — is kept and attributed to
  Halbeisen–Hungerbühler's conclusion in the cycle-length parameter.
* Remark D.8 (the crash block) is new: at the scale of (iii) a unit-depth block is excluded wherever
  a stated inequality holds, which it does at `p_1(X_0)` and `p_1(X_0) + 20` for `2^20 ≤ X_0 ≤ 2^200`.
* The *Sharpness evidence and assessment* and *Status of the assessment* paragraphs are replaced by
  *Verification and record*, which names the scripts and their counts and says that the
  configurations of (iii) were not tested for divisibility. Statements on the staircases concern the
  reach of size arguments only. Current record: `cycles.md` §12.8.6 and §12.8.7.

### Coordinates and provenance

* The provenance passage is restated from the author's dated evidence. v3 dated "the reduced
  coordinate system itself" to the hand-drawn note of 13 March 2023. v4 dates only the mechanism to
  that note — each rising step trades a factor of 2 for a factor of 3, which is classical (Steiner
  1977; Rozier 1990; LaDue 2018). The factorization `x + 1 = 2^m 3^a ω` was worked out by the author
  by hand in December 2025, and named and formalized as the state `(ω, d)` in AI-assisted work.
  v3's clause that any overlap with contemporary work lies in the superstructure, "not in the
  coordinate system", is deleted.
* The title-page footnote and Appendix A name both AI phases, where v1–v3 named Claude only: ChatGPT
  (OpenAI) from December 2025 to March 2026 — exploratory definitions and the early CollatzScout
  drafts, alongside the author's hand computations in spreadsheets — and Claude (Anthropic) from
  March 2026.
* The states `(ω, d)` are cited as the skeleton rows `(λ, k)` of J. Williams (arXiv:2607.01718,
  2 July 2026), posted earlier, with `λ = ω`, `k = d`, and Williams's Proposition 3.3, Theorem 3.6
  and Proposition 3.10 matched to Proposition B.2(iii), (i) and (ii). Section 4's laws answer
  Williams's open problem (1) in part: they give the depth of the row a trajectory lands in, and no
  law for its skeleton.
* Proposition D.1 is identified as the Böhm–Sontacchi cycle equation (1978) in block coordinates,
  and in integer form as Tao's `n`-Syracuse offset.

### Corrections

* Theorem C.3's unconditional bound is attributed to Baker theory for `ω ≠ 1` only (Bugeaud–Laurent,
  Corollaire 2). At `ω = 1` the pair `(9, 1)` is multiplicatively dependent; the bound holds there
  exactly, `s = 2 + v_2(d)`. No inequality printed in v3 was false.
* `T` is identified as Tao's `Syr`, and Appendix E's "from `T`-time to Syracuse time" (a clash: the
  paper's `T` is the Syracuse map) reads "from one-division-map time to Syracuse time".
* The entry-depth law's exhaustive check (Remark C.6, Appendix G) is restated from a re-run with
  independently written code: all `63,000` valid states with `ω < 3000`, `1 ≤ d < 64`, `ω = 1`
  included, where every law holds as stated, zero discrepancies; v3 printed `62,937`. The script,
  `experiments/depth_law_reverify.py`, is named.

### Bibliography

* Added: Rozier 1990 and 1991, Böhm–Sontacchi 1978, Halbeisen–Hungerbühler 1997, Brox 2000,
  LaDue 2018, Williams 2026, Sós 1958 and Świerczkowski 1958 (used in the proof of Theorem
  D.6(iii)), the mirror paper, and an entry for Rackl's 2021 thesis, which v3 named in its text
  without one.
* Updated: Simons–de Weger and Terras gain DOIs and issue numbers; Steiner gains "and Computing" and
  *Congr. Numer.* 20; Hercher gains its corrigendum of 14 June 2026 (a derivation repaired, no
  statement changed); Barina gains its issue number; Merle is cited at the version of 26 April 2026,
  at its version-specific DOI with the concept DOI beside it.

### Scope of v4

* Theorem D.6 is strengthened and proved; Remark D.8 is new; Theorem D.5 is attributed, unchanged in
  statement; Theorem C.3 changes only in the attribution of its unconditional bound. Nothing in v4
  is claimed new about the trim or about the exclusions at one to three blocks; what is offered for
  them is new derivations.
* The Version note is one paragraph with no drafting-time self-description, and the title page gives
  the version DOI and the concept DOI. Every wiki section and script named in the paper is cited at
  record commit `110f8b6`, public at <https://github.com/macindoe/collatz>.
* The document grows from 15 pages to 46: the main text takes pp. 4–12, and the appendices carry the
  formal text, the guided accounts, the proof of Theorem D.6 and the indexes.
