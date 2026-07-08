# AEH calibration experiments (aeh.md, section 13). Parts E1-E8:
# E1/E2 uniform-vs-orbit stats; E3/E5 window chains; E4 digit-sharing;
# E4b/E6 digit-uniformity tests; E7 bulk/bottom split; E8 anomaly recheck.

# ==== aeh.py ====
# AEH calibration (aeh.md 13.x):
# (E1) uniform random states -> exact one-step and two-step decision statistics
# (E2) real orbits -> same statistics along trajectories
# Compare: E1 vs independence-product (exact correlations = theorem targets),
#          E2 vs E1 (orbit measure vs product measure = AEH content).
import random
from collections import Counter
def v2(x): return (x & -x).bit_length() - 1
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = v3(C); wp = (C >> sig) // 3**a
    return s, wp, sig - s + a

random.seed(47)
def cls(w, d): return (w % 8, d % 2)

# E1: uniform states
N1 = 200000
m1_s = Counter(); pair_s = Counter(); ctrans = Counter(); m1_c = Counter()
for _ in range(N1):
    w = random.getrandbits(44) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 60)
    s0, w1, d1 = step(w, d)
    s1, w2, d2 = step(w1, d1)
    k0 = min(s0, 7); k1 = min(s1, 7)
    m1_s[k0] += 1; pair_s[(k0, k1)] += 1
    m1_c[cls(w, d)] += 1; ctrans[(cls(w, d), cls(w1, d1))] += 1
T1 = sum(m1_s.values())
print("E1 marginal P(s=k) vs 2^-k:")
for k in range(1, 8):
    print(f"  s={k}{'+' if k==7 else ' '}: {m1_s[k]/T1:.4f}  vs  {2**-k if k<7 else 2**-6:.4f}")
# independence test on s-pairs
print("E1 s-pair dependence (ratio P(j,k)/(P(j)P(k)), flag if |ratio-1|>0.05):")
flags = []
for (j, k), c in sorted(pair_s.items()):
    r = c / T1 / (m1_s[j]/T1 * m1_s[k]/T1)
    if abs(r - 1) > 0.05 and c > 200: flags.append((j, k, round(r, 3), c))
print("  flagged:", flags if flags else "none — s-sequence looks i.i.d. under uniform measure")
# class transition matrix: uniform rows?
print("E1 class-transition deviations from uniform next-class (flag |p-1/8|>0.02):")
cflags = []
tot_by_c = Counter()
for (c0, c1), c in ctrans.items(): tot_by_c[c0] += c
for (c0, c1), c in sorted(ctrans.items()):
    p = c / tot_by_c[c0]
    if abs(p - 0.125) > 0.02: cflags.append((c0, c1, round(p, 4)))
print("  flagged:", cflags[:12] if cflags else "none")
print()

# E2: real orbits
m2_s = Counter(); pair2_s = Counter(); T2 = 0
for _ in range(400):
    w = random.getrandbits(40) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 20)
    prev = None
    for _ in range(200):
        s, w2, d2 = step(w, d)
        k = min(s, 7); m2_s[k] += 1; T2 += 1
        if prev is not None: pair2_s[(prev, k)] += 1
        prev = k; w, d = w2, d2
        if (w, d) == (1, 1): break
print("E2 (orbits) marginal P(s=k) vs E1:")
for k in range(1, 8):
    print(f"  s={k}{'+' if k==7 else ' '}: {m2_s[k]/T2:.4f}  vs  {m1_s[k]/T1:.4f}")
print("E2 s-pair dependence (flag |ratio-1|>0.08):")
flags2 = []
for (j, k), c in sorted(pair2_s.items()):
    r = (c / sum(pair2_s.values())) / (m2_s[j]/T2 * m2_s[k]/T2)
    if abs(r - 1) > 0.08 and c > 150: flags2.append((j, k, round(r, 3), c))
print("  flagged:", flags2 if flags2 else "none")
# 3-gain rate and drift, orbits
gains = sum(c for (j,k),c in pair2_s.items() if j % 2 == 0)  # s even -> 3-gain (9.3)
print(f"3-gain rate along orbits: {gains/sum(pair2_s.values()):.4f} (ledger: 1/3 = 0.3333)")

# ==== aeh2.py ====
# Does the stationary law of the uniform-measure class chain predict the
# ORBIT statistics (including the s=3 excess and pair correlations)?
import random
from collections import Counter, defaultdict
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0
    u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
def cls(w, d): return (w % 8, d % 2)
random.seed(53)

# E1': estimate the joint kernel  class -> (s_trunc, class')  under uniform states
K = defaultdict(Counter); N1 = 400000
for _ in range(N1):
    w = random.getrandbits(48) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 64)
    s, w1, d1 = step(w, d)
    K[cls(w, d)][(min(s, 9), cls(w1, d1))] += 1
