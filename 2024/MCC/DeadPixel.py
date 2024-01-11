# 8 8 0 0
a,b,x,y = list(map(int,input().split()))
point=[x+1,y+1]
matrix_size=[a,b]
white_area = matrix_size[0]*matrix_size[1]

if matrix_size[0] <=2 and matrix_size[1] <= 2:
    finalvalue=int((matrix_size[0]*matrix_size[1])/2)
elif matrix_size[0] <= 2:
    finalvalue=point[1]*matrix_size[0]
elif matrix_size[1] <= 2:
    finalvalue=point[0]*matrix_size[1]

first = max(abs(white_area-finalvalue),abs(finalvalue-white_area))
print(first)