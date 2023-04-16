import sys
readl = sys.stdin.readline
from collections import deque

N, M = map(int, readl().split())

MAX = 10**6 + 1
check = [0] * (MAX)
move = [0] * (MAX)
    

def find_path(path, L):
    ans = []
    temp = path
    for i in range(L+1):
        # print(temp, move[path], ans)
        ans.append(temp)
        temp = move[temp]
    
    print(*ans[::-1])

def bfs():
    que = deque()  
    que.append((N, 0))    
    
    while que:
        now, cnt = que.popleft()
        if now == M:
            print(cnt)
            find_path(M, cnt)
            return
        
        for next in [now-1, now+1, 2*now]:
            if next not in range(100001): continue
            if check[next]: continue
            move[next] = now
            check[next] = 1
            que.append((next, cnt+1))               

bfs()



