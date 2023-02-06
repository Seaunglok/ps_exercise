from collections import deque

R, C = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(R)]
check = [[[0] * 2 for _ in range(C)] for _ in range(R)]

def bfs(st):
    que = deque()
    que.append((st[0], st[1], 1, 0))
    check[st[0]][st[1]][0] = 1
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dist = 10**9
    
    while que:
        dr, dc, cnt, bit = que.popleft()
        if dr == R-1 and dc == C-1:
            return cnt
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            # print(nr, nc, cnt)
            if nr not in range(R) or nc not in range(C): continue      
            if mat[nr][nc] == 0 and check[nr][nc][bit] == 0:
                check[nr][nc][bit] = 1
                que.append((nr, nc, cnt+1, bit))                  
            elif mat[nr][nc] and bit == 0:
                check[nr][nc][bit+1] = 1
                que.append((nr, nc, cnt+1, bit+1))                

    return -1    

def solve():    
    start = (0, 0)    
    ans = bfs(start)
    print(ans)    
    
solve()

