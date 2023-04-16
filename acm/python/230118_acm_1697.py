from collections import deque

N, K = map(int, input().split())

def solve():
    que = deque()
    que.append((N))
    rtn = 10**9
    check = [0] * (10**5 + 2)
    check[N] = 1
    
    while que:
        now = que.popleft()        
        if now == K:
            rtn = min(rtn, check[now]-1)
            return rtn        
        for next in [now-1, now+1, 2*now]:
            if not 0<= next < 10**5 + 2: continue
            if check[next]: continue            
            # print(next, now, cnt)         
            check[next] = check[now] + 1
            que.append((next))                               

ans = solve()
print(ans)


