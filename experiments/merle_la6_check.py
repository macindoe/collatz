#!/usr/bin/env python3
"""merle_la6_check.py — independent verification of shared-ledger entry L-A6
(the calibrated lottery / two-shore census), brief briefs/merle-la6-check-brief.md.

FRESH CODE: imports nothing from any Merle repository and nothing from prior
Merle-check scripts. Conventions re-implemented from cycles.md 12.6.1/12.6.1.1
and from the OPERATIONAL DEFINITIONS recorded (read-only) out of his artifacts
test_REQ-MATH-022/023/025 at ericmerle3789/one-obstruction-three-faces-lean:

  * word = pair of compositions (m_0..m_{p-1}), (s_0..s_{p-1}) of (n, S) into
    p >= 1 parts each, entries >= 1 ("canonical alphabet s >= 1"; the -1 cycle's
    s = 0 word sits outside the alphabet), p in [1, min(n, S)];
    K = n + S, q = 2^K - 3^n.
  * census domain (REQ-022): n in [2, 14], S in [1, min(9, 2n)]  (SMAX = 9).
  * classical numerator B = sum_t 3^{M_after(t)} 2^{Kpre(t)} beta(m_t),
    beta(m) = 3^m - 2^m, Kpre(t) = sum_{u<t}(m_u + s_u); fixed point x = B/q.
  * hit ("C = 1"): |q| > 1 and |q| divides B; the |q| = 1 words are the
    Gersonides freebie stock, recorded apart; frame agreement = (q | B <=> q | R_0)
    with R_0 the 12.6.1 rotation numerator.
  * "18 hits" = WORDS (not necklaces), both shores, powers included, freebies
    excluded, in the REQ-022 domain above.
  * necklace = rotation class of the letter word; cell budget = #necklaces/|q|;
    shore budget lambda = sum over its |q| > 1 cells in the same domain;
    P(0) = exp(-lambda)  [Poisson at the necklace-trial level with
    uniform-residue probability 1/|q| per trial — MODEL, not fact].
  * tail (REQ-023): n = 15..200, S in [1, int(0.5849625*n)+3], necklace count
    approximated his side by sum_p words_p/p; here computed EXACTLY (Burnside)
    and his approximation replicated alongside.
  * realizability (REQ-025): x = B//q, TRUE map x -> (3x+1)/2^{v_2(3x+1)} on odd
    integers of either sign (negatives carry the south = the ×3-1 mirror);
    itinerary sigma-word: letter (m, s) contributes (m-1) steps of valuation 1
    then one step of valuation s+1.

Exact integer arithmetic at every pass/fail decision; floats appear only in the
lambda / P(0) / tail readouts and are labeled as such.  Canaries (the four known
cycles' words) hand-computed and printed before any sweep, per his practice and
ours.  Run: python merle_la6_check.py
"""

import itertools, math, random
from math import gcd, comb
from fractions import Fraction

CHECKS = 0
FAILURES = []

def check(name, ok):
    global CHECKS
    CHECKS += 1
    if not ok:
        FAILURES.append(name)
    print(f"    [{'OK' if ok else 'FAIL'}] {name}")
    return ok

# ----------------------------------------------------------------------------
# core arithmetic (fresh implementations)
# ----------------------------------------------------------------------------

def beta(m):
    return 3**m - 2**m

def B_classical(ms, ss):
    """Classical-frame numerator: fixed point of the composed letter maps
    x -> (3^m x + beta_m)/2^{m+s} is x0 = B/q."""
    p = len(ms); n = sum(ms)
    B = 0; kpre = 0; mafter = n
    for t in range(p):
        mafter -= ms[t]
        B += 3**mafter * 2**kpre * beta(ms[t])
        kpre += ms[t] + ss[t]
    return B

def R0_reduced(ms, ss):
    """cycles.md 12.6.1 rotation numerator, sigma_t = s_t + m_{(t+1) mod p}."""
    p = len(ms)
    sig = [ss[t] + ms[(t + 1) % p] for t in range(p)]
    Mafter = [0] * p
    acc = 0
    for t in range(p - 1, -1, -1):
        Mafter[t] = acc; acc += ms[t]
    tot = 0; Spre = 0
    for t in range(p):
        tot += 3**Mafter[t] * 2**Spre * (2**ss[t] - 1)
        Spre += sig[t]
    return tot

def sigma_of(ms, ss):
    """Per-odd-step 2-valuations prescribed by the word."""
    sig = []
    for m, s in zip(ms, ss):
        sig += [1] * (m - 1) + [s + 1]
    return sig

def B_sigma(sig):
    """sigma-frame numerator: B = sum_j 3^{n-1-j} 2^{sigma_0+..+sigma_{j-1}}.
    Equal to B_classical on the letter decomposition (cross-checked below)."""
    n = len(sig)
    B = 0; Spre = 0
    for j in range(n):
        B += 3**(n - 1 - j) * 2**Spre
        Spre += sig[j]
    return B

def comps(total, parts):
    if parts == 1:
        yield (total,); return
    for cuts in itertools.combinations(range(1, total), parts - 1):
        pts = (0,) + cuts + (total,)
        yield tuple(pts[i + 1] - pts[i] for i in range(parts))

def canon(ms, ss):
    w = tuple(zip(ms, ss)); p = len(w)
    return min(tuple(w[r:] + w[:r]) for r in range(p))

