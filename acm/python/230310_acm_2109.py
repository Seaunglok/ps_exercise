import sys
from heapq import heapify, heappop, heappush
readl = sys.stdin.readline

N = int(readl())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x:x[1])

heap = []
for cost, day in A:
    heappush(heap, cost)
    if len(heap) > day:
        heappop(heap)

print(sum(heap))
    


    
    



    



