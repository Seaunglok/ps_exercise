A = [int(input()) for _ in range(10)]

A = set(a % 42 for a in A)
print(len(A))
