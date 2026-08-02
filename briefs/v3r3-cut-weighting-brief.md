# Brief: the cut, the weighting, and the clock (v3 round 3, major finding)

**Round.** Third external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `dc61306` (= current `main`). You are Wave 2. Two Wave 1 delegates have reported and their results are **inputs you must use, not questions you may reopen**.

**This is a design task, not an edit task.** Produce text; change nothing outside your findings file.

## What is already settled, and binding on you

**The author has chosen Option 1.** AEH is being strengthened to quantify over all finite block lengths, in letter coordinates. Read `briefs/v3r3-aeh-object-findings.md` §3 (the definitions block), §4 (Option 1), and §7 (its drop-in text) before you write anything. In particular these are fixed and you must use them exactly:

- the observable `W_{k,D}` with its capped labels;
- the cap `D`;
- the law `π_{k,D}`, with the cap visible in the notation;
- **total variation** as the norm;
- the **two-sided** `B̂` as the probability space;
- the segment-boundary treatment of §3.6.

If your work forces a change to any of them, that is a finding — report it loudly rather than quietly diverging.

**Delegate B has refuted the `1/β` support.** Read `briefs/v3r3-inselmann-horizon-findings.md` in full, especially §0, §2.5, §3 (S1–S4) and §5. The short form: the repository's claim that Inselmann's descent horizon *is* `θ = 1/β` reduced blocks per bit is circular — the conversion divides by `E[m] = 2` Syracuse steps per block, which is a two-letter statistic of the parity word that Inselmann never counts and that AEH itself asserts. So **the sentence at `aeh.md` L32 — "For `θ < 1/β` … the cut binds on a vanishing density of starts" — has no external support.** B supplies an unconditional in-house replacement (S1) that covers `θ < 1/4` only, and an honest restatement of what Inselmann does give (S2) in total-exponent time.

## The finding you own

The reviewer:

> For each start `x`, `ν_{k,N}(x)` is normalized by that orbit's number `Q_N(x)` of qualifying visits. Therefore the phrase "no visit reweighted by the orbit it came from" is misleading: each visit actually has weight `1/Q_N(x)`.
>
> When the cut binds, `Q_N(x)` is random — the exact ratio-estimator regime §13.5 forbids. The hypothesis nevertheless quantifies over every `θ > 0`. It also leaves `ν` undefined when `Q_N(x) = 0`.
>
> Clean options: restrict "admissible" to regimes where `Q_N(x) = T_N` for a density-one set, and state that condition rather than asserting its threshold; or retain deterministic normalization `1/T_N` and give below-cut visits a cemetery symbol, so that AEH itself says whether their mass vanishes; or keep stopped normalization for all `θ`, but stop identifying it with the unbiased calibration protocol.

Check each clause against the files before accepting it. The relevant sites are `aeh.md` L30 (Hypothesis 13.2.1), L32 (the "Why the ensemble" paragraph), L46–53 (§13.4's protocol and its reconciliation sentence — "a per-orbit mean is safe exactly when its denominator is deterministic"), L55–67 (§13.5's standing rule), and `paper/collatz-reduced-v3.tex` L243–257 and L259–277.

Note the tension you are resolving is *internal and already written down*: §13.4 states the safety criterion in exactly the terms that make the reviewer's objection bite, and the hypothesis then quantifies over every `θ > 0` regardless. Round 2 saw part of this and parked it (`briefs/v3r2-aeh-formulation-findings.md` §9 item 4: "for `θ ≥ 1/β` the cut genuinely binds, the tally denominator becomes random, and `13.5`'s rule bites … a formulation that is clean *and* covers `θ ≥ 1/β` with a deterministic denominator eluded me"). It is your job now, and B's verdict has moved the goalposts: the safe regime is not `θ < 1/β` but at best `θ < 1/4`, unless you can establish otherwise.

**"Admissible" is never defined.** `aeh.md` L30 and `paper` L256 both close with "for every admissible `θ` and `(X_N)`" and no section says what admissible means. Fix this; do not paper over it.

## The clock — a directive, not an option

This comes from the author, and it is an accounting fact rather than a preference. Implement it unless you find it false.

