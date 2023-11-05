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
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\Subsette.py") as f:
   for lines in f:
      n = list(map(int,lines.split()))
h,k = 10,1

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

  summ += total%998244353
print(summ)
biglist.sort()
for i in biglist:
   print(i)


# def sublists(lst):
#     n = len(lst)
#     sublists = []
     
#     for start in range(n):
#         for end in range(start + 1, n + 1):
#             sublists.append(lst[start:end])
     
#     return sublists
# a = 998244353

# h,k = list(map(int,input().split()))
# original_list = list(map(int,input().split()))
# new = []
# sublists_nested = sublists(original_list)
# l = 0
# new2 = []
# for k in sublists_nested:
#     c = 0
#     for g in s:
#          c+=pow(g,k)%a
#     new2.append(c)
# for num in new2:
#     l+=num
# print(l)

