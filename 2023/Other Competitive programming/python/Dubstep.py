first = input().replace("WUB"," ")
def remove_letter(string,index):
    b = bytearray(string,'utf-8')
    del b[index]
    return b.decode()
split = first.split()
final = ""
for words in split:
    print(words,end=" ")


