x = int(input())
for _ in range(x):
    n,a,b = list(map(int,input().split()))
    enemies = list(map(int,input().split()))
    enemies.sort()
    count = 0  
    while enemies[0] <a:
        last = enemies[0]
        enemies.pop(0)
    enemies.insert(0,last)
    print(enemies)

    for _ in range(n):
        if a<=enemies[0]:
            print(-1)
            break
        elif a>enemies[0]:
            a+=enemies[0]
            for d,i in enumerate(enemies):
                
                count+=1
            print(enemies)
        print(count)


