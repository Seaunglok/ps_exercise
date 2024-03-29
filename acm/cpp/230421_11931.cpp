#include <bits/stdc++.h>
using namespace std;

bool cmp(int a, int b)
{
    return a > b;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> vec;
    for (int i=0; i<N; i++)
    {
        int num;
        cin >> num;
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end(), cmp);

    for (auto v : vec)
    {
        cout << v << '\n';
    }
}