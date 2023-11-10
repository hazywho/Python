#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k;
    fstream fin("C:/Users/zanyi/OneDrive/Git hub/Python/MCC/CPP/Teechu.txt");
    fin >> n >> k; 
    vector<int> elements(n - k);
    for (int &elem : elements)
        fin >> elem;
    sort(elements.begin(), elements.end());
    int maxCount = 0;
    for (int i = 0; i < (n - k) - 1; i++) {
        bool flag = false;
        int remainingMoves = k;
        int currentCount = 1;

        for (int j = i + 1; j < (n - k); j++) {
            if (elements[j] == (elements[j - 1] + 1)) {
                currentCount++;
            } else if (elements[j] == elements[j - 1]) {
                continue;
            } else if (remainingMoves > 0) {
                if (remainingMoves - (elements[j] - (elements[j - 1] + 1)) >= 0) {
                    remainingMoves -= (elements[j] - (elements[j - 1] + 1));
                    currentCount += (elements[j] - (elements[j - 1] + 1)) + 1;
                } else {
                    while (remainingMoves--) {
                        currentCount++;
                    }
                    break;
                }
            } else break;

            if (j == (elements.size() - 1))
                flag = true;
        }

        currentCount += max(0, remainingMoves);
        maxCount = max(maxCount, currentCount);

        if (flag) break;
    }
    cout << maxCount << endl;

    return 0;
}