import sys
from collections import deque

readl = sys.stdin.readline

T = int(readl())

for _ in range(T):
    N = int(readl())
    
    if N == 1:
        print(1)
        continue
    
    check = [0] * (N+1)
    From = [0] * (N+1)
    How = [0] * (N+1)
    
    q = deque()
    q.append((1))
    check[1] = 1
    How[1] = 1
    
    while q:
        now = q.popleft()
        for i in range(2):
            next = (now * 10 + i) % N
            if not check[next]:
                check[next] = 1
                From[next] = now
                How[next] = i
                q.append((next))
                
    if check[0] == 0:
        print("BRAK")
    else:
        sol = []
        st = From[0]
        sol.append(How[0])
        
        while st:
            sol.append(How[st])
            st = From[st]
            
        sol.reverse()
        print(*sol, sep="")
                
            
    
    
    