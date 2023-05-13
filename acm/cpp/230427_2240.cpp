#include <bits/stdc++.h>
using namespace std;

int a[1002];
int dp[1001][31][3];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T, W;
    cin >> T >> W;

    for (int i=1; i<=T; i++)
    {        
        cin >> a[i];        
    }    

    int sol = 0;
    for (int i=1; i<=T; i++)
    {
        dp[i][0][1] = dp[i-1][0][1] + (a[i]==1);
        for (int j=1; j<=W; j++)
        {
            // if (i<j) break;
            dp[i][j][1] = max(dp[i-1][j-1][2], dp[i-1][j][1]) + (a[i]==1);
            dp[i][j][2] = max(dp[i-1][j-1][1], dp[i-1][j][2]) + (a[i]==2);
            
            sol = max({sol, dp[i][j][1], dp[i][j][2]});
        }
    }
    cout << sol;


}