import itertools
f = input().split(" ")
notbefore = int(f[0])-1
yesafter = int(f[1])-1
lest = [1,1]
n = 1
newfibbonacci = []
new = []
newnew  = []

while n < yesafter :
    lest.append(lest[n]+lest[n-1])
    n += 1
for index in range(notbefore,yesafter+1):
    newfibbonacci.append(lest[index])

r = newfibbonacci
n = len(r)
for s in range(1,n+1):
    subsets=list(itertools.combinations(r,s))
    for i in subsets:
        new.append(sorted(i))
    for m in new:
        if m not in newnew:
            newnew.append(m)
        newnew = sorted(newnew)
print("[]",end=" ")

for items in newnew:
    print(items,end= " ")