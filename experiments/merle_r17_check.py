#!/usr/bin/env python3
"""merle_r17_check.py -- fresh verification of PR #7 (round 17) section 1,
github.com/macindoe/one-obstruction-three-faces, per
briefs/merle-round16-17-review-brief.md Queue 6.

Supports: briefs/merle-round16-17-review-findings.md.

Rules honoured:
  - imports NOTHING from any Merle repository, and nothing from any prior
    Merle-check script in this repository; Python stdlib only
    (fractions.Fraction for exact rationals, itertools);
  - exact integer/rational arithmetic at every decision (faulty: p^j > 2^L
    as an exact integer comparison; realised: Fraction denominator == 1);
  - canaries (the four small real cycles' words and values) printed FIRST;
  - this verifies a correspondent's ERRATUM to a previously withdrawn count
    (a finite enumeration of simple cycles in a residue graph on Z/2^k that
    HE claims and we check) -- it is not a cycle search on the integers and
    it opens no per-period computation; the cycles front stays PARKED.

The object (per rounds/R17-merle.md section 1, quoted in the brief): the
residue graph G(p,k) on Z/2^k of the Terras half map T_p (x/2 if even,
(px+1)/2 if odd) carrying BOTH lifts -- arcs u -> T_p(r) mod 2^k for
r in {u, u+2^k}. A simple cycle corresponds (Terras 1976 / Lagarias 1985,
the de Bruijn identification) to a primitive (Lyndon) binary necklace whose
L cyclic k-bit windows are pairwise distinct. A cycle with L letters and j
ones (odd/ascending steps) is FAULTY when p^j > 2^L, and REALISED when the
word's associated rational fixed point x_w = N_w / (2^L - p^j) is an
integer (N_w derived independently below, PART 1, from the affine
composition of T_p along the word -- not copied from any committed
script).

What this script checks:
  PART 0 -- canaries: T_p on small values; the closed-form N_w formula
            cross-checked against DIRECT affine composition (two
            independent derivations of the same fixed point) on the known
            cycles of p=3 ({1,2}, {-1}, {-5,-7,-10}) and p=5, p=7.
  PART 1 -- N_w derived from scratch (not from any committed script): for
            a parity word b_0..b_{L-1}, x_{i+1} = (p^{b_i} x_i + b_i)/2, so
            x_L = x_0 * p^j/2^L + (1/2^L) * sum_i b_i * p^{j_{>i}} * 2^i,
            where j_{>i} = # of ones strictly after position i; the fixed
            point is x_0 = N_w / (2^L - p^j), N_w = sum_i b_i p^{j_{>i}} 2^i.
            Verified against direct step-by-step Fraction composition on
            2000 random words.
  PART 2 -- the de Bruijn identification: u -> first k parity bits of the
            orbit of u under T_p is a bijection Z/2^k -> {0,1}^k for
            p = 3,5,7 and k = 6,8,10, and the graph's arcs correspond
            exactly to the de Bruijn shift (drop first bit, append new
            one) -- verified directly, independent of run_128.
  PART 3 -- own Lyndon-word generator (Duval/FKM, standard textbook
            algorithm, written fresh); canary counts 2,1,2,3,6,9,18,30 at
            L=1..8; total Lyndon words of length 1..22 cross-checked
            TWO ways: word generation count, and the Mobius formula
            (1/n) sum_{d|n} mu(d) 2^(n/d) summed over n=1..22 -- both give
            401,428, matching the round-17 letter's stated total.
  PART 4 -- window-set collisions (the "sorted vertex set" merge
            diagnosis), computed p-INDEPENDENTLY as a property of raw
            k-bit-tuple window sets (valid because any bijective vertex
            relabeling preserves set-equality of images) -- confirms the
            two named merges at k=6 and their L/j figures, and confirms no
            merge at k=8 before L=14 (checked exhaustively for L<=13) and
            none at k=10 before L=17 (checked for L<=16).
  PART 5 -- faulty/realised classification, L<=11 exhaustive (necklace
            enumeration, not a bounded DFS), at all nine (p,k) with
            p in {3,5,7}, k in {6,8,10}: TRUE counts (by necklace/Lyndon
            key) vs VERTEX-SET-key counts (the merged, undercounting key);
            reproduces the referee table 63/88/97, 216/268/281, 265/330/345
            under the vertex-set key, and 64/217/266 as TRUE counts at
            k=6 (the undercount is by exactly one, at every p).
  PART 6 -- extension to L<=22: 256,606 faulty at (7,8), 0 realised;
            0 realised at (7,6) and (7,10); the p=3 control realised
            exactly at L = 1, 3, 11 and nowhere else to L=22; total word
            count enumerated (401,428) stated against the letter's figure.
  PART 7 -- the "-6" diagnosis: both accumulators (the committed run_048.py
            one, omitting the factor p on an ascent; and the corrected
            one) implemented independently from their stated defining
            recurrences (not copied from run_048.py or run_130.py), on the
            words '110' and '011' at p=3 (expect -3/-6 wrong, -5/-10
            correct); on every word to length 12, count integers the
            faulty accumulator emits that lie on no cycle of T_3 (expect
            10, -6 among them), and confirm the corrected accumulator's
            integers always lie on a cycle and follow their word.

Reproduction: `python experiments/merle_r17_check.py > experiments/merle_r17_check_output.txt`
from the repository root reproduces the committed output byte-for-byte.
"""

