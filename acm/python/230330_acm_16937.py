H, W = map(int, input().split())
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

sol = 0
for i in range(N-1):
    for j in range(i+1, N):
        r1, c1 = A[i]
        r2, c2 = A[j]
        
        if (max(r1, r2) <= H and c1+c2 <= W) or (max(c1, c2) <= W and r1+r2 <= H):
            sol = max(sol, r1*c1+r2*c2)
        if (max(c1, r2) <= H and r1+c2 <= W) or (max(r1, c2) <= W and c1+r2 <= H):
            sol = max(sol, r1*c1+r2*c2)
        if (max(c2, r1) <= H and r2+c1 <= W) or (max(r2, c1) <= W and c2+r1 <= H):
            sol = max(sol, r1*c1+r2*c2)
        if (max(c1, c2) <= H and r1+r2 <= W) or (max(r1, r2) <= W and c1+c2 <= H):
            sol = max(sol, r1*c1+r2*c2)

print(sol)
            
             
    
