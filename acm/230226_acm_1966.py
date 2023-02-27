from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = deque(map(int, input().split()))  
    cnt = 0
    while M != -1:        
        if A[0] == max(A):
            A.popleft()
            M -= 1
            cnt += 1
        else:
            A.append(A.popleft())
            if M == 0:
                M = len(A) - 1
            else:
                M -= 1
    print (cnt)
            
            
        
        
        
        


    



    
    