import sys
from heapq import heapify, heappop, heappush
readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
    N = int(readl())
    
    max_heap = []
    min_heap = []
    visit = [0] * N
    
    for i in range(N):
        op, num = map(str, readl().split())
        if op == 'I':
            heappush(max_heap, (-int(num), i))
            heappush(min_heap, (int(num), i))
            visit[i] = 1
        elif op == 'D':            
            if num == '-1':
                # print(min_heap)
                while min_heap and not visit[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = 0
                    heappop(min_heap)
            else:
                # print(max_heap)
                while max_heap and not visit[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = 0
                    heappop(max_heap)
    
    while min_heap and not visit[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heappop(max_heap)
        
    if not min_heap and not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
                    
                
                
                
                
        
    