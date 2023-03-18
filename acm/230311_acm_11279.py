import sys
from heapq import heapify, heappop, heappush
readl = sys.stdin.readline

N = int(readl())
A = [int(readl()) for _ in range(N)]
heap = []
for a in A:    
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -a)   
          
