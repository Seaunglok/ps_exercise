while True:
    N = int(input())
    if N == 0:
        break
    
    N = str(N)
    lenN = len(N)
    m = lenN // 2
    
    for i in range(m):
        if N[i] != N[lenN-1-i]:
            print("no")
            break
    else:
        print("yes")
            

    
