t = int(input())
for _ in range(t):
    p = input()
    flag=0
    array = list(map(int,input().split()))
    array = list(set(array))
    array.sort()
    for i in range(len(array)-1):
        if array[i]+1 != array[i+1]:
            print("NO")
            flag=1
            break
    if flag==0:
        print("YES")
