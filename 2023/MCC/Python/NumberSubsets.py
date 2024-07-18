import itertools
new = []
subsets = []
newnew  = []
final = []
n = int(input())
r = []


for i in range(1,n+1):
    r.append(i)
for s in range(1,n+1):
    subsets=(list(itertools.combinations(r,s)))
    for i in subsets:
        new.append(sorted(list(set(i))))
    for m in new:
        if m not in newnew:
            newnew.append(m)
        sorted(newnew)
print("[]",end=" ")

for items in newnew:
    print(items,end= " ")

