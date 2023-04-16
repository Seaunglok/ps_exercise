#include <bits/stdc++.h>
using namespace std;


int arr[10] = {0, };    
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string N;
    cin >> N;

    for (auto a : N)
    {
        arr[a-'0']++;
    }

    int sol = 0;
    for (int i=0; i<10; i++)
    {
        if (i == 6 || i == 9) continue;
        sol = max(sol, arr[i]);
    }
    sol = max(sol, (arr[6]+arr[9]+1)/2);

    cout << sol;

}