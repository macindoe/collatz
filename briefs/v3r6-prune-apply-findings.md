# Findings: the pruning plan applied (v3 round 6, apply)

**Branch.** `v3r6-prune`, cut from `main` at `29ecb1b`, worked in the main working directory. No
worktree, no push, no merge, no rebase, no other branch touched.

**Commits, in the order the brief prescribes.**

| commit | contents |
|---|---|
| `d03f1ea` | `aeh.md`: the `*`-density sentence at §13.3.2, and the status line's calibration clause |
| `881c92e` | `paper/collatz-reduced-v3.tex` + rebuilt PDF: the whole cut list |
| `91f76e0` | Appendix A's record pin `1663d30` → `881c92e`, and the rebuild that carries it |

**Headline.** **15 pages**, from 18. Typography untouched (`\documentclass[11pt]`, `margin=1.1in`,
no spacing or font change anywhere). Build clean: three `pdflatex -halt-on-error` passes, zero
overfull boxes, no undefined references, one pre-existing underfull hbox in the `lagarias`
bibliography entry. The six prohibited claims are absent and the qualifications that carry them are
all present. Every drop-in landed token-for-token as the design pass settled it, with one deliberate
one-clause deviation (§1, C5), recorded below with its reason.

---

## 1. The cut list, item by item

Verification method for "landed exactly": the applied text and the design pass's drop-in were
whitespace-normalised and compared token by token (`difflib`). Result per drop-in:
§3.1 143/143 tokens, 0 differing blocks; §3.2 324/324, 0; §3.3 157/157, 0; §3.5 256/256, 0;
§3.7 (the whole of §5) **2,973/2,973 tokens, 0 differing blocks**; §3.4 89 → 99 tokens, 2 differing
blocks — the deviation described under C5.

**Wiki landing (design §4) — done first, as instructed.** The `*`-density sentence is in `aeh.md`
§13.3.2, inserted in the Inselmann paragraph immediately after "…improving Tao's logarithmic-density
theorem to natural density for these thresholds." (the design pass's target sentence, confirmed at
that location in the file, not recalled). Nothing else in §13.3.2 was touched. C14 was therefore
applied; the parenthetical is gone from the paper and the fact is on exactly one page.

**Status-line asymmetry (brief item 2) — done.** `aeh.md`'s front-matter `status:` field read
"calibrated — bulk uniformity confirmed UNQUALIFIED at every tested depth and cell, at block lengths
L <= 2". It now reads "calibrated — no residual discrepancy at any tested depth or cell, within
three limits the campaign does not reach past: block lengths L <= 2, pooled adjudicating runs (a
consequence of 13.2.1, not its per-start form), and an altitude guard on the core that binds at
finite size (13.4, 13.5)". All three limits are what the record establishes: §13.5's *Status:
resolved* for the block length, §13.4's pooling paragraph ("the pooled runs test a consequence of the
hypothesis rather than the quenched statement itself"), and §13.4's protocol-gap paragraph (the core
cut "removes `4,191` of `158,580` visits (`2.6 %`)"). Kept to one clause plus pointers, per
`AGENTS.md`'s rule that `status:` is metadata and not a diary. The paper and the wiki now name the
same three limits. Two body sentences still say "unqualified" — see §7.1.

