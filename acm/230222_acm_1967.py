import sys
sys.setrecursionlimit(10**6)

N = int(input())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    G[a].append([b, c])
    G[b].append([a, c])
    
def dfs(node, dist):
    global check
    for next, next_dist in G[node]:
        if check[next] == -1:
            check[next] = dist + next_dist
            dfs(next, dist + next_dist)

check = [-1] * (N+1)
check[1] = 0
dfs(1, 0)
idx = check.index(max(check))

check = [-1] * (N+1)
check[idx] = 0
dfs(idx, 0)

print(max(check))
