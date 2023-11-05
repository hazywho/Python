
from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer   
from itertools import combinations
 
# normal function to run on cpu
@jit(target_backend='cuda')
def func(A):
    all_combinations =  []                                
    for r in range(1, len(A) + 1):
        all_combinations += list(combinations(A, r))
    # Convert the combinations to lists
    all_combinations = [list(c) for c in all_combinations]    
    return all_combinations
# function optimized to run on gpu  
@jit(target_backend='cuda')                        
def add(lst,k):
    result = 0
    # Print all combinations
    for c in lst:
        result += sum(c) ** k
    result = result % 998244353
    return result
if __name__=="__main__":                        
    k = 2
    with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\subsets.txt") as f:
        for lines in f:
            a = list(map(int,lines.split(" ")))
    start = timer()
    set = func(a)
    ans = add(set,k)
    print(ans)
    print("with GPU:", timer()-start)    