from collections import deque

R, C = map(int, input().split())
sr, sc, dir = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]

#북:0, 동:1, 남:2, 서:3
Dir = ((-1, 0), (0, 1), (1, 0), (0, -1)) 
# check = [[0] * C for _ in range(R)]

def solve(r, c, depth):
    global ans, dir
    
    if depth == 4:
        ndir = (dir+2) % 4
        ndr, ndc = Dir[ndir]
        nr, nc = r+ndr, c+ndc
        if mat[nr][nc] == 1:
            print(ans)
            exit(0)
        else:
            solve(nr, nc, 0)       
                   
    ndir = (dir+3) % 4
    ndr, ndc = Dir[ndir]
    nr, nc = r+ndr, c+ndc
    if mat[nr][nc] == 0:
        ans += 1
        dir = ndir
        mat[nr][nc] = 2
        solve(nr, nc, 0)
        
    elif mat[nr][nc] == 1 or mat[nr][nc] == 2:
        dir = ndir
        solve(r, c, depth+1)
        
ans = 1    
mat[sr][sc] = 2    
solve(sr, sc, 0)
