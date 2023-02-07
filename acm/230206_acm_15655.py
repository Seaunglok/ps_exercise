N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
check = [0] * (N+1)
def dfs(start, idx):
    if idx == M:
        print(*ans)
        return
    for i in range(start, N):
        if check[i]: continue
        check[i] = 1
        ans.append(A[i])
        dfs(i, idx+1)
        ans.pop()
        check[i] = 0        

dfs(0, 0)