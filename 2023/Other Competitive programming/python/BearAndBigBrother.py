first = input().split(" ")
bear = int(first[0])
big_brother = int(first[1])
count = 0
while bear <= big_brother:
    bear = bear*3
    big_brother = big_brother*2
    count +=1
print(count)