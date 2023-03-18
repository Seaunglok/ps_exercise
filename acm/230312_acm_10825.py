import sys
readl = sys.stdin.readline

N = int(readl())
A = [list(readl().split()) for _ in range(N)]

A.sort(key=lambda x: x[0])
A.sort(key=lambda x: int(x[3]), reverse=True)
A.sort(key=lambda x: int(x[2]))
A.sort(key=lambda x: int(x[1]), reverse=True)

for a in A:
    print(a[0])