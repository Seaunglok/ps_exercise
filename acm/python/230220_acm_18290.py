import sys
readl = sys.stdin.readline

N, M, K = map(int, readl().split())
mat = [list(map(int, readl().split())) for _ in range(N)]

rtn = -10001

check = [[0] * (M) for _ in range(N)]
move = ((-1, 0), (0, 1), (1, 0), (0, -1))

def impossible(r, c):
    for rr, cc in move:
        nr, nc = rr+r, cc+c
        if nr not in range(N) or nc not in range(M): continue
        if check[nr][nc]:
            return True
    return False

def dfs(r, c, cnt, dist):    
    global rtn     
    # print(cnt, dist)
    
    if cnt == K:
        rtn = max(rtn, dist)
        return rtn
    
    for nr in range(r, N):
        for nc in range(c if r == nr else 0, M):            
            if impossible(nr, nc): continue
            if check[nr][nc]: continue
            
            # print("j", r, c)
            check[nr][nc] = 1
            dfs(nr, nc, cnt+1, dist+mat[nr][nc])
            check[nr][nc] = 0
    

dfs(0, 0, 0, 0)                
print(rtn)