| item | disposition |
|---|---|
| **C1** version note → one paragraph | Applied, §3.1 verbatim, with the **first** of the two offered endings: "The repair history, item by item, is in this version's release description." The author's decision in the brief settles the choice the design pass declined to make. The v3-specific DOI leaves the note (it is on the title page, which the new note now points at: "the version-specific DOI on the title page is reserved"). |
| **C2** abstract | Applied verbatim. The *graded-residue* form of Theorem 3.7, the exit-valuation law and the depth closure are kept word for word, per the design pass's recorded near-miss. |
| **C3** introduction roadmap | Applied verbatim. |
| **C4** Related work | Not cut, as recommended. Untouched — the diff contains no hunk in that paragraph. |
| **C5** Remark 3.6 | Applied **with one deviation**. The drop-in reads "with the two branches on which $a_+$ is a $3$-adic function of $\w$ constructed rather than sampled". That is inaccurate against Lemma 3.4 as printed: $a_+$ is a $3$-adic function of $\w$ on the **boundary** branch $d = h(s)$ only (the third case of the display); the shallow branch $d < h(s)$ is constructed for a different reason, and `stage3.md` §11.8.6.3 says exactly that ("The resonant branch `d = h(s)` is **constructed rather than sampled** … as is the shallow branch `d < h(s)`"). Landed instead as: "with the boundary branch $d = h(s)$, on which $a_+$ is a $3$-adic function of $\w$, and the shallow branch $d < h(s)$ constructed rather than sampled." Ten tokens longer; the saving is otherwise as designed. Counts checked against `stage3.md`: `8,000` (status header), `62,937` with `ω < 3000`, `d < 64` (§11.8.6.3 numerical verification), `327,980` states and `983,954` checks (§11.8.6.3 *Verified*). |
| **C6** v2 note + correction → status paragraph | Applied verbatim (§3.5). Eleven-claim survival spot-checked at §2 below. The `9d9d1ec` record URL is preserved; the v2-era `72ec88e` URL is gone from the paper and is in the release-notes text at §4. |
| **C6b** sharpness cross-reference | Applied: "…the status paragraph below states what was proved, where, and at what scope." Nothing else in that paragraph changed. |
| **C7** window-chain `~1%` caveat | Cut. Survives at `aeh.md` §13.2 (final sentence of the `π_{k,D}` paragraph) and §13.6.5 (`17/63` vs `19/63`, `4/63` vs `2/63`, `19/63` vs `20/63`), both read in the file. The (R2) correction is carried by the definition, which is untouched. |
| **C8** class skeleton | Cut. Survives at `aeh.md` §13.2 "Supporting exact facts". The `(1 mod 8, d odd)` transition is kept in the paper where it does work — as the example showing the process is not independent across time. |
| **C9** `P(d=1)`, `P(d=2)` | Cut; the four `a_+` values that carry the Tao attribution are kept. Survives in Proposition 13.6.5's exact-values box, which the same paragraph already cites. |
| **C10** Chernoff tilt | Cut, with the pointer `(\texttt{aeh.md} \S13.2)` in its place. The rate `\log 2 - H(2\theta)` per bit and the vanishing at `θ = 1/4` are both kept verbatim, so the version note's promise about the base case still holds. |
| **C11** `O(2^{-k})` disclaimer | Cut. Survives at `aeh.md` §13.3.1, same sentence. |
| **C12** clock paragraph's block-time restatement | Cut, **after verifying copies 1 and 3 in the file being edited**: Related work's "All of these horizons are counted in steps… neither a theorem nor a consequence of Hypothesis~\ref{hyp:aeh}" (line 58) and the ledger paragraph's two-letter-statistic clause (lines 404–408). Both are present and unchanged. The clock paragraph keeps its own scoping clause, "a conversion available here precisely because the word is exactly $B$ here". |
| **C13** Inselmann recitation | Applied verbatim; `Cor.~1.4`, `Thm.~1.10`, `Thm.~1.6` keep their citations, and the sentence that does the work ("a theorem without the hypothesis **and a stronger one**") is kept. One wording observation at §7.2. |
| **C14** `*`-density parenthetical | Cut, **after** the wiki landing above. |
| **C15** bottom-regime gloss | The horizon copy is now the bare pointer "far above the \emph{bottom regime} of \texttt{aeh.md} \S13.1"; the Calibration copy is kept, where `z = 41` needs it. |
| **C16** calibration sentence | Applied in the design pass's form, not the reviewer's literal one, per the author's decision: "No residual discrepancy was detected at any tested depth or cell, under the stated protocol and within three limits the campaign does not reach past: …", all three named in full. The internal inconsistency ("two ceilings", then three) is gone. |
| **C17** remaining §5 compressions | Applied verbatim as part of the §3.7 whole-section text. |
| **not cut** | Hypothesis 5.1, the `W_{k,D}` display, the `gathered` display, Lemma 5.2, the two-sided `\hat B` definition, both Tao attributions with the `footnote 4 of arXiv v7` locator, the "product names exactly two clauses" scoping, the extended `(n+1)`-letter-word passage, the drift denial, protected/consistent/admissible, "the same unit, nothing converted", the `13.2.4(g)` scoping, "past that range the hypothesis supplies less", the shell-scale/triangular-array pair, the closing scope paragraph, Theorem 4.4's proof outline, Related work, the author's note, the responsibility and verification protocol. |

