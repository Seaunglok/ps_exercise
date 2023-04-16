N = int(input())
A = list(map(int, input().split()))

INF = -1001
DP = [INF] * (N+1)
DP[0] = A[0]

for i in range(1, N):
    DP[i] = max(A[i], DP[i-1]+A[i])

print(max(DP))