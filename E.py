import math
N = 10
A = [1,3,3,4,5,5,4,3,3,2]
B = [33,0,0,0,0,0,0,0,0,0]
times = 0





while A != B :

    for pos,x in enumerate(A):
        print(A)
        if x > B[pos]:
            A[pos] = A[pos]-1
            times +=1
        elif x < B[pos]:
            A[pos] = A[pos]+1
        else:
            pass
print(times)

