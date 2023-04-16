N = int(input())

DP = [[0]*2 for _ in range(100)]
DP[1] = [0, 1]
DP[2] = [1, 0]
DP[3] = [1, 1]

for i in range(4, N+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]
    
print(sum(DP[N]))
    