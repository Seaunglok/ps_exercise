from heapq import heapify, heappop, heappush

N = int(input())
A = [int(input()) for _ in range(N)]

left = []
right = []
sol = []

for i in range(N):
    if len(left) == len(right):
        heappush(left, (-A[i], A[i]))        
    else:
        heappush(right, (A[i], A[i]))        
        
    if right and left[0][1] > right[0][1]:
        max_left = heappop(left)[1]
        min_right = heappop(right)[1]
        
        heappush(left, (-min_right, min_right))
        heappush(right, (max_left, max_left))
        
    sol.append(left[0][1])
    
for s in sol:
    print(s)
    
        
    



