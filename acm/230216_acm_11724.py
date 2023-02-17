import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    
check = [0] * (N+2)
cnt = 0

def dfs(start):
    for i in G[start]:
        if check[i]: continue
        check[i] = 1
        dfs(i)        
    
for i in range(1, N+1):
    if check[i]: continue
    check[i] = 1
    dfs(i)
    cnt += 1

print(cnt)
    