# Period-1 cycles of F (fixed points).
# Derivation: F(w,d)=(w,d) with s, sigma, a, m' = sigma - s gives exactly
#     w * 3^a * (2^(s+m') - 3^m') = 2^s - 1,   m' >= 1, s >= 1, d = m' + a.
# So: q(m,s) = 2^(s+m) - 3^m must be positive and divide 2^s - 1.
# Sign:  2^s > (3/2)^m.   Size: q <= 2^s - 1  <=>  2^s (2^m - 1) <= 3^m - 1.
# => 2^s pinned to a multiplicative window of width (1-3^-m)/(1-2^-m) around (3/2)^m
# => at most ONE candidate s per m. Check it exactly, with divisibility.
sols = []
T = 3  # 3^m
for m in range(1, 20001):
    if m > 1: T *= 3
    # smallest s with 2^(s+m) > 3^m  <=>  2^s > 3^m / 2^m
    s = max(1, (T >> m).bit_length())          # 2^(s-1) <= T/2^m < 2^s ... verify
    while (1 << (s + m)) <= T: s += 1
    while s > 1 and (1 << (s - 1 + m)) > T: s -= 1
    # size window: need 2^s (2^m - 1) <= 3^m - 1 ; if smallest s fails, all fail
    if (1 << s) * ((1 << m) - 1) > T - 1:
        continue
    q = (1 << (s + m)) - T
    if (( (1 << s) - 1 ) % q) == 0:
        Q = ((1 << s) - 1) // q
        a = 0
        while Q % 3 == 0: Q //= 3; a += 1
        sols.append((m, s, a, Q))   # fixed point (w=Q, d=m+a)
print("period-1 solutions for m <= 20000:", sols)

# Sanity: brute-force cycle search of F over small states
def v2(x): return (x & -x).bit_length() - 1
def F(w, d):
    A = 3**d * w - 1; s = v2(A); C = A + (1 << s)
    sig = v2(C); a = 0; u = C >> sig
    while u % 3 == 0: u //= 3; a += 1
    return (u, sig - s + a)
cyc = set()
for w in range(1, 3000, 2):
    if w % 3 == 0: continue
    for d in range(1, 33):
        st = (w, d); seen = {}
        for i in range(200):
            if st in seen:
                # walk the cycle
                cur, c = st, []
                while True:
                    c.append(cur); cur = F(*cur)
                    if cur == st: break
                cyc.add(tuple(sorted(c))); break
            seen[st] = i; st = F(*st)
            if st[0] > 10**40: break
print("cycles found in direct search:", cyc)
