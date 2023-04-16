import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

check = [0] * (N+1)
station = set()
cycle = False

G = [[] * (N+1) for _ in range(N+1)]

for a, b in A:
    G[a].append(b)
    G[b].append(a)
    
# print(G)
    

def dfs(start, idx, cnt, st):    
    global cycle, station
    # print(st, start, idx, cnt)
    if start == idx and cnt >= 2:
        # print(start, idx, cnt, "hi")
        cycle = True       
        # print(st, cnt)
        for s in st:
            station.add(s)
        return
    
    for i in G[idx]:
        # print(start, idx, i, cnt)
        if check[i] == 0:
            check[i] = 1
            dfs(start, i, cnt+1, st+[i])
            check[i] = 0            
        elif start == i and cnt >= 2:
            dfs(start, i, cnt, st+[i])
        
    

for i in range(1, N+1):            
    if check[i] == 0:
        check[i] = 1
        dfs(i, i, 0, [i])
        check[i] = 0
    
    if cycle:        
        break

station = list(station)
ans = [10**9] * (N+1)

que = deque()

for st in station:
    que.append((st, 0))
    ans[st] = 0

while que:
    now, idx = que.popleft()
    for v in G[now]:
        if ans[v] == 10**9:
            ans[v] = idx+1
            que.append((v, idx+1))
            
print(*ans[1:])

    
        
    
    

