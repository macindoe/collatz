# Brief: one object named AEH (v3 round 3, both blocking findings)

**Round.** Third external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `dc61306` (= current `main`). The round-2 ensemble repair held: the reviewer confirms the sample now grows with the sampling scale and the hypothesis is no longer empty on convergent orbits. Five findings replace it, two blocking. **This brief owns both blockers, because they are one defect: the repository currently contains several non-equivalent objects under the name "AEH."**

**This is a design task, not an edit task.** Produce text; change nothing.

**The author has explicitly declined to set a default.** Round 2's brief pre-selected the ensemble form and asked for deviation-with-argument. Not this time. You are to argue the choice out, cost both options fully, recommend one, and return the decision to the author at review. Do not present a single option as settled.

## Blocking finding 1: the literal hypothesis is not the claimed genericity hypothesis

The reviewer:

> Hypothesis 13.2.1, like paper Hypothesis 5.1, asks only for the empirical distribution of individual window states. Bernoulli genericity requires the correct frequencies for every finite pattern of consecutive states or letters.
>
> The repository itself recognizes this in §13.6.4, qualifier q1: the literal hypothesis is only the (L=1) case, and its converse to genericity is obstructed. But the status header, `itinerary.md`, and §13.6's opening still call the relationship an equivalence.
>
> That is a direct contradiction. Choose one: strengthen AEH to quantify over all finite L-block distributions, so that "Bernoulli genericity" is correct; or retain the present single-visit hypothesis, which is enough for the ledger and the 1/3 rate, but call the process/genericity form a strictly stronger hypothesis. I favour the first because it gives AEH one clean symbolic meaning.

This is correct as a matter of fact. The three sites that say "equivalence" are `aeh.md` L2 (status header, "symbolic form NAMED and PROVED as an equivalence"), `aeh.md` L71 (§13.6 opening, "here upgraded to a proved, named equivalence"), and `itinerary.md` L73 ("an equivalence named and proved at aeh.md `13.6`"). The site that says otherwise is `aeh.md` L125, qualifier (q1): "Hypothesis `13.2.1` as literally stated is the `L = 1` case … the converse from the literal single-visit form is **obstructed, precisely**". Both readings are in the record simultaneously. Per `AGENTS.md`, a page's status claims must match what the page proves; this is a defect of exactly the genre the wiki exists to prevent.

Note what is *not* in dispute: the (⇐) direction and the process-form equivalence are at theorem grade, and (q1) states the obstruction correctly and for the right reason (the absorption sequence is `2`-adically invisible). Nothing below asks you to reopen the mathematics of 13.6.4. The defect is that the hypothesis being *named* and the hypothesis being *stated* are different statements.

## Blocking finding 2: "depth-`k` window" denotes three different spaces

| Location | Object |
|---|---|
| `paper/collatz-reduced-v3.tex` L159–161 (Thm `thm:onestep`) | Variable-depth residues **plus exact, unbounded labels** `(s,σ,a_+)` |
| `aeh.md` L20 (§13.2) | `(ω mod 2^{k+2}, min(d, D_k))` plus undefined "validity data", asserted to be a finite alphabet |
| `aeh.md` §13.6 (L113–121) | Labelled consecutive-window process reconstructed from two-sided letter windows |

The reviewer's objection is dilemmatic and, as far as this brief can tell, sound: *if "validity data" includes exact `(s, σ, a_+)`, the alphabet is not finite; if it does not, it is not the Theorem 3.8 window and does not carry the stated trichotomy.* §13.2 asserts the cap "does one job, keeping the window alphabet finite" — but `σ` and `a_+` are unbounded, and §13.6.3(iii) (L98) retro-reads "validity data" as exactly those labels: "with its stratum labels `(s, σ, a_+)` per stage4.md `11.8.7.6`, the reading of `13.2`'s 'validity data'". So the finiteness claim and the label content are in direct tension on the same page.

Two further gaps in the same sentence, both real:

- **`π_k` silently depends on `D_k`.** The window state carries `min(d, D_k)`; its law is therefore a pushforward that depends on the cap, but the law is written `π_k` throughout.
- **The norm is never specified.** `‖ν_{k,N}(x) − π_k‖` appears at `aeh.md` L30 and `paper` L253 with no definition anywhere in the repository. (Grepped: total variation appears once, at `aeh.md` L34, in the base-case bound, and is never tied to this norm.)

