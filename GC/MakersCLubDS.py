def countlen(item,threshold):
    count=0
    for words in item.split(" "):
        if len(words)>=threshold:
            count+=1
    return count

x = countlen("Dream or nightmare, we have to live our experience as it is, and we have to live it awake. We live in a world which is penetrated through and through by science and which is both whole and real. We cannot turn it into a game simply by taking sides.",4)
print(x)