#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int mian(){
    int i;
    cin >> i;
    vector<int> gifts(i);
    for(int&num:gifts){
        cin >> num;
    }
    int half = int(gifts.size()/2);
    for(int i = 0; i<half; i++){
        cout << gifts[i] << " ";
    }
    if(gifts.size()%2!=0){
        cout << gifts[(gifts.size()-1)/2] <<  " ";
    }
    for(int last = gifts.size(); last<half; last--){
        cout << gifts[last] << " ";
    }
    cout << endl;
}