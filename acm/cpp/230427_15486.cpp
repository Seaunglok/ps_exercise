#include <bits/stdc++.h>
using namespace std;

vector<pair<int, int>> vec;
int dp[1500002];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        int a, b;
        cin >> a >> b;
        vec.push_back({a, b});
    }

    int sol = 0;
    int current = 0;
    for (int i=0; i<=N; i++)
    {
        current = max(current, dp[i]);
        if (i+dp[i+vec[i].first] > N) continue;
        dp[i+vec[i].first] = max(current+vec[i].second, dp[i+vec[i].first]);
        sol = max(sol, dp[i+vec[i].first]);
    }   

    cout << sol;   

}

