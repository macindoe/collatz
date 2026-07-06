# Pilot + verification for the low-order anchor-increment law (stage4.md 11.8.7).
# Part 1: bucket pilot (11.8.7.1). Part 2: predictor + lift-invariance tests (11.8.7.4).

# Pilot: does the anchor increment ΔM admit a LOW-ORDER law?
# Test: is ΔM mod 8 a function of (ω mod 2^10, d mod 2^8, s, a+)?
import random
K = 40; MOD = 1 << K
def v2(x): return (x & -x).bit_length() - 1
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def N_anchor(u, bits):
    n = 0
    for j in range(bits):
        m = 1 << (j + 4)
        if pow(9, n, m) != pow(u % m, -1, m): n += 1 << j
    return n
def M_anchor(w, bits): return N_anchor((w * w) % (1 << (bits + 5)), bits)

random.seed(7)
buckets = {}
for _ in range(20000):
    w = random.randrange(1, 100000, 2)
    if w % 3 == 0: continue
    d = random.randrange(1, 60)
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    ap = v3(C); wp = C >> v2(C); wp //= 3**ap
    dM = (M_anchor(wp, 6) - M_anchor(w, 6)) % 8
    key = (w % 1024, d % 256, s, ap)
    buckets.setdefault(key, set()).add(dM)
multi = [(k, v) for k, v in buckets.items() if len(v) > 1]
tot = len(buckets)
print(f"keys: {tot}, keys with conflicting ΔM mod 8: {len(multi)}")
# where do conflicts live? by s and a+
from collections import Counter
cs = Counter((k[2], k[3]) for k, v in multi)
print("conflicts by (s, a+):", dict(list(cs.items())[:10]))
# retry with bigger moduli on the conflicting stratum
b2 = {}
random.seed(8)
for _ in range(20000):
    w = random.randrange(1, 100000, 2)
    if w % 3 == 0: continue
    d = random.randrange(1, 60)
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    ap = v3(C); wp = C >> v2(C); wp //= 3**ap
    dM = (M_anchor(wp, 6) - M_anchor(w, 6)) % 8
    key = (w % (1 << 14), d % (1 << 12), s, ap)   # more digits
    b2.setdefault(key, set()).add(dM)
m2 = [(k, v) for k, v in b2.items() if len(v) > 1]
print(f"bigger key: keys {len(b2)}, conflicts {len(m2)}")

# ---- Part 2: derived-law verification ----
import random
def v2(x): return (x & -x).bit_length() - 1
def v3(x):
    v = 0
    while x % 3 == 0: x //= 3; v += 1
    return v
def N_mod(u, k):
    n = 0
    for j in range(k):
        m = 1 << (j + 4)
        if pow(9, n, m) != pow(u % m, -1, m): n += 1 << j
    return n
def M_mod(w, k): return N_mod((w * w) % (1 << (k + 4)), k)
def true_dM_mod(w, wp, k): return (M_mod(wp, k) - M_mod(w, k)) % (1 << k)

def predictor(rw, rd, s, sigma, ap_modk, k):
    Q = sigma + k + 2; MQ = 1 << Q
    Chat = (pow(3, rd, MQ) * rw - 1 + (1 << s)) % MQ
    assert Chat % (1 << sigma) == 0
    r = k + 2; Mr = 1 << r
    whatp = ((Chat >> sigma) * pow(pow(3, ap_modk, Mr), -1, Mr)) % Mr
    ratio = (whatp * pow(rw % Mr, -1, Mr)) % Mr
    ratio2 = (ratio * ratio) % (1 << (k + 3))
    t = 0
    for j in range(k):
        m = 1 << (j + 4)
        if pow(9, t, m) != pow(ratio2 % m, -1, m): t += 1 << j
    return t

random.seed(11)
failsA, failsB, nA, nB = [], [], 0, 0
for k in (1, 3, 6):
    for _ in range(2000):
        w = random.randrange(1, 200000, 2)
        if w % 3 == 0: continue
        d = random.randrange(1, 50)
        A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
        sigma = v2(C); ap = v3(C)
        wp = (C >> sigma) // 3**ap
        truth = true_dM_mod(w, wp, k)
        rw = w % (1 << (sigma + k + 2)); rd = d % (1 << (sigma + k))
        nA += 1
        if predictor(rw, rd, s, sigma, ap % (1 << k), k) != truth:
            failsA.append((k, w, d)); continue
        if sigma + k > 13: continue  # keep lifted d computable
        for _ in range(4):
            w2 = w + (1 << (sigma + k + 2)) * random.randrange(1, 8)
            d2 = d + (1 << (sigma + k)) * random.randrange(1, 3)
            if w2 % 3 == 0: continue
            A2 = 3**d2 * w2 - 1; s2 = v2(A2); C2 = A2 + (1 << s2)
            if s2 != s or v2(C2) != sigma: failsB.append((k,"stratum",w,d,w2,d2)); continue
            ap2 = v3(C2)
            if ap2 % (1 << k) != ap % (1 << k): continue
            wp2 = (C2 >> v2(C2)) // 3**ap2
            nB += 1
            if true_dM_mod(w2 % (1 << (k+9)), wp2 % (1 << (k+9)), k) != truth:
                failsB.append((k, w, d, w2, d2))
print("A (predictor from truncations):", nA, "checks,", len(failsA), "failures")
print("B (lift-invariance):           ", nB, "checks,", len(failsB), "failures")
print("failures:", (failsA + failsB)[:6])
