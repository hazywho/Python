alphabets = {
 "b":2,
 "c":3,
 "e":5,
 "g":7,
 "k":11,
 "m":13,
 "q":17,
 "s":19,
 "w":23,
}
numb = 0
words = input()
words = words.lower()

if len(words) < 100:
    for letter in words:
        if letter in alphabets:
            numb += alphabets[letter]
    print(numb)
else:
    print("Invalid Length")