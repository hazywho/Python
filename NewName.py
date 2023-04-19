string = "^______^"
while True:
    for loc,x in enumerate(string):
        if x == "_":
            string = string[:2] + "^" + string[1:]
            print(string)


        
