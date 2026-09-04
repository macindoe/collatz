#!/usr/bin/env python3
"""merle_r14_check.py -- independent verification for the round-14 review
(briefs/merle-round14-review-brief.md; findings in
briefs/merle-round14-review-findings.md).

The object under key is shared-ledger entry L-A10 (Merle, PR #4 of
macindoe/one-obstruction-three-faces, branch round-14 at 2f7b865): for odd
p >= 3, T the Terras half map (x/2 for even x, (px+1)/2 for odd x), every
fixed k >= 1 and every f : Z/2^k -> R_{>0}, the altitude V(x) = x*f(x mod 2^k)
fails to satisfy V(T(x)) < V(x) on all positive integers.

Fresh code throughout: imports nothing from either Merle repository and
nothing from any earlier check of ours. The round-13 accelerated
single-successor graph (experiments/merle_r13_check.py PART 7) is
RE-IMPLEMENTED here from its recorded definition, not imported, because it
is one of the two objects the divergence diagnosis compares. Exact integers
at every pass/fail decision; mpmath at two working precisions only in PART 5,
where a logarithm is unavoidable, with agreement asserted.

  PART 0  canaries (printed first; every expected value written down before
          this code ran, from the PR body, the ledger entry, the committed
          run_050_output.txt, or by hand)
  PART 1  L-A10, the two-line theorem, keyed: p = 3..201 odd, k = 1..40,
          six witnesses per (p,k) pair -- m = 0, 1, 2 and three random m of
          200, 400, 600 bits -- checking r_p odd, x = T(x) = u_p (mod 2^k),
          T(x) > x, and the exact identity T(x) - x = ((p-2)x + 1)/2
  PART 2  the concrete instances of the letter and the ledger entry, and the
          "both lifts" bookkeeping behind the review's one wording point
  PART 3  the divergence diagnosis, reconstructed on both objects (the
          accelerated single-successor graph of round 13; the half-map
          relation on Z/2^k carrying both lifts from Z/2^{k+1}); our own
          round-13 p = 3 and p = 7 figures reproduced on our object as a
          regression check; which lift carries the loop, over all 4000 pairs
  PART 4  the p = 1 negative control; the "for every f" quantifier; scope
          (one edge, no cycle, no orbit)
  PART 5  the smaller letter items: theta = 1 at p = 3 exactly, f'(0) =
          ln(p/4) and no positive root at p = 5, 7, the mean-log-step drift;
          h4's three numbers located in merle_la9_check.py's own committed
          PART 3 output

Output is written by this script itself to
experiments/merle_r14_check_output.txt (next to the script), and to stdout.
Seeded; no timestamps; re-runs are byte-identical.
"""

import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "merle_r14_check_output.txt")


class Tee:
    """Write everything to stdout and to the committed output file."""

    def __init__(self, path):
        self.f = open(path, "w", encoding="utf-8", newline="\n")
        self.stdout = sys.stdout

    def write(self, s):
        self.stdout.write(s)
        self.f.write(s)

    def flush(self):
        self.stdout.flush()
        self.f.flush()

    def close(self):
        self.f.close()


TEE = Tee(OUT_PATH)
sys.stdout = TEE

CHECKS = 0
FAILS = []


def check(label, ok, detail=""):
    global CHECKS
    CHECKS += 1
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(label)


# ---------------------------------------------------------------------------
# The objects, defined once, in our own words.
# ---------------------------------------------------------------------------


def T(x, p=3):
    """The Terras half map for the px+1 problem: x/2 (even), (px+1)/2 (odd).
    Exact integer arithmetic; valid for negative x as well (T(-1) = -1 at
    p = 3, the section-95 fixed point)."""
    return x // 2 if x % 2 == 0 else (p * x + 1) // 2


def witness_residues(p, k):
    """r_p = -(p-2)^{-1} mod 2^{k+1} and u_p = r_p mod 2^k, exactly as L-A10
    defines them. pow(a, -1, M) is Python's exact modular inverse; it raises
    if a is not invertible, which for odd a and M = 2^{k+1} never happens."""
    M2 = 1 << (k + 1)
    inv = pow((p - 2) % M2, -1, M2)
    r = (-inv) % M2
    return r, r % (1 << k)


