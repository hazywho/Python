#5 1
#BGGBG
#GBGGB
r,l = list(map(int,input().split()))
s = input()
string = []
for m in s:
    string.append(m)
print(string)
for index,i in enumerate(string):
    if i == "B" and index != len(string)-1:
        last = "B"
        new  = string[index+1]
        string[index] = new
        string[index+1] = last
        continue
print(string)




