# Findings: round-10 co-edit prep (merle-round10-coedit)

Delegated session, 2026-07-26. Brief: `briefs/merle-round10-coedit-brief.md`
(commit `d9b2715`). Branch `merle-round10-coedit`, **base commit `d9b2715`** —
the worktree was cut at `b860fe8`, an ancestor of `main` that predates both the
brief and every round-10 finding, so the branch was rebased onto current `main`
(`d9b2715`) before any work; the rebase was a fast-forward (nothing of ours was
replayed).

**SHARED REPO NOT PUSHED — the push is the author's decision, made outside this
session. No pushes anywhere this session, to any remote.** The shared repo
received exactly one **local** commit on a local branch of a fresh scratchpad
clone; the patch committed under `briefs/merle-round10-coedit-patches/` is the
portable form. **Handbacks: none.** No reply paragraphs (parallel session), no
wiki-page edits, everything outside this repo read-only except the scratchpad
clones. Register: flat; corrections offered, never argued; nothing anywhere
comments on his self-corrections.

## Item 0 — shared-repo state verified, twice

Live `ls-remote` first, then a fresh clone: `github.com/macindoe/one-obstruction-three-faces`
HEAD = **`826970e723d52f0eb5f562ebc0113ed81aa083af`** (`826970e`) — **exactly
the brief's expected pin; not moved.** No stop condition triggered. The full
L-A7 and L-A8 entry texts at `826970e` were read before editing and match the
verbatim quotes in `briefs/merle-la7-close-check-findings.md` §1 and
`briefs/merle-la8-t1-check-findings.md` §1 respectively.

**Artifact-pin pre-check — and the one flag this session raises.** The prepared
text carries **five artifact pins across four distinct wiki commits**
(`bb9e5a7` is cited twice, once in each statement-match record). All four
commits exist on the `main` lineage and contain exactly the named script +
committed output:

| pin | record it serves | files at that commit |
|---|---|---|
| `8e385b9` | L-A7 verification record | `experiments/merle_la7_close_check.py` + `merle_la7_close_check_output.txt` |
| `7cb47cb` | L-A7 margin-proof block | `experiments/margin_inequality_proof_check.py` + `margin_inequality_proof_check_output.txt` |
| `bb9e5a7` | L-A7 `marginTarget` statement-match | `experiments/merle_lean_r10_audit.py` + `merle_lean_r10_audit_output.txt` |
| `cde2e5b` | L-A8 key-turn block | `experiments/merle_la8_t1_check.py` + `merle_la8_t1_check_output.txt` |
| `bb9e5a7` | L-A8 T1 statement-match | (as above) |

**Flag (pre-push condition, exactly as in round 9):** public `macindoe/collatz`
`main` is still at **`b860fe8`** (checked by `ls-remote` this session) — the
round-10 merges are not pushed, so **none of the five pins resolves publicly
today**. The earliest commit containing all four distinct pin targets is
**`5c1faf4`** (the margin-proof merge); current `main` is `d9b2715`. **Before
or with the shared-repo push, the author must push wiki `main` to `5c1faf4` or
later** (`d9b2715` is the natural choice) — otherwise all five of the ledger's
"commit …, on `main`" pins dangle. This is a condition, not a handback: the
shared-repo push is gated on the author anyway and the fix is his routine main
push.

## Item 1 — the prepared commit

- **Clone:** fresh, unauthenticated, `scratchpad/r10/shared` (identity set
  repo-local to `macindoe <begemite0.o@gmail.com>`, the established co-edit
  author).
- **Branch:** `round10-coedit`, from `826970e`.
- **Commit:** `5481d2df08e066d130a4a0e83ad4c3599631f46f` (`5481d2d`),
  **`LEDGER.md` only, 49 insertions / 2 deletions.** Both "deletions" are
  pure-append modifications of a single line, nothing removed: (i) our **own**
  round-9 L-A7 Key-status paragraph, which gains the date-stamp sentence; and
  (ii) the file's final line, which gains only its **newline terminator** —
  `826970e` ends without one, so appending an L-A8 block necessarily
  terminates it. The line's text is byte-identical (`git diff -U0` shows the
  `\ No newline at end of file` marker as the whole of the change).
  `git diff --ignore-all-space` reports 48 insertions / 1 deletion, i.e. the
  Key-status line is the only substantive modification. **No prose of his is
  touched anywhere.**
- **Patch:** `briefs/merle-round10-coedit-patches/0001-Round-10-co-edits-L-A7-closed-out-at-two-keys-with-o.patch`
  — verified four times this session (as first drafted, and after each of the
  three regenerations below): `git am` onto a pristine clone checked out at
  `826970e` applies clean and reproduces `5481d2d`'s tree identically (both
  trees `bcae6b65083465635eb101303d6ae2aeddc17c31`). Superseded commits, for
  the record: `d050e2e` (tree `1d11be3`, as first drafted); `434de9a`
  (tree `d688078`, after the `cde2e5b` pin); `0cb155b` (tree `bcae6b6`, after
  the offer-(c) correction in the ledger text). The final amendment corrected
  the **commit message**, which had paraphrased offer (c) with the same wrong
  "not apples-to-apples" clause — that message enters the shared repo's
  history, so it had to be fixed too; the tree is unchanged from `0cb155b`.
