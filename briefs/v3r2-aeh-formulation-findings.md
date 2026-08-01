# Findings: the AEH sample space and limiting procedure (v3 round 2)

**Task:** `briefs/v3r2-aeh-formulation-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `e4dac49`, working tree clean apart from the two round-2 briefs.

---

## 0. Verdict in one paragraph

The reviewer is right, and the defect is worse than "imprecise": **no formulation whose sample space is the visit sequence of a single fixed orbit can be non-degenerate for integers if Collatz is true.** The iterated limit is not the problem — the sample space is. The repair is the ensemble form the brief anticipates, with one addition that turns out to be the whole point: **the horizon must be linked to the sampling scale.** Unlinked (fixed horizon, scale → ∞) the statement is *true but empty* — it is a theorem, provable from the classical coding fact the wiki already carries at `itinerary.md` `14.15.1.5`. Linked, it is exactly `Heuristic~\ref{prop:budget}` with a number on it: provable for horizons up to `1/4` block per bit of start, hypothetical from there out to the `1.2047` blocks per bit that a full descent takes. The bulk cut survives, demoted from "the device that makes the question nondegenerate" (`13.6.6`, which is wrong on this point) to "the guard that excises the bottom regime", and constrained to be non-binding, because a binding cut is the selection rule that produced the record's own drift artifact (`13.4`). On the consequences: `13.3.1` survives restated; `13.3.2`'s `1/3` survives, its **drift clause does not follow and needs a stated rider**; `13.3.3` survives and gets *stronger* (it was already the most honest paragraph on the page); `13.6.4` survives **verbatim in its proof** once its opening definition is made regime-neutral, which is a two-sentence edit; the paper's L247 "almost-everywhere contraction" must be restated as a natural-density statement about *starting values at a finite horizon* and must stop implying anything about a fixed orbit's tail.

---

## 1. The defect, stated so it cannot be argued with

### 1.1 Why every single-orbit form fails

Fix any orbit `x_0 → x_1 → …` that reaches `(1,1)`, and let `A = max_n x_exit(n) < ∞`.

* For any cut `X ≥ A`: the qualifying set `{n : x_exit(n) > X}` is **empty**. The empirical distribution over it is undefined.
* For any cut `X < A`: the qualifying set is **finite** (the orbit is eventually at `(1,1)`, whose exit is `1`). The empirical distribution over it is a fixed finite object; the inner limit "orbit length → ∞" freezes it.

So `lim_{X→∞} lim_{len→∞}` is: a frozen finite sample for each of finitely many `X`, then undefined. It cannot equal `π_k` except by accident on a finite set of cuts, and it is undefined for all large `X`. If Collatz is true, this holds for **every** starting value, so `13.2.1` and `hyp:aeh` are, as literally written, false-or-undefined everywhere. The reviewer's summary is exact.

Two things follow that are worth stating because they close off the obvious escapes:

* **Reversing the limit order is worse, not better.** `lim_{len→∞} lim_{X→∞}`: the inner limit is undefined immediately (for fixed length, large `X` gives an empty sample).
* **A joint/diagonal single-orbit limit also fails.** Any `X = X(n) → ∞` as orbit length `n → ∞` still eventually exceeds `A`, after which no visit ever qualifies again. The failure is not about the order of limits; it is that a convergent orbit contains only finitely many bulk visits, full stop.

The only single-orbit reading that is *non-vacuous* is the one conditioned on the orbit having infinitely many bulk visits — i.e. conditioned on divergence. That is exactly the reviewer's "retaining a single-orbit formulation would require conditioning on infinitely many bulk visits", and the reviewer's verdict on it is also right: an assertion about orbits assumed not to converge cannot be used to argue that orbits contract. It survives as a *definition* (see §5.5), not as the hypothesis.

### 1.2 The record has never measured the stated hypothesis

Every number in `13.4`, `13.5` and `13.6.5` comes from a protocol with a **finite horizon and uniformly sampled large starts**:

| Protocol | Starts | Horizon | Cut | Weighting |
|---|---|---|---|---|
| `aeh_anomaly.py` X1 (L15–29) | `100`-bit odd, uniform | exactly `32` steps, no stopping rule | **none** | per-visit pooled |
| `aeh_anomaly.py` X2(b) (L66–75) | `140`-bit odd, uniform | exactly `150` steps | **none** | per-visit pooled, banded by step |
| `aeh_symbolic.py` `check_orbit_texture` (L539–584) | uniform in `[2^70, 2^71)` | burn-in `10` + exactly `30` | `2^30`, **deliberately non-binding** | per-visit pooled |
| `merle_aeh_key_check.py` `drift_fixed_horizon` (L268–273) | `[2^55,2^56)` | exactly `15` steps | **"no stopping rule, no cut"** | pooled, cluster SEs |

`check_orbit_texture`'s own docstring is the cleanest statement of the situation in the whole repository:

> starts in `[2^70, 2^71)` so the bulk cut `omega > 2^30` **never binds** within the burn-in + horizon (no survivorship selection at finite size; `13.2.1`'s limit regime realized directly)

It is not `13.2.1`'s limit regime — `13.2.1` has no scale parameter at all. It is the ensemble regime, with the cut present and inert. The record built the right protocol and then wrote down a different statement.

### 1.3 The cut, when it binds, is a known biasing selection

This is not speculation; the record documents it twice.

* `13.5` (L45–55): per-orbit ratios over cut-qualified visits produced a `z = 5.0` phantom, resolved by *removing* the estimator, not the cut. Standing rule at L53: "fixed-horizon, unweighted, per-visit sampling from uniform starts. Ratio estimators over correlated visit sequences are forbidden."
* `13.4` (L41): Merle's drift artifact `−0.33/−0.36` against `−0.4150` is "confirmed to be survivorship bias from the cut protocol"; under the fixed-horizon rule the same orbit population gives `−0.4166 ± 0.0037` per odd step and `−0.8367 ± 0.0060` per block.

`merle_aeh_key_check.py` isolates the mechanism: the biased variants condition a transition on **both** endpoints being above the cut (`if x <= cut or (censored and x2 <= cut): continue`, L229–230), which censors precisely the large descents. A cut that binds is an outcome-conditioning rule aimed at the quantity `13.3.2` wants to measure. Any repair that leaves the cut load-bearing re-opens this.

---

## 2. What the five required specifications must be

| # | Specification | Answer |
|---|---|---|
| 1 | Sample space | Odd integers `x` drawn uniformly from a dyadic block `[N, 2N)`, projected by `R`; natural density over starting **values**, not over states. |
| 2 | Horizon | `T = ⌈θ log₂ N⌉`, **linked to the sampling scale**, `θ > 0` a quantified rate. Deterministic; no stopping rule. |
| 3 | Weighting | Per-visit, unweighted, pooled with one normalisation. Per-orbit ratios are legitimate here *only because the denominator `T` is deterministic* — that is the real content of `13.5`'s rule. |
| 4 | Bulk cut | Retained as a guard on the bottom regime, required non-binding (`log X_N = o(log N)`); it is **not** what makes the statement nondegenerate. |
| 5 | Limit order | **There is no order.** One limit, `N → ∞`, with `θ` and `(X_N)` quantified outside it. Non-degenerate at the only point it is taken: each sampled orbit contributes `min(θ, (1−o(1))/β)·log₂ N → ∞` bulk visits. |

Two notes on 1 and 2 that are not cosmetic.

**On 1 — states versus integers.** `13.2.1` says "almost every state (in natural density of starting values)", which does not typecheck: a state is a pair `(ω,d)` and natural density on such pairs is not canonical. The code duly samples an *artificial* state (`w = rng.randrange(1<<70,1<<71)|1; d = rng.randrange(1,13)`) and then burns in `10` steps to forget it. Sampling integers and projecting removes the artificiality and — decisively — is the version for which the unconditional base case of §4 is exact. The burn-in is then a finite-size device, not part of the statement (Cesàro averaging over `T → ∞` visits absorbs any `O(1)` transient).

The transient is real and quantifiable, which is why the burn-in exists: for a uniform odd integer `x`, `a = v_3(x+1)` has `P(a=0) = 2/3`, `P(a=1) = 2/9`, `P(a≥2) = 1/9`, whereas the bulk law of `13.6.5` is `2/3`, `19/63 = 0.3016`, `2/63 = 0.0317`. The gap is exactly `13.6.5`'s "supported off the dead-door class (`ν(y ≡ 0 mod 3) = 0`, every door being live)": a uniform integer is `≡ 0 mod 3` a third of the time, a door never is. One `G`-step fixes the support; the remaining `3`-adic relaxation is geometric (`13.6.3`(iv): `P_B(a ≥ j) ≤ 2·(0.93)^j`, exact values far smaller).

**On 2 — why the horizon must be linked.** See §4. If `T` is fixed and only `N → ∞`, the statement is a theorem. The hypothesis lives entirely in the growth of `T` with `log N`.

---

## 3. The recommended formulation

> **AEH, ensemble form.** Fix a depth `k`, a horizon rate `θ > 0`, and a cut sequence `X_N → ∞` with `log X_N = o(log N)`. For each `N`, draw `x` uniformly from the odd integers of `[N, 2N)`; put `(ω_0,d_0) = R(x)` and `(ω_{n+1},d_{n+1}) = F(ω_n,d_n)`; let `ν_{k,N}(x)` be the unweighted empirical distribution of the depth-`k` window states of the first `T = ⌈θ log₂ N⌉` visits, restricted to the **bulk** visits — those with `x_exit > X_N` — each qualifying visit counted once and no visit reweighted by the orbit it came from. Then for every `ε > 0`, the density of starts `x` with `‖ν_{k,N}(x) − π_k‖ > ε` tends to `0` as `N → ∞`, for every admissible `(θ, (X_N))`.

Five properties, each of which the old form lacked.

1. **One limit.** `N → ∞`. Nothing is iterated; nothing is exchanged.
2. **Non-degenerate where it is taken.** For every `N`, every sampled orbit supplies `T = ⌈θ log₂ N⌉` visits, of which all but the ones below the cut are tallied; the per-orbit sample and the pooled sample both grow without bound. The growth comes from the scale, not from the age of any orbit.
3. **Quenched, not annealed.** It is a statement about individual sampled orbits (all but a vanishing density of them), not about a pooled average. This matters: only the quenched form can support a per-start conclusion, and the pooled form is strictly implied by it.
4. **It is the protocol.** Fixed horizon, uniform large starts, per-visit unweighted pooling, deterministic denominator — `13.5`'s standing rule, verbatim, with the one thing the rule does not say (how the horizon relates to the start scale) supplied.
5. **It has a proved base case and an explicit frontier.** §4.

### 3.1 The density statement is a genuine "almost every integer" statement

Worth recording because it is easy to under-sell. If for each dyadic block the bad density `δ_N → 0`, then the union of the bad sets has **natural density zero in the integers** (Cesàro). So the ensemble form does deliver a statement of the form:

> for every `ε, θ, k` there is a set `E` of natural density `0` such that every `x ∉ E` has its first `⌈θ log₂ x⌉` bulk window-state frequencies within `ε` of `π_k`.

The exceptional set is genuinely density-zero in the integers. What it is **not** is a set on which anything holds for infinite time: `E` depends on `ε` and `θ`, the property is a finite-horizon property, and no diagonal argument gets `θ → ∞` (past `θ = 1/β` the orbit is in the bottom regime, where the statement is false by design).

---

## 4. Why this one: the unconditional base case, and where the content actually is

This is the part of the finding I did not expect and consider the most useful output of the round.

**Claim (base case).** Let `x` be uniform on the odd integers of `[2^L, 2^{L+1})`. Let `W_n(x)` be the length-`n` door-letter word of `x`'s `G`-orbit (`13.6`'s alphabet). Then

```text
TV( Law(W_n(x)) , B^{⊗n} )  ≤  P_B( S_n ≥ L ),      S_n = Σ_{i<n} (m_i + r_i).
```

**Proof.** By Theorem `14.15.1.5` (`itinerary.md` L46–53) the odd integers following a word `W` form **exactly one odd residue class mod `2^{S(W)+1}`**. A dyadic block of `2^L` integers meets such a class in `2^{L−S−1}` integers, of which the block contains `2^{L−1}` odd ones, so `P(W_n(x) = W) = 2^{−S(W)} = B(W)` **exactly**, for every `W` with `S(W)+1 ≤ L`. The two laws therefore agree on `A = {W : S(W)+1 ≤ L}`, and `P(A^c) = B(A^c)`, giving `TV ≤ B(A^c) = P_B(S_n ≥ L)`. ∎

By Lemma `13.6.1` (aeh.md L63) the `m_i, r_i` are i.i.d. geometric(1/2), so `S_n` is the number of fair flips to reach `2n` heads, `E[S_n] = 4n`, and `P_B(S_n ≥ L)` is exponentially small in `L` whenever `n ≤ (1/4 − ε)L`. Concentration under `B^{⊗n}` (Sanov) then upgrades this to the **quenched** statement, and `13.6.3`(iii)+(iv) carries it from letters to depth-`k` window states at the cost of `2L(0.93)^W`. Hence:

> **For every `θ < 1/4`, the ensemble form is a theorem, not a hypothesis.**

And by the same accounting:

* `E[m+r] = 4` per block. This is the same `4` as `Heuristic~\ref{prop:budget}`'s "empirical mean `σ ≈ 4.0` along orbits" — indeed `σ = v_2(C) = s + m_+` and `E[s] = E[m] = 2` under `π_k`. The digit budget and the cylinder theorem are the same accounting seen from two sides.
* A full descent from `N` takes `1/β = 1.2047…` blocks per bit, `β = 2(2 − log₂3) = 0.8301…` (`aeh.md` L41).
* Ratio: `1.2047 / 0.25 = 4.82`. **The unconditional range covers about `20.8%` of a descent; AEH is the assertion that equidistribution survives the remaining `79%`, after the start's digits are spent.**

Two consequences.

**(a) The formulation must link horizon to scale, or it says nothing.** With `T` fixed and `N → ∞`, `n ≤ (1/4−ε)L` holds for all large `L`, so the statement is the theorem above. That is why the naive reading of "the calibration protocol, promoted to a hypothesis" is the wrong repair: it is true and empty. The hypothesis is the `θ ≥ 1/4` regime.

**(b) The calibration record is genuinely testing the hypothesis, not re-measuring a theorem.** Flagship run: starts in `[2^70, 2^71)` (`L = 70`, budget `17.5` blocks), burn-in `10` + horizon `30` = `40` blocks = `2.29 ×` budget; of the `30` tallied blocks, blocks `18–40` (`23` of `30`, `77%`) lie beyond it. `aeh_anomaly.py` X2(b) runs `150` blocks from `140`-bit starts = `4.3 ×` budget. This is a real strengthening of the calibration record's evidential value and should be stated on the page.

**One caution against over-reading (b).** The entropy accounting bounds where the *exact joint law* argument works. It does **not** obstruct the hypothesis: empirical frequencies of one long word are a far coarser statistic than the joint law, and matching a few dozen cell frequencies costs nothing like `4` bits per block. The frontier at `θ = 1/4` is a frontier of *proof technique*, not a barrier. Say it that way or the finding will be misread as evidence against AEH.

---

## 5. Rejected alternatives

**5.1 Keep the single-orbit form, condition on infinitely many bulk visits.** Rejected as *the hypothesis*. If Collatz is true the conditioning class is empty and the statement is vacuous; and an assertion about orbits assumed not to converge cannot support a contraction consequence about orbits in general. Retained as a *definition* used by `13.6.4` and by the `2`-adic side (§5.5).

**5.2 Swap the limit order (`X → ∞` first).** Rejected: degenerate at the first limit, for every orbit and every finite length.

**5.3 Single-orbit joint limit, `X = X(n) → ∞` as length `n → ∞`.** Rejected: still empty past the orbit's maximum. No single-orbit scheme works; the defect is the sample space.

**5.4 Ensemble with an *unlinked* fixed horizon (the literal protocol).** Rejected as the statement, kept as the protocol: it is a theorem (§4), so it carries no hypothesis content.

**5.5 Pooled (annealed) ensemble only.** Rejected as primary: pooling all visits of all starts and normalising once gives no per-start conclusion, so it cannot yield contraction in any form. Retained as the *measured* proxy — it is exactly what `check_orbit_texture` computes — and it is implied by the recommended (quenched) form.

**5.6 Reformulate on `Z_2` (Haar-a.e. genericity).** Rejected: that is a theorem already (`13.6.2` + Birkhoff) and says nothing about a Haar-null set. `13.6.6` makes this point correctly and it remains the reason the integer statement has to be a *scaling* statement.

**5.7 Logarithmic density instead of natural density.** Considered, not adopted. Natural density on a dyadic block is what the sampler realises and what makes §4 exact. Log-density on `[1,N]` is a weighted average of block statements and would be an acceptable variant; if the literature comparison of §9 favours it, it is a one-line change.

---

## 6. Drop-in text

### 6.1 `paper/collatz-reduced-v3.tex`, replacing lines 241–245 (hypothesis + explanatory paragraph)

```latex
\begin{hypothesis}[AEH, ensemble form]\label{hyp:aeh}
Fix a depth $k$, a horizon rate $\theta > 0$, and a cut sequence $X_N \to \infty$
with $\log X_N = o(\log N)$. For each $N$, draw $x$ uniformly from the odd integers
of $[N, 2N)$; put $(\w_0,d_0) = R(x)$ and $(\w_{n+1},d_{n+1}) = F(\w_n,d_n)$; and let
$\nu_{k,N}(x)$ be the empirical distribution of the depth-$k$ windows of the first
$T = \lceil \theta \log_2 N\rceil$ visits, restricted to the \emph{bulk} visits ---
those with $x_{\mathrm{exit}} > X_N$ --- each qualifying visit counted once and no
visit reweighted by the orbit it came from. Then for every $\varepsilon > 0$,
\[
  \frac{2}{N}\,\#\bigl\{\, x \text{ odd},\ N \le x < 2N \;:\;
     \lVert \nu_{k,N}(x) - \pi_k \rVert > \varepsilon \,\bigr\}
  \;\longrightarrow\; 0 \qquad (N \to \infty),
