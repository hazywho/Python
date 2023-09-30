l = input().split("+")
newl = []
for n in l:
    newl.append(int(n))

newl.sort()
for i in range(len(newl)-1):
    print(f"{newl[i]}+", end = "")
print(newl[-1])