N = int(input())

DP = [[0] * 3 for _ in range(N)]
DP[0][0] = 1
DP[0][1] = 1
DP[0][2] = 1
MOD = 9901

for i in range(1, N):
    DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2]) % MOD
    DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % MOD
    DP[i][2] = (DP[i-1][0] + DP[i-1][1]) % MOD

# print(DP)
print(sum(DP[N-1]) % MOD)