\]
for every admissible $\theta$ and $(X_N)$.
\end{hypothesis}

There is one limit here, $N \to \infty$, and the sample grows because the sampling
scale grows rather than because any one orbit is run forever. That is forced. Along
a fixed orbit no limiting procedure survives: the unrestricted empirical distribution
is false on every convergent orbit, whose tail sits at $(1,1)$ forever; and above a
fixed cut a convergent orbit supplies only finitely many qualifying visits, and none
at all once the cut exceeds its maximum, so a limit taking orbit length first and the
cut second is empty rather than merely delicate, in whichever order it is taken. The
bulk cut survives with a smaller and different job: it excises the \emph{bottom
regime} --- the fixed drainage basin of small integers, whose window statistics are
the digits of particular numbers rather than samples from a measure
(\texttt{aeh.md} \S13.1) --- for those sampled orbits that reach it inside the
horizon. The requirement $\log X_N = o(\log N)$ keeps it from becoming a selection
rule, a cut that binds censoring exactly the largest descents and so biasing the
quantities being measured (\texttt{aeh.md} \S13.4, \S13.5); for
$\theta < 1/\beta$, where $\beta = 2(2-\LL) = 0.8301\ldots$ is the classical
per-block contraction rate, the cut binds on a vanishing density of starts and the
tally denominator is the deterministic $\lceil\theta\log_2 N\rceil$ that
\texttt{aeh.md} \S13.5's standing rule --- fixed horizon, unweighted, per-visit
sampling from uniform starts --- was written to secure.
```

**Recommended second paragraph** (new; this is where the reformulation pays for itself, and it ties Section~5 to Heuristic~\ref{prop:budget}):

```latex
The hypothesis has an unconditional base case, and it is Heuristic~\ref{prop:budget}
with a number on it. The classical coding fact --- the odd integers whose first $n$
blocks realize a prescribed itinerary form exactly one residue class modulo
$2^{S+1}$, $S$ the itinerary's total exponent (Terras \cite{terras}; in the present
coordinates \texttt{itinerary.md} \S14.15.1.5) --- makes the first $n$ blocks of a
uniform start from $[2^L, 2^{L+1})$ exactly product-distributed on the event
$S + 1 \le L$, whose complement has probability $e^{-\Theta(L)}$ whenever
$n \le (\tfrac14 - \epsilon)L$. Since $S$ accumulates at mean rate $4$ per block ---
the $\sigma \approx 4.0$ of Heuristic~\ref{prop:budget}, exactly $2 + 2$ under
$\pi_k$ --- Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every horizon rate
$\theta < 1/4$. A descent from $N$ to $O(1)$ takes $1/\beta = 1.2047\ldots$ blocks
per bit, some $4.8$ times as long. Hypothesis~\ref{hyp:aeh} is exactly the assertion
that the product law still describes the orbit after the start's digits have been
spent; the digit budget locates the frontier, and this is the statistical statement
on the far side of it.
```

### 6.2 `paper/collatz-reduced-v3.tex`, replacing line 247

Full version:

```latex
AEH implies the ledger with error $O(2^{-k})$ via Theorem~\ref{thm:onestep} and the
exact $\tfrac13$ rate, in the form the hypothesis has: for every $\varepsilon$ and
every horizon rate, all but a set of starting values of natural density zero carry
those frequencies along their first $\lceil\theta\log_2 x\rceil$ bulk blocks. The
drift needs one ingredient more than equidistribution supplies --- the block length
$m_+$ and the exit valuation $s$ are unbounded, and convergence of window
frequencies at each fixed $k$ bounds their empirical means from below but not from
above --- so contraction is stated with the uniform tail rider recorded at
\texttt{aeh.md} \S13.3.2, which is automatic in the unconditional range above. What
``almost everywhere'' means here is therefore precise and narrow: a density-zero
exceptional set of \emph{starting values} at a prescribed finite horizon, not a null
set of orbits and not a statement about any orbit's infinite tail. It does not
exclude individual staircase tails (Remark~\ref{rem:staircase}); it does not iterate,
since the image of a density-one set of starts need not be density-one at the next
scale; and by Heuristic~\ref{prop:budget} it cannot be reached by finite-window
computation. Its content is a question about digits of $2$-adic logarithms, older and
broader than the Collatz problem.
```

**Conservative variant** — replace the second sentence's ending and drop the descent corollary entirely if the literature check of §9 is not done first. The full version above already stops short of asserting a descent bound; if the author wants the descent corollary stated (``almost every starting value descends below $x^{\eta}$ for every fixed $\eta>0$ within $O(\log x)$ blocks''), **do the §9 check first** — it is a conditional claim in the same genre as unconditional results of Terras, Korec and Tao, and it must not be advertised as new if it is weaker than what is already known.

### 6.3 `paper/collatz-reduced-v3.tex`, line 42 (Version note) — consequential

Current clause: `Hypothesis~\ref{hyp:aeh} states the order of its two limits;`

Replacement:

```latex
Hypothesis~\ref{hyp:aeh} is restated in ensemble form --- uniformly sampled starts,
a horizon linked to the sampling scale, per-visit weighting, a single limit --- the
previous single-orbit reading being empty on every convergent orbit;
```

The clause is inside a sentence that ends "No theorem or universal claim is strengthened", which remains true (a hypothesis is restated, not strengthened). The note's own tally ("repairs four defects and brings three statements back into line") is the author's to keep straight; I have not recounted it.

### 6.4 `aeh.md` Hypothesis `13.2.1` (line 22) — drop-in Markdown

```markdown
**Hypothesis 13.2.1 (AEH, ensemble form).** Fix a depth `k`, a horizon rate `θ > 0`, and a cut sequence `X_N → ∞` with `log X_N = o(log N)`. For each `N`, draw `x` uniformly from the odd integers of `[N, 2N)`, set `(ω_0, d_0) = R(x)` and `(ω_{n+1}, d_{n+1}) = F(ω_n, d_n)`, and let `ν_{k,N}(x)` be the unweighted empirical distribution of the depth-`k` window states over the **bulk visits** among the first `T = ⌈θ log₂ N⌉` — those with `x_exit > X_N` — each qualifying visit counted once, with no per-orbit reweighting (`13.5`). Then for every `ε > 0`, the density of starts `x ∈ [N, 2N)` with `‖ν_{k,N}(x) − π_k‖ > ε` tends to `0` as `N → ∞`, for every admissible `θ` and `(X_N)`.

