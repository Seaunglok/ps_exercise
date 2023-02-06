# N = int(input())
# A = list(map(int, input().split()))

N = int(input())
input_array = list(map(int, input().split()))
dp = [[n for n in input_array] for _ in range(2)]

if N == 1:
    print(input_array[0])
    exit(0)

for i in range(1, N):
    dp[0][i] = max(dp[0][i], dp[0][i - 1] + input_array[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + input_array[i])

print(max(max(dp[0]), max(dp[1])))

# DP = [[0] * N for _ in range(2)]
# DP[0][0] = A[0]
# DP[1][0] = A[0]

# ans = -10**9

# if N == 1:
#     A[0]
#     exit(0)

# for i in range(1, N):
#     DP[0][i] = max(A[i], A[i]+DP[0][i-1])
#     DP[1][i] = max(DP[0][i-1], A[i]+DP[1][i-1])
#     ans = max(ans, DP[0][i], DP[1][i])

# print(ans)
    


# for j in range(1, N):  
#     for i in range(1, N):      
#         # print(i, j, DP)
#         if i == j: 
#             DP[j][i] = DP[j][i-1]
#             continue
#         DP[j][i] = max(DP[j][i], A[i] + DP[j][i-1])            
#     DP[0][j] = max(DP[0][j], A[j] + DP[0][j-1])

# ans = 0
# for i in range(N):
#     for j in range(N):
#         ans = max(ans, DP[i][j])

# print(ans)