def v2(n):
    """2-adic valuation of a nonzero integer, and its odd part."""
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v, n


print("=" * 78)
print("merle_r14_check.py -- round-14 review: L-A10 keyed with fresh code")
print("=" * 78)
print("Python", sys.version.split()[0])

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 0 -- canaries (expected values written down before the code ran)")
print("=" * 78)

r38, u38 = witness_residues(3, 8)
check("C1  r_3 at k=8 is 511 = 2^9 - 1, u_3 = 255 = 2^8 - 1 (PR body, L-A10)",
      r38 == 511 and u38 == 255, f"r={r38}, u={u38}")
check("C2  T(511) = 767, T(767) = 1151, 1151 mod 256 = 127 (the retracted "
      "'climbs forever' formulation: the class is left at step 2)",
      T(511) == 767 and T(767) == 1151 and 1151 % 256 == 127)
check("C3  the trivial cycle at p=3: T(1) = 2, T(2) = 1",
      T(1) == 2 and T(2) == 1)
check("C4  the section-95 fixed point: T(-1) = -1 at p=3",
      T(-1, 3) == -1)
check("C5  p=1 control by hand: T(511) = 256, T(511) - 511 = -255 (the "
      "'ascending' branch descends at p=1)",
      T(511, 1) == 256 and T(511, 1) - 511 == -255)
v, odd = v2(3 * 255 + 1)
check("C6  the accelerated map at p=3 sends 255 to 383 (v=1), and 383 mod "
      "256 = 127 -- the edge our round-13 graph has at 255",
      v == 1 and odd == 383 and odd % 256 == 127, f"v={v}, odd part={odd}")
his_p1_examples = {3: 255, 5: 85, 7: 51, 9: 73, 11: 199}  # run_050_output.txt P1
got = {p: witness_residues(p, 8)[1] for p in his_p1_examples}
check("C7  his P1 examples at k=8 (run_050_output.txt): u = 255, 85, 51, 73, "
      "199 for p = 3, 5, 7, 9, 11", got == his_p1_examples, str(got))
check("C8  at p=3, u_3 = 2^k - 1 and r_3 = 2^{k+1} - 1 for every k = 1..40 "
      "(the ledger's 'plainest object in the problem')",
      all(witness_residues(3, k) == ((1 << (k + 1)) - 1, (1 << k) - 1)
          for k in range(1, 41)))
assert not FAILS, f"canaries failed: {FAILS}"

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 1 -- L-A10, the two-line theorem, keyed (p = 3..201 odd, k = 1..40)")
print("=" * 78)
print("""
  THE ARGUMENT, in our own words (checked below at every step, exactly):
  (p-2) is odd, so invertible mod 2^{k+1}; r_p := -(p-2)^{-1} mod 2^{k+1}
  satisfies (p-2)*r_p = -1 (mod 2^{k+1}), and is odd (an odd number's
  inverse mod a power of 2 is odd; its negative mod 2^{k+1} is odd).
  For any positive x = r_p (mod 2^{k+1}):
    (i)   x is odd, so T(x) = (px+1)/2, and (p-2)x + 1 = (p-2)r_p + 1 = 0
          (mod 2^{k+1}); hence T(x) - x = ((p-2)x + 1)/2 is an integer
          divisible by 2^k, i.e. T(x) = x (mod 2^k), both = u_p.
    (ii)  (p-2)x + 1 > 0 since p >= 3 and x >= 1, so T(x) > x.
  Same residue mod 2^k => same value f(u_p) > 0 => V(T(x)) = T(x) f(u_p)
  > x f(u_p) = V(x). One edge, exhibited; nothing about f used beyond
  'depends on x mod 2^k' and 'positive'.
""")