classes = sorted(K)
# stationary distribution of the class marginal chain (power iteration)
import itertools
pi = {c: 1/8 for c in classes}
for _ in range(500):
    nxt = {c: 0.0 for c in classes}
    for c in classes:
        tot = sum(K[c].values())
        for (s, c2), cnt in K[c].items():
            nxt[c2] += pi[c] * cnt / tot
    pi = nxt
# implied stationary s-marginal and consecutive-pair law
sm = Counter(); pair = Counter()
for c in classes:
    tot = sum(K[c].values())
    for (s, c2), cnt in K[c].items():
        sm[s] += pi[c] * cnt / tot
        tot2 = sum(K[c2].values())
        for (s2, c3), cnt2 in K[c2].items():
            pair[(s, s2)] += pi[c] * (cnt / tot) * (cnt2 / tot2)

# E2': clean orbit statistics (large starts, no absorption tail)
m2 = Counter(); pair2 = Counter(); T2 = 0
for _ in range(500):
    w = random.getrandbits(90) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 30)
    prev = None
    for _ in range(160):
        s, w1, d1 = step(w, d)
        k = min(s, 9); m2[k] += 1; T2 += 1
        if prev is not None: pair2[(prev, k)] += 1
        prev = k; w, d = w1, d1
        if w == 1 and d == 1: break

print("s-marginal: chain-stationary prediction vs ORBITS vs naive 2^-k:")
for k in range(1, 7):
    print(f"  s={k}: {sm[k]:.4f}   {m2[k]/T2:.4f}   {2**-k:.4f}")
print("\nconsecutive-pair ratios P(j,k)/(P(j)P(k)): chain prediction vs orbits (top deviations):")
rows = []
P2 = sum(pair2.values())
for (j, k) in sorted(set(pair) & set(pair2)):
    if j > 5 or k > 5: continue
    rc = pair[(j, k)] / (sm[j] * sm[k])
    ro = (pair2[(j, k)] / P2) / ((m2[j]/T2) * (m2[k]/T2))
    if abs(rc - 1) > 0.04 or abs(ro - 1) > 0.08:
        rows.append((j, k, round(rc, 3), round(ro, 3), pair2[(j, k)]))
for r in rows: print("  (s,s')=(%d,%d): chain %.3f  orbit %.3f  (n=%d)" % r)
print("\nstationary class law pi:", {c: round(pi[c], 4) for c in classes})

# ==== aeh3.py ====
# E3: chain on state (w mod 8, min(d,12)) with ONLY the omega-digits randomized
# (uniform 2-adically); d evolves dynamically. Stationary law -> predictions.
# This is candidate-AEH: "omega-digits equidistribute given the (class, d) state."
import random
from collections import Counter, defaultdict
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(59)
D = 12
def st(w, d): return (w % 8, min(d, D))

# kernel: for each state, sample omega uniform with that residue, d as given
K = defaultdict(Counter)
for w8 in (1, 3, 5, 7):
    for d in range(1, D + 1):
        for _ in range(30000):
            w = ((random.getrandbits(48) >> 3) << 3) | w8
            if w % 3 == 0: continue
            s, w1, d1 = step(w, d)
            K[(w8, d)][(min(s, 9), st(w1, d1))] += 1
states = sorted(K)
pi = {c: 1.0 / len(states) for c in states}
for _ in range(800):
    nxt = {c: 0.0 for c in states}
    for c in states:
        tot = sum(K[c].values())
        for (s, c2), cnt in K[c].items():
            nxt[c2] += pi[c] * cnt / tot
    pi = nxt
sm = Counter(); pair = Counter()
for c in states:
    tot = sum(K[c].values())
    for (s, c2), cnt in K[c].items():
        sm[s] += pi[c] * cnt / tot
        tot2 = sum(K[c2].values())
        for (s2, c3), cnt2 in K[c2].items():
            pair[(s, s2)] += pi[c] * (cnt / tot) * (cnt2 / tot2)

# orbits (same protocol as before)
m2 = Counter(); pair2 = Counter(); T2 = 0; dhist = Counter()
for _ in range(600):
    w = random.getrandbits(90) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 30)
    prev = None
    for _ in range(160):
        s, w1, d1 = step(w, d)
        k = min(s, 9); m2[k] += 1; T2 += 1; dhist[min(d, D)] += 1
        if prev is not None: pair2[(prev, k)] += 1
        prev = k; w, d = w1, d1
        if w == 1 and d == 1: break

