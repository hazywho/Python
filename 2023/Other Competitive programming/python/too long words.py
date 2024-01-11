# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis

# Input 
# The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. 
# All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

# Output
# Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

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

