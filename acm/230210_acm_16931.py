N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

top, down, front, back, left, right = 0, 0, 0, 0, 0, 0

top = N*M
down = N*M

#back
back += sum(mat[0])
for r in range(N-1):    
    for c in range(M):    
        # print(r, c, mat[r][c], mat[r+1][c])
        if mat[r][c] < mat[r+1][c]:
            back += mat[r+1][c] - mat[r][c]


#front
front += sum(mat[N-1])
for r in range(N-2, -1, -1):
    for c in range(M):
        if mat[r][c] > mat[r+1][c]:
            front += mat[r][c] - mat[r+1][c]

    
#left
ll = list(zip(*mat))
left += sum(ll[0])
for c in range(M-1):
    for r in range(N):
        if mat[r][c] < mat[r][c+1]:
            left += mat[r][c+1] - mat[r][c]

#right
right += sum(ll[M-1])
for c in range(M-2, -1, -1):
    for r in range(N):
        if mat[r][c] > mat[r][c+1]:
            right += mat[r][c] - mat[r][c+1]
        
ans = top + down + back + front + left + right
# print(top, down, front, back, left, right)
print(ans)
        

    
        
        
        
        
        
