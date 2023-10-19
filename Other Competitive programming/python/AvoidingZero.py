third = []
count = 0
first = int(input())
for _ in range(first):
    second = int(input())
    tp = input().split(" ")
    for l in tp:
        third.append(int(l))
    for n in third:
        count += n


    if count == 0:
        print("NO")
    else:
        print("YES")
        if count > 0:
            third.sort(reverse=True)


            for n in range(len(third)-1): print(third[n],end=" ")
            print(third[len(third)-1])



        else:
            third.sort(reverse=False)


            for n in range(len(third)-1): print(third[n],end=" ")
            print(third[len(third)-1])

            
    count = 0
    third = []
