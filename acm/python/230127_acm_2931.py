from collections import deque

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

check = [[0] * N for _ in range(N)]
move = ((-1, 0), (0, 1), (1, 0), (0, -1)) #북, 동, 남, 서   

def bfs(r, c, land):
    que = deque()
    que.append((r, c))
    check[r][c] = 1
    mat[r][c] = land 
    
    while que:
        dr, dc = que.popleft()
        
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(N): continue
            if check[nr][nc]: continue
            if mat[nr][nc] == 1:
                mat[nr][nc] = land
                check[nr][nc] = 1
                que.append((nr, nc))
                
def bfs_dist(ll):
    global check
    que = deque()
    check = [[0] * N for _ in range(N)]
    dist = 10**9
    
    for r in range(N):
        for c in range(N):
            if mat[r][c] == ll:
                que.append((r, c, 0))               
    
    while que:
        dr, dc, cnt = que.popleft()
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(N) or nc not in range(N): continue
            if check[nr][nc]: continue
            if mat[nr][nc] == ll: continue
            # print(nr, nc, cnt, ll)
            if mat[nr][nc] == 0:
                check[nr][nc] = 1
                que.append((nr, nc, cnt+1))
            elif mat[nr][nc] != ll:
                dist = min(dist, cnt)
                # print(nr, nc, ll, cnt, dist)
    return dist
    

def find_land():
    land = 2
    for r in range(N):
        for c in range(N):
            if mat[r][c] == 1:
                bfs(r, c, land)    
                land += 1
    return land
                
def find_min_dist(land):     
    ans = 10**9
    for ll in range(2, land):
        dd = bfs_dist(ll)    
        ans = min(ans, dd)
    print(ans)

def solve():    
    land_ = find_land()        
    find_min_dist(land_)
    

solve()