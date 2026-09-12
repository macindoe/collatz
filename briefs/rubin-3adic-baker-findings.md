# Findings: the 3-adic Baker cap on the mirror side (Rubin correspondence, 2026-09-05)

Brief: `briefs/rubin-3adic-baker-brief.md`. Branch **`rubin-3adic-baker`**.

**Base SHA.** The worktree was cut from `7232912` (pre-brief HEAD) and lacked
`briefs/rubin-3adic-baker-brief.md`. `git merge main` fast-forwarded to
**`36a8cf1`** ("briefs/rubin-3adic-baker-brief.md: delegation brief..."),
local `main`'s tip at session start, which does carry the brief. Branch
`rubin-3adic-baker` was cut from `36a8cf1`.

Register: flat, calibrated prose. Every number below either comes from
`experiments/mirror_baker_cap.py`'s committed output or is a hand computation
reproduced in this file; nothing is labeled proved without that script's
independent check.

---

## 1. Provenance (paraphrased; no verbatim letter, no address)

Per the brief: on 2026-09-05 Brett Rubin, an independent worker on the
problem since 2022, wrote to the author after reading paper 1 at v3. Point 3
of his letter, paraphrased: for fixed `e`, a small `k` can carry a deep
valuation whenever his reparametrized anchor `D` opens with a run of zero
digits, so "the analogue of Theorem 3.3's unconditional clause has to bound
the constant rather than the growth" — he named this a real gap and said he
does not hold the Yu / Bugeaud–Laurent references. The main session's
2026-09-05 pre-check already identified his law as Theorem 14.2.4 exactly
(under `s = (e mod 3) + 2k`, `D` an affine reparametrization of `M₃`) and his
`e = 1` degeneration as Lemma 14.2.1 / Proposition 14.2.3. This session's job
is Point 3's gap: a cap on `d` as a function of `s`, transplanting
stage1-synthesis.md 11.8.3.11.

Credit clause used throughout: "flagged by Brett Rubin (correspondence
2026-09-05)". No verbatim quotation of his letter and no email address appear
in any tracked file (checked by re-reading every edit before committing).

---

## 2. The derivation, written out (Queue 1)

Start from Theorem 14.2.4: for a door `y` (odd, `3∤y`) and `s` of the
admissible parity (14.1.1: `s` odd if `y ≡ 1 (mod 3)`, `s` even if
`y ≡ 2 (mod 3)`),

```text
d = v₃(2^s y + 1) = 1 + v₃(s − M₃(y)).
```

**Step 1 (squaring reduction).** By 14.2.4's own proof, `v₃(2^s y + 1) ≥ 1`
whenever `s` has the admissible parity, and since `(2^s y + 1) − (2^s y − 1)
= 2` is a 3-adic unit, `v₃(2^s y − 1) = 0` always. Hence

```text
d = v₃(2^s y + 1) = v₃(2^s y + 1) + v₃(2^s y − 1) = v₃((2^s y + 1)(2^s y − 1))
  = v₃(4^s y² − 1).
```

Multiplying by the unit `y²` (`3∤y`) does not change the valuation, so with
`α₁ = 4, b₁ = s, α₂ = y^(−2), b₂ = 1`:

```text
d = v₃(4^s y² − 1) = v₃(y² (α₁^b₁ − α₂^b₂)) = v₃(α₁^b₁ − α₂^b₂) = v₃(Λ).
```

This is the step the 2-adic pin did not need in this form: on the forward
side, the anchor `N(ω)` is *defined* by `9^n ≡ ω^(−1)`, so `9` and `ω^(−1)`
already sit as two independent bases with `ω^(−1)` raised to the fixed
exponent `1` — no squaring is needed to produce that shape. On the backward
side the raw quantity `2^s y + 1` has `y` appearing linearly, not
exponentiated, so there is no second base-to-a-power term to read off
directly; squaring converts `y` (linear) into `y²` (a fixed base to the fixed
exponent `1`), at the cost of also converting `2^s y + 1` into `4^s y² − 1`,
which is why the valuation identity above needs the intermediate unit fact
`v₃(2^s y − 1) = 0` to go through. This is exactly the step the brief
anticipated.

