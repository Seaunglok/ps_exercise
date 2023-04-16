N = int(input())

DP = [0, 1]

def fibo(n):      
    if n < len(DP):
        return DP[n]
    
    DP.append(fibo(n-1) + fibo(n-2))    
    
    return DP[n]
    

sol = fibo(N)
print(sol)