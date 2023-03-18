N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]
after_mat = [list(map(int, input().strip())) for _ in range(N)]

def change(r, c):
    for rr in range(r, r+3):
        for cc in range(c, c+3):
            mat[rr][cc] = 1 - mat[rr][cc]


def check():
    for r in range(N):
        for c in range(M):
            if mat[r][c] != after_mat[r][c]:
                return 1
    return 0

sol = 0
for r in range(N-2):
    for c in range(M-2):
        if mat[r][c] != after_mat[r][c]:
            change(r, c)
            sol += 1
            
if check():
    print(-1)
else:
    print(sol)
    
        