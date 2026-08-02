# Brief: what the hypothesis supplies about the budget (v3 round 4, blocking finding)

**Round.** Fourth external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `fa9edf5` (= current `main`). The reviewer calls the round-3 revision strong and every earlier concern repaired, and pauses publication for **one** correction. This brief owns it, together with the two smaller corrections in the same neighbourhood.

**This is a design task, not an edit task.** Produce text; change nothing.

**The author has declined to set a default.** Cost both options fully, recommend one, and return the decision. Do not present your recommendation as settled.

**Do not prune.** The reviewer also supplies a pruning plan for the paper; the author has deferred it to a separate pass. Your drop-in text should be as long as it needs to be and no shorter. Length is not your problem this round.

## The blocking finding

The reviewer:

> Literal Hypothesis 5.1 gives convergence of every fixed finite-pattern frequency. This is ordinary genericity on a countable alphabet. It does not imply convergence of the unbounded moment `(1/T_N)Σ_{n<T_N}(m_n + r_n) → 4`. Rare letters whose sizes grow with `N` can be invisible to every fixed pattern frequency while changing that average substantially.
>
> For example, take an otherwise `B`-generic word of length `T`, insert one letter of size `cT` at position `T − √T`, and let the remaining `√T` symbols become `†`. Every fixed pattern still has the correct limiting frequency and the cemetery proportion tends to zero, but the exponent mean changes by `c` and the budget has been exhausted.

Checked against the files by the main session and confirmed at three sites:

- **`aeh.md` L86**, the consistency bullet: "`π_{k,D}` gives `†` no mass, so the hypothesis says the first `T_N` blocks fit inside the budget, which is exactly `E_B[m + r] = 4` in Cesàro form." Zero cemetery mass says the *fraction* of out-of-budget blocks vanishes. It does not say the mean exponent converges.
- **`aeh.md` L88–90**, the two-range table, whose second row reads `4θ < τ < 4.8188… ⟺ θ < 1/β` with the annotation "the divisor `4` is `13.2.1`'s own content".
- **`paper/collatz-reduced-v3.tex` L315–329**, which says AEH supplies `E_B[m+r] = 4` and therefore the `1/β` block ceiling.

**The observation that makes this bite.** `aeh.md` `13.3.2` already declines to draw a drift consequence from AEH, and gives as its reason that equidistribution at each fixed `k` yields no `limsup` on the unbounded `m_+` — a missing uniform-integrability input. That is the same gap, in the same shape. The record deploys the argument against itself in one section and ignores it in another. Whatever you recommend must leave those two sections consistent.

## Where this came from, and why you must read it

Round 3 *introduced* the clock and this conversion. `briefs/v3r3-cut-weighting-findings.md` §7 sets `τ` as primitive and derives `θ = τ/E_B[m+r]`, "with the division named as AEH's own content" — the naming was intended to make the dependence honest and visible rather than hidden. The reviewer's charge is that naming it is not enough, because AEH does not contain it.

Read that section and say plainly whether the naming was ever defensible. If round 3 made an error, name it as an error; if it made a defensible choice that this round overturns on better information, say that instead. Do not smooth over which it was.

## The two options

