# Findings: L-A5 verify (merle-la5-check)

Delegated session, 2026-07-24. Brief: `briefs/merle-la5-check-brief.md`.
Branch `merle-la5-check`, base commit `1a32206` (the brief commit). Launch note,
for the record: the worktree was cut at `d74f430` (one commit behind the brief);
the branch was created directly from `1a32206`, which was present in the
repository — no rebase needed; `1a32206` is a descendant of `d74f430`, so the
brief's "verify `d74f430` or a descendant" is satisfied.
Register: findings only; confirmations and flags separated; nothing here
disputes the entry's text — where observation and claim differ, both are
recorded. Verification code: `experiments/merle_la5_check.py` (fresh code,
imports nothing from any Merle repository and nothing from prior Merle-check
scripts; conventions re-implemented from cycles.md 12.6.1/12.6.1.1 only; exact
integer arithmetic at every pass/fail decision; canaries hand-computed and
printed before sweeps); full run output committed alongside as
`experiments/merle_la5_check_output.txt`. **~10,372 exact decisions, 0
failures.** No pushes, no shared-repo or Merle-repo writes; all clones
unauthenticated and read-only into the scratchpad. **Handbacks: none.**

## Item 1 — the shared repo and the Lean artifacts, read-only

### (i) Shared repo state

Unauthenticated clone of `github.com/macindoe/one-obstruction-three-faces`
(2026-07-24). **HEAD `740edb3c4af3720e298f1af048c9fc0b400cd426` (`740edb3`,
ours) — exactly as expected; not moved.** The L-A5 entry sits in `LEDGER.md`
under Merle's seed commit `9f2dbcc`, below our three re-seated key-turn commits.

### (ii) L-A5 entry text, verbatim (entire entry)

