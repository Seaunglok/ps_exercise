import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().split()))
M = int(readl())
B = list(map(int, readl().split()))

A.sort()

def find(num):    
    start = 0
    end = N-1
    
    while start<=end:
        mid = (start+end)//2
        if A[mid] == num:
            return 1        
        elif A[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return 0
            

for b in B:
    print(find(b), end=' ')