import sys
from collections import deque
readl = sys.stdin.readline

N = int(readl())
G = [[] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, readl().split())
    G[a].append(b)
    G[b].append(a)
    
A = list(map(int, readl().split()))

que = deque()
que.append((1))
ans = []

check = [0] * (N+1)
check[1] = 1
while que:
    now = que.popleft()
    ans.append(now)
    for next in G[now]:
        if check[next]: continue
        check[next] = 1
        que.append((next))        
sol = 1
for a, aa in zip(A, ans):
    if a != aa:
        sol = 0
        break

print(sol)
        


        
        