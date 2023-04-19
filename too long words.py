n = 4
words = ["word", "localization", "internationalization", "pneumonoultramicroscopicsilicovolcanoconiosis"]


for string in words:
    length = len(string)
    if length > 10:
        print(f"{string[:1].lower()}{length-2}{string[length-1:].lower()}")
    else:
        print(string)

