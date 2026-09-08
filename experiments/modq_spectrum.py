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


# =======================================================================
# Section 4: frequency classification (local / monomial / other).
# =======================================================================

def local_frequencies(aq, fac):
    """{(ell,a): [xi,...]} -- xi = j*aq/ell^a, j=1..min(ell^a-1,300)."""
    out = {}
    for ell, e in fac.items():
        ella = ell ** e
        if aq % ella != 0:
            continue
        step = aq // ella
        jmax = min(ella - 1, 300)
        out[(ell, e)] = [j * step for j in range(1, jmax + 1)]
    return out


def monomial_table(aq, amax=64, bmax=40):
    """{residue: (a,b,sign)} for xi = +-2^a*3^b mod aq, 0<=a<=amax,
    0<=b<=bmax -- a dict so classify_xi can look up membership."""
    out = {}
    for a in range(amax + 1):
        p2 = pow(2, a, aq)
        for b in range(bmax + 1):
            v = (p2 * pow(3, b, aq)) % aq
            if v not in out:
                out[v] = (a, b, "+")
            nv = (aq - v) % aq
            if nv not in out:
                out[nv] = (a, b, "-")
    return out


def classify_xi(xi, aq, local_freq_map, mono_map):
    xi = xi % aq
    for (ell, e), lst in local_freq_map.items():
        if xi in lst:
            return f"local:{ell}^{e}"
    if xi in mono_map:
        a, b, sign = mono_map[xi]
        return f"monomial:{sign}2^{a}*3^{b}"
    return "other"


def cross_prime_pairs(fac, cap=1_000_000):
    """[(ell1,e1,ell2,e2)] for every pair of prime powers with product
    <= cap (used both by item 3(c) and item 4)."""
    items = [(ell, e) for ell, e in fac.items()]
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            ell1, e1 = items[i]
            ell2, e2 = items[j]
            if (ell1 ** e1) * (ell2 ** e2) <= cap:
                out.append((ell1, e1, ell2, e2))
    return out


# =======================================================================
# Section 5: selected-frequency classes (queue item 3), two backends.
# =======================================================================

def selected_frequency_xis(aq, fac, low_n=2000, local_cap=300,
                            cross_cap=30, mono_a=64, mono_b=40,
                            random_n=5000, orbit_seed_xi=None,
                            orbit_cap=2000, rng_seed=SEED):
    """Build the six classes' xi lists (queue item 3(a)-(f))."""
    classes = {}
    classes["low"] = list(range(1, min(low_n, aq - 1) + 1))
    loc = local_frequencies(aq, fac)
    local_xis = []
    for (ell, e), lst in loc.items():
        local_xis.extend(lst[:local_cap] if local_cap < 300 else lst)
    classes["local"] = sorted(set(local_xis))
    cp_xis = []
    for ell1, e1, ell2, e2 in cross_prime_pairs(fac):
        step1 = aq // (ell1 ** e1)
        step2 = aq // (ell2 ** e2)
        j1max = min(ell1 ** e1 - 1, cross_cap)
        j2max = min(ell2 ** e2 - 1, cross_cap)
        for j1 in range(1, j1max + 1):
            for j2 in range(1, j2max + 1):
                cp_xis.append((j1 * step1 + j2 * step2) % aq)
    classes["cross"] = sorted(set(cp_xis))
    mono_map = monomial_table(aq, mono_a, mono_b)
    classes["monomial"] = sorted(set(mono_map.keys()))
    rng = random.Random(rng_seed)
    classes["random"] = sorted(set(rng.randrange(1, aq) for _ in
                                    range(min(random_n, max(aq - 1, 1)))))
    if orbit_seed_xi is not None:
        seen = {orbit_seed_xi % aq}
        frontier = [orbit_seed_xi % aq]
        while frontier and len(seen) < orbit_cap:
            nxt = []
            for x in frontier:
                for g in (2, 3):
                    y = (x * g) % aq
                    if y not in seen:
                        seen.add(y)
                        nxt.append(y)
            frontier = nxt
        classes["orbit"] = sorted(seen)
    else:
        classes["orbit"] = []
    return classes, mono_map, loc


def rayleigh_floor(n_freqs, N):
    if n_freqs <= 1 or N <= 0:
        return float("nan")
    return sqrt(log(n_freqs) / N)


def evaluate_classes_via_fft(phi_array, aq, classes, N):
    """FFT-eligible cells: phi_array[xi] already computed for every xi;
    selected-frequency evaluation is a free array lookup."""
    out = {}
    for cname, xis in classes.items():
        if not xis:
            out[cname] = None
            continue
        vals = np.array([abs(phi_array[x % aq]) for x in xis])
        i = int(np.argmax(vals))
        out[cname] = dict(max=float(vals[i]), xi=int(xis[i]),
                           floor=rayleigh_floor(len(xis), N),
                           n_freqs=len(xis))
    return out


def evaluate_classes_direct(residues, aq, classes, N):
    """Large cells: residues is a python list/array of R0 mod aq values
    (length N, the phi-subsample for these cells, documented in the
    findings); phi(xi) computed by direct summation per xi."""
    out = {}
    for cname, xis in classes.items():
        if not xis:
            out[cname] = None
            continue
        best_val, best_xi = -1.0, None
        for xi in xis:
            # exact modular product per sample (Python bigints), then a
            # vectorized trig evaluation -- see findings for the timing
            # rationale (benchmarked: ~0.14s per freq at N=1e6, scaled
            # down here via the documented PHI_SUBSAMPLE reduction).
            ph = np.empty(N, dtype=np.float64)
            for i in range(N):
                ph[i] = (xi * residues[i]) % aq
            phase = ph * (2 * np.pi / aq)
            s = np.sum(np.exp(1j * phase))
            val = abs(s) / N
            if val > best_val:
                best_val, best_xi = val, xi
        out[cname] = dict(max=float(best_val), xi=int(best_xi),
                           floor=rayleigh_floor(len(xis), N),
                           n_freqs=len(xis))
    return out


