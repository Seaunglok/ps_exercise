N = int(input())

mat = [0 for _ in range(N)]
visit = [0 for _ in range(N)]
cnt = 0

def check(idx):
    for i in range(idx):
        if mat[i] == mat[idx] or abs(mat[idx] - mat[i]) == idx - i:
            return 0
    return 1


def dfs(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    
    for c in range(N):
        mat[idx] = c
        if check(idx):
            visit[c] = 1
            dfs(idx+1)
            visit[c] = 0
dfs(0)
print(cnt)