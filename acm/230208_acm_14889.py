N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

check = [0] * N
# ans = []
# S = []
# L = []
sol = 10**9
def dfs(start, idx):
    global sol
    if idx == N//2:
        s_sum = 0 
        l_sum = 0    
        for i in range(N):
            for j in range(i+1, N):
                if check[i] and check[j]:
                    s_sum += mat[i][j] + mat[j][i]
                elif not check[i] and not check[j]:
                    l_sum += mat[i][j] + mat[j][i]
        sol = min(sol, abs(s_sum - l_sum))        
        return
    
    for i in range(start, N):
        if check[i]: continue
        check[i] = 1
        # ans.append(i)
        dfs(i+1, idx+1)
        # ans.pop()
        check[i] = 0

dfs(0, 0)
print(sol)