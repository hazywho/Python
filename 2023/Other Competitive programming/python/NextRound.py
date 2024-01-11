first = input().split(" ")
second = input().split(" ")
print(second)
count = 0
for each in second:
    if int(each) >= int(second[int(first[1])-1]):
        if int(each) > 0:
            count+=1
print(count)