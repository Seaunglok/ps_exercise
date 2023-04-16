from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))
R = deque([0] * N)
ans = 0

while True:
    # print(A)
    A.rotate(1)
    # print(A)
    R.rotate(1)
    R[-1] = 0
    ans += 1
    
    for i in range(N-2, -1, -1):
        if A[i+1] >= 1 and R[i+1] == 0 and R[i] == 1:
            R[i+1] = 1
            R[i] = 0
            A[i+1] -= 1
    R[-1] = 0
    
    if not R[0] and A[0]:
        R[0] = 1
        A[0] -= 1
        
    if A.count(0) >= K:
        print(ans)
        break