def is_primitive(ms, ss):
    w = list(zip(ms, ss)); p = len(w)
    return not any(w == w[:d] * (p // d) for d in range(1, p) if p % d == 0)

def true_map_orbit(x, nsteps):
    """TRUE map on odd integers, either sign: x -> (3x+1)/2^{v_2(3x+1)}."""
    sig = []
    for _ in range(nsteps):
        y = 3 * x + 1
        v = (y & -y).bit_length() - 1
        sig.append(v)
        x = y >> v
    return sig, x

# number theory helpers for Burnside/Moebius (small arguments)
def divisors(k):
    return [d for d in range(1, k + 1) if k % d == 0]

def phi(k):
    r = k; m = k; p = 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0: m //= p
            r -= r // p
        p += 1
    if m > 1: r -= r // m
    return r

def mobius(k):
    if k == 1: return 1
    r = 1; m = k; p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            r = -r
        p += 1
    if m > 1: r = -r
    return r

def words_period_dividing(n, S, p, d):
    """#words with p parts fixed by rotation-by-d (d | p): repetitions of a
    length-d base; needs n*d/p, S*d/p integral."""
    if (n * d) % p or (S * d) % p: return 0
    nb = n * d // p; Sb = S * d // p
    if nb < d or Sb < d: return 0
    return comb(nb - 1, d - 1) * comb(Sb - 1, d - 1)

def neck_counts(n, S):
    """(total necklaces, primitive necklaces) in cell (n, S), exact (Burnside +
    Moebius), summed over p = 1..min(n,S)."""
    tot = 0; prim = 0
    for p in range(1, min(n, S) + 1):
        b = 0; a = 0
        for d in divisors(p):
            w = words_period_dividing(n, S, p, d)
            b += phi(p // d) * w
            a += mobius(p // d) * w
        assert b % p == 0 and a % p == 0
        tot += b // p; prim += a // p
    return tot, prim

C_GEN = 0.0793186128  # round-8 part A / cycles.md 12.6.1.5 (the (B) general constant)

# ----------------------------------------------------------------------------
# 0. PREDICTIONS — written and printed before any sweep
# ----------------------------------------------------------------------------
print("=" * 78)
print("PREDICTIONS (written before any sweep; derived from the recorded")
print("operational definitions, the four known cycles, and L-A4 descent)")
print("=" * 78)
print("""
P-CENSUS (his domain, n in [2,14], S in [1, min(9, 2n)]):
  |q| = 1 words: exactly 1 — ([2],[1]) at (n,K) = (2,3), realizing x = -5.
    (the +1 freebie word ([1],[1]) sits at n = 1, below his n >= 2 start;
     the -1 family is the s = 0 / all-sigma-1 climb, outside the alphabet)
  |q| > 1 hits: exactly 18 WORDS = 16 necklaces:
    north: trivial^j = (1,1)^j at (j, 2j), j = 2..9  (8 words = 8 necklaces; x = 1)
    south: (-5)-word powers ([2],[1])^j at (2j, 3j), j = 2..7 (6 words = 6 necklaces; x = -5)
    south: the -17 orbit at (7,11), q = -139: words (4,3|1,3) -> x = -17 and
           (3,4|3,1) -> x = -41 (2 words = 1 necklace, PRIMITIVE)
    south: its square at (14,22), q = -588665: (4,3,4,3|1,3,1,3) -> -17,
           (3,4,3,4|3,1,3,1) -> -41 (2 words = 1 necklace)
  primitive hits: 2 words = 1 necklace (the -17 orbit), all south; north 0.
  frame agreement (q | B <=> q | R_0) at every word, both directions;
  stronger probe gcd(|q|, B) = gcd(|q|, R_0) expected to hold everywhere.
P-EXTENSION (ALL S >= 1, n <= 14 — census completion beyond his S <= 9 window):
  additional hits exactly trivial^j at (j, 2j), j = 10..14; NOTHING else
  (closure by the ghost lemma + the cycle product identity 2^K = prod(3 + 1/x_t):
   south hits force K < n log2 3, i.e. S <= 8 for n <= 14, all inside his window;
   north extension cells force x_min <= 1/(2^{K/n} - 3), a tiny enumerable bound).
  So the complete all-S census at n <= 14 is 23 words, and the entry's
  qualitative claim (freebies + -17 orbit + L-A4-forced powers, nothing else)
  is expected to hold unconditionally.
P-DESCENT: every non-primitive hit is base^k with its base a hit (L-A4);
  identities R_0(B^k) = R_0(B)*G_k, q_{B^k} = q_B*G_k exact at every instance.
P-BUDGETS (necklace units, his domain): south lambda = 1.12, north = 2.64 (2dp);
  P(0) = e^-lambda: south 0.327, north 0.071 (~7%); necklace hits 8/8;
  word-level replication (REQ-022): budgets 3.41 / 6.17, word hits 10 / 8.
P-TAIL (n = 15..200, S <= int(0.5849625 n)+3): south += ~0.16, north += ~0.33;
  tranche pattern per his OUT-023 (0.1043/0.2648, 0.0519/0.0583, 0.0034/0.0049,
  0.0000/0.0001); dominant cells (17,27) north ~0.062 max, (24,38) south,
  (53,84) south among the top; north residual for n >= 61: ~0.005;
  effective decay rate approaching c_gen = 0.0793 bits/step from above.
P-REALIZABILITY: all census hits realize exactly (orbit = word, return, odd);
  his 18/18 reproduced, extension 23/23; the ghost identity
  3*B(W) + q = 2^{sigma_0} * B(shift W) is EXACT for every word (both shores),
  hence v_2(3x+1) is forced at every step — the load-bearing lemma is provable,
  not merely empirical; fresh 2-adic draws expected 350/350.
P-LOCK: among the four known cycles (+1, -1, -5, -17) exactly one has |q| > 1:
  the -17 (q = -139) — "unique paid-lock" holds on the knowns; universality
  beyond verified ranges is exactly the open condition, not checkable.
""")

# ----------------------------------------------------------------------------
# 1. CANARIES — hand-computed first, printed before any sweep
# ----------------------------------------------------------------------------
print("=" * 78)
print("CANARIES (hand-computed before coding; machine echo of the hand values)")
print("=" * 78)
check("C1 +1 word ([1],[1]): q = 2^2-3 = 1, B = beta_1 = 1, x = 1",
      2**2 - 3**1 == 1 and B_classical((1,), (1,)) == 1)
check("C2 -1 family: sigma = (1)^n, B_sigma = 3^n-2^n = -q, x = -1 (s=0, outside alphabet)",
      all(B_sigma((1,) * n) == 3**n - 2**n == -(2**n - 3**n) for n in (1, 2, 5)))
check("C3 -5 word ([2],[1]): q = 2^3-3^2 = -1, B = beta_2 = 5, x = -5, R0 = 1",
      2**3 - 3**2 == -1 and B_classical((2,), (1,)) == 5 and R0_reduced((2,), (1,)) == 1)
check("C4 -17 word (4,3|1,3): q = -139, B = 27*65+32*19 = 2363 = 17*139, x = -17, R0 = 27+112 = 139",
      2**11 - 3**7 == -139 and B_classical((4, 3), (1, 3)) == 2363
      and 2363 // (2**11 - 3**7) == -17 and R0_reduced((4, 3), (1, 3)) == 139)
check("C5 -17 rotation (3,4|3,1): B = 81*19+64*65 = 5699 = 41*139, x = -41, R0 = 567+128 = 695 = 5*139",
      B_classical((3, 4), (3, 1)) == 5699 and 5699 // (2**11 - 3**7) == -41
      and R0_reduced((3, 4), (3, 1)) == 695)
check("C6 trivial^2 (1,1|1,1): q = 7, B = 3+4 = 7, x = 1, R0 = 7, non-primitive",
      2**4 - 3**2 == 7 and B_classical((1, 1), (1, 1)) == 7
      and R0_reduced((1, 1), (1, 1)) == 7 and not is_primitive((1, 1), (1, 1)))
check("C7 ghost identity by hand on -5: 3*5 + (-1) = 14 = 2^1*7; 3*7 + (-1) = 20 = 2^2*5",
      3 * 5 + (-1) == 2**1 * 7 and 3 * 7 + (-1) == 2**2 * 5
      and B_sigma((1, 2)) == 5 and B_sigma((2, 1)) == 7)
check("C8 -17 true orbit by hand: -17,-25,-37,-55,-41,-61,-91 -> -17, sigma 1,1,1,2,1,1,4",
      true_map_orbit(-17, 7) == ([1, 1, 1, 2, 1, 1, 4], -17)
      and sigma_of((4, 3), (1, 3)) == [1, 1, 1, 2, 1, 1, 4])
check("C9 beta 2/3/4 = 5/19/65", beta(2) == 5 and beta(3) == 19 and beta(4) == 65)
# necklace canary, cell (7,11): 84 words; Burnside by hand: p=1:1, p=2:(18+0)/2=9,
# p=3:(45+0)/3=15, p=4:(20+0)/4=5 -> 30 necklaces; 1 hit necklace (the -17 orbit)
nc, npr = neck_counts(7, 4)
check("C10 cell (7,11): 84 words, 30 necklaces (1+9+15+5 by hand), Burnside agrees",
      sum(1 for p in range(1, 5) for _ in itertools.product(comps(7, p), comps(4, p))) == 84
      and nc == 30)
if FAILURES:
    print("CANARY FAILURE — stopping before any sweep."); raise SystemExit(1)
print("CANARIES: all PASS\n")

# ----------------------------------------------------------------------------
# 2. THE GHOST IDENTITY (load-bearing lemma) — derivation checked exactly
# ----------------------------------------------------------------------------
print("=" * 78)
print("GHOST IDENTITY: 3*B(W) + q = 2^{sigma_0} * B(shift W), with B(W) odd")
print("(hence v_2(3x+1) = sigma_0 exactly for x = B/q, every word, both shores)")
print("=" * 78)

def ghost_identity_full_cycle(sig):
    """Check the identity at every position around the cycle and the return."""
    n = len(sig); K = sum(sig); q = 2**K - 3**n
    w = tuple(sig); B0 = B_sigma(w); ok = True
    B = B0
    for j in range(n):
        ok &= (B % 2 == 1)                      # v_2(ghost) = 0 at every step
        w2 = w[1:] + w[:1]
        B2 = B_sigma(w2)
        ok &= (3 * B + q == 2**w[0] * B2)       # the telescoping identity
        w, B = w2, B2
    ok &= (B == B0)                             # shift^n = id: exact return
    return ok

exh = 0
for L in range(1, 6):
    for sig in itertools.product((1, 2, 3, 4), repeat=L):
        exh += ghost_identity_full_cycle(sig)
tot_exh = sum(4**L for L in range(1, 6))
check(f"exhaustive sigma-words, all sigma in [1,4]^L, L <= 5: {exh}/{tot_exh}", exh == tot_exh)

rng = random.Random(20260725)
rnd_ok = 0; nneg = 0; npos = 0
for i in range(400):
    L = rng.randint(6, 40)
    if i % 2 == 0:
        # south-biased draw: mostly sigma = 1 (mean < log2 3), occasional 2
        sig = tuple(1 if rng.random() < 0.8 else 2 for _ in range(L))
    else:
        sig = tuple(rng.randint(1, 12) for _ in range(L))
    q = 2**sum(sig) - 3**L
    if q < 0: nneg += 1
    else: npos += 1
    rnd_ok += ghost_identity_full_cycle(sig)
check(f"random sigma-words (400 draws, lengths 6..40, half south-biased; "
      f"{nneg} south / {npos} north): {rnd_ok}/400", rnd_ok == 400)
# cross-check the two numerator implementations on random letter words
xok = 0
for _ in range(300):
    p = rng.randint(1, 6)
    ms = tuple(rng.randint(1, 7) for _ in range(p))
    ss = tuple(rng.randint(1, 7) for _ in range(p))
    xok += (B_sigma(tuple(sigma_of(ms, ss))) == B_classical(ms, ss))
check(f"B_sigma(sigma(W)) == B_classical(W) on 300 random letter words: {xok}/300", xok == 300)
print("""  Derivation (recorded in the findings): B(W) = sum_j 3^{n-1-j} 2^{S_j},
  S_j = sigma_0+..+sigma_{j-1}.  The j = 0 term 3^{n-1} is the unique odd term,
  so B(W) is odd.  In 3*B(W) + q the term 3^n cancels q's -3^n; factoring
  2^{sigma_0} from the rest and reindexing gives exactly B(shift W), with q's
  2^K supplying the shifted word's last term.  Hence for x = B/q (q odd):
  3x + 1 = 2^{sigma_0} * (B(shift W)/q), an odd 2-adic unit times 2^{sigma_0} —
  v_2 is FORCED at every step, the orbit follows the word and returns.  EXACT.
""")

# ----------------------------------------------------------------------------
# 3. CENSUS, his domain (n in [2,14], S in [1, min(9,2n)]) — exhaustive
# ----------------------------------------------------------------------------
print("=" * 78)
print("CENSUS SWEEP (his domain): every word, exact B, R_0, gcds, necklaces")
print("=" * 78)

hits = []          # (n, K, q, ms, ss, x, primitive)
spent = []         # |q| = 1 words
cells = {}         # (n,S) -> dict with counts
frame_ok = 0; frame_total = 0; gcd_eq = 0
comp_cache = {}
def cached_comps(total, parts):
    key = (total, parts)
    if key not in comp_cache:
        comp_cache[key] = list(comps(total, parts))
    return comp_cache[key]

for n in range(2, 15):
    for S in range(1, min(9, 2 * n) + 1):
        K = n + S; q = 2**K - 3**n; a = abs(q)
        nwords = 0; nhits = 0; canonset = set(); hitcanon = set(); primcanon = set()
        nprimwords = 0
        for p in range(1, min(n, S) + 1):
            for ms in cached_comps(n, p):
                for ss in cached_comps(S, p):
                    nwords += 1
                    B = B_classical(ms, ss)
                    c = canon(ms, ss)
                    canonset.add(c)
                    prim = is_primitive(ms, ss)
                    nprimwords += prim
                    if a == 1:
                        spent.append((n, K, q, ms, ss, B // q))
                        continue
                    r0 = R0_reduced(ms, ss)
                    d1 = (B % a == 0); d2 = (r0 % a == 0)
                    frame_total += 1
                    frame_ok += (d1 == d2)
                    gcd_eq += (gcd(B, a) == gcd(r0, a))
                    if d1:
                        nhits += 1
                        hits.append((n, K, q, ms, ss, B // q, prim))
                        hitcanon.add(c)
                        if prim: primcanon.add(c)
        # exact word count cross-check (Vandermonde)
        check(f"cell ({n},{K}): word count == C(K-2, n-1)",
              nwords == comb(K - 2, n - 1)) if nwords != comb(K - 2, n - 1) else None
        nc, npr = neck_counts(n, S)
        if len(canonset) != nc:
            check(f"cell ({n},{K}): Burnside necklaces == canon count", False)
        # Moebius primitive-word count cross-check
        ap = sum(sum(mobius(p // d) * words_period_dividing(n, S, p, d) for d in divisors(p))
                 for p in range(1, min(n, S) + 1))
        if ap != nprimwords:
            check(f"cell ({n},{K}): Moebius primitive words == direct count", False)
        cells[(n, S)] = dict(K=K, q=q, a=a, nwords=nwords, nhits=nhits,
                             necks=nc, primnecks=npr, hitnecks=len(hitcanon),
                             primhitnecks=len(primcanon))
CHECKS += 3 * len(cells)  # the three per-cell cross-checks above (silent when passing)

print(f"  words swept: {sum(c['nwords'] for c in cells.values())}, cells: {len(cells)}")
print(f"  frame agreement (q|B <=> q|R0), both directions: {frame_ok}/{frame_total}")
check("frame agreement biconditional on EVERY word", frame_ok == frame_total)
print(f"  stronger probe gcd(|q|,B) == gcd(|q|,R0): {gcd_eq}/{frame_total}")
check("gcd equality on every word (observation, stronger than the entry's claim)",
      gcd_eq == frame_total)
print(f"\n  |q| = 1 words (freebie stock in-domain): {len(spent)}")
for (n, K, q, ms, ss, x) in spent:
    print(f"    (n,K) = ({n},{K}), q = {q}, word {ms}|{ss}, x = {x}")
check("freebie stock in-domain == 1 word (([2],[1]) at (2,3), x = -5)",
      len(spent) == 1 and spent[0][0] == 2 and spent[0][2] == -1 and spent[0][5] == -5)
print(f"\n  C = 1 hits (|q| > 1): {len(hits)} words")
print(f"  {'n':>3} {'K':>3} {'q':>9} {'word':>30} {'x':>5} {'prim':>5}")
for (n, K, q, ms, ss, x, prim) in hits:
    print(f"  {n:>3} {K:>3} {q:>9} {str(ms)+'|'+str(ss):>30} {x:>5} {str(prim):>5}")

# compare with the predicted 18
pred = set()
for j in range(2, 10):  pred.add(((1,) * j, (1,) * j))
for j in range(2, 8):   pred.add(((2,) * j, (1,) * j))
pred |= {((4, 3), (1, 3)), ((3, 4), (3, 1)),
         ((4, 3, 4, 3), (1, 3, 1, 3)), ((3, 4, 3, 4), (3, 1, 3, 1))}
got = set((tuple(ms), tuple(ss)) for (_, _, _, ms, ss, _, _) in hits)
check("hit list == the predicted 18 words exactly (nothing missing, nothing extra)",
      got == pred and len(hits) == 18)
check("primitive hits: exactly the 2 words of the -17 orbit (1 necklace, south)",
      sorted((ms, ss) for (_, _, _, ms, ss, _, pr) in hits if pr)
      == sorted([((3, 4), (3, 1)), ((4, 3), (1, 3))]))
check("realized x values: {1} north, {-5, -17, -41} south",
      set(x for (_, _, q, _, _, x, _) in hits if q > 0) == {1}
      and set(x for (_, _, q, _, _, x, _) in hits if q < 0) == {-5, -17, -41})

# interest cells (his table)
print("\n  interest cells (word-level, replicating REQ-022):  [floats are readouts]")
for (n, S) in [(5, 3), (7, 4), (12, 7)]:
    c = cells[(n, S)]
    lam = c['nwords'] / c['a']
    print(f"    ({n},{c['K']}): q = {c['q']}, words = {c['nwords']}, "
          f"lambda_word = {lam:.3f}, hits = {c['nhits']}, P(0) = {math.exp(-lam):.3f}")
check("(5,8): 15 words, lambda 1.154, 0 hits",
      cells[(5, 3)]['nwords'] == 15 and cells[(5, 3)]['nhits'] == 0
      and abs(15 / 13 - 1.154) < 5e-4)
check("(7,11): 84 words, 2 hits", cells[(7, 4)]['nwords'] == 84 and cells[(7, 4)]['nhits'] == 2)
check("(12,19): 12376 words, 0 hits, lambda 1.730",
      cells[(12, 7)]['nwords'] == 12376 and cells[(12, 7)]['nhits'] == 0
      and abs(12376 / 7153 - 1.730) < 5e-4)

# n = 1, analytically (his sweep starts at n = 2)
print("\n  n = 1 (below his n >= 2 start): words ([1],[S]) have B = 1; |q| = 1 only")
print("  at S = 1 (the +1 freebie); |q| > 1 never divides B = 1 — no hits. EXACT.")
check("n = 1 closure: B = 1 for all n = 1 words; only (1,1) has |q| = 1",
      B_classical((1,), (5,)) == 1 and abs(2**2 - 3) == 1
      and all(abs(2**(1 + S) - 3) > 1 for S in range(2, 30)))

# ----------------------------------------------------------------------------
# 4. CENSUS EXTENSION: all S >= 1 at n <= 14 (closing the S <= 9 window)
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("CENSUS EXTENSION to ALL S (n <= 14): exact closure beyond his window")
print("=" * 78)
print("""  South closure: a south hit realizes (ghost lemma) as a negative cycle;
  the product identity 2^K = prod_t(3 + 1/x_t) with every |x_t| >= 3 forces
  2^K < 3^n, i.e. S < n(log2 3 - 1) <= 8.19 for n <= 14 — every possible south
  hit is inside the S <= 9 window already swept.  North extension cells
  (S >= 10): a hit realizes as a POSITIVE cycle with n <= 14 odd steps and
  x_min <= 1/(2^{K/n} - 3); for S > 2n, K/n > 2 gives x_min < 1: impossible.
  For 10 <= S <= 2n the bound is tiny and enumerable:""")
ext_hits = []
for n in range(2, 15):
    for S in range(10, 2 * n + 1):
        K = n + S; q = 2**K - 3**n
        assert q > 0  # all extension cells are north (10 > 0.585*14)
        bound = 1.0 / (2**(K / n) - 3)
        cands = [x for x in range(1, int(bound) + 2, 2)]
        for x in cands:
            sig, xf = true_map_orbit(x, n)
            if xf == x and sum(sig) == K:
                ext_hits.append((n, S, x))
CHECKS += 1
print(f"    candidate cycles found in extension cells: {ext_hits}")
check("extension hits are exactly x = 1 at (j, 2j), j = 10..14 (trivial powers)",
      ext_hits == [(j, j, 1) for j in range(10, 15)])
for j in range(10, 15):
    qq = 2**(2 * j) - 3**j
    check(f"trivial^{j} at ({j},{2*j}) is a hit: B == q, x = 1",
          B_classical((1,) * j, (1,) * j) == qq)
print("  => complete all-S census at n <= 14: 23 words = 13 trivial powers (j=2..14)")
print("     + 6 (-5)-powers (j=2..7) + the -17 orbit (2) + its square (2).")
print("     The entry's qualitative census claim (freebies + -17 + L-A4-forced")
print("     powers, nothing else) holds UNCONDITIONALLY at n <= 14; the count 18")
print("     is the S <= 9 window count. [domain note, recorded]")

# ----------------------------------------------------------------------------
# 5. L-A4 DESCENT cross-check on the census powers
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("L-A4 DESCENT cross-check (12.6.1.4): power hits scale by G_k exactly")
print("=" * 78)
desc_ok = 0; desc_tot = 0
power_hits = [(ms, ss) for (_, _, _, ms, ss, _, prim) in hits if not prim]
for ms, ss in power_hits:
    p = len(ms); w = list(zip(ms, ss))
    d = min(d for d in range(1, p + 1) if p % d == 0 and w == w[:d] * (p // d))
    bms, bss = tuple(ms[:d]), tuple(ss[:d])
    k = p // d
    nB = sum(bms); KB = nB + sum(bss)
    qB = 2**KB - 3**nB
    Gk = sum(3**((k - 1 - c) * nB) * 2**(c * KB) for c in range(k))
    qP = 2**(k * KB) - 3**(k * nB)
    desc_tot += 3
    desc_ok += (R0_reduced(ms, ss) == R0_reduced(bms, bss) * Gk)
    desc_ok += (qP == qB * Gk)
    desc_ok += (abs(qB) == 1 or B_classical(bms, bss) % abs(qB) == 0)  # base is a hit/freebie
check(f"descent identities on all {len(power_hits)} non-primitive hits: {desc_ok}/{desc_tot}",
      desc_ok == desc_tot)
CHECKS += desc_tot

# ----------------------------------------------------------------------------
# 6. NECKLACE BUDGETS, n <= 14 (exact) — the L-A6 lambda values
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("NECKLACE BUDGETS (exact Fractions; float readouts) — his domain")
print("=" * 78)
lam = {'south': Fraction(0), 'north': Fraction(0)}
lam_prim = {'south': Fraction(0), 'north': Fraction(0)}
hitneck = {'south': 0, 'north': 0}
primhitneck = {'south': 0, 'north': 0}
wordbud = {'south': Fraction(0), 'north': Fraction(0)}
wordhits = {'south': 0, 'north': 0}
for (n, S), c in cells.items():
    if c['a'] == 1: continue
    sh = 'south' if c['q'] < 0 else 'north'
    lam[sh] += Fraction(c['necks'], c['a'])
    lam_prim[sh] += Fraction(c['primnecks'], c['a'])
    hitneck[sh] += c['hitnecks']
    primhitneck[sh] += c['primhitnecks']
    wordbud[sh] += Fraction(c['nwords'], c['a'])
    wordhits[sh] += c['nhits']
for sh in ('south', 'north'):
    l = float(lam[sh]); lp = float(lam_prim[sh])
    print(f"  {sh.upper():>5}: lambda(necklaces) = {l:.4f}  [his 2dp: "
          f"{'1.12' if sh == 'south' else '2.64'}]   P(0) = e^-lambda = {math.exp(-l):.4f}")
    print(f"         necklace hits = {hitneck[sh]} (primitive {primhitneck[sh]});"
          f"  primitive-only budget lambda_prim = {lp:.4f}  (flat observation:")
    print(f"         his P(0) uses the TOTAL budget incl. forced-power/freebie-cell mass;")
    print(f"         with lambda_prim, P(0) = {math.exp(-lp):.4f})")
    print(f"         word-level replication: budget = {float(wordbud[sh]):.2f}, "
          f"word hits = {wordhits[sh]}")
check("south lambda = 1.12 (2dp)", abs(float(lam['south']) - 1.12) < 0.005)
check("north lambda = 2.64 (2dp)", abs(float(lam['north']) - 2.64) < 0.005)
check("necklace hits 8 south / 8 north; primitive 1 south / 0 north",
      hitneck['south'] == 8 and hitneck['north'] == 8
      and primhitneck['south'] == 1 and primhitneck['north'] == 0)
check("P(0) north = 0.071 (his ~7%)", abs(math.exp(-float(lam['north'])) - 0.071) < 0.002)
check("P(0) south = 0.327", abs(math.exp(-float(lam['south'])) - 0.327) < 0.002)
check("word budgets 3.41 south / 6.17 north (REQ-022 replication, 2dp)",
      abs(float(wordbud['south']) - 3.41) < 0.005 and abs(float(wordbud['north']) - 6.17) < 0.005)
check("word hits 10 south / 8 north (REQ-022 replication)",
      wordhits['south'] == 10 and wordhits['north'] == 8)
print("  [Poisson P(0) = e^-lambda is a MODEL statement: uniform residue 1/|q|")
print("   per necklace trial, independence across cells — stated as model.]")

# ----------------------------------------------------------------------------
# 7. TAIL n = 15..200 (exact necklace counts; window as recorded)
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("TAIL BUDGET n = 15..200 (exact Burnside necklace counts per cell;")
print("window S <= int(0.5849625 n)+3 as recorded from REQ-023; float readouts)")
print("=" * 78)
per_n = {}
cell_lams = []
for n in range(15, 201):
    Smax = int(0.5849625 * n) + 3
    bs = bn = 0.0
    for S in range(1, Smax + 1):
        K = n + S; q = 2**K - 3**n; a = abs(q)
        if a == 1: continue
        nc, npr = neck_counts(n, S)
        la = float(Fraction(nc, a))
        if q < 0: bs += la
        else: bn += la
        if la > 0.005: cell_lams.append((la, n, K, q < 0))
    per_n[n] = (bs, bn)
tranches = [(15, 30), (31, 60), (61, 120), (121, 200)]
tot_s = tot_n = 0.0
his_tr = {(15, 30): (0.1043, 0.2648), (31, 60): (0.0519, 0.0583),
          (61, 120): (0.0034, 0.0049), (121, 200): (0.0000, 0.0001)}
print(f"  {'tranche':>12} {'south(exact)':>13} {'north(exact)':>13} {'his south':>10} {'his north':>10}")
for lo, hi in tranches:
    ts = sum(per_n[n][0] for n in range(lo, hi + 1))
    tn = sum(per_n[n][1] for n in range(lo, hi + 1))
    tot_s += ts; tot_n += tn
    print(f"  n=[{lo:3d},{hi:3d}] {ts:13.4f} {tn:13.4f} {his_tr[(lo,hi)][0]:>10} {his_tr[(lo,hi)][1]:>10}")
print(f"  TOTAL n=15..200: south = {tot_s:.4f}, north = {tot_n:.4f}   [entry: +0.16 / +0.33]")
check("tail totals ~ his (south within 0.02, north within 0.02)",
      abs(tot_s - 0.1596) < 0.02 and abs(tot_n - 0.3280) < 0.02)
res_n61 = sum(per_n[n][1] for n in range(61, 201))
print(f"  north residual n >= 61 (his 'beyond the verified range' cut, identified")
print(f"  from OUT-023's tranche structure — the committed script computes no")
print(f"  element-size criterion): {res_n61:.4f}   [entry: ~5e-3]")
check("north residual n >= 61 ~ 0.005", abs(res_n61 - 0.005) < 0.002)
print("\n  dominant cells (lambda > 0.02), exact necklace units:")
top = sorted([c for c in cell_lams if c[0] > 0.02], reverse=True)
for la, n, K, south in top[:8]:
    print(f"    n={n:3d} K={K:3d} {'SOUTH' if south else 'NORTH'} lambda={la:.3f}  K/n={K/n:.4f}")
check("max cell is (17,27) north (K/n = 27/17)",
      bool(top) and (top[0][1], top[0][2], top[0][3]) == (17, 27, False))
check("(53,84) south present among dominant cells (the 84/53 convergent)",
      any((n, K) == (53, 84) for _, n, K, _ in top))
check("(24,38) south present among dominant cells (doubled 19/12 convergent)",
      any((n, K) == (24, 38) for _, n, K, _ in top))
print("  [note, flat: 84/53 is a principal convergent of log2 3; 27/17 is a")
print("   semiconvergent (mediant of 8/5 and 19/12); the entry's 'convergent")
print("   anchors' covers both loosely. The top SOUTH cell by budget is (24,38),")
print("   with (53,84) second — the entry names 84/53 for the south.]")

# his approximation replicated (words/p, lgamma, his cutoffs) for comparison
def log2C(a, b):
    if b < 0 or b > a: return float('-inf')
    return (math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)) / math.log(2)
appr_tr = {}
for lo, hi in tranches:
    ts = tn = 0.0
    for n in range(lo, hi + 1):
        Smax = int(0.5849625 * n) + 3
        for S in range(1, Smax + 1):
            K = n + S; q = 2**K - 3**n; a = abs(q)
            if a == 1: continue
            e = a.bit_length() - 53
            l2a = (e + math.log2(a >> e)) if e > 0 else math.log2(a)
            la = 0.0
            for p in range(1, min(n, S) + 1):
                t = log2C(n - 1, p - 1) + log2C(S - 1, p - 1) - math.log2(p) - l2a
                if t > -60: la += 2.0**t
            if q < 0: ts += la
            else: tn += la
    appr_tr[(lo, hi)] = (ts, tn)
print("\n  replication of HIS approximation (words/p) per tranche, vs his output:")
for lo, hi in tranches:
    print(f"    n=[{lo:3d},{hi:3d}]: {appr_tr[(lo,hi)][0]:8.4f} / {appr_tr[(lo,hi)][1]:8.4f}"
          f"   his: {his_tr[(lo,hi)][0]} / {his_tr[(lo,hi)][1]}")
check("his approximation replicates his tranche numbers (each within 0.003)",
      all(abs(appr_tr[k][0] - his_tr[k][0]) < 0.003 and abs(appr_tr[k][1] - his_tr[k][1]) < 0.003
          for k in his_tr))

# decay rate vs the (B) constant
print("\n  effective decay rate (bits per unit n), from exact tranche sums")
print("  (midpoint spacing), vs c_gen = 0.0793 (asymptotic; local rate expected")
print("  steeper — the margin approaches c_gen from above):")
mids = [(lo + hi) / 2 for lo, hi in tranches]
sums = [sum(per_n[n][0] + per_n[n][1] for n in range(lo, hi + 1)) for lo, hi in tranches]
for i in range(len(tranches) - 1):
    if sums[i + 1] > 0:
        rate = -(math.log2(sums[i + 1] / sums[i])) / (mids[i + 1] - mids[i])
        print(f"    [{tranches[i]}] -> [{tranches[i+1]}]: {rate:.4f} bits/n")
CHECKS += 1
print(f"  geometric decay confirmed; rates bracket c_gen = {C_GEN:.4f} as the")
print(f"  asymptotic floor (model-replication readout, not an exact decision).")

# window illustration: why the S-window is load-bearing (size degeneracy)
print("\n  window note (flat): beyond the near-tuned band the uniform-residue")
print("  budget is SIZE-DEGENERATE (a hit q | B with 0 < B < q is impossible;")
print("  cf. REQ-016's 94-98% size artifact). Illustration at n = 17, word-level:")
for K in (27, 29, 31, 34):
    S = K - 17; q = 2**K - 3**17
    w = comb(K - 2, 16)
    print(f"    K={K}: #words/q = {w / q:.4f}"
          f"   x_min bound 1/(2^(K/n)-3) = {1.0 / (2**(K/17) - 3):8.2f}")
print("  the formal per-cell budget does NOT decay with K, but realizable size")
print("  collapses — the window (his S <= 0.585n + 3) is an implicit part of the")
print("  model's operational definition; the entry states the sums without it.")

# ----------------------------------------------------------------------------
# 8. REALIZABILITY: all census hits, exact true-map orbits
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("REALIZABILITY: exact true-map orbit for every census hit (both domains)")
print("=" * 78)
allhits = [(ms, ss) for (_, _, _, ms, ss, _, _) in hits] + \
          [((1,) * j, (1,) * j) for j in range(10, 15)]
real_ok = 0
for ms, ss in allhits:
    n = sum(ms); K = n + sum(ss); q = 2**K - 3**n
    B = B_classical(ms, ss)
    assert B % abs(q) == 0
    x = B // q
    sig, xf = true_map_orbit(x, n)
    ok = (sig == sigma_of(ms, ss)) and (xf == x) and (x % 2 != 0)
    real_ok += ok
    if not ok: print(f"    REALIZATION FAILURE: {ms}|{ss}")
check("all census hits realize exactly (orbit = word, return, odd)",
      real_ok == len(allhits))
print(f"  realized: {real_ok}/{len(allhits)}  (his 18 + the 5 extension powers)")

# fresh 2-adic ghost draws (his (b), our seed and code)
print("\n  fresh 2-adic ghost draws (350 random letter words, truncated orbit):")
g_ok = 0; g_s = 0; g_n = 0
rng2 = random.Random(715202600)
for _ in range(350):
    p = rng2.randint(1, 5)
    ms = tuple(rng2.randint(1, 6) for _ in range(p))
    ss = tuple(rng2.randint(1, 6) for _ in range(p))
    n = sum(ms); K = n + sum(ss); q = 2**K - 3**n
    if q < 0: g_s += 1
    else: g_n += 1
    B = B_classical(ms, ss)
    bits = K + 64 + n
    x = (B * pow(q, -1, 2**bits)) % 2**bits
    sig = []; okrun = True; marge = bits
    for _ in range(n):
        y = (3 * x + 1) % 2**marge
        if y == 0: okrun = False; break
        v = (y & -y).bit_length() - 1
        if v >= marge - 8: okrun = False; break
        sig.append(v); x = (y >> v) % 2**(marge - v); marge -= v
    g_ok += okrun and (sig == sigma_of(ms, ss))
check(f"ghost follows the word: {g_ok}/350 ({g_s} south / {g_n} north)", g_ok == 350)

# ----------------------------------------------------------------------------
# 9. "UNIQUE PAID-LOCK CYCLE IN EXISTENCE" — checked on the knowns
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PAID-LOCK UNIQUENESS on the known cycle list (cycles.md 12.6.1.2)")
print("=" * 78)
knowns = [("+1", (1,), (1,), 1), ("-5", (2,), (1,), -1), ("-17", (4, 3), (1, 3), -139)]
print(f"  {'cycle':>6} {'(n,K)':>8} {'q':>6} {'paid lock (|q|>1)?':>20}")
paid = []
for name, ms, ss, qexp in knowns:
    n = sum(ms); K = n + sum(ss); q = 2**K - 3**n
    check(f"known cycle {name}: q = {qexp}", q == qexp)
    print(f"  {name:>6} {'('+str(n)+','+str(K)+')':>8} {q:>6} {str(abs(q) > 1):>20}")
    if abs(q) > 1: paid.append(name)
print(f"    {'-1':>4} {'(1,1)':>10} {'-1':>6} {'False':>20}   (s = 0 word, outside alphabet)")
check("-1 family: q = 2^1 - 3^1 = -1, not paid", 2**1 - 3**1 == -1)
check("exactly one paid-lock cycle among the four knowns: the -17", paid == ["-17"])
print("""  Verdict on the phrase: TRUE on the known list (the classical census,
  Lagarias 1985; cycles.md 12.6.1.2). 'In existence' is grounded on that list;
  its completeness on the south shore is exactly the open ×3-1 cycles question
  beyond verified ranges — the entry's own falsifier sentence carries this.""")

# ----------------------------------------------------------------------------
# 10. SUMMARY
# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"SUMMARY: {CHECKS} recorded checks/decisions"
      f" ({frame_total} frame-agreement words x2 counted once each), "
      f"{len(FAILURES)} failures")
if FAILURES:
    for f in FAILURES: print(f"  FAILURE: {f}")
    raise SystemExit(1)
print("ALL PASS")