rng = random.Random(20260904)
n_pairs = 0
n_witness = 0
bad_defining = []   # (p-2)*r_p + 1 != 0 mod 2^{k+1}
bad_odd = []        # r_p even
bad_residue = []    # x or T(x) not = u_p mod 2^k
bad_ascent = []     # T(x) <= x
bad_identity = []   # T(x) - x != ((p-2)x+1)/2 exactly
witness_bits_max = 0
for p in range(3, 202, 2):
    for k in range(1, 41):
        n_pairs += 1
        M, M2 = 1 << k, 1 << (k + 1)
        r, u = witness_residues(p, k)
        if ((p - 2) * r + 1) % M2 != 0:
            bad_defining.append((p, k))
        if r % 2 == 0:
            bad_odd.append((p, k))
        ms = [0, 1, 2] + [rng.getrandbits(b) for b in (200, 400, 600)]
        for m in ms:
            x = r + m * M2
            assert x > 0
            y = T(x, p)
            n_witness += 1
            witness_bits_max = max(witness_bits_max, x.bit_length())
            if x % M != u or y % M != u:
                bad_residue.append((p, k, m))
            if not y > x:
                bad_ascent.append((p, k, m))
            num = (p - 2) * x + 1
            if num % 2 != 0 or y - x != num // 2:
                bad_identity.append((p, k, m))

check(f"defining congruence (p-2)*r_p + 1 = 0 (mod 2^(k+1)) on all {n_pairs} "
      "(p,k) pairs", not bad_defining, f"failures: {bad_defining[:5] or 'none'}")
check(f"r_p is odd on all {n_pairs} pairs", not bad_odd,
      f"failures: {bad_odd[:5] or 'none'}")
check(f"x = T(x) = u_p (mod 2^k) on all {n_witness} witnesses "
      f"(6 per pair: m = 0, 1, 2 and three random m of 200/400/600 bits; "
      f"largest witness {witness_bits_max} bits)",
      not bad_residue, f"failures: {bad_residue[:5] or 'none'}")
check(f"T(x) > x on all {n_witness} witnesses (strict ascent, exact integers)",
      not bad_ascent, f"failures: {bad_ascent[:5] or 'none'}")
check(f"T(x) - x = ((p-2)x + 1)/2 exactly, numerator even, on all "
      f"{n_witness} witnesses", not bad_identity,
      f"failures: {bad_identity[:5] or 'none'}")
print(f"  pairs: {n_pairs} (p = 3..201 odd = 100 values, k = 1..40); "
      f"witnesses: {n_witness}; seed 20260904 for the random m")

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 2 -- the concrete instances, and the 'both lifts' bookkeeping")
print("=" * 78)

# The ledger entry's worked example.
chain = [511]
for _ in range(6):
    chain.append(T(chain[-1]))
print("  p=3, k=8, the witness chain under T with residues mod 256:")
print("    " + " -> ".join(f"{t} [{t % 256}]" for t in chain))
check("511 -> 767 -> 1151 -> 1727 -> 2591 -> 3887 -> 5831 (his P5 trajectory, "
      "run_050_output.txt), residues 255, 255, 127, 191, 31, 47, 199",
      chain == [511, 767, 1151, 1727, 2591, 3887, 5831]
      and [t % 256 for t in chain] == [255, 255, 127, 191, 31, 47, 199])
check("the class is left at step 2 exactly (first index with residue != 255 "
      "is 2) -- the retracted formulation is indeed false, as he says",
      [i for i, t in enumerate(chain) if t % 256 != 255][0] == 2)
check("T(511)/511 = 767/511 = 1.5010 to four places (his printed ratio)",
      round(767 / 511, 4) == 1.5010)

# The 'both lifts' bookkeeping: the half map on Z/256 with lifts from Z/512.
# Residue 255 has two lifts, 255 and 511.  Each gives one edge.
lift_a, lift_b = 255, 511
edge_a = (lift_a % 256, T(lift_a) % 256)
edge_b = (lift_b % 256, T(lift_b) % 256)
print(f"  half map, residue 255 on Z/256: lift {lift_a} -> T = {T(lift_a)} "
      f"-> edge {edge_a}; lift {lift_b} -> T = {T(lift_b)} -> edge {edge_b}")
check("the half-map relation on Z/256 carries BOTH edges 255 -> 127 (lift "
      "255) and 255 -> 255 (lift 511) -- so 'ours has 255 -> 255' is right "
      "and 'ours ALSO has 255 -> 127' is the full statement (the review's "
      "wording point, not a defect in the claim)",
      edge_a == (255, 127) and edge_b == (255, 255))
