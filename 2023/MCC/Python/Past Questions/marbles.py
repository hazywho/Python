N = 20
A = [10, 12, 5, 8, 5, 6, 6, 8, 5, 4, 4, 5, 9, 9, 10, 9, 9, 6, 7, 8]
B = [3, 9, 3, 11, 11, 3, 6, 9, 3, 6, 9, 9, 11, 8, 6, 8, 7, 7, 12, 4]
count = 0

while A != B :
    for index in range(N-1):
        while A[index] > B[index]:
            A[index] = A[index]-1
            A[index+1] = A[index+1]+1
            count +=1
        while A[index] < B[index]:
            A[index] = A[index]+1
            A[index+1] = A[index+1]-1
            count += 1
print(count)