The reviewer's prescription: *define one explicit observable `W_{k,D}`, write `π_{k,D}` for its law, specify total variation; the labelled Theorem 3.8 window can remain a separate, countable object.*

**`D_k` itself is never defined in the repository.** This is not a new discovery — it is round 2's own unsettled item 5 (`briefs/v3r2-aeh-formulation-findings.md` L352): "`13.2` writes the window state as `(ω mod 2^(k+2), min(d, D_k))` and no section fixes `D_k`. Out of scope here, not renamed, but it is a genuine gap in the definition the hypothesis quantifies over." It is in scope now.

## The third input: which probability space the stationary law lives on

The reviewer raises this as a Major rather than a blocker, but it belongs to you because it determines what `π_{k,D}` *is*:

> The Bernoulli identification in §13.6.2 is one-sided: a 2-adic point determines its future letter word. But absorption and depth require letters to the *left* of the current time — the 3-adic past-limit. That past-limit belongs naturally to the two-sided Bernoulli extension. Thus §13.6.3(v)'s phrase "under Haar-odd (equivalently B)" is too compressed. The stationary labelled law should be defined as the pushforward of a two-sided law `B̂`. Actual integer segments approach it away from their initial boundary; they do not possess an exact infinite past at their first visit. This does not invalidate the computed depth marginal. It repairs the probability space on which it is exact.

Check this against the page rather than accepting it: §13.6.3(iii) (L98) does derive `a_{n+1}` from letters `n−W, …, n−1` — the past, explicitly — while §13.6.2 (L79–86) establishes a bijection onto the **one-sided** full shift `{(m,r)}^N`. §13.6.5 (L130) already reaches for the past-limit `y_3` (itinerary.md `14.15.3.3`). So the objects a two-sided extension would formalize are already in use.

The reviewer states the depth marginal values are unaffected. **Verify that; do not assume it.** If `P(a=0) = 2/3`, `P(a=1) = 19/63`, `P(a≥2) = 2/63` or the derived `P(d=·)` move under a two-sided formulation, that is a finding of the first importance and must be reported unhedged, because the Tao attribution at §13.6.5 and the paper's §5 both rest on them.

Note also the boundary point, which bears directly on blocking finding 1: an integer orbit segment has **no** infinite past at its first visit. Whatever formulation you recommend must say what happens at the start of the segment rather than leaving it implicit.

## What the reviewer recommends, stated so you can argue against it

> Formulate AEH first in letter coordinates: for every finite letter word `u`, the empirical frequency of `u` in the first `T_N = ⌈θ log₂ N⌉` bulk blocks of a uniformly sampled odd `x ∈ [N, 2N)` converges in probability to `B[u]`. Then define the stationary labelled window process as the pushforward of the two-sided `B̂`; derive `π_{k,D}` and all finite window-block laws as corollaries; and distinguish the within-state product law from temporal independence — the labelled window process is **not** `π_{k,D}^{⊗L}`.

That last clause is worth its own attention: nothing in the current record states it, and a reader could easily take the product law of 13.6.3(v) for temporal independence. Whichever formulation you recommend, say plainly whether the record currently invites that misreading.

## Read before deciding

- `aeh.md` §13 entire. Especially L2 (status header), L18–36 (§13.2 and the hypothesis), L38–44 (§13.3's consequences), L46–53 (§13.4 calibration protocol), L55–67 (§13.5's standing rule), L92–111 (§13.6.3, the dictionary — (iii) and (v) in particular), L113–128 (13.6.4 and its (q1)/(q2)), L130–141 (13.6.5), L143 (13.6.6), L145 (13.6.7).
- `paper/collatz-reduced-v3.tex` L149–165 (`thm:deltaM` and `thm:onestep` — the third window definition), L239–332 (all of §5).
- `itinerary.md` L69–75 (§14.15.2, including the L73 pointer sentence that asserts the equivalence).
- `briefs/v3r2-aeh-formulation-findings.md` — the round that produced the current text. **§9 (L346) especially**: items 2, 4 and 5 are unsettled questions this round reopens. Do not re-derive what it settled; do not treat what it parked as settled.
- `experiments/aeh_symbolic.py` and `experiments/aeh_calibration.py` — what the campaign actually tallied. The calibration record measures consecutive pairs (`aeh.md` L50, the `(s,s') = (4,3)` cell), which is evidence about which form the project has *in fact* always been testing.