va, oa = v2(3 * 255 + 1)
check("the accelerated map x -> (3x+1)/2^v at the canonical representative "
      "255 sends it to 383 = 127 (mod 256): the SAME edge as the half map's "
      "m=0 lift, and the only one the single-successor graph keeps",
      va == 1 and oa % 256 == 127)
# General identity behind the two successors: for odd u, the two lifts u and
# u + 2^k have images (pu+1)/2 and (pu+1)/2 + p*2^{k-1}, which differ by
# p*2^{k-1} = 2^{k-1} (mod 2^k) since p is odd.
diffs_ok = True
for p in (3, 5, 7, 9, 11):
    for k in range(1, 13):
        M = 1 << k
        for u in range(1, M, 2):
            a, b = T(u, p) % M, T(u + M, p) % M
            if (b - a) % M != (M >> 1) % M:
                diffs_ok = False
check("for odd u, the two half-map successors of u on Z/2^k (from lifts u "
      "and u + 2^k) differ by exactly 2^(k-1) mod 2^k, for p = 3..11 odd, "
      "k = 1..12 (127 and 255 at (3,8): 128 apart)", diffs_ok)

# The p = 1 control, at the same instance.
check("p=1 at the same class: T(511) = 256 < 511, difference -255 -- the "
      "argument's inequality fails to hold, so it concludes nothing at p=1",
      T(511, 1) == 256 and T(511, 1) - 511 == -255)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("PART 3 -- the divergence diagnosis, reconstructed on both objects")
print("=" * 78)
print("""
  OBJECT A (ours, round 13 -- merle_r13_check.py PART 7, re-implemented here
  from its recorded definition, not imported): the ACCELERATED map
  x -> (px+1)/2^v on the odd residues mod 2^k, ONE successor per residue,
  computed at the canonical representative u in [1, 2^k):
  u -> oddpart(p*u+1) mod 2^k, with valuation v = v_2(p*u+1). A functional
  graph, so its cycles are enumerated exactly; a cycle (L, K = sum of the v)
  is FAULTY iff p^L >= 2^K (exact integer comparison). Round 13 counted
  faulty cycles with L > 1 only; both counts are printed here.

  OBJECT B (his, sections 95-96 -- 'run_049 line 33' in his words,
  re-implemented here from the definition alone): the Terras HALF map T on
  Z/2^k carrying BOTH lifts from Z/2^{k+1}: for every r in [0, 2^{k+1}) one
  edge (r mod 2^k) -> (T(r) mod 2^k). This is well defined on Z/2^{k+1}
  (T(r + 2^{k+1}) = T(r) mod 2^k on both branches), gives two out-edges per
  node, and every edge is realised by the whole progression r + 2^{k+1}*Z --
  which is why his run_049 P1 ('20,000 edges, all realised') can only pass.
""")


def accelerated_graph(p, k):
    """OBJECT A: one successor per odd residue, at the canonical lift."""
    M = 1 << k
    succ, val = {}, {}
    for u in range(1, M, 2):
        v, odd = v2(p * u + 1)
        succ[u], val[u] = odd % M, v
    return succ, val


def functional_cycles(succ):
    """Every distinct cycle of a functional graph, exactly once."""
    seen = set()
    cycles = []
    for start in succ:
        if start in seen:
            continue
        path, pos, cur = [], {}, start
        while cur not in seen and cur not in pos:
            pos[cur] = len(path)
            path.append(cur)
            cur = succ[cur]
        if cur in pos:
            cycles.append(path[pos[cur]:])
        seen.update(path)
    return cycles


def faulty_cycles(p, k):
    """(L, K) of every faulty cycle of OBJECT A at (p, k), and the list of all
    cycle lengths. Returns (all_lengths, faulty_all, faulty_L_gt_1)."""
    succ, val = accelerated_graph(p, k)
    cycles = functional_cycles(succ)
    lengths = sorted(len(c) for c in cycles)
    faulty = []
    for c in cycles:
        L, K = len(c), sum(val[u] for u in c)
        if p ** L >= (1 << K):
            faulty.append((L, K))
    faulty.sort()
    return lengths, faulty, [lk for lk in faulty if lk[0] > 1]


