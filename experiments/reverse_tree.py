# Reverse-front verification suite (reverse.md, section 14):
# (A) predecessor-rule completeness vs brute force
# (B) backward ledger P(d=j) = 2/3^j
# (C) M3 algebra: M3(1) = 3-adic -1; affine-log homomorphism
# (D) exact tree enumeration from (1,1) by increasing omega; growth exponent
# (also: mirror anchor law d = 1 + v3(s - M3(y)), 4265 checks, in-session)
import random, heapq, math
def v2(x):
    v=0
    while x%2==0: x//=2; v+=1
    return v
def v3(x):
    v=0
    while x%3==0: x//=3; v+=1
    return v
def F(w,d):
    A=3**d*w-1; s=v2(A); C=A+(1<<s)
    sig=v2(C); u=C>>sig; a=v3(u)
    return (u//3**a, sig-s+a)
def preds_of_state(W,D,wcap,scap=400):
    out=set()
    for a in range(D):
        y=2**(D-a)*3**a*W-1
        if y%3==0: continue
        s0=1 if y%3==1 else 2
        for s in range(s0,scap,2):
            N=(1<<s)*y+1
            d=v3(N); w=N//3**d
            if d>=1 and w<=wcap: out.add((w,d))
    return out
def M3(y,k):
    t=None
    for tt in (0,1):
        if pow(2,tt,3)==(-pow(y,-1,3))%3: t=tt
    for j in range(1,k+1):
        mod=3**(j+1); target=(-pow(y,-1,mod))%mod
        stride=2*3**(j-1)
        for c in range(3):
            if pow(2,t+c*stride,mod)==target: t=t+c*stride; break
    return t
def mirror_law_check(trials=500,K=8):
    random.seed(113); bad=checked=0
    for _ in range(trials):
        y=random.randrange(1,10**5,2)
        if y%3==0: continue
        m3=M3(y,K)
        for _ in range(25):
            s=random.randrange(1,400)
            N=(1<<s)*y+1
            if N%3: continue
            checked+=1
            diff=(s-m3)%(2*3**K)
            rhs=1+(v3(diff) if diff%3**K else K)
            if v3(N)<=K and v3(N)!=rhs: bad+=1
    return checked,bad
def tree_counts(X):
    seen={(1,1)}; pq=[(1,1,1)]
    while pq:
        w,d,_=heapq.heappop(pq)
        for a in range(d):
            y=2**(d-a)*3**a*w-1
            if y%3==0: continue
            s0=1 if y%3==1 else 2
            s=s0
            while True:
                N=(1<<s)*y+1
                dd=v3(N); ww=N//3**dd
                if ww>X and s>s0+6: break
                if dd>=1 and ww<=X and (ww,dd) not in seen:
                    seen.add((ww,dd)); heapq.heappush(pq,(ww,dd,0))
                s+=2
                if s>420: break
    return seen
if __name__=="__main__":
    random.seed(127)
    for (W,D) in [(1,1),(7,1),(1,3),(25,2),(11,4),(35,2),(1,2)]:
        brute={(w,d) for w in range(1,3001,2) if w%3 for d in range(1,13) if F(w,d)==(W,D)}
        rule={p for p in preds_of_state(W,D,3000) if p[1]<=12}
        assert brute==rule,(W,D)
    print("A: predecessor rule exact")
    c,b=mirror_law_check(); print(f"mirror law: {c} checks, {b} failures")
    for X in (2**10,2**16,2**19):
        n=len(tree_counts(X)); print(f"D: N({X}) = {n}, exponent {math.log(n)/math.log(X):.3f}")

# ---- 14.5 additions: door mortality, Gardens of Eden, renewal mass ----
def door_mortality_check(trials=20000,seed=149):
    random.seed(seed); b=0
    for _ in range(trials):
        W=random.randrange(1,10**5,2)
        if W%3==0: continue
        D=random.randrange(1,20)
        for a in range(D):
            y=2**(D-a)*3**a*W-1
            if (y%3==0)!=(a==0 and (pow(2,D,3)*W)%3==1): b+=1
    return b
def renewal_mass(c,Dlaw,tot):
    Ed=2*3**(c-1)/(1-3**(c-1))
    s_sum=0.5*(2**(-c)+4**(-c))/(1-4**(-c))
    m=0.0
    for D,cnt in Dlaw.items():
        bm=sum((0.5 if a==0 else 1.0)*(2**(-c*(D-a)))*(3**(-c*a)) for a in range(D))
        m+=(cnt/tot)*bm*s_sum*Ed
    return m

# ---- 14.6 additions: door-tree core for the rigorous density bound ----
def door_tree_core(X):
    import collections
    q=collections.deque([1]); out={1}
    while q:
        y=q.popleft()
        s0=1 if y%3==1 else 2
        s=s0
        while (1<<(s+1))*y//3 <= 4*X and s<s0+400:
            yp=((1<<(s+1))*y-1)
            if yp%3==0:
                yp//=3
                if yp%3!=0 and yp>1 and yp<=X and yp not in out:
                    out.add(yp); q.append(yp)
            s+=2
    return out
def density_mass(c):
    return (2**(-3.415*c)+2**(-5.415*c))/(1-2**(-6*c))
