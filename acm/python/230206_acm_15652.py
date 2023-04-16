from itertools import combinations_with_replacement

N, M = map(int, input().split())
A = list(range(1, N+1))

# for a in combinations_with_replacement(A, M):
#     print(*a)
ans = []
def dfs(start, idx):
    if idx == M:
        print(*ans)
        return
    for i in range(start, N+1):
        ans.append(i)
        dfs(i, idx+1)
        ans.pop()

dfs(1, 0)