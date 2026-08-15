---
status: REFERENCE (lookup and collision visibility only; no fact lives here)
scope: wiki-wide symbol registry — one row per symbol per frame, defining pointers by section number, closing collision index; subsumes spine.md §4 by reference
updated: 2026-08-15
source: the signed-layer containment audit (2026-08-15); briefs/symbols-registry-brief.md
---

# Symbols: the wiki-wide registry

This page is the wiki's one lookup surface for notation: one row per symbol **per frame** — glyph, one-line meaning, defining pointer, cross-links — closing with a collision index for every glyph that carries more than one meaning across the wiki. Every fact stays on its owning page; a row's meaning is a reminder, never a statement of record, and spine.md §4 (the note's own Dictionary of Symbols) remains the authority for the spine's four layers, subsumed here by reference. **Standing norm:** a session introducing notation checks this page first; a new symbol gets a row with its defining pointer; a reused glyph gets its collision cross-linked in the same commit.

## 1. Spine / block frame

Defined in spine.md §3 (definitions) and §4 (the note's dictionary); transforms in §5.

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `T` | the Collatz map on the positive integers: `x/2` (even), `3x+1` (odd) | spine.md §3.1, §4.1 | aeh.md's `T` is the odd-to-odd map — see collision index |
| `x` | an integer of the raw dynamics; at a block entry, `x = 2^m u − 1` | spine.md §3.1, §4.1 | `x_exit` below |
| `u` | the odd seed of a BlockEntry | spine.md §3.3, §4.3 | |
| `m` | 2-adic entry depth, `m = v₂(x+1) ≥ 1` | spine.md §3.3, §4.3 | `m_t` (§3), `m(y)` (§4); the odd-step frame's `m` is **not** this — index |
| `(u,m)` | BlockEntry coordinates of `x = 2^m u − 1` | spine.md §3.3, §4.3 | |
| `E` | the structural step on BlockEntry coordinates | spine.md §4.3 | |
| `a` | 3-adic content of the seed, `a = v₃(u)` | spine.md §3.4, §4.4 | collision (`a` ×4) — index |
| `ω` | structural odd core: `u = 3^a ω` with `3 ∤ ω` | spine.md §3.4, §4.4 | cycle states `ω_t` (§3) |
| `d` | combined depth `d = m + a` | spine.md §3.5, §4.4 | |
| `(ω,d)` | the reduced structural state | spine.md §3.5, §4.4 | |
| `R` | projection `R(u,m) = (ω,d)` | spine.md §3.6, §4.4 | ≠ `R_r`, `R_{p,q}` — index |
| `F` | the reduced self-map, `F(ω,d) = R(x_exit(ω,d))` | spine.md §3.7, §4.4 | ≠ `F_i` — index |
| `A` | structural-step numerator `A = 3^d ω − 1` | spine.md §4.5 | ≠ `A_n`, `A_P`, arc `A` — index |
| `s` | exit valuation `s = v₂(A)` | spine.md §4.5 | per-step `s_t` (§3); a door's `r` is the *next* step's `s` (§4) |
| `x_exit` | the deterministic odd exit, `x_exit = A/2^s` | spine.md §3.7, §4.5 | = the door `y` (§4; reverse.md 14.14.1) |
| `m₊ u₊ a₊ ω₊ d₊` | the next block's quantities; `₊` marks the next entry/state | spine.md §4.5 | `m₊ = v₂(C) − s`, `a₊ = v₃(C)` (§2) |

## 2. Stage / digit frame (and the anchor family)

Digit-cost decomposition on stage3.md/stage4.md; the anchors' consolidated map is anchors.md §17.1–17.6 (pointers only — homes below).

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `C` | the step's carry: `C = A + 2^s = 3^d ω + (2^s − 1) = 2^s(x_exit + 1)` | stage3.md 11.8.6, 11.8.6.1 | door dictionary `C = 2^s(y+1)` (reverse.md 14.14.1.1); ≠ `C(ω)`, coset `C` — index |
| `σ` | the digit cost / scale parameter, `σ = v₂(C) = s + m₊` | stage4.md 11.8.7.1–11.8.7.2 | same quantity per-step as `σ_t` (§3); other `σ`s — index |
| `c` | shifted valuation target, `c ∈ 1 + 8Z₂`: the problem `v₂(3^d ω − c)` | stage3.md 11.8.6.3, Lemma 11.8.6.3.1 | faces: entry-depth targets `1 − 2^s` (stage3.md 11.8.6.3), ladder targets `c = 3^{−k}` (ladder.md 15.5.1–15.5.2), cycle targets `c = −q` (cycles.md 12.6.1.3(c)) |
| `N(c)` | the anchor evaluated at the target `c` (same `N` as below) | stage3.md Lemma 11.8.6.3.1 | |
| `δ_s` | shift constant `δ_s = N(1 − 2^s)`, `s ≥ 3` | stage3.md Definition 11.8.6.3.2 | |
| `N(ω)` | the 2-adic anchor: `9^{N(ω)} = ω^{−1}`; `N(ω) = −log ω/log 9`; law `s = 3 + v₂(n − N(ω))` | stage1-synthesis.md 11.8.3.6 (Def 11.8.3.6.1, Thm 11.8.3.6.6) | anchors.md 17.1; ≠ numerator `N`, scale `N` — index |
| `n` | the depth exponent on the even lifting branch, `d = 2n` (odd branch `d = 2n + 1`) | stage1.md 11.8.1.6.1–11.8.1.6.2, 11.8.4.1 | cycles' `n` is a different quantity — index |
| `M(ω)` | the unified (orbit) anchor `M(ω) = N(ω²)`; law `s = 2 + v₂(d − M(ω))` | stage2.md Definition 11.8.5.6.1 | anchors.md 17.1; `M(W)` is **not** this — index |
| `ΔM` | the anchor increment `ΔM = M(ω₊) − M(ω) = N((ω₊/ω)²)` — the Bridge's object | stage2.md 11.8.5.6 (low-order law stage4.md 11.8.7.3.1) | bridge.md §16 |
| `C(ω)` | effective Baker constant, `C(ω) = 208·log9·logω` (digit-match ceiling) | stage1-synthesis.md 11.8.3.11 | anchors.md 17.4 |
| `M₃(y)` | the 3-adic mirror anchor: `2^{M₃(y)} = −1/y`, valued in `Z/2 × Z₃`; law `d = 1 + v₃(s − M₃(y))` | reverse.md Definition 14.2.2 (law 14.2.4) | anchors.md 17.1 |
| `E₃` | the mirror exponent group `lim Z/(2·3^{k−1}) ≅ Z/2 × Z₃` | reverse.md Proposition 14.2.3 | |
| `ΔM₃` | mirror anchor increment along `G`: `ΔM₃(y) = M₃(G(y)) − M₃(y)`, total on live doors | reverse.md Definition 14.14.5.1 (graded law 14.14.5.3; partial top-door form 14.8.2) | |
| `J(n)` | the door anchor `J(n) = M(n/3^{v₃(n)}) = M(n) + v₃(n)`, every odd `n` | reverse.md Definition 14.14.2.1, Corollary 14.14.2.3 | |
| `log₂3 − 1 ≈ 0.585` | the drift constant: a block grows `log x` iff `s < 0.585·m` | stage1.md 11.8.4.4 (size ledger) | reverse.md 14.6.3 (proof); cycles.md 12.5.2, §12.8 — constants entry, index |

## 3. Cycles numerator frame

cycles.md; per-step data in the §12 preamble, the elimination in 12.6.1, trim machinery in §12.8.

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `(m_t, s_t)` | the cycle profile: entry depths and exit valuations, `t ∈ Z/pZ` | cycles.md §12 preamble, Proposition 12.6.1 | |
| `ω_t` | the cycle's states' odd cores, `F(ω_t,d_t) = (ω_{t+1},d_{t+1})` | cycles.md §12 preamble | |
| `σ_t` | per-step 2-valuation `σ_t = v₂(C_t)`; as `σ_j = s_j + m_{j+1}` the index shift is essential | cycles.md §12 preamble; Proposition 12.6.1 | = frame 2's `σ` at step `t` |
| `a_t` | per-step absorption `a_t = v₃(C_t)` | cycles.md §12 preamble | |
| `n` | total entry-depth mass `n = Σ_t m_t` (odd steps of the underlying `T`-cycle) | cycles.md Proposition 12.1.1, 12.6.1 | **not** frame 2's `n = d/2` — index |
| `K` | total halvings `K = Σ_t σ_t = Σ_t s_t + n` | cycles.md Proposition 12.1.1, 12.6.1 | odd-step frame renames it `m` — warning row below |
| `q` | the seam gap `q = 2^K − 3^n > 0`; the parked condition is `q \| R₀` nontrivially | cycles.md Proposition 12.6.1 (period-1 instance 12.2.2) | **flagship collision** — three other `q`s, index |
| `R_r` | rotation numerators: `ω_r · 3^{a_{r−1}} · q = R_r`, one per rotation `r` | cycles.md Proposition 12.6.1 | transport recurrence 12.6.1.1; seam identity `N_r + q = 2^{m_r}R_r` (itinerary.md 14.15.9.2, integer form) |
| `M_t`, `S_t` | exponent bookkeeping inside `R_r`: `M_t = Σ_{j>t} m_j`, `S_t = Σ_{j<t} σ_j` | cycles.md Proposition 12.6.1 | ≠ the word masses of §4 — index |
| `ε_t` | cycle product errors: `2^K = 3^n·Π_t(1+ε_t)`, `ε_t = (2^{s_t}−1)/(3^{d_t}ω_t)` | cycles.md Proposition 12.1.1 | ≠ signature `ε` (§5) — index |
| `G_k` | repetition factor: `R₀(B^k) = R₀(B)·G_k` and `q_P = q_B·G_k` (descent) | cycles.md Remark 12.6.1.4 | ≠ exit map `G` — index |
| `γ`, `γ'` | trim margins `γ = K − log₂ q`, `γ' = γ + log₂ p` | cycles.md §12.8 preamble | |
| `w(A)` | arc weight `w(A) = (log₂3 − 1)·m(A) − s(A)`, `A` an arc of consecutive blocks | cycles.md §12.8 preamble (Theorem 12.8.1) | |
| `n₀(p)` | effective finiteness threshold at period `p` | cycles.md 12.8.2 | quoted in README |
| `Λ` | the Baker linear form `Λ = K log 2 − n log 3` | cycles.md 12.8.2 (proof) | ≠ aeh budget `Λ_N` — index |
| `c_gen`, `c_strat` | margin limit constants of the capacity–demand count (local: `β = log₂3`, `H` = binary entropy) | cycles.md Remark 12.6.1.5 | `β`, `H` — index |

**Odd-step frame renaming (warning).** Remark 12.6.1.2/12.6.1.3 restate the same equation with renamed letters:

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `(k, m, q)` | odd-step frame: `k` odd steps, `m` halvings, `q = 2^m − 3^k` — the **same** equation as `(n, K, q)` under `K ↔ m`, `n ↔ k` | cycles.md Remark 12.6.1.2 (renaming stated at 12.6.1.3) | **warning:** that `m` is this frame's `K`, unrelated to the entry depths `m_t`; that `k` is this frame's `n` |
| `L` | `L = log₂3` in the envelope `q₊ + q₋ = 2^{⌊kL⌋}` and the side-asymmetry density `{kL} < log₂(3/2)` | cycles.md Remark 12.6.1.2 | ≠ aeh block length `L` — index |

## 4. Door / itinerary frame

The seam (reverse.md §14.14) and the itinerary language (itinerary.md §14.15).

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `y` | a door — the exit integer of a reduced edge; **live** iff `3 ∤ y`; edge parameterized by `(y, s)` | reverse.md 14.14.1 (from 14.1.1, 14.6.5.1) | signed door space: nonzero odd `y ≠ −1` (itinerary.md 14.15.6.1) |
| `state(y) = (Ω, D)` | the door's state: `y + 1 = 2^m 3^a Ω`, `D = m + a` | reverse.md 14.14.1 / Definition 14.14.3.1 (recovery 14.6.5.1) | `D` — index |
| `stratum(y) = (m,r)` | `m = v₂(y+1)`, `q = (y+1)/2^m`, `r = v₂(3^m q − 1)`; extended to every odd `y` | reverse.md 14.14.4 (live doors); itinerary.md Definition 14.15.1.1 (general), 14.15.6.1 (signed, verbatim) | `r` = next step's `s`; `(m,r)` = `(m₊, s₊)` of the edge (reverse.md 14.14.6) |
| `q(y)` | the odd part of `y+1`: `q(y) = (y+1)/2^{m(y)}` | itinerary.md Definition 14.15.1.1 (in-line at reverse.md 14.14.3.1) | a fourth `q` — index |
| `G` | the exit map `G(y) = (3^m q − 1)/2^r`: `F` in door coordinates (semiconjugacy), `G = T^m` | reverse.md Definition 14.14.3.1 (semiconjugacy 14.14.3.2; block-map identity 14.14.7.1) | ≠ `G_k` — index; lowercase `g_j`, `g_P` below |
| `W` | a word: sequence of letters `(m_i, r_i)`, `m_i, r_i ≥ 1`; a door **follows** `W` letter by letter; bi-infinite form for the two-sided coding | itinerary.md Definition 14.15.1.2 (bi-infinite: 14.15.3.5) | ≠ aeh `W_{k,D}`, past-window `W` — index |
| `S(W)`, `M(W)` | word masses `S(W) = Σ(m_i+r_i)`, `M(W) = Σ m_i` | itinerary.md Definition 14.15.1.2, Lemma 14.15.1.4 (as period sums: Lemma 14.15.10.1) | `M(W)` is **not** `M(ω)` — index |
| `S_n`, `M_n` | prefix masses: `S_n = S` of the length-`n` forward prefix; `M_n = Σ_{i≤n} m_{−i}` of the depth-`n` past | itinerary.md 14.15.3(a), 14.15.3(b) / Theorem 14.15.5.1 | at whole periods `S_n = nS_P`, `M_n = nM_P` (Theorem 14.15.9.5) |
| `A_n`, `B_n` | composed affine constants of a fixed itinerary: `G^n(y) = A_n y + B_n` over `Z₃`, `v₃(A_n) = Σ m_i` | reverse.md Theorem 14.14.8.2 | `B_n → y₃` (itinerary.md 14.15.3.3); ≠ measure `B` — index |
| `α_i, β_i` | letter `(m_i,r_i)`'s affine constants: `α = 3^m 2^{−(m+r)}`, `β = (3^m − 2^m)2^{−(m+r)}`, `G(y) = αy + β` on the stratum | reverse.md Theorem 14.14.4.1 (glyphs named in 14.14.8.2's proof; `g_j(u) = α_j u + β_j`, itinerary.md 14.15.9 setup) | `β` — index |
| `y₂(W)` | the 2-adic limit: the unique point of the forward cylinder tower (the future pins it) | itinerary.md Definition 14.15.3.1 | |
| `y₃(W)` | the 3-adic limit of the backward offsets `B_n` (the past pins it) | itinerary.md Theorem 14.15.3.3 | = Tao's Syracuse variable, `Syrac(Z₃)/2` (aeh.md 13.6.5) |
| `y*` | a periodic word's composed fixed point `y* = B_P/(1−A_P)`; both adelic limits; rotations `y*_i`, one affine orbit | reverse.md Corollary 14.14.8.4; itinerary.md 14.15.9 setup, Lemma 14.15.9.2, Theorem 14.15.9.3 | classical cycle candidate (reverse.md 14.14.8.4, reconciliation) |
| `a/q` | `y*` in lowest terms: `q > 0` odd, `gcd(q,6) = 1`, sign on `a`, `3 ∤ a`; `q = 1` ⟺ the word carries an integer cycle | itinerary.md Lemma 14.15.9.1(2) | **flagship collision**: not §3's `q`, `a` — index; frames linked at cycles.md 12.6.1.1 ↔ itinerary.md 14.15.9.2 |
| `N`, `D` | the unreduced fixed-point fraction `y* = N/D`: explicit numerator `N`, `D = 2^{S_P} − 3^{M_P}` | itinerary.md Lemma 14.15.9.1 | seam identity `N_r + q = 2^{m_r}R_r` (14.15.9.2, integer form); `N`, `D` — index |
| `(p,q)` | a window: `p` past letters, `q` future letters, around the word's fixed origin | itinerary.md Definition 14.15.4.3 | a third `q`, a second `p` — index |
| `R_{p,q}(W)` | the positive realization set of the window | itinerary.md Definition 14.15.4.3 | signed `R^σ_{p,q}` (§5) |
| `H_{p,q}(W)` | positive realization height `min R_{p,q}(W)`; Bridge ⟺ bounded vs escaping | itinerary.md Definition 14.15.4.3 (equivalence Theorem 14.15.4.5) | ≠ entropy `H` — index |
| `P`, `P^{(i)}` | a period (finite letter tuple) and its `i`-th rotation; `W = P^∞` | itinerary.md 14.15.9 setup | |
| `S_P`, `M_P` | period masses `S_P = Σ_i(m_i+r_i)`, `M_P = Σ_i m_i`, shared by all rotations | itinerary.md 14.15.9 setup | |
| `A_P` | the period multiplier `A_P = 3^{M_P}/2^{S_P}` | itinerary.md 14.15.9 setup | |
| `Q_n` | the whole-period CRT modulus `Q_n = 2^{nS_P+1}·3^{nM_P}` | itinerary.md 14.15.9 setup, Theorem 14.15.9.5 | |
| `ρ_n` | the combined class representative `ρ_n = a·q^{−1} mod Q_n`, in `(0, Q_n)` | itinerary.md 14.15.9 setup, Theorem 14.15.9.5(3) | |
| `g_P` | the composed unit `g_P = 2^{S_P}·3^{M_P} mod q` | itinerary.md 14.15.9 setup | |
| `j_n` | progression offset `j_n = (qρ_n − a)/Q_n = −a·2^{−1}·g_P^{−n} mod q`, purely periodic | itinerary.md Theorem 14.15.9.6(1) | |
| `t_n`, `t(j)` | the mod-3 door datum `t_n = (a + 2j_n)·q^{−1} mod 3`; the dead class is `κ ≡ t_n (mod 3)` | itinerary.md Theorem 14.15.9.6(2)–(3); `t(j)` at 14.15.9(d) | |
| `k₀` | escape index of the integer-fixed-point (capped) case, `k₀ ∈ {1,2}` by the first-viable rule | itinerary.md 14.15.7 (owner Corollary 14.15.9.7) | |
| `F_i` | the composed affine map of the rotation `P^{(i)}`, fixed point `y*_i` | itinerary.md Lemma 14.15.9.2 | ≠ the reduced map `F` — index |

## 5. Signed layer

itinerary.md §14.15.6 (the signed diagonal) and §14.15.9 (per-sector height laws).

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `σ` | the sector sign, `σ ∈ {+1, −1}` | itinerary.md Definition 14.15.6.8 | fourth `σ` row — index |
| `R^σ_{p,q}(W)` | per-sector realization set (sign-`σ` live doors; `σ = +1` recovers `R_{p,q}`) | itinerary.md Definition 14.15.6.8 | |
| `H^σ_{p,q}(W)` | per-sector height `min{\|y₀\| : y₀ ∈ R^σ_{p,q}(W)}` | itinerary.md Definition 14.15.6.8 (equivalence Theorem 14.15.6.10) | |
| `H⁺`, `H⁻` | the two sectors' whole-period heights; closed forms `H⁺ = ρ_n + [t_n=0]·Q_n`, `H⁻ = (1+[t_n=2])·Q_n − ρ_n` | itinerary.md Theorem 14.15.9.6(4) | instances 14.15.7–14.15.8 |
| `κ` | class parametrization `y₀ = ρ_n + κQ_n`, `κ ∈ Z`; sectors are `κ = k ≥ 0` and `κ = −k, k ≥ 1` | itinerary.md Theorem 14.15.9.6 | |
| `k⁺_n`, `k⁻_n` | first-viable progression indices: `k⁺_n = [t_n = 0] ∈ {0,1}`, `k⁻_n = 1 + [t_n = 2] ∈ {1,2}` | itinerary.md Theorem 14.15.9.6(3) | |
| `V₊(j)`, `V₋(j)` | normalized-height value functions `V₊ = j/q + [t(j)=0]`, `V₋ = 1 + [t(j)=2] − j/q` | itinerary.md 14.15.9(d) preamble | |
| `v_n` | normalized height `v_n = H^σ_{np,np}(W)/Q_n − σ·a/(qQ_n) = V_σ(j_n)`, purely periodic | itinerary.md Corollary 14.15.9.8 | |
| `P_alg` | the exact period `ord_q(g_P)` of `(j_n)` and `(v_n)` | itinerary.md Corollary 14.15.9.8 (from Theorem 14.15.9.6(1)) | |
| `c_σ(W)` | the sharp escape constant `c_σ = min_n v_n = min_O V_σ(j)` (not `j_min/q` in general) | itinerary.md Corollary 14.15.9.9 | third `c` — index |
| `sig(W)`, `C`, `ε` | the spectrum invariant `sig(W) = (q, g_P, C, ε)`: coset `C = −a·2^{−1}·⟨g_P⟩ ⊆ (Z/q)^×`, residue `ε = y* mod 3 ∈ {1,2}` (per rotation: `ε_i`, Lemma 14.15.9.2(3)) | itinerary.md Theorem 14.15.9.11 | `C`, `ε` — index |
| `Spec_σ(W)` | the per-sector escape spectrum `{v_n : n ≥ 1} = V_σ(C)`, a function of `sig(W)` alone | itinerary.md Theorem 14.15.9.11(1) | |

## 6. AEH / measure frame

aeh.md §13: the hypothesis (13.2), the symbolic identification (13.6).

| Symbol | Meaning | Defined | Elsewhere |
|---|---|---|---|
| `T`, `T₁` | this frame's `T` is the **odd-to-odd** map (`G = T^m`); `T₁` the one-division map `y ↦ y/2` or `(3y+1)/2`; three readings of `T` kept apart in-page | aeh.md 13.2.3 | spine's `T` is the raw map — index |
| `σ` | the shift on the full letter shift; `Φ ∘ G = σ ∘ Φ` | aeh.md Theorem 13.6.2(3) | index |
| `Φ` | the coding `y ↦ (stratum(G^i(y)))_{i≥0}`, a bijection off `X_sing` onto the full shift | aeh.md Theorem 13.6.2(2) | |
| `X_sing` | the countable singular set: odd `y ∈ Z₂` whose forward `G`-orbit hits `−1` | aeh.md Theorem 13.6.2 | itinerary.md 14.15.3(a), remark |
| `B`, `B̂` | the Bernoulli letter measure `⊗(geom(1/2) × geom(1/2))`, one-sided (`B`) and two-sided (`B̂`) | aeh.md 13.2 (`B̂`); Theorem 13.6.2(4) (`B`) | letter law Lemma 13.6.1 |
| `W_{k,D}(n)` | the capped depth-`k` window at visit `n` (five capped coordinates; a statistic, not stage4's deciding window) | aeh.md 13.2 | contrast stated at 13.2 vs stage4.md 11.8.7.6 |
| `π_{k,D}` | the stationary capped-window law under `B̂`; "product" names exactly two proved clauses | aeh.md 13.2 (derived at Theorem 13.6.3(v); depth marginal Proposition 13.6.5) | |
| `k`, `D` | window depth and cap (chosen together, quantified over) | aeh.md 13.2 | `D` — index |
| `τ`, `θ` | budget rate and block horizon rate; **admissible** = protected + consistent (`4θ < τ`); base case a theorem for `θ < 1/4` | aeh.md Hypothesis 13.2.1, 13.2.3 (base case Lemma 13.2.4, Corollary 13.2.4.1) | |
| `Λ_N`, `T_N`, `b` | budget `Λ_N = ⌈τb⌉`, block horizon `T_N = ⌈θb⌉`, `b = ⌊log₂ N⌋` at sampling scale `N` | aeh.md Hypothesis 13.2.1 | `Λ`, `N` — index |
| `ℓ_n`, `ℓ̃_n`, `†` | the letter at block `n`; its tallied symbol; the cemetery symbol (out of budget) | aeh.md Hypothesis 13.2.1 | |
| `S_n` | exponent spent before block `n` — **two counts kept apart in-page**: budget `Σ(m_i+s_i)` (13.2.1) vs letter `Σ(m_i+r_i)` (13.2.4) | aeh.md Hypothesis 13.2.1; the two readings at 13.2.3 | itinerary's `S_n` — index |
| `a` | the absorption `a_{+,n+1} = v₃(C_n) = v₃(y_n + 1)`, a function of the letter past alone | aeh.md 13.2, Lemma 13.6.3(iii) | collision (`a` ×4) — index |
| `ν_j` | the exact law of the absorption at precision `3^j` (`ν_1 = (2/3, 1/3)`) | aeh.md Proposition 13.6.5 | |
| `β` | `β = 2(2 − log₂3) = 0.8301…`; `1/β` blocks per bit is the descent ceiling | aeh.md 13.2.3 | ≠ affine `β_i`, ≠ cycles' local `β` — index |

## 7. Collision index

Every glyph with two or more registry rows, all meanings side by side. Frame numbers refer to the sections above.

| Glyph | The meanings, side by side |
|---|---|
| `σ` | **(2)** digit cost `σ = v₂(C) = s + m₊` (stage4.md 11.8.7.2) · **(3)** the same quantity per-step, `σ_t = v₂(C_t)` (cycles.md §12 preamble) · **(5)** sector sign `σ ∈ {+1,−1}` (itinerary.md 14.15.6.8) · **(6)** the shift map (aeh.md 13.6.2(3)). Four rows; the first two are one quantity in two frames. (`5σ` in calibration prose is standard deviations, not a registry symbol.) |
| `q` | **(3)** seam gap `q = 2^K − 3^n` (cycles.md 12.6.1) · **(4)** door odd part `q(y) = (y+1)/2^m` (itinerary.md 14.15.1.1) · **(4)** fixed-point denominator in `y* = a/q` (itinerary.md 14.15.9.1) · **(4)** window future-length in `(p,q)` (itinerary.md 14.15.4.3). **The flagship hazard is reading `q \| R₀` with the wrong `q`.** The frames connect but do not coincide: reduced `q` divides the unreduced `D = 2^{S_P} − 3^{M_P}` (= frame 3's `q` on the cycle's word), and `q = 1` (frame 4) ⟺ `q \| R₀` nontrivially (frame 3) — cycles.md 12.6.1.1 ↔ itinerary.md 14.15.9.2. |
| `a` | **(1)** 3-adic content `a = v₃(u)` (spine.md §3.4) · **(3)** per-step absorption `a_t = v₃(C_t)` (cycles.md §12 preamble) · **(4)** fixed-point numerator in `y* = a/q` (itinerary.md 14.15.9.1) · **(6)** the absorption as a random variable (aeh.md 13.2/13.6.3). Rows 1, 2, 4 are one `v₃`-family; the numerator `a` is unrelated. |
| `m` | **(1)** entry depth `m = v₂(x+1)` (spine.md §3.3) · **(3)** profile entries `m_t` (cycles.md 12.6.1) · **(3, odd-step frame)** total halvings — that frame's `m` is this wiki's `K`, **not** an entry depth (cycles.md 12.6.1.2/12.6.1.3) · **(4)** stratum component `m(y) = v₂(y+1)` (itinerary.md 14.15.1.1). |
| `r` | **(4)** stratum component `r(y) = v₂(3^m q − 1)` — the next step's `s` (reverse.md 14.14.4) · **(3)** rotation index in `R_r` (cycles.md 12.6.1). Also a pervasive truncation-precision parameter (`ω₊ mod 2^r`, stage4.md 11.8.7.2.3) — a bound variable, not a row. |
| `n` | **(2)** lifting-branch depth exponent, `d = 2n` (stage1.md 11.8.1.6.1, 11.8.4.1) · **(3)** cycle mass `n = Σ_t m_t` (cycles.md 12.6.1). Also the generic index of `S_n`, `M_n`, `Q_n`, `ρ_n`, `j_n`, `v_n` (§4–§5: number of periods/letters) and the visit index (§6). |
| `K` | **(3)** total halvings `K = Σ s_t + n` (cycles.md 12.6.1) — renamed `m` in the odd-step frame (12.6.1.2/12.6.1.3). Caution, in-page at cycles.md 12.5 ("Measure, pinned"): Simons–de Weger's `K` is our `n`, their `K+L` our `K` (external pin, stays there). Mirror window depth `K` (reverse.md 14.9.1) is a bound variable. |
| `M` | **(2)** the anchor `M(ω) = N(ω²)` (stage2.md 11.8.5.6.1) · **(3)** tail sums `M_t = Σ_{j>t} m_j` (cycles.md 12.6.1) · **(4)** word/prefix/period masses `M(W)`, `M_n`, `M_P` (itinerary.md 14.15.1.4/14.15.3/14.15.9). **`M(ω)` vs `M(W)`: same letter, same shape, different objects** — anchor of a core vs `m`-mass of a word. (`M₃` is the mirror anchor, its own glyph.) |
| `S` | **(3)** partial `σ`-sums `S_t = Σ_{j<t} σ_j` (cycles.md 12.6.1) · **(4)** word/prefix/period exponent masses `S(W)`, `S_n`, `S_P` (itinerary.md 14.15.1.2/14.15.3/14.15.9) · **(6)** exponent spent `S_n` — itself carrying two in-page readings, budget `Σ(m+s)` vs letter `Σ(m+r)`, kept apart at aeh.md 13.2.3. |
| `R` | **(1)** the projection `R(u,m) = (ω,d)` (spine.md §3.6) · **(3)** rotation numerators `R_r` (cycles.md 12.6.1) · **(4/5)** realization sets `R_{p,q}`, `R^σ_{p,q}` (itinerary.md 14.15.4.3/14.15.6.8). |
| `k` | **(3, odd-step frame)** odd-step count — that frame's `k` is this wiki's `n` (cycles.md 12.6.1.2) · **(2)** ladder step in the targets `c = 3^{−k}` (ladder.md 15.5.1) · **(5)** progression index `κ = ±k` with `k⁺_n`, `k⁻_n`, `k₀` (itinerary.md 14.15.9.6–14.15.9.7) · **(6)** window depth in `W_{k,D}` (aeh.md 13.2). Also the wiki's default truncation-precision parameter (`mod 2^k`, `mod 3^k`) — a bound variable, not a row. |
| `T` | **(1)** the raw Collatz map (spine.md §3.1) · **(6)** the odd-to-odd map, with `T₁` (one-division) and `T_N` (block horizon) — the three readings kept apart at aeh.md 13.2.3. |
| `F` | **(1)** the reduced map (spine.md §3.7) · **(4)** rotation-composed affine maps `F_i` (itinerary.md 14.15.9.2). |
| `G` | **(4)** the exit map on doors (reverse.md 14.14.3.1) · **(3)** repetition factor `G_k` (cycles.md 12.6.1.4). Lowercase `g_j`/`g_P` (§4) are the letter maps and the composed unit. |
| `A` | **(1)** step numerator `A = 3^d ω − 1` (spine.md §4.5) · **(4)** composed multipliers `A_n`, `A_P` (reverse.md 14.14.8.2; itinerary.md 14.15.9) · **(3)** an arc of blocks in `w(A)` (cycles.md §12.8). |
| `B` | **(4)** composed offsets `B_n`, `B_P` (reverse.md 14.14.8.2) · **(6)** the Bernoulli measure `B`, `B̂` (aeh.md 13.2/13.6.2). |
| `C` | **(2)** the carry `C = A + 2^s` (stage3.md 11.8.6) · **(2)** Baker constant `C(ω)` (stage1-synthesis.md 11.8.3.11) · **(5)** the signature coset `C = −a·2^{−1}·⟨g_P⟩` (itinerary.md 14.15.9.11). |
| `D` | **(4)** state depth in `state(y) = (Ω, D)` (reverse.md 14.14.1/14.6.5.1) · **(4)** unreduced fixed-point denominator `D = 2^{S_P} − 3^{M_P}` (itinerary.md 14.15.9.1) · **(6)** the cap in `W_{k,D}` (aeh.md 13.2). |
| `N` | **(2)** the anchor `N(ω)`, `N(c)` (stage1-synthesis.md 11.8.3.6) · **(4)** unreduced fixed-point numerator (itinerary.md 14.15.9.1) · **(6)** the sampling scale (aeh.md 13.2.1). |
| `H` | **(4/5)** realization heights `H_{p,q}`, `H^σ_{p,q}`, `H^±` (itinerary.md 14.15.4.3/14.15.6.8/14.15.9.6) · binary entropy `H`, named inline where used (cycles.md 12.6.1.5; aeh.md 13.2.4(b)). Simons–de Weger's `H` (cycles.md 12.5) is an external pin and stays there. |
| `W` | **(4)** a word (itinerary.md 14.15.1.2) · **(6)** the capped window `W_{k,D}` (aeh.md 13.2) · **(6)** the letter past-window depth (aeh.md 13.6.3(iii)). |
| `L` | **(3, odd-step)** `L = log₂3` (cycles.md 12.6.1.2) · **(6)** pattern/block length (aeh.md 13.2.1). Simons–de Weger's `L` (cycles.md 12.5) is an external pin. |
| `Λ` | **(3)** the Baker linear form `Λ = K log 2 − n log 3` (cycles.md 12.8.2) · **(6)** the budget `Λ_N = ⌈τb⌉` (aeh.md 13.2.1). |
| `β` | **(4)** letter affine offset `β_i` (reverse.md 14.14.4.1/14.14.8.2) · **(3)** local `β = log₂3` in the margin constants (cycles.md 12.6.1.5) · **(6)** `β = 2(2 − log₂3)`, the block-per-bit constant (aeh.md 13.2.3). |
| `ε` | **(3)** cycle product errors `ε_t` (cycles.md 12.1.1) · **(5)** signature residue `ε = y* mod 3`, per-rotation `ε_i` (itinerary.md 14.15.9.11/14.15.9.2(3)). Generic analysis `ε` (tolerances) is prose. |
| `c` | **(2)** the shifted valuation target family (stage3.md 11.8.6.3) · **(5)** sharp escape constant `c_σ(W)` (itinerary.md 14.15.9.9) · **(3)** margin limit constants `c_gen`, `c_strat` (cycles.md 12.6.1.5). |
| `p` | **(3)** the cycle period (cycles.md §12) · **(4)** past-window length in `(p,q)` (itinerary.md 14.15.4.3). |

**Numerical constants.**

| Numeral | The roles, side by side |
|---|---|
| `0.585` | One real number — `log₂3 − 1 = log₂(3/2) = 0.58496…` — in two unrelated roles: **the drift constant** (`m`-mass exchange rate: growth iff `s < 0.585·m`; stage1.md 11.8.4.4, reverse.md 14.6.3, cycles.md 12.5.2 and §12.8) and **the side-asymmetry density** (the Weyl density of `{kL} < log₂(3/2)`, the negative tower nearer; cycles.md 12.6.1.2). The two expressions are algebraically equal, so the numeral alone never says which role is meant — cite the section, not the number. |
