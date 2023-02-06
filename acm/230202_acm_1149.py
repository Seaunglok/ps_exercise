N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * 3 for _ in range(N)]
DP[0][0] = A[0][0]
DP[0][1] = A[0][1]
DP[0][2] = A[0][2]

#DP[i][0] = DP[i-1][1] + DP[i-1][2]

for i in range(1, N):
    DP[i][0] = min(DP[i-1][1] + A[i][0], DP[i-1][2] + A[i][0])
    DP[i][1] = min(DP[i-1][0] + A[i][1], DP[i-1][2] + A[i][1])
    DP[i][2] = min(DP[i-1][0] + A[i][2], DP[i-1][1] + A[i][2])
    
# print(DP)
print(min(DP[N-1]))
