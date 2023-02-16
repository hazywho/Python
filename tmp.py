coord = [1, 2, 3]
clearness = [7, 11, 10]

clearest = 0
i = 0
while i < len(clearness):
    if clearness[i] > clearness[clearest]:
        print(f"{clearness[i]} is larger than {clearness[clearest]}")
        clearest = i
    else:
        print(f"{clearness[i]} <= {clearness[clearest]}")
    
    i += 1

print(coord[clearest])