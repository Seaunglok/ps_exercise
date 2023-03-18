N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x:(x[1], x[0]))

sol = 1
st, e = A[0]
for start, end in A[1:]:
    if start >= e:
        sol += 1
        e = end

print(sol)
    