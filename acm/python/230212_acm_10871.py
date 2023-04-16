N, M = map(int, input().split())
A = list(map(int, input().split()))

sol = []

for a in A:
    if a < M:
        sol.append(a)
        
print(*sol)