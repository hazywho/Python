#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
vector<int> l;
int n, m, x;
long long counts;
int main(){
    cin >> n >> m;
    for(int i = 0; i<n; i++){
        cin >> x;
        l.push_back(x);
        sort(l.begin(), l.end());
    }

    for(int n=0; n<m; n++){
        if(l[n]<=0){
            counts -= l[n];
        }
    }
    cout << counts << endl; 
}
