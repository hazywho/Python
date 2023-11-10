with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Real\Collatztext.txt") as f:
    for lines in f:
        a = list(map(int,lines.split(" ")))
k = 798
for _ in range(k):
    for index,i in enumerate(a):
        if i%2 == 0:
            a[index] = i/2
        else:
            a[index] = 3*i+1
g = 0
for m in a:
    g+= m
print(int(g))