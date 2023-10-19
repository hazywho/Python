x = list(map(int,input().split()))
n = x[0]
m = x[1]
a = x[2]
count = 0
area = m*n
while area > 0:
    print(area)
    area -= a*a
    count += 1
print(count)