N = int(input())

A = list(map(int, input().split()))
DP = [1] * N


for i in range(1, N):    
    for j in range(i):
        # print(DP, i)
        if A[i] < A[j]:
            DP[i] = max(DP[i], DP[j] + 1)
    #     else:
    #         DP[i] = max(DP[i], DP[j])
    # ans = max(DP[i], ans)

# print(DP)
print(max(DP))