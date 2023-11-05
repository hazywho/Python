#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> log;
int main() {
    int t, n ,a, b;
    cin >> t;
    while (t--) {
        cin >> n >> a >> b;
        vector<int> enemylvl(n);
        for(int &i : enemylvl)
            cin >> i;
        sort(enemylvl.begin(), enemylvl.end());
        int count = 0;
        bool valid = true;
        while (a < b && enemylvl.size() > 0) {
            int i;
            for ( i = 0; (enemylvl[i] < a) && (i < enemylvl.size()); i++);
            i--;
            if(i == -1) {
                valid = false;
                break;
            }

            a += enemylvl[i];
            enemylvl.erase(enemylvl.begin()+i);
            count++;

        }
        if(!valid)
        {
            log.push_back(-1);
            continue;
        } 
        if (a < b) {
            log.push_back(-1);
        } else {
            log.push_back(count);
        }
    }
    for(auto h:log){
            cout << h << endl;
    }
    
    return 0;
}