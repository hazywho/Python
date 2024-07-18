m1 = input().split(" ")
m2 = input().split(" ")
m3 = input().split(" ")
m4 = input().split(" ")
m5 = input().split(" ")
pox = 0
poy = 0
a = 0
b = 0
matrix = [m1,m2,m3,m4,m5]
for y,m in enumerate(matrix):
    for x,v in enumerate(m):
        if v == "1":
            pox = int(x)+1
            poy = int(y)+1

if pox >3:
    a = pox-3
elif pox<3:
    a = 3-pox
if poy >3:
    b = poy-3
elif poy<3:
    b = 3-poy

print(a+b)
