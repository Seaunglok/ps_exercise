N = input() 
L = len(N)
 
ans = 0
 
for i in range(L-1):
    ans += 9 * (10**i) * (i+1)

ans += (int(N) - 10**(L-1) + 1) * L

print(ans)
    
 
 