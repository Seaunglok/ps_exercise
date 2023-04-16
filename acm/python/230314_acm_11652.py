import sys
from collections import Counter
readl = sys.stdin.readline

N = int(readl())
A = [int(readl()) for _ in range(N)]

cnt = Counter(A)
sol = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))
print(sol[0][0])
