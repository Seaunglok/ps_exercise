N = int(input())
mat = [list(input().strip()) for _ in range(N)]
ans = 0
def find():
    global ans
        
    for r in range(N):
        cnt = 1
        for c in range(1, N):
            if mat[r][c] == mat[r][c-1]:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
    print("c", ans)
            
    
    for c in range(N):   
        cnt = 1
        for r in range(1, N):
            if mat[r][c] == mat[r-1][c]:
                print(r, c, cnt)
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1
    print("r", ans)

for r in range(N):
    for c in range(1, N):
        mat[r][c-1], mat[r][c] = mat[r][c], mat[r][c-1]
        find()
        mat[r][c-1], mat[r][c] = mat[r][c], mat[r][c-1]
        
for r in range(1, N):
    for c in range(N):
        mat[r-1][c], mat[r][c] = mat[r][c], mat[r-1][c]
        find()
        mat[r-1][c], mat[r][c] = mat[r][c], mat[r-1][c]
        
print(ans)
        
        
