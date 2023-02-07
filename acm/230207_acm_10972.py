N = int(input())
A = list(map(int, input().split()))

idx = 0
for i in range(N-1, 0, -1):
    if A[i-1] < A[i]:
        idx = i-1
        break
else:
    print(-1)
    exit(0)
    
for i in range(N-1, 0, -1):
    if A[idx] < A[i]:
        A[idx], A[i] = A[i], A[idx]
        A = A[:idx+1] + sorted(A[idx+1:])
        print(*A)
        break
    
        
        

