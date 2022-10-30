import sys
from heapq import heappop, heappush

readl = sys.stdin.readline

N = int(readl())
M = int(readl())

G = [[] for _ in range(N+1)]
INF = 987654321
D = [INF] * (N+1)
V = [0] * (N+1)
for _ in range(M):
    s, e, c = map(int, readl().split())
    G[s].append((c, e))

start, det = map(int, readl().split())
D[start] = 0
q = []
heappush(q, (D[start], start))

while q:
    cost, now = heappop(q)
    if D[now] < cost: continue
    for g in G[now]:
        cc, ee = g
        if D[ee] > cost + cc:
            D[ee] = cost + cc
            V[ee] = now
            heappush(q, (D[ee], ee))
       
print(D[det])
cnt = 0
st = []
x = det
while x:
    st.append(x)
    x = V[x]    
    cnt += 1
    
    
print(cnt)
while st:
    print(st.pop())
    

    
     
    