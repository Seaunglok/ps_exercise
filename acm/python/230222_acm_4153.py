while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    A = [a, b, c]
    A.sort()
    
    if A[0]**2 + A[1]**2 == A[2]**2:
        print("right")
    else:
        print("wrong")
    