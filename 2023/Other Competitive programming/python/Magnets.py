times = int(input())
lest = []
count = 1
for _ in range(times):
    string = input()
    lest.append(string)
for x in range(1,len(lest)):
    if lest[x-1] != lest[x]:
        count += 1
print(count)