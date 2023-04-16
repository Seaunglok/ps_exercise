import sys
from collections import deque

readl = sys.stdin.readline

A = [list(map(int, readl().split())) for _ in range(3)]

start = 0
for i in range(3):
    for j in range(3):
        if A[i][j] == 0:
            A[i][j] = 9
        start = start * 10 + A[i][j]
        
q = deque()
q.append(start)
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
D = dict()
D[start] = 0

while q:
    now = q.popleft()
    now_str = str(now)
    z = now_str.find('9')
    dr = z // 3
    dc = z % 3
    # print(x, y, z)
    for rr, cc in move:
        nr = dr + rr
        nc = dc + cc
        if 0<=nr<3 and 0<=nc<3:
            temp = list(now_str)
            temp[dr*3+dc], temp[nr*3+nc] = temp[nr*3+nc], temp[dr*3+dc]
            num = int(''.join(temp))
            # print(num)
            if num not in D:
                D[num] = D[now] + 1
                q.append(num)
                
if 123456789 in D:
    print(D[123456789])
else:
    print(-1)