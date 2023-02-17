import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)    
    
check = [0] * 2001
sol = 0

def dfs(start, idx):
    global sol
    if idx == 4:
        sol = 1
        return
    
    for i in G[start]:
        if check[i]: continue
        check[i] = 1
        dfs(i, idx+1)
        check[i] = 0

for i in range(N):
    check[i] = 1
    dfs(i, 0)
    check[i] = 0
    if sol:
        break
    
        
print(sol)