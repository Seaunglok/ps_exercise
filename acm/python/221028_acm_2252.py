import sys
from heapq import heappop, heappush

readl = sys.stdin.readline

N, M = map(int, readl().split())
G = [[] for _ in range(N+1)]
indeg = [0] * (N+1)

for _ in range(M):
    A, B = map(int, readl().split())
    G[A].append(B)
    indeg[B] += 1
    
q = []
for i in range(1, N+1):
    if indeg[i] == 0:
        heappush(q, (i))

# print(q)
while q:
    now = heappop(q)
    print(now, end=' ')
    for n in G[now]:
        next = n
        indeg[next] -= 1
        if indeg[next] == 0:
            heappush(q, (next))
            

        
    