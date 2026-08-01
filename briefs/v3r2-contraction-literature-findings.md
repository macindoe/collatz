# Findings: does AEH's contraction consequence sit below the unconditional literature? (v3 round 2)

**Task:** `briefs/v3r2-contraction-literature-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `e4dac49`, working tree clean apart from the round-2 briefs.
**Method note.** Every statement below marked **[P]** was read by me from the primary source itself (the paper's own PDF, retrieved this session and read page by page). **[S]** marks something taken from a secondary description — an abstract, another author's summary, an encyclopedia entry. **[?]** marks something I could not confirm. Transcriptions of formulas from scanned or rendered pages are mine; where a scan was marginal I say so.

---

## 0. Verdict in one paragraph

**The contraction half is subsumed — decisively, and not by any of the three papers the brief named.** The relevant result is **Inselmann, arXiv:2402.03276 (v3, 13 Aug 2024)**, which the repository does not cite and which no round of this project has seen. His Corollary 1.4 is, verbatim in content, the restated AEH descent corollary: *for every fixed `ε > 0`, almost all `m` in **natural** density satisfy `T^{⌊log₂m/(1−log₂√3)⌋}(m) ≤ m^ε`* — unconditionally, in natural density, at a horizon linear in `log m`. His Theorem 1.1/1.10 is strictly stronger still: a **two-sided** trajectory envelope `(3/4)^k m^{1−ε} ≤ Syr^k(m) ≤ (3/4)^k m^{1+ε}` holding *simultaneously for all* `k` up to `(log₂⁴⁄₃)^{-1} log₂ m`. And the numbers are not merely comparable to ours, they are **ours**: Inselmann's classical starting horizon `α = (log 2)^{-1} ≈ 1.443` is exactly `θ = 1/4` blocks per bit, his maximal horizon `α = 2(log ⁴⁄₃)^{-1} ≈ 6.952` is exactly `θ = 1/β = 1.2047` blocks per bit, and their ratio `4.8188` is the reformulation findings' own `4.819`. Inselmann's paper *is* the crossing of the frontier that `briefs/v3r2-aeh-formulation-findings.md` §4 identifies and §9 item 2 leaves open — for the first-moment statistics. **The ledger half is split.** Its first moment (odd steps occupy half the schedule; equivalently `E[s] = 2`) is also unconditional to the full horizon, by his Theorem 1.6. Its *distributional* content — the full `2^{-j}` marginal at every `j`, the `1/3` rate, the depth law, `π_k` as a measure — is classical only within the digit budget (Terras) and I found nothing carrying it past. **That residue is where AEH's content actually lives, and the paper should be reframed onto it.** On density: **natural**, unambiguously — every neighbour in this genre is stated in natural density, natural-density-one implies logarithmic-density-one but not conversely, and Tao's reason for preferring logarithmic density is an iteration property our statement explicitly does not use. Korec, Tao **and Inselmann** should all be cited; Inselmann is the one that is not optional.

---

## 1. What each external result actually says

### 1.1 Terras (1976) — already cited as `\bibitem{terras}` **[P]**

Read in full from the ICM scan of *Acta Arith.* 30 (1976), 241–252 (`http://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf`). Terras's `T` is the one-division map `Tn = (3^{X(n)}n + X(n))/2`, i.e. `(3n+1)/2` on odds and `n/2` on evens.

* **Definition 0.1** (p. 241): `χ(n) = k` if `k` is the smallest positive integer with `T^k n < n`; `χ(n) = ∞` if no such `k` exists. This is the **stopping time**.
* **The stated principal result** (p. 241): "*The principal result of this paper touching on this problem is the demonstration that `χ` possesses a well defined distribution function*" `F(k) = lim_{m→∞}(1/m)·μ{n ≤ m | χ(n) ≥ k}`, "*where `μ` denotes the counting function*", and "*it shall be demonstrated that `lim_{k→∞} F(k) = 0`*."
* **Theorem 1.11** (p. 245): that limit exists for each `k` and equals `P[τ ≥ k]`. **Theorem 1.17** (p. 247): "*The sequence `F(k)` converges monotonely to `0`*", proved by a central-limit estimate on `Σ_{a≤[k(1−γ)]} C(k,a) 2^{-k}` with `γ = ln2/ln3`.
* **Density used: natural (asymptotic).** `F(k) = lim (1/m) μ{n ≤ m | …}` is a counting ratio. There is no logarithmic weighting anywhere in the paper.
* **Theorem 1.2 (Periodicity)** (p. 242): "*Two positive integers `n` and `m` have same encoding vectors `E_k(n) = E_k(m)` if and only if `n ≡ m mod 2^k`.*" **Corollary 1.3**: for fixed `k`, `n ↦ E_k(n)` is periodic with period `2^k` and assumes all `2^k` values. **Corollary 1.4**: `X_0, X_1, …` "*constitutes a family of independent random variables*", each parity pattern of length `k` having density exactly `2^{-k}`.

