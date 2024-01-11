x = int(input())
y = x+1
testy = []
for l in str(y):
    testy.append(l)
while testy != list(dict.fromkeys(str(y)).keys()):
    testy = []
    y +=1
    for l in str(y):
        testy.append(l)
print(y)