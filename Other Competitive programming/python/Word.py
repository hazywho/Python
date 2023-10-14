first = input()
uppered = first.upper()
count = 0
rcount = 0
for i in range(len(first)):
    if uppered[i] == first[i]:
        count += 1
    else:
        rcount += 1
if count > rcount:
    print(first.upper())
else:
    print(first.lower())