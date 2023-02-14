A = list(input().strip())

stack = []
sol = 0
for i, a in enumerate(A):
    if a == '(':        
        stack.append((a, i))
    elif a == ')':
        b, idx = stack.pop()
        if idx+1 == i:
            sol += len(stack)
        else:
            sol += 1
    
print(sol)
            
            
        
        
    