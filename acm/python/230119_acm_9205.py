from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    sx, sy = map(int, input().split())
    market = [list(map(int, input().split())) for _ in range(N)]
    ex, ey = map(int, input().split())
    
    def solve():
        que = deque()
        que.append((sx, sy))
        check = [0] * (N+1)
        
        while que:
            nowx, nowy = que.popleft()
            if abs(nowx-ex) + abs(nowy-ey) <= 1000: 
                print("happy")
                return
            
            for i, (mx, my) in enumerate(market):
                if check[i]: continue
                if abs(nowx-mx) + abs(nowy-my) <= 1000:
                    check[i] = 1
                    que.append((mx, my))
        print("sad")
        return
        
    solve()
    
    