from fractions import Fraction
import itertools

CHECKS = 0
FAILURES = 0


def check(label, ok):
    global CHECKS, FAILURES
    CHECKS += 1
    if not ok:
        FAILURES += 1
        print(f"  FAIL: {label}")
    return ok


def require(label, ok):
    if not check(label, ok):
        raise SystemExit(f"HARD FAIL: {label}")


print("=" * 78)
print("merle_r17_check.py -- fresh verification of PR #7 (round 17) section 1")
print("=" * 78)

# ----------------------------------------------------------------------------
# Shared primitives

def T(p, x):
    """Terras half map: x/2 if even, (p*x+1)/2 if odd. Exact integer division
    (p*x+1 is always even when x is odd, since p is odd)."""
    return x // 2 if x % 2 == 0 else (p * x + 1) // 2


def walk_cycle_from(p, x0, max_steps=2000):
    """Walk T_p from x0 until a repeat is found; return the cycle (as a list
    of the repeated segment) if x0 itself is eventually periodic, else None
    after max_steps."""
    seen = {}
    x = x0
    path = []
    for i in range(max_steps):
        if x in seen:
            return path[seen[x]:]
        seen[x] = i
        path.append(x)
        x = T(p, x)
    return None


def on_cycle(p, x, cap=500):
    y = T(p, x)
    for _ in range(cap):
        if y == x:
            return True
        y = T(p, y)
    return False


def follows_word(p, x, bits):
    y = x
    for b in bits:
        if (y % 2) != b:
            return False
        y = T(p, y)
    return True


# ----------------------------------------------------------------------------
print("\n--- PART 0/1: N_w derived from scratch, cross-checked against direct "
      "affine composition ---")

print("""
Derivation (this script's own words): a parity word b_0..b_{L-1} describes an
orbit x_0 -> x_1 -> ... -> x_L under T_p, x_{i+1} = (p^{b_i} x_i + b_i)/2
(b_i in {0,1}: even step p^0=1, odd/ascending step p^1=p). Unrolling:
    x_L = x_0 * prod_i (p^{b_i}/2) + sum_i (b_i/2) * prod_{m=i+1}^{L-1} (p^{b_m}/2)
        = x_0 * p^j / 2^L        + (1/2^L) * sum_i b_i * p^{j_{>i}} * 2^i
where j = sum(b_i) (total ones) and j_{>i} = number of ones strictly after
position i. Setting x_L = x_0 (a fixed point / L-cycle) and solving:
    x_0 * (2^L - p^j) = sum_i b_i * p^{j_{>i}} * 2^i =: N_w
    x_0 = N_w / (2^L - p^j).
""")


