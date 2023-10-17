f = list(map(int,input().split()))
s = list(map(int,input().split()))
w = 0
for i in s:
    if i > f[1]:
        w += 2
    else:
        w+=1

print(w)