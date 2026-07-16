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
