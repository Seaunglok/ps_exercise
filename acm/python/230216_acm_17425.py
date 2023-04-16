import sys
readl = sys.stdin.readline

MAX = 1000001
DP = [1] * MAX
S = [0] * MAX

for i in range(2, MAX):
    j = 1
    while i*j <= MAX-1:
        DP[i*j] += i
        j += 1
        
for i in range(1, MAX):
    S[i] = S[i-1] + DP[i]
        
        
T = int(readl())
for _ in range(T):
    N = int(readl())
    print(S[N])
    