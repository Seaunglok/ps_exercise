A = input()

C = 26
D = 10

pre = ''
sol = 1

for a in A:
    if pre == a and a == 'c':
        C = 25
    elif pre == a and a == 'd':
        D = 9
    else:
        C = 26
        D = 10
    if a == 'c':
        sol *= C
    elif a == 'd':
        sol *= D
    pre = a
        
print(sol)
        
    
    