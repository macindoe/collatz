# Brief: staircase status versus the declared no-strengthening scope (v3 round 2, finding 4)

**Round.** Second external review of the unpublished `paper/collatz-reduced-v3.tex`, reviewed at `e4dac49` (= current `main`).

**This is an audit, not an edit task.** Produce a recommendation and text; change nothing.

## The finding

> The correction now asserts: a proof at every p ≥ 16; finite coverage below; bounded γ, stronger than the theorem's assessed O(log p). That is a strengthened universal result, even though the numbered theorem was left unchanged. Consequently the version note's final sentence — "No theorem or universal claim is strengthened" — is no longer accurate.
>
> Meanwhile Theorem 4.6 still combines a universal theorem opening with "assessed … though not proved here for all p," followed by a correction saying it actually is proved elsewhere.
>
> Given the decision against v4, I would not import the whole proof. I would instead:
> * present only the uniform trim as the in-paper main theorem;
> * label the staircase passage "sharpness evidence and assessment";
> * describe the all-period result explicitly as a stronger companion-record result;
> * replace "No theorem or universal claim is strengthened" with "No numbered theorem is restated; v3 reports a stronger result established in the project record."

The record supports the objection. `cycles.md` front matter (L2) already reads: all-p sharpness **PROVED** (12.8.6 — unconditional for p ≥ 16, finite check for 3 ≤ p ≤ 15, p ∈ {2,4} by exhibition), with γ bracketed between the absolute constants `3.683012` and `5.140212` — "stronger than the `O(log p)` the published theorem assesses", in the page's own words.

Note also: "No theorem or universal claim is strengthened" appears **twice** in the version note (once for v2, once closing v3). Check both.

## The question you are being asked to settle

The reviewer's four bullets are ambiguous between two readings, and the choice is deliberately left to this audit:

**Minimal.** Theorem 4.6 stays a numbered theorem with its statement intact. Only its hedge sentence is lifted out into a labelled "sharpness evidence and assessment" passage; the all-period result is named as a stronger companion-record result; the version note's closing sentence is replaced. Abstract untouched. No renumbering.

**Full.** Follow the reviewer literally. The uniform trim alone carries the main-theorem role; the staircase becomes an unnumbered assessment passage. This requires editing the abstract's "Our main new theorem is a sharp dichotomy for counting arguments" sentence and Contributions item (v), and renumbers everything after 4.6.

Recommend one. Base the recommendation on what the record actually proves and what each option costs — not on which is less work.

## Read before deciding

- `cycles.md`: front matter, Current state, and §12.8.6 in full — establish precisely what is proved, at what scope, and what remains assessed or checked-by-exhibition. The gap between "proved for p ≥ 16" and "universal" matters; so does whether p ∈ {2,4} by direct exhibition genuinely closes the family.
- `paper/collatz-reduced-v3.tex`: L221–223 (Theorem 4.6 and its hedge), L225–227 (Remark 4.7), L229–232 (Note added in v2), L235 (the 2026-08-01 correction), L41–42 (version note, both sentences), L38 (abstract), L54 (Contributions, item v), L259 (Discussion), and any other site referring to the staircase's status.
- `briefs/staircase-status-audit-findings.md` and `briefs/staircase-status-apply-findings.md` — the previous round on this exact question. Read what was decided and why; you are not bound by it.

## Specific things to adjudicate

1. Is Theorem 4.6's *opening* claim ("No trim uniform in p can extend the small-period constants: there exist configurations …") now proved outright by 12.8.6, rather than assessed? If so, the theorem's internal hedge is not merely awkward — it understates a proved result inside a numbered theorem, which is its own defect.
2. v1 and v2 are published with DOIs (`10.5281/zenodo.21421120` for v2). v3 is unpublished, so renumbering is *possible* — but assess the cost to citation continuity and to any external correspondence that cites these numbers. `briefs/merle-*` rounds cite paper theorem numbers; check whether renumbering would strand any of them.
3. Does the abstract's claim survive the minimal option honestly? "Our main new theorem is a sharp dichotomy" — with the sharpness half now proved in the record but not the paper, is that sentence accurate as written?
4. Whichever option you recommend: the paper must not end up claiming the all-period proof as its own, and must not understate it either. Find the wording that reports it as a companion-record result at its true scope.

## Deliverable

Write **only** `briefs/v3r2-staircase-scope-findings.md`, containing:

1. a scope table: what `cycles.md` §12.8.6 proves, at what period ranges, by what means (proof / finite check / exhibition), against what the paper currently claims at each of its sites;
2. the recommendation — minimal or full — with the reasoning, and the cost of the rejected option stated fairly;
3. **exact drop-in LaTeX** for every site that changes under the recommended option, matching the surrounding register;
4. a site list for the rejected option too, so the decision can be reversed cheaply if overruled;
5. the version note's replacement sentence(s), both occurrences addressed.

## Constraints

- **Read-only on every tracked file.** The one file you may write is your findings file. Phase 2 applies the changes, by a different delegate.
- No `git` write operations of any kind: no commit, no branch, no checkout, no push. You are working directly in `c:\Users\Ace\Documents\Collatz` on `main`.
- Write files with the Write/Edit tools only. **Never** `Get-Content | Set-Content` or PowerShell redirection — PS 5.1 double-encodes this repo's `≤`, `—`, `ε`.
- Do not renumber any monolith anchor in the wiki (`12.8.6`, …); paper theorem numbers are a separate question, and are exactly what option "full" would disturb.
- Verify every quoted number and section reference against the files rather than recalling it.