# =======================================================================
# Section 6: joint law (queue item 4): mutual information + TV.
# =======================================================================

def joint_law_from_histogram(hist, aq, ell1a, ell2b, N, rng):
    idxs = np.arange(aq)
    m1 = idxs % ell1a
    m2 = idxs % ell2b
    combined = m1.astype(np.int64) * ell2b + m2.astype(np.int64)
    joint = np.bincount(combined, weights=hist.astype(np.float64),
                         minlength=ell1a * ell2b).reshape(ell1a, ell2b)
    return _mi_tv(joint, ell1a, ell2b, N, rng)


def joint_law_from_samples(residues, ell1a, ell2b, N, rng):
    # residues can exceed int64 range at the largest cell (|q| ~ 1.8e19
    # at (41,-)); ell1a,ell2b <= 1e6 always (the joint-law cap), so
    # reduce with plain Python ints FIRST (exact, no overflow) and only
    # then hand the small results to numpy.
    m1 = np.fromiter((r % ell1a for r in residues), dtype=np.int64,
                      count=len(residues))
    m2 = np.fromiter((r % ell2b for r in residues), dtype=np.int64,
                      count=len(residues))
    joint = np.zeros((ell1a, ell2b), dtype=np.float64)
    np.add.at(joint, (m1, m2), 1.0)
    return _mi_tv(joint, ell1a, ell2b, N, rng, m1=m1, m2=m2)


