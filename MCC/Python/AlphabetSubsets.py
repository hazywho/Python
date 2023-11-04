n,k = list(map(int,input().split()))
inp = input().split()
r = []
for letters in inp:
    r.append(letters)
import itertools
new = []
subsets = []
newnew  = []
for s in range(1,n+1):
    subsets=(list(itertools.combinations(r,s)))
    for i in subsets:
        new.append(sorted(list(set(i))))
    for m in new:
        if m not in newnew:
            newnew.append(m)
        sorted(newnew)
print(newnew)
