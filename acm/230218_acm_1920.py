import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().split()))
M = int(readl())
B = list(map(int, readl().split()))

A.sort()

def find(num):
    start = 0 
    end = N - 1
    
    while start<=end:
        m = (start+end) // 2
        # print(start, end, m, num)
        if num == A[m]:
            return True
        elif num > A[m]:
            start = m + 1
        else:
            end = m - 1
            
    return False
  
        
for b in B:
    if find(b):
        print(1)
    else:
        print(0)
            


        
