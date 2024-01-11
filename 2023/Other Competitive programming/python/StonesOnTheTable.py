first = int(input())
second = input()
newlist = []
count = 0
for c in second:
    newlist.append(c)
for i in range(1,len(newlist)):
    if newlist[i] == newlist[i-1]:
        count += 1
print(count)