**Step 2 (principal units, `D = 1`, `g = 1`).** `α₁ = 4 ≡ 1 (mod 3)` and
`α₂ = y^(−2) ≡ 1 (mod 3)` (`y² ≡ 1 (mod 3)` by Fermat, since `3∤y`): both are
already principal units mod `3`, so the least `g` with `α₁^g ≡ α₂^g ≡ 1
(mod 3)` is `g = 1` — automatic, exactly mirroring 11.8.3.11's "`9 ≡ 1
(mod 8)`, `g = 1`" at `p = 2`. Both `α₁, α₂` are rational, so
`D = [Q(α₁,α₂):Q] = 1`, matching 11.8.3.11's `D = 1`.

**Step 3 (multiplicative independence, and the excluded case).** `α₁ = 2²`
carries only the prime `2` in its factorization; `α₂ = y^(−2)`, for
`|y| ≥ 5` (odd, coprime to `6`), carries none of it. So `α₁^a = α₂^b` (for
integers `a, b`) forces `4^a` and `y^(−2b)` to agree prime-by-prime, hence
`a = 0` and (since `|y| ≥ 5`) `b = 0`. `α₁, α₂` are multiplicatively
independent **exactly when `|y| ≠ 1`**: at `y = ±1`, `α₂ = 1`, and `1` is
multiplicatively dependent with everything (`α₁^0 = α₂^b` for every `b`).

This is the second step the brief anticipated, and it is a genuine, not a
cosmetic, difference from the forward side. On the forward side,
11.8.3.11's own sentence — "multiplicatively independent whenever `3∤ω`,
which holds for every valid odd core by definition" — does not explicitly
exclude `ω = 1`, even though `α₂ = ω^(−1) = 1` at `ω = 1` is exactly as
degenerate as `y = ±1` here (see §6, "for the author's reply", for why this
is worth a quiet look but is not something this session edited). On the
backward side there are *two* excluded points, not one, because the relevant
algebraic quantity is `y²` (invariant under `y ↦ −y`), and because reverse.md
extends the underlying arithmetic identity beyond the literal (always
positive) doors of 14.1.1 to match Rubin's own sign-unrestricted `e`. In the
literal tree of 14.1.1, doors are always positive (`y_a = 2^(D−a)3^aΩ − 1 ≥
1`), so only `y = 1` is ever realized as an actual door; `y = −1` completes
the arithmetic identity's degenerate locus and matters for Rubin's own
`e`-indexed law and, later, for itinerary.md's signed extension (14.15.6.1
already excludes `y = −1` there, for the unrelated dynamical reason that `−1`
is `T`'s fixed point).

**Step 4 (the excluded case itself).** At `y = ±1`, Lemma 14.2.1 (`v₃(2^t−1)
= 1+v₃(t)` for even `t`) settles the law exactly, without any Baker input:

- `y = 1`, `s` odd: `2^s + 1 = 2^s + 1^s`; LTE for `p = 3` odd exponent gives
  `v₃(2^s + 1^s) = v₃(2+1) + v₃(s) = 1 + v₃(s)`.
- `y = −1`, `s` even: `2^s·(−1) + 1 = 1 − 2^s = −(2^s − 1)`, and Lemma 14.2.1
  gives `v₃(2^s−1) = 1+v₃(s)` directly.

So `d = 1 + v₃(s)` at both `y = 1` and `y = −1` — matching `M₃(1)`, `M₃(−1)`
being the two elements of `E₃` with vanishing `Z₃`-component (`M₃(−1) = 0`
exactly, since `2^0 = 1 = −1/(−1)`; `M₃(1)`'s `Z₃`-part is `0` too, by
Proposition 14.2.3's own computation, mod `2·3^(k−1)` the value `3^(k−1)`,
which is `0` in the `Z₃`-component and `1` (odd) in the `Z/2`-component).
This is Rubin's `e = 1` degeneration, his `D = −1/2`. It is *sharper* than
the general cap, not just an exception to it: `d = 1+v₃(s) ≤ 1 + log₃ s`,
linear in `log s`, the same phenomenon as cycles.md 12.6.1.3(b)'s rational
anchor point (`ω = 1` there, elementary and logarithmic against the general
`(log n)²` Baker ceiling).

---

## 3. The source statement, verbatim, and the specialization (Queue 2)

**What was obtainable.** ScienceDirect's copy of the primary source (Y.
Bugeaud, M. Laurent, *Minoration effective de la distance p-adique entre
puissances de nombres algébriques*, J. Number Theory 61 (1996), 311–342) is
behind a Cloudflare challenge that blocks both `WebFetch` and a direct
`curl` with a browser user-agent (HTTP 403, "Cf-Mitigated: challenge") — it
was not the open archive the brief expected. An arXiv note improving the
same paper (T. Yamada, *A note on the paper by Bugeaud and Laurent...*,
arXiv:math/0607072) was obtained in full but restates only the authors'
Lemme 10/11 and Théorème 1, not Corollaire 2, so it does not supply the
needed statement.

**What was used instead.** M. A. Bennett, Y. Bugeaud, *Effective results
for restricted rational approximation to quadratic irrationals* (2011),
obtained in full (`personal.math.ubc.ca/~bennett/BeBu.pdf`). Yann Bugeaud —
one of the two 1996 authors — restates the needed bound there as their own
Theorem 2.1, introduced as "a slightly simplified proof of Théorème 3 of
[Bugeaud–Laurent 1996]" (their reference [10], the exact J. Number Theory 61
(1996), 311–342 paper). Quoted verbatim (their notation; `Q̄_p` an algebraic
closure of `Q_p`, `ν_p` its valuation normalized `ν_p(p)=1`):

> Let `p` be a prime number and denote by `Q̄_p` an algebraic closure of the
> `p`-adic field `Q_p`. We equip the field `Q̄_p` with the ultrametric
> absolute value `|x|_p = p^(−ν_p(x))`... Let `α₁` and `α₂` be algebraic over
> `Q` and regard them as elements of the field `Q̄_p`. Write
> `D = [Q(α₁,α₂):Q]`. Our goal is to deduce a lower bound for the
> ultrametric absolute value of `Λ = α₁^b₁ − α₂^b₂`, where `b₁` and `b₂` are
> arbitrary positive rational integers.
>
> We assume that `ν_p(α₁) = ν_p(α₂) = 0` and denote by `g` the smallest
> positive integer such that `ν_p(α₁^g − 1) > 0` and `ν_p(α₂^g − 1) > 0`. It
> is easily seen that `g ≤ p^D − 1`. Let `A₁ > 1, A₂ > 1` be real numbers
> such that `log A_i ≥ max{h(α_i), (log p)/D}` for `i = 1` and `2`, where `h`
> denotes the logarithmic Weil height. Set `b' = b₁/(D log A₂) + b₂/(D log
> A₁)`.
>
> **Theorem 2.1.** With the above notation, if the algebraic numbers `α₁`
> and `α₂` are multiplicatively independent, then `ν_p(Λ)` is bounded above
> by
>
> `[24pg / ((p−1)(log p)^4)] D^4 (max{log b' + log log p + 0.4, (10 log
> p)/D, 10})^2 log A₁ log A₂.`

**Naming caveat (for the author).** Bennett–Bugeaud cite this as their
"slightly simplified proof of Théorème 3" of the 1996 paper, not as "their
Corollaire 2" — the name stage1-synthesis.md 11.8.3.11 uses. This session
did not obtain the 1996 French text itself to confirm the numbering matches
name-for-name; the identification rests entirely on the content and the
numerical control below, not on the label. See §6.

*Closed at review (2026-09-13).* The author supplied Corollaire 2 from the
1996 text: "Avec les hypothèses et notations du Théorème 3, supposons de
plus que α₁ et α₂ appartiennent à U_v^1. Alors v(Λ) ≤ 24p/((p−1)(log p)^4)
D^4 (max{log b' + log log p + 0.4, 10 log p / D, 10})^2 log A₁ log A₂ ≤
208 D^4 (max{…})^2 log A₁ log A₂." So Corollaire 2 is exactly the `g = 1`
case of Théorème 3 that both pins use; 11.8.3.11's label was right, the
Bennett–Bugeaud restatement is Théorème 3 in general `g`, and the two
agree at `g = 1`. The second inequality is the source of 11.8.3.11's
`208`: the paper's own uniform constant, `24p/((p−1)(log p)^4) ≤ 208` for
every prime `p`, attained at `p = 2` (`207.94…`). No label changes anywhere.

**The `p = 2` control (required before trusting the `p = 3` reading).**
Specializing Theorem 2.1 at `p = 2, D = 1, g = 1` (`9 ≡ 1 (mod 8)`),
`A₁ = 9, A₂ = ω, b₁ = n, b₂ = 1` — 11.8.3.11's own setup — gives:

```text
prefactor: 24·2·1 / ((2−1)·log(2)^4) · 1^4 = 207.940648...   (11.8.3.11 quotes "208")
```

and, at `ω = 5`:

| `n` | this formula | 11.8.3.11's published value | rel. error |
|---|---|---|---|
| `34,000` | `73,534.0` | `~73,555` | `0.029%` |
| `10^6` | `131,508.3` | `~131,500` | `0.006%` |
| `10^9` | `302,455.3` | `~302,500` | `0.015%` |

The residual `~0.03%` is fully explained by 11.8.3.11's own rounding of
`207.94...` to the displayed `208` (`208/207.9406 = 1.000285`, matching the
`34,000`-row error to three figures). **The control reproduces
11.8.3.11's constant.** Verified: `experiments/mirror_baker_cap.py` PART G.

**The `p = 3` specialization.** `D = 1, g = 1` (Step 2 above), `A₁ = 4`
(`log A₁ = log 4 ≥ max{log 4, log 3}`, the height requirement met with
equality), `A₂ = y²` (`log A₂ = 2 log|y| ≥ max{2log|y|, log 3}`, true for
every admissible `|y| ≥ 5`), `b₁ = s, b₂ = 1`, `b' = s/(2 log|y|) + 1/log 4`:

