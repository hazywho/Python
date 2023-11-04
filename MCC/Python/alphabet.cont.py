
newnew = []
firstlist = []
biglist = []
newbestl = []
summ = 0
for items in newnew:
    firstlist.append(items)
for l in firstlist:
    newlest = []
    for er in l:
        newlest.append(int(er))
    biglist.append(newlest)
for new in biglist:
    total = 0
    for numb in new:
        total += numb
    summ += pow(total,k,998244353)
print(summ)
