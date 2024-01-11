#include <bits/stdc++.h>

using namespace std;

int main()
{
    fstream fin ("innocation.txt");

    int n, m;
    fin >> n >> m;

    map<long long, vector<long long>> a;
    vector<pair<long long, long long>> ab(n);
    for(int i = 0; i < n; i++)
    {
        a[i] = vector<long long>(4);
        for(long long &j : a[i])
            fin >> j;

        ab[i] = {i, a[i][0] + a[i][1]};
    }

    sort(ab.begin(), ab.end(), [] (pair<long long, long long> x, pair<long long, long long> y)->bool {
        return x.second > y.second;
    });

    vector<vector<long long>> vals(m);
    for(int i = 0; i < (m-1); i++)
    {
        vals[i] = a[ab[i].first];
        a.erase(ab[i].first);
    }

    int pos = 0, mx = -1;
    for(pair<long long, vector<long long>> i : a)
    {
        int sum = i.second[0] + i.second[1] + i.second[2] + i.second[3];
        if(sum > mx)
        {
            pos = i.first;
            mx = sum;
        }
    }

    vals[m-1] = a[pos];

    long long largestCDsum = 0, ans = 0;
    for(vector<long long> i : vals)
    {
        ans += i[0] + i[1];
        largestCDsum = max(largestCDsum, i[2]+i[3]);
    }

    cout << ans + largestCDsum << endl;

    return 0;
}