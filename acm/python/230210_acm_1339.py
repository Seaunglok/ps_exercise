from collections import defaultdict
N = int(input())
A = [list(input().strip()) for _ in range(N)]

dd = defaultdict(int)

for a in A:
    for i, word in enumerate(a[::-1]):
        dd[word] += 10**i
        
dd = dict(sorted(dd.items(), key=lambda v: v[1], reverse=True))

n = 9
sol = 0
for k, v in dd.items():
    sol += v * n
    n -= 1

print(sol)    
    