**Why the ensemble, and what the cut is now for.** There is one limit, `N → ∞`; the sample grows because the sampling scale grows, not because any orbit is run forever. No single-orbit form is available: above a fixed cut a convergent orbit supplies finitely many qualifying visits and, once the cut exceeds its maximum, none, so a limit in orbit length is empty rather than delicate — in either order, and for a diagonal cut `X(n)` too. The bulk cut keeps a smaller job, excising the bottom regime of `13.1` for those sampled orbits that reach it inside the horizon; `log X_N = o(log N)` keeps it from becoming a selection rule, a binding cut being exactly the protocol that manufactured `13.4`'s drift artifact and `13.5`'s phantom cell. For `θ < 1/β`, `β = 2(2 − log₂3) = 0.8301…`, the cut binds on a vanishing density of starts, the tally denominator is the deterministic `⌈θ log₂ N⌉`, and `13.5`'s standing rule is satisfied as written. The sample space is starting *values*, not states: natural density on pairs `(ω,d)` is not canonical, and the integer form is the one with an exact base case below.

**Base case, and where the content is.** By Theorem `14.15.1.5` (itinerary.md) the odd integers following a given length-`n` letter word form exactly one class mod `2^{S+1}`, `S = Σ(m_i + r_i)`; so for `x` uniform on `[2^L, 2^{L+1})` the length-`n` word is *exactly* `B`-distributed on `{S + 1 ≤ L}`, and `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)`. With `E[m + r] = 4` (`13.6.1`) this is exponentially small for `n ≤ (1/4 − ε)L`; concentration under `B` and the dictionary of `13.6.3`(iii)–(iv) carry it to the window states. **Hypothesis 13.2.1 is therefore a theorem for every `θ < 1/4`.** A full descent takes `1/β = 1.2047…` blocks per bit — `4.8` times as long — so the hypothesis is precisely the assertion that equidistribution survives past the digit budget of stage4.md `11.8.7.7`, whose `σ ≈ 4.0` is this `E[m + r] = 4`. The calibration record is measured well past that frontier: the flagship run (starts `[2^70, 2^71)`, burn-in `10`, horizon `30`) runs `2.29 ×` the budget, with `23` of its `30` tallied blocks beyond it.
```

### 6.5 `aeh.md` Theorem `13.6.4`, bulk-frequency definition sentence (line 101)

Current opening: *"Fix one `F`-orbit and a cut `X`; call a statistic's bulk frequency its empirical frequency over the visits with `x_exit > X`, in the limit orbit length `→ ∞` then `X → ∞` (exactly `13.2.1`'s regime)."*

Replacement (the rest of the theorem statement, the displayed equivalence and the entire proof stand unchanged):

```markdown
**Theorem 13.6.4 (the genericity form of AEH).** Fix a **visit family**: a family of finite `F`-orbit segments indexed by a scale, together with a bulk cut — the bulk visits of one orbit's first `T` blocks as `T → ∞`, or the bulk segments of `13.2.1`'s uniformly sampled starts as `N → ∞`. Call a statistic's *bulk frequency* its limiting unweighted per-visit empirical frequency along that family, assumed to exist for every finite pattern; `13.2.1` is the assertion that the integers' ensemble family has the bulk frequencies of `π_k`. Say the family's letter word is **bulk-generic for `B`** if every finite letter pattern, at every fixed offset window around the visit index, has bulk frequency equal to its `B`-probability; say its window-state process is **bulk-equidistributed** if for every `k` and `L`, the `L`-blocks of consecutive depth-`k` window states (with their stratum labels, per `13.6.3`(iii)) have bulk frequencies given by the product law of `13.6.3`(v). Then, **for every visit family** — the dictionary below is deterministic and never inspects the family, so the equivalence holds in particular orbit by orbit, with no measure on starting values invoked:
```

**Why the proof is untouched.** Both directions use the frequency functional only through (a) exact finite-window functional dependence in the `(⇐)` direction, and (b) the explicit error `2L(0.93)^W` plus "for every `W`" in the `(⇒)` direction. Neither uses the *order* of any limit, nor the existence of a single orbit; the theorem was always a theorem about a dictionary, and only its opening definition tied it to a regime that does not exist. `(q1)` and `(q2)` are untouched: `(q1)` is about `L = 1` versus `L ≥ 2` and `(q2)` about the depth marginal, both orthogonal to the sampling regime.

### 6.6 `aeh.md` §13.3 — drop-in replacements

```markdown
**13.3.1 (ledger).** AEH at depth `k` implies the frequency ledger with explicit error `O(2^-k)`: the one-step trichotomy converts window frequencies into `s`-frequencies exactly, except on the undecided set of `π_k`-measure `~2^-(k+1)`. In `13.2.1`'s form: for every `k`, every horizon rate and every `ε`, all but a vanishing density of starting values of a given size carry the ledger to within `O(2^-k) + ε` along their first `⌈θ log₂ N⌉` bulk blocks. Letting `k → ∞` is a diagonal step — valid along any `k(N) → ∞` slow enough that the `k`-dependent densities still vanish, not uniformly — and gives the ledger exactly, in the limit, along those segments. There is no statement here about any fixed orbit's infinite tail: the exceptional set is a density-zero set of *starting values* at a prescribed finite horizon.