**Option 1 — the narrow correction (the reviewer's recommendation).** Keep AEH purely distributional:

- retain exponent time as the canonical clock;
- retain `4θ < τ` only as *compatibility with the target `B`-model*, not as something AEH delivers about actual orbits;
- stop saying AEH proves the empirical mean is `4`, or that it converts Inselmann's endpoint into `1/β` blocks per bit;
- replace "all of them within budget" with "all but `o(T_N)` blocks within budget".

**Option 2 — an explicit moment or non-binding-budget clause.** Strengthen AEH so the conversion holds. The reviewer's own objection to this: it "materially strengthens AEH and reintroduces conditional drift consequences". Note what that costs — `13.3.2` refuses a drift consequence on the grounds that it would be *worth nothing*, Inselmann having proved the trajectory statement unconditionally at natural density 1. A conditional consequence that is strictly weaker than a known theorem is not an asset.

For each option state: the exact statement; what becomes of `13.2.3`'s admissibility definition and the two-range table; what the paper's §5 becomes; what is newly claimed and no longer claimed; and whether `13.3.2` stays consistent.

**One asymmetry to check rather than assume.** The base case at `θ < 1/4` bounds the total variation between the joint word law and `B^{⊗n}`, and a total-variation bound transfers *every* event — including `{S_{T_N} ≥ τb}`. So the conversion may be available unconditionally *below* the budget and unavailable *above* it. If that is right, it is the same shape delegate B found in round 3 for Inselmann: the needed statistic is available precisely up to the digit budget and nowhere past. Work out whether it holds; it would make the correction a clean statement about where the conversion lives rather than a retraction.

## The two smaller corrections in the same sections

**(1) The base case omits the cemetery-budget step.** Lemma `13.2.4` does not quantify over `τ`, yet Corollary `13.2.4.1` claims the cemetery-form hypothesis for every admissible `(τ, θ)` with `τ < 1`. The reviewer's missing estimate is `P(S_{T_N} ≥ τb) → 0` for `4θ < τ < 1`, by the joint-word total-variation bound followed by the negative-binomial tail. Note that `13.2.4`(b) already contains this with `J = ⌈(1−η)b⌉` and `η < 1 − 4θ`; the step exists but is not surfaced as the budget clause. Surface it explicitly.

Two index errors in the same lemma:

- **`13.2.4`(a) prints `P_B(S_(n+1) ≥ J)`** where its own proof and the paper's displayed bound use `P_B(S_n ≥ J)`. The good event is `S(W) + 1 ≤ J` on a word of `n` letters, so `S_n` is the natural sharp form. Verify and correct.
- **`13.2.3` calls the gap between the two exponent counts `O(1)`** ("The gap is `O(1)` in a budget of `Θ(log N)`"). The two counts differ by one letter at each end, and letters are unbounded geometrics, so the gap is `O_P(1)` with geometric tails — negligible against `log N`, but not deterministic. State it correctly.

**(2) The Inselmann ceiling is overstated.** `aeh.md` L84 asserts "No `τ ≥ 4.8188…` is protected, and this is sharp rather than a gap in technique… Above the ceiling there is no orbit left to sample." The reviewer:

> Inselmann proves a simultaneous trajectory envelope up to the endpoint and descent to `m^ε` there; the strict protection claim for `τ < 4.8188…` follows. The cited theorem does not by itself prove the record's unconditional statement about every `τ` at or beyond that endpoint, particularly at reduced-block exits.

The paper uses only the valid strict inequality, so this is principally an `aeh.md` correction. Establish what the source supports and restate the bullet to exactly that. `briefs/v3r3-inselmann-horizon-findings.md` contains a delegate's direct reading of the paper — use it, but the claim under repair is *this repository's*, not Inselmann's.

## Read before deciding

Current text, not a findings file's quotation of it — much of §13 was rewritten in round 3 and several claims circulating in the round-3 findings are already stale:

- `aeh.md` `13.2` entire, `13.2.1`–`13.2.5` including `13.2.3` (the clock) and `13.2.4` with its corollary; `13.3.1`–`13.3.3`; `13.6.3`(i) and (v); `13.6.4`.
- `paper/collatz-reduced-v3.tex` L248–276 (the hypothesis) and L279–340 (the base case and consequences).
- `publication.md`, wherever it repeats the conversion or the ceiling.
- `briefs/v3r3-cut-weighting-findings.md` §7 and §11; `briefs/v3r3-inselmann-horizon-findings.md` §2–§3; `briefs/v3r3-basecase-density-findings.md` for what the lemma actually proves.

## Deliverable

Write **only** `briefs/v3r4-clock-findings.md`:

1. both options costed, with a recommendation and its reasoning;
2. the verdict on round 3's "named as AEH's own content" framing — error or superseded choice;
3. the asymmetry question answered: is the conversion a theorem below the budget?
4. **exact drop-in text for the recommended option** — Markdown for `aeh.md` L84, L86, L88–90, `13.2.3`'s gap sentence, `13.2.4`(a), and the new budget step; LaTeX for the paper's L315–329 and anything else that moves;
5. the same at lower resolution for the rejected option, sufficient to switch without another round;
6. the consequence trace, as a plain list: what survives verbatim, restated, or fails;
7. anything you could not settle, named as an open question.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file.
- No `git` write operations of any kind. You are on `main` at `fa9edf5`; do not branch or commit.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not renumber any monolith anchor; append if you need a new one.
- No change logs or dated journals in anything destined for a tracked page.
- Every number and section reference verified against the file, not recalled.
- The paper is **unpublished**; statements may be restated in place. No erratum framing.
- Do not attempt to prove AEH. Do not prune. Do not touch the `13.6.4` union-bound wording or the Appendix A pin — both are settled corrections for the apply wave.
