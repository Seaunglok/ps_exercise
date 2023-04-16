import sys

readl = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(readl())

LOG = 21
G = [[] for _ in range(N+1)]
P = [[0] * (LOG) for _ in range(N+1)]
C = [0] * (N+1)
D = [0] * (N+1)

for _ in range(N-1):
    s, e = map(int, readl().split())
    G[s].append(e)
    G[e].append(s)

M = int(readl())

def dfs(x, depth):
    D[x] = depth
    C[x] = True    

    for g in G[x]:
        if C[g]: continue
        P[g][0] = x    
        dfs(g, depth+1)

def make_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N+1):
            P[j][i] = P[P[j][i-1]][i-1]    

make_parent()

def LCA(x, y):
    if D[x] > D[y]:
        x, y = y, x
    
    for i in range(LOG-1, -1, -1):
        if D[y] - D[x] >= (1 << i):
            y = P[y][i]
    if x == y:
        return x
    
    for i in range(LOG-1, -1, -1):
        if P[x][i] != P[y][i]:
            x = P[x][i]
            y = P[y][i]
            
    return P[x][0]           

A = []
for _ in range(M):
    s, e = map(int, readl().split())
    print(LCA(s, e))