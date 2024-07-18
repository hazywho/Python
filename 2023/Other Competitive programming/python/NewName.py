string =["^______^","___^_^^^_^___^","^_","^","^_^^^^^_^_^^","___^^","_"]


for cases in string:
    count = 0
    if cases[0] != "^":
        count +=1
    if cases [-1] != "^":
        count +=1
    if cases.count("_") + cases.count("^") == 1 and cases[0] == "^":
        count +=1

    for i in range(1, len(cases)-1):
        if cases[i] == "_"  and cases[i-1] != "^":
            count += 1
    print(count)