**What this is, in our terms.** Corollary 1.3 is `itinerary.md` `14.15.1.5` in parity coordinates — the project's own identification, already recorded at `publication.md` L19 and L40, is correct. Corollary 1.4 is the exact base case the reformulation findings §4 rebuilt in door coordinates. The density consequence is descent **below the start**, in natural density, in a number of steps that is bounded *independently of `n`* for all but any prescribed density `ε` (this is what `F(k) → 0` says) — stronger in time than `O(log n)`, but reaching only `n` itself, not `n^θ`.

### 1.2 Allouche (1979) **[S]**

Not read. Two secondary attributions, which disagree with each other in a way worth recording:

* Korec's own text (p. 86) **[P]**: a referee informed him "*a similar result is contained also as a special case in [1], with however a larger bound `3/2 − log₃2 = 0.86907…` for `c`*". `3/2 − log₃2` does evaluate to `0.86907`.
* Tao (p. 2) **[P]** and Inselmann (p. 4) **[P]** both print the threshold as `3/2 − log 3/log 2` resp. `3/2 − log₂3`, which evaluates to `−0.085`, not `0.869`. Mazur's footnote 1 flags the same discrepancy and follows Korec's form.

**Take Korec's form.** The Allouche threshold is `3/2 − log₃2 = 0.86907…`; the expression printed in Tao and Inselmann is a typo propagated between them. Reference details (`Séminaire de Théorie des Nombres`, Bordeaux/Talence 1978–79, Exp. No. 9) come from a search summary **[S]** and should be checked against a library record before being printed.

### 1.3 Korec (1994) — the `0.7924` result **[P]**

Read in full from the DML-CZ scan of *Math. Slovaca* **44** (1994), no. 1, 85–89 (`https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf`).

* **Abstract**: "*The set of those initial values `y` for which a value less than `y^{0.7925}` is eventually reached after several steps of the algorithm from the `3x+1` problem … has asymptotic density 1.*"
* **Theorem 1**: "*For every real `c > log₄3` (`= 0.79248125…`) the set `M_c = {y ∈ N | (∃n)(T^n(y) < y^c)}` has asymptotic density 1.*"
* **Density used: natural.** Defined on p. 85 as `lim_{x→∞} card{y ∈ M | y < x}/x`.
* **Horizon** (p. 86, immediately after the theorem): "*Notice that `n` in (2) is not bounded (as we shall see from the proof, it could be bounded by `log₂ y`, but it could not be bounded independently of `y`).*" So Korec's result already carries an `O(log y)` horizon, and already knows that horizon is necessary.
* **Mechanism.** Lemma 1 is Terras's periodicity theorem quoted verbatim (`E_m(x) = E_m(y) ⟺ x ≡ y mod 2^m`); Lemma 2 is a central-limit statement that `U(m,d)/2^m → 1` for `d > 1/2`, where `U(m,d)` counts parity words of length `m` with at most `md` ones. The proof runs `m` parity steps from a start of size `≈ m²·2^m`, i.e. **exactly one parity step per bit of the start**, and needs `k/m ≤ d` with `d = ½(c/log₄3 + ½) > ½`, which is where `c > log₄3` comes from.

**This is our §4 argument, with the same threshold, arrived at independently.** The reformulation findings' base case runs the cylinder count to `S ≈ L`, i.e. to the exhaustion of the start's `2`-adic digits, and yields descent to `2^{L(1 − β/4)}`. That exponent is **exactly** Korec's:

```text
1 − β/4  =  1 − (2(2 − log₂3))/4  =  log₂3 / 2  =  log₄3  =  0.7924812503605781
```

verified to 16 digits by direct computation this session. The identity is algebraic, not numerical coincidence, and it means the project's `θ < 1/4` frontier and Korec's `c > log₄3` frontier are the same wall seen from two sides.

### 1.4 Tao (2019 / 2022) **[P]**

Read from arXiv:1909.03562**v7** (16 Jul 2026), pp. 1–5 and 9–12. Journal ref: *Forum Math. Pi* **10** (2022), Paper No. e12, 56 pp.

