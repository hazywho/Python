
third = []
answer = []
countph = []
count = 0
last = 0
first = int(input())
for _ in range(first):
    second = int(input())
    tp = input().split(" ")
    for l in tp:
        third.append(int(l))
    print(third)
    for x in range(second+1):
        for i in range(x):
            count += third[i]
            print(x, i)
        countph.append(count)
        count = 0
    for m in countph:
        last += m
    answer.append(last)
    last = 0
    count = 0
    third = []
print(answer)