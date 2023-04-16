A, B, C = map(int, input().split())

def solve(a, b):
    if b == 1:
        return a % C
    if b % 2 == 0:
        return (solve(a, b//2) ** 2) % C
    else:
        return ((solve(a, b//2) ** 2) * a) % C


print(solve(A, B))