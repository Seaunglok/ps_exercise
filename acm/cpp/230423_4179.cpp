#include <bits/stdc++.h>
using namespace std;

vector<string> vec;
queue<pair<int, int>> que_fire;
queue<pair<int, int>> que_ji;
int visit_fire[1001][1001];
int visit_ji[1001][1001];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    string str;
    for (int i=0; i<N; i++)
    {
        cin >> str;
        vec.push_back(str);
    }

    for (int r=0; r<N; r++)
    {
        for (int c=0; c<M; c++)
        {
            if (!visit_fire[r][c] && vec[r][c] == 'F')
            {
                que_fire.push({r, c});
                visit_fire[r][c] = 1;
            }
            if (!visit_ji[r][c] && vec[r][c] == 'J')
            {
                que_ji.push({r, c});
                visit_ji[r][c] = 1;
            }
            // cout << vec[r][c] << ' ';
        }
    }

    pair<int, int> move[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    while (!que_fire.empty())
    {
        pair<int, int> now = que_fire.front(); que_fire.pop();
        for (auto mv : move)
        {
            int nr = now.first + mv.first;
            int nc = now.second + mv.second;
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (visit_fire[nr][nc] || vec[nr][nc] == '#') continue;
            que_fire.push({nr, nc});
            visit_fire[nr][nc] = visit_fire[now.first][now.second] + 1;
        }
    }

    while (!que_ji.empty())
    {
        pair<int, int> now = que_ji.front(); que_ji.pop();
        for (auto mv : move)
        {
            int nr = now.first + mv.first;
            int nc = now.second + mv.second;
            // cout << nr << ' ' << nc << '\n';

            if (nr < 0 || nr >= N || nc < 0 || nc >= M)
            {
                cout << visit_ji[now.first][now.second];
                return 0;
            }
            if (visit_ji[nr][nc] || vec[nr][nc] == '#') continue;
            if (visit_ji[now.first][now.second] + 1 >= visit_fire[nr][nc] && visit_fire[nr][nc]) continue;
            que_ji.push({nr, nc});
            visit_ji[nr][nc] = visit_ji[now.first][now.second] + 1;            
        }
    }

    cout << "IMPOSSIBLE";
}