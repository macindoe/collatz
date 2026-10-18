# Findings: ccchallenge sweep for the counting ceiling — the register, forward citations, and Williams 2607.01718

**Task:** `briefs/ceiling-ccchallenge-sweep-brief.md` (rules of `briefs/ceiling-novelty-refresh-brief.md` apply unchanged). Branch `ceiling-ccchallenge-sweep`, base **`d9d26e6`** (worktree cut at `946e0d8`, fast-forwarded to `d9d26e6` before any work). All external reads 2026-10-18. Nothing outward: read-only GETs, no account, no email, no push. Downloads kept in the session scratchpad, outside the repo, read as data.

## 0. Verdict lines

- **Part 1 (upper half, Thm 4.5):** verdict label unchanged, **subsumed**. **Attribution changes: yes.** O. Rozier, *Problème de Syracuse : « majorations » élémentaires des cycles*, Singularité 2 no. 5 (1991), 8–11 (held: `https://www.probleme-syracuse.fr/cargo/Singularit%E9_2_5.pdf`, scanned, read from the page images). p. 8, Théorème: « Pour chaque entier n, il n'y a qu'un nombre fini de cycles alternant n séquences d'entiers impairs avec n séquences d'entiers pairs ». p. 11, **Lemme 4**: `2^{((α−1)/(α^n−1))M} − (a−2)((a−1)/(a−2))^n ≤ (a−2)u_0`, `α = log a/log 2`. With p. 10 (5), `u_0 < (1/ln 2)·n·M^14` (from the measure `|log 3/log 2 − p/q| > q^{−15}`), this bounds `M` effectively for every `n`. Here `n` is the number of local minima (= the record's `p`, = SdW's `m`) and `M` the number of odd steps (= the record's `n`, = SdW's `K`), and the exponent is the **same** `(L−1)/(L^p−1)` as SdW Lemma 7 and Theorem 12.8.1. It predates SdW 2005 by 14 years and Brox 2000 by 9. Neither SdW (v1.44 grepped) nor Hercher 2023 (grepped) cites it; Lagarias's bibliography I (item 152) does.
- **Part 2 (sharpness, Thm 4.6 / 12.8.6):** verdict label unchanged, **partially anticipated**. **The closest prior statement changes: yes.** Rozier 1991, p. 11, right after Lemme 4: « Cette relation apparaît si l'on recherche le minimum de ces maxima parmi tous les n-uplets (m_i) de réels positifs de somme fixée M. […] L'on voit ainsi que ce lemme est optimal si l'on part du lemme 3 et si l'on ne prend pas en compte d'autres propriétés éventuelles des (m_i). » This is closer than SdW p. 69. It is an optimality claim in the local-minima parameter, with its argument (a minimax over real tuples), and its extremal tuple is the staircase's profile (§3.2). What it lacks is in §3.2.

## 1. Item A — the ccchallenge register

**Read:** `https://ccchallenge.org/`, one HTML page (2,410,333 bytes), 2026-10-18. **Count: 389 entries** (one `/api/papers/<key>/bibtex` per card, 389 distinct keys). By year: 41 dated 2020–2026 (30 of them 2023–2026), 13 2010–19, 132 2000–09, 104 1990–99, 54 1980–89, 35 1970–79, 9 1960–69, and one undated (`Halemane2025-12-10`, DOI-dated 2025-12-10). The page itself carries abstracts for 41 entries.

**Register status as shown** (badge; the wishlist count and review/formalisation counts are on each card):
- Formalised (1): BohmSontacchi1978.
- Being formalised (4): Knight2026, Monks2006, KrasikovLagarias2003, Terras1976.
- Ready to be audited (6): Tao2022, Eliahou1993, BernsteinLagarias1996, Hercher2023 (Lean, `PhilNorfleet/Hercher2023_lean`), RozierTerracol2025, EliahouVergerGaugry2025.
- 378 entries carry no badge. 44 have wishlist > 0 (Tao2022 8; Eliahou1993, Knight2026, Monks2006 3; SimonsWeger2005, Hercher2023 and 9 others 2).
- The review panels checked (SimonsWeger2005, HalbeisenHungerbuhler1997, Hercher2023, Rozier1991) are links to Lagarias's bibliography entries or zbMATH reviews, not register-written reviews.

**Screening marks** (title, bibtex fields and the register abstract where present; the labels are screening marks, not matches): **C** = touches cycles (cycle bounds, m-cycles, circuits, rational cycles, cycles of `ax+b`/`qx+1` maps, cycle surveys) — 64; **T** = a Diophantine tool cited by the cycle line (linear forms in logarithms, measures for `log₂3`, `2^x − 3^y`) — 7; **P** = a claimed global proof that touches cycles only as a consequence — 3; **L** = "cycle" as a label only (graph/permutation cycles, cyclic groups) — 8; unmarked — 307.

**C (64)**, newest first, with register status (— = none) and wishlist:

| Key | Year | Status | WL | Read? |
|---|---|---|---|---|
| Park2026 | 2026 | — | 1 | **not held** (ResearchGate 403); characterized only by publication.md's own entry (Diophantine skeleton, 1–2-cycle exclusion) |
| PEREIRAENZO2026b | 2026 | — | 0 | Zenodo record 23242902 read (3x−1 "exceptional cycles"); zip not opened |
| Macindoe2026 | 2026 | — | 0 | ours (paper 1 v3) |
| Knight2026b | 2026 | — | 0 | held (Complex Systems 35(1), PDF) |
| Knight2026 | 2026 | Being formalised | 3 | **cited** (paywalled; round-15 record, Fernández–Ibáñez) |
| Siegel2024 | 2024 | — | 1 | held (arXiv 2412.02902) |
| Rebot2023 | 2023 | — | 0 | held (LPNU PDF) |
| Hercher2023 | 2023 | Ready to be audited | 2 | held (refresh; re-grepped) |
| Rozier2022 | 2022 | — | 2 | held (math.SE answer 4526766, via SE API) |
| Stokes2021 | 2021 | — | 0 | held (McMaster thesis) |
| Lagarias2021 | 2021 | — | 0 | held (refresh) |
| Santos2020 | 2020 | — | 1 | held (arXiv 2005.00346 v3) |
| Lagarias2012, Lagarias2011, Lagarias2003 | — | — | 0 | held (arXiv math/0608208, math/0309224) |
| Lagarias2010 | 2010 | — | 0 | overview chapter held (refresh) |
| Muller2009 | 2009 | — | 0 | cited (Lagarias II: "I have not seen this paper") — unchecked |
| LopezStoll2009 | 2009 | — | 0 | held (Integers 9 (2009) #A13, Colgate mirror) |
| Simons2008b, Simons2008a | 2008 | — | 0 | cited (Lagarias II items 98, 97) |
| Simons2008 | 2008 | — | 0 | held (refresh) |
| Simons2007 | 2007 | — | 0 | register abstract only |
| Monks2006 | 2006 | Being formalised | 3 | register abstract only (cycles as one of three sufficiency statements) |
| BelagaMignotte2006a/b/c | 2006 | — | 0 | cited (Lagarias II) |
| SimonsWeger2005 | 2005 | — | 2 | held (refresh) |
| Simons2005, Shi2005a, Luca2005, Li2005 | 2005 | — | 0 | cited (SdW p. 54; Lagarias II) |
| SimonsWeger2004, LiWu2004 | 2004 | — | 0 | cited (Lagarias II) |
| Sinisalo2003, Belaga2003 | 2003 | — | 0/1 | cited (Lagarias II) |
| RouetFeix2002, Brent2002, Mimuro2001 | 2001–02 | — | 0 | cited (Lagarias II) |
| Brox2000, BelagaMignotte2000 | 2000 | — | 0 | cited (refresh: matwbn 403; Lagarias II) |
| Metzger1999, Keller1999, BelagaMignotte1999 | 1999 | — | 0 | cited (Lagarias I/II) |
| BlecksmithMcCallumSelfridge1998 | 1998 | — | 0 | cited (Stokes 2021 §3; Williams 2026 [4]) |
| HalbeisenHungerbuhler1997 | 1997 | — | 1 | held (refresh) |
| FarruggiaLawrenceWaterhouse1996, Metzger1995 | 1995–96 | — | 0 | cited (Lagarias I) |
| FrancoPomerance1995 | 1995 | — | 1 | held, p. 1 only (scanned; Crandall numbers for `qx+1`) |
| Chisala1994 | 1994 | — | 0 | cited (refresh) |
| Eliahou1993 | 1993 | Ready to be audited | 3 | cited (refresh; register abstract) |
| Venturini1992 | 1992 | — | 0 | cited (Lagarias I) |
| **Rozier1991** | 1991 | — | 0 | **held** (open copy on the author's site; see §0, §3) |
| Rozier1990 | 1990 | — | 1 | held (register URL; scanned, read from page images) |
| Lagarias1990, Franco1990 | 1990 | — | 1/0 | cited (refresh; Lagarias I) |
| Seifert1988 | 1988 | — | 0 | cited (Lagarias I) |
| Lagarias1985 | 1985 | — | 0 | cited (publication.md pins it) |
| Steiner1981b | 1981 | — | 1 | held (fq.math.ca scan, OCR) |
| Steiner1981a | 1981 | — | 1 | not held (ResearchGate) |
| Garner1981 | 1981 | — | 0 | held (Proc. AMS 82, open archive) |
| Steiner1978, Crandall1978, BohmSontacchi1978, Davison1977 | 1977–78 | — | — | cited (refresh; SdW; Lagarias I) |

**T (7):** Baker1966, Ellison1971, Marcu1991, MichelMauriceYuri1995, Narkiewicz1980, Rhin1987, RhinToffin1986 — inputs, not cycle statements; not read.
**L (8):** Atkin1966, Klamkin1963, Shanks1965 (Collatz's original permutation, Problem 63-13), BernsteinLagarias1996 (the cycle structure of the conjugacy permutation `Φ_n`), Clark2006 (a different iteration), Tao2022 (cyclic group `Z/3^n`), Nashida2026d (cycles of a finite abstraction graph — Zenodo record and PDF held, no Collatz-cycle statement), Nashida2026e.
**P (3):** Halemane2025-12-10 (register abstract only), Novgorodtsev2026 (Zenodo 18659804 record and v14 PDF held; its "Theorem 4.3 (No Nontrivial Cycles)" is a claimed bit-exhaustion argument), Velazquez2026 (Zenodo 23122077 record held; "nontrivial cycle exclusion" from a finite residue cover). All three claim the full conjecture or cycle exclusion; none states a size-cap result.

**Unmarked (307), screened by title, listed for completeness:**
**2020–2026 (24):** Barina2025, CookSterinWoods2021, Daudin2020, EliahouFromentinSimonetto2022, EliahouVergerGaugry2025, Inclan2026, Inclan2026b, Jesus2026, KolpakovJumasLuo2026, Nashida2026, Nashida2026b, Nashida2026c, Nashida2026f, Novgorodtsev2026b, PEREIRAENZO2026, PEREIRAENZO2026c, PEREIRAENZO2026d, PereiraMazzoni2026, RozierTerracol2025, Sterin2020, Sterin2023, SterinWoods2020, Williams2024, YolcuAaronsonHeule2021.
**2000–2019 (116):** Akin2004, AlvesGracaDiasRamos2005, AmdeberhanMannaMoll2008, Andaloro2000, Andaloro2002, AndreiChinNguyen2007, AndreiKudlekNiculescu2000, ApplegateLagarias2003, ApplegateLagarias2006, BergelsonMisiurewiczSenti2006, BorovkovPfeifer2000, Bruckman2008, Cadogan2000, Cadogan2003, Cadogan2006, CanalesChaconVielhaber2004, Capco2015, Chamberland2003, DeMol2008, Domenici2009, Dumas2008, DumontReiter2001, DumontReiter2003, Farkas2005, GluckTaylor2002, Goodwin2003, He2003, HicksMullenYucasZavislak2008, Hotzel2003, HuangWu2000, ItoNakano2009, Kari2012, KariKopra2017, Ke2001, Ke2005, Kerner2000, Kohl2005, Kohl2007, Kohl2008a, Kohl2008b, Kohl2010, Konstadinidis2006, KontorovichMiller2005, KontorovichSinai2002, KraftMonks2010, KrasikovLagarias2003, KurtzSimon2007, Lagarias2006, LagariasSloane2004, LagariasSoundararajan2006, Lehtonen2008, Levy2004, Li2002, Li2003, Li2004, Li2006, LiLiang2002, LiLiu2006, LopezStoll2012, Margenstern2000, Matthews2005, Metzger2000, Metzger2003, Michel2004, Michel2014, MisiurewiczRodriguez2005, Monks2002, Monks2009, Monks2013, MonksYazinski2004, OhiraYamashita2004, OhiraYamashita2004a, Pan2000, Pe2004, PeresSimonSolomak2006, Qu2002, Roosendaal2004, Rozier2017, Rozier2018, Scollo2005, Shaw2006, Shi2005b, Silva2004, Simons2008c, Sinai2003a, Sinai2003b, Sinai2004, SlakmonMacot2006, SnappTracy2008, Tang2006, Urata2002, Urata2003, Urata2007, UrataHamada2005, Urvoy2000, VanBendegem2005, Volkov2006, Wang2002, WangWangFenXu2003, WangYu2007, WangYu2008, Wirsching2000, Wirsching2001, Wirsching2003, Wu2003, WuHao2003, WuHuang2001, WuHuang2001a, WuHuang2001b, Xia2003, Xie2006, Yamashita2002, Yamashita2006, Zarnowski2001, Zarnowski2008, ZhouZhou2007.
**1980–1999 (132):** AlbeverioMerliniTartini1989, AmlehGroveKentLadas1998, Anderson1987, AndreiMasalagiu1998, ApplegateLagarias1995a, ApplegateLagarias1995b, ApplegateLagarias1995c, Arsac1986, Ashbacher1992, Avidon1997, Baiocchi1998, Banerji1996, Barone1999, Belaga1998, BeltraminelliMerliniRusconi1994, BergMeinardus1994, BergMeinardus1995, Bernstein1994, BlazewitzPettorossi1983, Boyd1985, Brocco1995, Burckel1994, ButtsworthMatthews1990, Cadogan1984, Cadogan1991, Cadogan1996, Chamberland1996, Clark1995, ClarkLewis1995, ClarkLewis1998, CloneyGolesVichniac1987, Collatz1986, Conway1987, DevienneLebegueRoutier1993, DolanGilmanManickam1987, EiseleHadeler1990, Elliott1985, ErdosGraham1980, FeixMurielMerliniTartini1995, FeixMurielRouet1994, Filipponi1991, Flatto1992, Gale1991, Gao1993, GarciaTal1999, Garner1985, Gaschutz1982, GlaserWeigand1989, Gonnet1991, Guy1981, Guy1983a, Guy1983b, Guy1986, Hasenjager1990, Hayes1984, Hong1986, Jarvis1989, Joseph1998, Kascak1992, Kauffman1995, Klarner1981, Klarner1982, Klarner1988, KlarnerPost1992, Korec1992, Korec1994, KorecZnam1987, Krasikov1989, Kuttler1994, Lagarias1999, LagariasPortaStolarsky1993, LagariasPortaStolarsky1994, LagariasWeiss1992, LeavensVermeulen1992, Leigh1986, LethermanSchleicherWood1999, Lunkenheimer1988, Marcinkowski1999, MargensternMatiyasevich1999, Matthews1992, MatthewsLeigh1987, MatthewsWatts1984, MatthewsWatts1985, MerliniSala1999, Michel1993, Mignosi1995, Muller1991, Muller1994, OliveriVella1998, Pickover1989, PierantoniCurcic1996, Pippenger1993, Puddu1986, Qiu1997, Rawsthorne1985, Riele1983a, Riele1983b, Roubaud1993, Sander1990, ShallitWilson1991, Silva1999, Stolarsky1998, Targonski1991, Thwaites1985, Thwaites1996, Urata1999, UrataKajita1998, UrataSuzuki1996, UrataSuzukiKajita1997, Venturini1982, Venturini1989, Venturini1997, Viola1983, Wagon1985, Wang1988, Wiggin1988, Wirsching1993, Wirsching1994, Wirsching1996, Wirsching1997, Wirsching1998a, Wirsching1998b, Wu1992, Wu1993, Wu1995, Yamada1980, Yang1998, YangZhang1988, Zhang1990, ZhangYang1998, Zhou1995, Zhou1997.
**1963–1979 (35):** Allouche1979, BeelerGosperSchroeppel1972, Bringer1969, ChvatalKlarnerKnuth1972, Conway1972, Coppersmith1975, Coxeter1971, Dunn1973, ErdosGraham1979, Everett1977, Fredman1972, FredmanKnuth1974, Gardner1972, Hasse1975, Heppner1978, HoffmanKlarner1978, HoffmanKlarner1979, IsardZwicky1970, Kay1972, KlarnerRado1973, KlarnerRado1974, Mahler1968, Moller1978, Nivergelt1975, Ogilvy1972, Queneau1963, Queneau1972, Ratzan1973, Roubaud1969, Shanks1975, Stemmler1964, Terras1976, Terras1979, Tijdeman1972, TriggDodgeMeyers1976.

**Coverage of the 2020–2026 cycle entries:** 12 C + 3 P + 2 L (Nashida d/e). Of the 12 C entries, 8 were held and read this session or in the refresh. Macindoe2026 is ours. Knight2026 and Park2026 are not held. PEREIRAENZO2026b was read at its record only. The register does **not** contain Williams 2607.01718; `Williams2024` is a different author (M. Williams, ResearchGate preprint).

## 2. Search log (all 2026-10-18)

| # | Where | Query / action | Result |
|---|---|---|---|
| 1 | ccchallenge.org | index page; card fields parsed (key, year, badge, title, authors, venue, DOI/URL, wishlist, abstract) | 389 entries |
| 2 | ccchallenge.org `/htmx/paper-detail/<key>?tab=reviews` | SdW, HH, Hercher, Rozier1991, Macindoe2026 | review links only (Lagarias, zbMATH) |
| 3 | arXiv PDFs | 2005.00346, 2412.02902, 2504.13716, 2607.01718 (+abs), 1709.02979, 2008.11103, 2101.12747, 2107.08363, 2101.04067, 2112.12962, 2306.15284, 2205.10582, 2205.12724, 2307.11990, 2101.08060, 2209.14230, 1503.04661, math/0309224, math/0608208 | read / grepped (§4) |
| 4 | other open PDFs | Stokes 2021 (McMaster), Knight 2026b (Complex Systems), Rebot 2023 (LPNU), Rozier 1990 and 1991 (probleme-syracuse.fr), Steiner 1981b (fq.math.ca), Garner 1981 (AMS), Franco–Pomerance 1995 (Dartmouth), López–Stoll 2009 (Colgate), Simons 2022 NNTDM 28 (nntdm.net), SdW v1.44 (deweger.net), Hercher JIS PDF | held |
| 5 | Stack Exchange API | answer 4526766 (Rozier 2022) | held |
| 6 | Zenodo API | 23081447, 23242902, 18659804, 23122077, 21848913, 21725060, 21607750, 21017295, 20555113, 20363103, 23048411, 19874522; **20067344, 20305244, 20304354 → HTTP 410 (deleted)** | records read; PDFs held for 18659804, 21848913, 23081447, 21725060, 21670936 (Wang m≤95), 23050083 (Shimizu), 20363104 (Coppi) |
| 7 | ResearchGate | Park2026, Jesus2026 | 403, not held |
| 8 | OpenAlex | `cites:` for SdW (W2117023484), HH (W1723921989), Hercher (W4226227739); title search "Collatz m-Cycles" | 38 / 18 / 1 citing works; 9 title hits (§4.3) |
| 9 | Semantic Scholar | citations of SdW, HH, Hercher (arXiv:2201.00406) | SdW 49, HH 17 (both = refresh); **Hercher: HTTP 429 on every attempt (3 runs, backoff) — no result** |
| 10 | Crossref | `is-referenced-by-count`; `filter=references:` | SdW 19, HH 7; the cited-by list is member-only (`filter` → 400) |
| 11 | **zbMATH Open API** (not available to the refresh) | located Zbl 1136.11019 (SdW), 0863.11015 (HH), 1536.11052 (Hercher); `ci:` search | SdW cited by 3 (Feng–Fan–Ding–Wang 2012; Simons 2008; Hercher 2023); HH 0; Hercher 0 (the API returns 404 on an empty result) |
| 12 | arXiv export API (metadata; arXiv has no full-text search) | `abs:Collatz AND abs:cycles`; `abs:"m-cycles"`; `abs:"3x+1" AND abs:cycle`; `abs:Collatz AND abs:"local minima"`; `all:Hercher AND all:Collatz`; `abs:"rational cycles"` | 37 Collatz-cycle hits 2020–26 screened by title; Hercher found only itself |
| 13 | web search (extended) | Hercher citers 2025/2026 | GitHub `justinalick/collatz-m-cycles-101-lean`, `azadveersingh/collatz-research`, arXiv 2112.12962 |
| 14 | web search | López–Stoll; Simons "Exotic Collatz cycles"; Park 2026 | locations only |

Not available: Google Scholar (no tool access). Full-text arXiv search does not exist; item 12 is a metadata substitute.

## 3. Per-source table (everything read this session)

**Held** = read at source (URL, page, 2026-10-18). **Cited** = characterized only as far as a held source does.

| Source | Status | Relevant statement (quoted, page) | Part 1 / Part 2 | Verdict |
|---|---|---|---|---|
| **O. Rozier**, *Problème de Syracuse : « majorations » élémentaires des cycles*, Singularité 2 no. 5 (1991), 8–11 | **held** (`probleme-syracuse.fr/cargo/Singularit%E9_2_5.pdf`; 1.28 MB scan; pp. 8–11 read from the images) | p. 8 abstract: "we show there are only a finite number of cycles having n local minima, for every n, and we give a bound of their length." p. 8, Théorème (quoted in §0). p. 10 (5): `u_0 < (1/ln 2) n M^{14}`; p. 10 Lemme 3: `(2/a)^{M_{j−1}} 2^{m_j} − (a−2)((a−1)/(a−2))^n ≤ (a−2)u_0` (1 ≤ j ≤ n), from the 2-power divisibility at the j-th minimum; **p. 11 Lemme 4** (quoted in §0); p. 11 optimality remark (quoted in §0); p. 11 Corollaire: with `M′ ≥ 275000` (Lagarias 1985), no cycle with `n ≤ 13`. | **Part 1:** the uniform trim and its effective finiteness, in the local-minima parameter, with SdW's exponent. **Part 2:** optimality of Lemme 4 relative to Lemme 3, over real tuples (§3.2). | Part 1 **subsumed (earliest found)**. Part 2 **closest prior statement** |
| O. Rozier, *Démonstration de l'absence de cycles d'une certaine forme…*, Singularité 1 no. 3 (1990), 9–10 | **held** (register URL; scan) | p. 10 (4): `u_0 ≥ 2^m − 1` (from `2^m \| (a−2)u_0 + 1`); (5): `2^m − 1 < m^{14}/log 2`, so `m ≤ 91`, then a finite check | Circuits (1-cycles) only | no match |
| O. Rozier, math.SE answer 4526766 (2022-09-07) | **held** | "the desired bound can be proved by using Corollary 13 in Simons and de Weger (2005): `x_min < A·m·k^{13.3}`" | Uses the SdW min-element bound in `K`; no shape or sharpness statement | no match |
| R. Santos, arXiv 2005.00346 v3 (2021) | **held** | Thm 4: "for each odd number q ≥ 3, the function F_q(x) has finitely many cycles"; §2 recounts SdW's length bound | Claimed qn+1 results; no `m`-parameter cap | no match |
| M. C. Siegel, arXiv 2412.02902 (2024) | **held** (intro, main results; whole text grepped) | the Correspondence Principle (periodic points ↔ rational p-adic `z` with `χ_H(z) = x`); no hit for SdW/HH/Steiner/"local minima" | Böhm–Sontacchi in (p,q)-adic form | no match |
| A. Stokes, McMaster B.Sc. thesis (2021) | **held** | §2.2.3: SdW's "upper bound is shown to be exponential in M … it provides upper bounds for which some element in a k-cycle must be less than" | Survey restatement of part 1 | no match |
| K. Knight, *A Small Collatz Rule without the Plus One*, Complex Systems 35(1) (2026) | **held** | §5 Thm 2: "The rule K(n) takes (5/2)m steps to simulate a C(n) cycle"; "the length of any Collatz cycle must be a multiple of 5" (for the K-simulation) | Simulation bookkeeping | no match |
| P. Kosobutskyy, D. Rebot (2023) | **held** | 3n−1 cycles 5, 7, 17 "isolated from the main graph" | — | no match |
| S. Eliahou, J.-L. Verger-Gaugry, arXiv 2504.13716 (2025) | **held** | p. 4: no other cycle "can have length less than 114,208,327,604" (citing literature) | — | no match |
| D. Sha, arXiv 2112.12962 v16 (Jan 2026) | **held** | cites SdW and Hercher; "no finite nontrivial cycle is compatible with the iteration" (abstract) | Claimed proof | no match |
| J. L. Simons, *Cycles of higher-order Collatz sequences*, NNTDM 28 (2022) 48–63 | **held** | p. 49: SdW's proofs are "based on these expressions [Steiner's `x_0 = a2^k − 1`, `x_k = a3^k − 1`]" and "cannot simply be generalized"; closing remarks: further generalizations "left for further research" | Generalization; no sharpness | no match |
| J. L. Simons, arXiv 2205.10582 (2022) | **held** (§2) | SdW-type Λ bound for permutation sequences, "for fixed m a negative exponential function of L" | Part 1 transposed to another family | no match |
| O. Rozier, arXiv 2306.15284 v2 (Exp. Math. 2025) | **held** | "it is sharp with C ≈ 1" — an empirical constant in the lower-bound hypothesis for one-descent sequences | Circuit-type sequences; label "sharp" only | no match |
| N. Mghirbi, Zenodo 10.5281/zenodo.21725060 (2026-07-31) | **held** (record + PDF) | Thm 1.1: no m-cycle with `92 ≤ m ≤ 96`; inputs Barina, Hercher, SdW "K < 1.4784 m δ^m" (91 ≤ m ≤ 515,619); Remark 11.8: "The same threshold … fails first at m = 99" | Uses part 1 as an input; the ceiling stated is that of its own search | no match (landscape: m-record claim 96, unrefereed) |
| X. Wang, Zenodo 21017295 / 20555113 (2026) | **held** (m ≤ 95 PDF) | "contradicting the Simons–de Weger type upper bound" for m = 92…95 | As above | no match (landscape) |
| X. Wang, Zenodo 20067344, *Exponential Upper Bounds for the Collatz Linear Form and Exclusion of Long m-Cycles via Linear Forms in Logarithms* (2026-05-07) | **not held** (record deleted, HTTP 410; OpenAlex keeps the title only) | — | the title suggests part 1; not characterized | unchecked |
| H. Shimizu, Zenodo 23048411 (2026-09-30) | **held** | p. 4: `y_min > 2^{cK}`, `c = (λ−1)/(λ^m−1)`, "the form of Simons and de Weger (2005, Lemmas 6–7) for 3x+1, transposed"; §5 limitations: going further "needs the additional tools used for 3x+1" | Part 1 for 3x−1, later | no match |
| T. Y. K. Cheng, Zenodo 21607750 (2026-07-26) | **held** (record only; no files) | m ≤ 91 "structural contradiction" via Hercher's bound and Baker | — | no match |
| F. Coppi, Zenodo 20363103 (2026-05-24) | **held** (record + PDF grep) | "We conclude that the map T₃ admits no non-trivial cycle." | Claimed proof | no match |
| R. Hernández Reveles, Zenodo 19874522 v0.7 (2026) | **held** (record) | "Baker's theorem constrains cycles by bounding \|2^n − 3^T\| from below, but does not by itself exclude them"; "Baker bounds do not control numerator divisibility" | Folklore | no match |
| A. Gupta, arXiv 2008.11103 (2020) | **held** | Thm 5: the cycle equation over "orbs" `{u_i, d_i}` (up/down runs); open question "an upper bound on the number of cycles for a given F_k" | Block form of the cycle equation | no match |
| D. Cox, S. Ghosh, E. Sultanow, arXiv 2101.04067 v4 (2021) | **held** (full text this time) | p. 4: "staircase representing the partial sums of ⌈in/l⌉ − ⌈(i−1)n/l⌉ … where Halbeisen and Hungerbühler's logic can be used"; Cor. 2 for `3n+c` | **"Staircase" is a label here** (the Christoffel step function, length frame), not the record's staircase | no match |
| J. López, arXiv 2101.12747 (2021); Gupta et al., *Rotating Binaries*, arXiv 2107.08363 (2021); López–Stoll, Integers 9 (2009) #A13 | **held** (HH passages read) | HH's smallest element `R(m p_k/q_k)` (López); HH's boundary feature `M(l,n)` (Gupta et al.); HH's `φ` (López–Stoll Def. 13) | Length frame | no match |
| M. D. LaDue, arXiv 1709.02979 (Fibonacci Quart. 56 (2018)) | **held** (Lemma 3.1) | "For 0 ≤ i ≤ p we have T^i(m) = 3^i·2^{p−i}·(2q+1) − 1" | Not cycles. Bears on Item C (the block cascade, §5) | — |
| A. Novgorodtsev, Zenodo 21848913 v4.1 (2026-08-08) | **held** | p. 6: the forced-prefix identity "is prior-equivalent to LaDue's prefix lemma … and it is compatible with the diagonal flow in Williams' coordinate system"; §11 table lists Williams (2026) | Not cycles. Bears on Item C | — |
| Kiemes (OSF 2025), Kay (AJCM 2021), Ziauddin (IJFMR 2026) | abstracts via OpenAlex | cycle-length lower bound 1.7·10^10 steps; "virtually proved using probability theory"; prime maps | — | no match |
| Title-only citers (OpenAlex/S2): *Collatz Array* (MJMS 2020), *Pruning the binary tree* (2020), *Hilbert hotel* (2020/21), *Complete induction* (Mathematics 2022), *Permutation patterns* (arXiv 2308.00644), *Furstenberg topology* (Axioms 2025), Douzi arXiv 2205.12724 (grep: SdW in references only) | titles screened | — | none is cycle-sharpness by title | unchecked beyond titles |

### 3.1 Part 1 — the implication written out

Rozier's Lemme 4 at `a = 3` (`α = L = log₂3`), with `n` local minima and `M` odd steps, reads `2^{((L−1)/(L^n−1))M} ≤ u_0 + 2^n`. With (5), `u_0 < n M^{14}/ln 2`, this gives `((L−1)/(L^n−1))·M < log₂(n M^{14}/ln 2 + 2^n)`, and since the right side is `≤ n + 14·log₂M + O(1)`, `M = O(n·L^n)` for every `n`, explicitly. In the record's dictionary (`n_Rozier = p`, `M = n_record`, local minima = block starts, as fixed in the refresh's §4.3), this is Theorem 12.8.1's inequality `γ + log₂p > (L−1)n/(L^p−1)` in a different guise. It caps `log₂` of the smallest element rather than `γ`; the two are linked through `u_0 ≈ R/q`. It also carries Corollary 12.8.2's effective finiteness. The irrationality measure (`μ = 15`, quoted from Waldschmidt) is weaker than Rhin's, but effective. Rozier's additive `2^n` term makes the bound vacuous until `M ≳ n L^n/(L−1)`, exactly where the record's trim also begins to bite. **Verdict: part 1 subsumed, earliest found Rozier 1991; explicit constants and computation SdW 2005; finiteness for each `m` also Brox 2000.**

### 3.2 Part 2 — what Rozier's optimality remark anticipates and what it lacks

The implication, written out. Lemme 3 gives, at each minimum `j`, a lower bound for `(a−2)u_0` whose leading term is `(2/a)^{M_{j−1}}·2^{m_j} = 2^{m_j − (α−1)M_{j−1}}`. Lemme 4 bounds `max_j` of these from below by its minimum over all positive real tuples with `Σm_j = M`. Rozier says this minimum is attained where all `n` terms are equal. That gives `m_j − (α−1)M_{j−1} = c` for every `j`, hence `m_j = c·α^{j−1}` and `c = (α−1)M/(α^n−1)`: the bound `2^{((α−1)/(α^n−1))M}` is then **attained** by the relaxation, and the extremal profile is **geometric growth of the run lengths at ratio `log₂3`**. That is the staircase's profile (cycles.md 12.8.3: "blocks growing geometrically at ratio ≈ log₂3"). So Rozier 1991 states, with the minimax argument, that the exponential-in-`n` loss cannot be removed from the inequality system of Lemme 3 without using further properties of the `m_i`. That is part 2's content for a *relaxed* system, in the right parameter, 14 years before SdW p. 69.

**What it lacks** (each is in the record):
1. Integrality of the `m_i`. The optimum is over real tuples.
2. The exit lengths `m′_i` and the actual configuration. Lemme 3 is one necessary inequality per minimum, and the remark does not show that any parity pattern meets *every* size condition (every rotation's `q ≤ R_r`, i.e. every `a_i ≥ 1`) at that profile. The staircase does: an integer construction at every `p`, all rotations, by construction (12.8.6.2).
3. Bounded slack. No statement on `γ`. The record's `γ` bracket `[3.683012, 5.140212]` and the availability theorem from `8 − 5·log₂3` are not anticipated.
4. The divisibility moral. Rozier's "si l'on ne prend pas en compte d'autres propriétés éventuelles des (m_i)" points at it but does not name divisibility. HH 1997 p. 238 (length frame) still holds the closest statement of that moral.
5. The staircase–divergence reading (12.8.4). Not found.

**Verdict: part 2 still partially anticipated.** The closest prior statements are now Rozier 1991 p. 11 (an optimality remark with argument, real relaxation, `m` frame), SdW 2005 p. 69 (a belief, `m` frame), and HH 1997 pp. 230–238 (proof, length frame). The claimable residue narrows from "settling SdW's expectation" to **"realizing Rozier's real-relaxation extremal by integer configurations that meet every rotation's size condition at bounded slack, at every period"**.

## 4. Item B — the forward-citation log

| Index | SdW 2005 (10.4064/aa117-1-3) | HH 1997 (10.4064/aa-78-3-227-239) | Hercher 2023 (arXiv:2201.00406; JIS 26) |
|---|---|---|---|
| OpenAlex `cites:` | 38 works (2020–26: 12) | 18 (2020–26: 7) | 1 (an OSF 2024 proof claim); the JIS version is not separately indexed |
| Semantic Scholar | 49 (= refresh; 2020–26: 18) | 17 (= refresh; 2020–26: 5) | **429 on every attempt — no data** |
| Crossref | `is-referenced-by-count` 19; list member-only | 7; list member-only | no DOI (JIS) |
| zbMATH Open `ci:` | 3: Feng et al. 2012, Simons 2008, Hercher 2023 | 0 | 0 |
| arXiv metadata | — | — | only itself (`all:Hercher AND all:Collatz`) |
| Web search | — | — | 2 GitHub Lean projects, Sha arXiv 2112.12962, Mghirbi Zenodo 21725060 (cites it, found via OpenAlex title search, not via `cites:`) |

**2020–2026 citing works and their reading:** SdW citers: Santos 2020, Gupta 2020, Sha 2021–26, Lagarias 2021 (refresh), Simons 2022 NNTDM, Simons 2022 arXiv 2205.10582, Douzi 2022, Rozier 2023/25 (abc), Rozier–Terracol 2025 (register; not cycles), Hernández Reveles 2026, Shimizu 2026, Hercher 2022 (held) — read as in §3. *Collatz Array* 2020, *Pruning* 2020, *Hilbert hotel* 2020/21, *Complete induction* 2022, *An elementary proof of the Syracuse conjecture* 2022, *Permutation patterns* 2023, *Furstenberg* 2025, Kiemes 2025, Ziauddin 2026: titles or abstracts only. HH citers: Cox–Ghosh–Sultanow 2021 (both records), López 2021, *Rotating Binaries* 2021/22, Kay 2021 (abstract), Knight 2026 (cited) — all length frame. Hercher citers: Sha 2021–26, Mghirbi 2026, the OSF 2024 claim (title).

**None of the 2020–2026 forward citations states or proves part 2, in any parameter.** The only new anticipation found in this window, Rozier 1991, was found through the register, not through forward citation. No index links it to SdW, HH or Hercher.

## 5. Item C — Williams, arXiv:2607.01718

**Held:** J. Williams, *A Coordinate System for Collatz Dynamics*, arXiv:2607.01718 v1 (submitted 2 Jul 2026; no later version on the abs page, 2026-10-18), 21 pp., read in full.

**Ceiling question:** no cycle content. It cites Knight 2026 and poses its open problem (5), relating Knight's parity vectors to skeleton paths. Nothing bears on part 1 or 2.

**Coordinate question — it bears directly on paper 1's coordinate claims.**
1. **Exact dictionary.** Williams writes every odd `n` as `n = λ·2^a·3^b − 1`, `gcd(λ, 6) = 1`, `a ≥ 1` (p. 2, Lemma 2.14). Paper 1 (v3, Def. 2.1 and Prop. 2.3) writes `x + 1 = 2^m 3^a ω`, `3 ∤ ω`, with state `(ω, d)`, `d = m + a`. So **λ = ω**, Williams' `a` = paper's `m`, Williams' `b` = paper's `a`, and Williams's **row index `k = a + b` = the paper's depth `d`**.
   - Her skeleton row `(λ, k)` (Prop. 3.3: `b = 0..k−1`, `a = k − b`) is exactly the paper's representative list of the reduced state `(ω, d)` (Prop. 2.3(iii): `x = 2^{d−a}3^aω − 1`, `0 ≤ a ≤ d−1`).
   - Her diagonal flow `(a, b) → (a−1, b+1)` (Thm 3.6, "row index preserved", Cor. 3.8) is Prop. 2.3(i), the block cascade.
   - Her boundary exit (Prop. 3.10: `v₂(3n+1) = 1 + v₂(λ3^{b+1} − 1)`, next odd = the odd part of `λ3^{b+1} − 1`) is Prop. 2.3(ii): `x_exit = A/2^s`, `A = 3^dω − 1`.
2. **Her open problem (1)**, "the map sending one skeleton to the next has no known closed form. A complete characterization of this transition map would give a description of Collatz dynamics in skeleton coordinates" (p. 18), **is answered by paper 1's reduced map `F`** (Def. 2.1), together with the equivalence theorem (Thm 2.4).
   - Checked by fresh code: `python experiments/williams_coordinate_check.py > experiments/williams_coordinate_check_output.txt`. Every odd `n ≤ 200,001` (100,001 values, 66,668 distinct rows) gives 0 failures on all five identities, the last being `R(next odd) = F(R(n))` at every boundary exit.
3. **Dates.** Williams v1: **2 Jul 2026**. Paper 1 v1 (Zenodo 10.5281/zenodo.21273548): **2026-07-09** (Zenodo API `publication_date`). **Williams is public first, by seven days**, on the state space (λ, k) and its intra-row flow. Paper 1's provenance paragraph dates the coordinates to an unpublished hand-drawn note of 13 March 2023. That is not a public record. Neither paper cites the other.
4. **What is older than both.** The cascade itself is classical:
   - Steiner's 1977 parametrization `x_0 = a2^k − 1`, `x_k = a3^k − 1` (quoted by Simons, NNTDM 28 (2022) p. 49, held);
   - Rozier 1990 (4): `2^m | (a−2)u_0 + 1` (held);
   - LaDue, Fibonacci Quart. 56 (2018), Lemma 3.1(1) (arXiv 1709.02979, held);
   - Novgorodtsev 2026b, who already links LaDue's prefix lemma to Williams' diagonal flow (held).

   The record's existing concession ("Block-like decompositions … are classical", v3 p. 2; publication.md) already covers this. What Williams adds against the record is the **3-split and the row index**, i.e. the state `(ω, d)` itself.
5. **Consequence for `publication.md`'s "Reduced blocks / states `(ω, d)`" line.** It currently reads "not found in this exact form". **It is now found in this exact form**: the state, its fibre and the intra-block flow, independently, in Williams 2026, one week before paper 1 v1. Not found in Williams:
   - the induced self-map `F` and the conjugacy/equivalence (Thm 2.4, which Williams poses as open problem (1));
   - the anchor and every law built on it;
   - the cycle apparatus.

**Williams verdict.** No bearing on the ceiling. Direct bearing on the coordinate claim: the state space `(ω, d)` and the cascade are Williams 2026 (and classical for the cascade), contemporaneous and one week earlier. Paper 1's coordinate-level claim narrows to the induced map `F` and the equivalence theorem, plus everything downstream. **v4 should cite it** — in the related-work paragraph, next to the "reduced coordinate system itself … is the human author's invention" sentence, as an independent publication of the same coordinates (a suggested wording is in §6). LaDue 2018 could be cited for the cascade formula; this is optional, since the cascade is already conceded as classical.

## 6. For the main session

**Proposed `publication.md` changes** (not applied; owner's page):
- **12.8 line:** in the refresh's proposed wording (`briefs/ceiling-novelty-refresh-findings.md` §5.1), prepend the earliest attribution for the trim: "first in Rozier 1991 (Singularité 2 no. 5, pp. 8–11: finiteness for every number of local minima with Lemme 4's exponent `(α−1)/(α^n−1)`), explicit in Simons–de Weger 2005, Lemma 7 …". In the sharpness sentence, put Rozier 1991 p. 11 first: "Rozier observes, with a minimax over real run-length tuples, that the bound is optimal given his per-minimum inequalities, the extremal tuple growing geometrically at ratio `log₂3`; Simons–de Weger state the same as a belief (p. 69) …". Restate the residue as "realizing that extremal by integer configurations meeting every rotation's size condition at bounded slack, at every period".
- **Reduced-blocks line:** "*contemporaneous independent publication.* The state `(ω, d)` — odd core prime to 6 and depth `m + a` — with its representative fibre and intra-block cascade appears as the skeleton row `(λ, k = a + b)` of J. Williams, arXiv:2607.01718 (2 Jul 2026, one week before paper 1 v1), which leaves the row-exit map open; the induced map `F` and its equivalence theorem are paper 1's. The cascade itself is classical (Steiner's `a2^k − 1 → a3^k − 1`; LaDue 2018 Lemma 3.1). Checked 2026-10-18 (`experiments/williams_coordinate_check.py`)."
- **Collateral, flagged and not adjudicated:** paper 1 v3's provenance sentence ("The reduced coordinate system itself — the odd core ('seed'), the block cascade, the states (ω,d) … is the human author's invention") is true as a statement about independent origin. Read as priority, it is contradicted by the public record for the cascade (classical) and for the states (Williams, a week earlier).

**Citations owed (in addition to the refresh's §5.2):** paper 1 v4 → Rozier 1991 (Thm 4.5 attribution; Thm 4.6's closest prior remark) and Williams 2026 (coordinates). The joint note → Rozier 1991 alongside SdW p. 69 and HH p. 238, for the obstruction it locates. The abstract's "main new theorem" sentence (also on the ccchallenge `Macindoe2026` card) now overclaims for part 1 on three counts (Rozier 1991, SdW 2005, Brox 2000).

**For the author to decide:**
1. How v4 frames the sharpness residue. The refresh's "settling Simons–de Weger's 2005 expectation" is no longer the right framing: Rozier 1991 had already given the extremal profile for the relaxed system. The residue is its integer, all-rotations, bounded-slack realization.
2. How v4 states provenance for `(ω, d)` given Williams' one-week public priority, and whether `F` (which answers Williams's open problem (1)) is worth saying so in v4.
3. Whether to contact anyone. Rozier is active (register entries 2017–2025; the 2022 SE answer) and is the natural reader of the residue. Williams is the natural reader of `F`. Nothing outward was done.
4. Whether to pursue the Semantic Scholar Hercher gap further (an API key would lift the 429). zbMATH and OpenAlex both return 0–1 Hercher citers, so the gap is now small.

## 7. Record

- **Script:** `experiments/williams_coordinate_check.py`, fresh code, exact integer arithmetic. One command: `python experiments/williams_coordinate_check.py > experiments/williams_coordinate_check_output.txt`, committed output **ALL CHECKS PASS** (100,001 odd `n`; 0 failures). No cycle search, no divisibility test, in compliance with the README stopping rules.
- No computation was needed for Rozier 1991. The minimax in §3.2 is a two-line derivation, written out there.
- Held sources (scratchpad, not committed): every PDF and record named in §3 and §5. Not held: Knight 2026, Park 2026, De Jesus 2026, Steiner 1981a, Wang 20067344 (deleted), Chamberland's survey and Wirsching's LNM 1681 (as in the refresh).
- No wiki page, paper or joint note was edited.
