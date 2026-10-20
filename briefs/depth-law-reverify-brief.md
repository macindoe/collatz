# Brief: re-verify stage3.md 11.8.6.3's laws on all valid states with ω < 3000, 1 ≤ d < 64 — including ω = 1 — with a runnable script — for a delegated session

**Why.** `stage3.md` §11.8.6.3 ("Numerical verification", line ~613), paper 1 v4's Remark C.6 and the claims ledger row C-3.6 all say the laws were checked "over all valid states with `ω < 3000`, `1 ≤ d < 64` — 62,937 states". There are 63,000 such states (1,000 values of ω coprime to 6 below 3000, times 63 depths); 62,937 = 63,000 − 63 is exactly the count without ω = 1. The figure dates from monolith draft v075 and no script for it exists in `experiments/` (`briefs/v3-external-review-corrections-findings.md` line 224 already noted the missing script). The author stresses (2026-10-20) that ω = 1 is a very important class — it is the trivial cycle's class, the Baker bound's exceptional case (`d2cd6c6`), and central to the spider work — so the check must cover it, and say what happens there.

**Read first:** `AGENTS.md`, `stage3.md` §11.8.6 (the laws: absorption `a₊`, target shift, entry-depth law for `m₊` on all six residue-parity classes, `d₊ = m₊ + a₊`), `stage1.md` 11.8.3 (the valuation law and its ω = 1 scope after `d2cd6c6`), `spine.md` (the reduced map), `paper/collatz-reduced-v4.tex` Theorems C.3–C.5 and Remark C.6.

## Items

1. Fresh code (`experiments/depth_law_reverify.py`, exact integers, one documented command, committed output): for every valid state `(ω, d)` with `ω < 3000`, `gcd(ω, 6) = 1`, `1 ≤ d < 64` — all 63,000 — compute the exit and the next state directly, and check each law of 11.8.6.3 (and the valuation law of 11.8.3 on the lifting classes) against it. Report totals per residue-parity class, and **ω = 1 separately**: does every law hold there as stated, or is ω = 1 a case the laws state differently (as the Baker bound's was)?
2. Diagnose the 62,937: find whether the original run excluded ω = 1 (or anything else) and why, if the record says.
3. Update `stage3.md` §11.8.6.3's "Numerical verification" line in place: the exact range now checked, the count, the script, the date; if ω = 1 needs a stated exception or note in any law, add it conservatively and list it for the main session. One current verification line, no change-log prose; front matter `updated`.
4. Do not edit `paper/` — report the exact replacement sentence for Remark C.6 and the ledger row C-3.6, for the main session to apply.

## Rules and deliverables

Nothing outward; if a command is denied, stop and report. Edit/Write only; encoding scan before committing; foreground until committed. Branch `depth-law-reverify` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverables: the script + output, the `stage3.md` edit, `briefs/depth-law-reverify-findings.md` (totals per class, the ω = 1 verdict, the 62,937 diagnosis, the replacement sentences).