* **Theorem 1.3**: "*Let `f: ℕ+1 → ℝ` be any function with `lim_{N→∞} f(N) = +∞`. Then one has `Col_min(N) < f(N)` for almost all `N ∈ ℕ+1` (in the sense of logarithmic density).*" `Col_min(N) := inf_n Col^n(N)`, the minimum over the whole orbit.
* **"Almost bounded"** means exactly this: the threshold may grow arbitrarily slowly (`log log log N` is his own example), but not be constant. **Remark 1.4** explains why constant is out of reach and notes Theorem 1.3 is equivalent to: for every `δ > 0` there is `C_δ ≪ exp(δ^{-O(1)})` with `Col_min(N) ≤ C_δ` on a set of *lower* logarithmic density `≥ 1 − δ`.
* **Density used: logarithmic**, and deliberately. Definition 1.2 defines it via the logarithmically-uniform random variable `Log(R)`. His stated reason (p. 2): "*For technical reasons, the notion of 'almost all' that we will use here is based on logarithmic density, which has better approximate multiplicative invariance properties than the more familiar notion of natural density.*"
* **Prior art, in his words** (p. 2): "*In Terras [21] (and independently Everett [8]) it was shown that `Col_min(N) < N` for almost all `N`. This was improved by Allouche [1] … the range of `θ` was later extended to `θ > log3/log4 ≈ 0.7924` by Korec [9]. (Indeed, in these results one can use natural density instead of logarithmic density to define 'almost all'.)*" — primary-source confirmation that the whole pre-Tao line is natural density.
* **No time bound.** Theorem 1.3 is about `Col_min`, the infimum over the entire orbit; the statement carries no horizon. (Section 5.1 of his local argument does carry a `⌊log x/(10 log 2)⌋` first-passage time, but the global theorem does not.)
* **Remark 1.16**, the natural-density question, verbatim: "*In order to upgrade logarithmic density to natural density in our results, it seems necessary to strengthen Proposition 1.14 by establishing a suitable fine scale mixing property of the entire random affine map `Aff_{Geom(2)^n}`, as opposed to just the offset `F_n(Geom(2)^n)`. This looks plausibly attainable from the methods in this paper, but we do not pursue this question here.*"
* **The non-iteration obstruction, with a citation attached** (p. 2): "*one runs into the difficulty that the uniform (or logarithmic) measure does not enjoy any invariance properties with respect to the Collatz map: in particular, even if it is true that `Col_min(N) < x^θ` for almost all `N ∈ [1,x]`, and `Col_min(N') ≤ x^{θ²}` for almost all `N' ∈ [1, x^θ]`, the two claims cannot be immediately concatenated … since the Collatz iteration may send almost all of `[1,x]` into a very sparse subset of `[1,x^θ]`.*" This is `13.3.3`'s and the reformulation findings' §8 item 7 "the consequences do not iterate", stated by Tao for the same reason. **It should be cited there rather than presented as an in-house observation.**

**One incidental lead, flagged not established [?].** Tao's **Remark 1.13** introduces `Syrac(ℤ₃)`, a `3`-adic random variable that is "*the unique stationary measure for the discrete Markov process on `ℤ₃` that maps each `x ∈ ℤ₃` to `(3x+1)/2^a` … with transition probability `2^{-a}`*", and computes `Syrac(ℤ/3²ℤ)` as `0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63`. Our exact bulk absorption law (`aeh.md` `13.6.5`) is `P(a=0) = 2/3 = 42/63`, `P(a=1) = 19/63`, `P(a≥2) = 2/63` — **the same denominator `63`, and `2/63` appears in both lists**, and both are exact stationary `3`-adic laws for the same iteration with the same `2^{-a}` weights. I did **not** verify an identification and did not attempt the computation. If `13.6.5`'s `ν` is Tao's `Syrac(ℤ₃)` pushed through `v_3(· + 1)`, that is a genuine prior-art contact for a law the paper currently presents as computed in the project record, and it needs a dedicated check before the AEH section is finalized. **This is the largest unexamined risk I am leaving on the table.**

### 1.5 Inselmann (2024) — the result that settles the question **[P]**

*An Approximation of the Collatz Map and a Lower Bound for its Average Total Stopping Time*, Manuel Inselmann, arXiv:2402.03276, v1 5 Feb 2024, v3 13 Aug 2024. math.DS/CO/NT/PR. **No journal reference listed** — it is an arXiv preprint, not (as of this session) a refereed publication. Read pp. 1–6 from the arXiv PDF. Same one-division `T` as Terras.

