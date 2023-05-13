#include <bits/stdc++.h>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b)
{
    return a.first > b.first;    
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, C;
    cin >> N >> C;

    vector<pair<int, int>> vec;

    for (int i=0; i<N; i++)
    {
        int num;
        cin >> num;
        bool check = false;
        for (auto &v : vec)
        {
            if (v.second == num)
            {
                check = true;
                v.first++;
                break;
            }
        }
        if (!check) vec.push_back({1, num});
        
    }
    
    stable_sort(vec.begin(), vec.end(), cmp);

    for (auto v : vec)
    {
        for (int i=0; i<v.first; i++)
            cout << v.second << ' ';
    }
}