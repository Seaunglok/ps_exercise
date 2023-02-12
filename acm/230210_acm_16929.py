N, M = map(int, input().split())
mat = [list(input().strip()) for _ in range(N)]

st_r = 0
st_c = 0
st_ch = ''
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
visit = [[0] * M for _ in range(N)]

def check(r, c):
    if r not in range(N) or c not in range(M):
        return True
    return False

def dfs(r, c, idx, ch):
    global st_r, st_c, st_ch
    if idx == 0:
        st_r = r
        st_c = c
        st_ch = ch
        dfs(r, c+1, idx+1, mat[r][c])
    if check(r, c):
        return
    # print(r, c, idx, ch)
    if idx and st_r == r and st_c == c and st_ch == ch and idx >= 4:
        print("Yes")
        exit(0)   
    if visit[r][c]: return 
    
    if mat[r][c] == ch:
        visit[r][c] = 1
        dfs(r, c+1, idx+1, mat[r][c])
        dfs(r+1, c, idx+1, mat[r][c])
        dfs(r, c-1, idx+1, mat[r][c])
        dfs(r-1, c, idx+1, mat[r][c])       
        visit[r][c] = 0 
    else:
        return    

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, mat[r][c])
        # visit[r][c] = 0

print("No")