n = int(input())
words = []
for times in range(n):
    words.append(input())



for string in words:
    length = len(string)
    if length > 10:
        print(f"{string[:1].lower()}{length-2}{string[length-1:].lower()}")
    else:
        print(string)