**Byte-identity of the protected material, checked by hunk boundaries.** `git diff -U1` produces no
hunk overlapping old lines 248–276 (Hypothesis 5.1), 242–244 (the `W_{k,D}` display), 359–366 (the
round-5 `gathered` display, on its two deliberate lines), 461–463 (Lemma 5.2), 58–59 (Related work),
44–46 (the author's note), 199–205 (Theorem 4.4 and its outline) or 471–473 (Appendix A, before the
pin commit). Nothing was cut beyond the list.

---

## 2. Spot-check of the eleven-claim survival table

Each row was checked against `cycles.md` in the file, not against the design pass's table. All eleven
survive; the locations are as tabulated, with one refinement noted.

| # | paper claim | found at | verdict |
|---|---|---|---|
| 1 | `8 − 5·log_2 3 = 0.0751874964…`, arc `[0.0415, 0.1169390665…]`, "any 66 consecutive integers" | Thm `12.8.6.1` statement (`θ := 8 - 5L = 0.0751874964...`; `δ_hi = 0.1169390665...`, `δ_lo = 0.0415`) and its proof ("**66 consecutive integers suffice and 61 do not**") | ✔ |
| 2 | window `[L^p, 1.05·L^p]` holds `0.05·L^p` integers, `79` at `p = 16`, first period supplying `66` | `12.8.6.1` proof, same paragraph: "exactly `50` at `p = 15` and `79` at `p = 16` — so `p = 16` is the first period supplying 66 consecutive integers" | ✔ |
| 3 | partial quotients / badly-approximable dead end | `12.8.6.1`, *Superseded formulation*: "the multiplicative gaps in the convergent chain *are* the partial quotients, so a uniform bound on them is exactly the assertion that `L` is badly approximable" | ✔ |
| 4 | additive offset `1/(L−1) = 1.70951` per block, no correction step | Thm `12.8.6.2` (title: "explicit construction; no correction step") and *The shape, and the constant that was missing*: "**geometric plus a fixed `1/(L-1) = 1.70951` per block**" | ✔ |
| 5 | `p ≥ 16` unconditional, `3 ≤ p ≤ 15` finite check, `p ∈ {2,4}` by exhibition | `12.8.6.1` ("for **every period `p >= 16`**"; the widened-scale finite check; `p ∈ {2,4}` outside reach) and *Scope, and what is not covered* | ✔ |
| 6 | `γ ∈ [3.683012, 5.140212]`, no `p`-dependence | `12.8.6.1` display and its "**both ends absolute constants, uniform in `p`**"; the two constants printed again in *Scope, and what is not covered*; `12.8.6.2` *Scope, exactly*: "no `p`-dependence at all" | ✔ |
| 7 | end to end at `p ∈ {3,…,26}`; construction verified through `p = 32` | `12.8.6.2` *Verified*: `experiments/staircase_gamma_upper.py` "(`23` periods over `p ∈ {3, 5, ..., 26}`, end to end)" and `staircase_allp_diophantine.py` (`p = 3...26`); "`p = 31` and `p = 32` beyond that". **Refinement:** the "end to end" range is carried by the two independent evaluators; the theorem-certified sweep itself runs `p ∈ {2,…,30}` outside `{2,4}`. The paper's status paragraph does not print either range, so nothing in it depends on this row. | ✔ |
| 8 | "from `p = 8` upward not one working witness is a convergent or semiconvergent denominator" | `12.8.6.4`, *The two `p = 22` rows*, final sentence — verbatim | ✔ |
| 9 | v2 route: semiconvergents, rounded geometric profile, bounded correction | `12.8.6.3`, kept "because the published v2 note names it" | ✔ |
| 10 | v2 range `p ∈ {2,…,23}`, `γ/log_2 p ∈ [1.828, 3.643]`; `p = 22` at `n = 25217`, `n = 31202`, `13` and `8` moves | Prop `12.8.6.4` display (`p ∈ {2, 3, ..., 23}`, `γ / log_2 p ∈ [1.828, 3.643]`) and *The two `p = 22` rows* (`γ = 11.186`, `13` moves; `γ = 14.746`, `8` moves) | ✔ |
| 11 | every configuration a size-passer only, all fail `q ∣ R_r` | `12.8.6` preamble ("Every configuration constructed here is a **size-passer only** … **all fail**"), `12.8.6.4` ("none passes"), *Scope, and what is not covered* | ✔ |

