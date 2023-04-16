#include <bits/stdc++.h>
using namespace std;

int arr[2][7];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, K;
    cin >> N >> K;
    
    int a, b;
    for (int i=0; i<N; i++)
    {
        cin >> a >> b;
        arr[a][b]++;
    }

    int ans = 0;
    for (int i=0; i<2; i++)    
    {
        for (int j=1; j<7; j++)
        {   
            // cout << arr[i][j] / K << " " << arr[i][j] % K << '\n';         
            ans += arr[i][j] / K;
            if (arr[i][j] % K)
            {
                ans++;
            }
        }
    }
    cout << ans;
}