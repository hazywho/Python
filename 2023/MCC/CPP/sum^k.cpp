#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

const long MOD = 998244353;
fstream fin("sum^ke.txt");

// Function to calculate the sum of scores for all non-empty subsets
unsigned long long sum_of_subsets(long N, long K, vector<long long>& A) {
    unsigned long long result = 0;

    for (long bitmask = 1; bitmask < (1 << N); bitmask++) {
        unsigned long long subset_sum = 0;

        for (long i = 0; i < N; i++) {
            if (bitmask & (1 << i)) {
                subset_sum += A[i];
            }
        }

        result = (result + (subset_sum * subset_sum) % MOD)% MOD;
    }

    return result;
}

int main() {
    long N, K;
    fin >> N >> K;

    vector<long long> A(N);
    for (long i = 0; i < N; i++) {
        fin >> A[i];
    }

    unsigned long long result = sum_of_subsets(N, K, A);
    cout << result << endl;

    return 0;
}