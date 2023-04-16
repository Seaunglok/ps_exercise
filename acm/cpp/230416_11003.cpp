#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, L;
    cin >> N >> L;

    vector<int> vec;
    int num;
    for (int i=0; i<N; i++)
    {
        cin >> num;
        vec.push_back(num);
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> sol;
    for (int i=0; i<N; i++)
    {
        pq.push({vec[i], i});

        while (!pq.empty() && pq.top().second < i-L+1)
        {
            // cout << pq.top().first << ' ' << pq.top().second << '\n';
            pq.pop();
        }            
        
        sol.push_back(pq.top().first);
        
    // }
    }
    for (auto s: sol)
    {
        cout << s << ' ';
    }
}