import sys
readl = sys.stdin.readline

N = int(readl())
A = [list(readl().strip()) for _ in range(N)]

for a in A:
    # print("hi")
    stack = []
    flag = True
    for aa in a:
        if aa == '(':
            stack.append(aa)
        elif aa == ')':
            if len(stack) == 0:
                print("NO")
                flag = False
                break            
            stack.pop()
    
    if flag:
        if len(stack):
            print("NO")
        else:        
            print("YES")
    
