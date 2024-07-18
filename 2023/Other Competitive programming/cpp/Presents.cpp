//4021420   Jul 4, 2013 7:30:15 PM	fuwutu	 136A - Presents	 GNU C++0x	Accepted	15 ms	0 KB
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, p;
    cin >> n;
    vector<int> f(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> p;
        f[p-1] = i+1;
    }
    for (int i = 0; i < n; ++i)
    {
        cout << f[i] << " ";
    }
    cout << endl;
    return 0;
}