```text
d = v₃(4^s y² − 1)
   <= [36/(log 3)^4] · log 4 · log(y²) · (max{log b' + log(log 3) + 0.4, 10 log 3, 10})^2.
```

Collecting the `y`-dependence into a single coefficient of `(log s)²` (as
11.8.3.11 collects `208 log9 logω` into `C(ω)`):

```text
C₃(y) := 144 · log 2 · log|y| / (log 3)^4  ≈  68.5189 · log|y|.
```

`d ≤ C₃(y)·(log s)²` for `s ≥ 1` of the admissible parity, `|y| ≠ 1` — up to
the floor, exactly as 11.8.3.11's own `C(ω)` statement is qualified (see
§6). This is Corollary 14.2.5.1; Corollary 14.2.5.2 is the digit-match
reading via `d = 1+v₃(s−M₃(y))`.

---

## 4. Rubin's point about the constant, verified (Queue 3)

His two named instances, checked by direct integer computation
(`experiments/mirror_baker_cap.py` PART D):

- `e = 5, k = 1`: `s = (5 mod 3) + 2·1 = 4`; `2^4·5+1 = 81 = 3^4`, so `d = 4`.
- `e = 41, k = 13`: `s = (41 mod 3) + 26 = 28`; `2^28·41+1 = 11,005,853,697
  = 3^6 · 15,097,193` (the cofactor `≡ 2 (mod 3)`, confirming `v₃ = 6`
  exactly).

