N = int(input())
A = list(map(int, input().split()))

stack = [0]
sol = [-1] * N

for i in range(1, N):    
    
    while stack and A[stack[-1]] < A[i]:                
        idx = stack.pop()
        sol[idx] = A[i]
        # print(stack[-1], i, A[0])
    stack.append(i)

print(*sol)
        
    


        
        
        
        

