import math
x = input().split(" ")
y = x[0]
j = x[1]
numb = int(x[0])

for l in range(int(j)):
    print(numb)
    if str(numb)[len(str(numb))-1:] == "0":
        numb = math.floor(numb/10)
    else:
        numb -= int(j)

print(int(numb))

