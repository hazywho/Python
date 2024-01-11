#include <iostream>
using namespace std;
#include <string>

string input;

int main(){
    cin >> input;
    int length = input.length();
    if(length > 10){
        cout << tolower(input[0]) << length-2 << input[length-1] << endl;
    }
    else{
        cout << input << endl;
    }
}