Also checked, since the status paragraph asserts them: the record URL `…/blob/9d9d1ec/cycles.md` is
preserved in the paper, and `cycles.md` has **no commits since `9d9d1ec`** (`git log 9d9d1ec..HEAD --
cycles.md` is empty), so that in-text pin is still current. The Appendix A pin was moved separately
(§6); the `9d9d1ec` content pin was not touched.

---

## 3. The six-claim sweep, after the cuts

Swept the whole `.tex`, not only the edited paragraphs, and the extracted PDF text.

1. **"AEH supplies the mean exponent past the digit budget" — absent, and its denial is intact.** The
   four surviving occurrences of `E_B[m+r] = 4` are: the definition of *consistent* (line 308); "under
   $B$ a block spends $\mathbb{E}_B[m+r] = 4$ of exponent" — a statement about `B` (314); "Where the
   cylinder count runs it is more, and unconditionally: for $\tau < 1$ … converges to $4$
   (`aeh.md` Lemma 13.2.4(g))" (317–320); and the clock paragraph's "only through the mean exponent per
   block … a conversion available here precisely because the word is exactly $B$ here" (372–374). The
   denial survives verbatim at 320–326: "$T_N^{-1}\sum_{n<T_N}(m_n+r_n) \to 4$ does not follow there
   and can fail by any amount."
2. **"It converts a horizon into blocks per bit" — absent.** The cut removed copy 2 of the correction;
   copies 1 and 3 are present and unchanged (Related work line 58; ledger paragraph lines 404–408,
   naming the two-letter statistic, `aeh.md` Lemma 13.2.4(g) inside the budget and §13.2.3 past it).
   The only surviving "blocks per bit" is the clock paragraph's, with its scoping clause attached.
3. **"The finite bound is about a word beginning at the sampled start" — absent.** The round-5 passage
   is byte-identical at lines 341–346: "That fact is about the word beginning at $x$ itself, while
   $\ell_0$ is the letter of the block \emph{after} the start's own; it is applied here to the
   \emph{extended} $(n+1)$-letter word … of whose law the one displayed is a marginal", and the
   `gathered` display below it is unchanged, `S_{n+1}` in both lines.
4. **"Bulk uniformity stands unqualified" — absent.** Zero case-insensitive occurrences of
   "unqualified" in the paper.
5. **"`13.6.4`'s union mass is exact" — absent.** `13.6.4` is named once, for the equivalence
   ("a deterministic dictionary between letters and labelled window blocks"); no mass, bound or
   exceptional event is attributed to it. The only "union" left is the triangular-array sentence, which
   says the union over all scales *is not controlled*.
