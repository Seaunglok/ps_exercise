#include <bits/stdc++.h>
using namespace std;

int arr[2000001];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;    
    cin >> N;
    for (int i=0; i<N; i++)
    {
        int num;
        cin >> num;
        arr[num+1000000]++;
    }
    for (int i=0; i<2000001; i++)
    {
        while (arr[i]--)
        {
            cout << i-1000000 << '\n';
        }
    }
}