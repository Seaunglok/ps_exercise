import sys

readl = sys.stdin.readline

N = int(readl())
M = int(readl())

INF = 987654321
D = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, readl().split())
    if D[s][e] > c:
        D[s][e] = c
        
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: D[i][j] = 0
            if i == k: D[i][k] = 0
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if D[i][j] == INF: D[i][j] = 0
        print(D[i][j], end=" ")
    print("")
                
