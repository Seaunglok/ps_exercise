import sys

readl = sys.stdin.readline

N = int(readl())
A = [readl().split() for _ in range(N)]


st = ""
for aa in A:   
    ans = "" 
    for a in aa:    
        stack = []   
        n = len(a)
        for i in range(n-1, -1, -1):
            stack.append(a[i])            
            st = "".join(stack)
        ans += st + " "
    print(ans)
        
            
        
    
    
      
          
    
