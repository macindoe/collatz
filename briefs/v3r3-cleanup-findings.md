# Findings: the round-3 residuals (v3 round 3, Wave 6, closing)

**Task:** `briefs/v3r3-cleanup-brief.md`. **Branch** `v3r3-review-round3`, from `eca22d4`. Worked in the main
working directory; no worktree, no push, no merge, no rebase, no branch switch. Nothing under `paper/` was
touched, opened for edit, or rebuilt.

Four residuals, four edits, five changed lines across three files. All edits made with the Write/Edit tools.
Every edited file still decodes as UTF-8 with `0` mojibake characters (`â`, `Ã`, `Â`, `U+FFFD`): `aeh.md`
carries its `≤ 52`, `— 170`, `ε 29`, `π 31`, `θ 42`, `− 181`, `⌈⌉ 14`, `B̂ 14`, `≥ 66`; `anchor-digit-search.md`
and `stage1.md` likewise unchanged in their glyph counts.

**None of the four needed a `paper/` edit, and this was checked rather than assumed.**
`paper/collatz-reduced-v3.tex` carries no "pooled standard error" clause, no `0.018`, no bare `\pi_k` (it uses
`\pi_{k,D}` throughout), and neither index formula. So no second pin commit is required by this wave.

---

## 1. The chain-law rejection: re-measured, and printed as `≈ 15`

### What the clause states as its protocol

`aeh.md` `13.6.5`'s adjudication clause names its protocol in terms: *fixed-horizon, unweighted, per-visit,
uniform starts per `13.5`'s standing rule; starts in `[2^70, 2^71)`, burn-in `10`, horizon `30`, core cut
`ω_+ > 2^30` — which binds, `13.4` — `154,389` tallied visits of the run's `158,580`, seed `31005`.* That is
`experiments/aeh_symbolic.check_orbit_texture` at its defaults. **The printed cut is the stated protocol**, and
`28647e1` deliberately kept the clause's other four figures true of that run, so the printed figure must be the
cut one.

### What I ran

A scratchpad driver importing `experiments/aeh_symbolic.py` **unmodified** (no repository script was edited;
importing runs no `__main__` block), calling `check_b_side_laws`, `check_depth_comparison`, then
`check_orbit_texture(seed=31005)`. That function returns only the two `L1` distances, so the per-cell integer
counts were recovered by replaying its own loop with its own `F_step` / `stratum` primitives at the same seed
and the same parameters, and cross-checked against the frequencies the function itself prints.

**The replay reproduces the repository script exactly**: `154,389` tallied visits of `158,580` (`4,191` below
the cut), orbit `P(d=2) = 0.319187` against the function's own printed `0.31919`, `L1` orbit-vs-`B` `0.00517`
and orbit-vs-chain `0.03117` — all the values `13.6.5` already prints.

### The measurement

The chain law's cell is `P(d=2) = 19/63 = 0.3015873…` (reproduced by `check_depth_comparison`'s fresh analytic
kernel to `0.30158730158730185`). The offset is `0.319187 − 0.301587 = 0.017600`, which is the printed `0.018`.

| protocol | tallied visits | orbit `P(d=2)` | offset | SE at the predicted value | SE at the observed value | across-orbit SE |
|---|---|---|---|---|---|---|
| **core cut `ω_+ > 2^30`, as printed** | `154,389` | `0.319187` | `0.017600` | `1.16803e-3` → **`z = 15.07`** | `1.18639e-3` → `z = 14.83` | `1.19554e-3` → `z = 14.72` |
| cut-free, same seed | `158,580` | `0.318540` | `0.016952` | `1.15249e-3` → `z = 14.71` | `1.16998e-3` → `z = 14.49` | `1.16114e-3` → `z = 14.60` |

