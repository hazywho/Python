MOD = 998244353
from numba import jit, int64
import numpy as np
from itertools import combinations

@jit(target_backend='cuda')  
def resultOfAllSubsets(N, K, A):
 
     # Initialize result
    # Find all combinations
    all_combinations = []

    for r in range(1, len(A) + 1):
        all_combinations += list(combinations(A, r))

    # Convert the combinations to lists
    all_combinations = [list(c) for c in all_combinations]

    result = 0
    # Print all combinations
    for c in all_combinations:
        result += sum(c) ** K
    result = result % MOD
 
    return result
@jit(target_backend = 'cude')
def run(N,K,A):
    N, K = 10, 2

    result = resultOfAllSubsets(N, K, A)
    print(result)
if __name__ == "__main__":
    N, K = 10, 2
    with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Python\subsets.txt") as f:
        for lines in f:
            A = list(map(int,lines.split(" ")))
    E = np.array(A)
    run(N,K,E)