**13.3.2 (3-gain and drift).** AEH implies the `3`-gain rate is exactly `1/3` (measured along orbits: `0.3352`, `1.1σ` from `1/3`): `s` even is window-decidable and has `π_k`-probability `Σ_(j even) 2^-j = 1/3`, and the conclusion has the same density-of-starts form as `13.3.1`. **The drift needs one ingredient more than equidistribution supplies, and it is recorded here rather than assumed.** The per-block increment is `m_+·(log₂3 − 1) − s`, and `m_+`, `s` are unbounded; convergence of window-state frequencies at each fixed `k` gives `liminf` bounds on their empirical means (Fatou) but no `limsup` on `m_+`, and the drift needs the latter. **Rider:** if in addition the empirical frequency of `{m_+ + s ≥ j}` is at most `C·2^-j` uniformly in `N` and `j` — uniform integrability of the letter statistics along the sampled segments — then the classical negative drift per block follows, hence contraction of `log x` at the classical rate `2(log₂3 − 2) = −0.8301` per block (`= −β`, `β` the positive contraction rate of `13.2.1`) along the bulk segments of all but a density-zero set of starting values. The rider is automatic in `13.2.1`'s unconditional range `θ < 1/4`, where the letter law is exactly `B`; and the drift itself is measured directly under `13.5`'s standing rule at `−0.8367 ± 0.0060` per block and `−0.4166 ± 0.0037` per odd step (`13.4`). It is an assumption, not a deduction, and the page should not read as though equidistribution alone delivered it.

