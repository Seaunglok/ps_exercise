N = int(input())

if N == 1:
    print('')
    exit(0)
idx = 2
while N != 1:
    # print(N)
    if (N % idx) == 0:
        print(idx)
        N //= idx
    else:
        idx += 1
    
    