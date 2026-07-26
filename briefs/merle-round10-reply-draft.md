# Round-10 reply — business paragraphs (DRAFT)

Drafted per `briefs/merle-round10-reply-brief.md` (commit `d9b2715`), 2026-07-26.
Branch `merle-round10-reply`, base: main `d9b2715` (the worktree was cut at the stale
session-start HEAD `b860fe8` and was rebased onto `d9b2715`, which carries the brief and
all five round-10 findings files, before anything below was written).

Conventions as rounds 7–9. **Business paragraphs only:** the personal opening and closing,
and anything answering his personal paragraphs — the lycée, the year, the protocol born
"one rule per wound" — are the author's own and are not drafted here. They are marked as
placeholders below, for the author to write, fold in, reorder or cut. Sending stays with
the author; nothing here has been sent and nothing has been pushed.

**Verification.** Every number, SHA, section reference and citation below was checked at
its named place in the five round-10 records as it was drafted —
`briefs/merle-la7-close-check-findings.md`, `briefs/margin-inequality-proof-findings.md`,
`briefs/merle-la8-t1-check-findings.md`, `briefs/merle-lean-r10-audit-findings.md`,
`briefs/junction-repo-recon-findings.md` — and the load-bearing arithmetic was
additionally recomputed from scratch in this session before it was written down
(the constants `c_gen`, `1 + log₂β`, `2log₂β − Λ`, `γ`, `x*`, the `t/s` window, the
continued fraction of `log₂3` and its convergent denominators `q₀…q₂₄`, the exact and
integral Legendre windows, the discharge criterion and its tightest margin, the `−17`
product identity, the crude-route extrema under both constants, and the Corollary-B′
finite table). All agreed with the findings.

**Four things that could not be verified, or that diverge from the brief — flagged here,
not buried:**

1. *The Junction repository could not be reached at all* (recon findings). Every point of
   his self-audit is "not found", not "denied". The reply asks for the location and claims
   nothing else — see the paragraph marked accordingly.
2. *Kernel claims are read-not-built.* There is no Lean toolchain on this side. The Lean
   audit verifies statements, instantiations and committed axiom logs; kernel-3 /
   `[propext]` / no-user-axiom claims rest on his logs and his hardened protocol. The draft
   says so.
3. *The brief says the "3.9× further" Hercher comparison "is not apples-to-apples". The
   findings say the opposite* (`briefs/merle-la8-t1-check-findings.md`, Hercher
   adjudication item 3, and §(g)): the comparison **is** apples-to-apples on both axes —
   his `K` counts odd members, the same convention as `n = p+1` — and the one asymmetry
   runs in *his* favour, since Corollary 29 needs only `X₀ ≥ 3·2^69` of verified range
   against the `2^71` T1 instantiates. The draft follows the findings, not the brief. What
   genuinely needs correcting is the *label* (`q₂₃`, not `q₂₂`), the word "exactly" (the
   underlying threshold, not the printed decimal), and the naming of the Cor. 29 condition.
4. *One internal error in our own records, corrected here, not to be sent.*
   `briefs/merle-lean-r10-audit-findings.md` item (iv) gives the integral window as
   `⌊√(2079·2^71/4000)⌋ = 35 031 770 966`. The correct value is **35 031 771 147** — the
   figure `briefs/merle-la8-t1-check-findings.md` §(d) gives, recomputed independently
   twice this session (`4000·35031771147² ≤ 2079·2^71 < 4000·35031771148²`). Nothing
   depends on it: the 22-convergent count is identical under either number and under the
   exact window. The draft carries `35031771147`. Worth one line back to the audit record.

**Both bracketed fields are now filled — resolved at review, 2026-07-26.** The round-10
co-edit was prepared in a parallel session and pushed on the author's go-ahead: shared-repo
HEAD is now **`c966875`**, over his `826970e` (verified unmoved immediately before the push,
and the result confirmed by an independent fresh clone; tree `bcae6b6`, `LEDGER.md` only,
49 insertions / 2 deletions). The prepared commit was `5481d2d` in the preparing session's
clone — same tree, restamped by a fresh application, so `c966875` is the SHA to cite. The
wiki-`main` pin is **`ae402b9`**, pushed publicly by the author first; all four artifact
commits (`8e385b9`, `7cb47cb`, `bb9e5a7`, `cde2e5b`) were verified to resolve on public
`main` before the shared-repo push went out.

