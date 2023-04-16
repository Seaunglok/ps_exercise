from itertools import product

N, M = map(int, input().split())
A = list(range(1, N+1))

# for a in product(A, repeat=M):
#     print(*a)

ans = []
def dfs(idx):
    if idx == M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        ans.append(i)
        dfs(idx+1)
        ans.pop()

dfs(0)