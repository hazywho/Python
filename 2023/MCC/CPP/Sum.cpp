#include <iostream>
using namespace std;
int y;
int z;
unsigned long long x = 0;
int main(){
    cin >> y;
    for(int i = 0; i<y; i++){
        cin >> z;
        x+=z;
    }
    cout << x << endl; 
}