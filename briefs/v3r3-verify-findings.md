# Findings: verify round 3 (v3 round 3, Wave 4)

**Task:** `briefs/v3r3-verify-brief.md`. **Branch** `v3r3-review-round3` at `fa07929`; `main` at `dc61306`.
Worked in the main working directory. **No git write of any kind** — no commit, branch, checkout, push,
merge or stash. **No tracked file was edited**; this file is the only thing written.
The PDF rebuild modified `paper/collatz-reduced-v3.{aux,log,out,pdf}` in the working tree, as the brief
anticipates. Scratch code and downloaded sources are in the session scratchpad.

**Merge recommendation: merge after the named fixes in D1–D4.** Everything mathematical I was able to
check is sound and was independently reproduced. The defects are a citation locator that lands in the
paper, three pages the round left stale, and three unexecuted steps of `AGENTS.md`'s own proved-claim
workflow. None of them requires touching a proof or a measured value.

---

## 1. Defect list, most severe first

### D1. The Tao footnote-4 locator does not match the reference the paper prints. **[paper + record]**

Sites: `paper/collatz-reduced-v3.tex` L246 — `\cite[Remark~1.13, footnote~4]{tao}` (rendered PDF **p. 12**);
`aeh.md` `13.6.5` **Attribution**. Both were newly added this round (paper-apply §5 item 3; record-apply
§1, `13.6.5` attribution row), and both apply delegates state they did not re-read Tao.

I downloaded three arXiv versions of `1909.03562` and extracted the text of each:

| version | date | Remark 1.13's footnotes |
|---|---|---|
| v4 | 2021-09-18 | one footnote, **4** = *"This Markov process may possibly be related to the 3-adic Markov process for the inverse Collatz map studied in [24]. See also a recent investigation of 3-adic irregularities … in [23]."* No "ancient" anywhere in the paper (0 hits). |
| **v5** | **2022-02-15** | **identical to v4** — one footnote, numbered **4**, the Wirsching/Thomas pointer. `ancient`, `negative integers`, `arbitrarily large`, `aesthetic`: **0 hits each in the whole paper.** |
| v7 | 2026-07-16 | **two** footnotes. **4** = the "ancient" footnote, verbatim as `briefs/v3r3-inselmann-horizon-findings.md` §6.1 transcribes it, including *"arbitrarily large negative times (and whose initial condition is irrelevant)"* and *"arguably more natural"*. **5** = the Wirsching/Thomas pointer. |

So: **delegate B's transcription is exact and the substantive attribution is correct** — the ancient-iteration
reading is Tao's own, in Tao's own words, in the current arXiv version. **The locator is wrong against the
reference as printed.** The paper's bibliography entry (L456) and `aeh.md` `13.6.5` both cite
*Forum Math. Pi* **10 (2022)**, Paper No. e12 — which corresponds to arXiv **v5**, where footnote 4 of
Remark 1.13 is the Wirsching/Thomas note and the ancient-iteration footnote does not exist. A referee who
opens the printed reference finds the wrong footnote and no support for the sentence it is carrying.

Compounding it: the paper's Related work (L59) says *"Tao's paper carries a footnote to two further 3-adic
studies"* — that is footnote **5** in v7 and footnote **4** in v5. The two statements are jointly consistent
only against v6/v7.

**Fix (one line, two sites):** pin the version in the locator or the bibliography — e.g.
`\cite[Remark~1.13, footnote~4 (arXiv v7)]{tao}` — or drop the number and cite "Remark 1.13's footnote on
negative-time indexing". Nothing else about the attribution needs to move.

### D2. `README.md` is stale on all three of this round's headline corrections, and was not touched.

`README.md` L40, the "statistics door" paragraph, still reads:

* *"every tested statistic matches the **exact product law**"* — "product law" is precisely the misreading
  `briefs/v3r3-aeh-object-findings.md` §11 says the round exists to remove; the paper's abstract, §1 and §5
  and every `aeh.md` site were changed for it (`π_k → π_{k,D}`; "product" now names two clauses and no others).
* *"**Bulk uniformity stands unqualified at all tested depths.**"* — the exact retired sentence. The round
  narrowed it, in `aeh.md` `13.5` and at paper L332, to *"unqualified at every tested depth and cell, at block
  lengths `L ≤ 2`"* plus the pooled-versus-per-start ceiling. Neither ceiling appears in `README.md`.
  (`paper/collatz-reduced-v2.tex` L240 carries the same sentence, but v2 is published and immutable.)
* *"for all but a **density-zero set of starting values** over a prescribed finite horizon"* — the exact
  phrasing the paper deliberately weakened to *"a set of starting values of vanishing density"* (paper-apply
  §5 item 7), because `13.2.5` restricts unrestricted density zero to shell scale.

`README.md` is a tracked wiki-layer file (`AGENTS.md`, Layers 4: "the human-facing map, including the
program's strategy and stopping rules … binding on agents too") and it *was* edited in round 2 (`c2d465a`),
so it is inside the maintained set. Under `AGENTS.md`'s "every fact lives in exactly one page" it arguably
should point at `aeh.md` rather than restate; either way it is now wrong.

### D3. `bridge.md` §16.4.3 carries the retired unqualified claim — on a page this round edited.

`bridge.md` L71: *"The open object lives in the bulk (while `x` is large), **where uniformity stands
unqualified**"*, with no ceiling. The same bullet list's first item (L69) *was* rewritten this round
(`π_k → π_{k,D}`, the ensemble/window split), so the delegate was in this paragraph. L69 also keeps
*"a density-zero set of starting values over a prescribed finite horizon"*, the phrase the paper repaired.
Same defect class as D2, smaller blast radius.

### D4. `AGENTS.md`'s proved-claim workflow was invoked but only step 1 was executed.

`aeh.md`'s front matter now records a status change — *"unconditional base case **PROVED** at `13.2.4` (every
`θ < 1/4`, at every block length) with the exceptional set at shell scale (`13.2.5`)"* — and the record
delegate's own §5 item 1 justifies that clause by citing the workflow. The workflow has four steps:

