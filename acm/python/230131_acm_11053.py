N = int(input())
A = list(map(int, input().split()))

DP = [1] * (N+1)

for i in range(1, N):
    for j in range(i):
        # print(i, j, A[i], A[j], DP)
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)
            
print(max(DP))