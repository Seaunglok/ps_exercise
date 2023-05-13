#include <bits/stdc++.h>
using namespace std;

bool cmp(string &A, string &B)
{
    int lena, lenb, suma=0, sumb=0;
    lena = A.size(), lenb = B.size();

    if (lena != lenb)     
        return lena < lenb;

    for (auto a : A)        
        if (isdigit(a)) suma += a-'0';
        
    for (auto b : B)
        if (isdigit(b)) sumb += b-'0';

    if (suma != sumb)
    {
        return suma < sumb;        
    }
    return A < B;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    string str;
    vector<string> vec;

    for (int i=0; i<N; i++)
    {
        cin >> str;
        vec.push_back(str);
    }
    sort(vec.begin(), vec.end(), cmp);
    
    for (auto v : vec)
    {
        cout << v << '\n';
    }
}