> ## L-A5 — The adelic content invariant and the separation lemma (Merle, correspondence 2026-07-24)
>
> **DRAFT — one key (Merle side: Lean kernel + independent scripts); Macindoe key invited.**
>
> The content `C(P) = log gcd(q, R_0) / log |q| ∈ [0,1]` (rotation-invariant by L-A1's corollary;
> `C = 1 ⟺ cycle`) is the normalized fixed-point denominator collapse — the fixed-point-denominator
> frame is Macindoe's (`cycles.md`, `index.md`); the normalization and the landscape results are the
> new part. Measured landscape (REQ-MATH-018): aperiodic words sit at the pure-chance level at
> sampled depth (max `C` 0.11–0.50, tracking `q`'s wild factorization); repeated words `B^j` climb
> `C → 1` exactly per the L-A2 law; a single-letter change at fixed `q` collapses `C` to background.
> The cliff is now a **theorem**:
>
> **Separation lemma (T1/T2).** For adjacent one-unit transfers at fixed `q` (in the 2-shifted
> numerator `W0 = 2^{m_0} R_0`, same gcd with the odd `q`): the s-transfer difference is
> `2^{mssum(pre)} · 3^{msum(suf)} · 2^{m_1+s_1} · (3^{m_2} − 2^{m_2})` and the m-transfer difference is
> `−2^{mssum(pre)} · 3^{m_2+msum(suf)} · 2^{m_1} · (2^{s_1} − 1)` — valid at every position in W0
> coordinates (the boundary case is regular there). **Corollary:** a common divisor of `q` shared by
> two neighbours divides the letter-scale seam `3^{m_2} − 2^{m_2}` resp. `2^{s_1} − 1` — the letter
> constant being exactly the composed one-letter constant of Macindoe's affine law (`itinerary.md`,
> `β` and `G(y)`); with `m = 1`: shared content 1, total isolation. So content towers have no
> shoulders: the only road to `C = 1` is exact repetition, and repetition is sterile [L-A4]. The
> residual gap of NOTE §6 is thereby sharpened: no *aperiodic* word reaches `C = 1`.
>
> **Artifacts — Merle (2026-07-24), stack `e297d9d`:**
> [`OneObstruction/ContentSeparation.lean`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/e297d9d/OneObstruction/ContentSeparation.lean)
> — T1, T2, separation_T1/T2, q_divisor_coprime, all **kernel-3** (`propext`, `Classical.choice`,
> `Quot.sound`), **0 sorry, no user axioms, no `native_decide`**, non-vacuity canaries inside;
> [`REQ-MATH-018`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/9932f3f/experiments/test_REQ-MATH-018_contenu_adelique.py)
> (content landscape), [`REQ-MATH-019`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/9932f3f/experiments/test_REQ-MATH-019_lemme_separation.py)
> (identities exact 713/713, 604/604; corollary 560/560),
> [`REQ-MATH-020`](https://github.com/ericmerle3789/one-obstruction-three-faces-lean/blob/e297d9d/experiments/test_REQ-MATH-020_pont_lean.py)
> (Lean↔Python bridge `W0 = 2^{m_0} R_0`, exact 300/300 each). Anteriority sweep of `macindoe/collatz`
> (2026-07-24): "adjacent transfer", "separation/cliff", "adelic content" — no occurrences; the letter
> constant and the fixed-point-denominator frame are Macindoe's, credited above. Open for co-editing.

### (iii) Lean repo and commit graph

Unauthenticated clone of `ericmerle3789/one-obstruction-three-faces-lean`. One
wrinkle, recorded flat: the initial clone was served at `017288f` while
`ls-remote` already showed `main` at `e297d9d`; a direct `fetch origin main`
resolved it (stale mirror on the first clone). Both claimed commits exist on
`main`, and both post-date `017288f` as expected; the graph order is

- `017288f` (2026-07-24 12:38 +0200) — REQ-MATH-013..017 (the round-8 stack);
- `3ed1ef4` (14:38) — REQ-MATH-018 (content witness);
- `9932f3f` (14:56) — REQ-MATH-019 + the theorem doc ("the cliff is now a
  theorem");
- `e297d9d` (15:12, HEAD of `main`) — `ContentSeparation.lean` + REQ-MATH-020.

Pin note: the entry links REQ-MATH-018 at `9932f3f`; the file entered at
`3ed1ef4` but exists in `9932f3f`'s tree, so the link resolves. Not a mismatch.

### (iv) `ContentSeparation.lean` — statement-level review, clause by clause

The file defines `msum`, `mssum`, and the fold
`W0 [] = 0; W0 ((m,s)::rest) = 3^(msum rest)·2^m·(2^s − 1) + 2^(m+s)·W0 rest`
over `List (ℕ × ℕ)`, with the header claiming `W0(l) = 2^(m₀)·R₀(l)` for
nonempty `l` (numerically bridged in REQ-MATH-020) and regularity of the
position-0 m-transfer in `W0` coordinates. Against the entry's claim (3):

| Entry clause | Lean statement | Match |
|---|---|---|
| s-transfer difference `2^{mssum(pre)}·3^{msum(suf)}·2^{m₁+s₁}·(3^{m₂}−2^{m₂})` | `theorem T1`: `W0(pre ++ (m₁,s₁+1)::(m₂,c)::suf) − W0(pre ++ (m₁,s₁)::(m₂,c+1)::suf) = 2^mssum pre · (3^msum suf · 2^(m₁+s₁) · (3^m₂ − 2^m₂))` | **Exact** |
| m-transfer difference `−2^{mssum(pre)}·3^{m₂+msum(suf)}·2^{m₁}·(2^{s₁}−1)` | `theorem T2`: `= −(2^mssum pre · (3^(m₂+msum suf) · 2^m₁ · (2^s₁ − 1)))` | **Exact** |
| valid at every position, boundary regular in `W0` | `pre` is an arbitrary list in both theorems, including `[]` | **Exact** |
| corollary: shared divisor of `q` divides the letter seam | `separation_T1`/`separation_T2`: `d` coprime to 2 and 3 dividing both `W0` values divides `3^m₂ − 2^m₂` resp. `2^s₁ − 1`; `q_divisor_coprime`: every divisor of `2^K − 3^n` (`K, n ≥ 1`) is coprime to 2 and 3 | **Exact** (the coprimality hypothesis is discharged by `q_divisor_coprime` exactly as the entry composes them) |
| at `m = 1` shared content is 1 | immediate from `3^1 − 2^1 = 1` (and dually `2^1 − 1 = 1` for T2); not a separate Lean theorem, follows from `separation_T1` | Consistent (arithmetic consequence, not a named statement) |

Two flat statement-level observations. (1) The Lean letters live in `ℕ²` with
zero entries allowed — a superset of the wiki's entries-`≥ 1` convention; the
theorems are strictly more general, harmless. (2) The three non-vacuity
canaries (`W0 [(1,1),(1,1)] = 14`; a T1 instance `= 608`; a T2 position-0
instance `= −6`) were re-derived by hand this session and match.

**Build status, honestly: read, not built.** No Lean toolchain is available on
this machine (`lake`/`elan` absent), so the ~15-minute build window could not
be attempted. By read: 0 occurrences of `sorry`, 0 of `native_decide`, no
`axiom` declarations, single `import Mathlib`; the file ends with five
`#print axioms` commands whose *output is not committed anywhere in the repo*,
so the "kernel-3 (`propext`, `Classical.choice`, `Quot.sound`)" claim rests on
his header statement, not on a committed log — same posture as the L-A1
precedent, recorded flat. Independent of the build, the mathematical content of
T1/T2 and the corollary is confirmed by this session's own derivation and
machine verification (item 2c below), so nothing downstream hangs on the build.

### (v) The three REQ scripts — read, never run

- **REQ-MATH-018** (`contenu_adelique`): defines `C = log₂ gcd(q, R₀)/log₂ q`;
  canaries trivial² (`C = 1`), `(1,3)²` (`gcd 19`), staircase seed (`gcd 7`),
  rotation invariance; (A) random tuned profiles at `n ∈ {17, 25, 40, 63}`,
  `N = 20,000` each — his output: max aperiodic `C` = 0.3803, 0.5019, 0.2500,
  0.1093 (the entry's "0.11–0.50"); (B) `B^j` for bases `(1|3)` and
  `(1,2|3,1)` with the gcd formula `|q_P|/q_red` checked exact, `C` climbing
  0.5344 → 0.8844; (C) the cliff — one-letter transfers at fixed `q` on
  `B^j` towers, max perturbed `C` 0.00–0.35 vs tower `C` 0.68–0.85.
- **REQ-MATH-019** (`lemme_separation`): the operational definitions this
  session adopted — **T1 = adjacent s-transfer `(s_i+1, s_{i+1}−1)`**, `i ∈
  [0, p−2]`; **T2 = adjacent m-transfer `(m_i+1, m_{i+1}−1)`**, `i ∈ [1, p−2]`
  in `R₀` coordinates, with the R₀-frame closed forms
  `R₀(P′) − R₀(P) = 3^{M_{i+1}}·2^{S_i+s_i}·(3^{m_{i+1}} − 2^{m_{i+1}})` resp.
  `−3^{M_i−1}·2^{S_i}·(2^{s_i} − 1)`; the `i = 0` m-transfer has no simple
  closed form in `R₀` (the wrap term) — his header records a first version
  *rejected by the machine* and the rotation reduction used instead (licit by
  L-A1's rotation invariance), which is exactly what the Lean `W0` frame then
  repairs (position 0 regular). His output: 713/713, 604/604, 605/605
  (rotation), corollary 560/560 with isolation 553/560; plus the fixed-point
  reformulation `den(R₀/q) = |q|/gcd` and `x(B^j) = x(B)` (the L-A2 law in one
  line) — consistent with our Lemma 14.15.9.2/14.15.10.1 frame, which the
  entry credits.
- **REQ-MATH-020** (`pont_lean`): bridge `W0 = 2^{m₀}·R₀` 300/300; Lean-form
  T1/T2 in Python 300/300 each; position-0 T2 regular 300/300.

Convention check: his `R0` uses `sigma_t = s_t + m_{(t+1) mod p}` — exactly
cycles.md 12.6.1's convention; our independent implementation agrees on every
recorded instance.

### (vi) Anteriority claim

His sweep terms ("adjacent transfer", "separation/cliff", "adelic content")
were re-grepped over this repository's wiki pages: the only hit is
`HANDOFF.md`'s own description of the L-A5 seed (written after his push). The
credit split as stated — normalization and landscape his; the
fixed-point-denominator frame, the letter constant `β`/`G(y)`, and the
denominator-collapse reading ours — is accurate against 14.15.9.1–2 and
14.15.10.1–2.

## Item 2 — independent computational verification

`experiments/merle_la5_check.py`, run 2026-07-24; committed output alongside.
Canaries hand-computed and printed before any sweep: trivial² (`q = R₀ = 7`,
`C = 1`), **the `−17` scope canary** (below), the `(−5)`-shore and trivial
words (the `|q| = 1` domain edge), the `p = 7` staircase seed (`gcd = 7`,
`C = 0.0197`), the L-A2 word `(1,3)²` (`gcd = 19`, `C = 0.5344`), and
hand-computed numeric T1/T2/bridge instances. All passed before any sweep.

### (a) The invariant — CONFIRMED, with one domain note

- `gcd(q, R_r)` rotation-invariant: 600/600 random profiles (both signs of
  `q`, tuned and untuned) — the entry's "by L-A1's corollary" checks out.
- `C ∈ [0,1]` and `C = 1 ⟺ q | R₀`, in exact integer form
  (`1 ≤ gcd ≤ |q|`; `gcd = |q| ⟺ |q| divides R₀`): 600/600.
- **The `−17` scope canary, exact:** the `−17` cycle's word in 12.6.1
  coordinates is `m = (4,3)`, `s = (1,3)` (the door-word `((4,1),(3,3))` of
  14.15.10.1(4)): `n = 7`, `K = 11`, `q = 2^{11} − 3^7 = −139`,
  `R₀ = 3^3·(2^1−1) + 2^4·(2^3−1) = 27 + 112 = 139` (hand-computed),
  `gcd(q, R₀) = 139 = |q|` — **`C = 1` exactly**, with `|q| = 139` as the
  brief expected. The word is **primitive** (not a proper power) and
  **untuned** (`K = 11 < bitlength(3^7) = 12`, `q < 0`).
- Domain note, flat: `C` is `0/0`-undefined at `|q| = 1` — exactly the
  spent-stock words of 12.6.1.2 (trivial word, `(−5)`-shore word). The
  entry's "`C ∈ [0,1]`" silently assumes `|q| > 1`. Co-edit candidate, minor.
- On "`C = 1 ⟺ cycle`": `C = 1 ⟺ q | R₀`, and `q | R₀` nontrivially is
  integral realization of the word's fixed point (14.15.10.2, via the seam
  identity), sign carried by `sign(q)` — so the biconditional is right for
  `|q| > 1`, with the realized cycle on the sign-`q` shore (untuned negative
  `q` gives negative cycles: `−17` itself). Recorded as a precision, not a
  defect.

### (b) The landscape — consistent-at-reduced-scale, plus the exact climb law

- **(b1) Aperiodic band:** max `C` over sampled aperiodic tuned words
  (uniform compositions, `N = 4,000` per depth): 0.3803 (`n = 17`), 0.3018
  (`n = 25`), 0.2400 (`n = 40`) — inside/consistent with his 0.11–0.50 at his
  larger `N` and deeper grid. Labeled spot check, not a key turn.
- **(b2) `B^j` climb — the exact law, derived:** by the descent identity
  (12.6.1.4, re-verified here at every draw): `R₀(B^j) = R₀(B)·G_j` and
  `q_{B^j} = q_B·G_j` with `G_j = Σ_{c<j} 3^{(j−1−c)n_B}2^{cK_B} > 0`, so
  `gcd(q_{B^j}, R₀(B^j)) = G_j·gcd(q_B, R₀(B))` **exactly** — whence

  ```text
  C(B^j) = (ln G_j + ln g_B)/(ln G_j + ln |q_B|),   g_B := gcd(q_B, R₀(B)),
  1 − C(B^j) = ln(|q_B|/g_B)/ln(G_j·|q_B|) ~ c/j     (G_j has ~ (j−1)K_B bits).
  ```

  Checked exact on 75 (base, j) identity checks over five bases including
  negative-`q` and the `−17` word itself; his OUT-018 table values reproduced.
  Two flat consequences the gloss adjudication needs: **the climb `C → 1`
  happens for every base, divisible or not** (the entry's "per the L-A2 law"
  is exactly this); and **`C(B^j) = 1` at finite `j` iff `C(B) = 1`** (iff the
  base is already a cycle) — 12 exact checks. Repetition approaches `C = 1`;
  it *reaches* it only from a cycle.
- **(b3) Single-letter collapse:** at fixed `(n, K)` on his three towers,
  100 perturbations each: tower `C` 0.68/0.76/0.85 vs perturbed max
  0.00/0.26/0.35, mean 0.00/0.08/0.13 — the cliff reproduced at reduced scale.

### (c) T1/T2 clean-room — the derivation goes through; formulas EXACT

**Derivation (this session, from the `W0` fold alone).** Prefix lemma: the
contribution of `pre`'s letters to `W0(pre ++ r)` depends on the tail `r` only
through `msum r` (each prefix term carries `3^{msum(everything after it)}`),
and each prefix letter multiplies the tail's contribution by `2^{m+s}`; hence
if `msum r₁ = msum r₂`,
`W0(pre ++ r₁) − W0(pre ++ r₂) = 2^{mssum pre}·(W0(r₁) − W0(r₂))`.
For two-letter tails with `σ := msum suf`, `V := W0(suf)`:

- **T1** (`r₁ = (m₁,s₁+1)::(m₂,c)::suf`, `r₂ = (m₁,s₁)::(m₂,c+1)::suf`):
  the `V`-terms carry `2^{m₁+s₁+1+m₂+c}` and `2^{m₁+s₁+m₂+c+1}` — equal, they
  cancel; the middle terms give `3^σ2^{m₂}·2^{m₁+s₁}[2(2^c−1) − (2^{c+1}−1)]
  = −3^σ2^{m₂}2^{m₁+s₁}`; the first terms give `3^{m₂+σ}2^{m₁}·2^{s₁}`.
  Total: `2^{m₁+s₁}·3^σ·(3^{m₂} − 2^{m₂})`.
- **T2** (`r₁ = (m₁+1,s₁)::(m₂,s₂)::suf`, `r₂ = (m₁,s₁)::(m₂+1,s₂)::suf`):
  the bracket multiplying `[3^σ2^{m₂}(2^{s₂}−1) + 2^{m₂+s₂}V]` is
  `2^{m₁+1+s₁} − 2^{m₁+s₁+1} = 0`; the first terms give
  `(2^{s₁}−1)2^{m₁}3^{m₂+σ}(2 − 3) = −3^{m₂+σ}2^{m₁}(2^{s₁}−1)`.

With the prefix factor: **exactly the Lean file's T1/T2** — the derivation
agrees with his statements with no discrepancy.

**Verification grids** (all exact integer equality):

- Exhaustive: `pre, suf ∈ {[], [(a,b)] : a,b ∈ {1,2}}`, core letters
  `m₁,s₁,m₂,c ∈ {1,2,3}` — **T1 2,025/2,025, T2 2,025/2,025**.
- Random: 900 draws each, `pre`/`suf` lengths 0–4, entries 1–9 —
  **T1 900/900, T2 900/900** (exceeds his 713/604).
- Bridge `W0 = 2^{m₀}·R₀` between two independent implementations: 400/400.
- `R₀`-frame forms (his REQ-019 statements): T1 707, T2 interior 718, T2
  `i = 0` via rotation reduction 724 — all exact, confirming both his
  `R₀`-frame closed forms and the rotation reduction the Lean frame repairs.
- **Corollary:** `gcd(q, R₀(P), R₀(P′))` divides the letter-scale seam:
  664/664; total isolation (`shared = 1`) in 646/664; **all 79 unit-seam
  cases (`m₂ = 1` for T1, `s₁ = 1` for T2) had shared content exactly 1** —
  the "total isolation at `m = 1`" clause confirmed.

### (d) The gloss adjudication

**What T1/T2 + corollary prove** (confirmed above): for adjacent one-unit
transfers at fixed `q`, the difference of numerators is a unit times a
*letter-scale seam* (`3^{m₂} − 2^{m₂}` resp. `2^{s₁} − 1`), so any divisor of
`q` shared by the two neighbours divides that seam. Consequence: **adjacency
separation of content** — a word at or near `C = 1` shares at most
`log(seam)/log|q|` of content with every transfer-neighbour; there is no
gradual road up a content tower; at `m = 1` the shared content is exactly 1.

**What the gloss says:** "content towers have no shoulders: the only road to
`C = 1` is exact repetition, and repetition is sterile [L-A4]… no *aperiodic*
word reaches `C = 1`."

**Verdict: the gloss does not follow from the lemma — the flag stands.** The
implication fails on two independent counts, and one of them is now a computed
instance, not a hypothesis:

1. **Scope (the `−17` counterexample pattern, computed).** Unscoped, "no
   aperiodic word reaches `C = 1`" is false as a statement about words: the
   `−17` cycle's word `(m,s) = ((4,3),(1,3))` is primitive (aperiodic in his
   sense), has `C = 1` **exactly** (`gcd = |q| = 139`), and — the sharp part —
   is **totally isolated**: its worst shared content over all 6 adjacent
   one-unit-transfer neighbours (both rotations, both directions) is **1**,
   forced by the corollary itself (`gcd(139, 3^3 − 2^3) = gcd(139, 19) = 1`).
   So an aperiodic `C = 1` peak *exists while being perfectly separated from
   its neighbours*: the lemma and the peak's existence co-exist in one
   instance. Adjacency isolation demonstrably does not exclude isolated
   aperiodic peaks. (The instance is untuned — `q = −139 < 0`, `K` one below
   the tuned value — so a corrected gloss can survive with the tuned-regime
   scope; unscoped it has a live counterexample.)
2. **Modality (what the lemma quantifies over).** T1/T2 bound the content
   *shared between neighbours*; they say nothing about the *existence* of
   words with `C = 1`. In the tuned regime, "no aperiodic word reaches
   `C = 1`" restated exactly is "no primitive tuned profile satisfies
   `q | R₀`" — the parked cycle condition itself, which his own NOTE §6 names
   as the residual equidistribution gap and his letter record does not claim.
   The lemma converts "gradual conspiracies" into "isolated conspiracies"; it
   does not remove them.
3. **A third imprecision, minor but real ("the only road… is exact
   repetition"):** repetition is a road to the *limit* `C → 1` for **every**
   base, divisible or not (the exact law in (b2)); and it *reaches* `C = 1` at
   finite height **only from a base already at `C = 1`** (`C(B^j) = 1 ⟺
   C(B) = 1`, by the descent identity — 12 exact checks). So repetition is
   neither the only road toward `C = 1` in the limit sense that would matter,
   nor a road that ever arrives anywhere new — which is, in fact, a *cleaner*
   statement of "repetition is sterile" than the gloss's.

**The exact corrected co-edit language this session's results support**
(replacement for the entry's final two sentences, offered at co-edit;
acceptance is Merle's call):

> So content towers have no shoulders: a word at `C = 1` shares at most
> letter-scale content with every adjacent-transfer neighbour (content `1` at
> `m = 1`), so no word is *connected to* `C = 1` by one-unit transfers; and
> repetition, the one road that climbs (`C(B^j) → 1` for every base, per the
> L-A2 law), reaches `C = 1` at finite height only from a base already at
> `C = 1` — and is sterile [L-A4]. The *existence* of an isolated aperiodic
> `C = 1` peak is untouched: it is exactly the parked condition `q | R₀` —
> NOTE §6's residual gap — and untuned the pattern is realized: the `−17`
> cycle's primitive word has `C = 1` while sharing content `1` with every
> neighbour (its seam `3^3 − 2^3 = 19` is coprime to `139`).

If a shorter form is preferred, the one-sentence version:

> `C = 1` has no shoulders — no aperiodic word is *connected to* `C = 1` by
> one-unit transfers, and repetition arrives only from a cycle [L-A4]; whether
> an *isolated* aperiodic peak exists is exactly the open condition `q | R₀`
> (NOTE §6), untouched here, with the untuned `−17` word showing the isolated
> peak is a real pattern.

## Adjudication summary (one line per entry claim)

| Entry claim | Status |
|---|---|
| 1. Content invariant (`C ∈ [0,1]`, rotation-invariant, `C = 1 ⟺ cycle`; credit framing) | **Confirmed** — 600/600 rotation invariance, 600/600 range + divisibility equivalence; credit split accurate; two precisions recorded: `C` undefined at `|q| = 1` (spent-stock words), and the realized cycle sits on the sign-`q` shore |
| 2. Measured landscape (chance-level aperiodic 0.11–0.50; `B^j` climb per L-A2; one-letter collapse) | **Consistent-at-reduced-scale** — band reproduced at `N = 4,000` (max 0.24–0.38); climb law made *exact* via the descent identity (`gcd` scales by `G_j`), his table reproduced; collapse reproduced (100 perturbations per tower) |
| 3. Separation lemma T1/T2 + corollary (Lean statements) | **Confirmed** — clean-room derivation agrees exactly; 2,025 + 2,025 exhaustive + 900 + 900 random + `R₀`-frame forms + 664/664 corollary + all 79 unit-seam isolations, 0 failures; Lean statements match the entry clause-by-clause |
| 4. The gloss ("only road is repetition… no aperiodic word reaches `C = 1`") | **FLAGGED — does not follow from T1/T2.** The lemma proves adjacency separation, not non-existence; unscoped, the `−17` primitive word is a computed counterexample (`C = 1` exactly, totally isolated, untuned); tuned-scoped, the sentence restates the open cycle condition. Corrected language above. **Our key must not turn on the entry as written.** |
| 5. Artifacts (`e297d9d`, `9932f3f`; kernel-3, 0 sorry, no native_decide; 713/604/560; 300/300) | **Confirmed at statement level, read-not-built** — both commits exist, graph order recorded; file text has no `sorry`/`native_decide`/`axiom`; `#print axioms` output not committed, kernel-3 claim rests on his header; his counts match his committed outputs; no toolchain here, build not attempted |

**Flags, collected:** (i) **The gloss overreach — the round's substance — is
confirmed as a real overreach**, with the `−17` instance upgraded from
"presumably `C = 1`" to computed-exact and extended (total isolation of the
peak); co-edit language above; the key stays unturned until the gloss is
repaired. (ii) `C` is undefined at `|q| = 1` (0/0) — the entry's interval
claim needs the `|q| > 1` domain or a convention; minor co-edit item.
(iii) The kernel-3/axioms claim has no committed `#print axioms` output — flat
observation for the co-edit (an OUT file would close it), not a dispute; the
mathematical content is independently confirmed regardless. (iv) The initial
clone of his Lean repo was served one commit stale; resolved by direct fetch;
recorded only in case it recurs. **No discrepancies of digits, hashes, or
texts anywhere this round. Handbacks: none.**
