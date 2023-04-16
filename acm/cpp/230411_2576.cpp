#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr;
    int num;

    for (int i=0; i<7; i++)
    {
        cin >> num;
        if (num % 2 != 0)
        {
            arr.push_back(num);
        }    
    }
    if (arr.size() == 0)
    {
        cout << "-1";
        return 0;
    }
    cout << accumulate(arr.begin(), arr.end(), 0) << '\n';
    cout << *min_element(arr.begin(), arr.end());
}