* **Abstract** (transcribed): "*Results of Terras and Everett imply that, given any `ε > 0`, almost all `m ∈ ℤ⁺` (in the sense of natural density) fulfill `(√3/2)^k m^{1−ε} ≤ T^k(m) ≤ (√3/2)^k m^{1+ε}` simultaneously for all `0 ≤ k ≤ α log m` with `α = (log 2)^{-1} ≈ 1.443`. We extend this result to `α = 2(log ⁴⁄₃)^{-1} ≈ 6.952`, which is the maximally possible value.*"
* **Theorem 1.1**: the set of `m` such that for **all** `0 ≤ k ≤ log₂m/(1 − log₂√3)`, `(√3/2)^k m^{1−ε} ≤ T^k(m) ≤ (√3/2)^k m^{1+ε}`, **is of natural density 1**.
* **Corollary 1.4**: the set `{m ∈ ℤ⁺ | T^{⌊log₂m/(1−log₂√3)⌋}(m) ≤ m^ε}` **is of natural density 1**, for every `ε > 0`.
* **Theorem 1.6** (the first-moment ledger): the set of `m` such that for all `0 ≤ k ≤ log₂m/(1−log₂√3)`, `−ε log₂m ≤ Σ_{i<k} p(m)_i − k/2 ≤ ε log₂m`, **is of natural density 1**. (`p(m)_i` is the parity of `T^i(m)`.)
* **Theorem 1.9** (raw Collatz `Col`): same envelope with rate `(∛(3/4))^k` out to `3 log₂m/(2 − log₂3)`.
* **Theorem 1.10** (odd-to-odd Syracuse `Syr(m) = (3m+1)/2^{v₂(3m+1)}`): the set of odd `m` such that for all `0 ≤ k ≤ (log₂⁴⁄₃)^{-1} log₂ m`, `(3/4)^k m^{1−ε} ≤ Syr^k(m) ≤ (3/4)^k m^{1+ε}`, **is of natural density 1 in the odds**.
* **Density used: natural**, throughout, defined on p. 2 by `liminf_{n→∞} #{m ∈ A | m ≤ n}/n = 1`.
* **His own comparison** (p. 4, discussion of Question 1.5): "*Allouche showed the answer … is positive for all `f_θ` with `θ > 3/2 − log₂3`. Korec extended this result to all `f_θ` with `θ > log₂√3`. Recently, Tao answered Question 1.5 positively for all functions … with natural density replaced by logarithmic density … As there are subsets of `ℤ⁺` with logarithmic density 1 and lower natural density 0 …, it would be desirable to get Tao's result for natural density as well. Corollary 1.4 implies that the answer to Question 1.5 is positive for `f_θ` for any `θ > 0`, thus extending Korec's result to all `f_θ` with `log₂√3 ≥ θ > 0`, and improving Tao's result for these functions by replacing logarithmic density with natural density.*" He adds that his methods seem unlikely to reach arbitrary diverging thresholds.
* **Method** (§1.2): `∗`-dense sets — sets whose density in every dyadic-type window is `1 − O(N^{-D})` — combined with the Terras periodicity/fair-coin input, plus a push-forward property (his (1.1) and (1.5)) letting the property survive one application of `T^{⌊log₂m⌋}`. Iterating that push-forward is what extends `k` from `log₂m` to `(Σ_i (log₂√3)^i) log₂m`, and in the limit to `log₂m/(1 − log₂√3)`. **Note: `∗`-density is strictly stronger than natural density 1 — he says explicitly "sets of natural density 1 do not have this property" — and it is the strengthening that makes the iteration legal.** That is the technical answer to Tao's non-invariance obstruction, and to ours.

#### 1.5.1 Why this is our own frontier, in our own numbers

Every horizon in Inselmann's paper converts into the reformulation findings' coordinates exactly. Computed this session:

| Inselmann | his units | per bit of start | in our blocks/bit | our name for it |
|---|---|---|---|---|
| classical range, `α = (log 2)^{-1} = 1.443` | `T`-steps per `ln m` | `1.000` `T`-steps | `0.250` | **`θ = 1/4`, the digit budget (§4)** |
| his extension, `α = 2(log ⁴⁄₃)^{-1} = 6.952` | `T`-steps per `ln m` | `4.8188` `T`-steps | `1.2047` | **`θ = 1/β`, the full descent** |
| ratio | — | `4.8188` | `4.8188` | **§4's `1.2047/0.25 = 4.819`** |
| Thm 1.10 horizon `(log₂⁴⁄₃)^{-1}` | `Syr`-steps per bit | `2.4094` | `1.2047` | same, at `E[m] = 2` `Syr`-steps per block |
| Thm 1.9 horizon `3/(2−log₂3)` | raw `Col`-steps per bit | `7.2282` | `1.2047` | same, at `1.5×` raw-to-`T` |
| rate `(3/4)^k` per `Syr`-step | — | `−0.41504` bits | `−β = −0.83007` /block | the classical drift of `13.3.2` |

The conversions use `σ = 4` parity steps per block and `E[m] = 2` Syracuse steps per block — the same `E[m+r] = 4` accounting as §4. Nothing is approximate here: `1 − β/4 = log₄3` and `(1/β)/(1/4) = 2(log⁴⁄₃)^{-1}/(log 2)^{-1} = 4.8188…` are identities.

So: **the reformulation findings' §4 is a correct rediscovery of the classical unconditional range, its §9 item 2 ("how far past `θ = 1/4` does the base case extend? I could not find the barrier") is answered by the literature — all the way, and there is no barrier — and the technique that crosses it is `∗`-density, not a sharper cylinder count.**

### 1.6 Mazur (2026) — a claimed natural-density Tao, status uncertain **[P] for what it claims, [?] for whether it holds**

*Natural-Density Almost-Bounded Collatz Orbits in Logarithmic Time*, Lech Mazur, "Version 2, July 21, 2026". Hosted only at `proofatlas.ai` (`/papers/natural-density-log-time-collatz/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf`). **Not on arXiv, no DOI, no journal, not refereed.** Read pp. 1–4.

