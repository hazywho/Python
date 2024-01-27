testCases = int(input())
for _ in range(testCases):
    count = 0
    pcount = 0
    firstList=[]
    SecondList=[]
    length=int(input())
    f=input()
    s=input()
    for i in range(length):
        firstList.append(int(f[i]))
        SecondList.append(int(s[i]))
    for i in range(length):
        if firstList[i] > SecondList[i] and sum(firstList) > sum(SecondList):
            firstList[i]=0
            count += 1
    for i in range(length):
        if firstList[i] < SecondList[i] and sum(firstList) < sum(SecondList):
            firstList[i]=1
            count += 1
    for i in range(length):
        if firstList[i] > SecondList[i]:
            pcount += 1
    print(count+pcount)