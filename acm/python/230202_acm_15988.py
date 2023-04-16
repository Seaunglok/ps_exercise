T = int(input())

MOD = 1000000009
DP = [0] * (1000001)
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(4, 1000001):
    DP[i] = (DP[i-3] % MOD + DP[i-2] % MOD + DP[i-1] % MOD) 

for t in range(T):
    N = int(input())

    
    print(DP[N] % MOD)
            
