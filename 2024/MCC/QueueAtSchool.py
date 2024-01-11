# 5 1
# BGGBG
# GBGGB
amount,times = list(map(int,input().split()))
wordl=input()
word = []
for i in wordl: word.append(i)
flag1=False
index = 0
while times > 0:
    flag1=False
    index = 0
    while index < len(word) and flag1==False:
            
            
            if word[index] == "B":
                try:
                    if word[index+1]!="B":
                        word[index+1]="B"
                        word[index]="G"
                        index +=1
                    else:
                        word[index]="B"
                except IndexError:
                    flag1=True
            index += 1
    times -=1


print(''.join(str(x) for x in word))