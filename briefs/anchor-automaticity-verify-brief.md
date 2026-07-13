# Brief: independent verification of the automaticity / Christol screen (§17.7.3)

**For a delegated Sonnet session.** A *verification* brief. The work under review lives on branch **`anchor-automaticity`** (commit message "S17.7.3: automaticity/Christol screen"), **not** merged to `main`. It was author-run by the main (Opus) session with no independent second pair of eyes; you are that second pair. Re-derive the §17.7.3 result from scratch and either confirm it (record the confirmation, push the branch) or find where it breaks (stop, loudly).

**Context required before starting (in order):** `README.md` (strategy + binding stopping rules), `AGENTS.md` (house norms — fresh independent code before anything is called verified), `anchors.md` §17.7 (esp. §17.7.2 for the deep-probe lineage and §17.7.3, the claim under review), and the code under review on branch `anchor-automaticity`: `experiments/anchor_automaticity.py`.

## The claim being verified

§17.7.3 reports that a single bulk anchor `M(ω)`'s bit sequence is **not 2-automatic** — hence (Christol's theorem) its generating function is **not algebraic over `F_2(x)`**. Evidence: two structural signatures at `2^17` bits, each run against Thue–Morse (automatic positive control) and a fair coin (non-automatic pole):
- **2-kernel growth:** `M(ω)` shows all 2047 kernel subsequences distinct through depth 10 (matching the coin; Thue–Morse plateaus at 2).
- **Subword complexity `p(k)`:** `M(ω)` saturates at `p(k)=2^k` for `k≤12` (matching the coin; Thue–Morse stays linear, ~36 factors), which is incompatible with the linear complexity Cobham's theorem forces on any automatic sequence.

## What "verify" means here (non-negotiable)

1. **Know the theory, then trust nothing.** Confirm for yourself the three load-bearing facts so a coding bug can't masquerade as a result: Christol (2-automatic over `F_2` ⇔ generating function algebraic over `F_2(x)`), Eilenberg (⇔ finite 2-kernel), Cobham (automatic ⇒ subword complexity `p(k)=O(k)`). One paragraph in your report showing you can state these correctly.
2. **Fresh generator AND fresh test code.** Do not import from `anchor_automaticity.py`, `anchor_single_deep.py`, or any repo script. Rewrite both the `M(ω)` generator (2-adic-log series; validate 12/12 against the anchors.md §17.7 table) *and* your own 2-kernel counter and subword-complexity counter. Independent reimplementation is the whole point.
3. **The positive control is the linchpin — verify it first.** Your Thue–Morse implementation MUST show a 2-kernel that plateaus at exactly **2** and linear subword complexity. If your test does not flag Thue–Morse as automatic, your test is broken and no conclusion about `M(ω)` is trustworthy — fix it before proceeding. (Thue–Morse: `t_n = popcount(n) mod 2`; kernel `{t, 1−t}`.)
4. **Re-run the repo script** `python experiments/anchor_automaticity.py` on branch `anchor-automaticity` and confirm its printed table matches §17.7.3.
5. **Cross-check with your independent code** for the same bulk `ω = 4996160569905494617`: your fresh 2-kernel counter should also give all-distinct through the tested depth, and your fresh subword counter should also saturate at `2^k` for small `k`. Agreement across two independent implementations, with the Thue–Morse control passing in both, is the real check.
6. **Probe the one place a false negative could hide.** "Not automatic to this depth" rests on the kernel/complexity not having plateaued *yet*. Push a little further if you have budget (kernel depth 11–12 with a shorter compare length, or subword `k` up to ~16 with the caveat that finite `N` caps `p(k)` at `N−k+1`) and confirm `M(ω)` keeps tracking the coin and never starts plateauing like Thue–Morse. Note the finite-`N` saturation ceiling explicitly so it is not mistaken for structure.

## Success / stop criterion

- **Confirmed:** your fresh generator validates 12/12, your independent kernel + subword counters flag Thue–Morse as automatic and place `M(ω)` with the coin, and the repo script reproduces §17.7.3's table. Append a single independent-verification line to §17.7.3 — *"Independently verified 2026-07-.. (delegated Sonnet session): fresh generator 12/12 and independent kernel + subword-complexity counters reproduce the result; Thue–Morse positive control passes in the independent code; M(ω) tracks the coin, no plateau."* Commit on branch `anchor-automaticity-verify`, and **push that branch.** Do **not** merge to `main` — the main session merges after reading your report.
- **Discrepancy** (generator mismatch, Thue–Morse control fails in your code, `M(ω)` shows any plateau/low-complexity signature, or the repo numbers don't reproduce): **do not push a confirmation.** Record exactly what broke in `briefs/anchor-automaticity-findings.md` on your branch and stop for review. A found error is the point.

## Rules

- Branch **`anchor-automaticity-verify`** (based on `anchor-automaticity`); commit your verification code; push only on the confirmed path; never merge to `main`.
- Fresh code per AGENTS.md; failures recorded not deleted; `sources/` immutable; no scope expansion (off-brief interesting → `briefs/anchor-automaticity-findings.md`).
- This verifies an **experiment**, not a proof; nothing here concludes anything about AEH. The deliverable is "§17.7.3's not-automatic result reproduced independently" or "it did not, here's where."

## Definition of done

Either (a) an independent-verification line in §17.7.3 on branch `anchor-automaticity-verify`, pushed, not merged; or (b) a documented discrepancy in `briefs/anchor-automaticity-findings.md`, flagged for main-session review. One honest paragraph back either way, including your one-paragraph statement of the Christol/Eilenberg/Cobham chain.
