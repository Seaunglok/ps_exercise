N = int(input())
A = list(map(int, input().split()))

DP = [1] * (N+1)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j]+1)

ans = []
Max = max(DP)
print(Max)
for i in range(N-1, -1, -1):
    if DP[i] == Max:
        ans.append(A[i])
        Max -= 1
ans = reversed(ans)
print(*ans)