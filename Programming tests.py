string = "^_"
loc = 0
times = 0
while loc < len(string):
    if string[loc-1] == "_" and string[loc] != "^":
        string = string[:loc] + "^" + string[loc:]
        print(string)
        times +=1

    loc +=1
    
print(times)

#string = string[:2] + "^" + string[1:]