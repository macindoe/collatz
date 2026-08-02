# Findings: the exceptional set and the base-case lemma (v3 round 3, delegate D)

**Task:** `briefs/v3r3-basecase-density-brief.md`. Read-only round; the only file written is this one.
**Read at:** `main` = `dc61306`, working tree clean apart from the round-3 briefs.
**Inputs used, not reopened:** `briefs/v3r3-aeh-object-findings.md` §3, §4, §6, §7 (Option 1, `W_{k,D}`, the
cap `D`, `π_{k,D}`, total variation, two-sided `B̂`, §3.6's boundary treatment — all fixed);
`briefs/v3r3-inselmann-horizon-findings.md` §0, §2.5, §3 (S1 verified and credited below, §5.4).

**Late input, reconciled in §6:** `briefs/v3r3-cut-weighting-findings.md` (the parallel Wave 2 delegate)
landed while this was being written. It rewrites both of my sites and independently claims the anchor
`13.2.3`. **I yield the number**: their `13.2.3` (the clock and "admissible") is cited from inside
Hypotheses `13.2.1` and `13.2.2` themselves, mine only from prose, so theirs is the expensive one to
move. My anchors are therefore **`13.2.4`** (the base-case lemma) and **`13.2.5`** (the shell
proposition). Nothing is renumbered; all three are new appended anchors from this round. Their work and
mine are compatible and in two places mutually reinforcing (§6.1); the merged drop-ins are in §5.

---

## 0. Verdict, unhedged

**A's Option 1 justification survives assembly. All four gaps close. `θ < 1/4` is a theorem, at every
finite block length simultaneously, and nothing is provable past `1/4` by this argument.**

A's §6 item 1 says the record's own base case already proves the strengthened form because `aeh.md` L34
bounds `TV(Law(W_n), B^{⊗n})` — the joint law of the whole length-`n` word, not a marginal. I have
checked that claim to the ground and it is correct, for the reason A gives and with no hidden cost:

* the bound is genuinely on the joint word law (§3.2), and a total-variation bound on a joint law
  transfers **every** event of that law, so one bound serves every finite block length at once;
* the four gaps the reviewer names are all closable, and none of them is `L`-dependent in a way that
  reintroduces a marginal: gap (i) is a counting statement about the sampling window, gap (iii) removes
  a fixed number of visits, gap (iv) is a magnitude estimate, and gap (ii) — the only one that touches
  `L` — costs one union bound over a **finite** alphabet plus one explicit truncation;
* the strengthened hypothesis therefore has **exactly** the same unconditional range as the weaker one.
  Retaining `L = 1` buys nothing. This is the decision input A said it was, and it holds.

Two things the author should hear plainly alongside that verdict:

1. **As written, L34 was a sketch and "theorem" was premature.** L34 states the count for `x` uniform on
   `[2^L, 2^{L+1})` only, and closes the distance to the hypothesis with the eleven words "concentration
   under `B` and the dictionary of `13.6.3`(iii)–(iv) carry it to the window states". Neither the
   truncation of the countable letter alphabet nor the segment's missing past appears, and the bulk cut
   is not mentioned at all (its support sat at L32 and was `1/β`, which delegate B has refuted). After
   **Lemma 13.2.4** below it is a theorem; before it, it was a plan for one.
2. **The frontier is exactly `1/4`, and the argument dies exactly there, not near there.** The
   large-deviation rate is `I(θ) = log 2 − H(2θ)` nats per bit of start, `H` the binary entropy —
   `0.0201` at `θ = 0.20`, `0.00080` at `θ = 0.24`, `8·10^-8` at `θ = 0.2499`, and **exactly `0`** at
   `θ = 1/4`. Nothing in the assembly can be pushed past `1/4`; per the README stopping rules I did not
   try, and I report that the barrier is an exact entropy identity rather than a slack estimate.

---

## 1. Notation, fixed once

The brief names a collision: `aeh.md` L34 uses `L` for the bit-length of the start; Option 1 uses `L`
for the block length. **Option 1 wins** — `L` is the block length everywhere below, because A's
`π^{(L)}_{k,D}` is fixed and appears in the drop-ins. The bit scale becomes `b`:

| symbol | meaning |
|---|---|
| `b` | `⌊log₂ N⌋`, the bit scale of the sampling window (was `L` at `aeh.md` L34) |
| `L` | block length: the length of a letter word `w`, or of a window block (A §3.3) |
| `x` | the sampled start, odd, uniform on `[N, 2N)` |
| `y_{−1} := x`, `y_n := G^{n+1}(x)` | the doors; `y_n` is `x_exit` of block `n` (`13.6.3`(i)(a)) |
| `ℓ_n := stratum(y_n) = (m_n, r_n)` | the letter at block `n`; `= (m_{+,n}, s_{n+1})` (`13.6.3`(i)) |
| `S_n := Σ_{i<n}(m_i + r_i)` | total exponent of the length-`n` word — the **clock** |
| `T = T_N := ⌈θ log₂ N⌉` | the block horizon |
| `B` | the letter law `P(m,r) = 2^{−(m+r)}` (`13.6.1`); `B[w] = Π 2^{−(m_i+r_i)}` |
| `k`, `D`, `W_{k,D}`, `π_{k,D}`, `π^{(L)}_{k,D}`, `B̂` | exactly A §3, unchanged |
| `W` | the letter past-window of `13.6.3`(iii) (A's `W`), `W ≥ D` |
| `I(θ) := log 2 − H(2θ)` | `H(p) = −p log p − (1−p) log(1−p)`, natural log |

`ℓ_{−1} = stratum(x)` is a genuine letter: every positive odd `x` is a door and `G(x) = x_exit` of the
first block. **Verified numerically** (C0, §7): `G = T^{m}` on `4,000` random `64`-bit odd starts,
`x_exit(R(x)) = G(x)`, and `stratum(y_n) = (m_{+,n}, s_{n+1})`, `0` failures.

---

## 2. Finding 1 — the exceptional set is a triangular array

### 2.1 The site, verified

`aeh.md` L32, final sentence, read at `dc61306`:

> Because the bad density vanishes at every scale, the union of the bad sets has natural density zero
> in the integers — so the statement does deliver "almost every integer", for a finite-horizon property,
> with the exceptional set depending on `ε` and `θ`.

`paper` L301–304, same claim in the paper's voice:

> AEH implies the ledger with error $O(2^{-k})$ via Theorem~\ref{thm:onestep}, in the form the
> hypothesis has: for every $\varepsilon$ and every horizon rate, all but a set of starting values of
> natural density zero carry those frequencies along their first $\lceil\theta\log_2 x\rceil$ bulk
> blocks.

### 2.2 The inference is invalid, and the counterexample is one line

For each `N` the hypothesis supplies a set `Bad_N ⊆ [N, 2N)` with `|Bad_N| / |odd [N,2N)| → 0`. The
claim is that `⋃_N Bad_N` has natural density zero. **It does not follow.** Take

```text
Bad_N  :=  { x odd : N ≤ x < N(1 + 1/log N) }.
```

Its density inside `[N, 2N)` is `~1/log N → 0`, so the hypothesis of the inference holds; and every odd
`x ≥ 3` lies in `Bad_x`, so `⋃_N Bad_N` is **all** the odd integers — natural density one, the maximum
possible. The inference fails by the widest margin available.

The structural reason is the one the reviewer gives and it is worth stating on the page, because it is
not a technicality about limits. The family is a **triangular array**: `Bad_N` is not "the integers of
size `N` that fail one fixed property", it is "the integers of size `N` that fail *the property indexed
by `N`*" — the horizon `T_N = ⌈θ log₂ N⌉` and the cut `X_N` both move with `N`. A fixed `x` belongs to
`[N, 2N)` for about `x/2` different `N`, and is asked a different question by each of them. The union
over all `N` is therefore the set of integers failing **at least one of a growing family of different
tests**, which no amount of per-test smallness controls.

### 2.3 The dyadic-shell formulation, and the proof

Evaluate each `x` once, at its own scale. Define the **shell index** `β(x) := ⌊log₂ x⌋`, so
`x ∈ [2^{β(x)}, 2^{β(x)+1})`, and take the sampling family along `N = 2^b`, `b = 1, 2, 3, …`.

> **Proposition 13.2.5 (the exceptional set, at shell scale).** Fix `ε > 0`, a horizon rate `θ`, a cut
> sequence `(X_N)`, and an observable — a finite letter word `w` (for `13.2.1`), or a triple `(k, D, L)`
> (for `13.2.2`). For each `b` let
>
> ```text
> Bad_b := { x odd, 2^b ≤ x < 2^(b+1) : x fails the ε-test at sampling scale N = 2^b },
> β_b   := |Bad_b| / 2^(b−1)   (the shell density; 2^(b−1) odd integers per shell).
> ```
>
> If `β_b → 0` — which is exactly what `13.2.1` (resp. `13.2.2`) asserts along `N = 2^b` — then
>
> ```text
> Bad := ⋃_b Bad_b
> ```
>
> has **natural density zero in the odd integers, hence in the integers**: `#{x ∈ Bad : x ≤ X} = o(X)`.
> Each `x` appears in exactly one `Bad_b`, so `Bad` is the set of odd integers that fail the test *at
> their own scale* — a single property of `x`, not a family.
>
> **Proof.** Let `η > 0` and pick `b_0` with `β_b < η` for all `b > b_0`; put
> `C = Σ_{b ≤ b_0} |Bad_b| ≤ 2^{b_0}`, a constant. For `X ≥ 2` choose `B` with `2^B ≤ X < 2^{B+1}`.
> Every `x ∈ Bad` with `x ≤ X` lies in some `Bad_b` with `b ≤ B`, so
>
> ```text
> #{x ∈ Bad : x ≤ X}  ≤  C + Σ_{b_0 < b ≤ B} η·2^(b−1)  ≤  C + η·2^B  ≤  C + η·X.
> ```
>
> Hence `limsup_X #{x ∈ Bad : x ≤ X}/X ≤ η` for every `η > 0`, i.e. the limit is `0`. ∎

Two remarks on the proof, both load-bearing:

* **The geometry of the shells is what makes it work.** The only step that uses anything is
  `Σ_{b ≤ B} 2^{b−1} ≤ 2^B ≤ X`: the shells' sizes are dominated by the last one. Any family
  `N_1 < N_2 < …` with `N_{j+1}/N_j ≥ λ > 1` does the same job, with
  `Σ_{N_j ≤ X} N_j ≤ X·λ/(λ−1)` and the same conclusion; the constant degrades as `λ → 1`, and at
  `λ = 1` (all `N`) the sum is unbounded and the argument, correctly, dies. **The dyadic family is the
  canonical `λ = 2` case and is the one to print.**
* **Nothing is assumed beyond the hypothesis.** `13.2.1` quantifies over all `N → ∞`; restricting to
  `N = 2^b` is a specialisation, so `13.2.5` is a corollary of the hypothesis and, at `θ < 1/4`, of
  Lemma 13.2.4 below.

### 2.4 What the unrestricted union does and does not satisfy — stated exactly

**Does satisfy.**

1. *Per-scale smallness, which is the hypothesis itself.* For every `N`,
   `|Bad_N| / |odd [N,2N)| → 0`. This is the whole of what is asserted and it is not weakened by
   anything here.
2. *Geometric subfamilies.* For any `λ > 1` and any `(N_j)` with `N_{j+1}/N_j ≥ λ`, `⋃_j Bad_{N_j}` has
   natural density zero. (Proof as above, with `λ/(λ−1)` in place of `2`.)
3. *Upper density along any sequence.* For any single sequence `N_j → ∞`,
   `limsup_j |Bad_{N_j}|/|odd[N_j, 2N_j)| = 0`.

**Does not satisfy.**

4. *`⋃_{N ∈ ℕ} Bad_N` has no density bound at all* — §2.2 exhibits a legal family whose union is
   everything. In particular the sentence at `aeh.md` L32 is false as an implication, and the phrase
   "the union of the bad sets" should not appear on the page.
5. *No iteration, no transfer between scales.* `13.3.3` already says this ("the image of a density-one
   set of starts need not be density-one at the next scale") and `13.2.5` does not change it: the shell
   statement is about the *starts*, and says nothing about where they go.
6. *Not a statement about any individual orbit or any orbit's tail.* Unchanged from `13.3.3`.

**The dependence list is longer than the page currently says.** L32 says "with the exceptional set
depending on `ε` and `θ`". Under Option 1 it depends on `ε`, `θ`, the cut sequence `(X_N)`, and the
observable — the word `w`, or the triple `(k, D, L)`. All four must be fixed before the exceptional set
is named. The drop-in at §5.1 says so.

---

## 3. Finding 2 — the base case, assembled

### 3.1 The two sites, verified

`aeh.md` L34: "**Hypothesis 13.2.1 is therefore a theorem for every `θ < 1/4`.**"
`paper` L288–289: "Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every horizon rate $\theta < 1/4$."

The supporting text at L34 is one sentence of count plus one clause of gesture:

> By Theorem `14.15.1.5` (itinerary.md) the odd integers following a given length-`n` letter word form
> exactly one class mod `2^{S+1}`, `S = Σ(m_i + r_i)`; so for `x` uniform on `[2^L, 2^{L+1})` the
> length-`n` word is *exactly* `B`-distributed on `{S + 1 ≤ L}`, and
> `TV(Law(W_n), B^{⊗n}) ≤ P_B(S_n ≥ L)`. With `E[m + r] = 4` (`13.6.1`) this is exponentially small for
> `n ≤ (1/4 − ε)L`; concentration under `B` and the dictionary of `13.6.3`(iii)–(iv) carry it to the
> window states.

The count is right. The `TV` step is right (§3.2). Everything after the semicolon is the sketch.

### 3.2 The clock, and why the base case is natively in it

The brief's directive lands here without effort, and it improves the statement rather than complicating
it. `{S_n + 1 ≤ b}` is an **exponent-budget** event: it says the first `n` letters have not outspent the
start's supply of binary digits. In that clock:

* **The frontier is `1` unit of total exponent per bit of start, exactly**, and on that range the word
  law is not approximately `B` but *exactly* `B` — there is no estimate in the statement at all, only
  Theorem `14.15.1.5`'s class count. Since `n ↦ S_n` is nondecreasing, `n(γ) := max{n : S_n + 1 ≤ γb}`
  is a stopping time of the word, and the law of the stopped word is exactly the `B`-law of the stopped
  word, for every `γ ≤ 1`.
* **The conversion to blocks is the only estimate**, and it divides by `E[m + r] = 4` (`13.6.1`). That
  is delegate B's disputed exchange rate — and here, and only here, it is **licensed**, because on this
  range the word *is* `B`, so `E[m+r] = 4` is a theorem rather than an assumption. B's §2.6 says exactly
  this; the base case is the row of B's table where the answer is "yes".
* **Comparison with Inselmann becomes a comparison of two numbers in one unit** (B's S2/S3): our exact
  range is `S_n ≤ b`, his protected window is `S_n ≤ 4.8188… b`, ratio `(1 − log₂√3)^{-1} = 4.8188…`,
  unconditional in either time. No conversion, nothing to dispute.
* **This is exactly the frame the cut-weighting delegate arrived at independently**, from the other
  direction: their budget rate `τ` is my `γ`, their "protected" clause is my `(c)`, and their
  "consistent" clause `4θ < τ` is my `(b)` — the large deviation. Their `τ < 1` range and my `γ ≤ 1`
  range are the same range and are the same theorem. See §6.1; nothing in either had to move.

The `TV` bound is exact and elementary, which is worth printing because it retires the vague
"exponentially small":

```text
S_n = Σ_{i<n}(m_i + r_i) is the waiting time for the 2n-th head in a fair coin sequence, so
      P_B(S_n ≥ J)  =  P( Bin(J − 1, 1/2) < 2n )        exactly, for all n ≥ 1, J ≥ 2n.
```

**Verified exactly, in rational arithmetic** (C3, §7): equality at `(n,b) = (5,40), (10,60), (12,100),
(25,120), (30,121)`, `Fraction`-exact, no floating point. Chernoff on the right-hand side at
`n = ⌈θb⌉` gives rate `I(θ) = log 2 − H(2θ)`, the optimal tilt being `e^λ = 2(1 − 2θ)`, which requires
`λ > 0`, i.e. **`θ < 1/4` exactly**. Past `1/4` the tail is the typical event and the bound is vacuous —
the barrier is structural, not a slack constant.

### 3.3 The lemma

> **Lemma 13.2.4 (the base case, unconditional).** Let `θ > 0` and let `(X_N)` satisfy `X_N → ∞`,
> `log X_N = o(log N)`. For each `N` draw `x` uniformly from the odd integers of `[N, 2N)`, and use the
> notation of §1 with `b = ⌊log₂ N⌋`, `T = ⌈θ log₂ N⌉`. Then:
>
> **(a) Word law (exponent time).** For every `n ≥ 0` and every `J ≥ 1`,
>
> ```text
> TV( Law(ℓ_{−1}, …, ℓ_{n−1}),  B^(⊗(n+1)) )   ≤   2^(J+2)/N  +  P_B(S_{n+1} ≥ J).
> ```
>
> If `N = 2^b` the first term is absent at `J = b`; the general-window cost is that term and nothing
> else. Consequently the same bound holds for `Law(ℓ_0, …, ℓ_{n−1})` against `B^{⊗n}`.
>
> **(b) The tail, exactly.** `P_B(S_n ≥ J) = P(Bin(J−1, 1/2) < 2n)`. For `θ < 1/4` choose
> `η ∈ (0, 1 − 4θ)` and `J = ⌈(1−η)b⌉`; then both terms of (a) are `e^{−Θ(b)}` at `n = T + c` for any
> constant `c`, with exponential rate `min(η log 2, (1−η)·I(θ/(1−η)))` per bit. Write `δ_N` for the
> resulting bound; `δ_N = N^{−Θ(1)}`.
>
> **(c) The cut does not bind.** In door coordinates, for every step,
> `y_{i+1} + 1 > (y_i + 1)·(3/2)^{m_i}·2^{−r_i} ≥ (y_i + 1)·2^{−(m_i+r_i)}`, hence
> `log₂(y_n + 1) > log₂ N − S_n` for every `n`. Therefore on the event `{S_{T+1} ≤ (1−η)b}` every one of
> the first `T` exits satisfies `x_exit > N^{η} − 1`, which exceeds `X_N` for all large `N`. So off a
> set of starts of density `≤ δ_N`, **every block index in the horizon is bulk**, the bulk filter is
> vacuous, and the tally denominator is the deterministic `T`. The same holds for the code's stronger
> cut on the core `ω_+`, since `log₂ ω_{n+1} = log₂(y_n+1) − m_n − a_{n+1} log₂3` and, off a further set
> of density `o(1)`, `max_{n<T}(m_n + a_{n+1} log₂ 3) = O(log T) = O(log log N)`.
> *This clause is the cut-weighting delegate's `13.2.3` altitude bound, arrived at independently; their
> derivation (`T_1(y) ≥ y/2`, so `log₂ x_exit(n−1) ≥ log₂ x − S_n` for every odd `x`, every `n`, with no
> exceptional set) is simpler than mine and should be the one printed. Mine adds only the extra
> `(3/2)^{Σm}` of slack and the `ω_+` extension.*
>
> **(d) Letter frequencies — Hypothesis 13.2.1.** For every finite letter word `w` of length `L` and
> every `ε > 0`,
>
> ```text
> density{ x : |f_N(w, x) − B[w]| > ε }  ≤  δ_N + 2·exp( −2ε²(T−L+1)²/(T L²) )  →  0.
> ```
>
> **(e) Window frequencies — Hypothesis 13.2.2.** For every `k`, `D`, `L` and every `ε > 0`,
>
> ```text
> density{ x : ‖ν^(L)_{k,D,N}(x) − π^(L)_{k,D}‖_TV > ε }  →  0,
> ```
>
> total variation on the finite window alphabet, `|A_{k,D}| ≤ 2^{k+1}D³(D+1)`.
>
> **(f) What is not claimed.** The convergence in (d), (e) is **not uniform** in `(w, k, D, L, ε)`: the
> threshold `N₀` depends on all of them, through the past-window `W` and the letter truncation `Λ` of
> the proof. Nothing in `13.2.1`, `13.2.2` or `13.3` asks for uniformity. At `θ = 1/4` exactly, (b)
> gives `I(1/4) = 0` and the lemma is empty.

> **Corollary 13.2.4.1 (the named implication).** For every `θ < 1/4` and every admissible `(X_N)`,
> Lemma `13.2.4`(d) *is* the conclusion of Hypothesis `13.2.1` and Lemma `13.2.4`(e) *is* the conclusion
> of Hypothesis `13.2.2`. Hence both hold unconditionally in that range, at **every** finite block
> length, and `13.2.5` upgrades them to natural density zero at shell scale.

**The lemma proves the cemetery form too, and more easily.** The cut-weighting delegate replaces the
bulk cut by an exponent budget `Λ_N = ⌈τ log₂ N⌉` and a cemetery symbol `†`: block `n` is tallied as
`ℓ_n` if `S_n < Λ_N` and as `†` otherwise, at deterministic weight `1/(T_N − L + 1)`, with `B[w] = 0`
for any `w` containing `†`. That statement is **strictly stronger** than the cut form — it additionally
asserts `4θ < τ` — and Lemma `13.2.4` delivers it at `τ < 1` without a new argument:

* take `J = Λ_N` in (a); then by (b), `S_{T+1} < Λ_N` off a set of density `e^{−Θ(b)}` whenever
  `4θ < τ`, so `ℓ̃_n = ℓ_n` at every tallied block and **`†` never appears** on the good set;
* on that set the tallied word is the letter word, and (d), (e) apply verbatim;
* the extra assertion `4θ < τ` is exactly (b), i.e. exactly the large deviation whose rate is
  `I(θ)` — which is why `τ < 1` and `θ < 1/4` are one range and not two.

The cemetery reformulation is in fact *native* to the lemma: `{S_n + 1 ≤ J}` is the event the cylinder
count is stated on, so a budget-indexed hypothesis is the shape the base case already had. This is
recorded as a compatibility finding, not as a preference between formulations — the choice is theirs.

### 3.4 Proof, gap by gap

#### (i) Dyadic blocks to general `[N, 2N)` — **closes**

Fix `J`. Partition `ℤ` into blocks `[c·2^J, (c+1)·2^J)`. Let `E` be the event that `x` lies in one of the
blocks **entirely contained** in `[N, 2N)`. Then:

* *Off `E` there is very little.* `[N,2N)` meets at most two incomplete blocks, so `E^c` holds for fewer
  than `2^J + 1` odd integers out of `≥ (N−1)/2`, whence `P(E^c) ≤ 2^{J+2}/N` for `J ≥ 2`, `N ≥ 12`.
* *On `E` the count is exact.* A complete block of length `2^J` contains each odd residue class mod
  `2^J` exactly once; so conditionally on `E`, `x` is **exactly uniform** on the `2^{J−1}` odd residues
  mod `2^J`. By Theorem `14.15.1.5` the odd integers whose length-`(n+1)` word is `W` form exactly one
  odd class mod `2^{S(W)+1}`, which splits into `2^{J−1−S(W)}` odd classes mod `2^J` whenever
  `S(W) + 1 ≤ J`. Hence `P(word = W | E) = 2^{J−1−S(W)}/2^{J−1} = 2^{−S(W)} = B[W]`, exactly.
* *Total variation.* Two laws agreeing atom-by-atom on a set `𝒢` satisfy
  `TV ≤ ½(μ(𝒢^c) + ν(𝒢^c)) = ν(𝒢^c)` (the two are equal since the laws agree on `𝒢`), so
  `TV(Law(word | E), B^{⊗(n+1)}) ≤ P_B(S_{n+1} ≥ J)`. Adding `P(E^c)` gives (a).

The dyadic case `N = 2^b`, `J = b` is A's / L34's statement with `P(E^c) = 0`; the general window costs
`2^{J+2}/N` and nothing else. **This is the whole of gap (i).**

**Verified** (C1, C2, C4, §7). C1: exhaustive over all `2^{J−1}` odd residues mod `2^J` for
`J = 18, 20, 22`; every word with `S+1 ≤ J` realised by exactly `2^{J−1−S}` residues, `0` failures out
of `65,535` / `262,143` / `1,048,575` distinct words. (The word counts are exactly `2^{J−2} − 1`,
matching `Σ_{S=2}^{J−1} Σ_n C(S−1, 2n−1) = Σ_{S=2}^{J−1} 2^{S−2}` — an independent check on the
enumeration.) C2: exhaustive over `[N, 2N)` for seven windows near `10^6`–`3·10^6`, dyadic and
non-dyadic; measured `TV` at `n = 3` is `0.0152`–`0.0305` against `P_B(S_3 ≥ b) = 0.0133`–`0.0207`, and
at `N = 2^{21}` versus `N = 2^{21}+1` the measured `TV` values are `0.015212` and `0.015213` — the
non-dyadic window is not distinguishable from the dyadic one at this scale, which is the content of the
gap. C4: at the scale the lemma is actually used — `3,000`-bit starts, `n = 600` letters — the
length-`n` word is invariant under `x ↦ x + t·2^{S_n+1}` (`0` failures in `40` trials) and **not**
invariant under `x ↦ x + t·2^{S_n}` (a witness found in all `40`), so the modulus is exactly right.

#### (ii) Concentration of empirical pattern frequencies — **closes**

*Letters (the primary form under Option 1a).* Fix a word `w` of length `L`. Under `B^{⊗n}`,
`f_n(w) = (n−L+1)^{−1}#{i : (ℓ_i,…,ℓ_{i+L−1}) = w}` has `E f_n(w) = B[w]` exactly, and changing one
letter changes the count by at most `L`; McDiarmid's bounded-difference inequality gives

```text
P_B( |f_n(w) − B[w]| ≥ t )  ≤  2 exp( −2 t² (n−L+1)² / (n L²) ).
```

Transfer by (a): `density{x : |f_N(w,x) − B[w]| > ε} ≤ δ_N + 2exp(−2ε²(T−L+1)²/(T L²))`. **No truncation
of the letter alphabet is required at any point.** The alphabet is countable, but the hypothesis is
cellwise on the letter side (A §3.4) — one word at a time — and McDiarmid needs only the bounded
difference, which holds uniformly. The brief's warning about geometric tails applies to the window side,
not here.

*Windows.* Here the truncation is real and is handled rather than assumed. Fix `k, D, L, ε`; let
`A = A_{k,D}` be the window alphabet, `|A| ≤ 2^{k+1}D³(D+1)`, and set `ε' = 2ε/|A|^L`, so that
controlling every one of the `≤ |A|^L` block cells to `ε'` gives `TV ≤ ε`. Three ingredients:

1. *Reduction to letters.* By `13.6.3`(iii), for `W ≥ D` the `L`-block of capped windows at visit `n` is
   an explicit function `Ψ` of the letter window `ℓ_{n−1−W}, …, ℓ_{n+L−2+⌈(k+1)/2⌉}` — length
   `P := W + L + ⌈(k+1)/2⌉ + 1` — off the event `{a_i ≥ W` for some `n ≤ i < n+L}`, whose `B`-mass is
   `≤ 2L(0.93)^W` by `13.6.3`(iv). Choose `W` with `2L(0.93)^W < ε'/8`, i.e.
   `W = O(log(L/ε') ) = O(L log|A| + log(1/ε))`.
   *Worth recording:* four of `W_{k,D}`'s five coordinates carry **no** exceptional event at all —
   `min(s_n,D) = min(r_{n−1},D)` and `min(σ_n,D) = min(r_{n−1}+m_n, D)` are outright letter functions,
   and `min(d_n,D)`, `min(a_{+,n},D)` are exception-free once `D ≤ W` (`13.6.3`(iii)'s own clause,
   "`a ≥ W` forces `d > D_k`, so the cap applies"). Only the `ω`-residue needs `a` exactly, and it is
   the sole carrier of the `2L(0.93)^W`.
2. *Truncation.* Choose `Λ` with `P · 2^{1−Λ} < ε'/8`. Letters with `m > Λ` or `r > Λ` have `B`-mass
   `≤ 2^{1−Λ}`; lump them into one symbol `★`. The frequency of `★` is the empirical mean of an i.i.d.
   indicator sequence and concentrates by Hoeffding; the frequency of windows containing a `★` is at
   most `P` times it. On the complement, `Ψ^{−1}(cell)` is a **finite** set of at most `Λ^{2P}` letter
   patterns.
3. *Union bound.* Each of those patterns' frequencies concentrates by McDiarmid as above; union over
   `≤ Λ^{2P}` patterns and over `≤ |A|^L` cells — all finite, all fixed before `N → ∞`. Add the boundary
   term of (iii). Each cell lands within `ε'`, so `TV < ε`.

Every constant here (`W`, `Λ`, `P`) depends on `(k, D, L, ε)` and on nothing else; that dependence is
Lemma 13.2.4(f), and it is the only price.

**Verified** (C5, C8, §7). C5 measures the frequencies of the two-letter patterns `((1,1),(1,1))`,
`((1,1),(1,2))`, `((2,1),(1,1))` and the three-letter pattern `((1,1),(1,1),(1,1))` at
`θ = 0.20` over `b = 750, 1500, 3000, 6000`-bit starts. Means match `B[w]` to within `2.3σ` at every
scale; the per-start standard deviation halves as `T` quadruples (`0.02338 → 0.01664 → 0.01179 →
0.00825` against `√2 = 1.414` per doubling — measured ratios `1.405, 1.412, 1.428`); and the exceptional
density at `ε = 0.03` falls `0.188 → 0.065 → 0.0127 → 0.000`. That is the hypothesis's own conclusion,
watched converging. C8 does the window side: `L = 2` blocks of the coarse capped window
`(min(s,3), min(d,3))`, `72` cells realised, per-start `TV` to the pooled reference
`0.1854 → 0.1319 → 0.0935` at `T = 300, 600, 1200`, with `TV·√T` constant at `3.212, 3.231, 3.238` —
pure `T^{−1/2}` sampling noise on a fixed finite alphabet, exactly the `√(|A|/2πT)` prediction, and
therefore `→ 0`. Per-cell standard deviations match `√(p(1−p)/T)` cell by cell.

#### (iii) Removal of the initial past-boundary — **closes, and the term is small**

A §3.6 settles what the boundary *is*: `W_{k,D}(n)` is computed from `(ω_n, d_n)` and that state's own
step and is never undefined; only the *identification of its law* uses the past. What must be shown, and
is shown here, is that the boundary's contribution to the empirical frequencies vanishes.

* **The letter form has no boundary at all.** `ℓ_n = stratum(y_n)` depends on `y_n` alone. Gap (iii) is a
  gap for `13.2.2`, not for `13.2.1`. Under Option 1a — letters primary — the boundary is not in the
  main statement.
* **For the window form the cost is `O(1/T)`, deterministically.** The reconstruction of §3.4(ii) needs
  `W` letters of past and `⌈(k+1)/2⌉ + L − 1` of future. Discard the first `W` visits and the last
  `L + ⌈(k+1)/2⌉` of the horizon: `W + L + ⌈(k+1)/2⌉ = O_{k,D,L,ε}(1)` visits out of
  `T = ⌈θ log₂ N⌉ → ∞`. Deleting `c` visits changes any frequency by at most `c/(T−L+1)`. Since `W` is
  chosen from `ε` **before** `N → ∞`, this is `o(1)`. That is the entire boundary treatment, and it
  needs no burn-in parameter in the statement — A §3.6 item 3, confirmed.
* **Nothing about the retained visits is boundary-affected.** For `n ≥ W` the past window
  `ℓ_{n−1−W},…,ℓ_{n−2}` lies wholly inside the sampled segment, so `13.6.3`(iii) applies verbatim and
  the exceptional event `{a ≥ W}` is a *letter* event whose probability is exactly its `B`-probability
  under (a). No estimate about the start's `3`-adic digits is used anywhere.
* **The transient is real, exactly located, and measured.** For uniform odd `x`,
  `a_0 = v_3(x+1)` has `P(a_0 = j) = 2·3^{−(j+1)}` — `(2/3, 2/9, 2/27, …)` — against the bulk
  `(2/3, 19/63, 2/63, …)` of `13.6.5`. **Verified** (C6, §7; `40,000` starts of `400` bits, seed
  `34004`): the measured law of `a_n` at `n = 0` is `(0.6698, 0.22005, 0.11015)`, `L¹` distance
  `0.0063` from the uniform-start law and `0.1631` from the bulk law; at `n = 1` it is
  `(0.66655, 0.26998, 0.06348)`, `L¹` distance `0.0635` from bulk; and from `n = 2` onward the `L¹`
  distance from the bulk law is `≤ 0.0086`, at the sampling-noise floor of the run. **So the transient
  occupies exactly two visits**, with total-variation deviations `0.0815` and `0.0317`, and its
  contribution to any depth-marginal frequency over the horizon is at most `0.114/T`. The proof's bound
  (`W ~ log(1/ε')` discarded visits) is far more generous than the measured behaviour; nothing depends
  on closing that gap.

#### (iv) Treatment of the bulk cut — **closes; this is delegate B's S1, verified and credited**

B's S1 (`briefs/v3r3-inselmann-horizon-findings.md` §3) states: for every `θ < 1/4` and every cut with
`log X_N = o(log N)`, the cut binds on an exponentially small density of starts, unconditionally and
without Inselmann. **I verify it and adopt it.** B's route is through the `T`-step count ("each `T`-step
lowers `log₂` by at most `1`"); I re-derive it directly in door coordinates, which avoids the
block↔step dictionary the round is otherwise disputing and gives a slightly better constant:

```text
u_i := y_i + 1.   With q_i = u_i / 2^(m_i),
u_{i+1} = ( 3^(m_i) q_i − 1 + 2^(r_i) ) / 2^(r_i)
        = 3^(m_i) u_i · 2^(−(m_i + r_i))  +  1 − 2^(−r_i)
        > u_i · (3/2)^(m_i) · 2^(−r_i)                 (strictly, every step)
        ≥ u_i · 2^(−(m_i + r_i)).
```

Hence `log₂(y_n + 1) > log₂(x+1) − S_n ≥ log₂ N − S_n`, which is B's inequality with `(3/2)^{M_n}` of
slack to spare. Combined with (a)+(b) at `J = ⌈(1−η)b⌉` this is Lemma 13.2.4(c). The extension to the
code's stronger cut on `ω_+` is the extra `m_n + a_{n+1}log₂3` term of (c); `P_B(m ≥ t) = 2^{−(t−1)}` and
`P_B(a ≥ j) ≤ 2(0.93)^j` give `max_{n<T}(m_n + a_{n+1}log₂3) = O(log T)` off a set of `B`-mass `o(1)`,
and `ηb − O(log log N) ≫ log X_N = o(log N)`.

**Verified** (C7, §7). At `b = 1200`, `θ = 0.20`, `T = 240`, `300` starts, seed `34005`: `0` failures of
the per-step inequality over `72,000` steps, `0` failures of the `S1` bound, and
`min_n log₂(x_exit)/log₂N = 0.7736` (`min_n log₂(ω_+)/log₂N = 0.7694`) against the guaranteed floor
`1 − 4θ = 0.20`. At `b = 2400`, `θ = 0.24`, `T = 576`, `200` starts, seed `34007`: `0`/`0` failures,
`0.7512` and `0.7508` against a guaranteed floor of `0.04`. `max m = 21`, `max a = 8` over the whole run,
consistent with the `O(log T)` claim.

**Consequence for the parallel delegate, and one reinforcement.** In the `θ < 1/4` range Lemma 13.2.4(c)
settles two of the cut-weighting brief's items outright: `Q_N(x) = T` for all but a
density-`e^{−Θ(log N)}` set of starts, so the normalisation is deterministic and `Q_N(x) = 0` cannot
arise; and the cut may be stated on either `x_exit` or the core `ω_+` without changing anything, so the
`13.4` notational gap is harmless there. Neither settles their question for `θ ≥ 1/4`, which is theirs.
Their §8.6 measurement — that in the flagship run the cut *does* bind, on `2.6 %` of visits and `15.5 %`
of orbits for the core rule — is **consistent with**, not contrary to, my C7: the flagship runs at
`τ ≈ 2.29`, i.e. `θ ≈ 0.43`, more than `1.7 ×` past the range where (c) applies, while at `θ = 0.20` and
`θ = 0.24` C7 finds the worst exit over `187,200` sampled blocks still at `0.75 log₂ N`. **Binding begins
past the digit budget, exactly where (c) stops guaranteeing that it does not.** Two independent
observations, one boundary.

### 3.5 The honest claim

All four gaps close, so the honest claim is the full one — with three qualifications that belong on the
page and are in the drop-in:

1. **`θ < 1/4` strictly.** `I(1/4) = 0` exactly. The record's strict inequality was already right.
2. **Not uniform in `(w, k, D, L, ε)`.** Lemma 13.2.4(f).
3. **The theorem is about the *starts*, at a *finite* horizon, at *each* scale.** `13.3.3`'s scope is
   unchanged, and `13.2.5` is what converts "each scale" into "almost every integer".

Nothing was found past `1/4`, and the reason is an identity rather than an estimate (§3.2). Per the
brief and the README stopping rules, no effort was spent there.

---

## 4. Verdict on A's Option 1 justification — the answer the author's decision rests on

**It survives. Stated flatly: the base case proves Hypothesis `13.2.1` in A's strengthened, all-`L`,
letter-coordinate form, for every `θ < 1/4`, and proves `13.2.2` at every `(k, D, L)` in the same range.
Option 1 costs no unconditional territory.**

The three things that could have broken it, and did not:

* *Could the joint-law claim be a marginal claim in disguise?* No. `TV(μ,ν) ≤ δ` implies
  `|μ(A) − ν(A)| ≤ δ` for **every** event `A` of the joint law, including
  `A = {|f_n(w) − B[w]| > ε}` for a word `w` of any length. The record's own `Law(W_n)` is the law of
  the length-`n` word, verified at L34. One bound, all `L`.
* *Could the `L`-dependence blow up the range?* No. The `L`-dependence is confined to the constants
  `W = O(L log|A| + log(1/ε))` and `Λ`, both fixed before `N → ∞`. The exponential rate `I(θ)` in (b)
  does not involve `L` at all, so the frontier is `1/4` for every block length, not `1/4` shrinking in
  `L`.
* *Could the countable letter alphabet defeat the strengthening?* No, and the reason is A's own choice
  of norm: cellwise on the letter side (A §3.4). One word at a time needs no truncation. Had A chosen
  `TV` on the countable letter alphabet, the base case would still go through, but with a truncation in
  the primary statement; A's weaker choice is the right one and this is a second reason for it.

Two honest riders, neither of which touches the verdict:

* The record's calibration ceiling is unchanged by any of this: A §4.5's "block lengths `L ≤ 2`" is a
  statement about `experiments/`, not about the base case. My C5/C8 add fresh `L = 2` and `L = 3`
  measurements at `750`–`6000`-bit starts, but they are inside the provable range (`θ = 0.20 < 1/4`), so
  they measure the theorem, not the hypothesis. **They do not raise the calibration ceiling and must not
  be quoted as if they did.**
* A's §6 item 1 says the base case proves the strengthened form "without changing a symbol". That is
  true of the *conclusion* and false of the *text*: L34 as written proves it for dyadic windows only and
  waves at the rest. Lemma 13.2.4 is the change of symbols A's argument was entitled to assume.

---

## 5. Drop-in text

Consistent with A §7 (Option 1: `π_{k,D}`, `W_{k,D}`, `B̂`, TV, `13.2.2`), B §5 (the `1/β` retraction and
the exponent-time framing), and the cut-weighting delegate's §8 (the budget `τ`, the cemetery symbol, and
their `13.2.3`). §6 is the overlap register and is the section the apply phase needs.

### 5.1 `aeh.md` L32 — the final sentence

**The cut-weighting delegate's §8.4 replaces this whole paragraph and reproduces the defective sentence
verbatim** (only the dependence list changes, to "`ε`, `τ` and `θ`"). So this is not a standalone
replacement: it is the **final sentence of their §8.4 block**, and it must be substituted into it.

Current (verified at `dc61306`, and present unchanged in their §8.4):

> Because the bad density vanishes at every scale, the union of the bad sets has natural density zero in the integers — so the statement does deliver "almost every integer", for a finite-horizon property, with the exceptional set depending on `ε` and `θ`.

Replace with:

```markdown
The bad sets are a **triangular array**: one per sampling scale, each testing a horizon and a budget that move with `N`, so a given `x` is asked a different question by every scale it belongs to. Vanishing bad density at every scale therefore does *not* thin their unrestricted union — the sets `Bad_N = [N, N(1 + 1/log N))` have vanishing density in each `[N, 2N)` and their union over all `N` is every large integer. What is delivered, and delivered exactly, is the **shell** form: ask each `x` once, at its own scale `2^(⌊log₂ x⌋)`. Proposition `13.2.5` states and proves it, and its conclusion is natural density zero in the integers — so the statement does deliver "almost every integer", for a finite-horizon property, with the exceptional set depending on `ε`, the rates `(τ, θ)`, and the observable (the word `w`, or the triple `(k, D, ℓ)`).
```

### 5.2 `aeh.md` L34 — the base case

**Split with the cut-weighting delegate's §8.5.** They replace from "**Hypothesis 13.2.1 is therefore a
theorem for every `θ < 1/4`.**" through "…`23` of its `30` tallied blocks beyond it.", keeping A's
addendum and B's Inselmann clause. That leaves the paragraph's **opening** — the cylinder count and the
`TV` step — untouched by anyone but me, and it is the half that was a sketch. So:

* **apply my opening block below, down to and including the sentence ending "…with `13.2.2` following at
  every `k`, `D` and `L`"**;
* **then their §8.5 block**, which supersedes my second paragraph entirely (theirs is better: it carries
  the admissibility pair, the flagship's `τ ≈ 2.29` in the right unit, and its measured `4.0017` exponent
  per block);
* **then B's §5.2 Inselmann clause and the closing "What has not been carried past it…" sentence.**

My second paragraph is retained below only so the block reads as prose if their §8.5 is not applied; it
is the one to drop if both are.

This block **incorporates delegate B's §5.2 replacement verbatim** at its tail and **absorbs A's §7.4
added sentence**; see §6.

```markdown
**Base case, and where the content is.** The base case is native to *exponent* time. By Theorem `14.15.1.5` (itinerary.md) the odd integers whose first `n` letters are a prescribed word `W` form exactly one class mod `2^(S+1)`, `S = S(W) = Σ(m_i + r_i)`; so a start drawn uniformly from any window of `2^J` consecutive integers has its length-`n` letter word *exactly* `B`-distributed on the event `{S + 1 ≤ J}` — the event that the word has not outspent the start's supply of binary digits. Writing `b = ⌊log₂ N⌋`, this gives, for every `J ≥ 1`,

```text
TV( Law(letter word of x),  B^(⊗n) )  ≤  2^(J+2)/N  +  P_B(S_n ≥ J),
P_B(S_n ≥ J)  =  P( Bin(J − 1, 1/2) < 2n )        exactly.
```

The identity on the right holds because `S_n` is the waiting time for the `2n`-th head in a fair coin sequence. The first term is the price of a general window `[N, 2N)` over a dyadic one and is negligible for `J ≤ (1 − η)b`; the second is a large deviation of exact rate `I(θ) = log 2 − H(2θ)` nats per bit at `n = ⌈θ b⌉`, `H` the binary entropy — positive for every `θ < 1/4` (`0.0201` at `θ = 0.20`, `0.00080` at `θ = 0.24`) and **exactly `0` at `θ = 1/4`**, the optimal Chernoff tilt `e^λ = 2(1 − 2θ)` requiring `λ > 0`. The bound is on the joint law of the whole length-`n` word, so it delivers every finite block length at once and not merely the single-letter marginal. Lemma `13.2.4` assembles the rest — the extension from a dyadic window to a general `[N, 2N)`, the concentration of empirical pattern frequencies at every block length, the removal of the segment's initial past-boundary, and the altitude bound of `13.2.3` that makes the budget its own protection.

*[If the cut-weighting delegate's §8.5 is applied, it replaces this paragraph down to "…beyond it." Their version is the better one and should win; this is here only so the block reads as prose on its own.]* In exponent time the frontier is `1` unit of total exponent per bit of start, exactly: the start's own digit supply, with no estimate in it. It reads as `1/4` blocks per bit through `E[m + r] = 4` (`13.6.1`), and that conversion is licensed here and only here, because on this range the word *is* `B`. A full descent takes `1/β = 1.2047…` blocks per bit, `4.8188…` units of exponent per bit — `4.8188 ×` as far — so the hypothesis is precisely the assertion that equidistribution survives past the digit budget of stage4.md `11.8.7.7`, whose `σ ≈ 4.0` is this `E[m + r] = 4`. The calibration record is measured well past that frontier: the flagship run (starts `[2^70, 2^71)`, burn-in `10`, horizon `30`) runs `2.29 ×` the budget, with `23` of its `30` tallied blocks beyond it. The `1/4` frontier is this argument's, and the classical cylinder count's, not a barrier: for the *trajectory envelope* and for the ledger's *first moment* it has been crossed unconditionally at natural density `1` (Inselmann; `13.3.2`), by a different technique — but in step time: out to `(1 − log₂√3)^{-1} = 4.8188…` `T`-steps per bit, which is `4.8188 ×` the classical `log₂ m`. That window is `1/β` blocks per bit exactly on words whose blocks average `E[m + r] = 4` of exponent, so its block-per-bit reading is a consequence of the letter statistics asserted here, not independent corroboration of them. What has not been carried past it, as far as the literature check reached, is the distributional content — the full `2^-j` marginal at every `j`, the `1/3` rate, the depth law, `π_{k,D}` as a measure — and that is where AEH's content lives.
```

### 5.3 `aeh.md` — two appended anchors, after the L34 paragraph

No renumbering; `13.2.4` and `13.2.5` are new.

````markdown
**Lemma 13.2.4 (the base case, unconditional).** Let `θ > 0` and let `(X_N)` satisfy `X_N → ∞`, `log X_N = o(log N)`. Draw `x` uniformly from the odd integers of `[N, 2N)`; write `b = ⌊log₂ N⌋`, `T = ⌈θ log₂ N⌉`, `y_(−1) = x`, `y_n = G^(n+1)(x)` (the exit of block `n`, `13.6.3`(i)), `ℓ_n = stratum(y_n) = (m_n, r_n)` and `S_n = Σ_(i<n)(m_i + r_i)`. Then:

* **(a) Word law.** For every `n ≥ 0` and every `J ≥ 2`, `TV(Law(ℓ_0, …, ℓ_(n−1)), B^(⊗n)) ≤ 2^(J+2)/N + P_B(S_(n+1) ≥ J)`. For `N = 2^b` and `J = b` the first term is `0`. *Proof.* `[N, 2N)` contains all but at most `2^J + 1` of its odd integers in complete blocks of length `2^J`, and on a complete block the odd integers are exactly the `2^(J−1)` odd residues mod `2^J`, each once; by `14.15.1.5` the followers of a word `W` with `S(W) + 1 ≤ J` are exactly `2^(J−1−S(W))` of them, i.e. `B`-probability exactly. Two laws agreeing atom-by-atom on a set `𝒢` differ in total variation by at most the `B`-mass of `𝒢^c`. ∎
* **(b) The tail, exactly.** `P_B(S_n ≥ J) = P(Bin(J − 1, 1/2) < 2n)`. At `n = ⌈θb⌉` and `J = ⌈(1 − η)b⌉` with `0 < η < 1 − 4θ`, both terms of (a) are `e^(−Θ(b)) = N^(−Θ(1))`; call the sum `δ_N`.
* **(c) The cut does not bind.** `y_(i+1) + 1 > (y_i + 1)·(3/2)^(m_i)·2^(−r_i)` at every step, so `log₂(y_n + 1) > log₂ N − S_n` for every `n`. Hence off a set of starts of density `≤ δ_N`, every one of the first `T` exits exceeds `N^η − 1 > X_N`: the bulk filter is vacuous, the tally denominator is the deterministic `T`, and no orbit contributes zero qualifying visits. The same holds for the stronger cut on the core `ω_+` (`13.4`), since `log₂ ω_(n+1) = log₂(y_n + 1) − m_n − a_(n+1) log₂3` and `max_(n<T)(m_n + a_(n+1)log₂3) = O(log T)` off a further set of vanishing density. (The altitude bound is `13.2.3`'s, equivalently delegate B's S1; the door-coordinate form above is a second derivation with `(3/2)^(Σm)` of slack to spare, and if the page prints only one, print `13.2.3`'s.)
* **(d) Letter frequencies.** For every finite letter word `w` of length `L` and every `ε > 0`, the density of starts with `|f_N(w, x) − B[w]| > ε` is at most `δ_N + 2 exp(−2ε²(T − L + 1)²/(T L²))`, hence `→ 0`. *Proof.* `E_B f_n(w) = B[w]` exactly; changing one letter changes the count of `L`-blocks equal to `w` by at most `L`, so McDiarmid applies. No truncation of the countable letter alphabet is needed: the statement is cellwise.
* **(e) Window frequencies.** For every `k`, `D`, `L` and `ε > 0`, the density of starts with `‖ν^(L)_{k,D,N}(x) − π^(L)_{k,D}‖_TV > ε` tends to `0`. *Proof.* Fix `ε' = 2ε/|A_{k,D}|^L`. Choose the letter past-window `W ≥ D` with `2L(0.93)^W < ε'/8`, so that by `13.6.3`(iii)–(iv) the `L`-block of capped windows is an explicit function of `P = W + L + ⌈(k+1)/2⌉ + 1` consecutive letters off an event of `B`-mass `< ε'/8`; discard the first `W` and last `L + ⌈(k+1)/2⌉` visits of the horizon, which changes every frequency by `O(1/T)`; lump letters with a component above `Λ` into one symbol, `Λ` chosen with `P·2^(1−Λ) < ε'/8`, leaving finitely many patterns per cell; then (d) and a union bound over `≤ |A_{k,D}|^L · Λ^(2P)` events. ∎
* **(f) Scope.** The convergence in (d) and (e) is not uniform in `(w, k, D, L, ε)`: the threshold depends on all of them, through `W` and `Λ`. At `θ = 1/4` exactly, `I(1/4) = 0` and the lemma is empty.

**Corollary 13.2.4.1.** For every `θ < 1/4` and every admissible `(X_N)`, `13.2.4`(d) is the conclusion of Hypothesis `13.2.1` and `13.2.4`(e) is the conclusion of Hypothesis `13.2.2`. Both therefore hold unconditionally in that range, at every finite block length.

**Verified** — `experiments/aeh_basecase.py`, fresh code (imports nothing from `aeh_calibration.py`, `aeh_symbolic.py` or `itinerary_coding.py`), 2026-08-02. Cylinder count exhaustive over all odd residues mod `2^J` for `J = 18, 20, 22` (`1,376,253` distinct words, every one realised by exactly `2^(J−1−S)` residues, `0` failures) and, at the working scale, class invariance mod `2^(S_n+1)` with sharpness of the modulus on `3,000`-bit starts at `n = 600` letters (`40` trials, `0` failures, seed `34002`); the general window `[N, 2N)` exhaustive at seven `N` near `10^6`, dyadic and non-dyadic indistinguishable (`TV` `0.015212` vs `0.015213` at `N = 2^21`, `2^21 + 1`); the tail identity `P_B(S_n ≥ J) = P(Bin(J−1,1/2) < 2n)` exact in rational arithmetic at five `(n, J)`; pattern-frequency concentration at `θ = 0.20` for `b = 750, 1500, 3000, 6000` (two- and three-letter patterns, per-start s.d. `0.0234 → 0.0166 → 0.0118 → 0.0083`, exceptional density at `ε = 0.03` falling `0.188 → 0.065 → 0.013 → 0.000`, seed `34003`); the boundary transient measured at `40,000` starts (seed `34004`) — `a_0` at `L¹` distance `0.0063` from the uniform-start law `2·3^(−(j+1))` and `0.163` from the bulk law, `a_1` at `0.063` from bulk, `a_n` at the noise floor from `n = 2` on; and (c) with `0` failures over `72,000` steps at `b = 1200`, `θ = 0.20` (seed `34005`) and `115,200` at `b = 2400`, `θ = 0.24` (seed `34007`).

**Proposition 13.2.5 (the exceptional set, at shell scale).** Fix `ε`, `θ`, a cut sequence, and an observable (a word `w`, or a triple `(k, D, L)`). For each `b`, let `Bad_b` be the odd `x ∈ [2^b, 2^(b+1))` that fail the `ε`-test at sampling scale `N = 2^b`, and `β_b = |Bad_b|/2^(b−1)` its shell density. If `β_b → 0` — which is what `13.2.1` (resp. `13.2.2`) asserts along `N = 2^b`, and what `13.2.4` proves there for `θ < 1/4` — then `Bad = ⋃_b Bad_b` has **natural density zero** in the odd integers, hence in the integers. Each `x` lies in exactly one `Bad_b`, so `Bad` is the set of integers failing the test *at their own scale*: one property per integer, not a family. **Proof.** Given `η > 0`, take `b_0` with `β_b < η` beyond it and `C = Σ_(b ≤ b_0)|Bad_b|`. For `2^B ≤ X < 2^(B+1)`, `#{x ∈ Bad : x ≤ X} ≤ C + η Σ_(b ≤ B) 2^(b−1) ≤ C + η·2^B ≤ C + ηX`, so the upper density is `≤ η` for every `η`. ∎

**Scope, stated once.** The same argument works for any scale family `N_1 < N_2 < …` with `N_(j+1)/N_j ≥ λ > 1`, with `λ/(λ−1)` in place of `2`; it fails, and must fail, for the family of *all* `N`. That the union over all `N` is uncontrolled is not a defect of the hypothesis but a property of triangular arrays: `Bad_N = [N, N(1 + 1/log N))` has vanishing density in every `[N, 2N)` and unions to everything. `13.3.3`'s scope is unchanged by this proposition — it converts "at each scale" into "almost every integer", and supplies nothing about iteration, about individual orbits, or about tails.
````

### 5.4 `paper/collatz-reduced-v3.tex` L279–299 — replacing the base-case paragraph

The last three lines (L296–299, "not of the problem --- Inselmann…") are **delegate B's §5.5** and are
reproduced here so the block is contiguous; B's version wins on that clause.

```latex
The hypothesis has an unconditional base case, and it is Heuristic~\ref{prop:budget}
with a number on it. The classical coding fact --- the odd integers whose first $n$
blocks realize a prescribed itinerary form exactly one residue class modulo
$2^{S+1}$, $S$ the itinerary's total exponent (Terras \cite{terras}; in the present
coordinates \texttt{itinerary.md} \S14.15.1.5) --- makes the first $n$ blocks of a
start drawn uniformly from \emph{any} window of $2^{J}$ consecutive integers
exactly product-distributed on the event $S + 1 \le J$: the event that the itinerary
has not outspent the start's supply of binary digits. Writing
$b = \lfloor\log_2 N\rfloor$, this gives, for every $J \ge 2$,
\[
  \bigl\lVert \mathrm{Law}(\ell_0,\dots,\ell_{n-1}) - B^{\otimes n}
    \bigr\rVert_{\mathrm{TV}}
  \;\le\; \frac{2^{J+2}}{N} + P_B(S_n \ge J),
  \qquad
  P_B(S_n \ge J) \;=\; P\bigl(\mathrm{Bin}(J-1,\tfrac12) < 2n\bigr),
\]
the identity on the right because $S_n$ is the waiting time for the $2n$-th head in
a fair coin sequence. The first term is the price of a general window $[N,2N)$ over
a dyadic one and is negligible for $J \le (1-\eta)b$; the second decays at the exact
rate $\log 2 - H(2\theta)$ per bit at $n = \lceil\theta b\rceil$, $H$ the binary
entropy --- positive for every $\theta < 1/4$ and \emph{zero} at $\theta = 1/4$,
since the optimal Chernoff tilt is $e^{\lambda} = 2(1-2\theta)$ and needs
$\lambda > 0$. The bound is on the joint law of the whole length-$n$ word, so it
controls every finite block length at once. Together with the concentration of
empirical pattern frequencies, the removal of the segment's initial past-boundary
--- $O(1)$ blocks of a horizon $T \to \infty$ --- and the observation that the bulk
cut cannot bind while the itinerary stays inside the digit supply (a $T$-step lowers
$\log_2$ by at most one, so no exit among the first $n$ blocks sits below
$\log_2 N - S_n$), this yields the hypothesis outright:
Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every horizon rate
$\theta < 1/4$, at every block length. The assembly is Lemma 13.2.4 of
\texttt{aeh.md}.

The natural clock here is total exponent, not blocks. The frontier is one unit of
exponent per bit of start --- the start's own digit supply, with no estimate in it
--- and it reads as $1/4$ blocks per bit only through the mean exponent per block,
$E[m+r] = 4$, the $\sigma \approx 4.0$ of Heuristic~\ref{prop:budget} and exactly
$2+2$ under $\pi_{k,D}$. That conversion is available here precisely because the
word is exactly $B$ here. A descent from $N$ to $O(1)$ takes
$1/\beta = 1.2047\ldots$ blocks per bit, equivalently $4.8188\ldots$ units of
exponent per bit, some $4.8$ times as far. Hypothesis~\ref{hyp:aeh} is exactly the
assertion that the product law still describes the orbit after the start's digits
have been spent; the digit budget locates the frontier, and this is the statistical
statement on the far side of it. That frontier is the classical one: the same
$\theta < 1/4$ is where Terras's count stops, and $1 - \beta/4 = \log_4 3$ is
exactly the exponent Korec \cite{korec} obtains by exhausting it. It is a frontier
of this technique and
not of the problem --- Inselmann \cite{inselmann} crosses it unconditionally for the
trajectory envelope and the first moment, by an argument that buys the missing
iteration invariance from a density notion stronger than natural density
($*$-density: every initial segment carries all but $O(N^{-D})$ of its mass, which
sets of natural density one need not do) rather than from a sharper count. His
horizons are in step time: he starts from the classical range of $\log_2 m$ steps of
$T$ and extends it by the factor $(1-\log_2\sqrt3)^{-1} = 4.8188\ldots$. That factor
is $(1/\beta)/(1/4)$ --- the identity $4/\beta = 2/(2-\LL)$ --- and is the same
number in any time units; the endpoints read as $1/4$ and $1/\beta$ blocks per bit
only after dividing by the mean exponent per block, which is a theorem where the
cylinder count runs and is Hypothesis~\ref{hyp:aeh} where it does not.
```

### 5.5 `paper/collatz-reduced-v3.tex` L301–304 — the density clause

This **merges A §7.3** (which owns the ledger/cap clause) **with the repair of Finding 1** (which owns
the density clause). A's §7.3 as written reproduces the uncorrected "natural density zero" phrasing;
the version below is the one to apply.

```latex
AEH implies the ledger, in the form the hypothesis has: $s$ is a coordinate of
the observable, so $P(s = j) = 2^{-j}$ is a marginal of $\pi_{k,D}$ rather than a
deduction, exactly at every $j < D$ and up to the cap's single tail cell above;
and for every $\varepsilon$ and every horizon rate, all but a vanishing density of
the odd starting values of each size carry those frequencies along their first
$\lceil\theta\log_2 N\rceil$ bulk blocks. Evaluating each odd $x$ once, at its own
dyadic scale $2^{\lfloor \log_2 x\rfloor}$, turns that array of statements into a
single one: the odd integers that fail at their own scale have natural density
zero (\texttt{aeh.md} Proposition 13.2.5). The union over \emph{all} sampling
scales is a different and larger object and is not controlled --- the bad sets form
a triangular array, each testing a horizon and a cut that move with the scale, and
vanishing density in every window does not thin their unrestricted union. The error
$O(2^{-k})$ of Theorem~\ref{thm:onestep} prices a different statement ---
\emph{predicting} the next exit valuation from a window --- which the hypothesis
does not use.
```

---

## 6. Overlap register — every place my text meets another delegate's

Four delegates write into `aeh.md` §13.2 this round. **C** below is the cut-weighting delegate
(`briefs/v3r3-cut-weighting-findings.md`).

### 6.1 Where C and I meet — the two that matter

**Anchor `13.2.3` was claimed twice, and I yield.** C's `13.2.3` ("the clock, and what admissible means")
is cited from inside Hypotheses `13.2.1` and `13.2.2` themselves — twice in their §8.1 and once in their
§8.2 — and is a definition the hypothesis statements depend on. Mine are results cited from prose. So
theirs keeps `13.2.3`, and mine become **`13.2.4`** (base-case lemma), **`13.2.4.1`** (corollary),
**`13.2.5`** (shell proposition). Applied throughout this file. If the author prefers the reverse, the
only edits needed are the five pointers listed in §5.

**We proved the same altitude bound independently, and theirs is the better statement.** C's `13.2.3`
gives `log₂ x_exit(n−1) ≥ log₂ x − S_n` from `T_1(y) ≥ y/2`, deterministically, for every odd `x` and
every `n`, with no exceptional set. Mine (Lemma `13.2.4`(c), §3.4(iv)) gives
`y_{i+1}+1 > (y_i+1)(3/2)^{m_i}2^{−r_i}` in door coordinates. **Theirs should be printed**; mine adds
only the `(3/2)^{Σm}` slack and the `ω_+` extension. Both are B's S1 in different clothes, and my C7 is a
numerical check of all three at once (`187,200` blocks, `0` failures).

Three smaller reconciliations, none of which changes any statement:

* **Two exponent counts, differing by two letters.** C's `S_n = Σ_{i<n}(m_i + s_i)` counts divisions from
  `x` to `x_exit(n−1)`; L34's and mine, `S_n = Σ(m_i + r_i)`, is the letter word's total exponent, and my
  `(a)` includes the letter `ℓ_{−1} = stratum(x)` because that is the object `14.15.1.5` counts. Since
  `r_i = s_{i+1}`, the two differ by one letter at each end — C records this at their §3. It is `O(1)` in
  a budget of `Θ(log N)` and affects nothing; the apply phase should just pick one and say which.
* **The cemetery/budget reformulation is proved by my lemma, at `τ < 1`.** See the paragraph after
  Corollary `13.2.4.1`: their strictly stronger hypothesis follows from `(a)`+`(b)` with `J = Λ_N`, and
  the extra clause `4θ < τ` they must assert past the budget *is* my large deviation below it. Their
  `τ < 1` and my `θ < 1/4` are one range and one theorem.
* **Their §8.6 "the cut does bind" and my C7 "it does not" are the same finding.** Theirs is measured at
  the flagship's `τ ≈ 2.29` (`θ ≈ 0.43`); mine at `θ = 0.20, 0.24`. Binding starts past the budget,
  exactly where the guarantee stops. §3.4(iv).

### 6.2 The full register

| # | Site | Who touches it | Which wins |
|---|---|---|---|
| 1 | `aeh.md` L32, the `θ < 1/β` sentence | **B** §5.1, **C** §8.4 | **C**, whose §8.4 rewrites the whole paragraph and supersedes B's sentence-level replacement. I do not touch it. |
| 2 | `aeh.md` L32, the "union of the bad sets" sentence | **C** §8.4 (reproduces it uncorrected), **D** (§5.1) | **D.** Substitute my sentence for the last sentence of C's §8.4 block. C's block is otherwise unchanged. **This is the one place where applying another delegate's block verbatim would carry the defect forward.** |
| 3 | `aeh.md` L32, the sampling/normalisation/budget sentences | **C** §8.4 | **C.** |
| 4 | `aeh.md` L34, the cylinder count and the `TV` step (the paragraph's opening) | **D** (§5.2) | **D.** No one else writes here, and it is the half that was a sketch. |
| 5 | `aeh.md` L34, "**Hypothesis 13.2.1 is therefore a theorem…**" and the flagship sentence | **C** §8.5, **D** (§5.2 second paragraph) | **C.** Theirs carries the admissibility pair, `τ ≈ 2.29` in the right unit, and the measured `4.0017`. Drop my second paragraph when theirs is applied. |
| 6 | `aeh.md` L34, A's added sentence ("The bound is on the joint law of the whole length-`n` word…", A §7.4 tail) | **A**, **C** (keeps it), **D** (absorbs it) | **D.** My opening block says it in place, with the lemma pointer. Do not apply A's sentence as well — it would appear twice. |
| 7 | `aeh.md` L34, the Inselmann `1/β` clause | **B** §5.2, **C** (keeps it) | **B.** Reproduced verbatim inside my §5.2 block so the paragraph reads contiguously; if B's text is revised, revise it there. |
| 8 | `aeh.md` appended anchors | **A** (`13.2.2`), **C** (`13.2.3`), **D** (`13.2.4`, `13.2.4.1`, `13.2.5`) | Resolved in §6.1. Order: `13.2.1`, `13.2.2`, boundary paragraph, L32 paragraph, L34 paragraph, `13.2.3`, `13.2.4`, `13.2.4.1`, `13.2.5`. |
| 9 | `aeh.md` Hypotheses `13.2.1`, `13.2.2` (A §7.4 versions) | **A**, **C** §8.1/§8.2 | **C**, which amends A's. My Lemma `13.2.4`(d),(e) is stated against A's version; under C's cemetery version it still holds (§6.1, third bullet) and the lemma's wording needs one clause, given there. |
| 10 | `aeh.md` L48 (`13.4` reconciliation, cut coordinate) | **C** §8.6 | **C.** I do not touch it. |
| 11 | `aeh.md` `π_k → π_{k,D}` throughout | **A** §7.4 | **A.** Applied in my text already. |
| 12 | `paper` L279–295 | **D** (§5.4) | **D.** If C's `(τ, θ)` framing goes into the paper's `hyp:aeh` (their §8.7), the sentence "Hypothesis~\ref{hyp:aeh} is a \emph{theorem} for every horizon rate $\theta < 1/4$" in my block should gain "equivalently, for every admissible $(\tau,\theta)$ with $\tau < 1$". |
| 13 | `paper` L296–299 | **B** §5.5 | **B.** Reproduced inside my §5.4 block. |
| 14 | `paper` L301–304, the ledger/cap clause | **A** §7.3 | **A.** |
| 15 | `paper` L301–304, the density clause | **A** §7.3 (uncorrected), **D** (§5.5) | **D.** §5.5 is the merged block; apply it instead of A §7.3. |
| 16 | `paper` L307–313 (the Inselmann descent paragraph) | **B** §5.6 | **B.** I do not touch it. |
| 17 | `paper` L241, L243–257, L259–277 | **A** §7.1/§7.2, **C** §8.7 | **Theirs.** My §5.4 quotes `\ell_n` and `B[w]`, both introduced by A §7.2; if those names change, change them in §5.4 too. |
| 18 | The `x_exit` versus `ω_+` cut coordinate | **C** (their item 7), **D** (Lemma `13.2.4`(c)) | **C on the choice** (they drop the altitude cut from the statement entirely); my (c) supplies the fact that below the budget *both* coordinates are non-binding, so nothing is lost there. |
| 19 | "Admissible" and the `Q_N(x) = 0` case | **C** (their items 3, 4) | **C.** Lemma `13.2.4`(c) makes their "protected" clause a theorem for `τ < 1`; their `13.2.3` states it, and their definition governs. |
| 20 | A §4.5's "block lengths `L ≤ 2`" calibration ceiling | **A** | **A**, unchanged. My C5/C8 measurements are inside the provable range and must not be quoted as raising it (§4). |
| 21 | A open question 4 (the five-coordinate labelled reconstruction is not run as one test) | **A** | **A**, still open. My C8 exercises `(s, d)` jointly off the door orbit — a partial, not a complete, answer. |

---

## 7. Verification record

`AGENTS.md`, "Before marking anything proved": *run an independent numerical check (not the one quoted
in the text — a fresh implementation), and record what was checked, the range, and the date in the
page.*

**Code:** the file in §8, run 2026-08-02 under CPython. It imports nothing from
`experiments/aeh_calibration.py`, `experiments/aeh_symbolic.py` or `experiments/itinerary_coding.py`;
`v2`, `v3`, `stratum`, `G`, `R`, the per-step labels, the cylinder count and the Bernoulli reference law
are rebuilt from Definition~3.1 and Proposition~3.2 of the paper, `itinerary.md` `14.15.1.1`/`14.15.1.5`,
and `aeh.md` `13.6.1`/`13.6.3`. Written to the round's scratchpad; **no file was added to the
repository**. If the lemma lands, promote it as `experiments/aeh_basecase.py`.

| check | what was checked | range / counts | seeds | result |
|---|---|---|---|---|
| C0 | `G = T^m`; `x_exit(R(x)) = G(x)`; `stratum(y_n) = (m_{+,n}, s_{n+1})` | `4,000` random odd starts, `64` bits | `34001` | `0` failures on all three |
| C1 | **exact cylinder count**: every word with `S+1 ≤ J` realised by exactly `2^{J−1−S}` odd residues mod `2^J` | exhaustive, `J = 18, 20, 22`; `131,072` / `524,288` / `2,097,152` residues; `65,535` / `262,143` / `1,048,575` words, lengths `1`–`10` | — | `0` failures; word totals `= 2^{J−2}−1` as predicted |
| C2 | the count on a **general** window `[N, 2N)`, dyadic vs non-dyadic | exhaustive, `N ∈ {2^20, 1234567, 1500001, 1999999, 2^21, 2^21+1, 2999983}`, `n = 3`; and `N ∈ {2^21, 2999983}`, `n = 4`; `0.5`–`1.5` million odd starts each | — | `TV` measured `0.0152`–`0.0305` (`n=3`), `0.102`/`0.106` (`n=4`), against `P_B(S_n ≥ b)` `0.0133`–`0.0207` / `0.0946`; dyadic and non-dyadic indistinguishable (`0.015212` vs `0.015213`) |
| C3 | **the tail identity** `P_B(S_n ≥ J) = P(Bin(J−1,½) < 2n)`, exact rational arithmetic; and `I(θ)` | `(n,J) = (5,40), (10,60), (12,100), (25,120), (30,121)`; `θ = 0.10 … 0.25` | — | exact equality in all five; `I = 0.19274, 0.08228, 0.020136, 0.00080, 8·10^-8, 0` at `θ = 0.10, 0.15, 0.20, 0.24, 0.2499, 0.25` |
| C4 | **the exact-cylinder claim at the scale used**: word constant on classes mod `2^{S_n+1}`, and *not* on classes mod `2^{S_n}` | `3,000`-bit starts, `n = 600` letters, `40` trials, shifts `t < 2^20` | `34002` | `0` failures of invariance; sharpness witness found in all `40` |
| C5 | **concentration of multi-letter pattern frequencies** for `((1,1),(1,1))`, `((1,1),(1,2))`, `((2,1),(1,1))`, `((1,1),(1,1),(1,1))` | `θ = 0.20`; `b = 750, 1500, 3000, 6000`; `T = 150, 300, 600, 1200`; `1500/1500/1500/600` starts | `34003` | means within `2.3σ` of `B[w]` at every scale; s.d. `0.02338 → 0.01664 → 0.01179 → 0.00825` (ratios `1.405, 1.412, 1.428` vs `√2`); exceptional density at `ε = 0.03`: `0.188 → 0.065 → 0.0127 → 0.000`; `S_max < b` and `0` budget violations at every scale; mean exponent per block `4.009, 4.005, 4.005, 4.005` |
| C8 | window-side concentration: `L = 2` blocks of the capped window `(min(s,3), min(d,3))`, per-start `TV` to the pooled reference | `b = 1500, 3000, 6000`; `T = 300, 600, 1200`; `400` starts each; `72` cells realised | `34006 + b` | `TV_mean 0.1854 → 0.1319 → 0.0935`; `TV_mean·√T = 3.212, 3.231, 3.238` (constant, i.e. pure `T^{−1/2}` sampling noise on a fixed alphabet); per-cell s.d. matches `√(p(1−p)/T)` |
| C6 | **the size of the boundary term**: law of `a_n = v_3(y_{n−1}+1)` at `n = 0 … 12` | `40,000` starts of `400` bits | `34004` | `n=0`: `(0.6698, 0.22005, 0.11015)`, `L¹` `0.0063` from `2·3^{−(j+1)}` and `0.163` from bulk; `n=1`: `L¹` `0.063` from bulk; `n ≥ 2`: `L¹ ≤ 0.0086` from bulk, at the noise floor. Transient occupies exactly two visits; `TV` deviations `0.0815`, `0.0317` |
| C7 | **the cut is non-binding (B's S1)**: per-step `y_{i+1}+1 > (y_i+1)(3/2)^{m_i}2^{−r_i}`, the bound `log₂(y_n+1) > log₂N − S_n`, and the core cut on `ω_+` | `b = 1200`, `θ = 0.20`, `T = 240`, `300` starts (`72,000` steps); `b = 2400`, `θ = 0.24`, `T = 576`, `200` starts (`115,200` steps) | `34005`, `34007` | `0` failures of either claim in either run; `min log₂(x_exit)/log₂N = 0.7736` / `0.7512`, `min log₂(ω_+)/log₂N = 0.7694` / `0.7508`, against guaranteed floors `0.20` / `0.04`; `max m = 21`, `max a = 8` |

**Line for the page** (the form `aeh.md`'s other verification lines use) is embedded in the `13.2.4`
drop-in at §5.3.

---

## 8. Full source

To be promoted to `experiments/aeh_basecase.py` by the apply phase if the lemma lands. Not added to the
repository by this round.

```python
#!/usr/bin/env python3
"""
Independent verification for aeh.md Lemma 13.2.4 (the unconditional base case,
theta < 1/4) and Proposition 13.2.5 (the dyadic-shell exceptional set).

Fresh implementation.  Imports nothing from experiments/aeh_calibration.py,
experiments/aeh_symbolic.py or experiments/itinerary_coding.py.  The door map
G, the stratum, the cylinder count, the Bernoulli reference law and the
descent bound are all rebuilt here from the definitions:
  - Definition 3.1 / Proposition 3.2 of paper/collatz-reduced-v3.tex
    (reduced state, block structure, x_exit);
  - itinerary.md 14.15.1.1 (stratum) and 14.15.1.5 (cylinder theorem);
  - aeh.md 13.6.1 (letter law) and 13.6.3 (dictionary).

Checks
  C0  G = T^m, and stratum(y_n) = (m_+ of block n, s of block n+1).
  C1  Exact cylinder count, exhaustive on all odd residues mod 2^J.
  C2  The same count on a general window [N, 2N) with N not a power of two:
      measured TV against the bound of Lemma 13.2.4(a).
  C3  The exact identity  P_B(S_n >= b) = P(Bin(b-1, 1/2) < 2n), and the
      entropy rate I(theta) = log 2 - H(2 theta).
  C4  Cylinder-class structure at the scale actually used (3000-bit starts):
      the length-n word is constant on residue classes mod 2^{S_n+1} and not
      on classes mod 2^{S_n}.
  C5  Concentration of multi-letter pattern frequencies at 3000-bit starts.
  C6  The past-boundary term: the law of the absorption a_n at n = 0, 1, 2, ...
      against the uniform-start law 2*3^{-(j+1)} and the bulk law 13.6.5.
  C7  The cut is non-binding (delegate B's S1), in door coordinates.
  C8  Window side: per-cell concentration of L-block window frequencies.
"""

import math
import random
import sys
from collections import Counter, defaultdict
from fractions import Fraction

# ----------------------------------------------------------------------------
# primitives
# ----------------------------------------------------------------------------


def v2(n):
    """2-adic valuation of a nonzero integer."""
    return (n & -n).bit_length() - 1


def v3(n):
    """3-adic valuation of a nonzero integer."""
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def T_odd(x):
    """The odd-to-odd Collatz map T(x) = (3x+1)/2^{v2(3x+1)} (paper L50)."""
    z = 3 * x + 1
    return z >> v2(z)


def stratum(y):
    """itinerary.md 14.15.1.1:  m = v2(y+1), q = (y+1)/2^m, r = v2(3^m q - 1)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    return m, v2(pow(3, m) * q - 1)


def G(y):
    """The door map, reverse.md 14.14.3:  G(y) = (3^m q - 1)/2^r  = T^m(y)."""
    m = v2(y + 1)
    q = (y + 1) >> m
    z = pow(3, m) * q - 1
    return z >> v2(z)


def R(x):
    """The projection R of Definition 3.1: x+1 = 2^m 3^a w, R(x) = (w, m+a)."""
    u = x + 1
    m = v2(u)
    u >>= m
    a = v3(u)
    w = u // pow(3, a)
    return w, m + a


def step_labels(w, d):
    """Definition 3.1's per-step data for the state (w, d)."""
    A = pow(3, d) * w - 1
    s = v2(A)
    x_exit = A >> s
    C = A + (1 << s)
    sigma = v2(C)
    a_plus = v3(C)
    m_plus = sigma - s
    w_next = C // (pow(2, sigma) * pow(3, a_plus))
    return dict(A=A, s=s, x_exit=x_exit, C=C, sigma=sigma, a_plus=a_plus,
                m_plus=m_plus, w_next=w_next, d_next=m_plus + a_plus)


def word(x, n):
    """The length-n letter word of the odd integer x: (stratum(G^i x))_{i<n}."""
    out = []
    y = x
    for _ in range(n):
        out.append(stratum(y))
        y = G(y)
    return tuple(out)


# ----------------------------------------------------------------------------
# C0 -- the coding is the one the wiki describes
# ----------------------------------------------------------------------------


def check_C0(trials=4000, bits=64, seed=34001):
    rng = random.Random(seed)
    fail_gt, fail_seam, fail_exit = 0, 0, 0
    for _ in range(trials):
        x = rng.randrange(1 << (bits - 1), 1 << bits) | 1
        # G = T^m
        m = v2(x + 1)
        z = x
        for _ in range(m):
            z = T_odd(z)
        if z != G(x):
            fail_gt += 1
        # the door y_0 = G(x) is x_exit of the first block
        w, d = R(x)
        lab = step_labels(w, d)
        if lab["x_exit"] != G(x):
            fail_exit += 1
        # stratum(y_n) = (m_+ of block n, s of block n+1)
        y = G(x)
        lab2 = step_labels(lab["w_next"], lab["d_next"])
        if stratum(y) != (lab["m_plus"], lab2["s"]):
            fail_seam += 1
    return dict(trials=trials, bits=bits, seed=seed,
                fail_G_eq_Tm=fail_gt, fail_exit=fail_exit, fail_seam=fail_seam)


# ----------------------------------------------------------------------------
# C1 -- exact cylinder count, exhaustive over odd residues mod 2^J
# ----------------------------------------------------------------------------


def check_C1(J):
    """Every word W with S(W) + 1 <= J is realised by exactly 2^{J-1-S} of the
    2^{J-1} odd residues mod 2^J.  Exhaustive."""
    counts = defaultdict(int)
    for x in range(1, 1 << J, 2):
        y = x
        S = 0
        w = []
        while True:
            m, r = stratum(y)
            if S + m + r + 1 > J:
                break
            w.append((m, r))
            S += m + r
            counts[tuple(w)] += 1
            y = G(y)
    fails = 0
    worst = None
    for wd, c in counts.items():
        S = sum(m + r for m, r in wd)
        pred = 1 << (J - 1 - S)
        if c != pred:
            fails += 1
            worst = (wd, c, pred)
    by_len = Counter(len(w) for w in counts)
    return dict(J=J, odd_residues=1 << (J - 1), words=len(counts),
                failures=fails, worst=worst,
                words_by_length=dict(sorted(by_len.items())))


# ----------------------------------------------------------------------------
# C2 -- a general window [N, 2N), N not a power of two
# ----------------------------------------------------------------------------


def tv_word_law(N, n):
    """Exhaustive over odd x in [N, 2N): TV(Law(word_n(x)), B^{tensor n})."""
    cnt = Counter()
    tot = 0
    x = N | 1
    while x < 2 * N:
        cnt[word(x, n)] += 1
        tot += 1
        x += 2
    seen_B = Fraction(0)
    tv2 = Fraction(0)  # 2 * TV
    for wd, c in cnt.items():
        S = sum(m + r for m, r in wd)
        B = Fraction(1, 1 << S)
        seen_B += B
        tv2 += abs(Fraction(c, tot) - B)
    tv2 += (1 - seen_B)  # unobserved words carry only B-mass
    return float(tv2 / 2), tot, len(cnt)


def PB_S_ge(n, b):
    """P_B(S_n >= b) exactly, S_n = sum of 2n iid geom(1/2) on {1,2,...}."""
    if b <= 2 * n:
        return Fraction(1)
    tail = Fraction(1)
    for s in range(2 * n, b):
        tail -= Fraction(math.comb(s - 1, 2 * n - 1), 1 << s)
    return tail


def check_C2(Ns, n):
    rows = []
    for N in Ns:
        tv, tot, nw = tv_word_law(N, n)
        # Lemma 13.2.4(a) bound: 2^{J+2}/N + P_B(S_n >= J), minimised over J
        best = None
        for J in range(2 * n, 300):
            bd = float(Fraction(1 << (J + 1), tot)) + float(PB_S_ge(n, J))
            if best is None or bd < best[1]:
                best = (J, bd)
            if bd > 10:
                break
        b = N.bit_length()
        rows.append(dict(N=N, dyadic=(N == 1 << (b - 1)), n=n, odds=tot,
                         distinct_words=nw, TV_measured=round(tv, 6),
                         PB_S_ge_b=round(float(PB_S_ge(n, b)), 6),
                         J_star=best[0], lemma_bound=round(best[1], 4)))
    return rows


# ----------------------------------------------------------------------------
# C3 -- the exact tail identity and the entropy rate
# ----------------------------------------------------------------------------


def binom_lt(b, k):
    """P(Bin(b, 1/2) < k) exactly."""
    return Fraction(sum(math.comb(b, j) for j in range(0, k)), 1 << b)


def check_C3(cases):
    rows = []
    ok = True
    for (n, b) in cases:
        lhs = PB_S_ge(n, b)
        rhs = binom_lt(b - 1, 2 * n)
        if lhs != rhs:
            ok = False
        rows.append(dict(n=n, b=b, PB_S_ge=float(lhs), Bin=float(rhs),
                         exact_equal=(lhs == rhs)))
    return ok, rows


def I_rate(theta):
    """I(theta) = log 2 - H(2 theta), natural log; the Chernoff rate of
    P_B(S_{theta b} >= b).  Zero exactly at theta = 1/4."""
    p = 2 * theta
    if p <= 0 or p >= 1:
        return float("nan")
    H = -p * math.log(p) - (1 - p) * math.log(1 - p)
    return math.log(2) - H


# ----------------------------------------------------------------------------
# C4 -- the cylinder class structure at the scale actually used
# ----------------------------------------------------------------------------


def check_C4(bits=3000, n=600, trials=40, seed=34002):
    rng = random.Random(seed)
    fail_up, fail_down = 0, 0
    for _ in range(trials):
        x = rng.randrange(1 << (bits - 1), 1 << bits) | 1
        wd = word(x, n)
        S = sum(m + r for m, r in wd)
        t = rng.randrange(1, 1 << 20)
        if word(x + t * (1 << (S + 1)), n) != wd:
            fail_up += 1
        # the modulus is sharp: 2^S alone does not suffice for every shift
        sharp = False
        for tt in range(1, 40):
            xx = x + tt * (1 << S)
            if (xx & 1) and word(xx, n) != wd:
                sharp = True
                break
        if not sharp:
            fail_down += 1
    return dict(bits=bits, n=n, trials=trials, seed=seed,
                fail_class_invariance=fail_up, fail_sharpness=fail_down)


# ----------------------------------------------------------------------------
# C5 -- concentration of multi-letter pattern frequencies
# ----------------------------------------------------------------------------


def check_C5(bits=3000, theta=0.20, starts=1500, seed=34003,
             patterns=(((1, 1), (1, 1)),
                       ((1, 1), (1, 2)),
                       ((2, 1), (1, 1)),
                       ((1, 1), (1, 1), (1, 1)))):
    rng = random.Random(seed)
    N = rng.randrange(1 << (bits - 1), 1 << bits)  # generic, not a power of two
    b = math.log2(N)
    T = math.ceil(theta * b)
    freqs = {p: [] for p in patterns}
    S_max = 0
    exps = []           # per-start mean of m+r over the horizon
    budget_violations = 0
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        wd = word(x, T + 4)
        S = sum(m + r for m, r in wd[:T])
        S_max = max(S_max, S)
        if S + 1 > math.floor(b):
            budget_violations += 1
        exps.append(S / T)
        for p in patterns:
            Lp = len(p)
            hits = sum(1 for i in range(T - Lp + 1) if wd[i:i + Lp] == p)
            freqs[p].append(hits / (T - Lp + 1))
    out = dict(bits=bits, theta=theta, N_bits=N.bit_length(), T=T,
               starts=starts, seed=seed, S_max=S_max, b=b,
               budget_violations=budget_violations,
               mean_exponent_per_block=sum(exps) / len(exps))
    rows = []
    for p in patterns:
        Bp = 1.0
        for (m, r) in p:
            Bp *= 2.0 ** (-(m + r))
        f = freqs[p]
        mean = sum(f) / len(f)
        sd = (sum((v - mean) ** 2 for v in f) / (len(f) - 1)) ** 0.5
        z = (mean - Bp) / (sd / len(f) ** 0.5) if sd > 0 else float("nan")
        rows.append(dict(pattern=p, B=Bp, mean=round(mean, 6), sd=round(sd, 6),
                         z_of_mean=round(z, 2),
                         max_abs_dev=round(max(abs(v - Bp) for v in f), 5),
                         frac_dev_gt_0p02=sum(1 for v in f if abs(v - Bp) > 0.02) / len(f),
                         frac_dev_gt_0p03=sum(1 for v in f if abs(v - Bp) > 0.03) / len(f)))
    out["patterns"] = rows
    return out


# ----------------------------------------------------------------------------
# C8 -- the window side: per-cell concentration of L-block window frequencies
# ----------------------------------------------------------------------------


def check_C8(bits_list=(1500, 3000, 6000), theta=0.20, starts=400, L=2,
             seed=34006):
    """Coarse capped window V(n) = (min(s_n, 3), min(d_n, 3)), 9 letters, so
    9^L block cells.  s_n = r_{n-1} and d_n = m_{n-1} + v3(y_{n-1}+1) are read
    off the door orbit (13.6.3(i),(iii)).  We measure, per start, the empirical
    L-block law, and compare each start to the pooled reference: the claim
    under test is concentration, cell by cell and in total variation."""
    out = []
    for bits in bits_list:
        rng = random.Random(seed + bits)
        N = rng.randrange(1 << (bits - 1), 1 << bits)
        b = math.log2(N)
        T = math.ceil(theta * b)
        per_start = []
        pooled = Counter()
        pooled_tot = 0
        for _ in range(starts):
            x = rng.randrange(N, 2 * N) | 1
            y = x
            V = []
            for _ in range(T + L):
                m, r = stratum(y)
                a = v3(y + 1)
                V.append((min(r, 3), min(m + a, 3)))   # (s_{n+1}, d_{n+1})
                y = G(y)
            c = Counter(tuple(V[i:i + L]) for i in range(len(V) - L + 1))
            tot = sum(c.values())
            per_start.append((c, tot))
            pooled.update(c)
            pooled_tot += tot
        ref = {k: v / pooled_tot for k, v in pooled.items()}
        tvs = []
        for c, tot in per_start:
            keys = set(c) | set(ref)
            tvs.append(0.5 * sum(abs(c.get(k, 0) / tot - ref.get(k, 0.0))
                                 for k in keys))
        # per-cell spread on the busiest cells
        cells = sorted(ref.items(), key=lambda kv: -kv[1])[:6]
        cellrows = []
        for k, p in cells:
            vals = [c.get(k, 0) / tot for c, tot in per_start]
            mu = sum(vals) / len(vals)
            sd = (sum((v - mu) ** 2 for v in vals) / (len(vals) - 1)) ** 0.5
            cellrows.append(dict(cell=k, pooled=round(p, 5), mean=round(mu, 5),
                                 sd=round(sd, 5),
                                 sd_over_sqrtT_pred=round((p * (1 - p) / (T + 1)) ** 0.5, 5)))
        out.append(dict(bits=bits, T=T, starts=starts, cells_seen=len(ref),
                        TV_mean=round(sum(tvs) / len(tvs), 5),
                        TV_max=round(max(tvs), 5),
                        TV_mean_times_sqrtT=round(sum(tvs) / len(tvs) * T ** 0.5, 4),
                        busiest_cells=cellrows))
    return out


# ----------------------------------------------------------------------------
# C6 -- the past-boundary term
# ----------------------------------------------------------------------------


def check_C6(bits=400, starts=40000, depth=13, seed=34004):
    """a_n = v3(y_{n-1} + 1) with y_{-1} = x.  n = 0 is the uniform-start
    absorption v3(x+1); large n should be the bulk law of 13.6.5."""
    rng = random.Random(seed)
    N = 1 << (bits - 1)
    tal = [Counter() for _ in range(depth)]
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        y = x
        for n in range(depth):
            tal[n][min(v3(y + 1), 4)] += 1
            y = G(y)
    # collapse to (0, 1, >=2), where the record's exact values live
    bulk3 = (2 / 3, 19 / 63, 2 / 63)
    unif3 = (2 / 3, 2 / 9, 1 / 9)
    rows = []
    for n in range(depth):
        c = tal[n]
        tot = sum(c.values())
        emp = (c[0] / tot, c[1] / tot, (tot - c[0] - c[1]) / tot)
        rows.append(dict(n=n, P0=emp[0], P1=emp[1], Pge2=emp[2],
                         L1_to_bulk=sum(abs(a - b) for a, b in zip(emp, bulk3)),
                         L1_to_uniform_start=sum(abs(a - b) for a, b in zip(emp, unif3))))
    return dict(bits=bits, starts=starts, seed=seed, depth=depth,
                bulk=bulk3, uniform_start=unif3, rows=rows)


# ----------------------------------------------------------------------------
# C7 -- the cut is non-binding (delegate B's S1) in door coordinates
# ----------------------------------------------------------------------------


def check_C7(bits=1200, theta=0.20, starts=300, seed=34005):
    """Two claims:
       (a)  y_{i+1} + 1  >  (y_i + 1) * (3/2)^{m_i} * 2^{-r_i}   exactly;
       (b)  min_{n<=T} log2(y_n + 1)  >=  log2(x+1) - S_T,  and that this is
            already > (1 - 4 theta - o(1)) log2 N."""
    rng = random.Random(seed)
    N = rng.randrange(1 << (bits - 1), 1 << bits)
    b = math.log2(N)
    T = math.ceil(theta * b)
    fail_step, fail_bound = 0, 0
    worst_margin = None
    min_ratio = None
    min_ratio_core = None     # the code's stronger cut, on the core w_+
    max_m = 0
    max_a = 0
    for _ in range(starts):
        x = rng.randrange(N, 2 * N) | 1
        y = x
        S = 0
        lo = math.log2(x + 1)
        lo_core = None
        for n in range(T):
            m, r = stratum(y)
            y2 = G(y)
            if not (y2 + 1) * (1 << (m + r)) > (y + 1) * pow(3, m):
                # (y2+1) > (y+1) (3/2)^m 2^{-r}  <=>  (y2+1) 2^{m+r} > (y+1) 3^m
                fail_step += 1
            a = v3(y2 + 1)
            core = (y2 + 1) >> v2(y2 + 1)
            core //= pow(3, a)
            lc = math.log2(core)
            lo_core = lc if lo_core is None else min(lo_core, lc)
            max_m = max(max_m, m)
            max_a = max(max_a, a)
            S += m + r
            lo = min(lo, math.log2(y2 + 1))
            y = y2
        if lo < math.log2(x + 1) - S - 1e-9:
            fail_bound += 1
        margin = lo - (b - S)
        worst_margin = margin if worst_margin is None else min(worst_margin, margin)
        ratio = lo / b
        min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
        rc = lo_core / b
        min_ratio_core = rc if min_ratio_core is None else min(min_ratio_core, rc)
    return dict(bits=bits, theta=theta, T=T, starts=starts, seed=seed,
                fail_step_inequality=fail_step, fail_S1_bound=fail_bound,
                worst_margin_bits=round(worst_margin, 2),
                min_log2_exit_over_log2_N=round(min_ratio, 5),
                min_log2_core_over_log2_N=round(min_ratio_core, 5),
                max_m_seen=max_m, max_a_seen=max_a,
                predicted_floor_1_minus_4theta=1 - 4 * theta)


# ----------------------------------------------------------------------------


def main():
    print("=" * 78)
    print("C0  coding sanity: G = T^m, x_exit = G(x), stratum(y_n) = (m_+, s_+)")
    print(check_C0())

    print("=" * 78)
    print("C1  exact cylinder count, exhaustive over odd residues mod 2^J")
    for J in (18, 20, 22):
        r = check_C1(J)
        print({k: r[k] for k in ("J", "odd_residues", "words", "failures")},
              "words_by_length =", r["words_by_length"])

    print("=" * 78)
    print("C2  general window [N, 2N):  dyadic vs non-dyadic, same magnitude")
    Ns = [1 << 20, 1234567, 1500001, 1999999, 1 << 21, 2097153, 2999983]
    for row in check_C2(Ns, n=3):
        print(row)
    for row in check_C2([1 << 21, 2999983], n=4):
        print(row)

    print("=" * 78)
    print("C3  P_B(S_n >= b) = P(Bin(b-1,1/2) < 2n), exact; entropy rate")
    ok, rows = check_C3([(5, 40), (10, 60), (12, 100), (25, 120), (30, 121)])
    print("all exact:", ok)
    for r in rows:
        print(r)
    for th in (0.10, 0.15, 0.20, 0.24, 0.249, 0.2499, 0.25):
        print("  theta = %.4f   I(theta) = %.10f nats/bit" % (th, I_rate(th)))

    print("=" * 78)
    print("C4  cylinder class structure at 3000-bit starts, n = 600 letters")
    print(check_C4())

    print("=" * 78)
    print("C5  concentration of multi-letter pattern frequencies")
    for bits, starts in ((750, 1500), (1500, 1500), (3000, 1500), (6000, 600)):
        r = check_C5(bits=bits, starts=starts)
        print({k: r[k] for k in ("bits", "theta", "N_bits", "T", "starts",
                                 "seed", "S_max", "budget_violations",
                                 "mean_exponent_per_block")})
        for row in r["patterns"]:
            print("   ", row)

    print("=" * 78)
    print("C8  window side: L=2 blocks of (min(s,3), min(d,3)), concentration")
    for row in check_C8():
        print({k: row[k] for k in ("bits", "T", "starts", "cells_seen",
                                   "TV_mean", "TV_max", "TV_mean_times_sqrtT")})
        for cr in row["busiest_cells"]:
            print("   ", cr)

    print("=" * 78)
    print("C6  the past-boundary term: law of a_n at n = 0, 1, 2, ...")
    r = check_C6()
    print("bulk (13.6.5) =", r["bulk"], "  uniform start =", r["uniform_start"])
    for row in r["rows"]:
        print("   ", {k: (round(v, 5) if isinstance(v, float) else v)
                      for k, v in row.items()})

    print("=" * 78)
    print("C7  the cut is non-binding (delegate B's S1), door coordinates")
    print(check_C7())
    print(check_C7(bits=2400, theta=0.24, starts=200, seed=34007))


if __name__ == "__main__":
    main()
```

---

## 9. Open questions — named, not smoothed over

1. **Uniformity in `(w, k, D, L, ε)` is not obtained and I did not try for it.** The threshold `N₀` grows
   with `L` through `W = O(L log|A_{k,D}| + log(1/ε))` and with `k, D` through `|A_{k,D}|^L`. Nothing on
   the page asks for uniformity, and a uniform version would be a strictly stronger statement than
   either hypothesis. Worth one clause in `13.2.4`(f), which the drop-in has.
2. **The proved boundary discard is far larger than the measured transient.** The proof discards
   `W = O(log(1/ε'))` visits; C6 shows the absorption law is at the bulk values from visit `2` onward.
   I did not attempt to prove a `2`-visit bound, and nothing depends on it. If someone wants it, the
   object to control is the law of `v_3(y_n + 1)` for `n = 0, 1` under uniform integer sampling, which
   is a finite `3`-adic computation of the same genre as `13.6.5`.
3. **`θ = 1/4` exactly.** `I(1/4) = 0`, so the argument gives nothing there, and the exact tail
   `P(Bin(b−1,½) < 2⌈b/4⌉)` tends to `0` only like `b^{-1/2}` times a constant — not fast enough to
   survive a union bound against the concentration term without further work. I did not push it. The
   record's strict inequality is correct and should stay strict.
4. **Nothing past `1/4`, and the barrier is an identity.** Recorded here so it is not mistaken for an
   unexplored direction: the Chernoff tilt `e^λ = 2(1−2θ)` requires `λ > 0`, i.e. `θ < 1/4`, and past
   that `{S_n ≥ b}` is the typical event, not a deviation. Any crossing needs a different technique, not
   a sharper constant. Per the brief and the README stopping rules, no effort was spent there.
5. **A's open question 3 (the `2·(0.93)^j` bound under `B̂`) is used by my §3.4(ii) and inherited
   unchecked.** I use `13.6.3`(iv) as printed. A flags a one-paragraph re-derivation in the two-sided
   setting as an apply-phase item; if that re-derivation changes the constant, only my `W = O(log(1/ε'))`
   moves, and no conclusion does.
6. **The composite five-coordinate labelled reconstruction is still not run as one test** (A's open
   question 4). My C8 exercises `(min(s,3), min(d,3))` jointly from the door orbit, which covers the two
   coordinates that carry the absorption, but not `min(σ,D)` and `min(a_+,D)` with the `ω`-residue in one
   assertion. This remains A's item.
7. **`13.2.5` is stated for the dyadic family and for geometrically separated families.** Whether a
   sub-geometric family (`N_j = j²`, say) admits any density-zero union statement I did not investigate;
   the answer is almost certainly no by the §2.2 construction, and nothing in the record wants one.
8. **The `13.4` calibration record is untouched by this round.** Every number there stands. The one thing
   the apply phase must not do is quote my C5/C8 measurements as calibration evidence: they run at
   `θ = 0.20 < 1/4`, inside the theorem, and they measure the theorem.
9. **The `13.2.3` anchor collision is resolved by my yielding, not by adjudication.** Two Wave 2
   delegates independently appended a `13.2.3`. My reason for yielding (§6.1) is mechanical — theirs is
   cited from inside the hypothesis statements, mine only from prose — and the author may reverse it at
   the cost of five pointer edits. Flagged rather than assumed.
10. **`13.2.5` at cut-weighting's budget clock.** I state the shell proposition with the observable
   indexed by `(ε, θ, X_N, w)` or `(ε, θ, X_N, k, D, L)`. Under their `(τ, θ)` reformulation the cut
   sequence drops out and `τ` joins the list; the proof is unaffected (the shell argument never inspects
   the property), but the dependence list printed on the page must match whichever hypothesis form is
   adopted. My §5.1 drop-in is written for their form; if the author keeps the cut, restore `(X_N)` to
   the list.
