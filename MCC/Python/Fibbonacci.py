l = [1,1]
n = int(input())-1
m = 1
while m < n :
    number = l[m]+l[m-1]
    l.append(number)
    m += 1
print(l[len(l)-1])