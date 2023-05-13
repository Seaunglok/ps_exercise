#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;

    int x, y;
    vector<int> arr = {0, 1, 2, 3};
    for (int i=0; i<N; i++)
    {
        cin >> x >> y;
        swap(arr[x], arr[y]);
    }
    auto sol = find(arr.begin(), arr.end(), 1);

    cout << sol - arr.begin();

}