import sys

readl = sys.stdin.readline

N = int(readl())

G = [[0] * N for _ in range(N)]

for i in range(N):
    arr = list(map(int, readl().split()))
    for ii, a in enumerate(arr):
        G[i][ii] = a

for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][k] == 1 and G[k][j]:
                G[i][j] = 1

for i in range(N):
    for j in range(N):
        print(G[i][j], end=" ")
    print("")
 
    
    