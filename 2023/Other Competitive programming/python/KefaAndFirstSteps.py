first = input()
second = input().split(" ")
newlist = []
best = 0
count = 0
log = [0]
for l in second:
    newlist.append(int(l))

for x in newlist:
    if x >= best:
        best = x
        count +=1
        log.append(count)
    else:
        best = x
        count = 1

print(max(log))