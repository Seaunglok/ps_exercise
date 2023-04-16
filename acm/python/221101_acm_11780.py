import sys
from collections import deque

readl = sys.stdin.readline

N = int(readl())
M = int(readl())

INF = 987654321
D = [[INF] * (N+1) for _ in range(N+1)]
next = [[-1] * (N+1) for _ in range(N+1)]

def path(x, y):
    if next[x][y] == -1:
        print("0")
        return
    q = deque()
    q.append(x)
    
    while x != y:
        x = next[x][y]
        q.append(x)
    print(len(q), end=" ")
    
    while q:
        print(q.popleft(), end=" ")
    print()   
    

for _ in range(M):
    s, e, c = map(int, readl().split())
    if D[s][e] > c:
        D[s][e] = c
        next[s][e] = e        

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: D[i][j] = 0
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]
                next[i][j] = next[i][k]
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if D[i][j] == INF:
            D[i][j] = 0
        print(D[i][j], end=" ")
    print()
    
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            print("0")
        elif D[i][j] == INF:
            print("0")
        else:
            path(i, j)