---

> **[PLACEHOLDER — personal opening: the author's own. Nothing below answers the first
> letter's personal paragraphs; that reply is his to write.]**

---

**L-A7 is closed at two keys.** Your block 1 accepts all four clauses as stated —
Rhin 1987 / Simons–de Weger 2005, the `n ≈ 2233` headline, `C₀ ≈ 2.06`, the `< 1.94`
repair bits — which is exactly the condition our round-9 key was conditional on, so the
DRAFT marking is date-stamped and the entry stands at two keys, scoped as the entry
itself states it: a bound on the *expectation*, with the model→certainty step still the
×2×3 gap. The `≈ 550` withdrawal we take as written; our own chain re-derives `372`
per-scale and `440` cumulative, the same two readings, from our own code.

The four new blocks are verified our side, and everything matched: 66 recorded checks,
0 failures, fresh code, your scripts read for operational definitions only and never run.
Digit by digit — south floor `ε + ε′ = 1` with 0 violations to `n ≤ 200 000` and minimum
`9.3·10⁻⁸` at `n = 190537`; margin slack `2.8414` at `n = 2`; the entropy route dominating
to `n = 200 000` with minimum `1.6647` at `n = 16266` and maximum `2.10492` at
`n = 190537`; `c(12/7) = 0.0793165`, a loss of `2.07·10⁻⁶` against `c_gen`; the admissible
window `[5.727444, 5.747075]` re-derived from its two constraints, with `s = 15, t = 86`
confirmed the **unique** smallest admissible pair (`s = 1..14` exhausted in exact integers
— every one of those windows is empty, `t_A = t_a + 1` at each); atom margins `0.088` and
`0.327` bits, `atom_D` with `324.7`; `key_core` exact on all 1 137 hub-admissible `(k, j)`
with `k ≤ 60`, and failing at `(0,5)` just past the hub, so the Diophantine hypothesis is
load-bearing rather than decorative; both of the errors your machine caught confirmed
(the uncorrected window really does admit `s = 1, t = 6`, and the exact integer check
really does kill it on the `a` side: `141264177173406 > 106993205379072`; and
`3^86 ≤ 4^86 = 2^172` really is sufficient where you use it, `101 + 172 = 273 ≤ 562`);
and all six numbers of the threshold recompute — `1596 → 1655` per-scale, `1661 → 1722`
cumulative, with their two exhibited `C₀`s — reproduced, plus the `2233` reconciliation,
which is a different family of number from those and not in competition with them (fitted
versus derived constant, `log₂n` versus `log₂K₀` as the exponent carrier, "< 1 ticket"
versus "tail `< 5.2·10⁻⁴`").

**Two of your results are stronger than you reported them, and the entry should say so.**
The south floor is not a numerical observation with 0 violations: it is a theorem, in one
line. `nL` is irrational for every `n ≥ 1`, so `⌈nL⌉ = ⌊nL⌋ + 1`, so
`ε_n + ε′_n = (⌈nL⌉ − nL) + (nL − ⌊nL⌋) = 1` identically — hence at most one shore can be
small, ever, and the other is `≥ 1/2` for free. Nothing is being verified there; it is an
identity. Likewise `γ·log₂3 = c_gen` is not an error of `0.0` at fifty digits: it is an
exact algebraic identity. Expanding the binary entropy at `1/β`,
`h(1/β) = log₂β − ((β−1)/β)·log₂(β−1)`, so
`β(1 − h(1/β)) = β − β log₂β + (β−1) log₂(β−1)` — which is the closed form of `c_gen`
term for term. Since `γ = 1 − h(1/β)`, the product is `c_gen` by algebra, and the fifty
zeros are a consequence, not the evidence. Both restatements are offered in the co-edit;
your own wording is equally welcome.

Two scope clauses and one flat line, none of them a dispute. The negative control that
"fails at 241 scales" inherits its artifact's `x = 1709/1000`; at the entry's own `x = 12/7`
the count is 256 (`n = 1..3000` either way) — one clause pins which. The "minimum slack
1.700 bits" is the slack of the *provable route bound*, which is the quantity that matters
for the proof; the true margin's slack against `n/13` is larger (`1.923` at `n = 1`) — one
clause distinguishes them. And `OUT_REQ-MATH-043.txt` is committed without a generator
script, alone among the five blocks' artifacts; all six of its numbers reproduce for us
from the REQ-035 method run at exponent 13.3 under both constants, so this is an offer to
commit the script, not a doubt about the numbers.

---

**The margin inequality: proved our side, for all `n ≥ 1`, at the true `c_gen`.** This
discharges the offer we made in round 9 and you accepted.

> **Theorem A.** For every `n ≥ 1`, at the tuned north cell `K = ⌈n·log₂3⌉`,
> `margin(n) = K − log₂ C(K−2, n−1) > c_gen·n + 1 + log₂(log₂3)`,
> with `c_gen = β(1 − h(1/β))` **exactly** and `1 + log₂β = 1.66444870745388938…`.

So `margin(n) ≥ c_gen·n` for every `n ≥ 1` with a uniform surplus above `1.664` bits. The
proof is elementary and cites nothing: the textbook entropy bound
`C(m,k) ≤ 2^{m·h(k/m)}`, then concavity of `h` taken as the tangent line **at `p₀ = 1/β`**,
then two lines of algebra. There is a refinement carrying Robbins —

> **Theorem B′.** For every `n ≥ 2`,
> `margin(n) > c_gen·n + (1/2)·log₂ n + 2.12171397510694569916…`

— and the scope is wider than the tuned cell:

> **Theorem A′.** For every `n ≥ 2` and every integer `K` with
> `n+2 ≤ K ≤ nβ + 4.79982787…`, `K − log₂ C(K−2, n−1) ≥ c_gen·n`; and for `K ≤ ⌈nβ⌉` —
> the tuned north cell **and the entire south shore** — the full Theorem-A surplus holds
> verbatim.

That last one is worth a sentence in its own right: it closes the south-shore half of the
coverage gap that our Lean audit recorded against `marginTarget`, which bounds the count
at the tuned north cell and nothing else. The far-north cells (beyond `nβ + 4.7998`) stay
open to this route — there it gives only `margin > 2` — and in the L-A7 accounting those
cells are handled by the best-cell → both-shore repair anyway, not by this bound.

**And now the part we owe you, because you acted on it.** *Our Stirling warning was wrong
at the premise.* We wrote that the crude entropy route leaves an asymptotically constant
margin because it discards the `(1/2)log₂n` factor, and that the Stirling term would
therefore have to be handled with an explicit bound rather than absorbed, since there were
under two bits of room. The mechanism in that sentence is right; the reading of it is not.
A constant surplus is not a shortage. The constant is `1 + log₂β = 1.6644487…`, provably
positive and uniform in `n` — so the crude bound closes the inequality on its own, with no
Stirling, no citation and no `n₀`. Nor does the perturbation step need a Taylor remainder:
concavity puts `h` below its tangent at `1/β` in one line, exactly, with no remainder term
and no interval hypothesis. Which is why "under two bits of room" turned out not to be a
problem at all — the only step in the chain that spends anything material is the entropy
bound itself (minimum spend `1.0` bit, at `n = 2`), while the concavity step spends
`O(1/n)`. Robbins, carried out, turns out to be a **credit** rather than a debt, exactly as
one would hope: the `√(2πm)` in the numerator is outweighed by the two `√(2πk)`, `√(2πj)`
in the denominator, and it upgrades the surplus from `1.664` to `(1/2)log₂n + 2.122`. Worth
having; not the proof.

You restructured your whole route to avoid Stirling **on the strength of that warning**.
The route you built is your own and it is good: the elementary family
`C(m,k)·x^k ≤ (1+x)^m` at the rational `x = 12/7`, with `19 = 12 + 7` turning the statement
into *one summand ≤ the sum*, is a genuinely independent second proof of the same
inequality, and it is the one that reaches the kernel — which ours does not. But the reason
for the detour was our error, and it belongs on the record as ours, not as a shared
puzzle that happened to resolve.

The two routes meet at one point, which is worth saying plainly. Your `x = 12/7 = 1.714285…`
sits next to `x* = 1/(β−1) = 1.70951129135…`; in our chain that same `x*` appears as the
*slope of the tangent line*, `h′(1/β) = log₂(β−1) = −log₂x*`. That is exactly why your
constant lands `2.07·10⁻⁶` below `c_gen` — a nearby rational in place of the optimal
slope — and the further drop to `1/13` is the rounding to a safe rational, not the tangent
choice. Two routes, one optimum, described in two vocabularies. The structural fact behind
Theorem A is that at `p₀ = 1/β` the linear-in-`n` term cancels *identically* against
`c_gen`; at any other tangent point the slope is strictly below `c_gen` and the bound
drifts negative (checked as a negative control: at `p₀ = 0.60` it goes under `c_gen·n` at
`n = 383`).

Two arithmetic offers fall out of the proof, both small.

*(i) A closed form for your `[1.66, 2.10]` interval.* The bound gives the crude-route
surplus as lying in `(1 + log₂β, 2log₂β − Λ]` up to an `O(1/n)` concavity gap, with
`Λ = log₂(β−1)` — that is, `(1.66444871, 2.10248137]`. The lower end is the infimum,
approached as `θ(n) = ⌈nβ⌉ − nβ → 1⁻`; the interval is not an empirical range but a proved
one, and both ends are closed forms.

*(ii) A flat correction, and your figures are right for the constant you used.* The entry's
crude-route figures — `1.6647` at `n = 16266`, `2.10492` at `n = 190537` — are what one
gets from `c_gen` as the **7-digit decimal `0.0793186`**; we reproduce both of them
digit-exactly under that decimal (`1.664689`, `2.104916`). Under the exact
`β(1 − h(1/β)) = 0.07931861277485539…` the sweep gives minimum `1.664453` at `n = 111202`
and maximum `2.102482` at `n = 190537`; the truncation is worth `0.0024` bits by
`n = 190537`, which is enough to move the argmin. Nothing about the conclusion changes.
It is worth one clause only because the true minimum `1.664453…` is precisely the number
that matches the proved floor `1 + log₂β = 1.6644487…` — and that coincidence is the whole
content of Theorem A's constant being sharp.

The record is `briefs/margin-inequality-proof-findings.md` with
`experiments/margin_inequality_proof_check.py`; every link of the chain is checked
separately so a broken one cannot hide behind slack elsewhere, with six negative controls,
and Theorem A′ checked over 107 444 cells.

---

**L-A8: our key turns on the mathematics, and the kernel claims sit with the audit.** Every
link was derived in our own words in a clean room and confirmed — 62 recorded checks, 0
failures, fresh code that imports nothing from your repositories. The cycle product
identity is exact on all four real cycles, both shores (`−17`:
`∏(3x+1) = −403123745024000 = 2^11 · (−196837766125)`, `K = 11`); the survivor bound with
its per-factor equivalence `(3x+1)(3X) ≤ 3x(3X+1) ⟺ X ≤ x`; the seam bound; the log gap
with `δ = 4.0734·10⁻²²`. Your factor-2 correction is confirmed exactly, and the withdrawn
`4.955·10^10` is precisely the missing-factor-2 artifact — it is the corrected window times
`√2`, to the digit. There are 22 convergents in the window; the discharge criterion passes
at all 22, tightest `5.17×` at `q = 6586818670`, against an exact test of `5.44×`, so the
integer form is conservative exactly as you say it is by design; the non-vacuity canary
fails at the next convergent, which is why the window ends where it does; and each of the
four real cycles exits T1's scope exactly where the hypotheses say it should — the trivial
cycle by `x_min` alone, the three negative ones by the positive-shore hypothesis before any
size question arises.

One small tightening, offered rather than flagged. "`n` is one of the 22 convergent
denominators" is, a priori, "`n` is a **multiple** of one" — `quotient_is_convergent_gen`
concludes about the reduced `K/n`. It closes with no extra work: if `n = t·q_m`, then
`|K − nL| = t·θ_m` exactly and `nδ = t·q_m·δ`, so the `t` cancels and the same
per-convergent test kills every multiple at once. The same 22 checks therefore cover all
in-window `n`. Both of the glue facts you name — that `convPairs` is the in-window
denominator list, and the classical `θ_j > 1/(q_j + q_{j+1})` — are derived in our findings,
offered as the ledger's statement of exactly what "glue" means.

**Both of the round's discrepancies resolve without fault on either side.** The two window
figures are the *exact* and the *integral* windows and both are right: `3.5035·10^10` is
`√(1/2δ) = 35 035 491 004`, the definition in the `9428663`/`89d9efc` stacks and
REQ-MATH-054; `3.5032·10^10` is the largest solution of `4000n² ≤ 2079·2^71`, namely
`35 031 771 147`, which is what the kernel discharge actually runs over and therefore the
right figure for the closure statement. The integral window sits strictly inside the exact
one — a loss of `0.011%`, conservative, the right direction. The definition simply moved
mid-entry, at the point where the Legendre step was formalized with the threshold
abstracted, without a naming clause; one clause fixes it. And the `q₂₁` collision is an
indexing convention, with the substance right in both stacks. Under the indexing that makes
`89d9efc` and your OUT-054/056 correct — `q₀ = q₁ = 1`, both counted —
`q₂₁ = 6 586 818 670`, `q₂₂ = 65 470 613 321`, `q₂₃ = 137 528 045 312`, so the `0905b00`
block's two labels are each shifted down by one. The mathematics there is untouched: the
first scale the seam chain cannot exclude really is `65 470 613 321`. The origin is visible
in your own artifacts — `OUT_REQ-MATH-053.txt` carries two tables whose indexings differ by
one, while its own Hercher line uses the standard convention.

**The Hercher observation survives, with a correction, and it is the better for it.** Read
directly: Corollary 29 says that if `X₀ ≥ 1536·2^60 = 3·2^69`, every nontrivial cycle
contains at least `K > 1.375·10^11` odd numbers (*There are no Collatz m-cycles with
m ≤ 91*, J. Integer Sequences **26** (2023), Article 23.3.5; arXiv:2201.00406v3). The paper
prints only the display value `1.375·10^11 = 137 500 000 000`, which is **not** equal to
`q₂₃ = 137 528 045 312` — the printed figure is a safe rounding down, ratio `1.000204`, and
the exact integer appears nowhere in the paper. But the *underlying* threshold is `q₂₃`
exactly, and we verified that two independent ways in our own arithmetic: his Table-1
all-`m` row `K > 7.20·10^10` is the semiconvergent denominator
`q₂₁ + q₂₂ = 72 057 431 991` exactly, and his Remark-28 interval width `1.1032·10⁻²²` is
the distance from `log₂6` to that same semiconvergent (we compute `1.1033·10⁻²²`; the fifth
digit differs from his print, immaterial). Crossing that width forces the denominator to
the next rung, which is `q₂₃`. So the frame-prediction point — that these thresholds live
on the convergent grid — is genuinely supported, and by more than one instance. What needs
restating is the wording around it: the label is `q₂₃`, not `q₂₂`; "exactly" means the
underlying threshold rather than the printed decimal; and Cor. 29 is conditional on
`X₀ ≥ 3·2^69`, a condition Barina's `2^71` meets, so the bound stands today but the
condition should be named.

On the comparison itself we read it the other way from how one might expect. It **is**
apples-to-apples on both axes — his `K` counts odd members, the same length convention as
your `n = p+1`, and the verification condition is met — and the one asymmetry runs in
*his* favour: Cor. 29 needs only `3·2^69` of verified range, strictly less than the `2^71`
your chain instantiates. So "3.9× further, but on paper" is if anything understated on
hypotheses (the ratio against the integral window is `3.926`). None of which touches T1's
actual differential value, which is the machine-checkable chain and the shape rigidity —
`K` pinned per scale — and not range, exactly as your own honest-scope paragraphs already
say.

**The kernel claims are deferred, and here is what "deferred" means precisely.** There is
no Lean toolchain on this side, so our audit is read-not-built: what it verifies is that
the Lean *statements* say what the ledger says they say, that the committed axiom logs
match the axiom claims, that every statement is *true as stated* when instantiated at
hundreds to thousands of exact-integer points including the edges, and that the one
genuinely finite ingredient is independently recomputable. The kernel-3 / `[propext]` /
no-user-axiom claims rest on your committed logs and your now four-way-hardened protocol —
the same posture as ContentDescent and L-A1. On that basis: Lean HEAD `5c9b663`, the graph
from `97b57d7` linear over 20 commits, and no drift in any of the three previously audited
files; 15 930 exact checks, 0 failures. `marginTarget` **does** encode `margin(n) ≥ n/13`
exactly at the tuned north cell — its hypotheses admit exactly one `K` per `n` (checked
against `K₀ ± 1` for `n = 1..300`), `C(K−2, n−1)` is our word count by Vandermonde (checked
at all 144 cells `n, S ≤ 12`), the unfolding is `K − log₂#words ≥ n/13`, and outside the
hypothesis range the conclusion is genuinely false (at `(n,K) = (100,200)`), so the
hypotheses are load-bearing. And `convPairs` is independently confirmed: the 22 pairs are
exactly `(q_j, q_{j+1})` for `j = 0..21`, the denominators at or below the integral window,
computed here from a continued fraction of `log₂3` derived from scratch at two precisions.
That is the first of your two named glue facts, now two-key at the level of independent
computation.

**One mismatch of substance, and it is a formalization gap rather than a mathematical one.**
`ceiling_upper` proves the **upper half only**: the Lean statement concludes
`2^K < 2·3^(p+1)`, while the ledger block, the file's own docstring and the `41fa4f8`
commit message all state both bounds. The lower half `3^(p+1) < 2^K` is nowhere proved in
the file — it enters downstream, in `ratio_bound_at_barina`, `log_gap_gen` and
`quotient_is_convergent_gen`, as the hypothesis `hceil`. Mathematically it is one line from
`cycle_prod_identity` (`∏(3xᵢ+1) > ∏3xᵢ` gives `2^K·∏x > 3^(p+1)·∏x` for positive
elements), so nothing is in doubt; but as committed, "`K` is pinned to `⌈(p+1)·log₂3⌉`" is
half a kernel theorem plus an unproved elementary hypothesis threaded through the rest of
the chain. A one-lemma `ceiling_lower` would close it and discharge `hceil` everywhere it
appears; restating the prose as upper-half-plus-hypothesis would do equally well. Your
choice, and it is the only thing standing between the L-A8 "K pinned" sentence and a
two-key marking on the kernel side.

Hygiene, not substance, listed once and then dropped: the `DeficitLemma` axiom log covers
8 of the stated 10 — `key_shifted` and `key15` have no `#print axioms` probe, so your
protocol's fourth check is unmet for those two, though `margin_core`'s own probe
transitively bounds them; no committed log carries any `LegendreApprox` entry although
`T1Structure_axioms.txt`'s header names the file (read as "0 *user* axioms" the claim is
consistent with the file as read, which shows 0 `sorry`, 0 `native_decide`, 0 `axiom`);
`OUT_REQ-MATH-055/056` are committed without their scripts, and `OUT-052/053` carry
tracebacks from crashed first runs ahead of the good output; the `DeficitLemma` SCOPE
header still says `MarginTarget` is unproved, 200 lines above the place it is proved; and
"best approximation verified exhaustively to `q₁₀ = 190537`" matches neither the committed
sweep bound (`n < 31867`) nor its own indexing (`190537 = q₁₃`) — we re-verified the
property exhaustively to `n < 190537`, so the fact stands either way.

