import sys
from heapq import heappop, heappush

readl = sys.stdin.readline

N = int(readl())
M = int(readl())

INF = 987654321
G = [[] for _ in range(N+1)]
D = [INF] * (N+1)
chk = [0] * (N+1)

for _ in range(M):
    s, e, c = map(int, readl().split())
    G[s].append((c, s, e))
    
start, dep = map(int, readl().split())

D[start] = 0
chk[start] = 1
q = []

for g in G[start]:
    heappush(q, g)

while q:
    cost, st, end = heappop(q)
    if chk[end]: continue
    # print(st, end, cost)
    if D[end] > D[st] + cost:
        D[end] = D[st] + cost
        for g in G[end]:
            heappush(q, g)
            
print(D[dep])
    

