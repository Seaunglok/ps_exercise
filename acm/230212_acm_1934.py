T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    def gcd(a, b):
        while b > 0:
            a, b = b, a%b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    print(lcm(N, M))