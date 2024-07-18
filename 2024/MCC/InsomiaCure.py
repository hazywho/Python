k=[]
for _ in range(4):
    k.append(int(input()))
num = int(input())
count = 0
for i in range(1,num+1):
    if i%k[0] !=0 and i%k[1] != 0 and i%k[2] != 0 and i%k[3] != 0:
        count += 1
print(num-count)