* **Theorem 1.1(ii)**: with `C_Coll = 1509503/(5000 log 2) < 436`, for every `f → +∞`, the `N` for which some `m ≤ C_Coll log N` has `Col^m(N) < f(N)` **have natural density one**. (i) is the Syracuse version with `C_Syr < 145` at relative natural density one among the odds.
* **Corollary 1.3**: `log N/(2 log 2) < m ≤ 436 log N` with `Col^m(N) < √N`, so the `log N` order is optimal up to a constant.
* This is exactly Tao's Remark 1.16 programme and Inselmann's Question 1.5; the route is a natural-counting/logarithmic transport comparison closed by **Rhin's irrationality measure for `log₂3`** — the same `\bibitem{rhin}` the paper already carries, used at a different point.
* **Generative-AI disclosure, verbatim from the paper**: "*Generative AI played a substantial role in mathematical exploration, proof development, formalization, computation, and exposition. The agentic environments used included a custom harness, OpenAI Codex, and Anthropic Claude Code; the models used included GPT-5.5 and Fable 5. Lech Mazur designed the harness, curated and reconciled the outputs, and takes responsibility for the manuscript. The formal claims rest on the frozen Lean artifact identified below.*" Frozen Lean commit `f386357d453ac4dcf91242b76252d88a5a729906`; the site reports the build as complete and sorry-free, with a precursor formalization of Tao's own theorem at 397 files / 124,019 lines.

**How to treat it.** A sorry-free Lean 4 proof is strong evidence about the *formal* statement; it is no evidence at all that the formal statement says what the prose says, which is precisely the failure mode for a result this size claimed outside the refereed literature eleven days ago. **My recommendation: do not cite it in the paper and do not rest one word on it.** It changes nothing in the verdicts below, because Inselmann alone already subsumes our consequence. Record it on the wiki as a watch item. It is also, incidentally, an exact methodological precedent for this project's own register — disclosed AI role, named human responsibility, frozen artifact — and if the author ever wants a second precedent alongside `\cite{llmcollatz}` and `\cite{merle}`, this is one.

---

## 2. Natural versus logarithmic density: the crux, settled

Three facts, in the order they matter.

1. **Natural density one implies logarithmic density one; the converse is false. [S for the forward direction, [P] for the converse]** The forward implication is the standard partial-summation fact that asymptotic density, when it exists, is inherited by the logarithmic mean (PlanetMath, "inequality of logarithmic and asymptotic density"; standard analytic number theory — I did not verify it from a textbook this session). The converse failure is asserted in a primary source: Inselmann p. 4, "*there are subsets of `ℤ⁺` with logarithmic density 1 and lower natural density 0*".
2. **Therefore the two are not incomparable in the way the brief supposed.** For a *fixed conclusion*, natural density is the strictly stronger claim. What is genuinely incomparable is Tao's statement versus Korec's/Inselmann's, because the conclusions differ too: Tao reaches an arbitrarily small threshold in the weaker density; Inselmann reaches `m^ε` in the stronger one. Neither implies the other.
3. **Tao's reason for logarithmic density does not transfer to us.** He wants approximate multiplicative invariance because his argument *iterates across scales*; the reformulation findings §8 item 7 records, correctly, that our consequence does not iterate and makes no attempt to. Inselmann needed no logarithmic density either, because he bought invariance a different way (`∗`-density).

**Recommendation: natural density. Keep §5.7's choice and strengthen its justification.** Reasons, in order of weight: (a) every neighbour the statement will be read against — Terras, Everett, Allouche, Korec, Inselmann — is natural density, and stating ours in logarithmic density would make it incomparable to its own family and would read as hedging; (b) natural is strictly the stronger claim, and we lose nothing by making it, because (c) the §4 base case is *exact* in natural density on a dyadic block and would have to be re-derived to be exact in any other; (d) the one published motive for logarithmic density is an iteration property we do not use. §5.7's "acceptable variant" should be downgraded: logarithmic density here is a strictly weaker variant with no compensating advantage.

---

## 3. Verdicts on the brief's five questions

### Q1 — Is the restated AEH contraction consequence already known unconditionally?

**SUBSUMED.** Not partially, not comparably. The restated consequence is

> almost every starting value, in natural density, descends below `x^η` for every fixed `η > 0` within `O(log x)` blocks

and Inselmann's **Corollary 1.4** is that statement, proved, in the same density, at a horizon of exactly the same order — indeed at exactly the horizon `θ = 1/β` that our own formulation identifies as the full descent. His **Theorem 1.10** is strictly stronger than ours in three separate ways at once: it is unconditional; it is **two-sided**, pinning the orbit into `(3/4)^k m^{1±ε}` from below as well as above, which AEH does not give even with the uniform-integrability rider; and it holds **simultaneously for all `k`** in the range rather than at the endpoint. The AEH-conditional version has no residue whatever over it.

