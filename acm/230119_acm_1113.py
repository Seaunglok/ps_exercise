from collections import deque
# 
R, C = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(R)]
# R, C = (5, 5)
# mat = [[49, 48, 47, 48, 49], [36, 11, 16, 11, 48], [32, 11, 49, 16, 30], [40, 11, 11, 11, 29], [40, 42, 50, 29, 28]]

MAX = max(map(max, mat))
MIN = min(map(min, mat))
check = [[0] * C for _ in range(R)]
ans = 0

def bfs(r, c, h):
    global check, ans
    que = deque()
    que.append((r, c))
    check[r][c] = 1    
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    cnt = 1
    flag = True
    
    while que:
        dr, dc = que.popleft()
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(R) or nc not in range(C): 
                flag = False
                continue
            if check[nr][nc]: continue
            if mat[nr][nc] <= h:
                cnt += 1
                check[nr][nc] = 1
                que.append((nr, nc))
                
    if flag:
        ans += cnt
        

def solve():
    global check
    for h in range(MIN, MAX+1):
        check = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if check[r][c] == 0 and mat[r][c] <= h:
                    bfs(r, c, h)
    print(ans)

solve()
