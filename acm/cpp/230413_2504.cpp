#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    string str;
    cin >> str;

    int sum = 0;
    int temp = 1;
    vector<char> vec;
    char last;

    for (auto c : str)
    {
        if (c == '(')
        {
            vec.push_back(c);
            temp *= 2;
        }
        else if (c == '[')
        {
            vec.push_back(c);
            temp *= 3;
        }
        else if (c == ')')
        {
            if (vec.empty() || vec.back() != '(')
            {
                cout << 0;
                return 0;
            }
            if (last == '(')
            {                    
                sum += temp;                    
            }
            vec.pop_back(); 
            temp /= 2; 
        }
        else if (c == ']')
        {
            if (vec.empty() || vec.back() != '[')
            {
                cout << 0;
                return 0;
            }
            if (last == '[')
            {                    
                sum += temp;                    
            }
            vec.pop_back();
            temp /= 3;  
        }
        last = c;
        // for (auto v : vec)
        // {
        //     cout << v << '\n';
        // }         
        // cout << sum << ' ' << temp << '\n';
    }
    if (vec.empty()) cout<<sum;
    else cout << 0;
}