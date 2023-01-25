#include<iostream>
//#include <cstdio>
 
 
struct Box {
    int x{}, y{}, z{};
};
 
constexpr int XY{ 0 }, YZ{ 1 }, ZX{ 2 };
 
int N;
Box box[20];
 
int dp[20][3][21];
bool visited[20];
 
using namespace std;
 
int maxHeight = 0;
 
void clear() {
    fill(&dp[0][0][0], &dp[0][0][0] + 20 * 3 * 21, 0);
    fill(&visited[0], &visited[0] + 20, false);
    maxHeight = 0;
}
 
inline int getX(const Box& b, const int f) {
    return f == XY ? b.x : (f == YZ ? b.y : b.z);
}
inline int getY(const Box& b, const int f) {
    return f == XY ? b.y : (f == YZ ? b.z : b.x);
}
 
inline int getHeight(const Box& b, const int f) {
    return f == XY ? b.z : (f == YZ ? b.x : b.y);
}
 
inline bool stackable(const int b1_x, const int b1_y, const int b2_x, const int b2_y) {
    return (b1_x >= b2_x && b1_y >= b2_y) || (b1_x >= b2_y && b1_y >= b2_x);
}
 
bool stackable(const Box& b1, const int f1, const Box& b2, const int f2) {
    const int b1_x = getX(b1, f1);
    const int b1_y = getY(b1, f1);
    const int b2_x = getX(b2, f2);
    const int b2_y = getY(b2, f2);
    bool result = stackable(b1_x, b1_y, b2_x, b2_y);
    return result;
    //return stackable(b1_x, b1_y, b2_x, b2_y);
}
 
void dfs(int boxBottom, int boxX, int boxY, int boxSide, int numStack, int height) {
    if (height > maxHeight) maxHeight = height;
    if (numStack == N) return;
    if (dp[boxBottom][boxSide][numStack] > height) return;
    dp[boxBottom][boxSide][numStack] = height;
 
    for (int i = 0; i < N; i++) {
        if (visited[i])
            continue;
        visited[i] = true;
        if (stackable(box[i].x, box[i].y, boxX, boxY))
            dfs(i, box[i].x, box[i].y, XY, numStack + 1, height + getHeight(box[i], XY));
        if (stackable(box[i].y, box[i].z, boxX, boxY))
            dfs(i, box[i].y, box[i].z, YZ, numStack + 1, height + getHeight(box[i], YZ));
        if (stackable(box[i].z, box[i].x, boxX, boxY))
            dfs(i, box[i].z, box[i].x, ZX, numStack + 1, height + getHeight(box[i], ZX));
        visited[i] = false;
    }
}
 
void solve() {
    clear();
    dfs(0, 0, 0, XY, 0, 0);
     
}
 
int main(int argc, char** argv)
{
    int test_case;
    int T;
    int ans[50]{};
    FILE* f;
    //freopen_s(&f, "input.txt", "r", stdin);
    cin >> T;
    /*
       여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    */
    for (test_case = 1; test_case <= T; ++test_case)
    {
        cin >> N;
        /////////////////////////////////////////////////////////////////////////////////////////////
        /*
             이 부분에 여러분의 알고리즘 구현이 들어갑니다.
         */
         /////////////////////////////////////////////////////////////////////////////////////////////
        for (int i = 0; i < N; i++) {
            cin >> box[i].x >> box[i].y >> box[i].z;
        }
 
        solve();
        ans[test_case - 1] = maxHeight;
    }
    for (int i = 0; i < T; i++) {
        cout << "#" << i + 1 << " " << ans[i] << endl;
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}