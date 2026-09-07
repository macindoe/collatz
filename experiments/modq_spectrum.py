"""experiments/modq_spectrum.py -- the mod-q spectrum of the rotation
numerator: the joint law behind the parked condition q | R_0.

Supports: briefs/modq-spectrum-brief.md.

Fresh code. Reimplements from scratch, importing nothing from any
existing script: Miller-Rabin primality, Pollard's rho factorization,
the rotation numerator R_r of cycles.md 12.6.1 (prefix-sum, one pass),
and the profile-family sampler of the brief's Definitions section.
numpy is used for histogram storage and FFT only. sympy is not
installed in this environment (checked) and is not used.

Conventions (cycles.md 12.6.1, Remark 12.6.1.1):
  profile = (ms, ss), p = len(ms) = len(ss), entries m_t, s_t >= 1
  n = sum(ms); K = sum(ss) + n; q = 2^K - 3^n (signed, UNREDUCED)
  sigma_t = s_t + m_{(t+1) mod p}
  R_r = sum_t 3^{M_t} 2^{S_t} (2^{s_t} - 1), M_t = sum_{j>t} m_j,
  S_t = sum_{j<t} sigma_j, indices read cyclically starting at r.
  gcd(q,6) = 1 always (q odd, q == (-1)^K mod 3), so every prime
  factor of q is automatically coprime to 6.

Cell: (n, shore), shore in {'+','-'}. Positive shore K = bit_length(3^n)
(the smallest K with 2^K > 3^n, i.e. ceil(n log2 3), exact integer
arithmetic -- no floating log needed); negative shore K = K_pos - 1.
Family: all (ms,ss) with p in 1..min(n,S), sum(ms)=n, sum(ss)=S=K-n.
Count = C(K-2, n-1) (12.6.1.5).

Run:  python -u experiments/modq_spectrum.py <phase> [args...]
Phases (each fits the ~10-minute per-call harness budget; state persists
between phases via a JSON cache outside the repo):
  cells         -- re-derive the cell table (K, q, factorization,
                   profile counts) and print it against the brief's.
  canaries      -- queue item 1: the four canaries.
  fft <tag>     -- queue item 2 (+item 3's local/free lookup) for one
                   FFT-eligible cell (|q| <= 1e7): full spectrum, top-20,
                   per-period split, selected frequencies via array
                   lookup, joint law.
  large <tag>   -- queue items 3+4 for one of the 7 "large" cells
                   ((17,-) exact-but-too-big-for-FFT, or one of the 6
                   sampled cells): selected frequencies via a bounded
                   sub-sample (documented reduction), joint law, and
                   (for (17,+) only, and (17,-) as its own exact
                   population) the sampler-uniformity / calibration
                   checks.
  assemble      -- read the JSON cache, build the delta tables and the
                   verdict, write experiments/modq_spectrum_output.txt.
  all           -- run every phase in sequence (only for small/testing
                   use; the committed run uses the per-cell phases).
"""

import cmath
import itertools
import json
import math
import os
import random
import sys
import time
from collections import Counter, defaultdict
from math import comb, gcd, log, sqrt

import numpy as np

SEED = 20260908
DATE = "2026-09-08"
CHECKS = {"count": 0, "fail": 0}

CACHE_DIR = os.environ.get(
    "MODQ_CACHE_DIR",
    r"C:\Users\Ace\AppData\Local\Temp\claude\c--Users-Ace-Documents-Collatz"
    r"\5280892e-a4e6-433d-b91a-715dc2967ecb\scratchpad\modq_cache",
)
os.makedirs(CACHE_DIR, exist_ok=True)


def check(cond, label):
    CHECKS["count"] += 1
    if not cond:
        CHECKS["fail"] += 1
        print(f"FAIL: {label}")
    return cond


def log_line(s):
    print(s, flush=True)


# =======================================================================
# Section 0: number theory, fresh (Miller-Rabin + Pollard rho).
# =======================================================================

_SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_probable_prime(n):
    if n < 2:
        return False
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n >= 3_317_044_064_679_887_385_961_981:
        rng = random.Random(n ^ 0xABCDEF)
        witnesses = witnesses + [rng.randrange(2, n - 1) for _ in range(40)]
    for a in witnesses:
        a %= n
        if a < 2:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def _pollard_rho(n):
    if n % 2 == 0:
        return 2
    rng = random.Random(n ^ 0x5A5A5A)
    while True:
        c = rng.randrange(1, n - 1)
        f = lambda x: (x * x + c) % n
        x = y = rng.randrange(2, n - 1)
        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = gcd(abs(x - y), n)
        if d != n:
            return d


_FACTOR_CACHE = {}


def factorize(n):
    """Exact prime factorization of |n| as a sorted {prime: exp} dict."""
    n = abs(n)
    if n in _FACTOR_CACHE:
        return dict(_FACTOR_CACHE[n])
    if n == 1:
        return {}
    orig = n
    factors = {}
    for p in _SMALL_PRIMES:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    stack = [n] if n > 1 else []
    while stack:
        m = stack.pop()
        if m == 1:
            continue
        if is_probable_prime(m):
            factors[m] = factors.get(m, 0) + 1
            continue
        d = _pollard_rho(m)
        stack.append(d)
        stack.append(m // d)
    out = dict(sorted(factors.items()))
    _FACTOR_CACHE[orig] = out
    return dict(out)


def order_mod(a, ell):
    """Multiplicative order of a mod prime power ell (a a unit mod ell)."""
    a %= ell
    phi = ell - (ell // _smallest_prime_factor(ell)) if False else None
    # ell here is always a prime POWER l^e with l an odd prime dividing q;
    # for our uses (subgroup/character indexing) we only ever call this
    # with ell PRIME (the local-frequency character group is cyclic of
    # order ell-1 there); prime-power moduli are handled directly via the
    # residue arithmetic, not via order_mod.
    phi_val = ell - 1
    fac = factorize(phi_val)
    o = phi_val
    for p in fac:
        while o % p == 0 and pow(a, o // p, ell) == 1:
            o //= p
    return o


def _smallest_prime_factor(n):
    for p in _SMALL_PRIMES:
        if n % p == 0:
            return p
    return n


# =======================================================================
# Section 1: profile machinery (fresh; cycles.md 12.6.1 / Remark 12.6.1.1).
# =======================================================================

def K_of(n, shore):
    """K = bit_length(3^n) is the smallest K with 2^K > 3^n -- exact
    integer arithmetic, equal to ceil(n*log2(3)) since 3^n is never a
    power of 2. Negative shore is one less."""
    Kpos = (3 ** n).bit_length()
    return Kpos if shore == "+" else Kpos - 1


def profile_Knq(n, shore):
    K = K_of(n, shore)
    q = (1 << K) - 3 ** n
    return K, q


def R_rot_exact(ms, ss, r):
    """Exact big-integer R_r (12.6.1), one pass, prefix-sum style."""
    p = len(ms)
    mr = ms[r:] + ms[:r]
    sr = ss[r:] + ss[:r]
    pow3suf = [1] * p
    for t in range(p - 2, -1, -1):
        pow3suf[t] = pow3suf[t + 1] * 3 ** mr[t + 1]
    total, Spre = 0, 0
    for t in range(p):
        total += pow3suf[t] * (1 << Spre) * ((1 << sr[t]) - 1)
        Spre += sr[t] + mr[(t + 1) % p]
    return total


def R0_mod(ms, ss, q):
    """R_0 mod |q|, computed with modular exponentiation throughout so
    the intermediate integers stay bounded by |q| (used for the large
    cells; for the small exact cells the exact version is used and
    reduced at the end -- both are cross-checked against each other in
    the canary/self-test section)."""
    p = len(ms)
    Msuf = [0] * (p + 1)
    for t in range(p - 1, -1, -1):
        Msuf[t] = Msuf[t + 1] + ms[t]
    total = 0
    Spre = 0
    for t in range(p):
        Mt = Msuf[t + 1]
        term = pow(3, Mt, q) * ((pow(2, Spre, q) *
                                  ((pow(2, ss[t], q) - 1) % q)) % q)
        total = (total + term) % q
        Spre += ss[t] + ms[(t + 1) % p]
    return total % q


def compositions(total, parts):
    """All compositions of `total` into `parts` positive parts, via
    stars-and-bars cut points (itertools.combinations, C-speed)."""
    if parts == 1:
        yield (total,)
        return
    for cuts in itertools.combinations(range(1, total), parts - 1):
        prev = 0
        res = []
        for c in cuts:
            res.append(c - prev)
            prev = c
        res.append(total - prev)
        yield tuple(res)


def random_composition(total, parts, rng):
    """Uniform random composition of `total` into `parts` positive
    integers: parts-1 distinct cut points drawn uniformly from
    {1,...,total-1} (the standard stars-and-bars bijection)."""
    if parts == 1:
        return (total,)
    cuts = sorted(rng.sample(range(1, total), parts - 1))
    prev, out = 0, []
    for c in cuts:
        out.append(c - prev)
        prev = c
    out.append(total - prev)
    return tuple(out)


def family_pcounts(n, S):
    """{p: (n_ms, n_ss, total)} for p in 1..min(n,S)."""
    out = {}
    for p in range(1, min(n, S) + 1):
        n_ms = comb(n - 1, p - 1)
        n_ss = comb(S - 1, p - 1)
        out[p] = (n_ms, n_ss, n_ms * n_ss)
    return out


def sample_profile(n, S, pcounts, rng):
    """One uniform-at-random profile from the whole family: choose p
    with weight (n_ms*n_ss) EXACTLY (big-int cumulative, no float
    weights), then an independent uniform composition of n and of S
    into p parts."""
    ps = list(pcounts.keys())
    weights = [pcounts[p][2] for p in ps]
    total_w = sum(weights)
    r = rng.randrange(total_w)
    acc = 0
    chosen = ps[-1]
    for p, w in zip(ps, weights):
        acc += w
        if r < acc:
            chosen = p
            break
    ms = random_composition(n, chosen, rng)
    ss = random_composition(S, chosen, rng)
    return chosen, ms, ss


def enumerate_family(n, S):
    """Every profile in the family, p in 1..min(n,S) (exact cells only)."""
    pmax = min(n, S)
    for p in range(1, pmax + 1):
        for ms in compositions(n, p):
            for ss in compositions(S, p):
                yield p, ms, ss


# =======================================================================
# Section 2: the cell table (brief's "Cells to run", re-derived fresh).
# =======================================================================

CELLS = [
    (5, "+"), (5, "-"),
    (7, "+"), (7, "-"),
    (12, "+"), (12, "-"),
    (17, "+"), (17, "-"),
    (22, "+"), (22, "-"),
    (29, "+"), (29, "-"),
    (41, "+"), (41, "-"),
]

BRIEF_TABLE = {
    (5, "+"): (8, 13, {13: 1}, 15),
    (5, "-"): (7, -115, {5: 1, 23: 1}, 5),
    (7, "+"): (12, 1909, {23: 1, 83: 1}, 210),
    (7, "-"): (11, -139, {139: 1}, 84),
    (12, "+"): (20, 517135, {5: 1, 59: 1, 1753: 1}, 31824),
    (12, "-"): (19, -7153, {23: 1, 311: 1}, 12376),
    (17, "+"): (27, 5077565, {5: 1, 71: 1, 14303: 1}, 2042975),
    (17, "-"): (26, -62031299, {11: 1, 23: 1, 245183: 1}, 735471),
    (22, "+"): (35, 2978678759, {7: 1, 425525537: 1}, None),
    (22, "-"): (34, -14201190425, {5: 2, 19: 1, 97: 1, 308219: 1}, None),
    (29, "+"): (46, 1738366812781, {39409: 1, 44110909: 1}, None),
    (29, "-"): (45, -33446005276051,
                {23: 1, 47: 1, 307: 1, 3191: 1, 31583: 1}, None),
    (41, "+"): (65, 420491770248316829,
                {19: 1, 29: 1, 17021: 1, 44835377399: 1}, None),
    (41, "-"): (64, -18026252303461234787,
                {23: 2, 239: 1, 7237: 1, 19701228121: 1}, None),
}

FFT_ELIGIBLE = [(5, "+"), (5, "-"), (7, "+"), (7, "-"), (12, "+"),
                (12, "-"), (17, "+")]
EXACT_CELLS = [(5, "+"), (5, "-"), (7, "+"), (7, "-"), (12, "+"), (12, "-"),
               (17, "+"), (17, "-")]
SAMPLED_CELLS = [(22, "+"), (22, "-"), (29, "+"), (29, "-"),
                 (41, "+"), (41, "-")]
EXACT_THRESHOLD = 2_100_000
SAMPLE_N = 1_000_000
PHI_SUBSAMPLE = 100_000  # queue item 3's documented reduction, see findings


def tag(cell):
    n, shore = cell
    return f"{n}{shore}"


def cache_path(name):
    return os.path.join(CACHE_DIR, name + ".json")


def cache_save(name, obj):
    with open(cache_path(name), "w") as f:
        json.dump(obj, f)


def cache_load(name):
    p = cache_path(name)
    if not os.path.exists(p):
        return None
    with open(p) as f:
        return json.load(f)


def rederive_cell_table():
    log_line("=" * 72)
    log_line("Cell table, re-derived fresh (own K_of/factorize, no sympy)")
    log_line("=" * 72)
    rows = []
    for (n, shore) in CELLS:
        K, q = profile_Knq(n, shore)
        fac = factorize(q)
        S = K - n
        pmax = min(n, S)
        cnt = comb(K - 2, n - 1)
        Kb, qb, facb, cntb = BRIEF_TABLE[(n, shore)]
        ok_K = check(K == Kb, f"cell ({n},{shore}): K={K} matches brief {Kb}")
        ok_q = check(q == qb, f"cell ({n},{shore}): q={q} matches brief {qb}")
        ok_f = check(fac == facb,
                     f"cell ({n},{shore}): factorization {fac} matches "
                     f"brief {facb}")
        ok_c = True
        if cntb is not None:
            ok_c = check(cnt == cntb,
                         f"cell ({n},{shore}): profile count {cnt} "
                         f"matches brief {cntb}")
        rows.append(dict(n=n, shore=shore, K=K, q=q, S=S, pmax=pmax,
                          fac=fac, count=cnt))
        log_line(f"  ({n:>2},{shore}) K={K:<3} S={S:<3} pmax={pmax:<3} "
                  f"q={q:<22} count={cnt:<15} fac={fac} "
                  f"[K:{ok_K} q:{ok_q} fac:{ok_f} count:{ok_c}]")
    return rows


# =======================================================================
# Section 3: canaries (queue item 1).
# =======================================================================

MINUS17_MS, MINUS17_SS = [4, 3], [1, 3]


def canary_minus17():
    log_line("-" * 72)
    log_line("Canary (i): the -17 cell (7,-), block profile "
             "((4,1),(3,3)) = ms=[4,3], ss=[1,3]")
    K, q = profile_Knq(7, "-")
    R0 = R_rot_exact(MINUS17_MS, MINUS17_SS, 0)
    R1 = R_rot_exact(MINUS17_MS, MINUS17_SS, 1)
    check(K == 11 and q == -139, "(7,-): K=11, q=-139")
    check(R0 == 139, "R_0 = 139")
    check(R1 == 695, "R_1 = 695")
    check(R1 == 5 * 139, "R_1 = 5 * 139")
    check(R0 % 139 == 0 and R1 % 139 == 0, "both R_0, R_1 == 0 (mod 139)")
    log_line(f"  K={K}, q={q}, R_0={R0}, R_1={R1} = 5*139; both == 0 mod "
             f"139: {R0 % 139 == 0 and R1 % 139 == 0}")


# Predicted zero-bin (hit) counts at (5,+-),(7,+-),(12,+-), derived from
# briefs/merle-la6-check-findings.md 2(a)'s complete word census (indexed
# there by (n,K), matching this brief's cell indexing exactly: trivial^j
# hits at (j,2j) j=2..9; (-5)-power hits at (2j,3j) j=2..7; the -17 orbit
# (2 words) at (7,11); its square at (14,22); nothing else at n<=14. None
# of those (n,K) pairs equal (5,8),(5,7),(7,12),(12,20),(12,19) -- only
# (7,11) is a listed hit cell, with exactly 2 hits (the -17 orbit).
LA6_PREDICTED = {(5, "+"): 0, (5, "-"): 0, (7, "+"): 0, (7, "-"): 2,
                 (12, "+"): 0, (12, "-"): 0}


def canary_la6_census():
    log_line("-" * 72)
    log_line("Canary (ii): zero bin at (5,+-),(7,+-),(12,+-) vs the L-A6 "
             "census (briefs/merle-la6-check-findings.md sec 2(a))")
    log_line("  Reconciliation: that census indexes words by (n,K) "
             "exactly as this brief's cell table does. Its complete hit "
             "list at n<=14 is: trivial^j at (n,K)=(j,2j) for j=2..9; "
             "(-5)-powers at (2j,3j) for j=2..7; the -17 orbit (2 words) "
             "at (7,11); its square at (14,22). None of (5,8),(5,7),"
             "(7,12),(12,20),(12,19) appears in that list except (7,11) "
             "with exactly 2 hits -- so the predicted zero-bin counts "
             "are 0,0,0,2,0,0 for (5,+),(5,-),(7,+),(7,-),(12,+),(12,-).")
    results = {}
    for (n, shore) in [(5, "+"), (5, "-"), (7, "+"), (7, "-"),
                        (12, "+"), (12, "-")]:
        K, q = profile_Knq(n, shore)
        S = K - n
        zero = 0
        total = 0
        for p, ms, ss in enumerate_family(n, S):
            total += 1
            if R0_mod(list(ms), list(ss), q) == 0:
                zero += 1
        results[(n, shore)] = zero
        pred = LA6_PREDICTED[(n, shore)]
        ok = check(zero == pred,
                   f"({n},{shore}): zero-bin {zero} == L-A6 predicted "
                   f"{pred} (of {total} profiles)")
        log_line(f"  ({n},{shore}): zero-bin={zero} predicted={pred} "
                 f"total={total} match={ok}")
    return results


def canary_uniform_null():
    log_line("-" * 72)
    log_line("Canary (iii): uniform null -- the same pipeline (zero-bin "
             "rate, class maxima) on N i.i.d. uniform random residues "
             "mod |q|, at a representative cell, both signs")
    rng = random.Random(SEED + 999)
    for (n, shore) in [(12, "+"), (12, "-")]:
        K, q = profile_Knq(n, shore)
        aq = abs(q)
        N = 20000
        vals = [rng.randrange(aq) for _ in range(N)]
        zero = sum(1 for v in vals if v == 0)
        expected = N / aq
        log_line(f"  ({n},{shore}) |q|={aq}: N={N} uniform draws, "
                 f"zero-bin={zero} (expected {expected:.4f}, i.e. "
                 f"{'0 is the typical outcome' if expected < 1 else ''})")
        # class-maximum floor check: low class xi=1..2000 (or |q|-1 if
        # smaller), Rayleigh floor sqrt(ln(#xi)/N)
        xis = list(range(1, min(2000, aq - 1) + 1))
        maxphi = 0.0
        for xi in xis:
            s = sum(cmath.exp(2j * cmath.pi * xi * v / aq) for v in vals)
            maxphi = max(maxphi, abs(s) / N)
        floor = sqrt(log(len(xis)) / N) if len(xis) > 1 else float("nan")
        ratio = maxphi / floor if floor > 0 else float("nan")
        log_line(f"    low-class (xi=1..{len(xis)}) max|phi|={maxphi:.4f} "
                 f"floor={floor:.4f} ratio={ratio:.2f} "
                 f"(uniform null should sit near 1x, well under 3x)")
        check(ratio < 3.0, f"({n},{shore}) uniform null low-class max "
              f"under 3x floor")


def canary_sampler_calibration():
    log_line("-" * 72)
    log_line("Canary (iv): sampler calibration at (17,+) -- 10^6 samples "
             "vs the exact histogram, at a common set of frequencies, "
             "discrepancy vs 1/sqrt(N)")
    n, shore = 17, "+"
    K, q = profile_Knq(n, shore)
    S = K - n
    pcounts = family_pcounts(n, S)
    total_pop = sum(v[2] for v in pcounts.values())
    check(total_pop == BRIEF_TABLE[(17, "+")][3],
          "(17,+) family total matches the brief's count")

    # exact histogram (full population), needed as ground truth
    hist = np.zeros(q, dtype=np.int64)
    t0 = time.time()
    for p, ms, ss in enumerate_family(n, S):
        hist[R0_mod(list(ms), list(ss), q)] += 1
    dt_exact = time.time() - t0
    log_line(f"  Exact enumeration: {total_pop} profiles, {dt_exact:.1f}s")

    rng = random.Random(SEED)
    Nsamp = 1_000_000
    samp_hist = np.zeros(q, dtype=np.int64)
    t0 = time.time()
    for _ in range(Nsamp):
        p, ms, ss = sample_profile(n, S, pcounts, rng)
        samp_hist[R0_mod(list(ms), list(ss), q)] += 1
    dt_samp = time.time() - t0
    log_line(f"  Sampler: {Nsamp} draws, {dt_samp:.1f}s, seed {SEED}")

    freqs = [1, 2, 3, 5, 7, 11, 100, 1000]
    freqs = [f for f in freqs if f < q]
    print(f"  {'xi':>6} {'exact|phi|':>12} {'sample|phi|':>12} "
          f"{'|diff|':>10} {'1/sqrt(N)':>10}")
    max_ratio = 0.0
    for xi in freqs:
        ph_exact = abs(np.sum(hist * np.exp(2j * np.pi * xi *
                       np.arange(q) / q))) / total_pop
        ph_samp = abs(np.sum(samp_hist * np.exp(2j * np.pi * xi *
                      np.arange(q) / q))) / Nsamp
        diff = abs(ph_exact - ph_samp)
        floor = 1 / sqrt(Nsamp)
        ratio = diff / floor
        max_ratio = max(max_ratio, ratio)
        print(f"  {xi:>6} {ph_exact:>12.5f} {ph_samp:>12.5f} "
              f"{diff:>10.5f} {floor:>10.5f}  ratio={ratio:.2f}")
    check(max_ratio < 6.0, "(17,+) sampler-vs-exact discrepancy stays "
          "within a small multiple of 1/sqrt(N) at every tested xi")
    # also compare zero-bin rate
    zero_exact = hist[0] / total_pop
    zero_samp = samp_hist[0] / Nsamp
    log_line(f"  zero-bin: exact={zero_exact:.6f} ({hist[0]}/{total_pop}) "
             f"sample={zero_samp:.6f} ({samp_hist[0]}/{Nsamp}) "
             f"diff={abs(zero_exact-zero_samp):.6f} vs "
             f"1/sqrt(N)={1/sqrt(Nsamp):.6f}")
    cache_save("cell_17+_exact_hist_meta",
               dict(total_pop=total_pop, dt_exact=dt_exact,
                    zero=int(hist[0])))
    np.save(os.path.join(CACHE_DIR, "hist_17+.npy"), hist)
    return dict(max_ratio=max_ratio, dt_exact=dt_exact, dt_samp=dt_samp)


def run_canaries():
    t0 = time.time()
    log_line("=" * 72)
    log_line("QUEUE ITEM 1: instrument + canaries")
    log_line("=" * 72)
    canary_minus17()
    la6 = canary_la6_census()
    canary_uniform_null()
    samp = canary_sampler_calibration()
    dt = time.time() - t0
    log_line(f"Canaries section runtime: {dt:.1f}s")
    cache_save("canaries", dict(la6=[[list(k), v] for k, v in la6.items()],
                                 sampler_max_ratio=samp["max_ratio"],
                                 dt=dt))
    return dt


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    t_start = time.time()
    if phase == "cells":
        rederive_cell_table()
    elif phase == "canaries":
        rederive_cell_table()
        run_canaries()
    else:
        print(f"Phase '{phase}' not yet wired in this cut of the script; "
              f"see modq_spectrum_part2.py additions.", file=sys.stderr)
        sys.exit(1)
    print(f"[phase {phase}] wall time {time.time()-t_start:.1f}s, "
          f"checks {CHECKS['count']} fail {CHECKS['fail']}")