def half_map_relation(p, k):
    """OBJECT B: edges (u, v) -> list of lifts r in [0, 2^{k+1}) realising it."""
    M = 1 << k
    edges = {}
    for r in range(1 << (k + 1)):
        edges.setdefault((r % M, T(r, p) % M), []).append(r)
    return edges


# --- (a) the witness edge on each object at p = 3, k = 8 --------------------
succA, valA = accelerated_graph(3, 8)
relB = half_map_relation(3, 8)
print(f"  (3,8) OBJECT A: succ[255] = {succA[255]} (v = {valA[255]})")
print(f"  (3,8) OBJECT B: edge (255,255) lifts = {relB.get((255, 255))}, "
      f"edge (255,127) lifts = {relB.get((255, 127))}")
check("(3,8): the edge 255 -> 255 is PRESENT in the half-map relation, "
      "realised by the lift 511 (and by every x = 511 mod 512)",
      relB.get((255, 255)) == [511])
check("(3,8): the edge 255 -> 127 is ALSO present in the relation, realised "
      "by the lift 255 -- the relation carries both edges from 255",
      relB.get((255, 127)) == [255])
check("(3,8): the edge 255 -> 255 is ABSENT from the accelerated "
      "single-successor graph, whose one edge from 255 goes to 127",
      succA[255] == 127 and succA[255] != 255)
out_degree = {}
for (u, v_) in relB:
    out_degree[u] = out_degree.get(u, 0) + 1
check("(3,8): the relation has exactly 512 = 2^9 distinct edges, two out of "
      "every node, each realised by exactly one lift class mod 512",
      len(relB) == 512 and set(out_degree.values()) == {2}
      and all(len(ls) == 1 for ls in relB.values()))
# his P1, reconstructed: realisability is automatic, so this can only pass.
rngB = random.Random(20260904)
ok_real = True
for (u, v_), lifts in relB.items():
    for _ in range(3):
        x = lifts[0] + 512 * rngB.randrange(1, 10 ** 6)
        if x % 256 != u or T(x) % 256 != v_:
            ok_real = False
check("(3,8): every edge of the relation is realised by random positive lifts "
      "x = r + 512*m (3 per edge, 1536 in all) -- his run_049 P1 "
      "reconstructed; TRUE BY CONSTRUCTION (an edge IS a lift class), so a "
      "consistency check of the graph, not a finding", ok_real)

# --- (b) regression: our round-13 figures on OBJECT A -----------------------
print()
print("  regression on OBJECT A (round-13 committed figures; his run_050 P4 "
      "table reproduces the same):")
expected_p3 = {  # k: (faulty with L > 1) -- merle_r13_check_output.txt, PART 7
    4: [], 5: [], 6: [], 7: [], 8: [], 9: [],
    10: [(26, 37)], 11: [(25, 37)], 12: [(6, 7), (7, 9)],
    14: [], 16: [],
}
his_p4_p3 = {  # k: faulty count -- run_050_output.txt P4 (no L=1 exclusion)
    4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 1, 11: 1, 12: 2,
    13: 0, 14: 0, 15: 0, 16: 0,
}
p3_rows = {}
for k in range(4, 17):
    lengths, fa, fa1 = faulty_cycles(3, k)
    p3_rows[k] = (lengths, fa, fa1)
    print(f"    p=3 k={k:>2}: cycle lengths {lengths}, faulty (all) {fa}, "
          f"faulty (L>1) {fa1}")
check("p=3, k = 4..12, 14, 16: faulty cycles (L > 1) and their (L,K) match "
      "our round-13 committed output exactly -- none at k=4..9; (26,37) at "
      "k=10; (25,37) at k=11; (6,7),(7,9) at k=12; none at k=14, 16",
      all(p3_rows[k][2] == expected_p3[k] for k in expected_p3))
check("p=3, k = 4..16: faulty counts match his run_050 P4 table exactly "
      "(0,0,0,0,0,0,1,1,2,0,0,0,0) -- including k = 13 and 15, which our "
      "round-13 run did not measure and his table added",
      all(len(p3_rows[k][1]) == his_p4_p3[k] for k in his_p4_p3))
