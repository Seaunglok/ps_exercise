N = int(input())

DP = [0] * (N+1)
DP[1] = 1

def fibo(n):
    if n == 0:
        return DP[n]
    if n == 1:
        return DP[n]
    
    if DP[n] == 0:
        DP[n] = fibo(n-1) + fibo(n-2)
    
    return DP[n]

sol = fibo(N)
print(sol)



    

    
