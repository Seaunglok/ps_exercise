#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    string str;
    int sol = 0;

    for (int i=0; i<N; i++)
    {
        cin >> str;
        stack<char> st;
        for (auto s: str)
        {
            if (!st.empty() && st.top() == s)
            {
                st.pop();                
            }
            else
            {
                st.push(s);
            }
        }
        if (st.empty()) sol++;
    }
    
    cout << sol;
}