N = int(input())
# A = list(range(1, N+1))

ans = []
check = [0] * (N+1)
def dfs(idx):
    if idx == N:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if check[i]: continue
        check[i] = 1
        ans.append(i)
        dfs(idx+1)
        ans.pop()
        check[i] = 0
dfs(0)