print("s-marginal: (class,d)-chain prediction vs ORBITS:")
for k in range(1, 7): print(f"  s={k}: {sm[k]:.4f}   {m2[k]/T2:.4f}")
print("\npair ratios: chain vs orbit (all cells with orbit deviation > 8%):")
P2 = sum(pair2.values())
for (j, k) in sorted(set(pair) & set(pair2)):
    if j > 5 or k > 5: continue
    ro = (pair2[(j, k)] / P2) / ((m2[j]/T2) * (m2[k]/T2))
    rc = pair[(j, k)] / (sm[j] * sm[k])
    if abs(ro - 1) > 0.08:
        print(f"  ({j},{k}): chain {rc:.3f}   orbit {ro:.3f}   (n={pair2[(j,k)]})")
print("\nstationary d-law (chain) vs orbit d-histogram:")
dch = Counter()
for (w8, d), p in pi.items(): dch[d] += p
for d in range(1, 8): print(f"  d={d}: chain {dch[d]:.4f}   orbit {dhist[d]/T2:.4f}")

# ==== aeh4.py ====
# E4: two REAL steps from a once-randomized state (stationary (class,d) start,
#     omega-digits uniform) -> does digit-sharing reproduce the orbit pair law?
# E4b: along real orbits, are omega-digits uniform given (class, d)?
#     (test omega mod 32 within each mod-8 class at d = 1, 2)
import random
from collections import Counter
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(61)

# stationary-ish (w8, d) start law: sample by running short orbits (burn-in)
starts = []
for _ in range(4000):
    w = random.getrandbits(64) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 20)
    for _ in range(30):
        s, w, d = step(w, d)
    starts.append((w % 8, min(d, 12)))

# E4: two real steps, omega deep digits uniform, start (class,d) from the burn-in law
m4 = Counter(); pair4 = Counter()
for _ in range(300000):
    w8, d = random.choice(starts)
    w = ((random.getrandbits(64) >> 3) << 3) | w8
    if w % 3 == 0: continue
    s0, w1, d1 = step(w, d)
    s1, w2, d2 = step(w1, d1)
    a, b = min(s0, 9), min(s1, 9)
    m4[a] += 1; m4[b] += 0   # marginal from first coordinate
    pair4[(a, b)] += 1
T4 = sum(pair4.values())
# also need second-coordinate marginal
m4b = Counter()
for (a, b), c in pair4.items(): m4b[b] += c
print("E4 pair ratios (two real steps, digits shared) — compare with orbit values:")
targets = [(2,4,1.147), (3,3,0.845), (3,4,0.885), (4,3,1.280), (4,4,1.103)]
for j, k, orb in targets:
    r = (pair4[(j,k)]/T4) / ((m4[j]/T4) * (m4b[k]/T4))
    print(f"  ({j},{k}): E4 {r:.3f}   orbit {orb}")

# E4b: omega mod 32 uniformity along real orbits, per (class, d)
cnt = Counter(); tot = Counter()
for _ in range(500):
    w = random.getrandbits(90) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 30)
    for _ in range(160):
        if d in (1, 2):
            cnt[(w % 8, d, (w >> 3) % 4)] += 1; tot[(w % 8, d)] += 1
        s, w, d = step(w, d)
        if w == 1 and d == 1: break
print("\nE4b omega-digit uniformity along orbits: P(bits 3-4 of omega | class, d) vs 0.25")
bad = []
for (w8, d) in sorted(tot):
    if tot[(w8, d)] < 3000: continue
    ps = [cnt[(w8, d, b)] / tot[(w8, d)] for b in range(4)]
    dev = max(abs(p - 0.25) for p in ps)
    flag = " <-- BIASED" if dev > 0.02 else ""
    print(f"  class {(w8, d)}: {['%.3f' % p for p in ps]}  n={tot[(w8,d)]}{flag}")

# ==== aeh6.py ====
# Hardened test: per-orbit means + across-orbit SE (orbits independent).
# Cells: (class (1,1), bits34=3), (class (1,2), bits34=0), (class (7,1), bits34 in {0,3}),
# and the pair cell (s,s')=(4,3).
import random, math
from collections import Counter
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(71)
cells = {"c11_b3": [], "c12_b0": [], "c71_b03": [], "pair43": []}
NORB = 2500
for _ in range(NORB):
    w = random.getrandbits(90) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 30)
    h11 = [0, 0]; h12 = [0, 0]; h71 = [0, 0]; p43 = [0, 0]; prev = None
    for _ in range(160):
        w8, b34 = w % 8, (w >> 3) % 4
        if w8 == 1 and d == 1: h11[0] += 1; h11[1] += (b34 == 3)
        if w8 == 1 and d == 2: h12[0] += 1; h12[1] += (b34 == 0)
        if w8 == 7 and d == 1: h71[0] += 1; h71[1] += (b34 in (0, 3))
        s, w, d = step(w, d)
        k = min(s, 9)
        if prev == 4: p43[0] += 1; p43[1] += (k == 3)
        prev = k
        if w == 1 and d == 1: break
    if h11[0] >= 3: cells["c11_b3"].append(h11[1] / h11[0])
    if h12[0] >= 3: cells["c12_b0"].append(h12[1] / h12[0])
    if h71[0] >= 3: cells["c71_b03"].append(h71[1] / h71[0])
    if p43[0] >= 2: cells["pair43"].append(p43[1] / p43[0])
