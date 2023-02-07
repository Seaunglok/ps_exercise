N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ans = []
check = [0] * (N+1)
sol = set()

def dfs(idx):
    if idx == M:
        sol.add(tuple(ans))
        # print(*ans)
        return
    
    for i in range(N):
        if check[i]: continue
        check[i] = 1        
        ans.append(A[i])
        dfs(idx+1)
        ans.pop()
        check[i] = 0

dfs(0)
for a in sorted(sol):
    print(*a)
    
    
    

