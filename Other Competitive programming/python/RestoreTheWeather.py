r = int(input())
for _ in range(r):
    l, restrictions = list(map(int,input().split()))
    firstl = list(map(int,input().split()))
    secondl = list(map(int,input().split()))
    newl = []
    for i in firstl:
        if i > 0:
            secondl.sort(reverse=True)
        else:
            secondl.sort()
        for s in secondl:
            if abs(i-s) <= restrictions:
                newl.append(s)
                secondl.pop(secondl.index(s))
                

    for items in range(len(newl)-1): print(newl[items], end = " ")
    print(newl[len(newl)-1])
#need to search for all first