import sys

readl = sys.stdin.readline
T = int(readl())

for t in range(T):
    N, M, W = map(int, readl().split())
    G = []
    INF = int(1e9)    
    D = [INF] * (N+1)
    cycle = False
    
    for i in range(M):
        s, e, c = map(int, readl().split())
        G.append((c, s, e))
        G.append((c, e, s))
        
    for i in range(W):
        s, e, c = map(int, readl().split())
        G.append((-c, s, e))
    
    D[1] = 0
    
    for i in range(1, N+1):
        for g in G:
            cost, start, end = g
            if D[end] > D[start] + cost:
                D[end] = D[start] + cost
                if i == N:
                    cycle = True

    if cycle:
        print("YES")
    else:
        print("NO")
        