**13.3.3 (what AEH does not give).** Even in full, AEH yields *density* statements: for each scale, all but a vanishing density of starting values, over a bulk segment of prescribed finite length. It yields nothing about any individual orbit, nothing about any orbit's infinite tail, and it does not iterate — the image of a density-one set of starts need not be density-one at the next scale, which is the classical obstruction and is not removed by anything here. The exceptional tails — sustained deviations of exactly the staircase profile (`12.8.4`) — have `B`-probability zero as infinite words and vanishing density as segments, yet are not excluded for any *individual* orbit. AEH is the precise form of the missing statistical half; it is not a route to full convergence. This matches the program's honest scope (`11.8.4.4`, README). The staircase is simultaneously the cycle-sharpness family; the one-configuration-both-halves synthesis is charted at bridge.md `16.4.6`.
```

### 6.7 `aeh.md` Remark `13.6.6` — the adjudication, as drop-in

The offending clause (line 129) reads: *"…so the bulk cut is precisely what makes the integer question nondegenerate."* **The reviewer is right and this must go.** Replacement for that sentence (the surrounding remark is otherwise sound and unchanged):

```markdown
The positive odd integers are a countable, hence **Haar-null**, subset; and for them the unrestricted statement is not merely unproved but false on every convergent orbit (absorption at the fixed point writes `(1,1)` forever — the bottom regime of `13.1`), so *some* restriction to the bulk is necessary. The bulk cut is not that restriction. Applied along a single orbit it supplies no infinite sample either: above a fixed cut a convergent orbit has finitely many qualifying visits and, once the cut passes its maximum, none. What makes the integer question nondegenerate is the ensemble — the sample refreshed at growing scale (`13.2.1`) — and within it the cut keeps the narrower job of excising the bottom regime. The genericity form therefore exhibits AEH as the assertion that **this particular null set inherits genericity at scale**: the bulk segments of uniformly sampled large starts have the letter frequencies of `B`, for horizons well past the digit budget at which that is provable.
```

**Adjudication, stated flatly.** `13.6.6` is right that the unrestricted statement fails for integers and that a bulk restriction is necessary. It is wrong that the cut supplies nondegeneracy: on a single orbit the cut *is* the degeneracy, converting "wrong limit" into "no limit". The remark's remaining content — (a) measure theory proves genericity a.e. and says nothing about a prescribed null set; (b) `13.3.3`'s exceptional tails are the non-generic points of a Bernoulli shift; (c) no subshift constraint separates the integers — all stand. Point (b) needs a light touch under the ensemble form: infinite non-generic words remain the right object for `Z_2` points and for hypothetical divergent orbits, while a convergent integer orbit contributes a *finite* word whose length grows with the scale.

### 6.8 `aeh.md` Remark `13.6.7` — a fourth site the brief did not name

Line 131 describes AEH as: *"the sample space is visits along one orbit, the limit is orbit length then cut."* This is the same defective description and must change with the rest, or `13.6.7` — the remark whose entire purpose is to stop two different equidistributions being conflated — will itself carry the retired formulation. Drop-in for that clause:

```markdown
(1) **AEH's genericity form** (`13.6`): an *orbit-statistics* statement — the letter words of integer orbits are bulk-generic for the Bernoulli law `B`; the sample space is the bulk visits of uniformly sampled large starts, and the limit is the single limit in the sampling scale (`13.2.1`).
```

The contrast `13.6.7` draws with the seam-residue target survives intact, and is if anything sharper: both are now family statements with a single scale limit, differing in what is sampled (orbit visits versus forced profiles at fixed `(n,K)`).

---

## 7. The consequence chain: survives / restated / fails

| Consequence | Verdict | What changes |
|---|---|---|
| `13.3.1` ledger, error `O(2^-k)` | **Survives restated** | Conclusion becomes: density-zero exceptional set of *starting values*, finite horizon. The `k → ∞` step becomes an explicit diagonal, not a free exchange. |
| `13.3.2`, `3`-gain rate `= 1/3` | **Survives restated** | `s` even is window-decidable; same density-of-starts form. No new assumption. |
| `13.3.2`, drift / contraction of `log x` | **Does not follow; needs a stated rider** | Window equidistribution at each fixed `k` gives no upper bound on the empirical mean of the unbounded `m_+`. Needs uniform integrability of the letter statistics. Automatic for `θ < 1/4`; measured at `−0.8367 ± 0.0060` per block; **not a deduction**. |
| `13.3.3` scope discipline | **Survives, strengthened** | "almost-everywhere statements only" becomes "density statements about starting values, at finite horizon, which do not iterate". The paragraph was already the honest one; it becomes more so. |
| paper L247 "almost-everywhere contraction" | **Fails as written; survives restated** | It is not a per-orbit a.e. statement and never was one. It is: for each `ε, θ, k`, a natural-density-zero set of starting values outside which the first `⌈θ log₂ x⌉` bulk blocks equidistribute — plus the `13.3.2` rider for the contraction half. It says nothing about a fixed orbit's tail and does not iterate. |
| `13.6.4` equivalence theorem | **Survives verbatim in statement and proof**; opening definition replaced | The proof is a deterministic dictionary with explicit finite-window error control; it never uses a limit order or a single orbit. Restated over an arbitrary "visit family", it applies to (a) an infinite letter word — `Z_2` points and hypothetical divergent orbits — and (b) `13.2.1`'s ensemble family. `(q1)`, `(q2)` untouched. |
| `13.6.4`'s "orbit by orbit, no measure on starting values" selling point | **Survives** | The dictionary is still measure-free; what carries a measure is `13.2.1`, which the dictionary is then applied to. Nothing is lost. |
| `13.6.6` "the bulk cut is precisely what makes the integer question nondegenerate" | **Fails** | The cut is necessary-ish (bottom excision) but supplies no sample. Nondegeneracy comes from the ensemble. Sentence replaced (§6.7). |
| `13.6.6` rest (Haar-null framing, (a)/(b)/(c)) | **Survives** | (b) needs a clause distinguishing infinite words (`Z_2`, divergent orbits) from the growing finite words of convergent integer orbits. |
| `13.6.7`'s description of AEH's sample space | **Fails as written** | Fourth site (§6.8). |
| `13.6.1`, `13.6.2`, `13.6.3`, `13.6.5` | **Untouched** | All are statements about `B`/Haar or exact arithmetic dictionaries; none references the orbit-limit regime. `13.6.3`(i)'s "the bulk cut is literally the same on both sides" remains true. |
| `13.5` standing rule and Lemma `13.5.1` | **Untouched, and vindicated** | The new formulation is the standing rule made into a statement. Worth adding the sharpened reading: per-orbit ratios are safe exactly when the denominator is deterministic. |
| `13.4` calibration record | **Untouched; evidential value increases** | Every number was measured under the ensemble protocol. §4(b) shows the protocol runs `2.3 ×`–`4.3 ×` past the digit budget, so it tests the hypothesis rather than re-measuring a theorem. |

---

## 8. Everything that breaks or weakens, without hedging

1. **`13.2.1` and `hyp:aeh` as written are false or undefined for every starting value if Collatz is true.** Not imprecise — empty.
2. **The v3 repair made it worse.** Adding the explicit limit order converted a vague statement into a demonstrably empty one. The previous round's wording is not a constraint and should not be preserved.
3. **`13.6.6`'s nondegeneracy claim is wrong** and is the sentence the paper's L245 was written from, so the error propagated into the paper.
4. **The drift consequence does not follow from equidistribution.** `13.3.2`'s "hence contraction of `log x` at the classical rate" is currently asserted as a deduction and is not one. It needs a uniform-integrability rider, stated. This is a pre-existing defect that the reformulation exposes rather than creates.
5. **"Almost-everywhere" is the wrong phrase throughout** and must become "all but a density-zero set of starting values, at a prescribed finite horizon". Sites: `aeh.md` `13.3.3`, paper L247, `README.md` L40 ("the ledger, the 1/3 rate, drift — almost-everywhere statements only"), `bridge.md` L69 ("all almost-everywhere").
6. **Nothing survives about a fixed orbit's infinite tail, in any formulation.** The old wording invited the reading that AEH controls almost every orbit forever. It does not and cannot: any statement of that shape about integers is a statement about starting values at a scale.
7. **The consequences do not iterate.** Descent of a density-one set of starts to a lower scale does not give a density-one set at that lower scale. This is the classical obstruction; naming it is the honest thing to do and it should be named in `13.3.3`.
8. **Four sites, not three.** The brief named `hyp:aeh`, `13.2.1`, `13.6.4`. `13.6.7` (L131) carries the same description and must move with them, or the anti-conflation remark will be the last page still asserting the retired regime.
9. **`13.4`'s methodology sentence sits awkwardly with `13.5`'s rule.** L36 says statistics use "per-orbit means with across-orbit standard errors"; L53 forbids ratio estimators over correlated visit sequences. Both are right, and the reconciliation should be on the page: a per-orbit mean is safe exactly when its denominator is deterministic (fixed horizon, non-binding cut, no stopping rule) and unsafe when the denominator is the random count of qualifying visits. The quenched form of `13.2.1` needs per-orbit statistics, so this reconciliation is now load-bearing rather than decorative.
10. **The statements say `x_exit > X`; the code cuts on `ω_+ > X`** (`aeh_calibration.py` L361/L402, `aeh_symbolic.py` L566). Since `y + 1 = 2^m 3^a ω`, cutting on `ω` is strictly stronger than cutting on `x_exit`; harmless asymptotically and harmless in the runs (the cut never binds), but the statement and the code should say the same thing.
11. **Appendix A's commit pin `6a9183a` (paper L263) dies the moment `aeh.md` changes**, as does the PDF at `paper/collatz-reduced-v3.pdf`. Both are Phase-2 mechanics, and this repository has already had one round spent on exactly this failure.
12. **Paper L42's Version note explicitly advertises the old repair** ("states the order of its two limits") and becomes false.
13. Cosmetic but real: paper L175 and L259 say "typical orbits" where the hypothesis is now about typical *starting values*.

---

## 9. Open questions I could not settle

1. **Literature comparison for the contraction corollary.** The restated consequence is "almost every starting value, in natural density, descends below `x^η` for every fixed `η > 0` within `O(log x)` blocks", and with the cut pushed to `X_N = N^{o(1)}` it reaches sub-polynomial levels. This is the same genre as the unconditional density theorems (Terras 1976; Korec's `x^{0.7924}`; Tao's logarithmic-density result reaching almost-bounded values). **Before this is printed as a consequence of AEH, someone must check whether the conditional conclusion is weaker than what is already known unconditionally, and in which density.** Natural versus logarithmic density is not a detail here — it may decide whether the statement is worth making. I did not do this check; it needs the actual papers, and the repository's bibliography does not currently cite Tao.
2. **How far past `θ = 1/4` does the base case actually extend?** The `TV ≤ P_B(S_n ≥ L)` bound is tight in the sense that `S_n/n → 4`, but empirical *frequencies* are much coarser than the joint law, and a cleverer argument might prove frequency-equidistribution well past the joint-law threshold. I could not find the barrier. The honest statement is "provable to `θ < 1/4` by this argument", not "unprovable beyond".
3. **Is the uniform-integrability rider of `13.3.2` derivable from AEH at every `k` plus something already on the page?** I could not derive it, and I could not construct a counterexample either. The obstruction is one-sided and precise (`liminf` yes, `limsup` no, and the descent identity `x_{n+1}+1 = 3^{m}(x_n+1)/2^{m+s} + (1 - 2^{-s})` gives bounds in the wrong direction), which is why I recommend stating it as a rider rather than guessing.
4. **The right treatment of horizons past the descent.** For `θ ≥ 1/β` the cut genuinely binds, the tally denominator becomes random, and `13.5`'s rule bites. I have quantified over all `θ > 0` and noted the regime, but a formulation that is clean *and* covers `θ ≥ 1/β` with a deterministic denominator eluded me. If the author wants only the sub-descent regime, deleting the cut and restricting to `θ < 1/β` gives a simpler statement at the cost of making the bottom-regime exclusion conditional on the drift.
5. **`D_k` is never defined in `aeh.md`.** `13.2` writes the window state as `(ω mod 2^(k+2), min(d, D_k))` and no section fixes `D_k`. Out of scope here, not renamed, but it is a genuine gap in the definition the hypothesis quantifies over.

---

## 10. Verification table (every quoted value read, not recalled)

| Value | Source |
|---|---|
| `13.2.1` text, "as the orbit length and `X` grow" | `aeh.md` L22 |
| `13.6.4` "in the limit orbit length `→ ∞` then `X → ∞`" | `aeh.md` L101 |
| `13.6.6` "the bulk cut is precisely what makes the integer question nondegenerate" | `aeh.md` L129 |
| `13.6.7` "the sample space is visits along one orbit, the limit is orbit length then cut" | `aeh.md` L131 |
| `13.5` standing rule, ratio estimators forbidden | `aeh.md` L53 |
| drift `−0.4166 ± 0.0037` / odd step, `−0.8367 ± 0.0060` / block; `2(log₂3 − 2) = −0.8301` | `aeh.md` L41 |
| `P(a=0) = 2/3`, `P(a=1) = 19/63`, `P(a≥2) = 2/63`; `P(d=1) = 1/3`, `P(d=2) = 20/63` | `aeh.md` L121–122 |
| `P_B(a ≥ j) ≤ 2·(0.93)^j` | `aeh.md` L88 |
| `E[m] = 2`, `P(m=j) = 2^-j`, `P(r=j) = 2^-j` | `aeh.md` L63 |
| cylinder mass `2^{-S}`, `S = Σ(m_i + r_i)` | `aeh.md` L72 |
| one odd class mod `2^{S+1}` per length-`n` word | `itinerary.md` L46–53 (Thm `14.15.1.5`) |
| `hyp:aeh` text and the two-limit order | `paper/collatz-reduced-v3.tex` L241–243 |
| "The cut is what makes the hypothesis nondegenerate" | `paper/collatz-reduced-v3.tex` L245 |
| "AEH implies the ledger … and almost-everywhere contraction" | `paper/collatz-reduced-v3.tex` L247 |
| "Hypothesis~\ref{hyp:aeh} states the order of its two limits" | `paper/collatz-reduced-v3.tex` L42 |
| digit budget, `σ + k + 2`, "empirical mean `σ ≈ 4.0`" | `paper/collatz-reduced-v3.tex` L168 |
| Appendix A commit pin `6a9183a` | `paper/collatz-reduced-v3.tex` L263 |
| protocol: starts `[2^70,2^71)`, burn-in `10`, horizon `30`, cut `2^30`, `154,389` bulk visits, seed `31005` | `aeh.md` L125; `experiments/aeh_symbolic.py` L539–584 |
| "no stopping rule, no cut" in the fixed-horizon drift estimator | `experiments/merle_aeh_key_check.py` L268–273 |
| cut applied to both endpoints in the biased variants | `experiments/merle_aeh_key_check.py` L229–230 |
| anomaly protocol: `100`-bit starts, `32` steps, no cut; `140`-bit, `150` steps | `experiments/aeh_anomaly.py` L15–29, L66–75 |
| "almost-everywhere statements only" downstream | `README.md` L40; `bridge.md` L69 |

Derived numbers, and how: `β = 2(2 − log₂3) = 0.830075`; `1/β = 1.204718`; digit-budget horizon `= 1/4` block per bit from `E[m+r] = 2 + 2 = 4`; ratio `1.204718 / 0.25 = 4.819`; provable fraction of a descent `0.25 / 1.204718 = 0.2075`. Flagship protocol: `L = 70`, budget `70/4 = 17.5` blocks, run `10 + 30 = 40` blocks `= 2.29 ×` budget, tallied blocks `11–40` of which `18–40` (`23` of `30`, `76.7%`) lie beyond it. `aeh_anomaly` X2(b): `L = 140`, budget `35`, horizon `150 = 4.29 ×`. Uniform-start absorption law `P(v_3(x+1) = j) = 2·3^{-(j+1)}`, giving `2/3, 2/9, 1/9` against `13.6.5`'s bulk `2/3, 19/63, 2/63`.
