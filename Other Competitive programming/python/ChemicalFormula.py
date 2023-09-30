chem = "Al2(SO4)3·16H2O"
chem = chem+"1"
itemlist = []
if len(chem) < 25:
    for index,alphabets in enumerate(chem):
        try:
            int(alphabets)
        except ValueError:
            if alphabets.isupper():
                if chem[index+1].islower():
                    if alphabets+chem[index+1] not in itemlist:
                        itemlist.append(alphabets+chem[index+1])
                else:
                    if alphabets not in itemlist:
                        itemlist.append(alphabets)
    print(*itemlist)
    print(len(itemlist))
else:
    print("Invalid Length")