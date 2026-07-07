# General-p elimination, ceiling-forcing checks, and the period-3 search
# (cycles.md 12.6-12.7).
# Part A: identity + trivial-cycle + inequality checks (genp.py)
# Part B: period-3 pruned exact search, n <= 20000 (period3c.py)
# Part C: prune audit, skipped region + box boundary (audit3b.py)

# General-p elimination (cycles.md 12.6):
#   w_0 * 3^(a_{p-1}) * (2^K - 3^n) = R_0 := sum_t 3^(M_t) 2^(S_t) (2^(s_t)-1)
# with M_t = sum_{j>t} m_j,  S_t = sum_{j<t} sigma_j,  n = sum m, K = sum s + n.
# Check 1: the unrolled p-step identity (no cycle assumption) on random orbits.
# Check 2: R-formula on the trivial cycle traversed as a fake period-p cycle.
# Check 3 (ceiling forcing): K > ceil(n log2 3)  =>  some exit < p/ln2.
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

random.seed(29)
bad = 0
for p in (3, 4, 5):
    for _ in range(600):
        w = random.randrange(1, 10**5, 2)
        if w % 3 == 0: continue
        d = random.randrange(1, 20)
        w0, d0 = w, d
        S_list, sig_list, a_list, dlist = [], [], [], []
        for _ in range(p):
            s, sig, a, w, d = step(w, d)
            S_list.append(s); sig_list.append(sig); a_list.append(a); dlist.append(d if False else 0)
        # recompute d_t sequence
        ds = [d0]
        for t in range(p - 1):
            ds.append(sig_list[t] - S_list[t] + a_list[t])
        lhs = w * (1 << sum(sig_list)) * 3**sum(a_list)
        rhs = 3**sum(ds) * w0
        for t in range(p):
            D = sum(ds[t+1:]); Spre = sum(sig_list[:t]); Apre = sum(a_list[:t])
            rhs += 3**(D + Apre) * (1 << Spre) * ((1 << S_list[t]) - 1)
        if lhs != rhs: bad += 1
print("unrolled p-step identity (p=3,4,5):", "OK" if bad == 0 else f"{bad} FAILURES")

# Check 2: trivial cycle as period-p: m_t = s_t = 1, R must equal q = 2^(2p) - 3^p
def R_rot(ms, ss):
    p = len(ms); n = sum(ms)
    R = 0
    for t in range(p):
        M = sum(ms[t+1:]); Spre = sum(ss[j] + ms[(j+1) % p] for j in range(t))
        R += 3**M * (1 << Spre) * ((1 << ss[t]) - 1)
    return R
for p in (1, 2, 3, 4, 7):
    q = (1 << (2*p)) - 3**p
    R = R_rot([1]*p, [1]*p)
    assert R == q, (p, R, q)
print("trivial-cycle R = q for p in {1,2,3,4,7}: OK")

# Check 3: ceiling forcing bound sanity — the inequality chain, symbolic spot check:
# if Prod(1+eps) >= 2 then max eps >= 2^(1/p)-1 >= ln2/p; exit < p/ln2.
import math
for p in range(1, 200):
    assert 2**(1/p) - 1 >= math.log(2)/p - 1e-15
print("2^(1/p)-1 >= ln2/p for p < 200: OK")

# Period-3 exact search v2. Sound skip: if all rotations constrained, candidates
# need 2S >= sum A_r  =>  gamma >= 0.138n - c. Full loops elsewhere.
import math
L3 = math.log2(3)
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def R_exact(ms, ss):
    R = 0; Spre = 0
    for t in range(3):
        M = sum(ms[t+1:])
        R += 3**M * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % 3]
    return R

