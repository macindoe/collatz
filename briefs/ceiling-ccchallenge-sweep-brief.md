# Brief: ccchallenge sweep for the counting ceiling — close the gaps left by the novelty refresh (the register, Hercher's forward citations) before paper 1 v4 — for a delegated session

**Why.** `briefs/ceiling-novelty-refresh-findings.md` (merged 2026-10-18) found the uniform trim subsumed by Simons–de Weger 2005 and the sharpness partially anticipated (SdW 2005 p. 69 belief; Halbeisen–Hungerbühler 1997 in the length parameter). Its search did not browse ccchallenge.org's register (389 entries; ~30 from 2023–26), returned no forward citations of Hercher (Semantic Scholar index gap), and had no Google Scholar / zbMATH access. Paper 1 v4 (decided 2026-10-18) and a correction to the joint note will rest on the verdict; this window closes those gaps.

**Context required before starting:** `README.md`, `AGENTS.md`, `briefs/ceiling-novelty-refresh-brief.md` (the claim under test, parts 1 and 2, and the rules — they all apply here unchanged), `briefs/ceiling-novelty-refresh-findings.md` (what is already held and the verdicts — do not redo those sources), `TOUR.md` (the dictionary).

## Items

**A. The ccchallenge register.** Enumerate every entry at `https://ccchallenge.org/` (the page lists `/api/papers/<key>/bibtex`; record the count and the date read). Screen every entry's title/bibtex for cycles (cycle bounds, m-cycles, local minima, circuits, rational cycles, `ax+b` cycles, linear forms in logarithms, Diophantine approximation of `log₂3`, "impossibility"/"barrier" of methods). For every entry from 2020–2026 that touches cycles, read it at source (arXiv/Zenodo/journal) at least to its statements and closing remarks; for older cycle entries not already in the refresh's source table, read where an open copy exists. Record the register's own status for each (formalised / review / wishlist) where shown.

**B. Forward citations.** Papers citing Hercher 2023 (arXiv:2201.00406 / JIS 26) and Simons–de Weger 2005 (DOI 10.4064/aa117-1-3) and Halbeisen–Hungerbühler 1997 (DOI 10.4064/aa-78-3-227-239) published 2020–2026: try Crossref's cited-by where open, OpenAlex (`api.openalex.org`, `cites:` filter), Semantic Scholar again, and arXiv full-text search. Record which index returned what.

**C. The flagged item.** Williams, arXiv 2607.01718 (July 2026), uses `n = λ·2^a·3^b − 1` — the record's rising-run coordinate. Read it at source and say, separately from the ceiling question, whether it bears on paper 1's coordinate-system claims (Reduced blocks / states `(ω, d)`, `publication.md`), and whether v4 should cite it.

## Rules and deliverables

All rules of the refresh brief apply (a label is not a match; held vs cited; strongest verdict "not found in this search"; nothing outward; Edit/Write only; encoding scan; foreground until committed; edit no wiki page, paper or joint note). Branch `ceiling-ccchallenge-sweep` from current `main` (`git merge --ff-only main` first if behind; record the base SHA). Deliverable `briefs/ceiling-ccchallenge-sweep-findings.md`: the register enumeration (count, screened list with cycle-relevance mark), the per-source table for everything read, the forward-citation log, the Williams verdict, and a single line per part: does anything here change the refresh's verdicts — yes (with source, page, quote) or no.