1. Owning page + front matter + Current state + the statement. **Done.**
2. *"Update the compact ledger (stage1.md 11.8.4.5)."* **Not done.** `stage1.md` L620–623 still lists the
   frequency ledger `P(s=k)=2^{-k}` and the 3-gain rate `1/3` under **`heuristic, empirically sharp`**. They
   are now unconditional theorems inside the digit budget (`13.2.4`(d)/(e) + `13.2.4.1`).
3. *"Sweep `open-problems.md` for entries that posed the question as open; add a calibration note pointing to
   the closure."* **Not done.** Its one AEH entry (L84) still reads *"under AEH it is a conditional theorem
   (aeh.md 13.3.2), and what remains open is its unconditional derivation along orbits"* — with no note that
   the `θ < 1/4` range is now closed unconditionally.
4. *"If stage-level, update … the status summary in `index.md`."* **Not done.** `index.md` L46 describes AEH
   as *"formalized and calibrated clean at bulk uniformity … proof effort stays parked"*; no base case, no
   ceilings. (`index.md` L46's *"AEH ⟺ bulk Bernoulli-genericity of the door letter word"* **is** now true
   under Option 1 — see §3 item 1 — so that half needs no change.)

### D5. The unbriefed `13.6.4`(⇐) parenthetical is true and necessary, but is an incomplete repair.

