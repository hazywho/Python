f = input()
l = list(map(int,input().split(" ")))
nl = list(dict.fromkeys(l).keys())
nl.sort()
if len(nl) < 3:
    print("-1 -1 -1")
else:
    print(f"{nl[2]} {nl[1]} {nl[0]}")