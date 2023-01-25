from collections import deque

N, M = map(int, input().split())

mat = [list(map(int, input().strip())) for _ in range(N)]

check = [[0] * M for _ in range(N)]
start = (0, 0)
end = (N-1, M-1)
dist = 10**9
move = ((-1, 0), (0, 1), (1, 0), (0, -1))

que = deque()
que.append((start[0], start[1], 1))

while que:
    dr, dc, now = que.popleft()
    if dr == end[0] and dc == end[1]:
        print(dist, now)
        if dist > now:
            dist = now
        break
    for rr, cc in move:
        nr, nc = dr+rr, dc+cc            
        if nr not in range(N) or nc not in range(M): continue
        if not mat[nr][nc]: continue
        if check[nr][nc]: continue
        check[nr][nc] = 1
        que.append((nr, nc, now+1))

print(dist)
        
    


