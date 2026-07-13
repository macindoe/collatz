# Brief: independent verification of the deep single-anchor probe (§17.7.2)

**For a delegated Sonnet session.** This is a *verification* brief, not a build brief: the work under review already exists and is already on `main` (commit `ade574d`, "S17.7.2: deep single-anchor probe"). It was author-run by the main (Opus) session with no independent second pair of eyes — this brief supplies that second pair. Your job is to re-derive the §17.7.2 result from scratch and either confirm it (and record + push the confirmation) or find where it breaks (and stop, loudly).

**Context required before starting (in order):** `README.md` (strategy + binding stopping rules), `AGENTS.md` (house norms — especially "before marking anything proved / verified, run an independent numerical check with freshly written code"), `anchors.md` §17.7 in full (§17.7.1 is the breadth battery this extends; §17.7.2 is the claim you are verifying), and the code under review: `experiments/anchor_single_deep.py` and `viz/anchor_single_deep_visualizer.html`.

## The claim being verified

§17.7.2 reports a **clean pass** for a single bulk anchor `M(ω)` read to `2^17 = 131072` bits — 32× deeper than §17.7.1's 4096-bit breadth battery — across five tests (run-length vs Geometric(1/2), window bit-sum vs Binomial, autocorrelation to lag 512, block-entropy scaling, zlib), each against a matched i.i.d. fair-coin control. Two bulk anchors clean; `ω=3` and `ω=25` used as negative controls; two wrinkles explicitly recorded (ω=25's `z=−3.40` density deficit as expected bottom-regime structure; the second bulk anchor's run-length `p=0.026` as a multiplicity artifact).

## What "verify" means here (non-negotiable, from AGENTS.md)

1. **Fresh generator, independently written.** Do **not** import `compute_M_omega`/`anchor_bits` from `anchor_single_deep.py` or `anchor_digit_structure.py`. Write your own `M(ω)` generator from the definition (`9^N(ω) = ω^{-1} (mod 2^k)`, `M(ω) = N(ω^2)`; the 2-adic log via its convergent series, stage1-synthesis.md remark after Thm 11.8.3.6.6). Validate it against the 12-value worked-example table in anchors.md §17.7 (first 24 bits, lsb first) — if that fails, stop; nothing downstream is trustworthy.
2. **Re-run the actual script** `python experiments/anchor_single_deep.py` (seed `20260713`, defaults `--nbits 131072`). Confirm the printed statistics match §17.7.2 to the reported precision — the run is seed-deterministic, so this should reproduce exactly. Note runtime ≈ 2–3 min.
3. **Cross-check the two headline tests with your fresh generator**, not the repo's: recompute, for the primary bulk `ω = 4996160569905494617`, at least (a) the monobit density and (b) the run-length chi-square vs Geometric(1/2), and confirm they agree with both the script's output and your independent implementation. Agreement across two independent generators is the real check.
4. **Kick the tyres on the honest wrinkles, don't just accept them.** Specifically: is `ω=25`'s `z=−3.40` deficit stable, or an artifact of one 131072-bit window? Recompute it independently; if you have budget, extend `ω=25` alone to `2^18`–`2^19` bits and report whether the deficit persists or regresses to the mean. Either way is a valid recordable finding — persistence would upgrade it from "expected bottom-regime noise" to "a real property of M(25) worth a line"; regression confirms the §17.7.2 framing. Do **not** silently overwrite §17.7.2's characterization; report what you find and let it be read.
5. **Sanity-check the viz isn't broken.** The embedded `DATA` in `viz/anchor_single_deep_visualizer.html` should match the script's `--emit-json` payload for the primary anchor (regenerate with `--emit-json` and diff the numbers). The `file://` preview was flaky for the author; a node/JS syntax check plus a numeric diff of the embedded data is sufficient — don't block on rendering pixels.

## Success / stop criterion

- **Confirmed clean** (your fresh generator validates 12/12, the script reproduces §17.7.2's numbers under seed, your independent recomputation of density + run-length agrees, and the ω=25 wrinkle is either stable-and-noted or regresses): append a single independent-verification line to §17.7.2 in the form the wiki uses — *"Independently verified 2026-07-.. (delegated Sonnet session, branch `anchor-single-deep-verify`): fresh generator 12/12, script reproduced under seed, density + run-length cross-checked against an independent implementation; ω=25 deficit [stable/regressed]."* Commit it, and **push** (the code is already on `main`; you are pushing only the verification line + any ω=25 update).
- **Discrepancy found** (generator mismatch, numbers don't reproduce, a test is mis-specified, or the ω=25 wrinkle is actually a bulk-relevant signal): **do not push.** Record exactly what broke in `briefs/anchor-single-deep-findings.md` and in a commit message on your branch, and stop for review. A found error is the point of this brief, not a failure of it.

## Rules

- Branch **`anchor-single-deep-verify`**; commit with your verification code included; push only on the "confirmed clean" path above.
- Fresh code per AGENTS.md; failures recorded not deleted; `sources/` immutable; no scope expansion (anything interesting-but-off-brief → `briefs/anchor-single-deep-findings.md`).
- This verifies an **experiment**, not a proof. Nothing here concludes anything about AEH's truth; the deliverable is "the §17.7.2 clean pass was independently reproduced" or "it was not, here's where."

## Definition of done

Either (a) an independent-verification line in §17.7.2 + any ω=25 update, on branch `anchor-single-deep-verify`, pushed; or (b) a documented discrepancy in `briefs/anchor-single-deep-findings.md`, branch pushed-or-held per your judgement, **not** merged, flagged for main-session review. One honest paragraph back either way.