---

**One question, and it is only a question.** We could not check your self-audit, because we
could not find the repository. Your handle shows three public repositories —
`collatz-conditional-cycles`, `one-obstruction-three-faces-lean`,
`paper-trading-dashboard` — no organizations, and across every ref of
`collatz-conditional-cycles` (ten branches, seven tags) there is no `AUDIT_V9`, no
`STATUS.md` and no `*Legendre*` file; a code search finds no `AUDIT_V9` under your
ownership. So every point of your description is recorded on our side as *not found*, not
as confirmed and not as denied. A set-aside preprint repository may perfectly well be
private, or under an account nothing we can see links to, or simply never pushed — nothing
we found contradicts your account. So: where does it live? That is the whole of the ask.

Two notes so that it stays that size. The one open question we had about the deficit
lemma's provenance is already settled without access: REQ-MATH-037's own conversion
`S ~ n·log₂3` only works if the preprint's `S` is our `K`, since `S = K − n` would carry
`γ·(β−1) = 0.02928` per unit `n` rather than `c_gen = 0.0793186` — and your committed
output records the difference as exactly `0.0`. It is the *units* that decide it, not the
inequality, which does not discriminate (the `S = K − n` reading is strictly weaker and
also holds). So the provenance is not blocked on the repository. The second note does bear
on T1: `LegendreApprox.lean` is imported by the T1 chain and its home is unconfirmed. It is
not in `collatz-conditional-cycles` in any ref, and the only provenance readable anywhere
is your `da2c8db` commit message and the shared ledger, neither of which names a URL. The
file itself reads clean — 0 `sorry`, 0 `native_decide`, 0 `axiom` declarations,
byte-unchanged since `da2c8db` — but the T1 formalization rests on it, so a pointer to
where it lives is worth one line more than the rest of the ask. For the record: everything
above came from read-only clones and read-only API calls; no fork, issue, comment, star or
watch was made against anything of yours.

