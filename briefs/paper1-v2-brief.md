# Brief: paper 1 v2 — archive v1, restore the Merle subtitle, evidence the staircase hedge (for a delegated session)

**Context required before starting (in order):** `README.md`, `AGENTS.md`, `publication.md` (the "Sharpness-hedge status" entry under Uniform trim + staircase — it defines exactly what a v2 may and may not say), `HANDOFF.md` item 2 (the Merle correspondence state), `cycles.md` 12.8.6 entire (the floor-grade record every new sentence must be checked against), `TOUR.md` (status vocabulary), `paper/collatz-reduced-v1.tex`.

## Provenance and constraints

Paper 1 (*Reduced coordinates for the Collatz map*, Zenodo DOI 10.5281/zenodo.21273548) is published; Eric Merle's referee-grade reading (correspondence, 2026-07-15/16, author's mailbox — not in the repo) produced two v2 items, and the author's sent reply made two public commitments that this v2 must honor **exactly**:

1. **The citation fix.** The `merle` bibitem drops the subtitle of his preprint. The full corrected title is: *On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4, with documented structural obstructions* (Zenodo DOI 10.5281/zenodo.19790406 — DOI already correct, do not touch it). The reply commits: "The subtitle will be restored in v2."
2. **The hedge evidence.** The reply commits: "the hedge stays in any v2 — better evidenced, not closed." publication.md's entry says the same in ledger form: the `thm:staircase` sharpness hedge sentence is **not upgradable**; what a v2 may add is the evidence — the general construction recipe, verified instances at every period `p ∈ {2,…,21} ∪ {23}`, the ratio `γ/log₂(p)` inside the exact interval `[1.828, 3.643]`, and the two documented gaps: the unexplained combinatorial obstruction at `p = 22`, and the absence of a closed-form guarantee that the Diophantine (semiconvergent) step skips no period. Source of truth for every number and claim: `cycles.md` 12.8.6. The interval endpoints are outward-honest exact values (a review already fixed 1.83 → 1.828 once; do not re-round).

**Hard constraints.** No mathematical claim in the paper changes strength. The hedge sentence in the staircase theorem's statement stays **verbatim**. Nothing in the added text may exceed what cycles.md 12.8.6 records — where in doubt, quote the wiki's own wording. Zenodo upload/publication is the author's act alone (send-stays-with-author convention); this session prepares files only.

## Queue, in order (one commit per item)

1. **Archive v1 (pure moves, no content edits, one commit).** `git mv paper/collatz-reduced-v1.tex sources/paper/collatz-reduced-v1.tex` and `git mv paper/collatz-reduced-v1.pdf sources/paper/collatz-reduced-v1.pdf` (create `sources/paper/`). sources/ is immutable from this moment: v1 is never edited again. `paper/collatz-mirror-v1.*` stays where it is — paper 2 is out of scope.

2. **Seed v2 (pure copy, no content edits, one commit).** Copy the archived v1 tex byte-identically to `paper/collatz-reduced-v2.tex`. This commit ordering makes the later diffs pure content diffs.

3. **The two edits (one commit).**
   - Restore the subtitle in the `merle` bibitem (exact title above).
   - Add the hedge-evidence note. Locate `thm:staircase` (Theorem 4.11) and its environs (the sharpness discussion; Remark 5.9 is the staircase-divergence link). Add a clearly-marked **"Note added in v2 (July 2026)"** — a short paragraph, not a new theorem: prompted by correspondence on the sharpness hedge (cite the corrected `merle` entry), a general construction was attempted; state the recipe in one sentence (semiconvergents of `log₂ 3` select `n`, a rounded geometric profile builds the climb, a bounded correction closes the last bits), the verified range `p ∈ {2,…,21} ∪ {23}` with `γ/log₂(p) ∈ [1.828, 3.643]`, the two documented gaps exactly as above, the unchanged hedge, and a pointer to the public record (cycles.md 12.8.6 in the repository). Update the paper's version/date line to v2 with a one-line version history footnote if the class supports it cleanly; leave the DOI text as the concept/version structure requires (the author assigns the v2 DOI at upload — do not invent one).

4. **Build (one commit for the PDF).** Build `paper/collatz-reduced-v2.pdf` with pdflatex. Known quirk (HANDOFF): the mount locks aux files — build in a temp directory and copy the PDF in. `\wp`/`\dp` are TeX primitives; the source already uses `\wnext`/`\dnext` — do not "fix" that. If the toolchain fails, commit the tex anyway and record the build obstruction in the review bundle.

5. **The review bundle (one commit).** Create `paper/collatz-reduced-v2-review.md`, self-contained for pasting to an external reviewer (ChatGPT) who has no repo access:
   - a flat changelog (what changed and why, three bullets: subtitle, note, version line);
   - the full unified diff of the tex content changes (`git diff` of the item-3 commit), in a fenced block;
   - the complete text of the added note, quoted;
   - the verification statement from item 6.
   If `latexdiff` is available, also produce a marked-up PDF (`paper/collatz-reduced-v2-diff.pdf`); if not, note its absence and move on — the unified diff is the deliverable.

6. **Verification (same commit as 5 or separate).** This item has no new mathematics, so the check is fidelity, not proof: a small script or recorded procedure confirming (a) every number in the added note appears verbatim in `cycles.md` 12.8.6 (the set `{2..21} ∪ {23}`, `22`, `1.828`, `3.643`); (b) the hedge sentence in v2 is byte-identical to v1's; (c) the archived v1 is byte-identical to the original (hash both). Record results in the review bundle. A throwaway check committed under `experiments/` is not wanted here — this is editorial verification; put the transcript in the bundle.

7. **Cross-page sweep (one commit).** `publication.md`: extend the Sharpness-hedge entry with one sentence (v2 prepared on branch, evidence note added, hedge unchanged; awaiting the author's Zenodo upload). `HANDOFF.md` item 2: one clause noting the v2 branch is ready for author review. `README.md`: update the papers line if it names v1 paths explicitly. `TOUR.md`/`index.md`: only if they name the v1 file path; pointers only.

## Success / stop criteria

- **Floor = primary:** all seven items; this is editorial work with no research risk.
- **Stop:** after item 7, stop. Explicitly out of scope: paper 2 (`collatz-mirror`) in any way (its identical bibitem nit goes in `briefs/paper1-v2-findings.md` as an observation, nothing more); any new mathematical content; any rewriting of existing prose beyond the two edits; any Zenodo interaction; any change to cycles.md or the wiki's mathematical pages. Off-brief findings to `briefs/paper1-v2-findings.md`; log and stop.

## Rules (non-negotiable, from AGENTS.md)

- sources/ is immutable — the moved v1 files are never edited, including whitespace.
- Register norm: the added note is flat and calibrated; it reports an attempt's floor-grade outcome and keeps the hedge. Words like "settles", "establishes", or "confirms sharpness" are violations.
- Work on branch **`paper1-v2`**, one commit per queue item as specified, and **do not merge to main** — the main session reviews (including re-checking every number against cycles.md 12.8.6) before the author sees it.
- No scope expansion.

## Definition of done

v1 archived byte-identical under sources/paper/; `paper/collatz-reduced-v2.tex` differing from v1 in exactly the two edits plus version line; a built v2 PDF or a recorded build obstruction; a self-contained review bundle whose diff a reader without repo access can evaluate; the fidelity checks recorded; the ledger sweep done; clean per-item commits on `paper1-v2`.
