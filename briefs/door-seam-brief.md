# Brief: the door/exit seam — a door-centred Bridge identity and the exit map (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and stopping rules), `AGENTS.md` (binding house norms), `bridge.md` §16 (the open object and the core-extraction deficit — the thing this brief probes), `reverse.md` §14.1–14.2, 14.6.5.1, 14.8, 14.13 (doors, the 3-adic anchor `M₃`, the top-door increment law and its mortality freeze, the affine-collapse obstruction), stage2.md 11.8.5.6 (the orbit anchor `M(ω) = N(ω²)` and the increment identity `ΔM = N((ω₊/ω)²)`), stage4.md 11.8.7.2–11.8.7.3 (digit-determinacy lemmas, low-order `ΔM` law).

## Provenance and pre-check

This brief packages an external suggestion (ChatGPT, 2026-07-14), assessed by the main session against the live pages before delegation. All three core claims below were checked with fresh throwaway code (seed 12345, 2026-07-14): the door-centred identity (2,400 checks over `k ∈ {1,3,6}`, zero failures), the exit map's fiber-constancy (2,000 random states, all doors, zero failures), and the fixed-stratum contraction law (~30,000 pairs, zero failures). So the targets are true; your job is to *prove* them at house standard, place them correctly in the wiki, and then answer the one genuinely open question (item 5), which the pre-check did not touch. Your verification code must be your own fresh implementation, per AGENTS.md — the pre-check script is deliberately not provided.

## The state you are starting from

The Bridge (`bridge.md` §16) is the program's terminal open object: the anchor increment `ΔM = M(ω₊) − M(ω)` at unbounded depth. The core-extraction deficit (16.2) explains why no bounded window closes it: every step, in either direction, strips a power of the anchor's own prime and pays exactly that many anchor digits. The reverse front's 14.13 records the concrete form of this backward: a residue mod `3^k` propagates to the child only mod `3^(k−d)` because the collapse map is affine, not multiplicative.

The suggestion's observation: both the forward exit transform and the target's reduction share a single intermediate integer — the exit (equivalently, live door) `y`. For one reduced edge `(ω,d) → (Ω,D)` with exit `y` and exit valuation `s`:

```text
3^d ω = 1 + 2^s y          (exit equation, = 14.12.3's identity)
y + 1 = 2^m 3^a Ω,   m = v₂(y+1),  a = v₃(y+1),  D = m + a
```

(the second line is exactly reverse.md 14.6.5.1's recovery formula; note `C = 3^d ω − 1 + 2^s = 2^s (y+1)`, so `m = m₊` and `a = a₊` in stage4's notation — the two transforms are already in the repo, but no live page treats `y` as the central coordinate). Both `ΔM` and the reverse machinery can be re-expressed *around* `y`, and on `y` the dynamics may be better-behaved than on the extracted cores, because staying in door coordinates never divides by a power of 3 — and division by powers of 2 is a 3-adic unit operation, costing no 3-adic digits.

## Task

Prove and place the door-centred formulation, then test whether the exit-coordinate seam carries a total graded anchor law that the core coordinates provably cannot. Compact theorem targets; either a new coordinate map or a clean failure.

## Queue, in order

1. **Global edge parameterization.** State and prove: every reduced edge is parameterized by its live door `y` and admissible `s`, via the two displayed equations above, with the dictionary to stage4's `(C, σ, a₊)` made explicit (`C = 2^s(y+1)`, `σ = s + m`, `a₊ = a`). Mostly bookkeeping over 14.1.1/14.6.5.1 — but it is the load-bearing definition for everything below, so state it once, cleanly.

2. **The door-centred Bridge identity.** Define, for odd `n`, `J(n) := M(n / 3^(v₃(n))) = M(n) + v₃(n)` (well-defined for all odd `n` since `M(n) = N(n²)` and `n² ≡ 1 (mod 8)`; `M(3) = −1` from `M(ω) = −2·log ω/log 9`). Prove:

   ```text
   ΔM = J((y+1) / 2^(v₂(y+1))) − J(1 + 2^s y).
   ```

   The content is the *location* it gives the core-extraction deficit: the increment is the mismatch of two exact operations on the two sides of one integer `y`, rather than "information disappearing between abstract cores." Register warning: this is a reformulation of `ΔM = N((ω₊/ω)²)`, derived in a few lines from existing laws — present it flatly, as a better coordinate for the same open object, not as progress on the object.

3. **The exit map.** Define `G := E ∘ R` on odd exits: for `m = v₂(y+1)`, `q = (y+1)/2^m`,

   ```text
   G(y) = (3^m q − 1) / 2^(v₂(3^m q − 1)).
   ```

   Prove: (i) `G(y)` is the exit of `y`'s state — so `G` is the reduced map `F` conjugated to exit coordinates, not a new dynamical system (say so explicitly); (ii) `G` is constant across every representative fiber (all `D` doors of one state share one `3^m q = 3^D Ω`); (iii) `G` is total on live doors and its image consists of live doors (`2^s y = 3^D Ω − 1 ≡ 2 (mod 3)` forces `3 ∤ y` for every genuine exit) — contrast explicitly with 14.8.3, where the top-door lineage law is *partial* by mortality.

