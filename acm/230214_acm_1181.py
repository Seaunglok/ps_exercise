N = int(input())
A = [input() for _ in range(N)]

A.sort(key=lambda x: (len(x), x))
stack = []
for a in A:
    if a not in stack:
        stack.append(a)

for st in stack:
    print(st)



    
    
    
    
    