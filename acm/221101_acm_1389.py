import sys

readl = sys.stdin.readline

N, M = map(int, readl().split())
INF = 987654321
D = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, readl().split())
    D[A][B] = 1
    D[B][A] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

sum_d = []

for i in range(1, N+1):
    ssum = 0
    for d in D[i]:
        if d == INF: d = 0
        ssum += d
    sum_d.append((ssum, i))
    
sum_d = sorted(sum_d, key=lambda x:x[0])
print(sum_d[0][1])

# print(min(sum_d))    
     