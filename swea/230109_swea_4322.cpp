#include <stdio.h>
 
#define mm(a,b) a-b>0?a-b:0
 
int N;
int time[2][1000];
int now[5];
int tc;
char memo[11][12][12][12][12][1000];
   
void mysort(int arr[], int n) {
    int a[11] = { 0 };
    for (int i = 0; i < n; ++i) {
        a[arr[i]]++;
    }
    int p = 0;
    for (int i = 0; i < 11; ++i) {
        if (a[i]) {
            for (int j = 0; j < a[i]; ++j) {
                arr[p++] = i;
            }
        }
    }
}
   
bool divide(int p, int n, int t) {
    if (p == N) {
        return true;
    }
    //printf("tc:%d,%d ",tc, memo[now[0]][now[1]][now[2]][now[3]][now[4]][p]);
    //printf("now:%d %d %d %d %d\n", now[0], now[1],now[2],now[3], now[4]);
    if (memo[now[0]][now[1]][now[2]][now[3]][now[4]][p] == tc) {
        return false;
    }
    else {
        bool a, b;
        memo[now[0]][now[1]][now[2]][now[3]][now[4]][p] = tc;
        int tm = time[1][p] - t;
        int tp[5];
        for (int i = 0; i < n; ++i) {
            now[i] = mm(now[i], tm);
            tp[i] = now[i];
        }
        a = false;
        for (int i = 0; i < n; ++i) {
            if (now[i] + time[0][p] <= 10) {
                now[i] += time[0][p];
                mysort(now, n);
                b = divide(p + 1, n, time[1][p]);
                if (b) return b;
                for (int i = 0; i < n; ++i) {
                    now[i] = tp[i];
                }
            }
        }
        return a;
    }
}
   
int main() {
    int T;
    bool tf;
    int bst;
   
    scanf("%d", &T);
   
    tc = 1;
    for (; tc <= T; ++tc) {
        if (tc != 1) printf("\n");
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%d %d", &time[1][i], &time[0][i]);
        }
   
        for (int i = 0; i < 5; ++i) {
            now[i] = 11;
        }
        tf = false;
        for (int i = 1; i <= 5; ++i) {
            for (int j = 0; j < i; ++j) {
                now[j] = 0;
            }
            tf = divide(0, i, 0);
            if (tf) {
                bst = i;
                break;
            }
        }
        if (tf) printf("#%d %d", tc, bst);
        else printf("#%d -1", tc);
    }
    return 0;
}