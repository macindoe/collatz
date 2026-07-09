# Ladder law verification (ladder.md, section 15):
# A(w,d+1) = 3 A(w,d) + 2 forces:
#  (i)  s=1:   e(w,d+1) = T(e(w,d))
#  (ii) s>=2:  e(w,d+1) = 3*2^(s-1)*e(w,d) + 1  and  s(w,d+1) = 1
# plus the run-length histogram showing consecutive T-steps never stack.
import random
from collections import Counter
def v2(x):
    v=0
    while x%2==0: x//=2; v+=1
    return v
def T(x):
    y=3*x+1
    return y>>v2(y)
def exit_s(w,d):
    A=3**d*w-1; s=v2(A)
    return A>>s, s
if __name__=="__main__":
    random.seed(131)
    bad1=bad2=n1=n2=0
    for _ in range(30000):
        w=random.randrange(1,10**6,2)
        if w%3==0: continue
        d=random.randrange(1,40)
        e,s=exit_s(w,d); e2,s2=exit_s(w,d+1)
        if s==1:
            n1+=1; bad1+=(e2!=T(e))
        else:
            n2+=1; bad2+=(e2!=3*2**(s-1)*e+1 or s2!=1)
    print(f"(i) {n1} cases, {bad1} failures; (ii) {n2} cases, {bad2} failures")
    runlen=Counter()
    for w in range(1,4000,2):
        if w%3==0: continue
        d=1; r=0
        for _ in range(60):
            e,s=exit_s(w,d)
            if s==1: r+=1
            else: runlen[r]+=1; r=0
            d+=1
    print("T-step run lengths between spikes:", dict(sorted(runlen.items())))
