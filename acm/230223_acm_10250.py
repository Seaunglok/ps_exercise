T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    d, m = divmod(N, H)
    d = d + 1
    if m == 0:
        d = N//H
        m = H * 100
    else:
        m = m * 100

    print(m+d)
