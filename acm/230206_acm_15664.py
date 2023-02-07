N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = []
check = [0] * N
sol = set()
def dfs(start, idx):
    if idx == M:
        sol.add(tuple(ans))        
        return
    
    for i in range(start, N):
        if check[i]: continue
        check[i] = 1
        ans.append(A[i])
        dfs(i, idx+1)
        ans.pop()
        check[i] = 0

dfs(0, 0)

for a in sorted(sol):
    print(*a)