6. **"Any conditional drift consequence" — absent, and both denials are intact.** Opening paragraph:
   "window equidistribution at each fixed $(k,D)$ does not control the means of the unbounded $m_+$ and
   $s$, so no drift or contraction statement about orbits follows from it (`aeh.md` §13.3.2)". Ledger
   paragraph: "The descent consequence is not stated here, because it is a theorem without the
   hypothesis and a stronger one".

No deletion stranded a qualification: each of the three (R3)/(R4) copies, the (R2) product scoping,
the (R5) extended-word clause and the two drift denials was located in the post-cut file by search.

---

## 4. The repair history, plain text for the author

Not landed anywhere in the repository. This is the design pass's block, checked line by line against
the record before reproduction: the two DOIs against the paper's title page and the old version note;
`72ec88e` and `9d9d1ec` against the v2 note and the correction; every staircase number against
`cycles.md` §12.8.6 (the eleven rows of §2 above); the definition/statement items against the body
(Definition 2.1's `\w > 0`; Theorem 3.3's `C(\w)(1+\log d)^2`; Theorem 3.8's stratum labels; Theorem
4.5's `n_0(p)`; the `heuristic` environment on the digit budget; Proposition 4.1's `\sigma_j` and the
`M_t`-vs-anchor note); and the theorem numbers against the built PDF (staircase = Theorem 4.6,
hypothesis = Hypothesis 5.1, routing = Lemma 5.2).

