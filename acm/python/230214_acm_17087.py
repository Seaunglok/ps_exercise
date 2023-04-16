N, S = map(int, input().split())
A = list(map(int, input().split()))
sol = 0

M = []
for a in A:
    x = abs(S - a)
    if x == 0:
        continue
    M.append(x)    

def find_(a, b):        
    while b:
        a, b = b, a % b
    return a

sol = M[0]
for i in range(1, len(M)):
    sol = find_(M[i], sol)

print(sol)
        
        
        
        
    