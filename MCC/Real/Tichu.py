p = []
w = []
h = []
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Real\rectangles.txt") as f:
    for lines in f:
        p.append(list(map(int,lines.split(" "))))
base = 0
for i in p:
    h.append(i[0])
    w.append(i[1])
for x,l in enumerate(h):
    base += w[x]* l
print(base)