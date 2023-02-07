N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
sol = set()

def dfs(start, idx):
    if idx == M:
        sol.add(tuple(ans))
        return
    
    for i in range(start, N):
        ans.append(A[i])
        dfs(i, idx+1)
        ans.pop()

dfs(0, 0)

for a in sorted(sol):
    print(*a)