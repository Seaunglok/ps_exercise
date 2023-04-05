import sys
readl = sys.stdin.readline

N = int(readl())
A = [int(readl()) for _ in range(N)]

sol = 0
stack = []
for a in A:    
    while stack and stack[-1][0] < a:
        sol += stack.pop()[1]
        
    if not stack:
        stack.append((a, 1))
    else:
        if stack[-1][0] == a:
            cnt = stack.pop()[1]
            sol += cnt            
            if stack:
                sol += 1                
            stack.append((a, cnt+1))
        else:
            stack.append((a, 1))
            sol += 1
    
print(sol)
            
            
            
            
        
    
    
    
    