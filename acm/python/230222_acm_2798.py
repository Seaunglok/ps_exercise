from itertools import combinations

N, M = map(int, input().split())
A = list(map(int, input().split()))
MIN = 300000

for a in combinations(A, 3):
    SUM = sum(a)
    sol = M - SUM
    if sol < 0: continue
    MIN = min(sol, MIN)
    
print(M - MIN)
