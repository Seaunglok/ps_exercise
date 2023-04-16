import sys
readl = sys.stdin.readline

while True:    
    A = readl().rstrip('\n')
    if len(A) == 0:
        break
    sol = [0] * 4
    # print(A)
    for a in A:
        # print(a, sol)
        if a.isupper():
            sol[1] += 1
        elif a.islower():
            sol[0] += 1
        elif a == ' ':
            sol[3] += 1
        elif a.isnumeric():
            sol[2] += 1
    
    print(*sol)