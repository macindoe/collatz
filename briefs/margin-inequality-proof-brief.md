# Brief: our own proof of the margin inequality (the entropic route, Stirling explicit) — for a delegated session

**Context required before starting (in order):** `README.md` (binding stopping rules), `AGENTS.md` (nothing is "proved" without independently written verification code; conservative math edits), `HANDOFF.md` item 1 (round-10 paragraphs), `briefs/merle-la7-close-check-findings.md` (this round's numerics — §2(c) the entropy route's tightness, §3 the γ identity **with its symbolic derivation**, §2(e) the 12/7 constants, §2(h) the threshold reconciliation), `briefs/merle-lean-r10-audit-findings.md` (the **operational definitions**: what `margin(n)` is, why the hypotheses pin `K`, why `C(K−2, n−1)` is the L-A7 word count, and the tuned-north-cell coverage gap), `briefs/merle-la7-mu-check-findings.md` (the original L-A7 record).

## Why this exists

In round 9 we flagged, as an unproved ingredient of L-A7, the for-all-`n` margin inequality `margin(n) ≥ c_gen·n` (verified `n ≤ 2000`, min slack `2.84` at `n = 2`), and **offered to write the proof**. Merle accepted the offer, and then — prompted by our own Stirling warning — found a route that avoids Stirling entirely (the rational binomial bound at `x = 12/7`) and proved it at kernel with the rational constant `1/13`, about 3% below `c_gen`. His letter and the ledger both explicitly say the offer still stands and that he hopes we take it: *"Mine is the elementary route; yours would be the one that connects to the published form, with the Stirling term handled explicitly as your own warning demands. Two proofs of one inequality, from two directions, verified in two clean rooms."*

So this is **not** redundant work. Two things make our proof worth having: (a) it targets the **true constant `c_gen`**, not a rational 3% below it; (b) it is the route that connects to the published Junction-Theorem entropy form. Deliver it to our own standard, as an honest proof with every step checkable — including, if it comes to it, an honest failure.

**Stopping-rule compliance:** this is a proof of an elementary counting inequality that this project already uses, offered and accepted in correspondence. It is not a cycle search and opens no computational front.

## The statement

Fix `β = log₂ 3`. For `n ≥ 1` let `K = K(n) = ⌈nβ⌉` (the tuned north cell — the audit findings confirm the L-A7/Lean hypotheses `3^n ≤ 2^K < 2·3^n` pin exactly this `K`), and

> `margin(n) := K − log₂ C(K−2, n−1)`,  to be shown `≥ c_gen·n` for all `n ≥ 1`, where `c_gen = 0.0793186…`

**Establish the exact identity for `c_gen` first** and state it in the findings — do not carry it as a decimal. Our own round-8 derivation defines `c_gen` as a large-deviation rate; the round-10 findings prove symbolically that `γ·β = c_gen` with `γ = 1 − h(1/β)` and `h` the binary entropy. So

> `c_gen = β·(1 − h(1/β)) = β − β·h(1/β)`

Verify this against the round-8 (B) derivation yourself before using it (§3 of the la7-close findings has the symbolic steps). Everything downstream depends on it: the asymptotic margin is *exactly* `c_gen·n` to first order, which is why there is under two bits of room and why the route is tight.

## Route sketch — verify, improve, or replace; do not force it

The crude entropy bound `C(m,k) ≤ 2^{m·h(k/m)}` leaves an asymptotically **constant** margin (measured `[1.66, 2.10]` bits, min `1.6647` at `n = 16266`) because it discards exactly the `(1/2)log₂ n` Stirling factor. The natural fix is to **keep** that factor rather than bound it away: via Robbins' form of Stirling (`n! = √(2πn)(n/e)^n e^{r_n}`, `1/(12n+1) < r_n < 1/(12n)`), with `m = K−2`, `k = n−1`, `p = k/m`,

