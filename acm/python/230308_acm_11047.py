N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.sort(reverse=True)

sol = 0
for a in A:
    if K % a == K:
        continue
    sol += K // a
    K %= a

print(sol)
    