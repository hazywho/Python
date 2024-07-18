m = input()
l = input()
count = 0
for i in l:
    if i == "A":
        count += 1
    else:
        count -= 1
if count == 0:
    print("Friendship")
elif count > 0:
    print("Anton")
else:
    print("Danik")