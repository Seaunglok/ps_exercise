from itertools import product

N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]

def tomat(l):
    return [l[i:i+M] for i in range(0, len(l), M)]
A = product([0, 1], repeat=N*M)
for a in A:
    # mm = tomat(a)
    # print(mm)
    print(a)

ans = 0
for i in range(1<<N*M):
    total = 0
    for r in range(N):
        rsum = 0
        for c in range(M):
            idx = r * M + c
            if i & (1<<idx) != 0:
                rsum = rsum*10 + mat[r][c]
            else:
                total += rsum
                rsum = 0
        total += rsum
    
    for c in range(M):
        csum = 0 
        for r in range(N):
            idx = r * M + c
            if i & (1<<idx) == 0:
                csum = csum * 10 + mat[r][c]
            else:
                total += csum
                csum = 0                
        total += csum
    
    ans = max(ans, total)
    
print(ans)
    
    
    
        
                
                
            

