from collections import deque

R, C = map(int, input().split())
mat = [list(input().strip()) for _ in range(R)]
start = ()
check = [[[0] * 2**6 for _ in range(C)] for _ in range(R)]

def find_start():
    global start
    for r in range(R):
        for c in range(C):
            if mat[r][c] == '0':
                start = (r, c)    
                
def bfs(r, c):
    que = deque()
    que.append((r, c, 0, 1))
    check[r][c][0] = 1
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    dist = 10**9
    
    while que:
        dr, dc, bit, cnt = que.popleft()
        for rr, cc in move:
            nr, nc = dr+rr, dc+cc
            if nr not in range(R) or nc not in range(C): continue
            # print(nr, nc, bit, cnt, mat[nr][nc], check[nr][nc][bit])
            if mat[nr][nc] == '1':
                return cnt
            if check[nr][nc][bit]: continue        
            if mat[nr][nc].islower():
                nbit = bit | 1 << ( ord(mat[nr][nc]) - ord('a') )
                que.append((nr, nc, nbit, cnt+1))
                check[nr][nc][nbit] = 1
            if mat[nr][nc].isupper():
                chk = bit & 1 << ( ord(mat[nr][nc]) - ord('A') ) 
                # print("ch", chk)
                if chk:
                    que.append((nr, nc, bit, cnt+1))
                    check[nr][nc][bit] = 1
                else:
                    continue            
            # print("cc", mat[nr][nc] == '0')
            if mat[nr][nc] == '.' or mat[nr][nc] == '0':                
                que.append((nr, nc, bit, cnt+1))
                check[nr][nc][bit] = 1
                
    return -1
    
def solve():
    find_start()
    ans = bfs(start[0], start[1])
    print(ans)    

solve()