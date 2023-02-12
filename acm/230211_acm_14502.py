from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

result = 0
temp = [[0] * M for _ in range(N)]

def virus(r, c):
    visit = [[0] * M for _ in range(N)]
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    que = deque()
    visit[r][c] = 1
    que.append((r, c))
    
    while que:
        dr, dc = que.popleft()
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(M): 
                continue
            if visit[nr][nc]: continue
            if temp[nr][nc] == 0:
                que.append((nr, nc))
                visit[nr][nc] = 1
                temp[nr][nc] = 2

def calc_size():
    cnt = 0 
    for r in range(N):
        for c in range(M):
            if temp[r][c] == 0:
                cnt += 1
    return cnt  

def dfs(idx):
    global result
    if idx == 3:
        for r in range(N):
            for c in range(M):
                temp[r][c] = mat[r][c]
                
        for r in range(N):
            for c in range(M):
                if temp[r][c] == 2:
                    virus(r, c)        
        
        result = max(result, calc_size())
        return
    
    for r in range(N):
        for c in range(M):
            if mat[r][c] == 0:                
                mat[r][c] = 1
                # idx += 1
                dfs(idx+1)
                # idx -= 1
                mat[r][c] = 0


dfs(0)
print(result)