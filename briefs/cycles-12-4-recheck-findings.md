# Findings: cycles.md 12.4's `m`-cycle translation re-derived

Brief: `briefs/cycles-12-4-recheck-brief.md`. Branch `cycles-12-4-recheck`, base `6bb473a` (= `main` at the brief's commit). Verdict: **the undercount is confirmed.** Simons–de Weger's `m` is the record's `p` exactly, and 12.4 has been rewritten in place (its own commit).

## 1. The derivation, by hand

**SdW's `m`, from their text** (v1.44, 2010, pp. 1–2; the same definitions as Acta Arith. 117 (2005) p. 51). The map is the Terras map: "`T(n) = ½(3n+1)` if `n` is odd, `T(n) = ½n` if `n` is even". "We call a cycle an `m`-cycle if the numbers in it appear in `m` sequences, each consisting of an increasing subsequence of odd numbers, followed by a decreasing subsequence of even numbers." §1.2: there are `m` local minima at indices `t_i` and `m` local maxima at `s_i`; `k_i = s_i − t_i`, `ℓ_i = t_(i+1) − s_i`; `K = Σk_i` (the odd terms), `L = Σℓ_i` (the even terms). "The cycle `{1, 2}` is a 1-cycle."

**A reduced block in raw runs** (spine.md 5.4–5.5, and the BlockEntry coordinates). The entry is an odd `x = 2^m u − 1`, with `u` odd and `m = v_2(x+1) ≥ 1`. Each Terras odd step sends `2^j 3^i u − 1` to `2^(j−1) 3^(i+1) u − 1`, so the `m` values `x, …, 2·3^(m−1)u − 1` are odd and the next value, `3^m u − 1 = A`, is even. Then there are `s = v_2(A) ≥ 1` halvings down to the odd exit `A/2^s`, which is the next entry. So a block is exactly the Terras word `1^m 0^s` with `m, s ≥ 1`.

**`p` against SdW's `m`.** A reduced cycle of period `p` is a cyclic Terras word `1^(m_0) 0^(s_0) ⋯ 1^(m_(p−1)) 0^(s_(p−1))` with every exponent `≥ 1`. It therefore has exactly `p` maximal odd runs, and each one is an "increasing odd subsequence followed by a decreasing even subsequence": the odd steps raise the value and the halvings lower it. Each block entry `x` has predecessor `2x` and successor `(3x+1)/2`, both larger, so it is a local minimum. Each top `3^m u − 1` is a local maximum, and there are no others. So SdW's `k_i = m_t`, `ℓ_i = s_t`, `K_SdW = n`, `K_SdW + L = K`, and **`m = p`**. The case `m_t = 1` is no exception: the entry `x ≡ 1 (mod 4)` still satisfies `2x > x < (3x+1)/2`. It looks like a "pure fall" only in the odd-to-odd sequence, and SdW do not count there.

**What `#{t : m_t ≥ 2}` counts.** It equals `p − #{t : m_t = 1}`, the number of block entries `≡ 3 (mod 4)`. It differs from `p` exactly when some block entry is `≡ 1 (mod 4)`. That happens already at SdW's own trivial 1-cycle `{1, 2}`, the fixed point `(1, 1)` with `m_0 = 1`, where the formula gives `0`. It also happens on the `p = 7` staircase (`m_6 = 1`): formula `6`, `p = 7`. Nothing forces a nontrivial cycle to avoid depth-1 entries, so the formula is a genuine undercount, not a harmless relabelling.

**Consequence for 12.4's transfer.** If SdW (or Hercher) exclude `m ≤ M₀`, the implication is "no reduced cycle with `p ≤ M₀`", so every cycle has more than `M₀` blocks. The old clause "no reduced cycle has `#{t : m_t ≥ 2} ≤ M₀`" is strictly stronger and is not implied. A cycle with `p > M₀` blocks of which `≤ M₀` are deep is not excluded by any `m`-cycle theorem. The same goes for "more than `M₀` deep-entry blocks". The clause is **unsupported**, not refuted: no counterexample is known, and none can be expected while no nontrivial cycle is known.

The refresh's claim (`briefs/ceiling-novelty-refresh-findings.md` §4.3) is confirmed on every point it makes.

## 2. The check

`experiments/cycles_12_4_recheck.py` is fresh code. It imports nothing from `experiments/`; `ceiling_novelty_check.py` was read and not reused. It uses exact `Fraction` arithmetic and is seeded. One command reproduces the committed output:

```text
python experiments/cycles_12_4_recheck.py > experiments/cycles_12_4_recheck_output.txt
```

For each profile the script:
- composes the word's Terras branches and takes the rational fixed point;
- iterates the Terras map with parity read off the orbit itself (2-adic parity of an odd-denominator rational), and checks closure and that the parity vector equals the block word;
- checks the spine decomposition at every block: `m_t = v_2(x+1)`, `s_t = v_2(3^(m_t)u − 1)`, and that the exit equals the next entry;
- counts SdW's `m` on the raw orbit as strict local minima by value (positive shore) and as maximal odd runs (all draws), and checks that the minima, or on the negative shore the value maxima, sit exactly at the block entries.

| case | `p` | odd runs | SdW `m` (minima) | 12.4 formula |
|---|---|---|---|---|
| trivial `{1, 2}` | 1 | 1 | 1 | **0** |
| staircase `p = 7` (`m = (4,7,9,15,23,35,1)`, `n = 94`, `K = 149`) | 7 | 7 | 7 | **6** |
| `−5`, traced from the integer (`m = (2)`, `s = (1)`) | 1 | 1 | (neg. shore) | 1 |
| `−17`, traced (`m = (4,3)`, `s = (1,3)`) | 2 | 2 | (neg. shore) | 2 |
| `−1` | — | — | — | outside the block coding (word `1`, no even term) |
| random, `p = 2..20`, 60 per `p` | `p` | `p` on 1,140/1,140 | `p` on 665/665 positive-shore | `< p` on 961, `= p` on 179 |

Totals: **47,498 checks, 0 failures; ALL CHECKS PASS** (2026-10-19). Inside the random draws the formula falls short of `p` by up to `9`, and it falls below `p` exactly when some `m_t = 1`, which is itself checked on every draw. The negative controls have no depth-1 block, so the formula agrees with `p` there; they test the run count, not the gap. The output's last column, local minima of the odd-only subsequence, is informational only and is not claimed as a law.

## 3. Verdict and affected sentences

**12.4's translation is wrong**, and it has been rewritten on this branch (commit `479b3aa`). Only the statement and its consequence changed: the dictionary is now `m = p`, the "pure fall" sentence is restricted to the odd-to-odd frame, the consequence reads "more than `M₀` blocks", and a line says the exclusion carries no information about deep-entry counts. A one-line verification record was added and front matter `updated` is now 2026-10-19. Status is unchanged.

The other sentences that use 12.4's translation, from a grep for `12.4`, `M₀`/`M_0`, `deep-entry`, `m-cycle`, `local minim` and `Hercher` across tracked pages, `TOUR.md`, `publication.md`, `HANDOFF.md` and `paper/collatz-reduced-v3.tex`. None was edited.

- **cycles.md 12.7.3** — "By the translation of `12.4`, all `p <= 68` remain subsumed by Simons–de Weger". **Stands**, and is now exact. Separately, it is stale on the number: Hercher's record makes it `p ≤ 91`, and the same paragraph already cites Hercher. That is the main session's call and not part of this correction.
- **cycles.md 12.5.3** (the SdW dictionary "their `K` is our `n`, their `K+L` is our `K`") — **stands**. It agrees with `k_i = m_t`, `ℓ_i = s_t`.
- **cycles.md 12.2.3** ("a single block … a circuit") — **stands**. A one-block cycle is SdW's 1-cycle under `m = p`.
- **publication.md line 14** — "Our crossover threshold `p > 91` was correctly calibrated. (12.4, …)". **Stands**, and is now exact rather than a sufficient bound. Under the old formula some `p > 91` cycles would already have been excluded.
- **open-problems.md line 177** (the same calibration note) — **stands**.
- **TOUR.md line 36** (dictionary row pointing to 12.4) — **stands**. It names no formula.
- **index.md line 36** ("m-cycle translation (12.4)") — **stands**.
- **`briefs/ceiling-novelty-refresh-findings.md` §4.3, §5 proposals** — confirmed. Its proposal "12.4's `m = p` correction and the struck deep-entry clause" is now done on this branch.
- **paper/collatz-reduced-v3.tex** — it never states the `#{t : m_t ≥ 2}` formula or the deep-entry clause (grep: no `m_t \ge 2`, no "local minim", no "deep"). Its only use is `thm:smallp`, line 200: "no nontrivial cycles of 1, 2, or 3 blocks … contained in the classical results \cite{steiner,sdw,hercher}". **Stands** under either dictionary. v3 is therefore not wrong on this point, but it never states the identification v4 will rely on.
- No other tracked page repeats the deep-entry consequence. `reverse.md` and `HANDOFF.md` matched on unrelated text only: "deep entry depth" and the Hercher citations.

## 4. What paper 1 v4 must say

1. **The dictionary, stated once and correctly:** a `p`-block cycle of `F` is an `m`-cycle of Simons–de Weger with **`m = p`**. Each block is one local minimum of the Terras orbit, with `k_i = m_t`, `ℓ_i = s_t`, SdW's `K = n` and `K + L = K`, and depth-1 blocks included.
2. **The transfer, in its correct strength:** Hercher's `m ≤ 91` excludes every nontrivial `F`-cycle with `p ≤ 91` blocks, so `thm:smallp`'s `p ≤ 3` is a small special case. It must not claim, or imply, any bound on the number of deep-entry (`m_t ≥ 2`) blocks.
3. **The parameter for attribution:** SdW Lemma 7's `m` is v4's `p` exactly. The uniform trim (Thm 4.5) is therefore their Lemma 7 in the same parameter, as the refresh found, and not a statement "in a stronger parameter".

## 5. Commits on the branch

- `448e1dc` — `experiments/cycles_12_4_recheck.py` + output.
- `479b3aa` — cycles.md 12.4 rewrite (content, its own commit).
- this findings file (the encoding scan was run before it).

Source held: SdW v1.44 PDF, downloaded to the session scratchpad and not committed. Nothing outward was done.
