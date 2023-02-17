A, B = map(int, input().split())
N = int(input())
Arr = list(map(int, input().split()))

num = 0
idx = 0
for a in reversed(Arr):    
    num += a * (A ** idx)
    idx += 1

sol = []
while num:    
    sol.append(num % B)
    num //= B

print(*sol[::-1])
    
    