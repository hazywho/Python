#include <bits/stdc++.h>
using namespace std;
int a,times;
vector<char> str;
string s;
bool flag1;
int index;

int main(){
    cin >> a >> times;
    cin >> s;
    for(int i =0; i<a; i++){
        str.push_back(s[i]);
    }


    while(times--){
        flag1=false;
        index=0;
        while((index < a) && (flag1==false)){
            cout << str[index] << endl;
            if(str[index]=='B'){

                if(str[index+1]!='B'){
                    str[index+1]='B';
                    str[index]='G';
                    index ++;
                }
                else str[index]='B';
                }
            if(index+1 >= a) flag1=true;
            index++; 
            cout << index << endl;    
        }


        for(char x:str){cout << x;}
        cout << endl;
    }



}