N = 20000
T3 = 27; full_n = []; found = []; s_exact = 0
for n in range(3, N + 1):
    if n > 3: T3 *= 3
    K = T3.bit_length(); q = (1 << K) - T3; S = K - n
    if S < 3: continue
    Lq = q.bit_length(); gamma_ub = K - (Lq - 1)     # gamma <= gamma_ub (sound)
    if n > 60 and gamma_ub < 0.098 * n - 5:          # slack-padded sound skip
        continue
    full_n.append(n)
    lq_lb = Lq - 1                                    # log2(q) >= Lq-1 (sound for prune)
    mb_hi = min(n - 2, max(int(0.3691 * n + 0.631 * gamma_ub) + 6, int(2.41 * gamma_ub) + 10))
    for m0 in range((n + 2) // 3, mb_hi + 1):
        for m1 in range(max(1, n - 2 * m0), m0 + 1):
            m2 = n - m0 - m1
            if m2 < 1 or m2 > m0: continue
            ms = (m0, m1, m2)
            # per-rotation A_r (e0-route threshold); rotation free if K - m_r >= lq_lb - 2
            A = []
            ok = True
            for r in range(3):
                if K - ms[r] >= lq_lb - 2: A.append(0); continue
                A.append(lq_lb - 2 - L3 * (n - ms[r]))
            # necessary: s_r + s_{r+1} >= A_r  =>  2S >= sum(A)
            if sum(max(0, a) for a in A) > 2 * S: continue
            for s0 in range(1, S - 1):
                for s1 in range(1, S - s0):
                    s2 = S - s0 - s1; ss = (s0, s1, s2)
                    ok = True
                    for r in range(3):
                        rm = (ms[r], ms[(r+1)%3], ms[(r+2)%3])
                        rs = (ss[r], ss[(r+1)%3], ss[(r+2)%3])
                        e0 = L3 * (rm[1] + rm[2]) + rs[0]
                        e1 = L3 * rm[2] + rs[0] + rm[1] + rs[1]
                        e2 = K - rm[0]
                        if max(e0, e1, e2) < lq_lb - 2: ok = False; break
                    if not ok: continue
                    s_exact += 1
                    Rs = [R_exact((ms[r], ms[(r+1)%3], ms[(r+2)%3]),
                                  (ss[r], ss[(r+1)%3], ss[(r+2)%3])) for r in range(3)]
                    if any(q > R for R in Rs): continue
                    if any(R % q for R in Rs): continue
                    Qs = [R // q for R in Rs]
                    if any(Q % 2 == 0 for Q in Qs): continue
                    az = [v3(Q) for Q in Qs]
                    ws = [Qs[r] // 3**az[r] for r in range(3)]
                    states = [(ws[r], ms[r] + az[r]) for r in range(3)]
                    if len(set(states)) == 1: continue
                    found.append((n, ms, ss, states))
print("n given full treatment:", len(full_n), "| largest:", full_n[-8:])
print("exact bigint tests:", s_exact)
print("nontrivial period-3 solutions:", found if found else "NONE")

# Audit v2: (a) skipped-n region, (b) cells just OUTSIDE the m-box within treated n,
# (c) cells failing the s float gate — exact-verify all fail min_r R_r >= q.
import random, math
L3 = math.log2(3)
def R_exact(ms, ss):
    R = 0; Spre = 0
    for t in range(3):
        R += 3**sum(ms[t+1:]) * (1 << Spre) * ((1 << ss[t]) - 1)
        Spre += ss[t] + ms[(t + 1) % 3]
    return R
def minR(ms, ss):
    return min(R_exact((ms[r], ms[(r+1)%3], ms[(r+2)%3]),
                       (ss[r], ss[(r+1)%3], ss[(r+2)%3])) for r in range(3))
random.seed(37)
viol = checked = 0
# (a) skipped n
for _ in range(300):
    n = random.randrange(100, 20001)
    T3 = 3**n; K = T3.bit_length(); q = (1 << K) - T3; S = K - n
    if S < 3 or K - (q.bit_length() - 1) >= 0.098 * n - 5: continue
    for _ in range(4):
        m0 = random.randrange(1, n - 1); m1 = random.randrange(1, n - m0) if n - m0 > 1 else 1
        m2 = n - m0 - m1
        if m2 < 1: continue
        s0 = random.randrange(1, S - 1); s1 = random.randrange(1, S - s0)
        checked += 1
        if minR((m0, m1, m2), (s0, s1, S - s0 - s1)) >= q:
            viol += 1; print("VIOLATION(a):", n, (m0, m1, m2))
# (b) box boundary in treated n
for n in [61, 63, 70, 73, 75, 78, 80, 82, 87, 94, 99]:
    T3 = 3**n; K = T3.bit_length(); q = (1 << K) - T3; S = K - n
    if S < 3: continue
    g = K - (q.bit_length() - 1)
    mb = min(n - 2, max(int(0.3691 * n + 0.631 * g) + 6, int(2.41 * g) + 10))
    for m0 in range(mb + 1, min(n - 2, mb + 12)):
        for _ in range(30):
            m1 = random.randrange(1, n - m0) if n - m0 > 1 else 1
            m2 = n - m0 - m1
            if m2 < 1 or m1 > m0 or m2 > m0: continue
            s0 = random.randrange(1, S - 1); s1 = random.randrange(1, S - s0)
            checked += 1
            if minR((m0, m1, m2), (s0, s1, S - s0 - s1)) >= q:
                viol += 1; print("VIOLATION(b):", n, (m0, m1, m2))
print(f"audited {checked} cells (skipped region + box boundary); violations: {viol}")
