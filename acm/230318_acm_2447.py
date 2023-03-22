N = int(input())
star = ['***', '* *', '***']
cnt = 0 

def solve(n):
    global star
    if n == 3:
        return star
        
    stars = solve(n//3)
    mat = []
    
    for i in stars:
        mat.append(i*3)
    
    for i in stars:
        mat.append(i + ' '*(n//3) + i)
    
    for i in stars:
        mat.append(i*3)        
        
    return mat    
        
sol = solve(N)

for s in sol:
    print(s)
    


