n,k = list(map(int,input().split()))
l = list(map(int,input().split()))
ans = 2+(len(l)-2)*(len(l)-1)
count =0
for _ in range(ans-2):
    for i in range(1,sum(l)+1):
        print(i)
        count += pow(i,2)
 
print(count)
