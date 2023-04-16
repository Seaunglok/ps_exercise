H, M = map(int, input().split())

time = 45

if M - time < 0:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60 + (M - time)
else:
    M = M - time
    

print(H, M)
        
    