nm = input()
l = input().split(" ")
x = []
total = 0
for item in l:
    x.append(int(item))
x.sort()
for n in range(int(nm[-1])):
    if x[n]<=0:
        total += abs(x[n])
print(total)