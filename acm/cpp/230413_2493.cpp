#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    stack<pair<int, int>> st;
    vector<int> sol;
    int height;
    st.push(make_pair(100000001, 0));

    for (int i=1; i<=N; i++)
    {
        cin >> height;

        while (st.top().first < height)
        {            
            st.pop();
        }
        sol.push_back(st.top().second);
        st.push(make_pair(height, i));
    }

    for (auto s : sol)
    {
        cout << s << ' ';
    }
}