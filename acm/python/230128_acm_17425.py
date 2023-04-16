import sys
readl = sys.stdin.readline
T = int(readl())

for _ in range(T):
    N = int(readl())
    ans = 0
    for i in range(1, N+1):
        ans += (N//i)*i
    print(ans)     
    