import sys
readl = sys.stdin.readline

N = int(readl())
A = [int(readl()) for _ in range(N)]
ans = ""
stack = []
n = 1
flag = False
for a in A:    
    while n <= a:
        stack.append(n)
        ans += "+"
        n += 1
    
    if stack[-1] == a:
        stack.pop()
        ans += "-"
    else:
        print("NO")
        exit(0)

for a in ans:
    print(a)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    