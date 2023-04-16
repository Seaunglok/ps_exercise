import sys

readl = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(readl())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, readl().split())
    G[s].append(e)
    G[e].append(s)
    
M = int(readl())

LOG = 21
D = [0] * (N+1)
C = [0] * (N+1)
P = [[0] * (LOG) for _ in range(N+1)]

def dfs(x, depth):
    C[x] = True
    D[x] = depth
    
    for g in G[x]:
        if C[g]: continue
        P[g][0] = x
        dfs(g, depth+1)

def make_parent():
    dfs(1, 0)
    
    for j in range(1, LOG):
        for i in range(1, N+1):
            P[i][j] = P[P[i][j-1]][j-1]            


make_parent()

def LCA(x, y):
    #x, y 높이 중 y가 높이가 높게
    if D[x] > D[y]:
        x, y = y, x
    
    #x, y 높이 맞추기
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

for _ in range(M):
    s, e = map(int, readl().split())
    print(LCA(s, e))
    