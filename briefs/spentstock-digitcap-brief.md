# Brief: the spent `|q| = 1` stock as the rational-anchor instance of the digit-match ceiling (for a delegated session)

**Context required before starting (in order):** `README.md` (strategy and **binding stopping rules** — the cycle front is PARKED; this brief does not reopen it), `AGENTS.md` (binding house norms), `cycles.md` §12.6 entire (especially Remark 12.6.1.2 — the near-miss anchors, the spent stock, the side-asymmetry), `anchors.md` §17.4–17.5, `stage1-synthesis.md` §11.8.3.11 entire (the Bugeaud–Laurent pin, Corollaries 11.8.3.11.1–2), `bridge.md` §16.4.4 (the demand side: rigidity at the anchor-walk target; note the page charter — pointers only), `stage3.md` §11.8.6.3 (the target-shift lemma) and `ladder.md` §15.5 (the just-merged third face — your result is a fourth, and the coherence should be stated once, not belabored).

## Provenance and pre-check

Main-session exploration (2026-07-23) of knowledge-opportunity #2 from the post-cleanup flag list: cycles 12.6.1.2's `|q| = 1` spent stock and anchors 17.4's `O((log n)²)` digit-match ceiling may be two views of the same rigidity boundary at bridge 16.4.4's anchor-walk target. Pre-checked with fresh throwaway code (main session, 2026-07-23; script deliberately not provided):

