import sys
from collections import deque

readl = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(readl())
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e, c = map(int, readl().split())
    G[s].append((c, e))
    G[e].append((c, s))

M = int(readl())
A = []
for _ in range(M):
    A.append(list(map(int, readl().split())))
    
LOG = 21
D = [0] * (N+1)
C = [0] * (N+1)
P = [[0] * (LOG) for _ in range(N+1)]

def dfs(x, depth):
    C[x] = True
    D[x] = depth
    
    for cost, g in G[x]:
        if C[g]: continue
        P[g][0] = x
        dfs(g, depth+1)        

def make_parent():
    dfs(1, 0)
    for j in range(1, LOG):
        for i in range(1, N+1):
            P[i][j] = P[P[i][j-1]][j-1]
    
make_parent()

INF = 987654321
dist = [INF] * (N+1)
q = deque()
q.append(1)
dist[1] = 0

while q:
    now = q.popleft()
    for cost, next in G[now]:
        if dist[next] > cost + dist[now]:
            dist[next] = cost + dist[now]
            q.append(next)
            
def LCA(x, y):
    if D[x] > D[y]:
        x, y = y, x
    for i in range(LOG-1, -1, -1):
        if D[y] - D[x] >= (1<<i):
            y = P[y][i]
    if x == y:
        return x
    
    for i in range(LOG-1, -1, -1):
        if P[x][i] != P[y][i]:
            x = P[x][i]
            y = P[y][i]
    
    return P[x][0]
     
def solve(x, y):
    sol = dist[x] + dist[y] - 2 * dist[LCA(x, y)]
    return sol

for a in A:
   print(solve(a[0], a[1]))
    