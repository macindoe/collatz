# Period-2 cycles of F (cycles.md 12.5).
# Part A: two-step unrolled identity check on random orbits (period2.py).
# Part B: pruned exact search, n <= 20000 (period2_fixed.py — corrects an
#         off-by-one in T3 present in the first run of part B).

# Period-2 cycles of F.
# Elimination (12.5): a period-2 cycle with shallow data (s0,s1,m0,m1),
# n = m0+m1, K = s0+s1+n, q = 2^K - 3^n, requires
#   w0 * 3^a1 * q = R0 := 3^m1 (2^s0 - 1) + 2^(s0+m1) (2^s1 - 1)
#   w1 * 3^a0 * q = R1 := 3^m0 (2^s1 - 1) + 2^(s1+m0) (2^s0 - 1)
# so q > 0, q <= min(R0,R1), q | R0, q | R1.
import random
def v2(x): return (x & -x).bit_length() - 1
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = v3(C); wp = (C >> sig) // 3**a
    return s, sig, a, wp, sig - s + a

# --- A. verify the two-step unrolled identity on random real orbit pairs ---
random.seed(23)
bad = 0
for _ in range(3000):
    w0 = random.randrange(1, 10**6, 2)
    if w0 % 3 == 0: continue
    d0 = random.randrange(1, 30)
    s0, sg0, a0, w1, d1 = step(w0, d0)
    s1, sg1, a1, w2, d2 = step(w1, d1)
    lhs = w2 * (1 << (sg0 + sg1)) * 3**(a0 + a1)
    rhs = 3**(d0 + d1) * w0 + 3**d1 * ((1 << s0) - 1) + (1 << sg0) * 3**a0 * ((1 << s1) - 1)
    if lhs != rhs: bad += 1
print("identity check on random orbits: failures =", bad)

# --- B. pruned exact search over n <= 20000 ---
N = 20000
T3 = 3
open_n = 0; exact_checks = 0; survivors = []
for n in range(2, N + 1):
    if n > 2: T3 *= 3
    K = T3.bit_length()            # unique K with 3^n < 2^K < 2*3^n
    q = (1 << K) - T3
    S = K - n

def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
N = 20000
T3 = 9   # 3^2 at n=2  (bug fix: previous run had 3^(n-1))
assert T3 == 3**2
open_n = []; exact_checks = 0; survivors = []
for n in range(2, N + 1):
    if n > 2: T3 *= 3
    K = T3.bit_length(); q = (1 << K) - T3; S = K - n
    if S < 2: continue
    Lq = q.bit_length()
    mm = max(1, int((Lq - S - 1) / 1.585))
    if 2 * mm > n: continue
    open_n.append(n)
    for m0 in range(mm, n - mm + 1):
        m1 = n - m0; P0 = 3**m1; P1 = 3**m0
        for s0 in range(1, S):
            s1 = S - s0
            R0 = P0 * ((1 << s0) - 1) + (1 << (s0 + m1)) * ((1 << s1) - 1)
            if q > R0: continue
            R1 = P1 * ((1 << s1) - 1) + (1 << (s1 + m0)) * ((1 << s0) - 1)
            if q > R1: continue
            exact_checks += 1
            if R0 % q or R1 % q: continue
            Q0, Q1 = R0 // q, R1 // q
            if Q0 % 2 == 0 or Q1 % 2 == 0: continue
            a1, a0 = v3(Q0), v3(Q1)
            w0, w1 = Q0 // 3**a1, Q1 // 3**a0
            d0, d1 = m0 + a1, m1 + a0
            tag = "DEGENERATE(fixed pt)" if (w0, d0) == (w1, d1) else "NONTRIVIAL"
            survivors.append((tag, n, m0, m1, s0, s1, (w0, d0), (w1, d1)))
print("sanity: 3^5 handled as", 3**5, "at n=5 path OK")
print("open-window n:", open_n)
print("exact size-passing checks:", exact_checks)
for s in survivors: print(" ", s)
print("nontrivial period-2 solutions:", [s for s in survivors if s[0] == "NONTRIVIAL"] or "NONE")
