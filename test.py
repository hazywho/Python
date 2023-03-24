string = "oomooomoomoo"
front = 0
back = 3

while back <= len(string):
    clause = string[front:back]
    if clause == "moo":
        print("true")
        
    else:
        print("flase")
    front = front + 1
    back = back + 1
    print(clause)
        
    