Inselmann's map divides by 2 one step at a time, so **his step count is the total exponent `S = Σ(mᵢ + rᵢ)`** — which is the cascade's own currency, exactly what the repository's base case counts (`S + 1 ≤ L`, `aeh.md` L34), and exactly the unit the digit budget is stated in (`paper` L168: "consumes the state's `2`-adic data to depth `σ + k + 2`"). In that clock the three quantities are directly commensurable, per bit of start: our cylinder base case at `1`, Inselmann's protected window at `4.8188`, the digit budget in the same unit. **Nothing needs converting.**

The circular step existed only to re-express both endpoints in *blocks* per bit — and blocks are the one unit whose exchange rate is unknown, because that rate is `E[m]`. Note that `β = 2(2 − log₂3)`'s leading factor of 2 *is* `E[m]`, so "`1/β` blocks per bit" carries the disputed conversion inside its own definition (B's S4).

So: **restate the horizon in total-exponent (digits-spent) time**, and let blocks per bit be a derived quantity that visibly carries its AEH-dependence. Work out what this does to `θ`, which is currently a rate in blocks per bit — including whether `θ` survives as a symbol, what the horizon `T` becomes, and whether the hypothesis should be quantified over an exponent budget rather than a block count.

**One naming hazard to disambiguate wherever horizons are stated.** The paper's `T` is the odd-to-odd map (`paper` L50). Inselmann's `T` is the one-division map. `aeh.md` L94 (`13.6.3`(i)(b)) says "letter `n` occupies exactly `m_n` raw `T`-steps" in the odd-to-odd sense, while the same page's base case counts total exponent. Three readings, one letter. Say which is which, once, wherever it matters.

## The task

1. **Adjudicate the weighting.** Is each qualifying visit weighted `1/Q_N(x)`? If so, say plainly what the current sentence "each qualifying visit counted once, with no per-orbit reweighting" actually means and whether it is defensible as written.
2. **Choose the normalization.** Take one of the reviewer's three options or a better one, with reasoning, and state the cost. The cemetery-symbol option is attractive because it makes the hypothesis itself adjudicate the below-cut mass; check whether it interacts correctly with `W_{k,D}`'s alphabet (a cemetery symbol is one more letter, and A's alphabet is now finite — confirm this does not break anything of A's).
3. **Define "admissible."** Explicitly, for `θ` (or its exponent-time replacement) and for `(X_N)`.
4. **Handle `Q_N(x) = 0`.** State what `ν` is, or restrict the quantifier so the case cannot arise.
5. **Restate the non-binding claim.** Using B's S1 for what is unconditional, B's S2 for what Inselmann genuinely extends, and your own work for anything further. Do not restore a `1/β` claim without a proof; if you find one, that is a major result and must be flagged as such.
6. **Implement the clock.** As above.
7. **Resolve the `ω_+` versus `x_exit` cut gap.** `aeh.md` L48 records that the statements cut on `x_exit` while the code cuts on the core `ω_+`, calls the latter strictly stronger, and observes that neither binds in the runs. B's §2.7 rider 3 notes the envelope does not control `ω_+`. Settle whether the hypothesis should cut on the door or the core, and say which the calibration record then supports.
8. **Trace the consequences.** For each of `13.4`'s protocol reconciliation sentence, `13.5`'s standing rule, `13.3.1`, `13.3.2`, and the paper's §5: survives verbatim, survives restated, or fails.

## Deliverable

Write **only** `briefs/v3r3-cut-weighting-findings.md`, containing:

1. the weighting adjudication, stated plainly;
2. the chosen normalization with its cost, and the rejected options with why;
3. the definitions: "admissible", the `Q_N = 0` case, the cut coordinate;
4. the horizon in exponent time, with `θ`'s fate spelled out;
5. **exact drop-in text** — Markdown for `aeh.md` L30, L32, and any of L46–53 / L55–67 that move; LaTeX for `paper` L243–257 and L259–277 — consistent with A's §7 drop-ins and B's §5 drop-ins, which you must read first so that the three sets do not collide;
6. an explicit reconciliation note listing every place your text overlaps A's or B's, and which version should win;
7. the consequence trace;
8. anything you could not settle, named as an open question.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations of any kind. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not renumber any monolith anchor. Append new ones if needed.
- No change logs or dated journals in anything destined for a tracked page.
- Numbers, section numbers and quoted values must be verified against the files, not recalled.
- The paper is **unpublished**; statements may be restated in place. No erratum framing.
- Do not attempt to prove AEH, and do not reopen A's definitions or B's verdict. If you believe either is wrong, say so explicitly and stop rather than working around it.
