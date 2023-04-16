from collections import deque

C, R, H = map(int, input().split())
mat = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]

def bfs(que):      
    move = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0))
    
    while que:
        dh, dr, dc = que.popleft()
        # print(dh, dr, dc)
        
        for hh, rr, cc in move:
            nh, nr, nc = dh+hh, dr+rr, dc+cc
            if nh not in range(H) or nr not in range(R) or nc not in range(C): continue
            if mat[nh][nr][nc] or mat[nh][nr][nc] == -1: continue
            mat[nh][nr][nc] = mat[dh][dr][dc] + 1
            que.append((nh, nr, nc))
            

ans = 0
flag = False
def answer_check():
    global ans, flag
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if mat[h][r][c] == 0:
                    flag = True    
                ans = max(mat[h][r][c]-1, ans)       
                
    # print(mat)         
                   
    if flag:
        print(-1)
    else:
        print(ans)      
    

def solve():
    que = deque()
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if mat[h][r][c] == 1:
                     que.append((h, r, c))
                     
    bfs(que)                    
    answer_check()
    
    
solve()