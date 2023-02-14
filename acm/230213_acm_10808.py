from collections import Counter

A = input().strip()

sol = [0] * 26
AA = Counter(A)

for a, cnt in AA.items():
    st = ord(a) - ord('a')
    sol[st] = cnt
    
print(*sol)
    