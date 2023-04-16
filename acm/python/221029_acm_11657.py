import sys

readl = sys.stdin.readline

N, M = map(int, readl().split())
INF = 987654321
D = [INF] * (N+1)
G = [] * (N+1)
cycle = False

for i in range(M):
    s, e, c = map(int, readl().split())    
    G.append((c, s, e))
    
D[1] = 0
for i in range(1, N+1):
    for j in range(M):
        cost, start, end = G[j]
        if D[start] != INF and D[end] > D[start] + cost:
            D[end] = D[start] + cost
            if i == N:
                cycle = True
        
if cycle: 
    print(-1)
else:
    for d in range(2, N+1):
        if D[d] == INF:
            print(-1)
        else:
            print(D[d])        
        