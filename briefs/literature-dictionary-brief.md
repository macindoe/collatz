# Brief: the literature dictionary and the map-symbol convention (2026-09-04)

Delegation brief. Main session drives; the delegate produces. Read `README.md` (stopping rules), `AGENTS.md` (one fact one page; conservative math editing; no change logs in tracked files), `TOUR.md`, `symbols.md` (whole file, including the collision index), and the register norm in `HANDOFF.md` before touching anything.

## 0. The decision this brief executes

The author has decided (2026-09-04), on the main session's recommendation after the fresh-eyes assessment (`briefs/fresh-eyes-assessment-findings.md` §6; HANDOFF item 4): **no wholesale renaming of the record's coinages** (anchor, block, staircase, uniform trim, door, seam, Bridge, AEH stay), because they name objects the literature has not named, they are frozen into two DOI'd papers and into Eric Merle's shared ledger, and a rename would create citation drift. Instead, three targeted moves:

1. **A dictionary**, in one place, from this record's terms to the literature's names, with the citations the record already pins.
2. **The map-symbol convention made explicit** and the one genuine collision reduced: this record's `T` carries three readings (symbols.md collision index) while the literature's `T` is Terras's one-division map.
3. **Literature names at the point of definition** for the objects that are literally the literature's: the cycle numerator as Tao's n-Syracuse offset, the letter word as the parity vector in renewal form.

The constraint that matters most: **no symbol or term that Merle's side cites may change meaning.** The shared repo `github.com/macindoe/one-obstruction-three-faces` (public; `PROTOCOL.md`, `LEDGER.md`, `NOTE.md`, and his `NOTE-v1.md` if present) and his Lean repo `ericmerle3789/one-obstruction-three-faces-lean` cite this wiki's sections by number and use its vocabulary (numerator frame `R_r`, `q`, transport recurrence, spent stock, margin, staircase). Adding a literature name beside a term is safe; changing a symbol is not. Nothing in the shared repo is edited by this brief.

## 1. Discipline

- Work in the worktree named in your prompt, on branch `literature-dictionary` cut from local `main` (which carries this brief). First command: `git rev-parse --short HEAD`, `git branch --show-current`, `git status`. Report base SHA.
- Edit only with the Edit/Write tools (never PowerShell `Get-Content`/`Set-Content`; HANDOFF quirk). Run `python experiments/encoding_scan.py` before the final commit; report CLEAN.
- One commit per page; commit messages say what was changed and why; every commit message ends with the trailer line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.
- Do not touch `sources/`, `paper/` (the papers are frozen at their DOIs; their conventions are *recorded*, not changed), or `experiments/`.
- **Conservative editing, strictly:** no theorem statement, proof, number, or section number moves. Where this brief says "one clause", add one clause; do not rewrite the sentence around it.
- Record obstructions rather than force. If a step turns out to require touching a math statement, stop that step and record it in the findings.
- Wait in the foreground; do not stop until every commit exists. Final report: branch, HEAD SHA, base SHA, `git log --oneline main..HEAD`, the usage counts of §2, the shared-repo convention check of §2, and any obstruction.

## 2. Measure first (report these numbers in the findings)

Before editing, count and classify, page by page across the wiki (`*.md` at the root, `archive/`, and the paper sources `paper/*.tex` read-only):

- occurrences of the symbol `T` denoting (a) the raw Collatz map `x/2`, `3x+1` (spine.md §3.1, §4.1 and wherever else), (b) the odd-to-odd map `x -> (3x+1)/2^{v_2(3x+1)}` (spine.md §9.8, cycles.md, ladder.md, reverse.md, itinerary.md, aeh.md), (c) the one-division map (`T_1`, aeh.md 13.2.3), and (d) the block horizon `T_N`. Use `git grep -n` with word boundaries and read each hit's context; report counts per page per reading.
- which convention each published paper's source uses (`paper/*.tex`: search for the map definitions), so that the dictionary can tell a reader coming from the PDFs what they saw there.
- which convention the shared repo uses: fetch the raw files `https://raw.githubusercontent.com/macindoe/one-obstruction-three-faces/main/NOTE.md`, `.../LEDGER.md`, `.../PROTOCOL.md` (and `NOTE-v1.md` if it exists) with WebFetch, and record whether they define or use `T`, `Syr`, `Col`, `T_1`, and which wiki terms they cite. If the fetch fails, say so and use `briefs/jointnote-v1-draft-findings.md` and `briefs/merle-round13-review-findings.md` for what the record already knows about the note's vocabulary.

