import sys
readl = sys.stdin.readline

N = int(readl())
A = list(map(int, readl().split()))

temp = []
for i, a in enumerate(A):
    temp.append((a, i))    
temp.sort()

sol = []
num = 0
pre_t = temp[0][0]
for t, i in temp:
    if pre_t != t:        
        num += 1        
    sol.append((i, num))
    pre_t = t

sol.sort()
for s in sol:
    print(s[1], end=' ')

    
    

    