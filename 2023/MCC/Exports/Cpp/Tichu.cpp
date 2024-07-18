#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,k;
    fstream fin("C:/Users/zanyi/OneDrive/Git hub/Python/MCC/Real/techu.txt");
    fin >> n >> k; 
    vector<int> c(n-k);
    for(int&i:c)
        fin >> i;
    sort(c.begin(),c.end());
    int ans=0;
    for(int i = 0; i< (n-k)-1; i++){
        bool flag = false;
        int tmp = k, count = 1;

        for(int j = i+1; j< (n-k); j++){
            if(c[j]==(c[j-1]+1)){
                count ++;
            }
            else if(c[j]==c[j-1]){
                continue;
            }
            else if(tmp>0)
            {
                if(tmp-(c[j]-(c[j-1]+1))>=0){
                    tmp -= (c[j]-(c[j-1]+1));
                    count += (c[j]- (c[j-1]+1))+1;
                }
                else{
                    while(tmp--){
                        count++;
                    }
                    break;
                }
            }
            else break;

            if(j==(c.size()-1))
                flag = true;

        }

        count += max(0,tmp);
        ans = max(ans,count);

        if(flag) break;
    }
    cout << ans << endl;

    return 0;
}