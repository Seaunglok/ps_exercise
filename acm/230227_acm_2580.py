import sys
readl = sys.stdin.readline

N = 9
mat = [list(map(int, readl().split())) for _ in range(N)]
        
def check(r, c, num):    
    for i in range(N):
        if mat[r][i] == num:
            return 0
    
    for i in range(N):
        if mat[i][c] == num:
            return 0
        
    nr = r // 3 * 3
    nc = c // 3 * 3
    
    for rr in range(3):
        for cc in range(3):
            if mat[nr+rr][nc+cc] == num:
                return 0
    
    return 1

def dfs(idx):
    global mat    
    if idx == len(empty):
        for i in range(N):
            print(*mat[i])
        exit(0)
    
    for i in range(1, 10):
        r, c = empty[idx][0], empty[idx][1]
        if check(r, c, i):
            mat[r][c] = i
            dfs(idx+1)
            mat[r][c] = 0

empty = []
for r in range(N):
    for c in range(N):
        if mat[r][c] == 0:
            empty.append((r, c))
            
dfs(0)
            