> `log₂ C(m,k) ≤ m·h(p) − (1/2)·log₂(2π·m·p(1−p)) + (log₂ e)/(12m)`

which turns the Stirling term from a debt into a **credit that grows like (1/2)log₂ n**. The remaining work is then the perturbation term: bounding `K − m·h(p)` below by `c_gen·n` plus controllable error, where `K = nβ + θ` (`θ ∈ [0,1)`), `m = K−2`, `p = (n−1)/(K−2)` — i.e. comparing `m·h(p)` against `nβ·h(1/β)` when `p` differs from `1/β` by `O(1/n)`. Use concavity/Taylor with an **explicit** second-order remainder (`h″(p) = −1/(p(1−p)ln2)`, bounded on the relevant `p`-interval — state the interval and prove `p` stays in it for all `n ≥ n₀`), and keep every constant explicit. Note `h′(1/β) = log₂(β−1)` is the natural conjugate — the same `x* = 1/(β−1)` that Merle's rational route approximates by `12/7`; recording that correspondence in the findings is worthwhile.

Then close the small-`n` range `n < n₀` by **exact finite computation** (exact integers for `C(K−2,n−1)`, controlled precision for the logs, robustness of every decision stated), and say plainly what `n₀` the analytic argument needs.

**Honesty requirements, non-negotiable.**
- Every inequality displayed must be *proved*, not observed. Where a step is "verified numerically to `N`", label it that way and do not let it into the proof chain.
- If the route does not close for all `n` — e.g. the perturbation term eats the Stirling credit at some scale — **say so and report where**, with the obstruction stated exactly. An honest negative here is a real deliverable and is worth more to this correspondence than a forced proof. Merle's whole round is built on withdrawing an unbacked estimate; we hold the same bar.
- Scope must be stated as precisely as the audit stated his: this covers the **tuned north cell** `K = ⌈nβ⌉`. If the argument extends to the south shore / other cells, say so and prove it; if not, name the gap.

## Queue

1. **Derivation.** Write the proof in `briefs/margin-inequality-proof-findings.md` as running mathematics: the exact `c_gen` identity, the statement, the Robbins step with the direction of every inequality justified, the perturbation bound with explicit constants, the choice of `n₀`, the finite closure, and a final theorem statement with its exact hypotheses. Include a short "what this does not cover" section.
2. **Verification code** (`experiments/margin_inequality_proof_check.py`, freshly written, importing nothing from prior checks): (a) verify the **final** inequality directly over `n = 1..20,000` (exact integer binomials; state your log precision and why every decision is robust); (b) verify **each intermediate bound separately** over the same range — the Robbins step, the perturbation bound, the `p`-interval claim — so a broken link would be caught rather than masked by slack in another; (c) print the minimum slack of each step and where it occurs; (d) include a **negative control**: the same chain with `c_gen` replaced by a constant slightly above it must fail, and the code must show it failing.
3. **Cross-check against the round's known figures:** min slack `2.8414` at `n = 2`; the crude-route figures (`1.6647` at `n = 16266`, max `2.10492` at `n = 190537`) should be reproducible as the *degenerate* case of your bound with the Stirling credit discarded — a good sanity check that your version really is the refinement.
4. **Record:** the findings file (item 1, completed with results), the script + committed output, and **one scoped paragraph** in `HANDOFF.md` item 1. If the proof closes, state exactly what is now proved our side and that it is offered to the ledger as the second, entropic proof at the true constant.

## Rules

- Branch **`margin-inequality-proof`** from your worktree HEAD (verify it contains this brief; state the base SHA). Per-item commits; do NOT merge — the main session reviews (re-runs the script) and merges.
- Read-only everywhere outside this repo: no pushes, no shared-repo writes, no web access (all ingredients are internal; the Diophantine input is not needed for this inequality).
- No reply paragraphs, no ledger/co-edit text, no key turns. Stop after item 4.
- Register: flat and calibrated. No excitement inflation. A proof is called a proof only when it is one.
