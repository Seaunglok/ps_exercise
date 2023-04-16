#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    vector<int> arr;
    int cost;
    for (int i=0; i<N; i++)
    {
        cin >> cost;
        arr.push_back(cost);
    }

    int young = 0;
    int min = 0;    
    for (auto a : arr)
    {
        young += int(a / 30) + 1;
        min += int(a / 60) + 1;
    }
    young *= 10;
    min *= 15;
    
    if (young < min)
    {
        cout << "Y " << young;
    }
    else if (young > min)
    {
        cout << "M " << min;
    }
    else
    {
        cout << "Y M " << young;
    }
}