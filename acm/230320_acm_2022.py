import math

X, Y, C = map(float, input().split())

def check(D):
    h1 = math.sqrt(X**2 - D**2)
    h2 = math.sqrt(Y**2 - D**2)
    h = (h1*h2) / (h1+h2)
    
    return h    

left = 0
right = min(X, Y)
sol = 0
while right - left > 0.000001:
    mid = (left + right) / 2
    
    if check(mid) > C:
        sol = mid
        left = mid
    else:
        right = mid
        
print(sol)
        
        