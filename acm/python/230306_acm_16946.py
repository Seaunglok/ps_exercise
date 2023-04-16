from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
sol = [[0] * M for _ in range(N)]
D = dict()
move = ((-1, 0), (0, 1), (1, 0), (0, -1))

def count(dr, dc):
    group = set()
    for rr, cc in move:
        nr, nc = dr+rr, dc+cc
        if nr not in range(N) or nc not in range(M): continue
        if not visit[nr][nc]: continue
        group.add(visit[nr][nc])
    
    cnt = 1
    for g in group:
        cnt += D[g]
        cnt %= 10
        
    return cnt

def bfs(r, c, cnt):
    que = deque()
    que.append((r, c))
    visit[r][c] = cnt
    rtn = 1   
    
    while que:
        dr, dc = que.popleft()
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(M): continue
            if visit[nr][nc] == 0 and mat[nr][nc] == 0:
                visit[nr][nc] = cnt
                que.append((nr, nc))
                rtn += 1                
    return rtn
        
    
cnt = 1
for r in range(N):
    for c in range(M):
        if mat[r][c] == 0 and visit[r][c] == 0:
            total = bfs(r, c, cnt)            
            D[cnt] = total
            cnt += 1

for r in range(N):
    for c in range(M):
        if mat[r][c] == 1:
            sol[r][c] = count(r, c)
            
for r in range(N):   
    print(''.join(map(str, sol[r])))

    


