import sys
from collections import deque

readl = sys.stdin.readline
N = int(readl())

G = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)
work = [0] * (N+1)

for i in range(1, N+1):
    L = list(map(int, readl().split()))
    if L[1] == 0:
        G[0].append(i)        
    for ii in range(L[1]):
        G[L[ii+2]].append(i)
        indegree[i] += 1
    time[i] = L[0]
    
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append((i))
        work[i] = time[i]

while q:
    now = q.popleft()
    for nn in G[now]:        
        work[nn] = max(work[nn], work[now] + time[nn])
        indegree[nn] -= 1
        # print(nn, now, work[nn], time[nn])
        
        if indegree[nn] == 0:
            q.append((nn))
            
ans = 0
for i in range(1, N+1):
    ans = max(ans, work[i])
            
print(ans)
        
        
        
    
    



        



    