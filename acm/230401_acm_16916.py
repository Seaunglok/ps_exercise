S = input().rstrip()
P = input().rstrip()

sol = 0

def LPS(p):
    M = len(p)
    arr = [0] * M
    j = 0
    
    for i in range(1, M):
        while j > 0 and p[i] != p[j]:
            j = arr[j-1]
        if p[i] == p[j]:
            j += 1
            arr[i] = j
    return arr

def KMP(s, p):
    j = 0
    N = len(s)
    M = len(p)
    
    for i in range(N):
        while j > 0 and s[i] != p[j]:
            j = t[j-1]
            
        if s[i] == p[j]:
            if j == M - 1:
                return 1
            else:
                j += 1
    return 0


t = LPS(P)
sol = KMP(S, P)
print(sol)

        