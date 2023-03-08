N = int(input())

SUM = 0
for i in range(1, N+1):
    SUM = i + sum(map(int, str(i)))
    
    if SUM == N:
        print(i)
        break
    if i == N:
        print(0)
        break
 