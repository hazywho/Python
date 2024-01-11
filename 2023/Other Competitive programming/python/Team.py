l = int(input())
rcount = 0
for _ in range(l):
    m = list(map(int,input().split()))
    count = 0
    for i in m:
        if i == 1:
            count +=1
    if count >1:
        rcount +=1
print(rcount)