Full verdict in §4. Summary: true; the proof is correct with it; it *was* necessary (the sentence became
false when the round capped the window's labels); but it still leaves a limit argument implicit, and the
(⇒) direction of the same proof spells the analogous step out.

### D6. The Appendix A pin needs a follow-up commit.

Full verdict in §5. `b278e5a` makes Appendix A's sentence literally true but names a commit at which
`paper/collatz-reduced-v3.tex` is the *previous* paper and still prints `c2d465a`.

### D7. `aeh.md` `13.2`: "23 of its 30 tallied blocks past the first budget" measures **22.0**.

Re-running the flagship protocol (seed `31005`, starts `[2^70, 2^71)`, burn-in `10`, horizon `30`) under the
page's own accounting — the accounting that reproduces its `τ ≈ 2.29` exactly — the mean number of tallied
blocks with `S_n ≥ 70` is **22.006**, not 23. Mean total exponent over burn-in + horizon is `160.06`
(`τ = 2.2866`), so one budget is spent after `70/4.0016 = 17.49` blocks and the tallied blocks past it are
indices `18…39`, i.e. 22 of 30. Off by one; nothing downstream depends on it.

### D8. The "parity pattern `11`" identification is a complement slip, in two pages.

`aeh.md` `13.3.2` and `publication.md` landscape item 4 both say the missing statistic — *"the frequency with
which a `Syr`-step ends a block"*, i.e. `P(v₂(3m+1) ≥ 2) = 1/2` — *"in parity coordinates is the density of
the pattern `11`"*. A Syracuse step **ends** a block when the valuation is `≥ 2`, which in the `T`-parity
word is a `1` followed by a `0`; `11` is the complementary event (valuation `= 1`, block continues). Both
have probability `1/2` and both are two-letter statistics, so the **load-bearing claim is unaffected and is
correct** (see §3 item 2). Cosmetic, but it is a statement about a source and both pages say it the same
wrong way.

### D9. The paper-apply delegate's claim that the version note contains "no 'was X, now Y'" is false.

`briefs/v3r3-paper-apply-findings.md` §5 item 2: *"It is a description, not a change log: no 'was X, now Y'."*
The version note (tex L42, PDF **p. 1–2**) contains at least: *"Section 5 carries one object where it
**previously** carried several"*; *"its sharpness assessment, **previously** the theorem's closing clause"*;
*"**retiring** both the single-orbit reading … and the single-visit reading"*; *"the bulk cut **is replaced
by** an exponent budget"*. A version note is the correct genre for that content in a DOI'd paper, and
`AGENTS.md`'s no-change-log rule targets wiki pages; what is wrong is the self-assessment, not obviously the
note. Author's call — flagged so it is a decision rather than an oversight.

### D10. The paper prints two calibration numbers the record now qualifies, without the qualifier.

PDF **p. 15**: *"deviations reach `z = 41`"* and *"1,600–2,600 independent orbits per cell"*. `z = 41` is
row A2 of the biased-number list — the bottom-regime deviation read off the **complement** of the core cut
in the same `aeh_calibration.py` run. The paper asserts nothing false (it never claims a cut does not bind),
but a reader comparing paper and record finds the record strictly more qualified. Already flagged by the
paper delegate (§7 item 3); repeated because it is merge-relevant.

### D11. Rendered layout: clean. Two cosmetic observations only.

See §6. No overfull boxes, no broken displays, no widows, no orphaned headings on any of the 17 pages.

### D12. The round adds **five** new `aeh.md` anchors, not three; no existing anchor was renumbered.

New: `13.2.2`, `13.2.3`, `13.2.4`, `13.2.4.1`, `13.2.5`. (`git show dc61306:aeh.md | grep "13\.2\.[2-9]"`
returns nothing, so `13.2.2` is new too; the brief's "three new ones" matches the three the *paper* newly
cites.) Every pre-existing anchor survives with its meaning: `13.2.1`, `13.3.1`–`13.3.3`, `13.5.1`,
`13.6.1`–`13.6.7`. **No renumbering.** Informational, not a defect.

---

## 2. What I independently reproduced, and the numbers I got

Everything in this section is a number I ran or computed here. Where a number is quoted from a page I give
the page's value alongside.

### 2.1 `experiments/aeh_basecase.py` — run in full, exit 0

Every figure in `aeh.md` `13.2.4`'s **Verified** line reproduced:

| claim on the page | what I got |
|---|---|
| cylinder count exhaustive `J = 18, 20, 22`, `1,376,253` distinct words, `0` failures | `65,535 + 262,143 + 1,048,575 = 1,376,253`; `0` failures at each `J` |
| class invariance + modulus sharpness, `3,000`-bit starts, `n = 600`, `40` trials, seed `34002` | `fail_class_invariance 0`, `fail_sharpness 0` |
| general window, seven `N`, `TV 0.015212` vs `0.015213` at `2^21`, `2^21+1` | seven `N`; `0.023518, 0.030505, 0.026863, 0.019983, 0.015212, 0.015213, 0.017810` |
| tail identity exact at five `(n, J)` | `all exact: True`, five rows |
| per-start s.d. `0.0234 → 0.0166 → 0.0118 → 0.0083` | `0.023381, 0.016640, 0.011786, 0.008253` |
| exceptional density at `ε = 0.03`: `0.188 → 0.065 → 0.013 → 0.000` | `0.18800, 0.06533, 0.01267, 0.00000` |
| `a_0` at `L¹` `0.0063` from the uniform-start law, `0.163` from bulk; `a_1` at `0.063` | `0.00627`, `0.16307`, `0.06346` |
| (c) `0` failures over `72,000` steps (`b=1200`, `θ=0.20`) and `115,200` (`b=2400`, `θ=0.24`) | `240×300 = 72,000` and `576×200 = 115,200`, `0` failures both |
| `I(0.20) = 0.0201`, `I(0.24) = 0.00080`, `I(1/4) = 0` | `0.0201355136`, `0.0008002135`, `0.0000000000` |

### 2.2 The entropy rate and the tail identity, derived by hand (not taken from the script)

`S_n = Σ_{i<n}(m_i + r_i)` is the sum of `2n` iid geometric(1/2) on `{1,2,…}`, i.e. the waiting time for the
`2n`-th head. Hence `P(S_n ≥ J) = P(fewer than 2n heads in J−1 flips) = P(Bin(J−1,½) < 2n)` — **exactly**,
as printed. Chernoff on the `S_n` side: `E[e^{λS}] = (e^λ/(2−e^λ))^{2n}`; optimising `−λJ + 2n log(e^λ/(2−e^λ))`
gives `2 − e^λ = 4n/J`, so at `J = b`, `n = θb` the tilt is **`e^λ = 2(1−2θ)`** and `λ > 0 ⟺ θ < 1/4` —
exactly the page's clause. The rate is
`(1−2θ)log(2(1−2θ)) + 2θ log(4θ) = log 2 − H(2θ)`, vanishing at `θ = 1/4`. **Both identities confirmed
analytically, not just numerically.**

### 2.3 The depth marginal, in exact rational arithmetic, from a derivation I did myself

I did not use the repository's offset formula. From `G(y) = (3^m(y+1) − 2^m)/2^{m+r}` and `z = y+1`:

```
z' = (3/2)^m · 2^{-r} · z + (1 − 2^{-r})   in Z_3,   letters iid, m ⊥ r, each geom(1/2)
```

Mod `3^j` the coefficient vanishes once `m ≥ j`, so `j` iterations from any start give the exact law.
Kernel built from `j` `m`-branches and `L = 2·3^{j-1}` exact `r`-residue branches, all `Fraction`:

| | page (`13.6.5`) | mine |
|---|---|---|
| `P(a=0)` | `2/3` | `2/3` |
| `P(a=1)` | `19/63` | `19/63` |
| `P(a≥2)` | `2/63` | `2/63` |
| `P(a≥3)` | `~0.0061` | `1598/262143 = 0.006095909…` |
| `P(d=1)` | `1/3` | `1/3` |
| `P(d=2)` | `20/63` | `20/63` |
| `P(d=3)` | `~0.171555` | `44972/262143 = 0.1715550…` |
| `P(d=4)` | `~0.087916` | `1583755369414100/18014398509481983 = 0.0879159…` |

**Cross-check against the source, not against the record:** pushing my law forward by `S = 2z − 2` gives
`Syrac(Z/9Z) = 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63` — **character-for-character Tao's printed
nine values**, which I read in his own PDF (p. 10, immediately after the proof of Lemma 1.12). The `2/63` sits
at residue `7 ≡ −2 (mod 9)`, as `13.6.5` says.

The window-chain contrast also checks: `P(a≥2) = (20/63)(1/3)(1/2) + (1/63)(2/3) = 12/189 = 4/63`, hence
`P(a=1) = 17/63` and `P(d=2) = 19/63`. Re-running `aeh_symbolic.py` reproduces the chain's quoted digits
exactly: `0.333333, 0.301587, 0.172524, 0.092939, 0.048695`.

### 2.4 The flagship cut measurement — replicated with fresh primitives and the same RNG stream

The brief's no-code check first: the run does `HOR = 30` steps for every orbit that passes `w % 3 ≠ 0`, so a
cut-free tally is a multiple of 30. `154,389 / 30 = 5146.3` — **not** a multiple of 30, so the cut binds.
Confirmed by measurement:

| quantity | page / docstring | mine |
|---|---|---|
| orbits sampled | — | `5,286` (`158,580 = 30 × 5,286`) |
| visits removed by the **core** cut `ω₊ > 2^30` | `4,191` of `158,580` (`2.6 %`) | `4,191`, `2.643 %` |
| orbits on which the core cut binds | `15.5 %` | `820 / 5,286 = 15.51 %` |
| visits removed by the **door** cut | `2,653` (`1.7 %`) | `2,653`, `1.673 %` |
| orbits on which the door cut binds | `8.9 %` | `472 / 5,286 = 8.93 %` |
| visits where the two rules disagree | `1,538` | `1,538` |
| mean `s`: uncut / door / core | `1.9999 / 1.9930 / 1.9871` | `1.9999 / 1.9930 / 1.9871` |
| `s ≥ 6` tail depressed by | `2.0 %` / `3.4 %` | `2.02 %` / `3.41 %` |
| tallied visits | `154,389` | `154,389` |

Every number in `13.4`'s protocol-gap paragraph and `aeh_symbolic.py`'s new docstring is exact.

### 2.5 `13.6.5`'s orbit adjudication, and the same run **without** the cut

| | core cut (as printed) | no cut |
|---|---|---|
| `P(d=2)` | `0.31919` (page: `0.3192`) | `0.31854` |
| `L¹` over `d ≤ 5` vs the exact law | `0.00517` (page: `≤ 0.006`) | `0.00241` |
| chain-law offset at `P(d=2)` | `0.01760` (page: `0.018`) | `0.01695` |
| `P(ω₊ ≡ 1 mod 3 \| a₊ = 0)` | `0.6662 ± 0.0015` (`0.3σ` from `2/3`, `112σ` from `1/2`) | `0.6651 ± 0.0015` (`1.1σ` from `2/3`) |

The pooled standard error at `n = 154,389` is `0.00117`, so `0.01760 / 0.00117 = 15.1`; the page says
`≈ 14`. Within "≈", but it understates.

### 2.6 Other reproductions

* `experiments/aeh_anomaly.py`: `P(ω ≡ 25 mod 32 | class) = 0.2503` over `84,739` visits ✓; the routing
  lemma exhaustive on `6587 + 6602 + 6705 + 6779 = 26,673` states, all four residues deterministic, zero
  exceptions ✓ (`13.5.1`'s figure exactly).
* `experiments/aeh_symbolic.py`: full run, **all checks passed**, `0` failures; the `4,368`-visit / `1`-exceptional
  reconstruction (seed `31003`) and the `400 × 50` seam/time checks (seed `31002`) reproduce.
* `13.2`'s *"measured exponent per block is `4.0017`"*: I get `4.0017` for the mean of `m + s` over all 30
  tallied blocks **with no cut** (the core-cut value is `3.9782`). So that figure is cut-free.
* `τ ≈ 2.29` and "47 % of the descent": mean total exponent `160.06` over 40 blocks, `160.06/70 = 2.2866`,
  `2.2866/4.8188 = 47.5 %` ✓.
* `β = 2(2 − log₂3) = 0.8301…`, `1/β = 1.2047…`, `4/β = (1 − log₂√3)^{-1} = 4.81885…`, `1 − β/4 = log₄3 =
  0.7924813` (Korec's exponent) — all check.

### 2.7 The PDF rebuild

Three `pdflatex -halt-on-error -interaction=nonstopmode` passes, MiKTeX-pdfTeX 4.23.0, exit `0/0/0`.
**17 pages, 432,124 bytes — byte-for-byte the same length as the committed PDF.** `cmp -l` finds
**62 differing bytes in total**, all inside `/CreationDate`, `/ModDate` and the trailer `/ID`. So the
committed PDF is exactly reproducible from the committed `.tex`. Log: `0` overfull boxes, `1` underfull
(`badness 1067`, the pre-existing `rhin` bibliography box, now at tex lines `470--471`), `0` `LaTeX Warning`
lines, `0` undefined references or citations.

I also re-derived the paper delegate's §4 claim independently: extracting every `theorem / proposition /
lemma / corollary / definition / hypothesis / heuristic / remark` environment from both `.tex` files and
whitespace-normalising gives **22 before, 22 after, same labels in the same order**, and exactly **two**
differ — `thm:onestep` ("the product law of Section 5" → "the law `$\pi_{k,D}$` of Section 5", nothing else)
and `hyp:aeh` (restated, as authorised). Confirmed.

### 2.8 Inselmann, read at the source

I downloaded `arXiv:2402.03276v3` and extracted the text. Checked directly:

* **Thm 1.10** — *"the set `{m ∈ D+ | 0 ≤ k ≤ (log₂(4/3))^{-1} log₂ m : (3/4)^k m^{1−ε} ≤ Syr^k(m) ≤
  (3/4)^k m^{1+ε}}` is of natural density 1 in `D+`."* **Exactly what `aeh.md` `13.3.2` states**, including
  the `(3/4)^k` envelope, the Syracuse-step unit and the odd-integer domain. ✓
* **Cor 1.4** — `{m : T^{⌊log₂ m/(1−log₂√3)⌋}(m) ≤ m^ε}` of natural density 1, stated for `T`. ✓ matches.
* **Thm 1.6** — bounds `|Σ_{i=0}^{k−1} p(m)_i − k/2| ≤ ε log₂ m` over the same horizon: **the density of the
  one-letter pattern `1` and nothing more.** ✓ The page's claim that it "gives nothing about `11`" is correct.
* **The circularity claim is correct, and Inselmann's own step is not.** His Syracuse theorem is **Thm 3.8**,
  whose proof uses **Thm 2.18** (the `∗`-dense form of Thm 1.1) **plus Thm 3.3** (the `∗`-dense form of
  Thm 1.6) and **eq. (3.20): `Syr^{Σ_{i=0}^{j-1} p(m)_i}(m) = T^j(m)`** — transcribed verbatim in the source.
  So `13.3.2`'s sentence *"Inselmann makes the analogous time change one level up and proves his input"* is
  accurate, and the step this page needs (Syracuse time → block time, needing `P(exponent ≥ 2) = 1/2`) has no
  counterpart theorem in his paper. ✓
* **Def 2.6** — `(C,D)`-density: `μ_{[1…N]}(S ∩ [1…N]) ≥ 1 − C/N^D` for every `N`, `0 < D ≤ 1`, `∗`-dense =
  `D`-density for **some** `0 < D ≤ 1`. ✓ The paper's gloss "all but `O(N^{-δ})` … for some `δ > 0`" and the
  `D → δ` re-lettering (paper-apply D5) are both right.
* **Inselmann's `T`** is `m/2` (even), `(3m+1)/2` (odd) — the one-division map, so `13.2.3`'s parenthetical
  identifying it with `T_1` is correct. ✓
* The constant: his abstract's `α = 2(log 4/3)^{-1} ≈ 6.952` in natural log is `6.952 × log 2 = 4.8188` in
  `log₂` — the same number the page uses, confirmed from the source rather than recomputed from the page. ✓
* The two-sidedness claim in `13.2.3`'s third bullet also checks: Thm 1.3 gives `m^{γ±ε}` at `T`-time
  `(1−γ)·4.8188·log₂ m`, i.e. altitude `(1 − τ/4.8188)log₂ N ± ε log₂ N` at budget `τ`, exactly as printed.

### 2.9 UTF-8, protocol hygiene, script behaviour

* `≤ — ε ≥` decode cleanly in every edited page; **no mojibake byte sequence** (`â`, `Ã`, `Â`, `U+FFFD`) in
  `aeh.md`, `publication.md`, `itinerary.md`, `bridge.md`, `anchor-digit-search.md`, either script, or the
  `.tex`. The `.tex` is pure ASCII, as claimed.
* `git diff dc61306..HEAD -- experiments/aeh_symbolic.py` touches **only** the `check_orbit_texture`
  docstring — 4 lines removed, 15 added, `0` code lines changed. Behaviour byte-identical. ✓
* `experiments/aeh_basecase.py` carries the repo's `Run: … (date: …)` header and names the page and results
  it supports; `import sys` is indeed absent. ✓
* No change log, dated journal or branch narration entered a tracked page. The two dated strings added to
  `aeh.md` are `Verified — … 2026-08-02` lines, which `AGENTS.md` explicitly requires. One borderline phrase:
  `13.2` says *"The horizon does the job the bulk cut **used to do**"* (the paper's version, *"the job a bulk
  cut would do"*, is cleaner). Cosmetic.

---

## 3. The round's own claims, checked

1. **The equivalence overclaim.** Under Option 1, `13.2.1` is stated at every finite block length, `13.6.4`
   is a genuine equivalence, and (q1) has been narrowed to say that the `L = 1` *marginal* is strictly weaker
   — not that AEH is. So the sites that assert "AEH ⟺ bulk Bernoulli-genericity of the door letter word"
   are now **true where they stand**: `anchors.md` L59, `index.md` L46, `HANDOFF.md` L20, `bridge.md` L69,
   `itinerary.md` L73, `aeh.md`'s front matter and Current state, `13.6.6`, `13.6.7`, `publication.md` L44.
   I found **no surviving site that contradicts (q1)**.
2. **The Inselmann conversion is circular.** Confirmed at the source — §2.8. The one blemish is D8's
   complement slip on "pattern `11`", which does not touch the argument.
3. **The bulk cut binds.** Confirmed exactly — §2.4, including the arithmetic check the brief specifies.
4. **The density inference was false.** `Bad_N = [N, N(1 + 1/log N))` has density `1/log N → 0` in each
   `[N, 2N)` and unions to every large integer — the counterexample is correct. `13.2.5`'s proof is correct
   as written (`#{x ∈ Bad : x ≤ X} ≤ C + η Σ_{b≤B} 2^{b−1} ≤ C + ηX`, upper density `≤ η` for every `η`), and
   its use is consistent: `13.3.1`, `13.3.3`, `13.6.6` and paper L301–304 all now route the "almost every
   integer" reading through shell scale. `bridge.md` L69 is the one page that still says "density-zero set of
   starting values" flatly (D3).
5. **Base case and the `1/4` barrier.** Reproduced and re-derived — §2.1, §2.2.
6. **The depth marginal did not move.** Reproduced in exact rationals from my own derivation, and
   cross-checked against Tao's printed table — §2.3.

---

## 4. Verdict on (a), the unbriefed proof edit in `13.6.4`(⇐)

The added parenthetical: *"the capped labels are coordinates of `W_{k,D}`, and each letter is read off exactly
once `D` exceeds its components, the definition quantifying over every `D`"*.

**Is it true?** Yes, as a pointwise statement. Letter `n = (σ_n − s_n, s_{n+1})`, and `W_{k,D}` carries
`min(σ_n, D)`, `min(s_n, D)`, `min(s_{n+1}, D)`. When all three are strictly below `D` the letter is recovered
exactly; when any is capped it is not.

**Was it necessary?** **Yes, and it repairs breakage this round introduced.** Before the round, `13.6.4`'s
proof read *"(13.6.3(i); the labels are part of every depth-`k` window)"* and the window carried the **exact**
labels `(s, σ, a₊)`, so the sentence was true as stated. Delegate A's restatement introduced the cap `D`,
which made *"letters are exact functions of consecutive labeled window states"* **false at fixed `D`**. The
parenthetical is the minimal repair of a defect the round created, not an improvement of a pre-existing
proof — which is the right side of `AGENTS.md`'s line, and the delegate flagged it either way.

**Is the proof correct with it?** The theorem is correct, but the parenthetical does not finish the argument.
`s_n` is the *previous* letter's `r`-component, so for a **fixed** letter pattern `w` the relevant window
labels are still unbounded: the event `{letters n…n+L−1 = w}` is not a union of `W_{k,D}`-block cells at any
single `D`. What closes it is the extra step

```
|bulk freq(w) − B[w]|  ≤  freq({min(s_n, D) = D})  →  π_{k,D}({s ≥ D}) = 2^{-(D-1)},  for every D,
```

i.e. `D → ∞` against the cap's tail cell. That step is not on the page. The (⇒) direction of the *same*
proof does write its analogous bound out (*"off an exceptional event of `B`-mass `≤ 2L(0.93)^W` … hence to
it exactly"*), so the asymmetry is visible.

**Recommendation:** keep the parenthetical (it is true and the proof is worse without it) and, in a
content commit rather than an organizational one, add one clause to (⇐) mirroring (⇒) — the residual is the
cap's tail cell `{s ≥ D}`, of `π_{k,D}`-mass `2^{-(D-1)}`, and the definition quantifies over every `D`.

---

## 5. Verdict on (c), the Appendix A pin

Appendix A (PDF **p. 16**) reads *"every wiki section and script named in this paper is cited at commit
`b278e5a`."*

* **Is the sentence true?** Yes. `b278e5a` contains `9d160d8` (`experiments/aeh_basecase.py`), `a1e1701`
  (`aeh.md` `13.2.3`, `13.2.4`, `13.2.4.1`, `13.2.5`, `13.6.4` and the rest) and `957f6cb` (`publication.md`).
  Those are every wiki section and script the paper names. The paper cites no `paper/` path, so the sentence
  is not self-referential and does not fail.
* **Is the pin honest?** **No, not as the repository has always meant it.** A reader who checks out
  `b278e5a` gets a working tree in which `paper/collatz-reduced-v3.tex` is the **pre-round** paper — no
  capped window, no base case, no `π_{k,D}` — and in which Appendix A itself prints **`c2d465a`**. The pin
  points at a snapshot that contradicts the document carrying it. That is exactly the situation `3511a0d`
  ("Appendix A record pin: `6a9183a` → `c2d465a`, the commit that contains the round") and `643e864` were
  created to fix.
* **Which commit should it name?** A commit that contains **both** the record and this paper — i.e.
  `fa07929` if the branch fast-forwards, or the merge commit if it does not. That requires the same one-line
  follow-up commit the two precedents made, after this round lands. The paper delegate's own §6 caveat says
  this correctly and declines to make the commit, which was the right call for an apply delegate.
* **One extra risk the delegate did not name:** `b278e5a` is a branch commit. If the branch is squashed or
  rebased at merge, the pin dangles entirely. `c2d465a`, the pin it replaces, is on `main`.

**Verdict: needs a follow-up.** Merging as-is ships a paper pinned to a commit at which the paper is not the
paper. The fix is one commit and one token.

---

## 6. Rendered-layout report

Rebuilt from the committed `.tex`, rendered all 17 pages to PNG at 110 dpi with `pdftoppm`, and **looked at
every page**. Result: **no layout defect.** Specifically, none of: an overfull line, a broken or split
display, a widow, an orphan, a section heading stranded alone at a page foot, a mis-set fraction, a mangled
math symbol, or a cross-reference rendering as `??`.

Page by page, the material the round touched:

| page | content | note |
|---|---|---|
| 1 | title, abstract, start of version note | Abstract's new letter-genericity sentence sets cleanly to the foot; footnote rule and author footnote correct. |
| 2 | version note, entire | One paragraph filling the full text block. ~1.5 in of white below it because the "Author's note" heading could not fit — ordinary LaTeX behaviour before a `\subsection*`, not a defect. |
| 3 | Author's note, §1 opens, Contributions | Clean. |
| 4 | §1 close, **Related work** (new Inselmann/step-unit sentence) | Dense but clean; the new sentence sets without a bad break. |
| 5–9 | §2–§4 | Unchanged material, reflowed. Clean throughout; `thm:onestep` on p. 8 shows the `π_{k,D}` rename correctly. |
| 10 | Thm 4.6, Note added in v2 | Clean; the `p ∈ {2,…,23}` display centred correctly. |
| 11 | Correction paragraph, **§5 opens** | §5's heading sits at roughly two-thirds down with 4 lines of body following — fine. The new Tao/`Syrac(Z_3)` paragraph sets cleanly, fractions `2/3`, `19/63`, `2/63`, `1/3`, `20/63` all correct. |
| 12 | capped-window display, `π_{k,D}`, **Hypothesis 5.1** | The `W_{k,D} = (ω mod 2^{k+2}, d ∧ D, s ∧ D, σ ∧ D, a₊ ∧ D)`, `u ∧ D := min(u,D)` display is on one line and correct. The tally display and the `2/N #{…} → 0` display both set cleanly; the hypothesis environment does **not** break across the page. |
| 13 | `B[w]` line, window form, one-limit, budget/admissible | The `\dagger` symbol renders; "admissible means both" present; the `4θ < τ < 1` / `4θ < τ < 4.8188…` prose renders inline without overflow. |
| 14 | **the base-case two-part display**, clock, ledger, shell scale | This is the display that overflowed on the delegate's first build. It now sets on **one line** inside the margins: `‖Law(ℓ_0,…,ℓ_{n−1}) − B^{⊗n}‖_TV ≤ 2^{J+2}/N + P_B(S_n ≥ J), P_B(S_n ≥ J) = P(Bin(J−1,½) < 2n)`. No overflow, no break, both halves legible. |
| 15 | descent, **Calibration** + two ceilings, Lemma 5.2, **§6 opens** | Both ceilings print (`L = 1` and `L = 2`; the pooled-versus-per-start scope with `‖ν − π_{k,D}‖_TV`). §6's heading falls near the foot with **two** lines under it — tight but within LaTeX's own club/widow tolerance. Cosmetic only. |
| 16 | §6 close, **Appendix A** with the `b278e5a` pin, refs [1]–[9] | Pin renders as `b278e5a`. Clean. |
| 17 | refs [10]–[18] | Ends at ~one-third page; normal. |

The one underfull box in the log (`badness 1067`, tex `470--471`) is the pre-existing `rhin` bibliography
entry on p. 17; it is invisible at reading size.

---

## 7. Verdict on the biased-number list

**Broadly correct, and correct on the hard part.** I re-read the code behind every entry rather than taking
the list's word:

**List B ("verified *not* under any cut") — all four entries confirmed by reading the source:**

* `merle_aeh_key_check.drift_fixed_horizon` takes `trans[:horizon]` unconditionally — no cut. ✓
* `aeh_anomaly.py` — I grepped the whole file; the only `1 <<`-style constants are in `step()`. No cut. ✓
* `check_two_sided_reconstruction` (seed `31003`) — random odd `w < 2^60`, no altitude filter. ✓
* `check_pushforward` / the exhaustive counts — sampling only, no cut. ✓

**List A row 4 is more precise than it needed to be and is right:** `merle_aeh_key_check.skeleton_and_spectrum`
does `if x <= cut: continue` on `x` — the **exit/door**, not the core, exactly as the list says.

**Two small gaps:**

1. **`13.1`'s printed `P(ω ≡ 1 mod 32 | class (1,2)) = 0.499`** is the same complement-of-the-core-cut
   selection as row A2, printed on a different page section, and is not named. Low stakes (the page's point
   is that these are "digits of specific small numbers, not samples from a measure"), but the list is
   site-indexed and this site is missing.
2. **`13.4` bullet 3** — *"the `(class, d)`-chain reproduces the orbit `d`-law to `~1%`"* — is a measured
   comparison. I read the code: `aeh_calibration.py` E1'/E2', 90-bit starts, 160 steps, `break` at `(1,1)`,
   **no cut**. So it correctly does *not* belong on list A. But it has exactly list item C's protocol defect
   (whole orbits, a stopping rule, no bulk/bottom separation) and is not flagged there. One line in item C
   would close it.

**One value the list correctly leaves off, verified:** `13.2`'s *"measured exponent per block is `4.0017`"*
is the no-cut mean of `m + s` over the 30 tallied blocks (`3.9782` under the core cut). Cut-free. ✓

**Nothing on the list is actually cut-free.** Rows A1, A2, A4(complement), A5 are all genuinely selected.

**Where I can bound the effect (row A5, `13.6.5`'s orbit adjudication):** re-running the same seed with and
without the cut (§2.5) gives:

* `L¹ ≤ 0.006` over `d ≤ 5` — **survives, and improves**: `0.0052` cut, `0.0024` cut-free. Can come off the
  list.
* the chain-law rejection at `≈ 14–15` pooled SE — **survives**: offset `0.0176` cut, `0.0170` cut-free.
  Can come off the list.
* `P(ω₊ ≡ 1 mod 3 | a₊ = 0) = 0.6662 ± 0.0015` — bias `−0.0011`, **inside the printed error bar**; verdicts
  move from `0.3σ` to `1.1σ` from `2/3` and from `112σ` to `~110σ` from `1/2`. Neither verdict is touched,
  exactly as `13.6.5` already says. Can come off the list, or be reduced to a footnote.
* `P(d=2) = 0.3192` — **stays**: cut-free it is `0.3185`, so the bias moves the fourth printed decimal. This
  is the one value whose bias is *not* below its quoted precision.
* `154,389` tallied visits — definitionally the cut's own count; cut-free the run has `158,580`.

**So row A5 reduces from five items to two** — `P(d=2)`'s last digit and the visit count — and neither needs
a re-run, only a footnote. That is the useful shape for the author's decision.

**One measurement the author may want, not on the list:** under the flagship bulk protocol the 3-gain rate is
`0.3314 ± 0.0012` cut-free and `0.3284` under the core cut — a `−0.0030` (`2.5` across-orbit SE) bias on
exactly the statistic `13.3.2` is about. `13.3.2`'s printed `0.3352` comes from the *other*, cut-free protocol
(list item C), so it is unaffected; but this quantifies why the core cut is the wrong coordinate here, and it
is a cheap number to have in hand.

---

## 8. The two apply deviations lists, checked against the files

**Record delegate's 11 (its §5).** Items 1, 2, 3, 4, 5, 6, 7, 9, 10 are all present in `aeh.md` exactly as
described and are all consequences of a named design finding; item 11 (`import sys` removed) is correct;
item 8 is D5 above. Nothing in the list is a change the files do not show, and nothing in the diff is a
change the list does not mention. **Two of them deserve the author's eye:** item 1 (the front-matter `PROVED`
clause, which triggers D4's unexecuted workflow steps) and item 8.

**Paper delegate's 10 (its §5).** Verified in the rendered PDF and the `.tex`:

| item | check |
|---|---|
| 1 abstract restated | p. 1 — *"the block letters of uniformly sampled large starts carry, at every finite block length, the frequencies of an exactly computable Bernoulli law … exhibit an unconditional base case inside the digit budget"*. Consistent with §5 and `13.2.4`. ✓ |
| 2 version note | Present; content accurate; the "no was-X-now-Y" self-claim is false — **D9**. |
| 3 footnote-4 attribution | Present at p. 12 — **D1**. |
| 4 class-skeleton refers back | p. 12, *"the transition from `(ω ≡ 1 (8), d odd)` cited above holds because `m₊ = 1` and `a₊ = 0` there"*. Both facts survive, repetition gone. ✓ |
| 5 `w_i = (m_i, r_i)` defined | p. 13, first line. ✓ |
| 6 "in the sense defined below" | p. 13. ✓ |
| 7 "below the cap" / "of vanishing density" | p. 15, both. ✓ Consistent with `13.2.5`. |
| 8 §5's opening question | p. 11, *"What is the right comparison object?"* ✓ |
| 9 display-spacing fix | `0` overfull boxes in my own build; the display sets on one line at p. 14. No symbol moved. ✓ |
| 10 Appendix A pin | **D6**. |

And its §3 disagreements D1–D10: I checked D5 (`O(N^{-δ})`, against Inselmann Def 2.6 — correct), D6
(`thm:onestep`, verified by independent environment diff — a rename only), D7, D8, D9 (all present), and D1
(commit `3213f0d` does contain the drift-clause fix, so the brief's G3 was indeed stale). **All ten are
accurate.** The apply phase's least-reviewed edits came through clean; the round's defects are elsewhere.

---

## 9. What I could not check

Named plainly, as the brief requires.

1. **The published *Forum of Mathematics Pi* text of Tao.** I read arXiv v4, v5 and v7. D1's conclusion rests
   on v5 being the version that corresponds to the 2022 journal publication (dates and content match), but I
   did not obtain the Cambridge PDF. If the journal version happens to carry the ancient-iteration footnote
   as footnote 4, D1 dissolves — the check is one download.
2. **Merle's independent replication** (`13.4` bullet 4: `|λ₂| ≤ 0.06`, our `0.028/0.036`). I read
   `merle_aeh_key_check.py` to confirm the cut coordinate but did not re-run it, and I have no access to his
   implementation.
3. **The eight-round calibration campaign** (`13.4` bullets 1–2, `13.5`'s opening `0.2677 / z = 5.0 / 2,610`
   orbits). I did not re-run `aeh_calibration.py`; those remain as the record has them, under the protocol
   the list flags.
4. **`13.6.3`(iv)'s `2·(0.93)^j` bound under `B̂`.** Delegate A's open question 3, which both apply delegates
   left open and which `13.2.4`(e) and `13.6.4`(⇒) both consume. I did not re-derive it. Still open, and it
   is a *proof* dependency of the new lemma, not a cosmetic one.
5. **The composite five-coordinate labelled reconstruction as one test** (A's open question 4). Still open;
   `13.6`'s verification block still describes the two-coordinate test it actually runs.
6. **The `θ`-frontier claim that `13.2.4` is *empty* at `θ = 1/4` exactly**, and `13.2.4`(f)'s
   non-uniformity claim. I verified `I(1/4) = 0` analytically and numerically, but did not attempt to
   confirm that no other argument rescues the endpoint.
7. **`13.2.4`(e)'s proof in detail.** I checked its structure and that `13.2.4`(d)'s McDiarmid step is right,
   but I did not verify the `ε' = 2ε/|A_{k,D}|^L` bookkeeping or the union bound over
   `|A_{k,D}|^L · Λ^{2P}` events line by line.
8. **Zenodo DOI `10.5281/zenodo.21730505`.** I did not check that it is reserved and unpublished; the paper
   and `publication.md` both assert it.
9. **The Mazur watch item** in `publication.md` (proofatlas.ai, no arXiv, no DOI). Not fetched; the page says
   nothing rests on it.
10. **`archive/`, `cycles.md`, `reverse.md`, `ladder.md`, `spine.md`, `stage2–4.md`** were checked only by
    targeted grep for AEH-related stale phrasing, not read end to end. The cross-page pass in §1 is
    grep-complete for the phrases the round retired, not a full reading of every page.
11. **`experiments/aeh_basecase.py`'s C2 lemma-bound column** (`lemma_bound 0.337`, `0.2745`, …) — the
    measured `TV` is well under it everywhere, but I did not re-derive the bound's own constant.