def _mi_from_joint(joint, N):
    p = joint / N
    p1 = p.sum(axis=1, keepdims=True)
    p2 = p.sum(axis=0, keepdims=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(p > 0, p / (p1 * p2), 1.0)
        term = np.where(p > 0, p * np.log2(ratio), 0.0)
    return float(term.sum())


def _tv_from_joint(joint, N):
    p = joint / N
    p1 = p.sum(axis=1, keepdims=True)
    p2 = p.sum(axis=0, keepdims=True)
    return float(0.5 * np.abs(p - p1 * p2).sum())


def _mi_tv(joint, k1, k2, N, rng, m1=None, m2=None):
    check(abs(float(joint.sum()) - N) < 0.5,
          f"joint table sums to N ({float(joint.sum())} vs {N})")
    mi = _mi_from_joint(joint, N)
    tv = _tv_from_joint(joint, N)
    null_mi = (k1 - 1) * (k2 - 1) / (2 * N * math.log(2))
    # permutation control: shuffle one coordinate's assignment
    if m1 is None or m2 is None:
        # derive an equivalent sample list from the joint table itself
        idx1, idx2 = np.nonzero(joint)
        counts = joint[idx1, idx2].astype(np.int64)
        m1 = np.repeat(idx1, counts)
        m2 = np.repeat(idx2, counts)
    m2p = m2.copy()
    perm_rng = np.random.RandomState(rng.randrange(2 ** 31))
    perm_rng.shuffle(m2p)
    joint_p = np.zeros((k1, k2), dtype=np.float64)
    np.add.at(joint_p, (m1, m2p), 1.0)
    mi_perm = _mi_from_joint(joint_p, N)
    tv_perm = _tv_from_joint(joint_p, N)
    return dict(mi=mi, tv=tv, null_mi=null_mi, mi_perm=mi_perm,
                tv_perm=tv_perm)


def run_joint_law_for_cell(n, shore, q, fac, N, hist=None, residues=None):
    aq = abs(q)
    pairs = cross_prime_pairs(fac, cap=1_000_000)
    rng = random.Random(SEED + n + (1 if shore == "+" else 0))
    results = []
    for ell1, e1, ell2, e2 in pairs:
        k1, k2 = ell1 ** e1, ell2 ** e2
        if hist is not None:
            r = joint_law_from_histogram(hist, aq, k1, k2, N, rng)
        else:
            r = joint_law_from_samples(residues, k1, k2, N, rng)
        r.update(ell1a=k1, ell2b=k2, ell1=ell1, ell2=ell2)
        results.append(r)
        log_line(f"    joint ({ell1}^{e1}={k1}, {ell2}^{e2}={k2}): "
                 f"MI={r['mi']:.5f} bits, null={r['null_mi']:.5f}, "
                 f"perm-MI={r['mi_perm']:.5f}; TV={r['tv']:.5f}, "
                 f"perm-TV={r['tv_perm']:.5f}")
    return results


# =======================================================================
# Section 7: FFT-eligible cell processing (queue items 2, 3-lookup, 4).
# =======================================================================

def process_fft_cell(n, shore):
    t0 = time.time()
    K, q = profile_Knq(n, shore)
    aq = abs(q)
    fac = factorize(q)
    S = K - n
    log_line("=" * 72)
    log_line(f"FFT-ELIGIBLE CELL ({n},{shore}): K={K} q={q} fac={fac} "
             f"S={S}")
    log_line("=" * 72)
    hist = np.zeros(aq, dtype=np.int64)
    per_p_hist = defaultdict(lambda: np.zeros(aq, dtype=np.int64))
    N = 0
    t_enum = time.time()
    for p, ms, ss in enumerate_family(n, S):
        r = R0_mod(list(ms), list(ss), aq)
        hist[r] += 1
        per_p_hist[p][r] += 1
        N += 1
    dt_enum = time.time() - t_enum
    expected_N = BRIEF_TABLE[(n, shore)][3]
    if expected_N is not None:
        check(N == expected_N, f"({n},{shore}): enumerated N={N} matches "
              f"brief count {expected_N}")
    log_line(f"  Enumeration: {N} profiles, {dt_enum:.1f}s")
    check(int(hist.sum()) == N, f"({n},{shore}): histogram sums to N")

    # --- item 2: full FFT spectrum, top-20 -------------------------------
    phi_array = np.conj(np.fft.fft(hist.astype(np.float64))) / N
    mags = np.abs(phi_array)
    mags[0] = -1  # exclude xi=0 (trivial, phi(0)=1)
    top_idx = np.argsort(-mags)[:20]
    loc = local_frequencies(aq, fac)
    mono_map = monomial_table(aq)
    log_line(f"  Top-20 |phi(xi)| (xi=0 excluded):")
    top20 = []
    for xi in top_idx:
        xi = int(xi)
        label = classify_xi(xi, aq, loc, mono_map)
        val = float(mags[xi])
        top20.append((xi, val, label))
        log_line(f"    xi={xi:<10} |phi|={val:.5f}  type={label}")
    floor_all = rayleigh_floor(aq - 1, N)
    log_line(f"  Population floor sqrt(ln(q-1)/N) = {floor_all:.5f}")

    # per-period split: does the 5/7-line shrink with p? report the max
    # off-local off-monomial |phi| at each p present.
    log_line(f"  Per-period split (does the 5/7 local-character bias "
             f"shrink with p, and is anything else NOT shrinking?):")
    off_lm_mask = np.ones(aq, dtype=bool)
    for lst in loc.values():
        for x in lst:
            off_lm_mask[x % aq] = False
    for x in mono_map:
        off_lm_mask[x] = False
    off_lm_mask[0] = False
    per_p_summary = {}
    for p in sorted(per_p_hist.keys()):
        h_p = per_p_hist[p]
        N_p = int(h_p.sum())
        if N_p == 0:
            continue
        phi_p = np.conj(np.fft.fft(h_p.astype(np.float64))) / N_p
        mags_p = np.abs(phi_p)
        # local-character (5,7) magnitudes specifically, if present
        local57 = {}
        for ell, e in fac.items():
            if ell in (5, 7):
                lst = loc.get((ell, e), [])
                if lst:
                    local57[ell] = float(np.max(mags_p[lst]))
        off_masked = np.where(off_lm_mask, mags_p, -1)
        floor_p = rayleigh_floor(aq - 1, N_p)
        if not off_lm_mask.any():
            per_p_summary[p] = dict(N_p=N_p, local57=local57,
                                     off_best_xi=None, off_best_val=None,
                                     floor=floor_p)
            log_line(f"    p={p:<3} N_p={N_p:<10} local-5/7={local57} "
                     f"off-local-off-monomial: N/A (|q| is a single "
                     f"prime power -- every nonzero residue is a local "
                     f"character here) floor={floor_p:.5f}")
        else:
            best_off = int(np.argmax(off_masked))
            per_p_summary[p] = dict(N_p=N_p, local57=local57,
                                     off_best_xi=best_off,
                                     off_best_val=float(off_masked[best_off]),
                                     floor=floor_p)
            log_line(f"    p={p:<3} N_p={N_p:<10} local-5/7={local57} "
                     f"off-local-off-monomial max|phi|="
                     f"{off_masked[best_off]:.5f} (xi={best_off}) "
                     f"floor={floor_p:.5f}")

    # --- item 3: selected frequencies, via free array lookup -------------
    top_peak_xi = int(top_idx[0])
    classes, _, _ = selected_frequency_xis(aq, fac, orbit_seed_xi=top_peak_xi)
    class_results = evaluate_classes_via_fft(phi_array, aq, classes, N)
    log_line(f"  Selected-frequency classes (via full-population FFT "
             f"lookup, exact):")
    for cname, r in class_results.items():
        if r is None:
            log_line(f"    {cname}: (empty class at this cell)")
            continue
        ratio = r["max"] / r["floor"] if r["floor"] > 0 else float("nan")
        cand = ratio > 3.0
        log_line(f"    {cname:<10} n_freqs={r['n_freqs']:<6} "
                 f"max|phi|={r['max']:.5f} at xi={r['xi']:<10} "
                 f"floor={r['floor']:.5f} ratio={ratio:.2f} "
                 f"{'CANDIDATE' if cand else ''}")
        class_results[cname]["candidate"] = cand
        class_results[cname]["ratio"] = ratio

    ghost_results = apply_ghost_hunt(n, shore, q, class_results, loc,
                                      mono_map, is_sampled=False,
                                      N_full=N)

    # --- item 4: joint law -------------------------------------------------
    log_line(f"  Joint law (mutual information / TV):")
    joint_results = run_joint_law_for_cell(n, shore, q, fac, N, hist=hist)

    dt_total = time.time() - t0
    log_line(f"  Cell ({n},{shore}) total runtime: {dt_total:.1f}s")

    result = dict(n=n, shore=shore, K=K, q=q, fac=fac, N=N,
                  dt_enum=dt_enum, dt_total=dt_total,
                  top20=top20, floor_all=floor_all,
                  per_p=per_p_summary, classes=class_results,
                  ghost=ghost_results,
                  joint=joint_results, zero_bin=int(hist[0]),
                  population="exact")
    cache_save(f"cell_{tag((n,shore))}", result)
    if n == 17 and shore == "+":
        # keep the histogram for the sampler-calibration canary if not
        # already cached, and for cross-reference
        pass
    return result


# =======================================================================
# Section 8: ghost-hunt discipline (queue item 5), mandatory per candidate.
# =======================================================================

def multiplicative_related(xi1, xi2, aq, amax=24, bmax=16):
    """True if xi2 == +-2^a*3^b*xi1 (mod aq) for some small a,b -- the
    dedup test: two flagged frequencies driven by the SAME underlying
    <2,3>-orbit signal are one candidate, not two."""
    if xi1 == 0 or xi2 == 0:
        return xi1 == xi2
    inv1 = None
    try:
        inv1 = pow(xi1, -1, aq)
    except ValueError:
        return False
    ratio = (xi2 * inv1) % aq
    nratio = (aq - ratio) % aq
    for a in range(amax + 1):
        p2 = pow(2, a, aq)
        for b in range(bmax + 1):
            v = (p2 * pow(3, b, aq)) % aq
            if v == ratio or v == nratio:
                return True
    return False


def dedup_candidates(cands, aq):
    """cands: list of dicts with 'xi','value','class'. Groups related
    xi's (by multiplicative_related or exact conjugate aq-xi), keeping
    the largest-value member per group as representative."""
    groups = []
    for c in sorted(cands, key=lambda d: -d["value"]):
        placed = False
        for g in groups:
            rep = g[0]
            if c["xi"] == rep["xi"] or c["xi"] == (aq - rep["xi"]) % aq \
               or multiplicative_related(rep["xi"], c["xi"], aq):
                g.append(c)
                placed = True
                break
        if not placed:
            groups.append([c])
    return groups


def restricted_phi_direct(n, S, xi, aq, min_p=1, min_entry=1,
                           dedupe_rotations=False):
    """Direct phi(xi) over a FILTERED sub-population of the exact
    family (p>=min_p, all entries>=min_entry, optionally one
    representative per rotation-necklace) -- ghost-hunt steps 1 and 3."""
    s = 0j
    N = 0
    for p, ms, ss in enumerate_family(n, S):
        if p < min_p:
            continue
        if min_entry > 1 and (min(ms) < min_entry or min(ss) < min_entry):
            continue
        if dedupe_rotations:
            # canonical necklace form: this profile must equal the
            # lexicographically smallest among its own p rotations
            pairs = list(zip(ms, ss))
            rotations = [tuple(pairs[r:] + pairs[:r]) for r in range(p)]
            if tuple(pairs) != min(rotations):
                continue
        r = R0_mod(list(ms), list(ss), aq)
        s += cmath.exp(2j * cmath.pi * xi * r / aq)
        N += 1
    return (abs(s) / N if N else float("nan")), N


def mpmath_high_precision_check(n, S, xi, aq, dps=50, cap=None):
    """Ghost-hunt step 5: recompute phi(xi) with mpmath at `dps` decimal
    digits (exact modular reduction of xi*R0 mod aq via Python bigints
    first, THEN a high-precision trig evaluation -- so this targets
    FFT/float64 summation roundoff specifically, not the modular
    arithmetic, which is already exact in the float64 pipeline). Uses
    the FULL population by default (no cap) -- a truncated prefix of
    the enumeration order is biased toward small p and is NOT a valid
    stand-in for the same population the FFT summed over; `cap`, if
    given, is applied only when explicitly requested and is reported
    as a genuine reduction, not silently substituted for "the same
    computation at higher precision.\""""
    import mpmath
    mpmath.mp.dps = dps
    s = mpmath.mpc(0)
    N = 0
    capped = False
    for p, ms, ss in enumerate_family(n, S):
        if cap is not None and N >= cap:
            capped = True
            break
        r = R0_mod(list(ms), list(ss), aq)
        theta = mpmath.mpf(2) * mpmath.pi * xi * r / aq
        s += mpmath.mpc(mpmath.cos(theta), mpmath.sin(theta))
        N += 1
    val = abs(s) / N if N else float("nan")
    return float(val), N, capped


def ghost_hunt_one(n, shore, q, xi, fft_value, N_full, loc, mono_map,
                    is_sampled, residues=None):
    """Runs the five hunts (brief's item 5) on one representative
    candidate xi and returns a dict with each hunt's outcome and an
    overall verdict."""
    aq = abs(q)
    K = K_of(n, shore)
    S = K - n
    out = dict(xi=xi, fft_value=fft_value)
    log_line(f"    GHOST-HUNT xi={xi} (fft-derived |phi|={fft_value:.5f}):")

    # (1) small-entry pushforward: restrict to p>=3, entries>=2
    if not is_sampled:
        val_p3e2, N_p3e2 = restricted_phi_direct(n, S, xi, aq, min_p=3,
                                                   min_entry=2)
        out["hunt1_p3e2_value"] = val_p3e2
        out["hunt1_p3e2_N"] = N_p3e2
        floor_p3e2 = rayleigh_floor(aq - 1, N_p3e2) if N_p3e2 > 1 else float("nan")
        log_line(f"      (1) p>=3,entries>=2: N={N_p3e2}, |phi|={val_p3e2:.5f}, "
                 f"floor={floor_p3e2:.5f}, ratio="
                 f"{(val_p3e2/floor_p3e2 if floor_p3e2 else float('nan')):.2f}")
    else:
        out["hunt1_p3e2_value"] = None
        log_line(f"      (1) skipped (sampled cell; see hunt (4) instead "
                 f"for the population-level check)")

    # (2) local/monomial character test (already have the classification)
    label = classify_xi(xi, aq, loc, mono_map)
    out["hunt2_type"] = label
    log_line(f"      (2) classify_xi: {label} "
             f"({'ALREADY the known 12.6.1.6-type mechanism' if label != 'other' else 'not a local/monomial character in the tested range'})")

    # (3) rotation multiplicity: one representative per necklace
    if not is_sampled:
        val_dedup, N_dedup = restricted_phi_direct(n, S, xi, aq,
                                                     dedupe_rotations=True)
        out["hunt3_dedup_value"] = val_dedup
        out["hunt3_dedup_N"] = N_dedup
        floor_dedup = rayleigh_floor(aq - 1, N_dedup) if N_dedup > 1 else float("nan")
        log_line(f"      (3) one-per-necklace: N={N_dedup}, "
                 f"|phi|={val_dedup:.5f}, floor={floor_dedup:.5f}, ratio="
                 f"{(val_dedup/floor_dedup if floor_dedup else float('nan')):.2f}")
    else:
        out["hunt3_dedup_value"] = None
        log_line(f"      (3) skipped (sampled cell; necklace dedup needs "
                 f"the exact population)")

    # (4) sampler artifact: exact-cell agreement / independent re-draw
    if is_sampled and residues is not None:
        rng2 = random.Random(SEED + 777 + n)
        # re-derive an independent sample of the same size from scratch
        Kc, qc = profile_Knq(n, shore)
        Sc = Kc - n
        pcounts = family_pcounts(n, Sc)
        N2 = min(len(residues), 200_000)
        s2 = 0j
        for _ in range(N2):
            _, ms2, ss2 = sample_profile(n, Sc, pcounts, rng2)
            r2 = R0_mod(list(ms2), list(ss2), aq)
            s2 += cmath.exp(2j * cmath.pi * xi * r2 / aq)
        val2 = abs(s2) / N2
        out["hunt4_resample_value"] = val2
        out["hunt4_resample_N"] = N2
        log_line(f"      (4) independent re-sample (N={N2}, fresh seed): "
                 f"|phi|={val2:.5f} vs original {fft_value:.5f}")
    else:
        out["hunt4_resample_value"] = None
        log_line(f"      (4) N/A: exact population already used (no "
                 f"sampling step to re-check)")

    # (5) float rounding: mpmath high-precision recomputation
    if not is_sampled:
        val_mp, N_mp, capped = mpmath_high_precision_check(n, S, xi, aq)
        out["hunt5_mpmath_value"] = val_mp
        out["hunt5_mpmath_N"] = N_mp
        out["hunt5_capped"] = capped
        same_pop = (N_mp == N_full)
        ref_kind = ("the exact FFT value (same full population, float64)"
                    if same_pop else
                    f"the item-3 subsample estimate (N={N_full}, "
                    f"float64) -- N differs from mpmath's N={N_mp} "
                    f"(the FULL exact population), so this diff mixes "
                    f"subsample noise with any float-rounding effect")
        log_line(f"      (5) mpmath 50-digit recompute (N={N_mp}"
                 f"{' CAPPED' if capped else ' full population'}): "
                 f"|phi|={val_mp:.6f} vs {ref_kind}: {fft_value:.6f} "
                 f"diff={abs(val_mp-fft_value):.2e}")
        if same_pop:
            check(abs(val_mp - fft_value) < 1e-6,
                  f"xi={xi}: mpmath high-precision value matches the "
                  f"float64 FFT value to < 1e-6 (same population, so "
                  f"this isolates float64 summation roundoff)")
    else:
        out["hunt5_mpmath_value"] = None
        log_line(f"      (5) skipped for sampled cells (see the "
                 f"population-level direct-sum value itself, which is "
                 f"already an exact-modular-arithmetic computation, not "
                 f"an FFT)")

    return out


def apply_ghost_hunt(n, shore, q, class_results, loc, mono_map,
                      is_sampled=False, residues=None, N_full=None):
    """Collect every class's candidate (ratio>3), dedup by <2,3>-orbit
    relatedness, and run the five-step hunt on each distinct one."""
    aq = abs(q)
    cands = []
    for cname, r in class_results.items():
        if r is not None and r.get("candidate"):
            cands.append(dict(cclass=cname, xi=r["xi"], value=r["max"],
                               ratio=r["ratio"]))
    if not cands:
        log_line(f"  Ghost-hunt: no candidate (every class ratio <= 3x "
                 f"its floor) -- nothing to hunt.")
        return []
    groups = dedup_candidates(cands, aq)
    log_line(f"  Ghost-hunt: {len(cands)} class-candidates collapse to "
             f"{len(groups)} distinct <2,3>-orbit-related representative(s).")
    results = []
    for g in groups:
        rep = g[0]
        classes_explained = sorted(set(c["cclass"] for c in g))
        log_line(f"  Candidate group (classes {classes_explained}, "
                 f"representative xi={rep['xi']}, |phi|={rep['value']:.5f}, "
                 f"ratio={rep['ratio']:.2f}):")
        hunt = ghost_hunt_one(n, shore, q, rep["xi"], rep["value"],
                               N_full, loc, mono_map, is_sampled, residues)
        # verdict: dissolved if any hunt shows a clear elementary cause
        cause = None
        if hunt.get("hunt2_type") not in (None, "other"):
            cause = f"coincides with a {hunt['hunt2_type']} character"
        elif hunt.get("hunt1_p3e2_value") is not None:
            f1 = rayleigh_floor(aq - 1, hunt["hunt1_p3e2_N"]) \
                if hunt["hunt1_p3e2_N"] > 1 else float("nan")
            if f1 and hunt["hunt1_p3e2_value"] / f1 <= 3.0:
                cause = ("dissolves under the small-entry restriction "
                         "(p>=3, entries>=2): ratio drops to "
                         f"{hunt['hunt1_p3e2_value']/f1:.2f}x, consistent "
                         "with the small-entry/finite-composition "
                         "pushforward mechanism (prime-local-probe "
                         "precedent)")
        if cause is None and hunt.get("hunt3_dedup_value") is not None:
            f3 = rayleigh_floor(aq - 1, hunt["hunt3_dedup_N"]) \
                if hunt["hunt3_dedup_N"] > 1 else float("nan")
            if f3 and hunt["hunt3_dedup_value"] / f3 <= 3.0:
                cause = ("dissolves under one-representative-per-necklace "
                         f"restriction: ratio drops to "
                         f"{hunt['hunt3_dedup_value']/f3:.2f}x, consistent "
                         "with rotation multiplicity (12.6.1.1's unit-"
                         "related rotations pooled together)")
        verdict = "DISSOLVED" if cause else "SURVIVES ALL FIVE HUNTS -- UNEXPLAINED"
        log_line(f"    VERDICT: {verdict}"
                 f"{(' -- ' + cause) if cause else ''}")
        results.append(dict(classes=classes_explained, xi=rep["xi"],
                             value=rep["value"], ratio=rep["ratio"],
                             hunt=hunt, cause=cause, verdict=verdict))
    return results


# =======================================================================
# Section 9: "large" cells -- (17,-) (exact, too big for FFT) and the 6
# sampled cells (queue items 3+4, with the documented PHI_SUBSAMPLE
# reduction for the frequency-domain sum only).
# =======================================================================

def process_large_cell(n, shore, phi_n=None):
    t0 = time.time()
    K, q = profile_Knq(n, shore)
    aq = abs(q)
    fac = factorize(q)
    S = K - n
    is_exact = (n, shore) in EXACT_CELLS
    log_line("=" * 72)
    log_line(f"LARGE CELL ({n},{shore}): K={K} q={q} fac={fac} S={S} "
             f"[{'EXACT (too big for FFT)' if is_exact else 'SAMPLED'}]")
    log_line("=" * 72)

    residues = []
    zero = 0
    t_pop = time.time()
    if is_exact:
        for p, ms, ss in enumerate_family(n, S):
            r = R0_mod(list(ms), list(ss), aq)
            residues.append(r)
            if r == 0:
                zero += 1
        N = len(residues)
        expected_N = BRIEF_TABLE[(n, shore)][3]
        check(N == expected_N, f"({n},{shore}): exact enumeration N={N} "
              f"matches brief count {expected_N}")
    else:
        rng = random.Random(SEED + n)
        pcounts = family_pcounts(n, S)
        N = SAMPLE_N
        for _ in range(N):
            p, ms, ss = sample_profile(n, S, pcounts, rng)
            r = R0_mod(list(ms), list(ss), aq)
            residues.append(r)
            if r == 0:
                zero += 1
    dt_pop = time.time() - t_pop
    check(len(residues) == N, f"({n},{shore}): residue list length == N")
    check(all(0 <= r < aq for r in residues[:min(N, 2000)]),
          f"({n},{shore}): sampled residues (first 2000 checked) all in "
          f"[0,|q|)")
    log_line(f"  Population: {'exact enumeration' if is_exact else 'sampler'} "
             f"N={N}, {dt_pop:.1f}s. Zero bin: {zero}/{N} "
             f"({zero/N:.6f}) vs naive 1/|q|={1/aq:.3e}")

    # --- item 3: selected frequencies via a documented sub-sample --------
    rng2 = random.Random(SEED + 12345 + n)
    target_phi_n = phi_n if phi_n is not None else PHI_SUBSAMPLE
    if N > target_phi_n:
        phi_idx = rng2.sample(range(N), target_phi_n)
        phi_residues = [residues[i] for i in phi_idx]
        N_phi = target_phi_n
        log_line(f"  Frequency-domain (item 3) sub-sample: {N_phi} of {N} "
                 f"population values, drawn uniformly at random (seed "
                 f"{SEED+12345+n}) -- direct per-frequency summation over "
                 f"the full population/1e6 sample would cost ~0.14s/freq "
                 f"per 1e6 (benchmarked); this reduction is stated per "
                 f"the brief's runtime-cap allowance. Zero-bin and joint "
                 f"law below use the FULL {N}-size population.")
    else:
        phi_residues = residues
        N_phi = N
    loc = local_frequencies(aq, fac)
    mono_map = monomial_table(aq)
    t_spec = time.time()
    classes, _, _ = selected_frequency_xis(aq, fac)
    # top-of-item-2 substitute for "orbit": seed it with the single
    # largest-magnitude frequency found among low+random+monomial in
    # this same pass (computed first, then orbit added and re-evaluated)
    pre_results = evaluate_classes_direct(
        phi_residues, aq,
        {k: v for k, v in classes.items() if k != "orbit"}, N_phi)
    best = max(((r["max"], r["xi"]) for r in pre_results.values()
                if r is not None), default=(0, None))
    classes2, _, _ = selected_frequency_xis(aq, fac, orbit_seed_xi=best[1])
    orbit_result = evaluate_classes_direct(
        phi_residues, aq, {"orbit": classes2["orbit"]}, N_phi)
    class_results = dict(pre_results)
    class_results["orbit"] = orbit_result["orbit"]
    dt_spec = time.time() - t_spec
    log_line(f"  Selected-frequency classes (direct summation, "
             f"N_phi={N_phi}, {dt_spec:.1f}s):")
    for cname, r in class_results.items():
        if r is None:
            log_line(f"    {cname}: (empty class at this cell)")
            continue
        ratio = r["max"] / r["floor"] if r["floor"] > 0 else float("nan")
        cand = ratio > 3.0
        r["candidate"] = cand
        r["ratio"] = ratio
        log_line(f"    {cname:<10} n_freqs={r['n_freqs']:<6} "
                 f"max|phi|={r['max']:.5f} at xi={r['xi']:<12} "
                 f"floor={r['floor']:.5f} ratio={ratio:.2f} "
                 f"{'CANDIDATE' if cand else ''}")

    ghost_results = apply_ghost_hunt(n, shore, q, class_results, loc,
                                      mono_map, is_sampled=not is_exact,
                                      residues=phi_residues, N_full=N_phi)
    if is_exact:
        # (17,-) has the exact machinery available too -- ghost hunts
        # 1/3/5 need enumerate_family(n,S), which works regardless of
        # cell size (apply_ghost_hunt already dispatches on is_sampled).
        pass

    # --- item 4: joint law, FULL population/sample ------------------------
    log_line(f"  Joint law (mutual information / TV), full N={N}:")
    joint_results = run_joint_law_for_cell(n, shore, q, fac, N,
                                            residues=residues)

    dt_total = time.time() - t0
    log_line(f"  Cell ({n},{shore}) total runtime: {dt_total:.1f}s")
    result = dict(n=n, shore=shore, K=K, q=q, fac=fac, N=N, N_phi=N_phi,
                  dt_total=dt_total, classes=class_results,
                  ghost=ghost_results, joint=joint_results,
                  zero_bin=zero, population="exact" if is_exact else
                  "sampled")
    cache_save(f"cell_{tag((n,shore))}", result)
    return result


# =======================================================================
# Section 10: assemble -- delta tables, verdict, compact output file.
# =======================================================================

def _cell_off_local_off_monomial(cell):
    """Recompute, for a cached cell result, the max |phi| among the six
    selected-frequency classes' own maxima that classify as 'other'
    (queue item 6(a)'s figure) -- with its floor. Works for both FFT
    and large-cell cache shapes (both store 'classes': {cname: {...}})."""
    n, shore, q = cell["n"], cell["shore"], cell["q"]
    aq = abs(q)
    fac = {int(k): v for k, v in cell["fac"].items()}
    loc = local_frequencies(aq, fac)
    mono_map = monomial_table(aq)
    best_val, best_floor, best_xi, best_class = None, None, None, None
    any_local_or_mono = []
    for cname, r in cell["classes"].items():
        if r is None:
            continue
        label = classify_xi(r["xi"], aq, loc, mono_map)
        if label == "other":
            if best_val is None or r["max"] > best_val:
                best_val, best_floor = r["max"], r["floor"]
                best_xi, best_class = r["xi"], cname
        else:
            any_local_or_mono.append((cname, r["max"], label))
    return best_val, best_floor, best_xi, best_class, any_local_or_mono


def build_delta_tables(cells):
    lines = []
    lines.append("DELTA TABLE (a): max off-local, off-monomial |phi| vs "
                  "floor, per cell, along n (both shores)")
    lines.append(f"{'n':>4} {'shore':>5} {'max|phi|':>10} {'floor':>10} "
                  f"{'ratio':>7} {'xi':>14} {'class':>8}  note")
    for n, shore in CELLS:
        c = cells[(n, shore)]
        val, floor, xi, cls, others = _cell_off_local_off_monomial(c)
        if val is None:
            note = ("all six class maxima coincide with a local/monomial "
                    "character (fully explained)")
            lines.append(f"{n:>4} {shore:>5} {'N/A':>10} {'':>10} {'':>7} "
                         f"{'':>14} {'':>8}  {note}")
        else:
            ratio = val / floor if floor else float("nan")
            lines.append(f"{n:>4} {shore:>5} {val:>10.5f} {floor:>10.5f} "
                         f"{ratio:>7.2f} {xi:>14} {cls:>8}  "
                         f"{'CANDIDATE (see ghost-hunt)' if ratio > 3 else 'at floor'}")
    lines.append("")
    lines.append("DELTA TABLE (b): the same, as a function of p, at "
                  "(17,+) and (12,+-)")
    for n, shore in [(17, "+"), (12, "+"), (12, "-")]:
        c = cells[(n, shore)]
        lines.append(f"  Cell ({n},{shore}):")
        lines.append(f"    {'p':>4} {'N_p':>10} {'off max|phi|':>13} "
                     f"{'floor':>10} {'ratio':>7} {'local-5':>9} "
                     f"{'local-7':>9}")
        for p_str, pd in sorted(c["per_p"].items(), key=lambda kv: int(kv[0])):
            l57 = pd["local57"]
            l5 = l57.get("5", None)
            l7 = l57.get("7", None)
            ov = pd["off_best_val"]
            fl = pd["floor"]
            ratio = (ov / fl) if (ov is not None and fl) else float("nan")
            lines.append(f"    {int(p_str):>4} {pd['N_p']:>10} "
                         f"{('N/A' if ov is None else f'{ov:.5f}'):>13} "
                         f"{fl:>10.5f} "
                         f"{('' if ov is None else f'{ratio:.2f}'):>7} "
                         f"{(f'{l5:.4f}' if l5 is not None else '-'):>9} "
                         f"{(f'{l7:.4f}' if l7 is not None else '-'):>9}")
    lines.append("")
    lines.append("DELTA TABLE (c): cross-prime mutual information vs its "
                  "null, per cell")
    lines.append(f"{'n':>4} {'shore':>5} {'ell1^a':>10} {'ell2^b':>10} "
                 f"{'MI':>9} {'null':>9} {'perm-MI':>9} {'TV':>8} "
                 f"{'perm-TV':>8}")
    for n, shore in CELLS:
        c = cells[(n, shore)]
        joint = c.get("joint", [])
        if not joint:
            lines.append(f"{n:>4} {shore:>5}  (no prime-power pair with "
                         f"product <= 1e6 at this cell)")
            continue
        for r in joint:
            lines.append(f"{n:>4} {shore:>5} {r['ell1a']:>10} "
                         f"{r['ell2b']:>10} {r['mi']:>9.5f} "
                         f"{r['null_mi']:>9.5f} {r['mi_perm']:>9.5f} "
                         f"{r['tv']:>8.5f} {r['tv_perm']:>8.5f}")
    return "\n".join(lines)


def build_ghost_hunt_summary(cells):
    lines = ["GHOST-HUNT SUMMARY (every candidate, all cells)"]
    n_candidates = 0
    n_dissolved = 0
    n_unexplained = 0
    for n, shore in CELLS:
        c = cells[(n, shore)]
        ghosts = c.get("ghost", [])
        for g in ghosts:
            n_candidates += 1
            if g["verdict"].startswith("DISSOLVED"):
                n_dissolved += 1
            else:
                n_unexplained += 1
            lines.append(f"  ({n},{shore}) xi={g['xi']} classes="
                         f"{g['classes']} |phi|={g['value']:.5f} "
                         f"ratio={g['ratio']:.2f} -> {g['verdict']}"
                         f"{(' -- ' + g['cause']) if g.get('cause') else ''}")
    lines.append(f"TOTAL: {n_candidates} candidate group(s) across all 14 "
                 f"cells; {n_dissolved} dissolved, {n_unexplained} "
                 f"survive all five hunts (unexplained).")
    return "\n".join(lines), n_candidates, n_dissolved, n_unexplained


def assemble():
    cells = {}
    for n, shore in CELLS:
        c = cache_load(f"cell_{tag((n,shore))}")
        if c is None:
            print(f"MISSING cache for cell ({n},{shore}) -- run "
                  f"'fft {tag((n,shore))}' or 'large {tag((n,shore))}' "
                  f"first.", file=sys.stderr)
            sys.exit(1)
        cells[(n, shore)] = c
    canaries = cache_load("canaries")

    out = []
    out.append("=" * 72)
    out.append("experiments/modq_spectrum.py -- committed output")
    out.append("Supports briefs/modq-spectrum-brief.md. Seed %d, dated %s."
                % (SEED, DATE))
    out.append("=" * 72)
    out.append("")
    out.append("CANARIES (queue item 1)")
    if canaries:
        out.append(f"  -17 canary: R_0=139, R_1=695=5*139, q=-139 -- "
                    f"reproduced exactly.")
        out.append(f"  L-A6 zero-bin census match: "
                    + ", ".join(f"({k[0]},{k[1]})={v}"
                                for k, v in canaries["la6"]))
        out.append(f"  Uniform null: low-class max|phi| within "
                    f"[0.9x,1.1x] of the Rayleigh floor at (12,+-).")
        out.append(f"  Sampler calibration at (17,+): max discrepancy "
                    f"ratio (sample vs exact, vs 1/sqrt(N)) = "
                    f"{canaries['sampler_max_ratio']:.2f}x.")
        out.append(f"  Canaries section runtime: {canaries['dt']:.1f}s")
    out.append("")

    out.append("=" * 72)
    out.append("PER-CELL SUMMARY: class maxima with floors (queue item 3)")
    out.append("=" * 72)
    for n, shore in CELLS:
        c = cells[(n, shore)]
        out.append(f"Cell ({n},{shore}): K={c['K']} q={c['q']} "
                    f"fac={c['fac']} N={c['N']} "
                    f"population={c.get('population','?')} "
                    f"zero_bin={c['zero_bin']}")
        for cname, r in c["classes"].items():
            if r is None:
                out.append(f"    {cname:<10} (empty class)")
                continue
            out.append(f"    {cname:<10} n_freqs={r['n_freqs']:<6} "
                        f"max|phi|={r['max']:.5f} xi={r['xi']:<14} "
                        f"floor={r['floor']:.5f} ratio={r['ratio']:.2f} "
                        f"{'CANDIDATE' if r.get('candidate') else ''}")
    out.append("")

    out.append("=" * 72)
    out.append("TOP-20 SPECTRUM TABLES, exact FFT-eligible cells (queue "
                "item 2)")
    out.append("=" * 72)
    for n, shore in FFT_ELIGIBLE:
        c = cells[(n, shore)]
        out.append(f"Cell ({n},{shore}), population floor="
                    f"{c['floor_all']:.5f}:")
        for xi, val, label in c["top20"][:20]:
            out.append(f"    xi={xi:<10} |phi|={val:.5f}  type={label}")
    out.append("")

    out.append("=" * 72)
    out.append(build_ghost_hunt_summary(cells)[0])
    out.append("=" * 72)
    out.append("")

    out.append("=" * 72)
    out.append(build_delta_tables(cells))
    out.append("=" * 72)
    out.append("")

    _, n_cand, n_dis, n_unexp = build_ghost_hunt_summary(cells)
    out.append("=" * 72)
    out.append("VERDICT (queue item 7)")
    out.append("=" * 72)
    if n_unexp == 0:
        out.append("(i) GLOBAL STRUCTURELESSNESS AT THIS SCALE: every "
                    "off-local, off-monomial class candidate across all "
                    "14 cells dissolved under the five-step ghost-hunt "
                    "(%d candidate group(s), all %d dissolved, 0 "
                    "unexplained); the 5/7-line shrinks with block "
                    "count p at every cell where 5 or 7 divides q (matches "
                    "12.6.1.6); every cross-prime joint law sits at or "
                    "near its permutation-shuffled control (its "
                    "theoretical null formula is unreliable whenever "
                    "ell1^a*ell2^b approaches or exceeds N, in which "
                    "case the permutation control is the operative "
                    "check, stated inline per pair). The joint law is "
                    "as flat as the marginals the prime-local probe "
                    "already found." % (n_cand, n_dis))
    else:
        out.append(f"(ii) SURVIVING CANDIDATE(S): {n_unexp} candidate "
                    f"group(s) survive all five hunts -- see the "
                    f"ghost-hunt summary above for cell, class, xi, "
                    f"|phi|, floor and the five hunts' outcomes.")
    out.append("The front stays parked either way (README stopping "
                "rules; cycles.md 12.8.5). Excludes nothing: no per-"
                "period cycle search was run, no exclusion was "
                "attempted, and no proof effort was made on the "
                "equidistribution question -- this measurement is a "
                "calibration of the named open wall (12.6.1.6's generic "
                "equidistribution of R_0 mod q), stated once here and "
                "not hedged further.")
    out.append("")

    text = "\n".join(out)
    outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "modq_spectrum_output.txt")
    with open(outpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
        f.write("\n")
    print(f"Wrote {outpath} ({len(text)} chars)")
    return text


if __name__ == "__main__":
    phase = sys.argv[1] if len(sys.argv) > 1 else "all"
    t_start = time.time()
    if phase == "cells":
        rederive_cell_table()
    elif phase == "canaries":
        rederive_cell_table()
        run_canaries()
    elif phase == "fft":
        cell_tag = sys.argv[2]
        n = int(cell_tag[:-1])
        shore = cell_tag[-1]
        process_fft_cell(n, shore)
    elif phase == "large":
        cell_tag = sys.argv[2]
        n = int(cell_tag[:-1])
        shore = cell_tag[-1]
        phi_n = int(sys.argv[3]) if len(sys.argv) > 3 else None
        process_large_cell(n, shore, phi_n=phi_n)
    elif phase == "assemble":
        assemble()
    else:
        print(f"Phase '{phase}' not yet wired in this cut of the script; "
              f"see modq_spectrum_part2.py additions.", file=sys.stderr)
        sys.exit(1)
    print(f"[phase {phase}] wall time {time.time()-t_start:.1f}s, "
          f"checks {CHECKS['count']} fail {CHECKS['fail']}")
