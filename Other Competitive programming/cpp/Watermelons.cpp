#include <iostream>
using namespace std;
int numb;
int main(){
    cin >> numb;
    if(numb >= 1 && numb <= 100){
        if(numb%2 == 0 && numb != 2){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }
    else{
        return 0;
    }
}