**The retraction.** You reported it before we could have found it, and our audit confirms
the record is clean: the full `RETRACTED` note is present at `7d46474`, superseded at
`4856058` by the one-line reference inside the successful attempt's section comment, and
nothing at HEAD depends on the withdrawn theorem — the non-general
`quotient_is_convergent` does not exist in the file at `5c9b663`, and
`quotient_is_convergent_gen` is a fresh proof with the threshold abstracted. One flat note
in case permanence was the intent: the note's own text said it stays as the record, and at
HEAD the standalone form no longer does; the history and the ledger block carry it.

**The joint note: agreed, and agreed with your framing** — as honest about what it does not
do as about what it does — and with no schedule on either side. We are deliberately not
proposing an outline or a section list here; that is its own conversation, and it should
start when it starts.

**Where everything lives.** Wiki `main` stands at `ae402b9`, public — every artifact pinned
below was verified to resolve there before the co-edit went out. The five round-10 records are
`briefs/merle-la7-close-check-findings.md` (the L-A7 closure and the four new blocks),
`briefs/margin-inequality-proof-findings.md` (our proof), `briefs/merle-la8-t1-check-findings.md`
(the clean-room L-A8 chain), `briefs/merle-lean-r10-audit-findings.md` (the read-not-built
statement match on `DeficitLemma` and `T1Structure`) and `briefs/junction-repo-recon-findings.md`
(the recon, and the `S`-is-`K` settlement). The fresh verification code is
`experiments/merle_la7_close_check.py`, `experiments/margin_inequality_proof_check.py`,
`experiments/merle_la8_t1_check.py`, `experiments/merle_lean_r10_audit.py` and
`experiments/junction_deficit_units_check.py`, each with its output committed alongside.
The round-10 co-edit — the L-A7 date-stamp and verification record with its three offers,
our margin proof offered as the second proof at the true constant, the L-A8 key turned on
the mathematics with the kernel claims scoped out, and the `ceiling_upper` repair — is
pushed at `c966875`, over your `826970e`, `LEDGER.md` only, your prose untouched throughout.

No new claims ride along with any of this. Everything cited above sits at its named place
in the five findings records, and the two bracketed fields are the only values not yet on
file.

---

> **[PLACEHOLDER — personal closing: the author's own.]**
