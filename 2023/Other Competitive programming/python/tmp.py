coord = [1, 2, 3, 4]
clearness = [7, 11, 10, 40]

i2 = 0 
i = 0





for i in range(len((clearness))):
    
    if clearness[i] > clearness[i2]:
        print(f"{clearness[i]} is larger than {clearness[i2]}")
        i2 = i
    
print(coord[i2])

