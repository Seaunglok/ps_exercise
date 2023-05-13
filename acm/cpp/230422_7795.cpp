#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int t=0; t<T; t++)
    {
        int N, M;
        cin >> N >> M;

        vector<int> A;
        vector<int> B;
        vector<pair<int, int>> V;

        for (int i=0; i<N; i++)
        {
            int num;
            cin >> num;
            V.push_back({num, 0});
            A.push_back(num);
        }
        for (int i=0; i<M; i++)
        {
            int num;
            cin >> num;
            V.push_back({num, 1});
            B.push_back(num);
        }
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        sort(V.begin(), V.end());

        for (auto v : V)
        {
            cout << v.first << ' ' << v.second << '\n';
        }

        int sol=0;

        for (auto a : A)
        {
            for (auto b : B)            
                if (a > b)
                {
                    // cout << a << ' ' << b << '\n';
                    sol++;
                }
                else break;
            
        }
        cout << sol << '\n';
    }
}