**Which SE is "pooled".** The script fixes the term itself. `check_orbit_texture` computes its letter-marginal
tolerance as `se = (e * (1 - e) / nvis) ** 0.5 * 1.5` under the comment *"tolerance 5 pooled-SE with 1.5x
inflation"*, with `e` the **predicted** cell probability — so the repository's "pooled SE" is the per-visit
binomial SE at the predicted value, `sqrt(e(1−e)/n)`. The word also does contrastive work in the very sentence
being fixed: the mod-3 cell two clauses later is quoted as `0.6662 ± 0.0015`, which is the **across-orbit** SE
the same function computes separately. Pooled = per-visit; that is the convention.

### What I printed, and why

**`≈ 15`.** Under the stated protocol the measurement is `z = 15.07`. The choice is robust to the SE
convention: every per-visit reading of the printed-cut run rounds to `15` (`15.07` at the predicted value,
`14.83` at the observed value), and the across-orbit reading, `14.72`, also rounds to `15`. Only the *cut-free*
run rounds to `14` under some conventions — and the cut-free run is not the protocol the clause states. The
edit is one token: `` `≈ 14` `` → `` `≈ 15` `` at `aeh.md` L219. Nothing else in the clause moved; `0.018`,
`L1 ≤ 0.006`, `0.3192`/`0.3185`, `0.6662 ± 0.0015` and the two `σ` verdicts all remain true of the same run and
were left alone.

**My measurement agrees with the fix delegate's `15.1` for the cut and its `14.5` cut-free, but those two
figures are not on one convention** — `15.1` is the predicted-value SE and `14.5` is the observed-value SE. Held
to a single convention the pair is (`15.07`, `14.71`) or (`14.83`, `14.49`). Recorded because the fix findings
present the pair as a like-for-like comparison; the disposition is unaffected either way, since both readings of
the printed-cut run round to `15`.

---

## 2. The retired symbol — `anchor-digit-search.md` L139. **Landed, one token.**

`equals aeh.md's `π_k`` → `equals aeh.md's `π_{k,D}``, inside the item-5 verdict's parenthetical *"(modulo the
routine check that Haar, read in the block/anchor coordinates, equals aeh.md's `π_{k,D}`)"*. The symbol only;
the claim is about the invariant measure and is unaffected. A `git grep` for bare `π_k` over tracked
`*.md`/`*.tex` outside `briefs/` now returns **nothing** — this was the one surviving instance, as the fix
findings reported.

**Front matter not bumped.** `anchor-digit-search.md` still reads `updated: 2026-07-23`. The round's own
precedent on this exact page is `a1e1701`, which edited it and left both `status` and `updated` untouched; and
the brief's rule against unscoped edits points the same way for a cross-reference token. `status` is untouched
for the same reason — a symbol rename does not move the page's status, which is about the executed search.

---

## 3. The status sentence — `stage1.md` L579. **Landed, minimally: the first remark only.**

`11.8.4.4`'s "Three remarks" paragraph opened *"First, it is a heuristic, but its only nontrivial ingredient …"*,
which now sits behind `11.8.4.5`'s ledger snapshot. The first remark now reads:

> First, its status divides at the digit budget: the ledger is the `s`-marginal of the capped-window law
> `π_{k,D}`, exact below the cap, and inside the budget it is unconditional — proved at every horizon rate
> `θ < 1/4` block per bit, for all but a vanishing density of starting values of each size (aeh.md `13.2.4`(d)–(e),
> `13.2.4.1`). Past the budget it remains a heuristic, and its only nontrivial ingredient there — the geometric
> tail on the lifting branch — is exactly the anchor-digit pseudo-randomness for which Appendix `A.4.6` provides
> direct evidence and `11.8.3.11` provides the unconditional worst-case cap.

The wording of the range, the exceptional set and the pointers is `11.8.4.5`'s own, so the two subsections now
say the same thing in the same words. **What survived untouched:** the second remark (empirical sharpness,
`48,000` block steps, `0.3338`), the third (where the deep-cascade machinery sits), the ledger derivation and
its stated premise at L565, the size ledger, and *"What the ledgers imply for Route A"* — including its
statement that the fiber-to-orbit bridge `11.8.5.6` is what *"would make the frequency ledger rigorous along
orbits"*, which remains exactly right, since the base case is a density statement about starting values and
supplies nothing along an individual orbit. `stage1.md`'s `updated:` was already `2026-08-02`.

