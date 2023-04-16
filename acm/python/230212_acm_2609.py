N, M = map(int, input().split())

min_ = 0

flag = M
last = 0

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        # print(a, b)
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(N, M))
print(lcm(N, M))
    

    