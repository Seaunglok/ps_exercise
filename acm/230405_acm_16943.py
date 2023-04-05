from itertools import permutations

A, B = map(str, input().split())

sol = -1
for i in permutations(A):
    a = ''.join(i)    
    if a[0] == '0':
        continue    
    if int(a) < int(B):
        sol = max(sol, int(a))

print(sol)
    
