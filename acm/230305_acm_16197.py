import sys
sys.setrecursionlimit(10**9)
readl = sys.stdin.readline

N, M = map(int, readl().split())
mat = [list(readl().strip()) for _ in range(N)]

coins = []
for r in range(N):
    for c in range(M):
        if mat[r][c] == 'o':
            coins.append((r, c))
            
sol = 987654321        
move = ((-1, 0), (0, 1), (1, 0), (0, -1))
visit = []
def dfs(coin1, coin2, cnt):
    global sol
    r1, c1 = coin1
    r2, c2 = coin2
    
    if cnt >= sol or cnt > 10:
        return
    if r1 == r2 and c1 == c2:
        return
    if (r1 not in range(N) or c1 not in range(M)) and (r2 not in range(N) or c2 not in range(M)):
        return
    if (r1 not in range(N) or c1 not in range(M)) or (r2 not in range(N) or c2 not in range(M)):
        sol = min(sol, cnt)
        return
    
    for rr, cc in move:
        nr1 = r1+rr
        nc1 = c1+cc
        nr2 = r2+rr
        nc2 = c2+cc
        if nr1 in range(N) and nc1 in range(M) and nr2 in range(N) and nc2 in range(M):
            if mat[nr1][nc1] != '#' and mat[nr2][nc2] != '#' and (nr1, nc1, nr2, nc2) not in visit:
                visit.append((nr1, nc1, nr2, nc2))
                dfs((nr1, nc1), (nr2, nc2), cnt+1)
                visit.pop()
            elif mat[nr1][nc1] == '#' and mat[nr2][nc2] != '#' and (nr1, nc1, nr2, nc2) not in visit:
                visit.append((r1, c1, nr2, nc2))
                dfs((r1, c1), (nr2, nc2), cnt+1)
                visit.pop()
            elif mat[nr1][nc1] != '#' and mat[nr2][nc2] == '#' and (nr1, nc1, nr2, nc2) not in visit:
                visit.append((nr1, nc1, r2, c2))
                dfs((nr1, nc1), (r2, c2), cnt+1)
                visit.pop()
        else:
            visit.append((nr1, nc1, nr2, nc2))
            dfs((nr1, nc1), (nr2, nc2), cnt+1)
            visit.pop()
            
dfs(coins[0], coins[1], 0)

print(sol if sol<=10 else -1)
            

            