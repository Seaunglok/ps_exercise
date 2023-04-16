import sys
from collections import deque

readl = sys.stdin.readline

N = int(readl())
G = [[] for _ in range(N+1)]

INF = 987654321

for _ in range(N-1):
    s, e, c = map(int, readl().split())
    G[s].append((c, e))
    G[e].append((c, s))
M = int(readl())

def solve(a, b):
    q = deque()
    q.append((a))
    chk = [0] * (N+1)
    dist = [INF] * (N+1)
    
    chk[a] = True    
    dist[a] = 0
    
    while q:
        start = q.popleft()
        for cost, end in G[start]:
            if chk[end]: continue
            if dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost
                chk[end] = True
                q.append((end))
                
    print(dist[b]) 
    
for _ in range(M):
    A, B = map(int, readl().split())
    solve(A, B)
    

    