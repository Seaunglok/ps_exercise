import sys
from collections import deque
readl = sys.stdin.readline

N = int(readl())
que = deque()
for _ in range(N):
    A = readl().split()
    if A[0] == "push_front":
        que.appendleft(A[1])        
    elif A[0] == "push_back":
        que.append(A[1])
    elif A[0] == "pop_front":
        if not len(que):
            print(-1)
        else:
            print(que.popleft())
    elif A[0] == "pop_back":
        if not len(que):
            print(-1)
        else:
            print(que.pop())
    elif A[0] == "size":
        print(len(que))
    elif A[0] == "empty":
        if not len(que):
            print(1)
        else:
            print(0)
    elif A[0] == "front":
        if not len(que):
            print(-1)
        else:
            print(que[0])
    elif A[0] == "back":
        if not len(que):
            print(-1)
        else:
            print(que[-1])