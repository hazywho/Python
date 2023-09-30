times = int(input())
count = 0
for r in range(times):
    key = input()
    key = key.replace("X", '')
    if key == "--":
        count -= 1
    if key == "++":
        count += 1

print(count)

