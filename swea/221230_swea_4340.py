T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * (N) for _ in range(N)]
    DP = [[[1000000 for _ in range(N)] for _ in range(N)] for _ in range(4)]    
    #dir : right, down, left, up
   
                   
    def dfs(r, c, dir, cnt):
        # print(cnt, min_cnt, r, c, pre)
        # print(visit)        
        if r not in range(N) or c not in range(N) or visit[r][c] or mat[r][c] == 0:
            return    
        if DP[dir][r][c] <= cnt:
            return    
        if r == N-1 and c == N-1 and cnt != 1:
            if mat[r][c] == 6 and dir != 3:
                return
            if mat[r][c] == 1 and dir != 2:
                return
        if r == 0 and c == 0 and cnt != 1:
            if mat[r][c] == 4 and dir != 1:
                return
            if mat[r][c] == 1 and dir != 0:
                return
            
        DP[dir][r][c] = cnt
        visit[r][c] = 1
        
        if mat[r][c] <= 2:
            if dir == 2:
                dfs(r, c+1, dir, cnt+1)
            elif dir == 3:
                dfs(r+1, c, dir, cnt+1)
            elif dir == 0:
                dfs(r, c-1, dir, cnt+1)
            elif dir == 1:
                dfs(r-1, c, dir, cnt+1)
            
        else:
            if dir == 0 or dir == 2:
                dfs(r-1, c, 1, cnt+1)
                dfs(r+1, c, 3, cnt+1)
            elif dir == 1 or dir == 3:
                dfs(r, c+1, 2, cnt+1)
                dfs(r, c-1, 0, cnt+1)            
        visit[r][c] = 0
        
    ans = 1000000
    dfs(0, 0, 2, 1)
    for i in range(4):
        if ans > DP[i][N-1][N-1]:
            ans = DP[i][N-1][N-1]
        
    visit = [[0] * (N) for _ in range(N)]
    DP = [[[1000000 for _ in range(N)] for _ in range(N)] for _ in range(4)]    
    dfs(N-1, N-1, 0, 1)
    for i in range(4):
        if ans > DP[i][0][0]:
            ans = DP[i][0][0]
    
    
    print(f'#{t} {ans}')
                
