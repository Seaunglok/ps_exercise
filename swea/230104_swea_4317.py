T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(R)]
    
    ans = 0
    dp = [[-1] *  C for _ in range(1<<R)]
    
    def check(r, c):
        if r not in range(R) or c not in range(C): return False
        if mat[r][c] or mat[r+1][c] or mat[r][c+1] or mat[r+1][c+1]:
            return False
        return True
    
    def convert(r, c, val):
        mat[r][c] = val
        mat[r+1][c] = val
        mat[r][c+1] = val
        mat[r+1][c+1] = val
    
    def dfs(r, c, cnt, bit):
        global ans
        # print(r, c, cnt, bit, ans)
        if c >= C-1:
            if ans < cnt:
                ans = cnt
            return
        if r >= R-1:
            if dp[bit][c] >= cnt:
                return
            else:
                dp[bit][c] = cnt
            dfs(0, c+1, cnt, 0)
            return
        if check(r, c):
            convert(r, c, 1)
            dfs(r+2, c, cnt+1, bit | 1 << r)
            convert(r, c, 0)
        dfs(r+1, c, cnt, bit)           
    
    dfs(0, 0, 0, 0)
    print(f'#{t} {ans}')
    