Both reproduce exactly. His `D`'s two named runs of zero digits (his own
symbol; not entered into the wiki's registry — see §5) are the mechanism:
`D` opens with two zero base-`3` digits at `e = 5` before the digit that
delivers `d = 4` at `k = 1`, and with a longer such run at `e = 41` before
the digit delivering `d = 6` at `k = 13`.

**Texture, against the cap** (PART F, `S = 4,000`, fresh integer scan):

| `y` | max `d(y,s)` for `s ≤ 4000` | at `s` | cap at `S = 4000` |
|---|---|---|---|
| `5` | `7` | `1192` | `13,309.9` |
| `7` | `8` | `335` | `16,092.4` |
| `11` | `10` | `2876` | `19,830.3` |
| `13` | `8` | `3799` | `21,211.8` |
| `41` | `8` | `2458` | `30,710.8` |
| `−5` | `8` | `1921` | `13,309.9` |
| `−7` | `8` | `2522` | `16,092.4` |

Rubin's own two instances against the cap **at their own `s`** (not `S =
4000`): `e=5,k=1` (`s=4`): observed `d=4`, cap `13,309.9`; `e=41,k=13`
(`s=28`): observed `d=6`, cap `30,710.8`. The cap is nowhere near binding at
either — stated flatly, per the brief: it excludes nothing, and bounds how
long a run of vanishing digits can last, not how often one occurs.

**Sanity-check narrative for `y = 5`** (PART F, mirroring 11.8.3.11's own
numeric paragraph): the bound is `~13,310` for `s` up to `~116,000`
(dominated by the floor `10 log 3 ≈ 10.986` inside the `max`), then grows as
`(log s)²` beyond that — `~19,042` at `s = 10^6`, `~44,324` at `s = 10^9` —
large but finite and slow-growing, the same qualitative picture as
11.8.3.11's.

---

## 5. Registry check (Queue 5, `symbols.md`)

`symbols.md`'s existing `D` collision index (frame 4, "Door / itinerary
frame") already carries three meanings: state depth in `state(y)=(Ω,D)`
(14.14.1), the unreduced fixed-point denominator (itinerary.md 14.15.9.1),
and the AEH window cap `W_{k,D}` (aeh.md 13.2). Rubin's own `D` (his affine
reparametrization of `M₃`, `e·2^((e mod 3)+2D) = −1`) is a **fourth**, purely
personal notation — checked, and **not added** to the registry, per the
brief: it is his name for an object the wiki already has a name for
(`M₃`, via the affine identity `s − M₃(e) = 2(k−D)` the main session's
pre-check already established). `C₃` was checked for collisions across the
whole tree (`grep`) and found unused before this session — no collision-index
entry was needed for it, only the new row alongside `C(ω)`.

---

## 6. For the author's reply

The drafted sentence "It transplants directly" needs three corrections, all
recorded above and all in reverse.md 14.2.5 itself, not silently smoothed
over:

1. **The squaring step is not free.** The 2-adic anchor's defining
   congruence (`9^n ≡ ω^(−1)`) hands Baker's theorem its two-logarithm shape
   for free; the backward law's `2^s y + 1` does not, because `y` appears
   linearly, not as a base-to-a-power. Converting it costs one extra
   valuation fact (`v₃(2^s y − 1) = 0`, itself a one-line consequence of
   14.2.4) and one squaring, which is why the mirror's statement reads
   `4^s y² − 1` rather than a direct analogue of `9^n ω − 1`.

2. **The excluded case is two points, not the forward side's (unstated)
   one.** `y = ±1` both degenerate (`y² = 1` either way), against the
   forward side's single `ω = 1`. Worth a quiet look on the forward page at
   some point: 11.8.3.11's own sentence "multiplicatively independent
   whenever `3∤ω`, which holds for every valid odd core by definition" does
   not itself flag `ω = 1` as an exception, even though `α₂ = ω^(−1) = 1`
   there is exactly as degenerate as `y = ±1` is here (`1` is
   multiplicatively dependent with everything). This session did **not**
   edit stage1-synthesis.md's math to add that caveat — out of scope for
   this brief, and the numbers there are unaffected (`ω = 1`'s law is
   already handled elsewhere and correctly, via the elementary reading at
   cycles.md 12.6.1.3(b)) — but the author may want it named explicitly
   there too, for the same reason Rubin's letter asked for the mirror's own
   version of this cap.

3. **The constant is pinned, but the source citation carries a naming
   gap.** The general-`p` statement used here (§3) is quoted verbatim from
   Bennett & Bugeaud (2011) Theorem 2.1, which they present as derived from
   "Théorème 3" of the 1996 Bugeaud–Laurent paper — not literally "their
   Corollaire 2", the name stage1-synthesis.md 11.8.3.11 uses. This session
   could not reach the 1996 French text itself (ScienceDirect's copy is
   behind a Cloudflare challenge; the brief's assumption of an "open
   archive" did not hold in practice). The identification of Theorem 2.1
   with 11.8.3.11's cited "Corollaire 2" rests on content and on the `p = 2`
   control reproducing 11.8.3.11's own pinned `208` constant and its three
   worked numeric values to `< 0.03%` (§3) — strong evidence they are the
   same result under two different exposition's numbering, but not a
   confirmed name-for-name match against the original. If the author (or a
   future session) obtains the 1996 paper directly, this is the one thing
   worth a two-minute check.

---

## 7. Compliance

`python experiments/encoding_scan.py` — see the top-level session report for
the exact `RESULT:` line (run once, immediately before the final commit, per
the brief).
