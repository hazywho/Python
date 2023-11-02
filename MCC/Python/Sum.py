g = 0
with open(r'C:\Users\zanyi\Downloads\settings') as f:
    for line in f:
        x = list(map(int,line.split(" ")))
for i in x:
    g+= i
print(i)