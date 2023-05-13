#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    string str;
    int input;

    queue<int> que;

    for (int i=0; i<N; i++)
    {
        cin >> str;
        if (str == "push")
        {
            cin >> input;
            que.push(input);
            continue;
        }
        else if(str == "pop")
        {
            if (!que.empty())
            {
                cout << que.front();
                que.pop();
            }
            else            
                cout << -1;
            
        }
        else if(str == "size")
        {
            cout << que.size();
        }
        else if (str == "empty")
        {
            if (que.empty())            
                cout << 1;            
            else 
                cout << 0;            
        }
        else if (str == "front")
        {
            if (!que.empty())            
                cout << que.front();
            else
                cout << -1;           
        }
        else if (str=="back")
        {
            if (!que.empty())
                cout << que.back();
            else
                cout << -1;
        }      
        cout << '\n';  
    }
}