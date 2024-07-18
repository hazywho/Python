x = []
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\pastingFile.txt") as f:
    for lines in f:
        x.append(list(map(int, lines.split(" "))))
h = []
w = []
for i in x:
    h.append(i[0])
    w.append(i[1])
count = 0
for g in w:
    count += g
print(max(h)*(count))
