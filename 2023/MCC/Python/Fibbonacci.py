l = [0,1]
n = int(input())
m = 1
count = 0
while m < n :
    number = l[m]+l[m-1]
    l.append(number)
    m += 1
    count += 1
print(l[len(l)-1])
print(count)