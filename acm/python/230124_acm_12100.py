from copy import deepcopy

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

dir = (0, 1, 2, 3) #북, 동, 남, 서
ans = 0    

def left(mat_):
    for r in range(N):
        idx = 0
        for c in range(1, N):
            if mat_[r][c]:
                tmp = mat_[r][c]
                mat_[r][c] = 0
                if mat_[r][idx] == 0:
                    mat_[r][idx] = tmp
                elif mat_[r][idx] == tmp:
                    mat_[r][idx] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    mat_[r][idx] = tmp
    return mat_

def right(mat_):
    for r in range(N):
        idx = N-1
        for c in range(N-1, -1, -1):
            if mat_[r][c]:
                tmp = mat_[r][c]
                mat_[r][c] = 0
                if mat_[r][idx] == 0:
                    mat_[r][idx] = tmp
                elif mat_[r][idx] == tmp:
                    mat_[r][idx] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    mat_[r][idx] = tmp
    return mat_

def up(mat_):
    for c in range(N):
        idx = 0
        for r in range(N):
            if mat_[r][c]:
                tmp = mat_[r][c]
                mat_[r][c] = 0
                if mat_[idx][c] == 0:
                    mat_[idx][c] = tmp
                elif mat_[idx][c] == tmp:
                    mat_[idx][c] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    mat_[idx][c] = tmp
    return mat_

def down(mat_):
    for c in range(N):
        idx = N-1
        for r in range(N-1, -1, -1):
            if mat_[r][c]:
                tmp = mat_[r][c]
                mat_[r][c] = 0
                if mat_[idx][c] == 0:
                    mat_[idx][c] = tmp
                elif mat_[idx][c] == tmp:
                    mat_[idx][c] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    mat_[idx][c] = tmp
                
    return mat_         

def solve(tmp_mat, cnt):
    global ans
    if cnt >= 5:
        for r in range(N):
            for c in range(N):
                if tmp_mat[r][c] > ans:
                    ans = tmp_mat[r][c]
        
        # ans = max(ans, max(map(max, tmp_mat)))
        return  

    
    solve(left(deepcopy(tmp_mat)), cnt+1)
    solve(right(deepcopy(tmp_mat)), cnt+1)
    solve(up(deepcopy(tmp_mat)), cnt+1)
    solve(down(deepcopy(tmp_mat)), cnt+1)    
    

solve(mat, 0)
print(ans)
