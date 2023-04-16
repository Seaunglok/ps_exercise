N, M, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

def rotate():   
    r, c = 0, 0
    n, m = N, M
    idx = min(N, M) // 2
    
    while idx:
        temp = mat[r][c]        
        #up
        for i in range(m-1):
            mat[r][c+i] = mat[r][c+i+1]
            
        for i in range(n-1):
            mat[r+i][c+m-1] = mat[r+i+1][c+m-1]
        
        for i in range(m-1):
            mat[r+n-1][c+m-1-i] = mat[r+n-1][c+m-2-i]
        
        for i in range(n-1):
            mat[r+n-1-i][c] = mat[r+n-2-i][c]
        
        mat[r+1][c] = temp
        
        r += 1
        c += 1
        n -= 2
        m -= 2
        idx -= 1

for _ in range(R):
    rotate()
    
for row in mat:
    print(*row)
            