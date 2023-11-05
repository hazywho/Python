
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\subsets.txt") as f:
    for i in f:
        s = list(map(int,i.split()))
f = open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\pastingFile.txt", "a")
for i in s:
    f.write(f"{i},")
f.close()