It is worth being blunt about how complete this is. Our consequence also required a rider (`13.3.2`'s uniform integrability) that the reformulation findings could not derive. Inselmann's needs nothing. **A conditional statement with an underived rider is strictly weaker than an unconditional theorem that says more, and it must not be printed as a consequence worth advertising.**

### Q2 — Is the ledger half also subsumed?

**SPLIT, and the split is exactly where the paper's remaining value is.**

* **First moment: subsumed, unconditionally, to the full horizon.** Inselmann Theorem 1.6 pins `|Σ_{i<k} p(m)_i − k/2| ≤ ε log₂ m` uniformly for all `k` up to `log₂m/(1−log₂√3)`, natural density one. At `k ≍ log₂ m` this says the frequency of odd steps converges to `1/2` along the whole descent — which is `P(s = 1) = 1/2` in Cesàro form, equivalently `E[s] = 2`. Theorem 1.10's envelope pins the same first moment on the valuations.
* **Fixed-window distributional ledger: classical, and already conceded.** Terras Corollary 1.4 gives every length-`k` parity pattern natural density exactly `2^{-k}` for fixed `k`. `publication.md` L40 already frames AEH as "a precise restatement of classical heuristics (Terras; Haar-genericity)" and `itinerary.md` L14 already disclaims novelty for the cylinder theorem. Nothing here contradicts the project's own adjudication; it sharpens it.
* **Distributional ledger at a growing horizon: NOT subsumed, as far as I could establish.** I found nothing carrying the full `2^{-j}` marginal at every `j`, the `Σ_{j even} 2^{-j} = 1/3` `3`-gain rate, the exact depth marginal, or `π_k` as a measure, past the digit-budget horizon. Inselmann controls a running *sum*; knowing the mean of the parity bits does not give the distribution of run lengths, and `P(s even) = 1/3` is a run-length statistic. **[?]** His `∗`-density machinery looks to me like it could plausibly be pushed to distributional statements, and he does not say it cannot; I did not attempt it and I read only his introduction and §2 opening, so treat "not subsumed" here as "not stated anywhere I looked", not as "known to be open".

**So the honest one-line summary of §5's standing is:** the descent is gone, the first moment is gone, and what remains is `π_k` as an exact *law* — every marginal at every depth, and the per-step trichotomy that produces it — asserted along horizons past the digit budget.

### Q3 — Should the paper cite Korec and/or Tao?

**Yes to both; and Inselmann is not optional — omitting it would leave the paper asserting as a conditional consequence something the literature proves outright.** Draft entries and sentences at §4 below.

### Q4 — Natural or logarithmic density?

**Natural.** Full reasoning at §2 above.

### Q5 — Does this change how the AEH section should be framed?

**Yes, and in exactly the direction the brief anticipated.** Three concrete consequences.

1. **Drop the descent corollary entirely.** The reformulation findings' §6.2 already offers a "conservative variant" that omits it pending this check. Take it — and go further: the full version's clause about the drift "stated with the uniform tail rider" should also go, because the drift *at that horizon* is now a theorem of Inselmann's without any rider, and stating our weaker conditional version alongside would be worse than silence.
2. **State the value claim where the value is.** AEH's content is the *exactness* of `π_k` and the per-step laws — the `2^{-j}` marginal at every `j`, the `1/3` rate from Lemma `lem:absorption`, the depth law of `13.6.5`, the error-free window trichotomy — along horizons the classical cylinder count does not reach. That is a distributional claim, not a descent claim, and it is the one claim in Section 5 that nothing I found in the literature makes.
3. **Correct §4's framing of its own frontier.** The reformulation findings say "the unconditional range covers about `20.8%` of a descent; AEH is the assertion that equidistribution survives the remaining `79%`". That is exactly right about *the cylinder-plus-concentration argument*, and it is exactly the classical range Inselmann names as `α = 1.443`. But the sentence as it stands invites the reading that `79%` of the descent is unconditionally untouched territory, and for the coarse statistics it is not — Inselmann covers all of it. The paper's version of that paragraph must say "the frontier of *this* argument, and of the classical ones; for the trajectory envelope and the first moment it has been crossed unconditionally (Inselmann), by a different technique". Otherwise the paper's most interesting new observation is stated in a form a referee will read as an overclaim.

---

## 4. Draft `\bibitem` entries and citing sentences

### 4.1 Bibliography additions (after `\bibitem{terras}`, keeping the file's existing order and register)

```latex
\bibitem{everett} C.~J.~Everett, \emph{Iteration of the number-theoretic function
  $f(2n) = n$, $f(2n+1) = 3n+2$}, Adv.\ Math.\ 25 (1977), 42--45.
\bibitem{korec} I.~Korec, \emph{A density estimate for the $3x+1$ problem},
  Math.\ Slovaca 44 (1994), no.\ 1, 85--89.
\bibitem{tao} T.~Tao, \emph{Almost all orbits of the Collatz map attain almost
  bounded values}, Forum Math.\ Pi 10 (2022), Paper No.\ e12, 56 pp.;
  arXiv:1909.03562.
\bibitem{inselmann} M.~Inselmann, \emph{An approximation of the Collatz map and a
  lower bound for the average total stopping time}, arXiv:2402.03276 (2024).
```

Notes on the entries. **Korec and Tao are verified from the primary documents** (title, journal, volume, year, pages, article number). **Inselmann's title differs between the arXiv metadata ("…a lower bound for the average total stopping time") and his own title page ("…a lower bound for **its** average total stopping time")** — the entry above follows the arXiv metadata; pick one and be consistent. **Inselmann has no journal reference**, and the entry must therefore say `arXiv:2402.03276 (2024)` and nothing more; check before submission whether it has since appeared. **Everett is optional** — it is already pinned at `publication.md` L19, and Tao and Inselmann both cite Terras and Everett jointly for the same fact, so including it costs one line and removes an asymmetry. **Allouche is not drafted**: I could not verify the reference details from a primary source, and the threshold is printed incorrectly in two of the three secondary sources that state it (§1.2). If the author wants it, verify the Séminaire volume and exposé number against a library record first.

### 4.2 Related work, L59 — insertion after the first sentence

Current opening: *"Block-like decompositions and stochastic models are classical (Terras \cite{terras}; see Lagarias \cite{lagarias} for the literature), and the $2$-adic conjugacy of the Collatz map to the shift underlies all Haar-genericity heuristics."*

```latex
The unconditional density line descending from Terras is long and is not what
Section~\ref{sec:aeh} adds to. Terras \cite{terras} and Everett \cite{everett}
place descent below the start at natural density one; Korec \cite{korec} lowers
the target to $y^{c}$ for every $c > \log_4 3 = 0.7924\ldots$, in natural density
and within $O(\log y)$ steps; Inselmann \cite{inselmann} carries a two-sided
trajectory law --- the orbit tracked to within $m^{\pm\varepsilon}$ of its
classical drift, simultaneously at every time up to the full descent horizon
$(\log_2\tfrac43)^{-1}\log_2 m$ --- at natural density one, and so reaches
$m^{\varepsilon}$ for every fixed $\varepsilon>0$; and Tao \cite{tao} reaches
every divergent threshold, in logarithmic density. What
Hypothesis~\ref{hyp:aeh} asserts is not descent but the exact window law
$\pi_k$ itself, at horizons past the digit budget of
Heuristic~\ref{prop:budget}.
```

### 4.3 Section 5, replacing the contraction clause of L247

To be inserted into whichever version of L247 the AEH round settles on, in place of "and almost-everywhere contraction":

```latex
The descent consequence is not stated here, because it is a theorem without the
hypothesis. That all but a set of starting values of natural density zero drop
below $x^{\eta}$, for every fixed $\eta > 0$, within $O(\log x)$ blocks is
Inselmann \cite[Cor.~1.4]{inselmann}; his \cite[Thm.~1.10]{inselmann} is stronger
than anything Hypothesis~\ref{hyp:aeh} yields here, being two-sided, uniform in
the time, and unconditional, and it already runs to the full descent horizon
$1/\beta$ blocks per bit rather than the $1/4$ at which the cylinder count of
Section~\ref{sec:aeh} stops. The first entry of the ledger --- that odd steps
occupy half the schedule to the same horizon --- is likewise unconditional
\cite[Thm.~1.6]{inselmann}. What the hypothesis supplies beyond these is
distributional and is the whole of its content: the full $2^{-j}$ marginal at
every $j$, the exact $\tfrac13$ rate of Lemma~\ref{lem:absorption}, and the depth
law, at every finite depth and past the budget at which the classical count
reaches. Its exceptional set is a density-zero set of \emph{starting values} at a
prescribed finite horizon --- not a null set of orbits, and not a statement about
any orbit's infinite tail. It does not exclude individual staircase tails
(Remark~\ref{rem:staircase}); it does not iterate, the image of a density-one set
of starts needing not be density-one at the next scale, an obstruction Tao states
in the same terms \cite{tao}; and by Heuristic~\ref{prop:budget} it cannot be
reached by finite-window computation.
```

### 4.4 One sentence for §4's base-case paragraph (reformulation findings §6.1, second paragraph)

Its closing currently reads *"the digit budget locates the frontier, and this is the statistical statement on the far side of it."* Append:

```latex
That frontier is the classical one: the same $\theta < 1/4$ is where Terras's
count stops, and $1 - \beta/4 = \log_4 3$ is exactly the exponent Korec
\cite{korec} obtains by exhausting it. It is a frontier of this technique and
not of the problem --- Inselmann \cite{inselmann} crosses it unconditionally for
the trajectory envelope and the first moment, by an argument that buys the
missing iteration invariance from a density notion stronger than natural
density rather than from a sharper count.
```

---

## 5. What I could not establish

1. **[?] Whether `aeh.md` `13.6.5`'s absorption law `ν` is Tao's `Syrac(ℤ₃)`.** §1.4 records the circumstantial case — same iteration, same `2^{-a}` weights, both exact stationary `3`-adic laws, denominator `63` in both, `2/63` in both lists. I did not do the computation and this is not a small matter: if they coincide, a law the paper presents as computed in the project record has a 2019 primary source. **This is the one open item I would not let the AEH section be finalized without.**
2. **[?] Whether anything in the literature gives the *distributional* ledger past the digit budget.** My negative finding is "not stated in anything I read", not "known to be open". Inselmann's `∗`-density method looks capable of more than he claims for it; a targeted read of his §2 and Lemmas 2.9–2.16, which I did not do, would settle whether the run-length distribution comes along for free.
3. **[?] Whether Mazur's claimed natural-density theorem is correct.** Unrefereed, AI-generated, not on arXiv, eleven days old, Lean-verified only at the level of the formal statement. Verdicts above do not depend on it.
4. **[S] Allouche's reference details and threshold.** Not read. Korec's `3/2 − log₃2 = 0.86907` is the arithmetically consistent form; Tao and Inselmann both print an expression that evaluates to `−0.085`. Verify against a library record before printing.
5. **[?] Whether Inselmann has been published or superseded since Aug 2024.** arXiv lists no journal reference and v3 is the current version. I did not find a later paper in this line other than Mazur's. I also did not check whether the `Generalized Collatz Maps with Almost Bounded Orbits` line (Gonçalves–Greenfeld–Madrid, arXiv:2111.06170, per Mazur's §1) bears on the single-map case; Mazur describes it as generalizing Tao to a family of maps and discussing the natural-density obstruction, which suggests it does not, but I did not read it.
6. **Not attempted:** whether the paper's `π_k` chain, the routing lemma, or the window trichotomy have neighbours in the literature. That is a different sweep from this one and `publication.md` L34 already carries the project's verdict on the anchor layer.

