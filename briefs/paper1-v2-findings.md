# Off-brief findings: paper 1 v2 (`paper1-v2` branch)

Per `briefs/paper1-v2-brief.md`'s stop criteria: logged, not acted on beyond what's noted.

## 1. Paper 2 (`collatz-mirror-v1.tex`) has the identical `merle` bibitem nit

`paper/collatz-mirror-v1.tex` line 329 carries the same truncated title as paper 1's pre-v2 `merle` bibitem:

```
\bibitem{merle} E.~Merle, \emph{On the non-existence of non-trivial Collatz cycles: a conditional formal proof in Lean 4}, preprint, Zenodo DOI 10.5281/zenodo.19790406 (2026).
```

— missing the same subtitle ("...with documented structural obstructions") that this brief restored in paper 1's v2. Explicitly out of scope per the brief ("paper 2 (`collatz-mirror`) in any way ... goes in `briefs/paper1-v2-findings.md` as an observation, nothing more"). Not touched. A future paper-2 v2 brief would fix it the same way.

## 2. HANDOFF.md's "Papers" line named a now-stale v1 path (fixed, minor, in-scope of item 1's consequence)

`HANDOFF.md`'s "State of the fronts" bullet under **Papers** said `Sources at paper/collatz-reduced-v1.tex, paper/collatz-mirror-v1.tex` — accurate before this brief's item 1 (the archive move), stale after it, since `collatz-reduced-v1.tex` now lives at `sources/paper/collatz-reduced-v1.tex`. This wasn't explicitly named in the brief's item-7 sweep list (which named HANDOFF.md item 2 specifically, not this "Papers" bullet), but leaving a path our own item 1 made false felt like the wrong kind of quiet — it's a direct, mechanical consequence of the archive move, not new content or a new claim, so it was folded into the item-7 commit rather than left stale or split into a separate unscoped commit. Fixed in the same commit as the item-7 sweep, alongside the HANDOFF.md item-2 clause and the publication.md sentence the brief called for.

## 3. `cycles.md` 12.8.6 itself is internally inconsistent on the "per-period" vocabulary (observation only, not touched)

`cycles.md` §12.8.6 line 239 (the subsection's own opening summary) says the attempt reached "a general **per-period** construction recipe" — the phrasing the `paper1-v2-revision-brief.md` cited as authoritative to fix the paper's "non-per-period" wording. But line 265 (the "Achieved grade" closing paragraph of the same subsection) says the opposite: "one general, **non-per-period** construction recipe," and also uses "a **dense**, algorithmically generated range" — exactly the two register-flagged phrases the revision brief required removed from the paper as "internal informalism, wrong register for print." Line 8 (the page's "Current state" paragraph) independently uses "a **combinatorial obstruction** precisely located at `p = 22`" — the third phrase the revision brief flagged. So the paper (now register-calibrated, verified above by grep) is *more* consistent with the wiki's stated register norm than the wiki page itself. `cycles.md` is out of scope for this and both prior briefs (wiki pages untouched); logged only, for whoever next touches 12.8.6 — lines 239 and 265 should agree on "per-period" vs "non-per-period," and lines 8/265's "combinatorial obstruction"/"dense" read as the same register slip the paper's revision round corrected.

**Update (2026-07-17, `paper1-v2-p22` branch): resolved.** The current `cycles.md` §12.8.6 (as rewritten by `briefs/p22-record-update-brief.md`, merge commit `72ec88e`, whose own message records "register slips fixed") no longer contains "non-per-period", "dense", or "combinatorial obstruction" anywhere in the section — re-checked by grep against the full section text (lines 237–273) while preparing this round's note update. No action was needed or taken here; recorded to close the loop on the observation above.

## 4. Stale rendered section/theorem number in the prior review bundle (fixed while regenerating, `paper1-v2-p22` branch)

The review bundle's "Version note, quoted in full" section, as it stood before this round, quoted the sharpness hedge as being in "Section 5"; the actual `pdflatex`-rendered output (checked fresh via `pdftotext` on this round's rebuild) numbers it "Theorem 4.6 ... (Section 4)". This was the kind of stale-quote drift the `paper1-v2-final-polish-brief.md` was written to prevent (a second external reviewer had caught an earlier instance of the same pattern). Corrected in this round's regenerated bundle (`paper/collatz-reduced-v2-review.md`) since the brief for this round asked for the bundle's build section and quotes to reflect the current build; not a content change to the tex, only to what the bundle reports about it.
