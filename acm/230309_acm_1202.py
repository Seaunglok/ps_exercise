import sys
from heapq import heapify, heappop, heappush
readl = sys.stdin.readline

N, K = map(int, readl().split())
A = [list(map(int, readl().split())) for _ in range(N)]
B = [int(readl()) for _ in range(K)]

A.sort(key=lambda x: x[0])
B.sort()

heap = []
sol = 0
for b in B:
    while len(A) != 0 and A[0][0] <= b:
        heappush(heap, -heappop(A)[1])
    
    if heap:
        sol -= heappop(heap)

print(sol)
        
        





