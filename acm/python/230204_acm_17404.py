N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

R, G, B = 0, 1, 2
INF = 10**9
ans = INF


for color in [R,G,B]:
    DP = [[INF] * 3 for _ in range(N)]
    DP[0][color] = A[0][color]
    
    for i in range(1, N):
        DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + A[i][0]
        DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + A[i][1]
        DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + A[i][2]
    
    DP[N-1][color] = 10**9
    
    # print(DP)
    ans = min(ans, min(DP[N-1]))

print(ans)
    


