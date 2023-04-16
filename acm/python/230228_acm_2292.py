N = int(input())

i = 0
L = 1
if N == 1:
    print(L)
    exit(0)
while True:
    L += 6 * i
    # print(L)
    if N <= L:
        break
    i += 1
    
print(i+1)