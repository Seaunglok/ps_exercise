
while True:
    try:
        N = int(input())
    except:
        break
    num = 0
    cnt = 1
    
    while True:
        num = num*10 + 1
        num %= N
        if num == 0:
            print(cnt)
            break
        cnt += 1
        