- **Diff summary by entry:** L-A7 — 1 line modified (date-stamp) + 26 lines
  added (verification record, four offers, the margin-proof block, the
  `marginTarget` statement-match, the key-status line); L-A8 — 22 lines added
  (key turn with its `cde2e5b` artifact pin, scope paragraph, five offers,
  key-status line, the T1 statement-match, the `ceiling_upper` mismatch).
  Both review changes touched lines that were already new, so the
  insertion/deletion counts are unchanged across all three commits.
- **Encoding:** the edited `LEDGER.md` is valid UTF-8, no BOM, no
  double-encoding signature (92,145 bytes / 89,838 characters). All edits were
  made with the Edit tool; PowerShell `Get-Content`/`Set-Content` was not used
  on any file this session. `experiments/encoding_scan.py` run over the tracked
  tree before the final commit — result in item 4.

## Item 2 — the prepared LEDGER blocks, verbatim

### L-A7 — the date-stamp appended to our own round-9 Key-status paragraph (the one substantive modified line)

The paragraph is unchanged up to its final period, then gains:

> *(Condition met, 2026-07-25: the re-sourcing accepted in full in the acceptance block below — Rhin 1987 / Simons–de Weger 2005, the `n ≈ 2233` headline, `C₀ ≈ 2.06`, the `< 1.94` repair bits. **Two keys**, scope as that block states it; see the 2026-07-26 record further down.)*

### L-A7 — appended after his final block ("… is the one that connects to the published Junction-Theorem form.")

