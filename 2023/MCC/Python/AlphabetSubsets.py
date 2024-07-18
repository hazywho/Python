l = int(input())
for _ in range(l):
    x= input()
    newx = []
    for i in x:
        newx.append(dict[int(i)])
    newx.insert(0,0)
    final = 0
    for g in range(0,len(newx)-1):
        final +=  abs(newx[g+1]-newx[g])
    final += 4         
    print(final)
    


