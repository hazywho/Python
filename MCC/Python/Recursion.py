import math

def is_prime(n):
  for i in range(2,n):
    if (n%i==0):
      return False
  return True

def prime(n, div):
  if n!=1:
    if n%div==0:
      print(div, end=" ")
      prime(int(n/div), div)
    else:
      for i in range(div+1, n+1):
        if is_prime(i):
          prime(n,i)
          break

n = 29
prime(n,2)
print()
