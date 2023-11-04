def operate(set, subsets, subset, index):
  subsets.append(subset.copy())
  for i in range(index, len(set)):
    subset.append(set[i])
    operate(set, subsets, subset, i+1)
    subset.pop(-1)
  return subsets

def set_op(set):
  subset = []
  subsets = []
  index = 0
  operate(set, subsets, subset, index)
  return subsets
h,k = list(map(int,input().split()))
n = list(map(str,input().split()))
k = k%998244353
subsets = set_op(n)
firstlist = []
biglist = []
newbestl = []
summ = 0
for items in subsets:
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
    
    summ += pow(total,k)
print(summ)


