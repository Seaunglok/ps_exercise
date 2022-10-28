import sys
from heapq import heappop, heappush

readl = sys.stdin.readline

N = int(readl())
M = int(readl())

G = [[] for _ in range(N+1)]
chk = [0] * (N+1)

for _ in range(M):
    a, b, c = map(int, readl().split())
    G[a].append((c, b))
    G[b].append((c, a))
    
q = []
chk[1] = True
for g in G[1]:
    heappush(q, g)
ans = 0
while q:
    cost, next = heappop(q)    
    # print(next)
    if chk[next]:
        continue
    chk[next] = True
    ans += cost
    # print(next, cost, G[next])
    for nn in G[next]:
        heappush(q, nn)

print(ans)      