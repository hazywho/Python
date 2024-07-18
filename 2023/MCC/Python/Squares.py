count = 0
with open(r'C:\Users\zanyi\Downloads\settings') as f:
    for line in f:
        x = list(map(int,line.split(" ")))
import math
for i in x:
    if math.sqrt(i) == int(math.sqrt(i)):
        count += 1
print(count)

