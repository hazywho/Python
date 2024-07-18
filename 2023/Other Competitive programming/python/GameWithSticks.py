grids = input().split()
x = int(grids[0])
y = int(grids[1])
count = 0
while x >=1 and y>=1:
    x-=1
    y-=1
    count +=1
if count %2 ==0:
    print("Malvika")
else:
    print("Akshat")
