def set_op(set):
  x = len(set)
  for i in range(2**x):
        for j in range(x):
            if (i & (2**j)):
                print([j])


n = int(input())
set_op(range(1,n+1))

print()