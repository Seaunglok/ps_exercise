from itertools import combinations

T = int(input())

for _ in range(T):
    A = list(map(int, input().split()))
    
    def gcd(a):
        x, y = a[0], a[1]
        
        while y > 0:
            x, y = y, x % y
        
        return x
    
    total = 0
    for a in combinations(A[1:], 2):
        total += gcd(a)
        # print(total)
        
    print(total)
        
    