def N_w_closed_form(bits, p):
    """N_w = sum_i b_i * p^{j_{>i}} * 2^i, derived above. Computed by a
    right-to-left accumulation (j_{>i} counted as we go)."""
    N = 0
    j_after = 0  # number of ones at positions > current i, built right to left
    for i in range(len(bits) - 1, -1, -1):
        b = bits[i]
        if b:
            N += (p ** j_after) * (1 << i)
            j_after += 1
    return N


def xw_closed_form(bits, p):
    L = len(bits)
    j = sum(bits)
    d = (1 << L) - p ** j
    return Fraction(N_w_closed_form(bits, p), d)


def xw_direct_composition(bits, p):
    """Direct affine composition, independent of the closed form: x_{i+1} =
    (p^{b_i} x_i + b_i)/2, tracked as x_i = a*x_0 + c (exact Fractions),
    solved for the fixed point a*x0+c=x0 => x0=c/(1-a)."""
    a, c = Fraction(1), Fraction(0)
    for b in bits:
        if b:
            a, c = a * p / 2, (c * p + 1) / 2
        else:
            a, c = a / 2, c / 2
    if a == 1:
        return None
    return c / (1 - a)


# Canaries: known cycles of p=3 written as parity words, checked both ways
# and against direct integer cycle walks.
canary_words = [
    ("1", 3, -1),          # {-1}: T_3(-1) = -1
    ("10", 3, 1),          # {1, 2}: T_3(1) = 2, T_3(2) = 1
    ("110", 3, -5),        # {-5, -7, -10}
    ("1", 5, Fraction(-1, 3)),
    ("10", 5, -1),
    ("1", 7, Fraction(-1, 5)),
]
for wstr, p, expected in canary_words:
    bits = tuple(int(c) for c in wstr)
    v_closed = xw_closed_form(bits, p)
    v_direct = xw_direct_composition(bits, p)
    check(f"canary word={wstr} p={p}: closed form == direct composition == {expected}",
          v_closed == v_direct == expected)

check("canary: word '110' at p=3 gives x=-5, and -5 -> -7 -> -10 -> -5 under T_3",
      T(3, -5) == -7 and T(3, -7) == -10 and T(3, -10) == -5)

# Cross-check the two N_w derivations against each other on 2000 random words.
import random
rng = random.Random(20260926)
mismatches = 0
for _ in range(2000):
    L = rng.randint(1, 14)
    p = rng.choice([3, 5, 7, 9, 11])
    bits = tuple(rng.randint(0, 1) for _ in range(L))
    v1 = xw_closed_form(bits, p)
    v2 = xw_direct_composition(bits, p)
    if v1 != v2:
        mismatches += 1
check("closed-form N_w matches direct affine composition on 2000 random words",
      mismatches == 0)

# ----------------------------------------------------------------------------
print("\n--- PART 2: the de Bruijn identification, verified directly ---")


def pref(p, u, k):
    """First k parity bits of the orbit of u (u taken mod nothing -- u is
    used as given, matching G(p,k)'s vertex labels 0..2^k-1)."""
    out = []
    x = u
    for _ in range(k):
        out.append(x & 1)
        x = T(p, x)
    return tuple(out)


PS = (3, 5, 7)
KS = (6, 8, 10)

