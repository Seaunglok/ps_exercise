from collections import deque

R, C = map(int, input().split())
mat = [list(input().strip()) for _ in range(R)]

red = ()
blue = ()
check = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if mat[r][c] == 'R':
            red = (r, c)
        elif mat[r][c] == 'B':
            blue = (r, c)
            
def gogo(dr, dc, rr, cc):
    cnt_ = 0
    while mat[dr+rr][dc+cc] != '#' and mat[dr][dc] != 'O':
        dr += rr
        dc += cc
        cnt_ += 1
    return dr, dc, cnt_
            
def solve():
    que = deque()
    que.append((red[0], red[1], blue[0], blue[1], 0))
    check[red[0]][red[1]][blue[0]][blue[1]] = 1
    move = ((-1, 0), (0, 1), (1, 0), (0, -1))
    
    while que:
        drr, drc, dbr, dbc, cnt = que.popleft()
        if cnt >= 10:
            break
        for rr, cc in move:
            nrr, nrc, rcnt = gogo(drr, drc, rr, cc)
            nbr, nbc, bcnt = gogo(dbr, dbc, rr, cc)
            
            if mat[nbr][nbc] == 'O':
                continue
            
            if mat[nrr][nrc] == 'O':
                print(cnt+1)
                return
            
            if nrr == nbr and nrc == nbc:
                if rcnt > bcnt:
                    nrr -= rr
                    nrc -= cc
                else:
                    nbr -= rr
                    nbc -= cc
            if not check[nrr][nrc][nbr][nbc]:
                check[nrr][nrc][nbr][nbc] = 1
                que.append((nrr, nrc, nbr, nbc, cnt+1))
    print(-1)    

solve()
            
            
            

            
            