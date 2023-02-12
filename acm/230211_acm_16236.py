from collections import deque

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

baby = 2
now_r, now_c = 0, 0

for r in range(N):
    for c in range(N):
        if mat[r][c] == 9:
            now_r, now_c = r, c
            mat[r][c] = 0

def bfs():
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visit = [[-1] * N for _ in range(N)]
    visit[now_r][now_c] = 0
    que = deque()
    que.append((now_r, now_c))
    
    while que:
        dr, dc = que.popleft()
        for rr, cc in moves:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(N):
                continue
            if visit[nr][nc] != -1: continue
            if mat[nr][nc] <= baby:
                visit[nr][nc] = visit[dr][dc] + 1
                que.append((nr, nc))
    # print(visit)
    return visit

def find(dist):
    x, y, min_dist = 0, 0, 10**9
    # print(dist)
    for r in range(N):
        for c in range(N):
            if dist[r][c] == -1: 
                continue
            if 1 <= mat[r][c] and mat[r][c] < baby:
                if dist[r][c] < min_dist:
                    min_dist = dist[r][c]
                    x, y = r, c
    # print(min_dist)
    if min_dist == 10**9:
        return False
    return x, y, min_dist    
    

result = 0
fish = 0
while(1):
    ans = find(bfs())
    if not ans:
        print(result)
        break
    else:
        now_r, now_c = ans[0], ans[1]
        result += ans[2]
        mat[now_r][now_c] = 0
        fish += 1
    
    if fish >= baby:
        baby += 1
        fish = 0
        