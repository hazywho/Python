#include <iostream>
using namespace std;
int layers,x1,x2,x3,counts = 0;
int main(){
    cin >> layers;
    for(int i = 0; i < layers; i++){
        cin >> x1 >> x2 >> x3;
        int total = x1+x2+x3;
        if(total >= 2){
            counts +=1;
        }
    }
    cout << counts << endl;
}