These numbers decide the scope of §4 below and go into the findings.

## 3. Deliverable 1: the dictionary, in `TOUR.md`

`TOUR.md` is the external reader's trailhead and carries pointers only, so the dictionary lives there, as a new section **"Dictionary: this record's terms against the literature"** placed after "If you are coming from the papers". Two-column table, one row per term, third column the wiki page that defines the term. Every literature name carries the citation already pinned in `publication.md` (do not invent citations; if a name has no pinned citation, say "no literature name" or pin it from publication.md's bibliography). Rows, at minimum:

| This record | Literature | Defined at |
|---|---|---|
| the Collatz map `Col` (raw), the odd-to-odd map, the one-division map | Tao 2019: `Col`, `Syr`; Terras 1976 / Lagarias 1985: `T` for the one-division map | the convention note (below) |
| reduced map `F`; block; reduced state `(ω, d)`, odd core, depth | the Syracuse map with rising runs (maximal `2^m u - 1` chains) grouped; no literature name for the state | spine.md §3, §5.6 |
| anchor `N(ω)`, `M(ω)` | a normalized 2-adic logarithm, `N(ω) = -log ω / log 9`; the valuation law is lifting-the-exponent (the isometry of the 2-adic log) | stage1-synthesis.md 11.8.3.6 |
| exit valuation `s`; entry depth `m`; letter `(m, r)`; stratum word; itinerary language | Terras's parity vector / Tao's n-Syracuse valuation `a^{(n)}(N)`, in a renewal recoding at the entries `≥ 2` (aeh.md 13.6.5's dictionary); the coding is Terras 1976, Everett 1977, Lagarias 1985 | itinerary.md 14.15.1; aeh.md 13.6.5 |
| digit budget; window trichotomy | Terras's stopping-time window (the cylinder count); Tao 2019 Prop 1.9; the 2-adic shift conjugacy (Lagarias 1985; Bernstein–Lagarias 1996) | stage4.md 11.8.7.6–11.8.7.7 |
| AEH | Tao 2019 Heuristic 1.8 (the valuation heuristic), stated in ensemble form; the Lagarias stochastic model | aeh.md 13.2 |
| the depth law; the 3-adic past-limit `y_3` | Tao's Syracuse random variable `Syrac(Z_3)` (aeh.md 13.6.5 already attributes) | aeh.md 13.6.5 |
| the 3-adic anchor `M_3` | a 3-adic discrete logarithm base 2 (affine) | reverse.md 14.2 |
| rotation numerator `R_r`; cycle product equation; `q = 2^K - 3^n` | Tao's n-Syracuse offset `F_n(a)` via `2^{m_0} R_0 = 2^K F_n(a) + q` (cycles.md 12.6.1.7); the linear cycle equation, Böhm–Sontacchi 1978, surveyed in Lagarias 1985 | cycles.md 12.1, 12.6.1 |
| period-1, period-2 exclusions | Steiner 1977 (circuits); Simons–de Weger 2005 (m-cycles); Hercher 2022/23 | cycles.md 12.2, 12.5 |
| the density bound of the door tree | the Krasikov–Lagarias program (2002) and its predecessors Crandall 1978, Krasikov 1989 | reverse.md 14.6 |
| uniform trim; staircase; door; seam; Bridge; core-extraction deficit; spent stock; margin | no literature name (this record's, or joint with Merle where the ledger says so) | cycles.md 12.8; reverse.md 14.14; bridge.md §16; cycles.md 12.6.1.2–12.6.1.5 |

Add rows for any other coined term you meet in `symbols.md` that a reader from outside would not recognise. Keep each cell short; the table is a pointer, and every fact lives on its own page.

**The convention note**, directly above the table, three or four sentences: this record's `T` is the odd-to-odd map, which is Tao's `Syr`; the literature's `T` (Terras, Lagarias: one division per step) is this record's `T_1`; the raw map is `Col`; `T_N` is a block horizon and not a map. State which convention each paper uses (from §2). This is the one place a reader is told; symbols.md and spine.md point here.

## 4. Deliverable 2: the map-symbol convention in the pages

- **spine.md §3.1 and §4.1** (and any other place in spine.md §1–8 where `T` means the *raw* map): rename that reading to `Col`, so that spine.md's own two readings of `T` become one. Do this only where the symbol denotes the raw map; the odd-to-odd `T` of §9.8 stays. Check every occurrence individually; `T_{odd}` in §6 is a separate symbol and stays. If the count from §2 shows raw-map `T` appears in more than a handful of places or inside a displayed proof, stop and record instead.
- **spine.md §9.8**, the sentence "Throughout, `T` denotes the odd-to-odd Collatz map ...": add one clause naming it as Tao's `Syr` and pointing at the TOUR.md convention note.
- **aeh.md 13.2.3**, the sentence listing the three readings of `T`: add the literature names in one clause (`T_1` is the literature's `T`; this page's `T` is Tao's `Syr`).
- **symbols.md**: a short preamble paragraph "Conventions against the literature" (pointer to TOUR.md's note, no restatement beyond one sentence), and the collision-index row for `T` extended with the literature mapping. If `Col` is introduced, add its row in §1 and in the collision index.
- **Not in scope:** the global swap of the odd-to-odd `T` to `Syr` across the wiki. Record in the findings, with the §2 counts, what that swap would touch (pages, occurrence counts, whether any displayed statement contains `T`), so the author can decide it separately. Do not perform it.

## 5. Deliverable 3: literature names at the point of definition

- **cycles.md Proposition 12.6.1**: after the display defining `R_r`, one clause (not a new sentence inside the statement; a remark-style clause after the proof or in the Remark 12.6.1.1 lead) naming the numerator as Tao's n-Syracuse offset up to `2^{m_0}` and the summand `q`, pointing at Remark 12.6.1.7. Do not alter the proposition's statement or proof.
- **itinerary.md 14.15.1** (the letter word / itinerary language): check whether the page already identifies it with the Terras/Everett/Lagarias parity-vector coding (publication.md says 14.15.1 does). If it does, leave it. If it does not at the defining sentence, add one clause there.
- **anchors.md 17.1**: already says the anchor is a 2-adic logarithm; add the literature name "lifting-the-exponent" for the valuation law in one clause only if it is absent from that page.
- **README.md**: one pointer, in the sentence that already sends external readers to `TOUR.md` (the second paragraph), adding that TOUR.md carries the dictionary against the literature. One clause; nothing else on README changes.

## 6. Deliverable 4: the findings and the Merle note

- `briefs/literature-dictionary-findings.md`: the §2 measurements (usage counts per page per reading; the papers' conventions; the shared repo's conventions and which wiki terms it cites), what was changed on each page, what was deliberately left (the global `T` swap, with its cost), and any obstruction. Flat register.
- In that findings file, a section **"For the next round's mail to Merle"** containing two or three sentences the author can paste: the wiki now carries a dictionary of its terms against the literature (TOUR.md), no term or symbol cited by the shared ledger or note changed meaning, and the one symbol change (`Col` for the raw map in spine.md §3–4) touches no section the ledger cites. Sending is the author's; do not draft anything longer.
- **HANDOFF.md** open work item 4: replace the "decision pending" sentence with the decision and what landed (one or two sentences), and note the global `T` swap as the author's separate call with a pointer to the findings.

## 7. Verification before you report

- `git grep -nw T` counts before and after, per page, reconciled: the only changed occurrences are the raw-map ones renamed to `Col` and the added clauses.
- Every table row's "Defined at" pointer resolves to a real section (open each page and check the section exists).
- `python experiments/encoding_scan.py` CLEAN.
- `git log --oneline main..HEAD` in the report.
