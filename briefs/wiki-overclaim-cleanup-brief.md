# Brief: bring two wiki sentences into line with the paper's v4 fix pass — cycles.md Remark 12.8.4 and aeh.md §13.5 — for a delegated session

**Why.** The v4 fix pass (merged 2026-10-19; `briefs/paper1-v4-fixpass-findings.md` §5 item 4) tightened two paper sentences whose wiki originals still overstate: `cycles.md` Remark 12.8.4's "equivalently … rigidity of closed anchor walks" (the paper's U6: Theorem 4.6 concerns the divisibility conditions `q | R_r`; the equivalence with anchor-walk rigidity is not proved) and `aeh.md` §13.5's "the unique class with a deterministic self-loop channel" (U17). Every fact lives in one page; the page must say what is proved.

**Read first:** `AGENTS.md`, `briefs/paper1-v4-fixpass-findings.md` (U6, U17 rows and their sources), `cycles.md` 12.8 (12.8.3–12.8.4), `aeh.md` §13.5, and grep every tracked page for the same two phrasings.

## Items

1. Rewrite each sentence conservatively to what the page proves, matching the paper's fixed wording where the content is the same. If the anchor-walk equivalence is proved elsewhere in the record, cite it instead and say so in the findings; do not weaken a proved statement.
2. Fix any other page repeating either phrasing (list them); front matter `updated` on each edited page; no change-log prose.

## Rules and deliverables

Conservative edits only; no proof changes. Nothing outward; Edit/Write only; encoding scan before committing; foreground until committed. Branch `wiki-overclaim-cleanup` from current `main` (`git merge --ff-only main` first; record the base SHA). Findings `briefs/wiki-overclaim-cleanup-findings.md`: each edit, old → new, with its source.
