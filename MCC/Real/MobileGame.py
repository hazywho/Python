x = int(input())
for _ in range(x):
    n,a,b = list(map(int,input().split()))
    enemies = list(map(int,input().split()))
    enemies.sort()
    count = 0  
    while a<b and n>0:
        while enemies[0] <a:
            last = enemies[0]
            enemies.pop(0)
        enemies.append(last)
        if a<enemies[0]:
            print(-1)
            break
        else:
            a += enemies[0]
            enemies.pop(0)
            count +=1
    print(count)

