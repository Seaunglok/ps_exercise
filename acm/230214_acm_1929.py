N, M = map(int, input().split())

def isprime(M):
    prime = [1] * (M+1)
    prime[1] = 0
    m = int(M**0.5)
    
    for i in range(2, m+1):
        if prime[i]:
            for j in range(i+i, M+1, i):
                prime[j] = 0
    return prime

prime = isprime(M)

for i in range(N, M+1):
    if prime[i]:
        print(i)
    
    
    