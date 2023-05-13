#include <bits/stdc++.h>
using namespace std;

int arr[100001];
int check[100001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cin >> arr[i];
    }

    long long sol = 0;
    int en = 0;
    for (int st=0; st<N; st++)
    {        
        
        while (en < N && !check[arr[en]])
        {            
            check[arr[en]] = 1;            
            en++;
        }
        sol += en - st;
        check[arr[st]] = 0;
    }

    cout << sol;
}