#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n)
{
    if (n == 1) return 0;
    for (int i=2; i*i<=n; i++)
    {
        if (n%i == 0) return 0; 
    }
    return 1;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    int sol=0;

    for (int i=0; i<N; i++)
    {
        int num;
        cin >> num;
        sol += isPrime(num);
    }

    cout << sol;

}