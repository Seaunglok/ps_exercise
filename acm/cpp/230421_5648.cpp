#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll change(ll a)
{
    // cout << a << ' ';
    ll rtn = a % 10;
    a /= 10;

    while (a)
    {
        rtn *= 10;
        rtn += a % 10;
        a /= 10;
    }
    // cout << rtn << '\n';
    return rtn;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<ll> vec;
    vector<ll> sol;

    for (int i=0; i<N; i++)
    {
        ll num;
        cin >> num;

        vec.push_back(num);        
    }

    for (auto v : vec)
    {
        ll c = change(v);
        sol.push_back(c);
    }
    sort(sol.begin(), sol.end());

    for (auto s : sol)
    {
        cout << s << '\n';
    }
}