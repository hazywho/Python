x = input().split(" ")
n = []
for k in x: 
    n.append(int(k))
number = n[0]
times = n[1]
for _ in range(times):
    if int(number/10) == number/10:
        number = number/10
    else:
        number -=1
print(int(number))