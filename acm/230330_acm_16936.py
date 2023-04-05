N = int(input())
A = list(map(int, input().split()))

L = []
for i in range(N):
    temp = A[i]
    cnt = 0
    while temp % 3 == 0:                        
        cnt += 1
        temp //= 3    
    L.append((cnt, A[i]))
        
L.sort(key=lambda x:(-x[0], x[1]))
        
for a in L:
    print(a[1], end=' ')
    
    
        
        