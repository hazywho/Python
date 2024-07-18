first = input().split(" ")
cost = int(first[0])
savings = int(first[1])
wanted = int(first[2])
moneyneeded = 0
for x in range(1,wanted+1):
    moneyneeded += cost*x
needed = savings-moneyneeded
if needed >=0:
    print(0)
else:
    print(abs(needed))