#include <bits/stdc++.h>

using namespace std;

int c = 0;

int getArea(vector<pair<int, int>> sz)
{
    int ans = 0;
    for(pair<int, int> i : sz)
        ans += i.first*i.second;

    return ans;
}

pair<int, int> getNewSz(pair<int, int> a, pair<int, int> b)
{
    return {max(a.first, b.first), (a.second + b.second)};
}

int findMinArea(const vector<pair<int, int>> sz, int k, int starting = 0, int index = 0,
            vector<pair<int, int>> subset = {}, int minArea = INT_MAX)
{
    try
    {
        if(k == 0)
        {
            minArea = min(minArea, getArea(subset));
        }
        else if(k == 1)
        {
            for(int i = starting; i < sz.size(); i++)
                subset.at(subset.size()-1) = getNewSz(subset.at(subset.size()-1), sz[i]);

            minArea = min(minArea, findMinArea(sz, 0, 0, 0, subset, minArea));
        }
        else
        {
            for(int i = starting, c = 1; i < (sz.size() - k + 1); i++, c++)
            {
                subset.at(index) = getNewSz(sz[i], subset.at(index));
                minArea = min(minArea, findMinArea(sz, k-1, starting+c, index+1, subset, minArea));
            }
        }
    }
    catch(exception err)
    {
        cout << "error" << endl;
        cerr << err.what();
        cout << endl;

        terminate();
    }

    return minArea;
}

int main()
{
    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> sz(n);
    for(pair<int, int> &i : sz)
        cin >> i.first >> i.second;

    vector<pair<int, int>> subset(k, {0, 0});

    cout << findMinArea(sz, k, 0, 0, subset) << endl;

    return 0;
}