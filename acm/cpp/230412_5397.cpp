#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    
    for (int i=0; i<N; i++)
    {
        string A;
        cin >> A;

        list<char> Arr = {};
        auto cnt = Arr.begin();

        for (auto a : A)
        {
            // cout << a << ' ' << cnt << '\n';
            if (a == '<')
            {
                if (cnt != Arr.begin())                
                    cnt--;
                
            }
            else if (a == '>')
            {
                if (cnt != Arr.end())
                    cnt++;
            }
            else if (a == '-')
            {
                if (Arr.empty()) continue;
                if (cnt != Arr.begin())
                {
                    cnt--;
                    cnt = Arr.erase(cnt);    
                }                
            }
            else
            {
                Arr.insert(cnt, a);
            
            }
            // cout << "cnt: " << cnt << '\n';
        }

        for (auto v : Arr)
        {
            cout << v;
        }
        cout << '\n';

    }
}