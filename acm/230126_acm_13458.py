N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N
for a in A:
    a = a - B
    if a > 0:
        if a % C:
            cnt += (a // C) + 1
        else:
            cnt += (a // C)

print(cnt)
    