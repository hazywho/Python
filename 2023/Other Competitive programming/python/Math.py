cases = int(input())
matrix = []
steps = 0
for i in range(0,cases):
    msize = int(input())
    matrix = [[None]*msize for _ in range(msize)]
    for y in range(msize):
        line = input()
        for x in range(msize):
            matrix[y][x] = line[x]
    

    #calculation

    x = 0
    y = 0
    while x < msize and y < msize:
        try:
            if matrix[y][x+1] == '.':
                x += 1
                continue
            if matrix[y+1][x] == '.':
                y += 1
                continue
            if x > 4 or y > 4:
                 steps += 1
                 print(steps)
                 break
        except IndexError:
            break