---

## 6. Verification table

| Fact | Source, and grade |
|---|---|
| Terras `χ` definition, `F(k)` natural-density definition, `lim F(k) = 0` | *Acta Arith.* 30 (1976), pp. 241, 245, 247 — **[P]**, ICM scan read |
| Terras periodicity `E_k(n) = E_k(m) ⟺ n ≡ m mod 2^k`; Cor. 1.3, 1.4 | ibid., pp. 242–243 — **[P]** |
| Korec abstract, `y^{0.7925}`; Theorem 1 at `c > log₄3 = 0.79248125…`; asymptotic density | *Math. Slovaca* 44 (1994) 85–89, p. 85 — **[P]**, DML-CZ scan read |
| Korec's horizon "could be bounded by `log₂ y`, but not independently of `y`" | ibid., p. 86 — **[P]** |
| Korec's Lemma 1 = Terras periodicity; Lemma 2 = CLT at `d > 1/2` | ibid., pp. 86–87 — **[P]** |
| Allouche threshold `3/2 − log₃2 = 0.86907…` | Korec p. 86, referee remark — **[P]** for the quote, **[S]** for Allouche |
| Tao Theorem 1.3, Definition 1.2 (logarithmic density), Remark 1.4 | arXiv:1909.03562v7, pp. 2–3 — **[P]** |
| Tao's reason for logarithmic density ("better approximate multiplicative invariance") | ibid., p. 2 — **[P]** |
| Tao's survey of Terras/Everett/Allouche/Korec, "one can use natural density" | ibid., p. 2 — **[P]** |
| Tao's non-iteration/concatenation obstruction | ibid., p. 2 — **[P]** |
| Tao Remark 1.16, natural-density upgrade needs fine-scale mixing of the full affine map | ibid., p. 12 — **[P]** |
| Tao Remark 1.13, `Syrac(ℤ₃)`; `Syrac(ℤ/3²ℤ) = 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63` | ibid., pp. 10–11 — **[P]** |
| Inselmann abstract, `α = 1.443 → 6.952`, "maximally possible value" | arXiv:2402.03276v3, p. 1 — **[P]** |
| Inselmann Theorem 1.1, 1.3, Corollary 1.4, Question 1.5 and its discussion | ibid., pp. 2, 4 — **[P]** |
| Inselmann Theorems 1.6, 1.9, 1.10 | ibid., p. 5 — **[P]** |
| "there are subsets of `ℤ⁺` with logarithmic density 1 and lower natural density 0" | ibid., p. 4 — **[P]** |
| "sets of natural density 1 do not have this property" (`∗`-density strictly stronger) | ibid., p. 3 — **[P]** |
| Natural density 1 ⟹ logarithmic density 1 | standard, partial summation — **[S]** (PlanetMath), not verified from a textbook |
| Mazur Theorem 1.1, `C_Coll < 436`, `C_Syr < 145`; AI disclosure; frozen Lean commit | `proofatlas.ai` PDF v2, 21 Jul 2026, pp. 1–3 — **[P]** for what it claims |
| Mazur's history paragraph crediting Inselmann | ibid., p. 2 — **[P]** (this is how Inselmann was found) |
| No local copy of any of these in `sources/` | `sources/` listing — checked, none present |
| Project has never cited Tao, Korec, Inselmann or Allouche mathematically | repo-wide grep; Tao appears only as a ccchallenge queue entry in `briefs/jointnote-premise-external-findings.md` — checked |

**Derived numbers, and how.** All computed this session in exact/float arithmetic: `log₂3 = 1.584962500721156`; `β = 2(2 − log₂3) = 0.8300749985576878`; `1 − β/4 = 0.792481250360578` and `log₄3 = 0.7924812503605781` — equal to the last displayed digit, and equal identically since `1 − (2(2−log₂3))/4 = log₂3/2`; `1/β = 1.204710419826604`; `(1/β)/(1/4) = 4.818841679306416`; `2/log(4/3) = 6.952118993564416` (`T`-steps per `ln m`), `× log 2 = 4.818841679306419` (`T`-steps per bit) — equal to the previous line to 15 digits. Block conversions use `σ = E[m+r] = 4` parity steps and `E[m] = 2` Syracuse steps per block, from `aeh.md` `13.6.1` via the reformulation findings §4.
