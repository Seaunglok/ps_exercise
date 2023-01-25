from collections import deque

R, C = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
check = [[0] * C for _ in range(R)]

def bfs(r, c):            
    global check
    que = deque()
    que.append((r, c))
    check[r][c] = 1
    move = ((0, -1), (-1, 0), (0, 1), (1, 0))
    
    while que:
        dr, dc = que.popleft()
        zero = 0
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(R) or nc not in range(C): continue
            if check[nr][nc]: continue
            if mat[nr][nc] == 0:
                zero += 1
                continue
            elif mat[nr][nc] > 0:
                que.append((nr, nc))
                check[nr][nc] = 1        
        mat[dr][dc] -= zero    
        if mat[dr][dc] < 0:
            mat[dr][dc] = 0        
        
        # print("mat", mat, zero)   
    # print("check", check)

def solve():
    global check
    rtn = 0    
    flag = False    
    
    while (1):
        cnt = 0
        chk = 0
        check = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if mat[r][c] > 0 and check[r][c] == 0:
                    bfs(r, c)                    
                    cnt += 1
                    # print("hihi", r, c, cnt, check)
                elif mat[r][c] == 0:
                    chk += 1
        # print("check", cnt, chk, mat)        
        if cnt >= 2:
            break
        if chk == R*C:
            flag = True
            break
        rtn += 1   
    
    if flag:
        return 0
    else:
        return rtn  

print(solve())