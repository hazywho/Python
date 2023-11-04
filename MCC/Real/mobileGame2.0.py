l  = 20
ans = []
mn = []
countes=0
while countes < 2*l:
    with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Real\MobileGame.txt") as f:
        for lines in f:
            mn.append(list(map(int,lines.split())))
    n,a,b = mn[countes]
    array = mn[countes+1]
    amount = 0
    newl = []
    while a < b:
        for e,i in enumerate(array):
            if i<a:
                newl.append(i)
                array.pop(e)
        try:
            a += max(newl)
            newl.pop(newl.index(max(newl)))
            amount += 1
        except ValueError:
            ans.append(-1)
            break
    else:
        ans.append(amount)
    countes +=  2
for m in ans:
    print(m)

