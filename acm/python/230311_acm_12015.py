import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().split()))

def binary(target):    
    start = 0
    end = len(stack)
    
    while start <= end:
        mid = (start+end) // 2
        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

stack = [0]
for a in A:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[binary(a)] = a
        
print(len(stack) - 1)
    
