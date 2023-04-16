N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

DP = [0] * (N+2)

for i in range(N-1, -1, -1):
    if i + A[i][0] > N:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], A[i][1] + DP[i+A[i][0]])
        
print(DP[0])
    
    

