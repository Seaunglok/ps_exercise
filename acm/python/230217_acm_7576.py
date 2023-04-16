from collections import deque

C, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]

check = [[0] * C for _ in range(R)]
que = deque()

def bfs():
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))    
    
    while que:
        dr, dc = que.popleft()
        for rr, cc in move:
            nr, nc = rr+dr, cc+dc
            if nr not in range(R) or nc not in range(C): continue
            # if check[nr][nc]: continue            
            if mat[nr][nc] != 0: continue
            # print(nr, nc)
            if mat[nr][nc] == 0:
                mat[nr][nc] = mat[dr][dc] + 1
                que.append((nr, nc))

sr, sc = 0, 0
for r in range(R):
    for c in range(C):
        if mat[r][c] == 1:            
            que.append((r, c))

bfs()
        
sol = 0
sol = max(map(max, mat))
# print(mat)
for r in range(R):
    for c in range(C):
        if mat[r][c] == 0:
            sol = -1
            print(sol)
            exit(0)        
            
print(sol-1)
        