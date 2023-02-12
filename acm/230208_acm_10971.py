N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = []
check = [0] * N
rtn = 10**9 
def dfs(idx, start, cost):
    global rtn
    if idx == N-1 and mat[start][0] != 0:
        rtn = min(rtn, cost+mat[start][0])
        return
    for i in range(N):
        if check[i]: continue
        if mat[start][i] == 0: continue
        check[i] = 1
        dfs(idx+1, i, cost+mat[start][i])
        check[i] = 0

check[0] = 1
dfs(0, 0, 0)

print(rtn)