## The task

Settle what the single object named AEH is, and produce the text that says so once.

**Present both options fully. Recommend one. The author decides at review.**

For each of the two options — (1) strengthen to all finite `L`-block distributions, letter coordinates primary; (2) retain the single-visit form and demote genericity to a strictly stronger named hypothesis — state:

1. the exact statement of the hypothesis, in drop-in form;
2. what becomes of 13.6.4's equivalence, and of (q1);
3. what the paper's Hypothesis 5.1 becomes;
4. the cost: what is claimed that was not claimed before, what is no longer claimed, and whether any consequence weakens;
5. how the calibration record reads against it — is the campaign evidence for the hypothesis as newly stated, or for something weaker?

Whichever you recommend, the deliverable must fix, unambiguously:

- **one observable**, `W_{k,D}` — its exact content, and whether the labels `(s, σ, a_+)` are in it, capped, or excluded;
- whether its alphabet is finite, and if the labels break finiteness, what the repair is;
- **`D_k`** — defined, not assumed;
- **`π_{k,D}`** — the law, its dependence on the cap made visible in the notation;
- **the norm** — total variation unless you argue otherwise;
- **the probability space** — one-sided `B` or two-sided `B̂`, with the segment-boundary question answered;
- the status of the paper's Theorem 3.8 window as a **separate, countable** object, and the sentence that says so.

**Then trace the consequence chain.** For each, state: survives verbatim, survives restated, or fails.

- 13.3.1 (ledger, error `O(2^-k)`);
- 13.3.2 (the `1/3` rate; the drift non-consequence);
- 13.3.3 (the scope discipline);
- 13.6.3(v)'s product law, under the probability space you choose;
- 13.6.4 and (q1) — this is where the round's content is;
- 13.6.5's values and the Tao attribution;
- 13.6.6 and 13.6.7;
- the three "equivalence" sites: `aeh.md` L2, `aeh.md` L71, `itinerary.md` L73;
- the paper's §5, L241 (the `π_k` paragraph) and L243–257 (the hypothesis).

If the honest answer is that one of these weakens, say so without hedging. A round that discovers a claim must be retracted is a successful round. Vagueness is what produced three objects under one name.

## Deliverable

Write **only** `briefs/v3r3-aeh-object-findings.md`, containing:

1. the two options, fully costed, with a recommendation and its reasoning;
2. **exact drop-in text for the recommended option** — LaTeX for the paper's `hypothesis` environment, its preceding `π_k` paragraph, and `thm:onestep`'s window sentence if it moves; Markdown for `aeh.md` §13.2, Hypothesis 13.2.1, 13.6.4's statement and (q1), the status header, and `itinerary.md` L73;
3. **the same drop-in text for the rejected option**, at lower resolution but sufficient for the author to switch without a further round;
4. the definitions block: `W_{k,D}`, `D_k`, `π_{k,D}`, the norm, the probability space;
5. the consequence trace as a plain list;
6. the verdict on whether the depth marginal values move under a two-sided formulation;
7. anything you could not settle, named as an open question rather than smoothed over.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file. No edits to `aeh.md`, `itinerary.md`, the `.tex`, or any other page — those are the apply phase, by a different delegate.
- No `git` write operations of any kind: no commit, no branch, no checkout, no push. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε` and silently corrupts the wiki pages.
- Do not renumber any monolith anchor (`13.2`, `13.2.1`, `13.6.4`, …). They are stable citation targets (`AGENTS.md`). A new object may need a new anchor; append, do not renumber.
- No change logs, no dated journals, no "was X, now Y" prose in anything destined for a tracked page (`AGENTS.md`). Your findings file is a working document and is exempt.
- Numbers, section numbers and quoted values must be verified against the files, not recalled.
- The paper is **unpublished**; Hypothesis 5.1 may be restated in place. No erratum framing.
- Do not attempt to prove AEH. Proof effort is parked per the README stopping rules, and nothing in this round changes that.