4. **The fixed-stratum affine/contraction law.** On the stratum `m = v₂(y+1)`, `r = v₂(3^m q − 1)`, prove `G` is affine over `Z₃` with unit multiplier `3^m 2^(−(m+r))`, hence for `y, z` in the same `(m, r)` stratum:

   ```text
   v₃(G(y) − G(z)) = v₃(y − z) + m.
   ```

   Record the contrast with 14.13 precisely: extracting a predecessor core *loses* `d` 3-adic digits; advancing the exit map on a fixed stratum *gains* `m` digits of 3-adic agreement — no contradiction, because `G` never extracts a core (the only divisions are by powers of 2, which are 3-adic units).

5. **The decision point: a total graded law for the 3-adic anchor along forward orbits.** Ask whether `ΔM₃(y) := M₃(G(y)) − M₃(y)` — total on live doors by 3(iii), unlike 14.8's partial backward version — obeys a graded law on the `(m, r)` strata: determined by, and computable from, `y mod 3^(k + f(m,r))` plus the stratum labels, for an explicit offset `f`, in the mold of 14.8.2 / 11.8.7.3.1. Note `ΔM₃ = −log₂(G(y)/y)` by the affine-log identity (14.2.3), so the question is whether the stratum data pins the increment's digits. Either prove the law (theorem + fresh verification) or record the obstruction with the same precision as 14.13's three numbered failures.

6. **Reconciliation with the deficit (mandatory closing step, whatever item 5 yields).** The stratum labels `(m, r)` are *2-adic* data about `y`. Answer explicitly: does the exit seam evade the core-extraction deficit, or relocate it — i.e., when the contraction law is composed along an orbit, where does unbounded-depth information now sit (in the 3-adic residues, which propagate with gain, or in the stratum-label sequence, which is exactly the forward `(σ, s)` data the digit budget 11.8.7.7 already prices)? A precise "relocated, here is the accounting" extends the deficit's diagnostic reach and is a fully successful outcome. Do not let the gain in item 4 be quoted anywhere without this accounting next to it.

## Success / stop criteria

- **Floor (expected):** items 1–4 proved and verified — they are checked-true statements whose proofs are short. This alone justifies the session: it gives the Bridge page a working formulation instead of a perimeter map.
- **Primary:** item 5 resolved either way — a total graded `ΔM₃` law on strata, or a precisely recorded obstruction.
- **Stop:** after item 6 is written, stop. Do not open a density-exponent computation (that front is closed per 14.13's own stop criterion), do not iterate `G` numerically hunting statistics (the §17.7 program is at its natural endpoint), and do not chase a proof of any equidistribution statement (parked by the stopping rules). If item 5 produces a law and the law suggests further structure, log the suggestion in `briefs/door-seam-findings.md` and stop anyway — composition of the law along orbits is a separate decision for the main session.

## Placement and numbering

- Theorems go in `reverse.md` as a new **§14.14 (the door/exit seam)** — the machinery is door machinery, even though item 2's identity is about the forward `ΔM`. Never renumber existing anchors.
- `bridge.md` §16 gets **pointers only** (its charter forbids proof effort on the page): a short paragraph in 16.1 naming the door-centred formulation with a pointer to 14.14, and a perimeter entry (16.4.7 or extending 16.4.5). Update its `updated:` field.
- Cross-page status sweep per AGENTS.md when done (HANDOFF.md "State of the fronts" one-liner included).

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the code that suggested the result; record what was checked, the range, seeds, and the date, inline in the owning section.
- Verification code goes in `experiments/` (suggested `experiments/door_seam.py`), states which results it supports, stays runnable.
- Failures and obstructions are recorded, not deleted; 14.13 is the register precedent for item 5's negative branch.
- Register norm: flat, calibrated prose. The exit map is a *coordinate change on known dynamics* — no excitement inflation, and item 4's "gain" is never quoted without item 6's accounting.
- Work on branch **`door-seam`**, commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging (mirror-queue precedent).
- No scope expansion. Off-brief findings go to `briefs/door-seam-findings.md`.

## Definition of done

Items 1–4 as proved, verified theorems in reverse.md §14.14; item 5 as a theorem or a recorded obstruction; item 6's accounting paragraph; bridge.md pointer edits; clean per-item commits on `door-seam` with `experiments/door_seam.py` committed and passing. An honest closing status paragraph in §14.14 stating what the seam did and did not change about the Bridge.
