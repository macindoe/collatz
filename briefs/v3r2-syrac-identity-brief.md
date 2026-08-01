# Brief: is `aeh.md` 13.6.5's absorption law Tao's `Syrac(Z_3)`? (v3 round 2, gate on the AEH section)

**Why this exists.** `briefs/v3r2-contraction-literature-findings.md` flagged that Tao's Remark 1.13 (*Almost all orbits of the Collatz map attain almost bounded values*, 2019/2022) defines a stationary `3`-adic law `Syrac(Z_3)` for the map `x ↦ (3x+1)/2^a` with weights `2^{-a}`, and computes

```text
Syrac(Z/3^2 Z) = 0, 8/63, 16/63, 0, 11/63, 4/63, 0, 2/63, 22/63     (residues 0..8)
```

Our `aeh.md` Proposition `13.6.5` presents an absorption law with the **same denominator 63**, the **same iteration**, the **same `2^{-a}` weighting**, and `2/63` appearing in both. C1 did not do the computation and flagged it as the single item that should block finalizing the AEH section.

**If these are the same object, a law the paper presents as computed in the project record has a 2019 primary source.** That is a citation-integrity question, not a correctness question — the computation may be perfectly right and still need attribution.

**This is a computation and comparison task.** Produce a verdict; change nothing.

## What is already checked, so you don't repeat it

I did a partial check by hand. Take it as a starting point to confirm or overturn, not as established:

- **Support matches.** Tao's law vanishes at residues `0, 3, 6` — supported off multiples of `3`. `aeh.md` L125 says our `ν` is "supported off the dead-door class (`ν(y ≡ 0 mod 3) = 0`, every door being live)". Same structural feature.
- **Mod-3 marginals are exactly swapped.** Tao: `P(≡1 mod 3) = 21/63 = 1/3`, `P(≡2 mod 3) = 42/63 = 2/3`. Ours (`13.6.5`, `ν_1`): `(2/3, 1/3)` on `(1,2) mod 3`. A sign convention (`x = −y`, or `z = y+1`) would explain this; **verify rather than assume**.
- **Mod-9 does not line up under the obvious dictionaries.** Our `P(a ≥ 2) = 2/63` means `P(y ≡ 8 mod 9) = 2/63`. Tao's value at residue `8` is `22/63`; his `2/63` sits at residue `7`. Negation `r ↦ 9−r` sends our `8` to `1`, where Tao has `8/63`. So no naive identification works. Either there is a subtler coordinate dictionary, or these are genuinely different objects that share a denominator because they share an iteration.
- Tao's nine values sum to `1`. Confirmed.

## The task

1. **Get Tao's Remark 1.13 from the primary source** (arXiv:1909.03562). State his definition of `Syrac(Z_3)` exactly — what the random variable is, what it is a limit of, and what the `2^{-a}` weights are attached to. Do not work from C1's summary or from mine.
2. **State `13.6.5`'s object exactly.** `aeh.md` L118–128: `a` is the law of `v_3(y_3 + 1)` where `y_3` is the `3`-adic past-limit of `itinerary.md` `14.15.3.3`, with `ν_j` the exact image of `B^{⊗j}` under the offset formula. Establish precisely what `y_3` is and in which direction it is a limit — **the past-limit versus a forward-orbit limit is the crux.** Tao's is a forward object.
3. **Compute both to mod `3^2` and, if they survive that, mod `3^3`**, in exact rationals, from the definitions. Show the computation.
4. **Adjudicate.** One of: (a) same law, different coordinates — give the dictionary; (b) different laws sharing structure — say precisely what is shared and why (both are stationary laws of a `3`-adic map driven by geometric-`1/2` exponents, which would explain a common `63 = 3^2·7` denominator without identity); (c) could not settle — say what is missing.
5. **Say what follows for the record.** If (a): `13.6.5` and the paper's Section 5 need a citation and an attribution sentence — draft them. If (b): the resemblance is worth a one-line remark distinguishing the two objects, since any referee who knows Tao's paper will ask — draft that. If (c): state exactly what a further check would need.

Check also whether `13.6.3`(v)'s Bernoulli construction, `13.6.1`'s letter law, or `13.6.2`'s identification have counterparts in Tao §1.3 / his Syracuse random variables. The absorption law is the flagged item, but it is not obviously the only candidate.

## Deliverable

Write **only** `briefs/v3r2-syrac-identity-findings.md`. Include the exact statement of Tao's definition with its source, both computations in full, the verdict with its dictionary or its distinguishing argument, and drop-in text for whichever of (a)/(b) applies.

Mark clearly what is verified from a primary source versus inferred. If you cannot obtain Remark 1.13's text, say so and stop rather than reconstructing it — a reconstructed definition would make the whole comparison worthless.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations of any kind.
- Write with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Exact rational arithmetic. No floating point in any pass/fail comparison. If you use a script, keep it in the scratchpad — do not add it to `experiments/`.
