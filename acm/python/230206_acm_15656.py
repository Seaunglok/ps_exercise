N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
def dfs(idx):
    if idx == M:
        print(*ans)
        return
    
    for i in range(N):
        ans.append(A[i])
        dfs(idx+1)
        ans.pop()

dfs(0)