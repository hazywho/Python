# 4
# 3 1 2 3
# 2 2 4

x = int(input())
y = list(map(int,input().split()))
z = list(map(int,input().split()))
for i in z:
    y.append(i)
l=sorted(list(dict.fromkeys(y)))
for id, i in enumerate(l):
    if  i == 0:
        l.pop(id)

if l != [1,2,3]:
    if list(range(1,x+1))==l:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
else:
    print("Oh, my keyboard!")


level =  set(range(1, int(input()) + 1))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = set(x[1:])
y = set(y[1:])

print('I become the guy.' if level - (x | y) == set() else 'Oh, my keyboard!')