N = int(input())
A = list(map(int, input().split()))

max_ = 1001
def isprime():
    prime = [1] * max_
    prime[0] = 0
    prime[1] = 0
    m = int(max_ ** 0.5)
    for i in range(2, m+1):
        if prime[i]:
            for j in range(i+i, max_, i):
                prime[j] = 0
    return prime


sol = 0
prime = isprime()
# print(prime)
for i in range(N):
    if prime[A[i]]:
        sol += 1

print(sol)
        