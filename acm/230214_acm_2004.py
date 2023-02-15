N, M = map(int, input().split())

def find_five(n):
    cnt = 0
    while n:
        cnt += n // 5
        n //= 5
    return cnt

def find_two(n):
    cnt = 0
    while n:
        cnt += n // 2
        n //= 2
    return cnt

five = find_five(N) - find_five(M) - find_five(N-M)
two = find_two(N) - find_two(M) - find_two(N-M)

sol = min(five, two)

print(sol)
        