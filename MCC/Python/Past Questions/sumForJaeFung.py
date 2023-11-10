x =  open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\Past Questions\gyat.txt","r").readlines()
n,k = list(map(int,x[0].split(" ")))
number = list(map(int,x[1].split(" ")))
a = 0
for i in number:
    p = i
    for _ in range(k):
        p = (p/2 if p%2==0 else 3*p+1)
    a+=p
print(int(a))  