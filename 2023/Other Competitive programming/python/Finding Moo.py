string = "MOOMOMOMOOM"
count = 0
stringList = []
s = ""
for alphabet, index in enumerate(string):

    s = string[index] + string[index+1] + string[index+2] 
    if s == "MOO":
        count +=1
    


        
