#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> arr;
    int num;

    for (int i=0; i<5; i++)
    {
        cin >> num;
        arr.push_back(num);
    }
    sort(arr.begin(), arr.end());

    int sum = accumulate(arr.begin(), arr.end(), 0);
    cout << int(sum/5) << "\n";
    cout << arr[2];

}