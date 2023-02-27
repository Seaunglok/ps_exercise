from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    
    mat = [[0] * N for _ in range(N)]
    mat[sr][sc] = 1    
    
    que = deque()
    que.append((sr, sc))
    
    def bfs():
        move = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))
        
        while que:
            dr, dc = que.popleft()
            if dr == er and dc == ec:
                return mat[dr][dc]
            for rr, cc in move:
                nr, nc = dr+rr, dc+cc
                if nr not in range(N) or nc not in range(N): continue
                if mat[nr][nc] != 0: continue
                elif mat[nr][nc] == 0:
                    mat[nr][nc] = mat[dr][dc] + 1
                    que.append((nr, nc))                    
    
    print(bfs()-1)
    
    
        
            
            