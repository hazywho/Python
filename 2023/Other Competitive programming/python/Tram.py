n = int(input())
ml = []
for _ in range(n):
    m = list(map(int,input().split()))
    ml.append(m)
final = []
count = 0
for f in ml:
    count += f[1]
    count -= f[0]
    final.append(count)

print(max(final))