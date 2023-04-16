from copy import deepcopy

N = int(input())

A = list(map(int, input().split()))
B = deepcopy(A)
B.reverse()
# print(B)

DP = [1] * N
DP_B = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j]+1)
        if B[i] > B[j]:
            DP_B[i] = max(DP_B[i], DP_B[j]+1)          

ans = 0        
for i in range(N):
    ans = max(ans, DP[i] + DP_B[N-1-i])

print(ans-1)