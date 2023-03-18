import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().strip()))
B = list(map(int, readl().strip()))

def change(A):
    rtn = 0
    M = A[:]
    for i in range(1, N):
        if M[i-1] != B[i-1]:
            rtn += 1
            M[i-1] = 1 - M[i-1]
            M[i] = 1 - M[i]
            if i != N-1:
                M[i+1] =  1 - M[i+1]                        
    if M == B:
        return rtn
    else:
        return 10**9

sol = change(A)

A[0] = 1 - A[0]
A[1] = 1 - A[1]
sol = min(sol, change(A)+1)

print(sol if sol != 10**9 else -1)
    
    
    
    
        
    
        
        

