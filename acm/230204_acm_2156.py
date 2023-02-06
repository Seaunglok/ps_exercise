N = int(input())
A = [0] + [int(input()) for _ in range(N)] + [0]

DP = [0] * (N+2)
DP[0] = A[0]
DP[1] = A[0]+A[1]
DP[2] = max(DP[1], A[0]+A[2], A[1]+A[2])

for i in range(3, N+1):
    DP[i] = max(DP[i-1], DP[i-2]+A[i], DP[i-3]+A[i]+A[i-1])
    
print(DP[N])