# Brief: reverse.md consolidation (this file ONLY)

Date: 2026-07-22. Branch: create `wiki-consolidation-reverse` from `main`. Edit **only `reverse.md`** — a parallel delegation owns every other page. If a fix seems to require touching another page (index resolver, cycles.md pointers, etc.), record it in your final report instead; the main session reconciles at merge.

## Ground rules (non-negotiable)

- Read `AGENTS.md` first and comply: no change-logs, dated append-entries, branch-by-branch narration, or "was X, now Y" prose; verification records are a single current line; every fact lives in one place — within a page too.
- Math statements are edited conservatively: this brief authorizes ONE wording fix (item 1) and otherwise only deletion of narrative and reorganization of proved content into a single owner with pointer-stubs. Never alter a theorem statement, a constant, or a proof step. If a trim would change mathematical content, skip it and report.
- Separate commits per numbered group below, in order. The 14.15.7/8 collapse (item 3) is organizational only and MUST be its own commit with no other edits mixed in.
- Section numbers are stable citation anchors — nothing is renumbered; collapsed sections keep their headings as stubs.
- Update front-matter `updated:` to 2026-07-22. Do not push, do not merge; leave the branch for main-session review.
- Line numbers cited are from the 2026-07-22 audit of the pre-edit file; locate by quoted text.

## 1. Referee wording fix (commit 1)

§14.5.2 still reads "…classically one third of odd numbers are unreachable values." The mirror paper's referee pass (`0771aef`) replaced this register with "have no odd predecessor." Adopt the published wording (the sentence already uses "no odd preimages" earlier — make the whole passage consistent with the paper's form). No other claim changes.

## 2. Narrative trims (commit 2)

1. **Provenance stamps.** The section-opening stamps carrying dates, branch names, and prompting narration ("Added 2026-07-16, branch `door-seam`, per `briefs/…`", "Prompted by an external suggestion (ChatGPT, 2026-07-16)", etc.) at the heads of 14.5, 14.6, 14.6.5, 14.13, 14.14, 14.14.7, 14.14.8, 14.15, 14.15.4, 14.15.5, 14.15.6, 14.15.8, 14.15.9: strip date/branch/prompt narration; keep at most a bare `briefs/…-findings.md` pointer where the proof or verification detail lives there. The `source:` front-matter field is the sanctioned provenance slot.
2. **"was X, now Y" notes.** (a) The "(Language corrected 2026-07-12 per paper-2 referee: the earlier '3-adic −1' conflated…)" parenthetical — delete; the corrected language stands on its own. (b) "(corrected 2026-07-12; the earlier `2^(10.5)` was slack in the wrong direction)" inside the §14.6 proof — delete the parenthetical, keep the correct constant. (c) The triple-stated first-renewal-equation dead end (14.4 "Recorded failure", 14.5.3's restatement, and the adjacent Remark): keep the 14.4 record (house norm permits recorded dead ends), shrink the other two to pointers to it.
3. **Accounting-sentence dedup.** The sentence "nothing here reduces how much of the stratum word an infinite orbit requires (11.8.7.7, 14.14.6, 14.15.2)" appears nine times (14.14.6, 14.14.8, 14.15.2, 14.15.4(d), 14.15.5(d), 14.15.6(e), 14.15.7(d), 14.15.8(d), 14.15.9(e)), each prefaced by an "extends …'s own accounting sentence" append-chain. Keep the full statement ONCE at 14.14.6 (the reconciliation that owns the identification, pointing at bridge.md §16 / stage4 11.8.7.7 as the owners); replace the other eight with one clause each: "Bridge status unchanged (14.14.6)." Do not lose any *section-specific* content that rides in those sentences — where a copy adds a genuinely local claim (e.g. 14.15.9(e)'s "height growth itself contributes no further obstruction once q is known… periodic cycle exclusion remains open"), keep the local claim and trim only the repeated accounting boilerplate.
4. **Front-matter "Current state" paragraph** (~6 KB, one paragraph): rewrite to a few sentences of current standing — what is proved (duality complete, density bound, seam, full shift, three-way diagonal characterization signed over the nonzero odd integers, whole-period height laws with the q-dichotomy), what is open (periodic cycle exclusion = ruling out q = 1 beyond the known instances; the Bridge unchanged). Drop the per-subsection dates and branch attributions — each subsection carries its own status.

## 3. Collapse 14.15.7 / 14.15.8 into 14.15.9 (commit 3 — organizational only)

The page itself states the subsumption: 14.15.9.7 ("14.15.7's capped/escaping dichotomy is the q=1 degenerate case … its instances are reproduced verbatim"), 14.15.9.6 = 14.15.8.3 generalized (identical closed forms), 14.15.9.8–10 = 14.15.8.4–6 generalized (14.15.9.9 correcting 14.15.8.5's sharp-constant scope), and 14.15.9.4(3) discharging 14.15.7.5's hypotheses. Execute the consolidation the "cross-referenced, never edited" posture deferred:

- Reduce §14.15.7 and §14.15.8 to short stubs under their existing headings. Each stub states: (i) the section's named deliverables as corollaries of 14.15.9 — keep verbatim the three closed-form instance laws (`H = 4·72^n − 5`; `H⁻ = 2·12^n − 1`; the period-7 word's `H = 4·(2^11·3^7)^n − 17` / `4·4478976^n − 17`) and each section's single current verification line; (ii) a pointer to the exact 14.15.9 subsections that now own mechanism and proof (14.15.9.6, 14.15.9.7, 14.15.9.8–10); (iii) one line noting 14.15.7.5 now holds hypothesis-free via 14.15.9.4(3).
- Deep anchors that other text cites (14.15.7.3, 14.15.7.4, 14.15.7.5, 14.15.7.6, 14.15.8.3, 14.15.8.4, 14.15.8.5, 14.15.8.6) must remain resolvable: keep each as a one-line entry inside the stub (statement name + pointer to its 14.15.9 owner). Grep `reverse.md` and report (do not edit) any OTHER page citing these anchors.
- Do not touch 14.15.9's own text except where it says 14.15.7/8 "stand as the p=1 and q=1 faces of one law" — that framing is current and stays.
- This is subsumption, not refutation: nothing goes to archive/.

## 4. Cross-pointers (commit 4; pointer prose only)

1. §14.15.6(d)(iv) (the four known cycles as G-periodic diagonal points with door-words): add the census cross-pointer → cycles.md Remark 12.6.1.2, where the same four cycles appear as `|q| = 1` near-miss anchors `(k, m, q)` — two frames of one census. Pointer only; do not restate the anchor table.
2. §14.15.9(e): alongside its existing open-front statement, note the numerator frame of the same parked condition via the existing lemma link (q = 1 in the fixed-point frame ⟺ q | R₀ nontrivially; cycles.md 12.6.1.1 ↔ 14.15.9.2). One sentence.
3. §14.15.2: where AEH is restated as cylinder-measure equidistribution, confirm the aeh.md §13.2 pointer exists (it should); the aeh-side back-pointer is the other delegation's job.

## Final report

Return: per-commit summary; byte/line size of reverse.md before and after; the list of external pages citing 14.15.7.x/14.15.8.x deep anchors (found by grep, unedited); any trim skipped with reason.
