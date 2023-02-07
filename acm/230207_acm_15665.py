N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
sol = set()
ss = []
def dfs(idx):
    if idx == M:
        sol.add(tuple(ans))
        ss.append(list(ans))
        return
        
    for i in range(N):
        ans.append(A[i])
        dfs(idx+1)
        ans.pop()

dfs(0)

for a in sorted(sol):
    print(*a)
    