null = {"c11_b3": 0.25, "c12_b0": 0.25, "c71_b03": 0.50, "pair43": None}
# null for pair43: P(s'=3) unconditional ~ 0.125-0.131; use orbit marginal measured separately
print(f"{'cell':10s} {'orbits':>6s} {'mean':>7s} {'null':>6s} {'SE':>7s} {'z':>6s}")
for name, vals in cells.items():
    m = sum(vals) / len(vals); se = (sum((v - m)**2 for v in vals) / (len(vals)-1))**0.5 / len(vals)**0.5
    nl = null[name] if null[name] else 0.128
    print(f"{name:10s} {len(vals):6d} {m:7.4f} {nl:6.3f} {se:7.4f} {(m-nl)/se:6.1f}")

# ==== aeh7.py ====
# Same hardened cells, but tallied ONLY while omega > 2^24 (bulk regime),
# and separately for omega <= 2^24 (bottom regime).
import random
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(73)
CUT = 1 << 24
res = {}
for regime in ("bulk", "bottom"):
    cells = {"c11_b3": [], "c12_b0": [], "c71_b03": [], "pair43": []}
    for _ in range(2500):
        w = random.getrandbits(90) | 1
        if w % 3 == 0: continue
        d = random.randrange(1, 30)
        h = {k: [0, 0] for k in cells}; prev = None
        for _ in range(200):
            big = w > CUT
            use = (regime == "bulk") == big
            w8, b34 = w % 8, (w >> 3) % 4
            if use:
                if w8 == 1 and d == 1: h["c11_b3"][0] += 1; h["c11_b3"][1] += (b34 == 3)
                if w8 == 1 and d == 2: h["c12_b0"][0] += 1; h["c12_b0"][1] += (b34 == 0)
                if w8 == 7 and d == 1: h["c71_b03"][0] += 1; h["c71_b03"][1] += (b34 in (0, 3))
            s, w2, d2 = step(w, d); k = min(s, 9)
            if use and prev == 4: h["pair43"][0] += 1; h["pair43"][1] += (k == 3)
            prev = k; w, d = w2, d2
            if w == 1 and d == 1: break
        for kk in cells:
            if h[kk][0] >= 2: cells[kk].append(h[kk][1] / h[kk][0])
    res[regime] = cells
null = {"c11_b3": 0.25, "c12_b0": 0.25, "c71_b03": 0.50, "pair43": 0.128}
print(f"{'cell':10s} {'regime':>7s} {'orbits':>6s} {'mean':>7s} {'null':>6s} {'z':>6s}")
for name in null:
    for regime in ("bulk", "bottom"):
        vals = res[regime][name]
        if len(vals) < 30: print(f"{name:10s} {regime:>7s}  (insufficient)"); continue
        m = sum(vals)/len(vals)
        se = (sum((v-m)**2 for v in vals)/(len(vals)-1))**0.5/len(vals)**0.5
        print(f"{name:10s} {regime:>7s} {len(vals):6d} {m:7.4f} {null[name]:6.3f} {(m-null[name])/se:6.1f}")

# ==== aeh8.py ====
# c11_b3 recheck with CUT = 2^40 (eliminate near-bottom contamination)
import random
def v2(x): return (x & -x).bit_length() - 1
def step(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return s, u, sig - s + a
random.seed(79)
CUT = 1 << 40
vals = []
for _ in range(4000):
    w = random.getrandbits(100) | 1
    if w % 3 == 0: continue
    d = random.randrange(1, 30)
    num = den = 0
    for _ in range(220):
        if w > CUT and w % 8 == 1 and d == 1:
            den += 1; num += ((w >> 3) % 4 == 3)
        s, w, d = step(w, d)
        if w == 1 and d == 1: break
    if den >= 2: vals.append(num / den)
m = sum(vals)/len(vals)
se = (sum((v-m)**2 for v in vals)/(len(vals)-1))**0.5/len(vals)**0.5
print(f"c11_b3, CUT=2^40: {len(vals)} orbits, mean {m:.4f} vs 0.25, z = {(m-0.25)/se:.1f}")

