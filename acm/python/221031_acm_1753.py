import sys
from heapq import heappop, heappush

readl = sys.stdin.readline

V, E = map(int, readl().split())
start = int(readl())

G = [[] for _ in range(V+1)]
INF = 987654321
D = [INF] * (V+1)
for _ in range(E):
    s, e, c = map(int, readl().split())
    G[s].append((c, e))
    
D[start] = 0
q = []
heappush(q, (D[start], start))

while q:
    cost, now = heappop(q)
    if D[now] < cost: continue
    for cc, ee in G[now]:
        if D[ee] > cost + cc:
            D[ee] = cost + cc
            heappush(q, (D[ee], ee))

for i in range(1, V+1):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])
    