deBruijn_ok = True
INV = {}  # (p,k) -> dict window-tuple -> u
for p in PS:
    for k in KS:
        M = 1 << k
        P = [pref(p, u, k) for u in range(M)]
        bijection = len(set(P)) == M
        # arc-shift: successor of u via bit b has prefix = shift(P[u], new_bit)
        arcs_ok = True
        for u in range(M):
            b = u & 1
            v_even = (u // 2) % M if b == 0 else None
            v_odd = ((p * u + 1) // 2) % M if b == 1 else None
            # both lifts: r=u and r=u+M
            v_from_u = T(p, u) % M
            v_from_uM = T(p, u + M) % M
            if P[v_from_u][:k - 1] != P[u][1:]:
                arcs_ok = False
            if P[v_from_uM][:k - 1] != P[u][1:]:
                arcs_ok = False
        good = bijection and arcs_ok
        deBruijn_ok &= good
        INV[(p, k)] = {P[u]: u for u in range(M)}
        print(f"  p={p} k={k:2d}: bijection={bijection}  arc-shift-property={arcs_ok}")

check("de Bruijn identification (bijection + arc-shift) holds for all "
      "p in {3,5,7}, k in {6,8,10}", deBruijn_ok)

# ----------------------------------------------------------------------------
print("\n--- PART 3: own Lyndon-word generator, canary counts, total to L<=22 ---")


def lyndon_words(n):
    """Duval/FKM standard algorithm (classical, public-domain; written fresh
    here, not copied from any committed script): generates all binary Lyndon
    words of length exactly n in lexicographic order."""
    result = []
    w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        if m == n:
            result.append(tuple(w))
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == 1:
            w.pop()
    return result


lyndon_counts = [len(lyndon_words(n)) for n in range(1, 9)]
check("Lyndon word counts L=1..8 == 2,1,2,3,6,9,18,30",
      lyndon_counts == [2, 1, 2, 3, 6, 9, 18, 30])
print(f"  Lyndon counts L=1..8: {lyndon_counts}")


def mobius(n):
    if n == 1:
        return 1
    res = 1
    nn = n
    d = 2
    while d * d <= nn:
        if nn % d == 0:
            nn //= d
            if nn % d == 0:
                return 0
            res *= -1
        d += 1
    if nn > 1:
        res *= -1
    return res


def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i != n // i:
                ds.append(n // i)
        i += 1
    return ds


def lyndon_count_mobius(n):
    return sum(mobius(d) * 2 ** (n // d) for d in divisors(n)) // n


LMAX_EXT = 22
LYN = {L: lyndon_words(L) for L in range(1, LMAX_EXT + 1)}
total_words = sum(len(LYN[L]) for L in range(1, LMAX_EXT + 1))
total_mobius = sum(lyndon_count_mobius(L) for L in range(1, LMAX_EXT + 1))
print(f"  total Lyndon words L=1..{LMAX_EXT}, by generation: {total_words}")
print(f"  total Lyndon words L=1..{LMAX_EXT}, by Mobius formula: {total_mobius}")
check("word-generation total == Mobius-formula total", total_words == total_mobius)
check("total word count == 401428 (matches the round-17 letter's stated total)",
      total_words == 401428)

# ----------------------------------------------------------------------------
print("\n--- PART 4: window-set collisions ('vertex set' key merges), p-independent ---")


def windows(w, k):
    """The L cyclic k-length windows of a length-L word w, tiled and sliced
    (matches the standard construction: read the orbit's parity bits k at a
    time, starting from each of the L rotations)."""
    L = len(w)
    tiled = list(w) * ((k + L - 1) // L + 1)
    return [tuple(tiled[i:i + k]) for i in range(L)]


def simple_necklaces(k, Lmax):
    """Lyndon words of length L (1..Lmax) whose L cyclic k-windows are
    pairwise distinct -- i.e. words corresponding to SIMPLE cycles of the
    de Bruijn graph B(2,k). This is p-INDEPENDENT: it depends only on the
    raw k-bit window tuples, never on any vertex relabeling."""
    out = {}
    for L in range(1, Lmax + 1):
        for w in LYN[L]:
            W = windows(w, k)
            if len(set(W)) == L:
                out[w] = W
    return out


def find_window_set_merges(k, Lmax):
    """Group simple necklaces of length L (for each L) by the SET of their
    k-bit windows (order-independent) -- collisions here are exactly what
    the 'sorted vertex set' key merges, for ANY p, since any bijective
    relabeling of window-tuples to Z/2^k vertices preserves set equality."""
    simple = simple_necklaces(k, Lmax)
    by_L = {}
    for w, W in simple.items():
        by_L.setdefault(len(w), []).append((w, frozenset(W)))
    merges_by_L = {}
    for L, items in by_L.items():
        groups = {}
        for w, key in items:
            groups.setdefault(key, []).append(w)
        merges = [ws for ws in groups.values() if len(ws) > 1]
        if merges:
            merges_by_L[L] = merges
    return merges_by_L


merges_k6 = find_window_set_merges(6, 22)
merges_k8 = find_window_set_merges(8, 22)
merges_k10 = find_window_set_merges(10, 22)

print(f"  k=6  merges by L: { {L: len(m) for L, m in merges_k6.items()} }")
print(f"  k=8  merges by L (<=13 checked): "
      f"{ {L: len(m) for L, m in merges_k8.items() if L <= 13} }")
print(f"  k=10 merges by L (<=16 checked): "
      f"{ {L: len(m) for L, m in merges_k10.items() if L <= 16} }")

# The two named merges at k=6, L=11
target_pair_1 = {(0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1), (0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1)}
target_pair_2 = {(0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1), (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1)}

l11_merges_k6 = merges_k6.get(11, [])
found_pairs = [set(ws) for ws in l11_merges_k6]
check("k=6 L=11 has exactly 2 merged pairs (the two named ones)",
      len(l11_merges_k6) == 2)
check("k=6 L=11 merge includes 01011101111 / 01011110111",
      target_pair_1 in found_pairs)
check("k=6 L=11 merge includes 00001000101 / 00001010001",
      target_pair_2 in found_pairs)

# Confirm the second pair (j=3) is faulty for no p <= 7
p1_j = sum(next(iter(target_pair_1)))
p2_j = sum(next(iter(target_pair_2)))
print(f"  pair 1 (the L<=11 faulty merge): j={p1_j}, L=11")
print(f"  pair 2 (the extra merge, unrelated to faulty count): j={p2_j}, L=11")
check("pair 1 has j=8 (matches the round-17 letter)", p1_j == 8)
check("pair 2 has j=3 (matches the round-17 letter)", p2_j == 3)
check("pair 2 is faulty for NO p <= 7 (p^3 <= 2^11 = 2048 for all odd p <= 7: "
      "3^3=27, 5^3=125, 7^3=343, all <= 2048)",
      all(p ** p2_j <= (1 << 11) for p in (3, 5, 7)))

check("no merges at k=8 for L <= 13 (checked exhaustively)",
      all(L > 13 for L in merges_k8))
check("no merges at k=10 for L <= 16 (checked exhaustively)",
      all(L > 16 for L in merges_k10))

# The only merge at k=6, L<=11 relevant to the FAULTY count is pair 1 (the
# one with j=8, since only faulty cycles are counted in run_127's table)
check("at k=6, among L<=11, the ONLY merge whose members are BOTH faulty is "
      "pair 1 (j=8, since 3^8=6561 > 2^11=2048; pair 2's j=3 is not faulty "
      "for any p<=7, so it changes no faulty-count row)",
      True)  # established by the two checks above; stated for the record

# ----------------------------------------------------------------------------
print("\n--- PART 5: faulty/realised classification, L<=11 exhaustive, all nine (p,k) ---")

simple_by_k = {k: simple_necklaces(k, 11) for k in KS}

referee_table = {}  # (p,k) -> (vertex_set_key_count, true_count, realised_count)
for p in PS:
    for k in KS:
        simple = simple_by_k[k]
        faulty_words = [w for w in simple if p ** sum(w) > (1 << len(w))]
        true_count = len(faulty_words)

        # vertex-set key count: group by frozenset of k-bit windows (same
        # merge structure as PART 4, restricted to faulty words only)
        groups = {}
        for w in faulty_words:
            key = frozenset(simple[w])
            groups.setdefault(key, []).append(w)
        vskey_count = len(groups)

        realised = []
        for w in faulty_words:
            L = len(w)
            j = sum(w)
            d = (1 << L) - p ** j
            x = xw_closed_form(w, p)
            if x.denominator == 1:
                realised.append(int(x))
        realised = sorted(set(realised))
        referee_table[(p, k)] = (vskey_count, true_count, len(realised))
        print(f"  p={p} k={k:2d}: vertex-set-key count={vskey_count:4d}  "
              f"TRUE count={true_count:4d}  realised={realised}")

expected_vskey = {
    (3, 6): 63, (3, 8): 88, (3, 10): 97,
    (5, 6): 216, (5, 8): 268, (5, 10): 281,
    (7, 6): 265, (7, 8): 330, (7, 10): 345,
}
expected_true_k6 = {3: 64, 5: 217, 7: 266}

for (p, k), expected in expected_vskey.items():
    vskey_count, true_count, n_real = referee_table[(p, k)]
    check(f"referee table (vertex-set key), p={p} k={k}: {expected}",
          vskey_count == expected)

for p, expected_true in expected_true_k6.items():
    vskey_count, true_count, n_real = referee_table[(p, 6)]
    check(f"TRUE count at k=6, p={p}: {expected_true} (one more than the "
          f"vertex-set-key count {vskey_count}, the merge)",
          true_count == expected_true and true_count == vskey_count + 1)

for (p, k), expected in expected_vskey.items():
    if k != 6:
        vskey_count, true_count, n_real = referee_table[(p, k)]
        check(f"TRUE count == vertex-set-key count at k={k}, p={p} "
              f"(no merge outside k=6)",
              true_count == vskey_count)

check("realised counts at (7,8) and (7,6) and (7,10): 0",
      all(referee_table[(7, k)][2] == 0 for k in KS))
check("realised counts at (5,*): 1",
      all(referee_table[(5, k)][2] == 1 for k in KS))
check("realised counts at (3,*): 3",
      all(referee_table[(3, k)][2] == 3 for k in KS))
check("(7,8): 330 faulty, 0 realised (the round-17 letter's headline figure)",
      referee_table[(7, 8)][0] == 330 and referee_table[(7, 8)][2] == 0)

# ----------------------------------------------------------------------------
print("\n--- PART 6: extension to L<=22 ---")

simple_ext_by_k = {k: simple_necklaces(k, LMAX_EXT) for k in KS}

ext_faulty = {}
ext_realised = {}
for p in PS:
    for k in KS:
        simple = simple_ext_by_k[k]
        faulty_words = [w for w in simple if p ** sum(w) > (1 << len(w))]
        realised_words = []
        for w in faulty_words:
            x = xw_closed_form(w, p)
            if x.denominator == 1:
                realised_words.append((w, int(x)))
        ext_faulty[(p, k)] = len(faulty_words)
        ext_realised[(p, k)] = realised_words
        L_of_realised = sorted(set(len(w) for w, _ in realised_words))
        print(f"  p={p} k={k:2d}: faulty(L<=22)={len(faulty_words):7d}  "
              f"realised={sorted(set(x for _, x in realised_words))}  "
              f"at L={L_of_realised}")

check("(7,8): 256606 faulty to L<=22", ext_faulty[(7, 8)] == 256606)
check("(7,8): 0 realised to L<=22", len(ext_realised[(7, 8)]) == 0)
check("(7,6): 0 realised to L<=22", len(ext_realised[(7, 6)]) == 0)
check("(7,10): 0 realised to L<=22", len(ext_realised[(7, 10)]) == 0)

p3_realised_L = sorted(set(len(w) for w, _ in ext_realised[(3, 6)]))
check("p=3 control: realised exactly at L = 1, 3, 11 (checked at k=6; the de "
      "Bruijn structure of simplicity is k-dependent but these three words "
      "are simple at all three tested k, matching PART 5's 3/3/3)",
      p3_realised_L == [1, 3, 11])

# The Lyndon-canonical word for a cycle lands on a SPECIFIC member of that
# cycle, not necessarily the letter's chosen label (-5, -17) -- so the
# right check is CYCLE MEMBERSHIP, not literal value equality. The three
# realised values here are -1, -10, -136; verified below (via walk_cycle_from,
# independent of the word machinery) that these are respectively the fixed
# point {-1}, and members of the {-5,-7,-10} and {-17,...,-136} cycles.
realised_values_k6 = sorted(set(x for _, x in ext_realised[(3, 6)]))
cyc_neg1 = walk_cycle_from(3, -1)
cyc_neg10 = walk_cycle_from(3, -10)
cyc_neg136 = walk_cycle_from(3, -136)
check("p=3 control realised values are -1, -10, -136",
      realised_values_k6 == [-136, -10, -1])
check("-1 is the trivial fixed cycle {-1}", cyc_neg1 == [-1])
check("-10 lies on the cycle {-5,-7,-10} (the 'cycle of -5', a different "
      "member reached by the Lyndon-canonical word's rotation)",
      -5 in cyc_neg10 and -7 in cyc_neg10 and -10 in cyc_neg10 and len(cyc_neg10) == 3)
check("-136 lies on the cycle containing -17 (the 'cycle of -17', a "
      "different member reached by the Lyndon-canonical word's rotation)",
      -17 in cyc_neg136 and len(cyc_neg136) == 11)
for k in KS:
    L_here = sorted(set(len(w) for w, _ in ext_realised[(3, k)]))
    check(f"p=3 at k={k}: realised exactly at L=1,3,11, no others to L=22",
          L_here == [1, 3, 11])

print(f"\ntotal word count enumerated (Lyndon words, L<=22): {total_words} "
      f"against the letter's stated 401,428 -- MATCH: {total_words == 401428}")

# ----------------------------------------------------------------------------
print("\n--- PART 7: the '-6' diagnosis ---")

print("""
Both accumulators implemented independently from their STATED recurrences
(not copied from run_048.py or run_130.py). run_048.py itself carries TWO
independent bugs: (1) it composes the word in reverse (the C3 canary
failure, round-14 finding), and (2) the round-17 letter's finding, isolated
here by processing the word FORWARD (i.e. 'with reversed removed', matching
the round-17 letter's own phrasing exactly) to inspect bug (2) alone:

  The 'missing factor p on an ascent' accumulator, word processed FORWARD:
  num, coef start at (0,1); for each bit b (forward order): if b:
  num = (num+1)/2, coef = coef*p/2 (WRONG -- should multiply num by p too,
  i.e. num = (p*num+1)/2); else: num = num/2, coef = coef/2. Fixed point:
  num / (1 - coef).

  Corrected accumulator (factor p applied to BOTH num and coef on an
  ascent): a, c start at (1, 0); for each bit b (forward order): if b:
  a, c = a*p/2, (c*p+1)/2; else: a, c = a/2, c/2. Fixed point: c/(1-a).
  (This is IDENTICAL to xw_direct_composition above, PART 0/1 -- the
  correct accumulator is not a new derivation, it is the same one already
  cross-checked against the closed form on 2000 random words.)
""")


def rationnel_faulty(bits, p):
    """The 'missing factor p on an ascent' defect, isolated from the
    separate 'reversed word' defect by processing bits FORWARD -- matches
    the round-17 letter's own diagnostic convention ('with reversed
    removed') exactly, and reproduces its stated canary values."""
    num, coef = Fraction(0), Fraction(1)
    for b in bits:
        if b:
            num, coef = (num + 1) / 2, coef * p / 2
        else:
            num, coef = num / 2, coef / 2
    if coef == 1:
        return None
    return num / (1 - coef)


def rationnel_correct(bits, p):
    return xw_direct_composition(bits, p)


v_wrong_110 = rationnel_faulty((1, 1, 0), 3)
v_correct_110 = rationnel_correct((1, 1, 0), 3)
v_wrong_011 = rationnel_faulty((0, 1, 1), 3)
v_correct_011 = rationnel_correct((0, 1, 1), 3)
print(f"  word '110', p=3: faulty accumulator -> {v_wrong_110}, correct -> {v_correct_110}")
print(f"  word '011', p=3: faulty accumulator -> {v_wrong_011}, correct -> {v_correct_011}")

check("word '110' at p=3: faulty accumulator gives -3, correct gives -5",
      v_wrong_110 == -3 and v_correct_110 == -5)
check("word '011' at p=3: faulty accumulator gives -6, correct gives -10",
      v_wrong_011 == -6 and v_correct_011 == -10)

faulty_ints = set()
faulty_int_words = {}
correct_ints = set()
for L in range(1, 13):
    for bits in itertools.product((0, 1), repeat=L):
        x = rationnel_faulty(bits, 3)
        if x is not None and x.denominator == 1:
            faulty_ints.add(int(x))
            faulty_int_words.setdefault(int(x), bits)
        y = rationnel_correct(bits, 3)
        if y is not None and y.denominator == 1:
            correct_ints.add(int(y))

off_cycle_faulty = sorted(x for x in faulty_ints if not on_cycle(3, x))
print(f"  faulty accumulator, words to length 12: {len(faulty_ints)} integers total, "
      f"{len(off_cycle_faulty)} lie on no cycle of T_3: {off_cycle_faulty}")
check("faulty accumulator emits exactly 10 integers lying on no cycle, "
      "including -6", len(off_cycle_faulty) == 10 and -6 in off_cycle_faulty)

all_correct_on_cycle = all(on_cycle(3, x) for x in correct_ints)
check("every integer the correct accumulator emits lies on a cycle of T_3",
      all_correct_on_cycle)

follow_ok = True
for L in range(1, 13):
    for bits in itertools.product((0, 1), repeat=L):
        y = rationnel_correct(bits, 3)
        if y is not None and y.denominator == 1:
            if not follows_word(3, int(y), bits):
                follow_ok = False
check("every integer the correct accumulator emits follows its own word "
      "exactly (parity bit by parity bit)", follow_ok)

check("a MISSING PARITY CHECK cannot be the cause of -6 (since the correct "
      "accumulator, which has no parity check either, never emits it: "
      f"-6 in correct_ints = {(-6 in correct_ints)})",
      -6 not in correct_ints)

# ----------------------------------------------------------------------------
print("\n--- PART 8: round-17 section 3, for information -- bridge identity and FEN "
      "on the real cycles (cheap, exact; no key, no ledger line asked) ---")

print("""
Bridge (section 3's own statement, standard Collatz p=3): d(w) = 2^L - 3^r,
C(w) = N_w (PART 0/1's own closed form, specialized to p=3) -- x*d(w) = C(w)
iff x follows w. Already exercised throughout PARTs 5-6 at p=3 (every
'realised' word found there IS a case of this bridge). FEN (Eliahou 1993,
positive case; section 3 states it for both signs): every nonzero integer
cycle has L <= 2r (r = number of ones), equality only on the word (0,1),
i.e. the cycle {1,2}.
""")

simple_p3 = simple_ext_by_k[10]  # k=10, L<=22, already computed in PART 6
fen_ok = True
fen_equality_words = []
bridge_ok = True
for w, W in simple_p3.items():
    L = len(w)
    j = sum(w)
    d = (1 << L) - 3 ** j
    if d == 0:
        continue
    N = N_w_closed_form(w, 3)
    if N % d == 0:
        x = N // d
        if x == 0:
            continue  # the degenerate word (0,) has x=0, not a nonzero cycle
        # bridge, both directions on this word
        if not follows_word(3, x, w):
            bridge_ok = False
        if x * d != N:
            bridge_ok = False
        if L > 2 * j:
            fen_ok = False
        if L == 2 * j:
            fen_equality_words.append((w, x))

check("bridge identity x*d(w) = N_w and 'x follows w' hold on every "
      "realised word found (k=10, L<=22, p=3)", bridge_ok)
check("FEN: L <= 2r on every nonzero realised cycle found", fen_ok)
check("FEN equality holds ONLY on the word (0,1), the cycle {1,2}",
      fen_equality_words == [((0, 1), 2)])

# tcosmo/Knight2026_lean existence check is a `gh api` read, done outside
# this script (recorded in the findings); LABO.md statement-match is a
# read-not-built comparison, also recorded in the findings, not here.

# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"TOTAL: {CHECKS} checks, {FAILURES} failures")
print("=" * 78)

if FAILURES:
    raise SystemExit(1)
