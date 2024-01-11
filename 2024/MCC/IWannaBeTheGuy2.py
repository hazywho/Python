level =  set(range(1, int(input()) + 1))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = set(x[1:])
y = set(y[1:])

print('I become the guy.' if level - (x | y) == set() else 'Oh, my keyboard!')