from collections import deque, defaultdict

N = int(input())
K = int(input())
A = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
Dir = [list(input().split()) for _ in range(L)]
dir = defaultdict()

for t, a in Dir:
    dir[int(t)] = a

mat = [[0] * N for _ in range(N)]
for r, c in A:
    mat[r-1][c-1] = 1
    
move = ((-1, 0), (0, 1), (1, 0), (0, -1)) #북, 동, 남, 서

que = deque()
que.append((0, 0))
cnt = 1
go = 1
dr, dc = 0, 0

while True:        
    rr, cc = move[go][0], move[go][1]
    nr, nc = dr+rr, dc+cc
    
    #벽, 자기자신 몸과 부딪히면
    if nr not in range(N) or nc not in range(N): break
    if mat[nr][nc] == 2: break
    
    # 사과를 먹을 떄
    if mat[nr][nc] == 1:
        mat[nr][nc] = 2
        que.append((nr, nc))      
    else:
        mat[nr][nc] = 2
        que.append((nr, nc))
        pr, pc = que.popleft()
        mat[pr][pc] = 0        
    
    if cnt in dir.keys():
        if dir[cnt] == 'D':
            go = (go + 1) % 4
        else:
            go = (go - 1) % 4            
    
    dr, dc = nr, nc                
    cnt += 1

print(cnt)
        
        
    
    




    


