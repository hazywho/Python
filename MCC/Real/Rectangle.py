# rectangle:
# get total base 
# get total height 
# base * height 
# YOU WILL GET TOTAL AREA
# rectangle base *rectangle height = rectangle area
# total area - sum of all rectangle area = 

height = []
width = []
maxheight= []
maxwidth = []
n,k = list(map(int,input().split()))
for _ in range(n):
    h,w = list(map(int,input().split()))
    height.append(h)
    width.append(w)
def doesnt_repeat(n):
    if n not in maxheight:
        return n
    else:
        return 0
def doesnt_repeat_W(n):
    if n not in maxwidth:
        return n
    else:
        return 0
for i in range(k):
    maxheight.append(max(height,key=doesnt_repeat))
    maxwidth.append(max(width,key=doesnt_repeat_W))
print(maxheight)
print(maxwidth)
