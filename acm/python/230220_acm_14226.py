import sys
from collections import deque

readl = sys.stdin.readline
N = int(readl())
MAX = 1001
check = [[0] * MAX for _ in range(MAX)]
def bfs():
    que = deque()
    que.append((1, 0, 0))
    
    check[1][0] = 1
    
    while que:
        display, board, cnt = que.popleft()
        # print(display, board, cnt)
        if display == N:
            return cnt
            
        for i in range(3):
            if i == 0:
                n_dis = display
                n_board = display
            elif i == 1:
                n_dis = display + board
                n_board = board
            elif i == 2:
                n_dis = display - 1
                n_board = board
            # print(n_dis, n_board, cnt)
        
            if n_dis not in range(MAX) or n_board not in range(MAX): continue
            if check[n_dis][n_board]: continue
            check[n_dis][n_board] = 1
            que.append((n_dis, n_board, cnt+1))

print(bfs())

