dit = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
}

inp = input().lower()
r = []
for letters in inp:
    r.append(dit[letters])
n = len(r)

import itertools
new = []
subsets = []
newnew  = []
final = []
for s in range(1,n+1):
    subsets=(list(itertools.combinations(r,s)))
    for i in subsets:
        new.append(sorted(list(set(i))))
    for m in new:
        if m not in newnew:
            newnew.append(m)
        sorted(newnew)
print("[]",end=" ")
output=dict(map(reversed,dit.items()))
abced = []
for items in newnew:
    print("[",end="")
    for g in items:
        print(f"{output[g]} ",end="")
    print("]",end="")