---

## 4. The two index nits — `aeh.md`. **Both landed, as `briefs/v3r3-tailbound-findings.md` U5 words them.**

* **`13.2.4`(e), L101.** `` `P = W + L + ⌈(k+1)/2⌉ + 1` `` → `` `P = W + L + ⌈(k+1)/2⌉` ``. `P` had
  over-counted by one, in the safe direction; it enters only through `Λ` and the union bound, both monotone in
  `P`, so no bound in (e) changes sign or size in a way that matters, and the proof reads the same.
* **`13.6.4`(⇒), L201.** `` `n−W..n+L+⌈(k+1)/2⌉` `` → `` `n−1−W..n+L−2+⌈(k+1)/2⌉` ``. The old window started one
  letter late, supplying past depth `W−1` where the exceptional bound is quoted at `W`. Immaterial to the
  conclusion (`W` is universally quantified and the conclusion is a `W → ∞` limit), but the two indices are now
  right.

**The pair is internally consistent, which is the check worth recording.** `13.6.3`(iii) — untouched, and
correct as it stood — reads the window at visit `n+1` off letters `n−W, …, n+⌈(k+1)/2⌉`. So the window at visit
`v` needs letters `v−1−W … v−1+⌈(k+1)/2⌉`, and an `L`-block of window states at visits `n … n+L−1` needs
`n−1−W … n+L−2+⌈(k+1)/2⌉`, which is `L + W + ⌈(k+1)/2⌉` consecutive letters — exactly the corrected `P` of
`13.2.4`(e). The three statements now agree.

---

## 5. Found and not fixed

Reported, per the brief's rule against unscoped edits at this point in the round.

1. **The `15.1`/`14.5` pair in `briefs/v3r3-fix-findings.md` §2 mixes two SE conventions** (§1 above). Not a
   page defect — no tracked page quotes either figure — and the printed value is unaffected.
2. **`stage1.md` L565's ledger is still derived "under the equidistribution heuristic".** That is the
   derivation's stated premise and is still accurate as such; what changed is the status of the premise, which
   is what the first remark now records. Rewriting the derivation line would have been a rewrite rather than a
   status reconciliation, which the brief rules out.
3. **The Appendix A pin now names a commit that is no longer the branch tip.** `2e79417` claims "every wiki
   section and script named in this paper is cited at commit `677a76a`". That claim is still true *of*
   `677a76a`, and the paper carries none of the four facts this wave moved (checked: no `0.018`, no "standard
   error", no bare `\pi_k`, neither index formula in `collatz-reduced-v3.tex`), so nothing the paper prints has
   gone stale. But `aeh.md` `13.6.5` and `stage1.md` `11.8.4.4` have moved on by one commit since the pinned
   tree, and whether to re-point the pin at the merge commit — as `3511a0d` re-pointed the last one — is the
   author's call, unchanged in shape from what the fix findings §4 already flagged. **I did not touch
   `paper/`.**
4. **U1–U4 of the tail-bound findings and items 1–11 of verify §9 remain untouched**, as do items 5 and 6 of
   the fix findings' own "found and not fixed" list — in particular the true decay rate (`≈ 3^{−j}` measured,
   `5/6` proved), `13.2.4`(e)'s `ε'`/`Λ`/union-bound bookkeeping, and the composite five-coordinate
   reconstruction. None is a cleanup-wave item.
5. **Nothing new was found beyond the above.** Reading the current `§13` text before editing — the round
   rewrote much of it — the four sites were exactly as the brief described them, and the surrounding claims the
   edits touch (`13.6.3`(iii)'s window, `13.6.3`(iv)'s constant, `13.2.4`'s range, `11.8.4.5`'s snapshot) were
   all current.