```
RELEASE NOTES — "Reduced coordinates for the Collatz map", v3 (August 2026)

v1 — July 2026. Original publication.

v2 — July 2026. Zenodo DOI 10.5281/zenodo.21421120.
  - Restored the subtitle of the `merle` citation.
  - Added a Note evidencing the sharpness hedge of Theorem 4.6 (the staircase),
    prompted by correspondence with Eric Merle: a single period-parametrized
    construction procedure — semiconvergents of log_2 3 select the exponent n, a
    rounded geometric profile builds the climb, a bounded correction closes the
    last bits — verified by exact big-integer arithmetic to produce a passing
    size-condition witness at every period p in {2,...,23}, with
    gamma / log_2 p in [1.828, 3.643]. The recipe's own candidate chain initially
    left p = 22 unresolved; correspondence with Eric Merle identified the cause as
    a gap in that chain's coverage at the required scale, not a failure of the
    correction step, and candidates outside the chain (n = 25217, n = 31202)
    resolved it with 13 and 8 correction moves. The note named its remaining gap:
    no proved closed-form bound on the multiplicative gap between consecutive
    correctly-signed semiconvergent runs.
  - No theorem or universal claim strengthened. v2 adds a finite computational
    evidence record.
  - Record of the v2 note: cycles.md 12.8.6 at commit 72ec88e.

v3 — August 2026 (drafted; version-specific Zenodo DOI 10.5281/zenodo.21730505
     reserved; not yet published). Five rounds of external review.

  THE STAIRCASE (Section 4).
  - The gap named in the v2 note has been closed, and closed by replacing the
    route rather than completing it. Candidate availability needs no
    continued-fraction input: 8 - 5*log_2 3 = 0.0751874964... is positive and
    below the target arc's length, so any 66 consecutive integers contain an n
    whose ceil(n*log_2 3) - n*log_2 3 lies in [0.0415, 0.1169390665...], and the
    scale window at period p holds 0.05*(log_2 3)^p integers — 79 at p = 16 — so
    p = 16 is the first period supplying 66 consecutive integers.
  - The bound the v2 note asked for is not needed and, as posed, is a dead end:
    those gaps are the partial quotients of log_2 3, so a uniform bound on them is
    exactly the assertion that log_2 3 is badly approximable.
  - The p = 22 episode was a property of the candidate list used, not of log_2 3:
    under the availability statement it does not arise — from p = 8 upward not one
    working witness is a convergent or semiconvergent denominator.
  - The construction half is closed independently: a corrected profile — the
    geometric climb with a fixed additive offset 1/(log_2 3 - 1) = 1.70951 per
    block, absent from the v2 profile — satisfies all p size conditions by
    construction, with no correction step. The bounded correction is removed from
    the argument rather than bounded.
  - The two halves compose to a proof for every period p >= 16, at gamma between
    the absolute constants 3.683012 and 5.140212 — no p-dependence at all — with
    3 <= p <= 15 meeting the same bracket by finite check, and p in {2,4}, outside
    the construction's reach, covered by direct exhibition. End to end verified at
    p in {3,...,26}; the construction itself verified through p = 32.
  - The proof is established in the project record and is NOT reproduced in the
    paper. Theorem 4.6 stands exactly as written in v1 and v2. Every constructed
    configuration remains a size-passer only and fails the divisibility conditions
    q | R_r: sharper evidence that counting cannot do better, and no evidence
    about exclusion.
  - Current record: cycles.md 12.8.6 at commit 9d9d1ec.
  - Presentational: the sharpness assessment, previously Theorem 4.6's closing
    clause, is set out beside the theorem under "Sharpness evidence and
    assessment", so the theorem environment carries only what the paper proves.

  DEFINITIONS AND STATEMENTS BROUGHT BACK INTO LINE WITH THE RECORD.
  - Definition 2.1 requires omega > 0, without which (-1, 1) leaves F undefined.
  - Theorem 3.3's unconditional bound reads C(omega)(1 + log d)^2; the printed
    (log d)^2 was vacuous at d = 1.
  - Theorem 3.8 states its depth-k window as the residues of Theorem 3.7 TOGETHER
    WITH the stratum labels (s, sigma, a_+), matching its own proof. Theorem 3.7
    is unchanged.
  - Theorem 4.5's n_0(p) is defined.
  - The digit budget is labelled a heuristic, as its own text always said; no part
    of it is claimed as proved.
  - Proposition 4.1 defines sigma_j at its point of use (sigma_j = s_j + m_{j+1},
    as in Definition 2.1) and distinguishes M_t, a partial sum of entry depths,
    from the anchor M(omega).

  SECTION 5 — ONE OBJECT, ONE CLOCK, ONE HYPOTHESIS.
  - The section now carries one object where it previously carried several. The
    observable is the capped window W_{k,D}, at a depth k and a cap D quantified
    together, the cap bounding the stratum labels as well as the depth.
  - The comparison law pi_{k,D} is the law of that window under the two-sided
    Bernoulli measure, its depth component the exact convolution rather than the
    window chain's stationary law. "Product" names its two proved clauses and no
    others — in particular the window process is stationary but not independent
    across time.
  - Hypothesis 5.1 is stated in ensemble form — uniformly sampled starts, a
    horizon linked to the sampling scale, every block counted once, a single limit
    — in letter coordinates and at every finite block length. This retires both
    the single-orbit reading, which is empty on every convergent orbit, and the
    single-visit reading, which is strictly weaker. The distance is total
    variation on the finite window alphabet, named where it is used.
  - The bulk cut is replaced by an exponent budget whose admissibility is defined
    and whose protection is a deterministic identity rather than an assumption.
  - The section states NO descent or contraction consequence of Hypothesis 5.1:
    that conclusion is a theorem without the hypothesis, and stronger, so the
    section is framed onto what the hypothesis alone supplies, which is
    distributional.
  - The unconditional base case is given with the exact rate at which it holds and
    the exact horizon at which that rate vanishes. It is about the EXTENDED
    (n+1)-letter word — the start's own letter followed by the n sampled letters —
    and not about a word beginning at the sampled start; the displayed bound is a
    marginal of that word's law.
  - The density conclusion is stated at dyadic-shell scale, where it is exact; the
    union over all sampling scales is a triangular array that no per-scale
    statement controls.
  - Section 5 does not claim that Hypothesis 5.1 supplies E_B[m + r] = 4, or the
    empirical exponent mean, past the digit budget; and the reading of any
    step-time horizon in reduced blocks is a theorem of the cylinder count inside
    the digit budget and, past it, neither a theorem nor a consequence of the
    hypothesis.

  ATTRIBUTIONS PAID.
  - The stationary 3-adic law governing the absorption is Tao's Syracuse random
    variable (Forum Math. Pi 10 (2022) e12, Lemma 1.12 and Remark 1.13), in the
    present normalisation; the block coordinate's 3-adic past-limit has the law of
    Syrac(Z_3)/2.
  - Its negative-time reading is Tao's own alternative to his positive-time
    indexing, at Remark 1.13, footnote 4 of arXiv v7.
  - The unconditional density line the hypothesis does not add to — Terras,
    Everett, Korec, Inselmann, Tao — is cited in Related work, with the horizons
    given in the step units in which they are proved.
  - The two further 3-adic studies a reader of Tao's footnote will reach
    (Wirsching, Thomas) are cited and distinguished from the object appearing
    here.

  CALIBRATION.
  - The record is reported with the limits it does not reach past: block length
    L <= 2, pooled adjudicating estimates, and an altitude guard on the core that
    binds at finite size (2.6% of visits in the adjudicating run, moving the
    reported statistics at the third decimal).

  SCOPE OF v3.
  - No numbered theorem's claim is strengthened, weakened, or renumbered, and
    nothing new is proved in the paper. v3 reports two results established in the
    project record and not reproduced there: the sharpness construction of
    Section 4 and the base-case assembly of Section 5.
  - Verification pointers and script names are concrete throughout. The complete
    record is public at https://github.com/macindoe/collatz; Appendix A pins the
    commit at which every wiki section and script named in the paper is cited.
```

