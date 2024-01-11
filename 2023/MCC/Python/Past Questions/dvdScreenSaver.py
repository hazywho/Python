Q = 4
H = [3, 2, 7, 36]
W = [5, 2, 2, 28]
T = [5, 5, 0, 127]
for i in range(1):
    matric = []
    largem = []
    for _ in range(W[i]):
        matric.append(0)
    for _ in range(0,H[i]):
        largem.append(matric.copy())
largem[len(H)-2][0] = 1
print(largem)
    
