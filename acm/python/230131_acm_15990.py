N = int(input())
A = [int(input()) for _ in range(N)]
DP = [[0] * 3 for _ in range(100000+1)]
DP[1] = [1, 0, 0]
DP[2] = [0, 1, 0]
DP[3] = [1, 1, 1]
DIV = 1000000009

for i in range(4, 100000+1):
    DP[i][0] = (DP[i-1][1]) % DIV + (DP[i-1][2]) % DIV
    DP[i][1] = (DP[i-2][0]) % DIV + (DP[i-2][2]) % DIV
    DP[i][2] = (DP[i-3][0]) % DIV + (DP[i-3][1]) % DIV

for a in A:
    # print(DP[:a+1])
    print((sum(DP[a])) % DIV)
    

    
    