One wording call left to the author: the block says "Five rounds of external review", which counts the
rounds that changed claims. This pruning round changed no claim, so the count is unchanged unless the
author prefers to count it, in which case the line reads "six rounds".

---

## 5. Build report

Rebuilt after the paper commit and again after the pin commit; both are reported.

| pass | command | exit | result |
|---|---|---|---|
| 1 | `pdflatex -halt-on-error -interaction=nonstopmode collatz-reduced-v3.tex` | 0 | 15 pages |
| 2 | same | 0 | 15 pages |
| 3 | same | 0 | 15 pages |

After the pin change, three further passes, all exit 0, 15 pages, 417,117 bytes; `rerunfilecheck`
reports `collatz-reduced-v3.out` unchanged, so the run is converged.

* **Overfull boxes: none**, at any pass.
* **Underfull boxes: one**, `Underfull \hbox (badness 1067) in paragraph at lines 459--460` — the
  `\bibitem{lagarias}` entry ("J. C. La-garias, The 3x+1 prob-lem: an an-no-tated bib-li-og-ra-phy,
  I--II, arXiv math/0309224,"). Pre-existing, as the design pass recorded, and untouched by this round.
* **Unresolved references or citations: none.** No `LaTeX Warning`, no "undefined", no "multiply
  defined", no rerun request in the log.
* **Page count: 15**, exactly the design pass's measured Plan B. No discrepancy to explain.
* **PDF text checks.** `pdftotext -layout` shows 15 page breaks; zero occurrences of "Note added in
  v2", "Correction, 2026-08-01", "stationary law of the exact window chain", "class skeleton",
  "Chernoff", "blocks per bit only after dividing", "density: every initial segment", "Uniformity
  stands unqualified", "two ceilings" and "prices a different statement"; and the replacements are all
  present ("Status of the assessment", "No residual discrepancy", "three limits", "release
  description", "status paragraph below").

Typography untouched: `\documentclass[11pt]{article}`, `\usepackage[margin=1.1in]{geometry}`, no
change to any spacing, font size or environment.

---

## 6. The pin, and the verification of its claim

Appendix A now reads "every wiki section and script named in this paper is cited at commit
`881c92e`" — format unchanged, one `\texttt{}` seven-hex pin in the same sentence.

Verified with `git show`, never the working tree:

* **Positive.** `git show 881c92e:aeh.md` contains the `*`-density sentence ("What buys the iteration
  invariance his argument needs…") and its status line carries "within three limits the campaign does
  not reach past: block lengths L <= 2, pooled adjudicating runs …". `git show
  881c92e:paper/collatz-reduced-v3.tex` contains the pruned paper (the status paragraph is present).
* **Negative.** `git show 1663d30:aeh.md` contains **no** `*`-density sentence (0 matches) and its
  status line still says `UNQUALIFIED` (1 match). The old pin could not have supported the pruned
  paper's pointers.
* **Coverage.** At `881c92e`, every record and script the paper names resolves: `stage3.md`
  §11.8.6.3; `cycles.md` §12.8.6, §12.6.1, §12.2.3, §12.5.3, §12.7.5, §12.5.2, §12.7.4, §12.6.2;
  `itinerary.md` §14.15.1.5; `aeh.md` §13.2.4, §13.6.4 (and §13.1, §13.2.3, §13.3.1, §13.3.2, §13.4,
  §13.5, §13.6.3, §13.6.5, §13.6.6); and `experiments/absorption_law.py`,
  `one_step_propagation.py`, `anchor_increment.py`, `period1_cycles.py`, `period2_cycles.py`,
  `period3_cycles.py`.
* The pin commit `91f76e0` contains only the pin line and the rebuilt PDF.

---

## 7. Found and not fixed

1. **`aeh.md` still says "unqualified" twice in the body.** §13.5 *Status: resolved* ("Bulk uniformity
   stands **unqualified** at every tested depth and cell, at block lengths `L ≤ 2` — the campaign tests
   `L = 1` and `L = 2` and is silent above") and the *Current state* blockquote ("Bulk uniformity
   stands unqualified at block lengths `L ≤ 2`, which is as far as the campaign reaches"). The brief's
   item 2 names the status line, which is the front-matter field, and that is what was changed; both
   body sentences qualify themselves in the same sentence, and rewriting page prose is outside this
   round. The paper is now the more conservative of the two documents. Handed back.
2. **The Inselmann pair is described jointly.** C13's settled text reads "Inselmann's `[Cor. 1.4,
   Thm. 1.10]`, cited in Related work, is two-sided, uniform in the time, unconditional". `Cor. 1.4`
   on its own is the one-sided descent statement; `Thm. 1.10` is the two-sided envelope from which it
   follows, and Related work states each accurately three paragraphs earlier. Landed as settled, but
   if the author wants the pair split, the minimal repair is "…are unconditional and run to
   `4.8188…` times the classical range, the second two-sided and uniform in the time".
3. **Two paper-only facts remain paper-only**, as the design pass recorded and this round did not
   change: the identity `1 − β/4 = log_4 3` tying the frontier to Korec's exponent, and the Wirsching
   "siblings in shape" comparison in Related work. Both are kept in the paper; neither is in the wiki.
   A later pass that trims either should land it first, exactly as C14 was handled here.
4. **The retired-route pointer is `\S12.8.6.3` only** (design §8.4). `12.8.6.4` also carries the
   `p = 22` episode and the instance record. Left as settled to save the line; naming
   `\S12.8.6.3--\S12.8.6.4` is a one-word change if the author prefers precision.
5. **Whether the v2 note's text should be reproduced permanently** (design §8.3) is untouched and
   remains the author's editorial call. The release-notes block at §4 reproduces its substance, and
   `cycles.md` §12.8.6.3 keeps the superseded recipe "because the published v2 note points at it".
6. **The Discussion's "transfer-operator analysis of the exact window chain" was left exactly as it
   is**, per C7's checkpoint: after the cut it reads as the chain of Theorem 3.8's exact windows,
   which the paper defines, and it must not be rewritten into a claim about a stationary law.
7. **Not attempted, per the brief:** `open-problems.md` 11.12 (the indexing standardization), the
   deferred prefix result, and any change to `13.3.2` beyond the `*`-density addition.