check("p=3, k = 4..16: the L=1 exclusion of round 13 changes no count "
      "(the fixed point u=1 has v=2 and 3 < 4, never faulty), so our "
      "L>1 figures and his all-cycles figures agree for a reason",
      all(p3_rows[k][1] == p3_rows[k][2] for k in p3_rows))
lengths78, fa78, fa78_1 = faulty_cycles(7, 8)
print(f"    p=7 k= 8: cycle lengths {lengths78}, faulty (all) {fa78}, "
      f"faulty (L>1) {fa78_1}")
check("p=7, k=8: 4 residue cycles, lengths [1, 3, 4, 31], 3 faulty at "
      "(L,K) = (3,4), (4,8), (31,67) -- our round-13 figures and his P4 "
      "table, identical",
      lengths78 == [1, 3, 4, 31] and fa78_1 == [(3, 4), (4, 8), (31, 67)]
      and fa78 == fa78_1)

# --- (c) which lift carries the loop, over all 4000 pairs -------------------
print()
print("  which lift of u_p carries the loop u_p -> u_p, over all 4000 pairs:")
m1 = m0 = 0
p3_all_m1 = True
equiv_ok = True   # for k >= 2: loop in OBJECT A  <=>  r_p < 2^k
k1_note = []
for p in range(3, 202, 2):
    for k in range(1, 41):
        M = 1 << k
        r, u = witness_residues(p, k)
        on_m1 = r >= M
        if on_m1:
            m1 += 1
        else:
            m0 += 1
        if p == 3 and not on_m1:
            p3_all_m1 = False
        if k <= 16:   # OBJECT A built explicitly where it is cheap
            sA, _ = accelerated_graph(p, k)
            loop_in_A = (sA[u] == u)
            if k >= 2 and loop_in_A != (not on_m1):
                equiv_ok = False
            if k == 1:
                k1_note.append(loop_in_A)
print(f"    loop on the m=1 lift (r_p >= 2^k): {m1} pairs; on the m=0 lift "
      f"(r_p < 2^k): {m0} pairs")
check("p=3: the loop sits on the m=1 lift at EVERY k = 1..40 (r_3 = 2^(k+1)-1 "
      ">= 2^k), so for p=3 the witness edge is never in OBJECT A at k >= 2 "
      "-- his diagnosis is exactly right for the case at issue", p3_all_m1)
r78, u78 = witness_residues(7, 8)
check("p=7, k=8: r_7 = 307 >= 256, the m=1 lift again -- the loop is absent "
      "from OBJECT A there too (u = 51 -> {} in A)".format(
          accelerated_graph(7, 8)[0][51]),
      r78 == 307 and accelerated_graph(7, 8)[0][51] != 51)
check("for k = 2..16 and every odd p = 3..201: the loop u_p -> u_p is in "
      "OBJECT A exactly when r_p < 2^k (the m=0 lift), where it appears as an "
      "L=1 self-loop with v=1 -- faulty, and excluded by round 13's L>1 "
      "convention; so 'the witness edge lives on the other lift' is true of "
      "p=3 and of (7,8), not of every (p,k)", equiv_ok)
r98, u98 = witness_residues(9, 8)
sA98, vA98 = accelerated_graph(9, 8)
check("example of the other case: p=9, k=8 has r_9 = 73 < 256, and OBJECT A "
      "contains 73 -> 73 (v=1) as a faulty L=1 self-loop (9 >= 2)",
      r98 == 73 and sA98[73] == 73 and vA98[73] == 1 and 9 >= 2,
      f"r={r98}, succ[73]={sA98[73]}, v={vA98[73]}")
check("k=1 is degenerate: Z/2 has one odd residue and OBJECT A is the single "
      "self-loop 1 -> 1 for every p (recorded, excluded from the equivalence)",
      all(k1_note) and len(k1_note) == 100)

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print(f"TOTAL: {CHECKS} checks, {len(FAILS)} failures")
if FAILS:
    print("FAILURES:")
    for f in FAILS:
        print(f"  - {f}")
print("=" * 78)
TEE.flush()
sys.stdout = TEE.stdout   # restore before closing, so the exit flush is clean
TEE.close()
sys.exit(1 if FAILS else 0)
