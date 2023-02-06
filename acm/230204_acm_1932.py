N = int(input())
A = [0] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

if N == 1:
    print(A[1][1])
    exit(0)

DP = [[0] * i + [0] for i in range(1, N+2)]

DP[1][1] = A[1][1]
DP[2][1] = A[1][1] + A[2][1]
DP[2][2] = A[1][1] + A[2][2]

for i in range(3, N+1):
    for j in range(1, i+1):
        # print(A, DP, DP[i-1][j], DP[i-1][j-1], A[i][j], DP[i][j], i, j)
        DP[i][j] = max(DP[i][j], max(DP[i-1][j], DP[i-1][j-1]) + A[i][j])

# print(DP)

print(max(DP[N]))