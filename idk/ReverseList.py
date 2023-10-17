def reverse(x):
    rList = []
    y = len(x)
    while y > 0:
        y-=1
        rList.append(x[y])
    return rList
mm = "racecar"
mm2 = list(map(str,mm))
mm2= []
for i in mm: #i = mm[range(0,len(mm)+1)]
    mm2.append(i)
print(mm2)

if reverse(mm.lower()) == mm2:
    print("p")
else:
    print("n")

