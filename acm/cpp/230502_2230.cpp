#include <bits/stdc++.h>
using namespace std;

int arr[100001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    for (int i=0; i<N; i++)
    {
        cin >> arr[i];
    }
    sort(arr, arr+N);

    int en = 1;
    int MIN = 2e9+1;    
    for (int st=0; st<N; st++)
    {
        while (arr[en] - arr[st] < M) en++;
        if (en == N) break;
        MIN = min(MIN, arr[en] - arr[st]);
    }

    cout << MIN;
}