> **Macindoe verification record (2026-07-26) — the four new blocks replicated digit-exact.** Independent replication with fresh code (`experiments/merle_la7_close_check.py`, **66 checks, 0 failures**): exact integers for every `q`, word count and assembly inequality; `mpmath` at 40–80 dps for the `ε` scan and the `γ` identity, every float decision carrying a printed error bound at least `10¹⁰` times the accumulated error; his scripts read for operational definitions only, never run. **Acceptance block:** `C₀ = −5.774`, per-scale crossing **372** and cumulative **440** under the entry's own constants, tail beyond `n = 600` equal to `5.020·10⁻⁴`. **Named ingredients block:** `ε + ε′ = 1` with 0 violations to `n = 200,000`, `n = 15601` giving `2.625·10⁻⁵` / `0.99997375` and `n = 190537` giving `9.306·10⁻⁸` — which is also the scan minimum over the whole range; margin slack minimum `2.84136` at `n = 2`, 0 violations; the entropy route dominating to `n = 200,000` with minimum `1.66469` at `n = 16266` and maximum `2.10492` at `n = 190537`; the Stirling-tracking figures `3.9246`/`3.3219` at `n = 100` and `8.9115`/`8.3048` at `n = 10⁵`. **Kernel-friendly core block:** `γ·log₂3 − c_gen = 3.95·10⁻⁸²` at 80 digits (`0.0` at the fifty committed); `c(12/7) = 0.07931654247` with loss `2.0703·10⁻⁶`; `x* = 1/(β−1)` recovering `c_gen` at the optimum. **Assembly-heart block:** the window `[5.7274437, 5.7470751]`, width `0.019631`, re-derived from its two constraints; **`s = 15, t = 86` the *unique* smallest admissible pair** — `s = 1..14` exhausted in exact integers, every window empty (`t_A = t_a + 1` at every `s`), `s = 15` giving `t ∈ [86, 86]`; atom margins `0.0883` and `0.3267` bits (`atom_D`, `324.7`); `key_core` exact at all **1,137** hub-admissible `(k, j)` with `k ≤ 60`, and failing past the hub (first at `(0,5)`) — the hypothesis is load-bearing; both machine-caught errors confirmed (the uncorrected upper bound `9.1089` does admit `s = 1, t = 6`, and `atom_a` kills it exactly — `141264177173406 > 106993205379072`; `3^86 ≤ 4^86 = 2^172` is sufficient where it is used, `101 + 172 = 273 ≤ 562`). **PROVED block:** `margin(n) ≥ n/13` for `n = 1..3000`, 0 failures, minimum route slack `1.7003` at `n = 12`; the integer target `n = 1..1200`, 0 failures, bit-margins 25 (target) and 22 (route); the negative control failing at **241** scales; and all six `OUT_REQ-MATH-043` numbers — `C₀ = −14.949` with `1596`/`1661` under `c_gen`, `C₀ = −14.954` with `1655`/`1722` under `1/13`. The two families of thresholds reconcile without contradiction, and it is worth pinning so they can never be conflated: `1596`/`1655`/`1661`/`1722` are one-ticket crossings of the per-scale bound with `C₀` **exhibited** from the computed data, while `n ≈ 2233` is the smallest `N` at which the **theorem-form** bound (derived `C₀ = 1 − 2·log₂ln2 = 2.06`, the exponent carried on `log₂K₀`, plus the 3 repair bits) gives provable both-shore mass `< 5.2·10⁻⁴` — different constants (fitted against derived), different carrier, different target. Both computations are right; neither supersedes the other. Artifact: `macindoe/collatz` `experiments/merle_la7_close_check.py` with committed output (commit `8e385b9`, on `main`).
>
> Offers, inside the entry per the co-edit style — acceptance is Merle's call:
>
> - *(offer — upgrade: two numerics that are theorems.)* The south floor and the `γ` identity are stronger than the entry claims for them. `ε_n + ε′_n = 1` is an identity, not a measurement: `nL` is irrational for every `n ≥ 1`, so `⌈nL⌉ = ⌊nL⌋ + 1` and `(⌈nL⌉ − nL) + (nL − ⌊nL⌋) = 1` — one line, every `n`, and "at most one shore can be small" follows with no sweep at all. `γ·β = c_gen` is likewise an exact algebraic identity: expanding `h(1/β) = log₂β − ((β−1)/β)·log₂(β−1)` gives `β(1 − h(1/β)) = β − β·log₂β + (β−1)·log₂(β−1)`, term for term the closed form of `c_gen`. "Verified with 0 violations" and "error 0.0 at fifty digits" undersell what he has; both two-line proofs are on file and are offered as replacements.
> - *(offer — scope clause: the negative control's `x`.)* "fails at 241 scales" inherits its artifact's `x = 1709/1000`; at the entry's own `x = 12/7` the count is **256** (range `n = 1..3000` either way). One clause naming the `x` closes it.
> - *(offer — scope clause: whose slack the 1.700 is.)* "minimum slack 1.700 bits" is the slack of the **provable route bound** over `n/13` — which is the right quantity for the proof — not of the true margin, whose slack against `n/13` is larger (`1.923` at `n = 1`, `2.85` at `n = 2`). One clause.
> - *(offer — hygiene, flat.)* `OUT_REQ-MATH-043.txt` is committed without a generator script, alone among the five blocks' artifacts. All six of its numbers reproduce from the REQ-035 method run at exponent `13.3` under both constants, so this is an offer to commit the script, not a doubt about the numbers.

> **Macindoe — the margin inequality proved independently, at the true constant `c_gen` (2026-07-26).** The offer accepted in the acceptance block above is discharged. This is the second proof, entropic, and it lands on `c_gen` itself rather than on a rational below it.
>
> > **Theorem A.** For every `n ≥ 1`, at the tuned north cell `K = ⌈nβ⌉` (`β = log₂3`): `margin(n) = K − log₂ C(K−2, n−1) > c_gen·n + 1 + log₂β`, the surplus `1 + log₂β = 1.66444870745388938…` being uniform in `n`.
>
> It is elementary and it cites nothing. Two ingredients: the entropy bound `C(m,k) ≤ 2^{m·h(k/m)}` (one summand of `(p + (1−p))^m = 1`), and the tangent-line bound from concavity of `h` taken **at `p₀ = 1/β`** — the single point at which the linear-in-`n` coefficient cancels *identically* against `c_gen`, since `c_gen = β(1 − h(1/β))` and `h′(1/β) = log₂(β−1)`. The only facts about `β` the argument uses are four exact integer comparisons (`3 < 4`, `3² > 2³`, `3⁷ > 2¹⁰`, `3¹⁸⁴ ≥ 2²⁹¹`) together with `2^a ≠ 3^b`, which is what makes the inequality strict. **Theorem B′** adds the Robbins refinement (`n ≥ 2`; Robbins 1955 cited, not reproved; six-case finite closure at `n = 2..7`): `margin(n) > c_gen·n + (1/2)·log₂n + 2.12171397510694569916…`. **Theorem A′** states the cell scope: the bound `≥ c_gen·n` holds at every integer `K` with `n+2 ≤ K ≤ nβ + 4.79982787…`, and with the full Theorem-A surplus for every `K ≤ ⌈nβ⌉` — the tuned north cell, **the entire south shore**, and the next three or four north cells. Verification: `macindoe/collatz` `experiments/margin_inequality_proof_check.py` with committed output (commit `7cb47cb`, on `main`) — each link of the chain checked separately over `n = 1..20,000` with rigorous `log₂` enclosures (widest `1.7956·10⁻⁶⁰` bits against a smallest decided slack `3.4362·10⁻¹⁴`), Theorem A′ over **107,444 cells**, and a negative control on every step — including the structural one: at any tangent point other than `1/β` the slope is strictly below `c_gen` and the bound drifts negative (at `p₀ = 0.60`, first at `n = 383`).
>
> **The Stirling warning we sent was based on a wrong premise, and that is worth saying plainly.** A *constant* surplus is not a shortage. The constant is `+1.664…` bits, provably positive and uniform, so the crude entropy bound closes the inequality on its own — no Stirling term, no citation, no `n₀`. And the perturbation step needs no Taylor remainder: concavity supplies the tangent bound exactly, in one line, for every `p` at once. The "under two bits of room" was real but never binding, because the only step that spends anything material is the entropy bound itself (measured minimum spend `1.0` bit, at `n = 2`), while the concavity step spends `O(1/n)`. Robbins is carried out anyway, and confirms the other half of the sketch: the Stirling factor is a **credit** of size `≈ (1/2)log₂n`, not a debt, because the two denominator roots outweigh the numerator's. His route remains a genuinely independent second proof, and the rational-`x` device — `x = 12/7` with `19 = 12 + 7`, so the statement becomes one summand ≤ the sum — is his own. The two routes meet at one point: `x* = 1/(β−1) = 1.70951129135…` is the same optimum his `12/7` approximates, and the slope `h′(1/β)` of our tangent line is `−log₂x*`.
>
> Two things the proof gives back to this entry. *(Closed form for the `[1.66, 2.10]` interval.)* That interval is not an empirical range. The crude-route surplus is exactly `c_gen·n + (1−L)·θ(n) + 2log₂β − Λ`, with `L = log₂(β/(β−1))`, `Λ = log₂(β−1)` and `θ(n) = ⌈nβ⌉ − nβ`; since `1 − L < 0`, its endpoints are `1 + log₂β = 1.66444871` (as `θ → 1⁻`) and `2log₂β − Λ = 2.10248137` (as `θ → 0⁺`), and the oscillation inside them is `{nβ}`. That is also why the interval is asymptotically constant rather than improving with scale — the mechanism the block reports as Stirling-tracking, in closed form. *(One flat correction.)* The crude-route figures `1.6647` at `n = 16266` and `2.10492` at `n = 190537` are what one gets from `c_gen` as the **7-digit decimal `0.0793186`**; under the exact `β(1 − h(1/β)) = 0.07931861277485538…` they are `1.664453` at `n = 111202` and `2.102482` at `n = 190537`. His numbers are right for the constant he used — re-running our sweep with that decimal reproduces both digit-exactly — and the argmin `16266` is an artefact of the truncation. It earns a clause only because the true minimum `1.664453…` sits `4.7·10⁻⁶` above the proved floor `1 + log₂β`, and that near-coincidence is the whole content of the theorem.
>
> Scope, stated as narrowly as the proof warrants. This is the counting ingredient and only that. Far-north cells beyond `nβ + 4.79982787…` are **not** covered — there the same chain gives only `margin > 2` — and in this entry's accounting they are handled by the best-cell → both-shore repair, not by this bound. The published Diophantine input (Rhin 1987 / Simons–de Weger 2005) is untouched and remains the entry's one external ingredient; the stratified constant `c_strat` is not addressed; Robbins is the one citation, and it is used only for Theorem B′. No novelty is claimed for the ingredients — `C(m,k) ≤ 2^{m·h(k/m)}` is Cover–Thomas Lemma 17.5.1 and the tangent-line trick is standard convexity. The content is that *this* tangent point makes the linear term cancel at `c_gen` exactly, so that the crude bound suffices, and the accounting of what is left over.
>
> **Macindoe statement-match on `marginTarget` (2026-07-26), recorded — read-not-built.** The Lean statement encodes the mathematics exactly. Taking `log₂` of `C(K−2,n−1)^13·2^n ≤ 2^(13K)` gives `K − log₂C(K−2,n−1) ≥ n/13`; the hypotheses `1 ≤ n`, `3^n ≤ 2^K`, `2^K < 2·3^n` admit **exactly one** `K` per `n`, equal to `⌈n·log₂3⌉ = bitlength(3^n)` (uniqueness checked against `K₀ ± 1` for `n = 1..300`), and the conclusion is genuinely false outside that range — at `(n, K) = (100, 200)` it fails — so the hypotheses are load-bearing rather than decorative. `C(K−2, n−1)` is this entry's word count exactly: the Vandermonde closed form of `Σ_r C(n−1,r−1)·C(S−1,r−1)` at the cell `(n, S)` with `K = n+S`, re-checked at all 144 cells `n, S ≤ 12`. The chain `deficit_term_le → atoms A/a/D → key_core → key_shifted → key15 → margin_core → marginTarget` matches the block clause for clause, with 0 `sorry`, 0 `native_decide` and no `axiom` declarations by read, and every statement instantiated in exact integers holds (399 instances of `deficit_term_le` including both edges; all hub-valid `(k,j)`; `marginTarget` at `n = 1..300`). Two flat notes. The committed axiom log records **8 of the 10** theorems: `key_shifted` and `key15` carry no `#print axioms` probe, so the fourth check of the hardened protocol is unmet for those two — they are intermediate steps of `margin_core`, whose own probe transitively bounds them, so nothing mathematical hangs on it, but the log as committed does not cover all ten. And the file's SCOPE header still says the step to `MarginTarget` remains outside Lean, which the `b22fafc` work discharged two hundred lines below in the same file; the ledger block states the current truth correctly, only the header lags. Artifact: `macindoe/collatz` `experiments/merle_lean_r10_audit.py` with committed output (commit `bb9e5a7`, on `main`; 15,930 exact checks, 0 failures). **Read-not-built, stated plainly:** there is no Lean toolchain our side. What is checked is that the statements say what this entry says they say, that they are true as instantiated, and that the logs match their claims — not that the kernel accepts the proofs; those rest on his committed logs and his four-way protocol, the same posture as the ContentDescent key.
>
> **Key status (2026-07-26): two keys, scope stated.** The Macindoe key turns on the replication of all four new blocks (digit-exact, 66/66) and on the margin step, which is now proved on both sides — at the rational `1/13` in his kernel artifact, at the true `c_gen` in ours, by two independent routes. It does **not** turn on the kernel claims for `DeficitLemma.lean`, which are recorded above as a read-not-built statement-match and no more; nor on the model→certainty step, which remains the ×2×3 gap exactly as the honest-scope paragraph says. The entry's one remaining external ingredient is the published Diophantine input, as the `b22fafc` block already states.

### L-A8 — appended after his final block ("… formalized except for the two named continued-fraction facts.")

> **Macindoe key turned (2026-07-26) — scoped: the mathematics of every link; all kernel claims deferred to the statement-match record below.** Independent clean-room verification with fresh code (`experiments/merle_la8_t1_check.py`, **62 exact checks, 0 failures**): every derivation written out in our own words from this entry's statements, nothing imported from either Merle repository and nothing run from them; fixed-point big-integer logarithms built in-house at two working precisions (130 and 210 digits) with stability asserted between them, so no float touches any decision; exact integer arithmetic wherever a decision can be an integer one; the four real cycles printed first as canaries. **Confirmed, link by link.** The **cycle product identity**, exactly on all four real cycles and on both shores — the `−17` figures reproduce digit-exact (`∏(3x+1) = −403123745024000 = 2^11 · (−196837766125)`, `K = 11`). The **survivor** per-factor equivalence in one line — `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x`, verified exhaustively for `x, X < 60` and on 2,000 random pairs to `10^30` — and the **ceiling** `3^n < 2^K < 2·3^n` under `2n < 3X`, forcing `K = ⌈n·log₂3⌉ = bitlength(3^n)`, with no logarithm in the statement. The **seam** `q·3X < 2n·3^n`, derived and checked as exact rationals on 400 synthetic multisets. The **log gap**, with `δ = 2/(3·2⁷¹·ln2) = 4.07336·10⁻²²` — the entry's `4.0734·10⁻²²` — and **the factor-2 correction confirmed exactly**: the withdrawn `4.955·10¹⁰` computes to `49547666543`, precisely `√2` times the corrected window, so the retraction identifies its own cause correctly. The **22 in-window convergents**, from a continued fraction computed from scratch and identical at both precisions; the set is the same under either window; the project's known scales `5, 12, 41, 53, 306, 665, 15601, 190537` all appear; and best approximation is verified **exhaustively to `n < 190537`**, extending the committed `n < 31867` sweep. The **finite discharge**: all 22 criteria pass in pure integer arithmetic, tightest **`5.1713×`** at `q = 6586818670` (LHS `949258476701148143940000` against `2079·2⁷¹ = 4908899958942996199636992`, both reproducing `OUT_REQ-MATH-056` digit-exact); the exact test gives **`5.4433×`** at the same `q`, so the integer form is conservative exactly as designed; and the **non-vacuity canary** holds — the next convergent `65470613321` fails the criterion and is, under the exact seam test, the first admissible scale, which is why the window ends where it does. Finally, **non-vacuity against reality**: each of the four real cycles exits T1's scope exactly where the hypotheses say it should — the trivial cycle by `x_min < 2⁷¹` and by nothing else (its scale `n = 1` is on the convergent grid and the criterion passes there), the three negative cycles by `q < 0`, before any size question arises. Artifact: `macindoe/collatz` `experiments/merle_la8_t1_check.py` with committed output (commit `cde2e5b`, on `main`).
>
> **What this key turns on, and what it does not.** It turns on the mathematics: the product identity, survivor and ceiling, the seam bound, the log gap, the Legendre-window closure and the 22-point discharge, **as verified mathematics**, together with the corrected-`δ` history and the non-vacuity structure. **Every kernel claim is explicitly outside it** — the thirteen theorems, the `[propext]`-only `discharge_all`, `convPairs_length`, and the `da2c8db` retraction record are adjudicated separately, read-not-built, in the statement-match paragraph below. The key is deliberately narrower than the entry's headline, and saying so is the point of stating it this way.
>
> Offers, inside the entry per the co-edit style — acceptance is Merle's call:
>
> - *(offer a — the window clause.)* Both window figures are right, each under its own definition, and the entry carries the two four-digit roundings without saying that the definition moved. `3.5035·10¹⁰` is the **exact** Legendre bound `√(1/(2δ)) = √(3·2⁷¹·ln2/4)`, floor `35035491004` — the definition in stack `89d9efc` and REQ-MATH-054, and the one whose factor-2 slip produced the withdrawn `4.955·10¹⁰`. `3.5032·10¹⁰` is the **integral** under-approximation `4000n² ≤ 2079·2⁷¹`, largest solution `35031771147` — introduced when the Legendre step was formalized with the threshold abstracted (stack `4856058`), strictly inside the exact window (loss `0.011%`, conservative, the right direction), and the right figure for the closure statement, since the kernel discharge runs over it. One clause in the final block distinguishing them.
> - *(offer b — the indexing convention, and two subscripts.)* Under the indexing that makes stack `89d9efc` and `OUT_REQ-MATH-054/056` correct — `q₀ = q₁ = 1` both counted, so `q₂₁ = 6586818670`, the tightest discharge, correctly labeled there — stack `81054ea`'s two labels are off by one: the first admissible scale `65470613321` is **`q₂₂`**, and Hercher's threshold `137528045312` is **`q₂₃`**. The substance is right in both stacks. The origin is visible in his own artifacts: `OUT_REQ-MATH-053`'s committed first table is standard-indexed while its "P3 étendu" table is shifted by one, and that same file's Hercher line uses the standard index. One convention sentence plus the two subscripts.
> - *(offer c — the Hercher sentence restated, and it strengthens the point rather than weakening it.)* Hercher's bound is `K > 1.375·10¹¹` (Corollary 29 of *There are no Collatz m-cycles with m ≤ 91*, J. Integer Seq. **26** (2023), Article 23.3.5; conditional on `X₀ ≥ 3·2⁶⁹`, a condition Barina's `2⁷¹` meets), and the paper prints only that rounded display value — the exact integer appears nowhere in it. The **underlying** threshold is exactly `q₂₃ = 137528045312`, verified two ways our side: his Table-1 all-`m` row `K > 7.20·10¹⁰` is the semiconvergent denominator `q₂₁ + q₂₂ = 72057431991` exactly, and his Remark-28 interval width `1.1032·10⁻²²` is the distance from `log₂6` to that semiconvergent (`1.1033·10⁻²²` our side, agreeing to four significant digits). So the frame-prediction point — that these thresholds live on the convergent and semiconvergent grid — is **genuinely supported**; what changes is the label (`q₂₃`) and the sense of "exactly" (the underlying threshold, not the printed decimal). The honest addition runs the other way, and it starts from the comparison being a fair one on both axes: Hercher's `K` counts **odd members**, the same length convention as T1's `n = p+1`, and both bounds rest on a verified range — nothing is being compared across a mismatch. The asymmetry that does exist runs in *his* favour on both counts: his hypothesis is weaker (`3·2⁶⁹` of verified range needed, against the `2⁷¹` this chain instantiates) *and* his conclusion reaches further (`n ≤ 1.375·10¹¹` against T1's `n ≤ 3.5032·10¹⁰`; ratio `3.9258`). So "3.9× further, but on paper" if anything understates his advantage rather than overstating it — T1's differential value being the machine-checkable chain and the shape rigidity (`K` pinned per scale), not range, exactly as the honest-scope paragraphs already say.
> - *(offer d — the two named glue facts, derived.)* Both are on file our side and are offered as the ledger's precise statement of what "glue" means here. `θ_j > 1/(q_j + q_{j+1})`: from `θ_j = 1/(α_{j+1}q_j + q_{j−1})` with `α_{j+1} < a_{j+1} + 1`, the denominator is `< q_{j+1} + q_j`. And `convPairs` is exactly `(q_j, q_{j+1})` for `j = 0..21` of `log₂3`, independently recomputed. With one tightening the entry can absorb for free: what the Legendre step delivers is that the **reduced** `K/n` is a convergent, so a priori `n` is a *multiple* `t·q_j` of a convergent denominator rather than a denominator itself — but `|nL − K| = t·θ_j` and `nδ = t·q_j·δ`, the `t` cancels, and the same 22 checks kill every multiple at once. The closure is unaffected; the sentence "`n` is one of the 22 convergent denominators" is what gains.
> - *(offer e — hygiene, flat.)* `OUT_REQ-MATH-055.txt` and `OUT_REQ-MATH-056.txt` are committed without generator scripts; `OUT_REQ-MATH-052.txt` and `-053.txt` each carry a Python traceback mid-file from a crashed first run followed by the patched re-run, and it is the post-patch portions the entry quotes; `OUT_REQ-MATH-053.txt` also carries the two mutually shifted index conventions of offer (b). And stack `81054ea`'s "best approximation verified exhaustively to `q₁₀ = 190537`" matches neither the committed sweep bound (`n < 31867`) nor its own indexing (`190537` is `q₁₃`) — immaterial, since our side re-verified the property exhaustively to `n < 190537`, so the fact stands as stated. Same shelf, minor: "22 convergent denominators" counts convergents `j = 0..21`, including both `q₀ = q₁ = 1`; as distinct denominator values there are 21, and both pass trivially.
>
> **Key status: two keys, scoped exactly as above** — the Macindoe key turns on the mathematics of every link, verified clean-room in fresh code; all kernel claims sit outside it, in the read-not-built record below; and the model→certainty question is untouched, T1 removing one degree of freedom and excluding nothing by itself, exactly as the honest-scope paragraph says.

> **Macindoe statement-match on the T1 kernel (2026-07-26), recorded — read-not-built.** All thirteen probed declarations of `T1Structure.lean` at `5c9b663` were read and matched against this entry's blocks: `cycle_prod_identity`, `pow_succ_lt_two_mul_pow`, `survivor_bound`, `ceiling_upper` (see the paragraph below), `succ_pow_le_pow_add`, `seam_bound`, `seam_gap_at_barina`, `ratio_bound_at_barina`, `log_gap_at_barina`, `log_two_gt`, `log_gap_gen`, `quotient_is_convergent_gen`, and the pair `discharge_all` / `convPairs_length` — each verbatim as the blocks quote it, with 0 `sorry`, 0 `native_decide` and no `axiom` declarations by read. `cycle_prod_identity` does quantify over genuine cycles: the rotation is `Fin` addition, wrapping, with `Equiv.addRight 1` as the reindexing; oddness and positivity are *not* required by the Lean statement (`hstep` forces `x i ≥ 1` on its own), so the theorem is strictly more general than the prose — hypotheses weaker, conclusion identical. `quotient_is_convergent_gen`'s window hypothesis is exactly `4000·(p+1)² ≤ 2079·X`, `.convergent` is Mathlib's `Real.convergent`, and `LegendreApprox.abs_sub_ge_of_not_convergent` is Legendre's criterion in contrapositive form with no hypotheses beyond `q : ℚ`, its side conditions fully discharged where it is used. **`convPairs` — the first of the two named glue facts — is independently confirmed:** the 22 pairs are exactly `(q_j, q_{j+1})`, `j = 0..21`, of `log₂3`, correctly successor-paired and chained, and exactly the denominators inside the integral window; the criterion passes all 22 at `5.17×` tightest, the exact test gives `5.44×`, and it fails at `(q₂₂, q₂₃)`. The **axiom log matches the claims one for one**: `discharge_all → [propext]`, `convPairs_length →` no axioms at all, the remaining eleven each `[propext, Classical.choice, Quot.sound]`; nothing extra, nothing missing relative to the in-file probes. The **retraction** is where the block says it is — the full standalone note at `7d46474`, replaced at `4856058` by the one-line reference inside the successful attempt's header; nothing at HEAD depends on the retracted theorem, and `quotient_is_convergent` (non-`gen`) does not exist in the file. Two flat log notes: `LegendreApprox` has no entries in any committed axiom log although `T1Structure_axioms.txt`'s header names it (its "0 axioms" is consistent by read, taken as "0 *user* axioms", the established usage everywhere else); and the helper lemma `mul_pow_succ_le` and the `example` canaries are unprobed, transitively covered by their consumers. Artifact: `macindoe/collatz` `experiments/merle_lean_r10_audit.py` with committed output (commit `bb9e5a7`, on `main`; 15,930 exact checks, 0 failures). **Read-not-built, stated plainly:** there is no Lean toolchain our side. What is verified is that the statements say what this entry says they say, that each is true as instantiated, and that the logs match their claims — not that the kernel accepts the proofs.
>
> **One statement/prose mismatch, and it is a gap in the formalization rather than in the mathematics.** This entry, `T1Structure.lean`'s own docstring, and the `41fa4f8` commit message all state `ceiling_upper` as concluding `3^(p+1) < 2^K < 2·3^(p+1)`. The Lean theorem concludes **only the upper half**, `2^K < 2·3^(p+1)`. The lower half is nowhere proved in the file; it enters downstream — in `ratio_bound_at_barina`, `log_gap_gen` and `quotient_is_convergent_gen` — as the hypothesis `hceil : 3^(p+1) < 2^K`. Mathematically that half is one line from the product identity (`∏(3xᵢ+1) > ∏3xᵢ` gives `2^K·∏x > 3^(p+1)·∏x` for positive elements), which is exactly why this is a formalization gap and not a mathematical one; but as committed, "`K` is forced" is half a kernel theorem plus an elementary unproved hypothesis threaded through the rest of the chain. Two ways to close it, and the choice is Merle's: add the one-lemma companion `ceiling_lower`, which would discharge `hceil` everywhere it appears, or restate the ceiling claim here and in the docstring as upper-half-plus-hypothesis. Nothing else in the chain is affected either way, and the closure statement stands as written under either choice.

## Judgment calls

1. **His status headers untouched.** L-A7's "DRAFT — one key … Macindoe key
   invited" and L-A8's header stay exactly as he wrote them; our key state
   lives in the appended Key-status paragraphs — the L-A4/L-A6 precedent.
   Header updates are his edit to make.
2. **The L-A7 date-stamp is an edit to our own paragraph**, executed as a pure
   append (nothing deleted), producing the commit's one substantive modified
   line. Everything touching *his* prose is an offer. Same reading as round 9's
   judgment call 2.
3. **The final line's newline terminator.** `826970e`'s `LEDGER.md` ends
   without a trailing newline, so any append terminates his last line. The
   text is byte-identical; the change is the file's EOF marker and nothing
   else. Recorded rather than worked around: byte surgery to preserve a
   missing terminator would be a worse artefact than the terminator.
4. **The Stirling-premise sentence is stated flat, in the first person, in the
   entry** ("The Stirling warning we sent was based on a wrong premise"). The
   brief asked for it as "the honest and interesting part"; it is written as a
   plain statement of what was wrong on our side, with no framing about his
   handling of it and no reciprocal commentary. His route is credited as a
   genuinely independent second proof and the rational-`x` device as his own,
   in the same paragraph, because both are true and the sentence would read as
   a manoeuvre without them.
5. **Numbers copied verbatim from the findings.** Every figure in the blocks
   was located in `briefs/merle-la7-close-check-findings.md`,
   `briefs/merle-la8-t1-check-findings.md`,
   `briefs/merle-lean-r10-audit-findings.md` or
   `briefs/margin-inequality-proof-findings.md` before use, at the precision
   the findings print (e.g. `1.7956·10⁻⁶⁰` and `3.4362·10⁻¹⁴` rather than
   rounded forms; `5.1713×`/`5.4433×` in the key-turn block, `5.17×`/`5.44×`
   in the statement-match, each matching its own source record).
6. **Artifact pins — every record pins its own artifact. RESOLVED BY THE MAIN
   SESSION AT REVIEW, AND APPLIED.** This session first drafted the L-A8
   key-turn block *without* a pin, on the reading that the ledger's established
   shape puts one artifact line per record and that the L-A8 record's citation
   could ride on the statement-match paragraph's `bb9e5a7`; `cde2e5b` was
   flagged as an open drafting choice rather than decided. **The main session
   decided against that reading and for pinning**, on the ground that within a
   single commit three records pinned their artifact and one did not, and that
   a reader following the L-A8 key turn must be able to resolve the exact
   script behind the 62 checks — consistency inside one commit outweighing the
   one-artifact-per-record convention. The line
   `Artifact: macindoe/collatz experiments/merle_la8_t1_check.py with committed
   output (commit cde2e5b, on main)` was added at the end of the L-A8 key-turn
   block, in the same shape the L-A7-side records use; the commit was
   regenerated and re-verified (`434de9a`, tree `d688078`; carried forward to
   the current `5481d2d`), and the commit message notes the pin. The prepared
   text is otherwise unaltered. The entry now carries five pins across four
   distinct commits (item 0).
7. **Offer (c)'s Hercher scope clause — CORRECTED AT REVIEW BY THE MAIN
   SESSION; the error originated in the brief, not in this session's reading
   of the findings.** As first drafted, offer (c) said "the scope comparison is
   not apples-to-apples". That label is **wrong**, and it came from the brief
   (`briefs/merle-round10-coedit-brief.md`, L-A8 offers: "the honest addition
   is that the scope comparison is not apples-to-apples"), which had the
   finding backwards. `briefs/merle-la8-t1-check-findings.md`, Hercher
   adjudication item 3, is the authority and says the opposite: **the
   comparison IS apples-to-apples on both axes** — Hercher's `K` counts odd
   members, the same length convention as T1's `n = p+1`, and both bounds rest
   on a verified range — **with one asymmetry, running in Hercher's favour on
   both counts**: his hypothesis is weaker (`3·2⁶⁹` of verified range needed
   against the `2⁷¹` this chain instantiates) *and* his conclusion reaches
   further (`n ≤ 1.375·10¹¹` against `n ≤ 3.5032·10¹⁰`, ratio `3.9258`). The
   drafted sentence's explanatory half already carried the right substance; it
   was the label that had to go, because in his ledger "not apples-to-apples"
   would read as a scope objection to Hercher that we do not have. The clause
   is restated to match the findings, in the ledger text **and in the commit
   message**, which had paraphrased the offer with the same wrong label and
   which enters the shared repo's history (`5481d2d`, tree `bcae6b6`).
   Recorded here with its origin named, the same
   way the round-10 Junction recon's spring-2025 dating slip was recorded as
   ours rather than his (`5611699`): a brief that contradicts a findings file
   loses to the findings file, and this one was caught at review rather than
   before drafting.
8. **`briefs/merle-lean-r10-audit-findings.md` item (iv) carries a wrong
   integral-window figure — noted, not fixed here.** It gives
   `⌊√(2079·2⁷¹/4000)⌋ = 35 031 770 966`. The correct value is
   **`35 031 771 147`**, which is what `briefs/merle-la8-t1-check-findings.md`
   §2(d), this record, and the prepared L-A8 offer (a) all carry, and which
   the main session recomputed independently. Nothing in the prepared commit
   is affected; the main session is repairing the audit record on `main`
   directly. Flagged so the two findings files are not read as disagreeing.
9. **Stack SHAs, not shared-repo SHAs.** Where an offer points at one of his
   blocks it names the **Lean stack** SHA the block's own header carries
   (`89d9efc`, `81054ea`, `4856058`, `b22fafc`), never the shared-repo commit
   SHA — a ledger reader can resolve the former from the entry itself.
10. **Hercher's `q₂₁ + q₂₂` is written as the semiconvergent of `log₂6`.** The
    la8 findings establish that his threshold machinery runs on `(K+L)/K` just
    above `log₂6`, whose denominators are `log₂3`'s; the offer says "the
    distance from `log₂6` to that semiconvergent" so the frame is explicit and
    the reader is not left to infer that the grids coincide by accident.
11. **The Junction repository is nowhere in this commit**, per the brief. It is
    correspondence, not a ledger fact.
12. **Author identity** set repo-local to `macindoe <begemite0.o@gmail.com>`,
    the established co-edit author (the `e53630f`/`641a530` precedent).

## Flags

1. **Pre-push condition (item 0):** **all five** artifact pins in the prepared
   text fail to resolve on public wiki `main`, which is at `b860fe8` at this
   session's `ls-remote`. In full, with the record each serves:
   `8e385b9` (L-A7 verification record), `7cb47cb` (the margin-proof block),
   `bb9e5a7` (the `marginTarget` statement-match), `cde2e5b` (the L-A8 key-turn
   block), `bb9e5a7` again (the T1 statement-match) — four distinct commits.
   **The author's wiki-main push to `5c1faf4` or later (`d9b2715` current) must
   accompany or precede the shared-repo push**, or all five dangle.
2. **Judgment call 6 is closed** — the main session ruled for pinning and the
   `cde2e5b` line is applied; nothing is left open for review here.
3. **Patch line endings, minor.** The archived patch is generated with LF and
   is checked out with CRLF on this machine (`core.autocrlf=true`) — the same
   state as the round-9 archive. `git am` strips the trailing CRs by default
   (`am.keepCr` unset), so it applies cleanly either way; the authoritative
   apply path remains the scratchpad clone.
4. No other flags. No stop-and-hand-back was triggered; the shared HEAD was
   `826970e` at both checks; no discrepancy of digits, SHAs or citations was
   found between the prepared blocks and the four findings records.

## What the main session does next

1. Review is **done** (main session, 2026-07-26): patch verified applying
   clean and tree-identical, counts and both modified lines confirmed, shared
   HEAD re-checked unmoved. Two changes were made at review and are applied —
   judgment call 6 decided in favour of pinning (`cde2e5b` added to the L-A8
   key-turn block) and judgment call 7, offer (c)'s "not apples-to-apples"
   clause corrected against the la8 findings. The commit was regenerated after
   each, plus once more to correct the commit message's paraphrase of offer
   (c); the current one is **`5481d2d`** (tree `bcae6b6`).
2. **Author pushes wiki `main` (≥ `5c1faf4`, i.e. `d9b2715`) so all five pins
   resolve publicly.**
3. On the author's go-ahead: push `5481d2d` from the scratchpad clone
   (`scratchpad/r10/shared`, branch `round10-coedit` → `main`, fast-forward
   over `826970e`) — or `git am` the committed patch onto a fresh clone if the
   scratchpad has been cleaned. If the shared repo has moved past `826970e` by
   then, re-seat first (the round-8 precedent).
4. The round-10 reply draft is a **parallel session** (its own brief in
   `d9b2715`); this session makes no claim on it.
