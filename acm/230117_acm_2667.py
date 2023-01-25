from collections import deque

N = int(input())
mat = [list(map(int, input().strip())) for _ in range(N)]

check = [[0] * N for _ in range(N)]
def bfs(r, c):
    que = deque()
    check[r][c] = 1
    count = 1
    que.append((r, c, count))
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    while que:
        dr, dc, now = que.popleft()
        # print("now", now)
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(N): continue
            if check[nr][nc]: continue
            if not mat[nr][nc]: continue
            check[nr][nc] = 1
            count += 1
            que.append((nr, nc, now+1))
            
    return count
    

rtn = []
house = 0
for r in range(N):
    for c in range(N):
        if mat[r][c] == 1 and check[r][c] == 0:
            house += 1
            cnt = bfs(r, c)
            rtn.append(cnt)

print(house)
for rr in sorted(rtn):
    print(rr)

