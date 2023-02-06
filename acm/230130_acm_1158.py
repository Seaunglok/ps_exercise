import sys
from collections import deque
readl = sys.stdin.readline
N, K = map(int, readl().split())
que = deque(range(1, N+1))
ans = []
while que:
    que.rotate(-2)
    ans.append(que.popleft())

print("<",", ".join(str(i) for i in ans),">", sep='')
