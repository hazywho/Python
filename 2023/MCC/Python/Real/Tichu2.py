n,e = list(map(int,input().split()))
array = list(map(int,input().split()))
k = e
count = 0
array = list(set(array))
array.sort()
saves = []
last = array[0]-1
print(array)
for ind, i in enumerate(array):
    if i == last+1:
        count+= 1
        last = i
    elif i-k <= last+1:
        print(i)
        for g in range(1,k+1):
            if i+g-1 == last:
                k-=g-1
                count+=1
                print(g)
                last = i+g
    elif i-k >= last+1:
        saves.append(count)
        saves.append(k)
        count = 0
        k = e
        last = i
        continue
    
    

print(saves)