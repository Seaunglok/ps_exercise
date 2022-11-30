import sys
from collections import deque

readl = sys.stdin.readline

N, K = map(int, readl().split())

MAX = 500000
D = [[-1] * 2 for _ in range(MAX+1)]

q = deque()
D[N][0] = 0
q.append((N, 0))

while q:
    now, t = q.popleft()
    for next in [now-1, now+1, 2*now]:
        if not 0<=next<=MAX: continue
        if D[next][1-t] == -1:
            D[next][1-t] = D[now][t] + 1
            q.append((next, 1-t))
            
ans = -1
t = 0

# print(D)

while True:
    K += t
    if K > MAX:
        break
    if D[K][t%2] <= t:
        # print(D, K, t)
        ans = t
        break
    t += 1
    
print (ans)
        
