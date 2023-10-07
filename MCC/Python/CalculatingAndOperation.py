x = 20
bit16 = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
bits = []
for l in range(x):
    for each in bit16:
        if x>each:
            x -= each
            bits.append[int(each)]