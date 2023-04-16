#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    long long num;
    stack<long long> st;
    long long sol=0;

    for (int i=0; i<N; i++)
    {
        cin >> num;

        while (!st.empty() && st.top() <= num)
        {
            st.pop();
        }
        sol += st.size();
        st.push(num);
    }
    cout << sol;
}