- **A `|q| = 1` near-miss is a linear-in-`n` digit-match demand.** `2^K − 3^n = +1 ⟺ 3^n = 2^K − 1 ⟺ v₂(3^n + 1) ≥ K` (with unit quotient forcing equality-and-exactness); `2^K − 3^n = −1 ⟺ v₂(3^n − 1) ≥ K`. Since `2^K = 3^n ± 1` forces `K ≥ n·log₂3 − 1`, the demand is **linear in `n`**. (Mind the sign pairing: `q = +1` pairs with `v₂(3^n + 1)`, `q = −1` with `v₂(3^n − 1)`. The main session's own throwaway check briefly got this backwards; state it carefully.)
- **The capacity at targets `±1` is exact, elementary, and logarithmic:** `v₂(3^k − 1) = 1` (`k` odd), `= 3 + v₂(k/2)` (`k` even — this is precisely the `c = 1` global valuation law `11.8.4.1` at `ω = 1`, `N(1) = 0`); `v₂(3^k + 1) = 2` (`k` odd), `= 1` (`k` even). **Verified `k ≤ 2000`, 0 failures.** So capacity `≤ 3 + log₂ n` — logarithmic.
- **Linear demand vs logarithmic capacity closes the stock:** `n·log₂3 − 1 ≤ 3 + log₂ n` forces `n ≤ 2` (n = 1, 2 hand-enumerable), giving exactly `(K, n) ∈ {(1,1), (2,1), (3,2)}`. **Exhaustive check `K, n ≤ 500`: exactly those three.** At all three stock points demand meets capacity with **exact equality** (hand-verified: `(1,1)`: `v₂(3−1) = 1`; `(2,1)`: `v₂(3+1) = 2`; `(3,2)`: `v₂(9−1) = 3`).
- **Fixed-`q` near-misses are target-shift problems:** `2^K − 3^n = q ⟺ 3^n − (−q) = 2^K`, the valuation problem `v₂(3^n − c)` at the shifted target `c = −q` — the same mechanism as stage3's entry-depth targets `1 − 2^s` and ladder 15.5's targets `3^(−k)`. Empirical texture: record matches `max_{n ≤ N} v₂(3^n + q)` grow like `log₂ N` for sampled `q ∈ {±1, ±5, 7, 23, −139}` (all records `≤ ~2·log₂N` at `N = 4000`).

So the flagged identification is true and sharpenable; your job is to record it at house standard. Your verification code must be your own fresh implementation, per AGENTS.md.

## The framing mandate (read before item 1)

This is a **unification note, not a new lever**, and the cycle front **stays parked**. Binding calibration constraints:

1. **Nothing is excluded that was not excluded.** 12.6.1.2 already says the spent stock "excludes nothing"; the identification explains *why* the stock is finite (logarithmic capacity vs linear demand), it does not extend the exclusion. The parked condition — `q | R₀` nontrivially for every further cycle — is untouched: the digit-match ceiling says **nothing** about divisibility at `|q| > 1`.
2. **Do not reprove classical results as new.** The fixed-`q` finiteness of `2^K − 3^n = q` is Pillai's theorem (effective via Baker theory; S. S. Pillai 1931/1945 for the statement, effective form standard from Baker-type bounds — pin a citation at house standard, primary source or standard reference, as 12.6.1.2 did with Gersonides). The Gersonides classification itself is already correctly attributed in 12.6.1.2; your contribution is only the *identification* of its mechanism with the wiki's own valuation law.
3. **The register sentence:** the `|q| = 1` spent stock is the **rational-anchor instance** of the digit-match ceiling — at targets `±1` the anchor value is an integer (`N(1) = 0`; the `+1` target handled by the elementary odd/even laws), so the capacity is *exactly* logarithmic and *elementary*, giving a complete finite classification; at general fixed targets the anchor is irrational and the capacity bound is Baker's `O((log n)²)` (11.8.3.11.2) — effective but asymptotic, no classification. One boundary — linear closure demand vs (poly)logarithmic tracking capacity — read at a rational point and at general points. That is the entire claim.
4. Any prose implying progress on cycle exclusion, the Bridge, or the parked divisibility condition is a register violation.

## Queue, in order

1. **The identification remark.** New **Remark 12.6.1.3** in cycles.md, directly after 12.6.1.2 (never renumber existing anchors). Content, in order:
   - *(a)* The sign-paired equivalence: `|q| = 1` near-misses are exact 2-adic digit-match demands `v₂(3^n ∓ 1) ≥ K` (state both signs explicitly and correctly), with `K ≥ n·log₂3 − 1` making the demand linear in `n`.
   - *(b)* The capacity laws at `±1` (state all four cases: `3^k ∓ 1`, `k` odd/even), identified as the `c = 1` global law `11.8.4.1` at `ω = 1` (even case of `3^k − 1`) plus elementary mod-8 checks (the other three cases) — i.e., the wiki's own valuation formalism already contains Gersonides: linear demand vs logarithmic capacity forces `n ≤ 2`, and the enumeration is the stock. This re-derivation *is* 12.6.1.2's cited "elementary (mod 8 plus a two-line factoring)" argument, now recognized as an instance of the anchor law rather than an ad-hoc fact — say exactly that, one sentence.
   - *(c)* The general boundary: a fixed-`q` near-miss is the valuation problem at shifted target `c = −q`; for general `q` the capacity is Baker's ceiling `O((log n)²)` (`11.8.3.11.2` / anchors 17.4) — effective finiteness for every fixed `q` (Pillai, cited per mandate item 2), no classification, and **no divisibility information**. Hence: the spent stock and the digit-match cap are one rigidity boundary — the linear-demand/logarithmic-capacity gap at bridge 16.4.4's anchor-walk target — read at the rational anchor point (elementary, exact, classified, divisibility-free) and at general points (Baker, asymptotic, parked behind `q | R₀`).
   - *(d)* One coherence sentence: the target family `c = −q` joins the mechanism's other faces (entry-depth targets `1 − 2^s`, ladder targets `3^(−k)`, ladder.md 15.5) — pointer, no restatement.
2. **The calibration sentences.** Same remark, mandatory: framing-mandate items 1 and 3 in the page's own words; the front stays parked; `−17` remains the lone nontrivial divisibility instance; nothing about `q | R₀` moves.
3. **The pointer sweep.**
   - `anchors.md` §17.4: extend the Corollary-11.8.3.11.2 bullet by one clause — the ceiling's rational-anchor instance is the spent `|q| = 1` stock (cycles.md 12.6.1.3). §17.5's 12.6.1.2 bullet: append the 12.6.1.3 pointer to the existing line (one clause).
   - `bridge.md` §16.4.4: one clause on the tools-with-traction or counting-limit bullet tying the spent stock to the digit-match ceiling via 12.6.1.3 (pointers only, per the page charter).
   - `cycles.md` front matter `updated:`; Current-state paragraph only if it already mentions 12.6.1.2's stock (check; if not, no addition — this remark changes no status).
   - Do **not** restate content anywhere outside 12.6.1.3 — every fact lives in exactly one page.

## Success / stop criteria

- **Floor:** item 1(a)–(b) proved and verified (the elementary identification), item 3's anchors.md pointer.
- **Primary (expected, given the pre-check):** all three items.
- **Stop:** after item 3, stop. Explicitly forbidden, whatever the results suggest: any attempt on the divisibility condition `q | R₀` (parked; reopening requires a divisibility-aware idea per README's stopping rules); any small-`|q|` census, near-miss enumeration campaign, or per-period cycle search (README stopping rules; the side-asymmetry facts of 12.6.1.2 are complete as recorded); any strengthening attempt on the Baker exponent or constants (17.4 is pinned); any touch of the remaining two flagged knowledge opportunities. Off-brief findings go to `briefs/spentstock-digitcap-findings.md`; log them and stop anyway.

## Placement and numbering

- `cycles.md`: new **Remark 12.6.1.3** holding items 1–2. Existing anchors untouched.
- `anchors.md` §17.4 + §17.5: one clause each. `bridge.md` §16.4.4: one clause. Front-matter `updated:` on every touched page.
- Cross-page status sweep per AGENTS.md when done: index.md (no status change expected — verify, don't invent), HANDOFF.md (the Cycles line: at most one appended clause naming the identification; the PARKED status is unchanged). publication.md: nothing.

## Rules (non-negotiable, from AGENTS.md)

- Every proved claim gets an **independent** numerical check — fresh code, not the pre-check's constructions; record what was checked, the range, seeds where applicable, and the date, inline in the owning remark (overwriting style, no journals).
- Verification code goes in `experiments/spentstock_digitcap.py`, states which results it supports, stays runnable, imports nothing from `experiments/merle_round5_check.py` or `experiments/ladder_targetshift.py` (independence). Exact integer arithmetic wherever a pass/fail decision is made. Suggested coverage: the four capacity laws to a stated bound; the exhaustive `|2^K − 3^n| = 1` window; the three stock points' demand-capacity equality; the sign pairing; spot texture for two or three fixed `q` (bounded, stated ranges — this is verification of stated claims, not a search campaign).
- Citation pinning at house standard for Pillai (primary or standard reference, with the effective-form attribution done carefully — if pinning the effective form to a specific theorem proves murky within a bounded effort, cite the ineffective classical statement plus the fact that 11.8.3.11.2's own Bugeaud–Laurent pin supplies effectivity for the case at hand, which is all the remark needs).
- Register norm: flat, calibrated prose. The framing mandate's four constraints are binding.
- Work on branch **`spentstock-digitcap`**, based at current main **`2b17956`** (verify: `git log --oneline -1 main` in your worktree should show 2b17956; if your worktree's HEAD is older, branch from 2b17956 explicitly — it is in the shared object store). Commit per item with verification in the same commit, and **do not merge to main** — the main session reviews and re-runs all verification code before merging.
- No scope expansion.

## Definition of done

Item 1 as a proved, verified Remark 12.6.1.3 (sign-paired equivalence, capacity laws identified with the wiki's own valuation law, the demand/capacity closure of the stock, the general-`q` boundary with Pillai pinned, the one-sentence coherence pointer); item 2's calibration stating plainly what is identified (one rigidity boundary, two readings) and what is not (no new exclusion, divisibility untouched, front parked); item 3's pointers in anchors.md, bridge.md, HANDOFF; clean per-item commits on `spentstock-digitcap` with `experiments/spentstock_digitcap.py` committed and passing.
