#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> vec;
    for (int i=0; i<N; i++)
    {
        int num;
        cin >> num;

        vec.push_back(num);
    }
    sort(vec.begin(), vec.end());

    int sol=0;
    for (int i=1; i<=N; i++)
    {
        sol = max(sol, vec[N-i]*i);
    }
    cout << sol;
}