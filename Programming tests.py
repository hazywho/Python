string = "^_"
loc = 0
times = 0
while loc < len(string):
    if string[loc] == "_" and string[loc+1] != "^" or string[loc] == "^" and string[loc+1] != "_" :
        string = string[:loc] + "^" + string[loc:]
        print(string)
        times +=1

    loc +=1
    
print(times)

#string = string[:2] + "^" + string[1:]