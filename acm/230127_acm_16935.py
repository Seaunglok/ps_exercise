R, C, A = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(R)]
B = list(map(int, input().split()))

def first(m):
    rr = len(m)
    cc = len(m[0])    
    mat_ = [[0] * cc for _ in range(rr)]
    
    for r in range(rr):
        for c in range(cc):
            mat_[r][c] = m[rr-1-r][c]
    return mat_

def second(m):
    rr = len(m)
    cc = len(m[0])    
    mat_ = [[0] * cc for _ in range(rr)]
    
    for r in range(rr):
        for c in range(cc):
            mat_[r][c] = m[r][cc-1-c]
    return mat_

def third(m):
    rr = len(m)
    cc = len(m[0])
    mat_ = [[0] * rr for _ in range(cc)]
    # print(rr, cc)
    
    for r in range(rr):
        for c in range(cc):
            # print(r, c)
            mat_[c][r] = m[rr-1-r][c]
    return mat_

def forth(m):
    rr = len(m)
    cc = len(m[0])    
    mat_ = [[0] * rr for _ in range(cc)]
    
    for r in range(rr):
        for c in range(cc):
            mat_[c][r] = m[r][cc-1-c]
    return mat_

def fifth(m):
    rr = len(m)
    cc = len(m[0])
    midr = rr // 2
    midc = cc // 2
    
    mat_ = [[0] * cc for _ in range(rr)]
    for r in range(midr):
        for c in range(midc):
            mat_[r][c] = m[rr-midr+r][c]
    for r in range(midr):
        for c in range(midc, cc):
            mat_[r][c] = m[r][c-midc]
    for r in range(midr, rr):
        for c in range(midc):
            mat_[r][c] = m[r][cc-midc+c]
    for r in range(midr, rr):
        for c in range(midc, cc):
            mat_[r][c] = m[r-midr][c]
    return mat_

def sixth(m):
    rr = len(m)
    cc = len(m[0])
    midr = rr // 2
    midc = cc // 2
    
    mat_ = [[0] * cc for _ in range(rr)]
    for r in range(midr):
        for c in range(midc):
            mat_[r][c] = m[r][cc-midc+c]
    for r in range(midr):
        for c in range(midc, cc):
            mat_[r][c] = m[rr-midr+r][c]
    for r in range(midr, rr):
        for c in range(midc):
            mat_[r][c] = m[r-midr][c]
    for r in range(midr, rr):
        for c in range(midc, cc):
            mat_[r][c] = m[r][c-midc]
    return mat_            

for b in B:
    if b == 1:
        mat = first(mat)
    elif b == 2:
        mat = second(mat)
    elif b == 3:
        mat = third(mat)
    elif b == 4:
        mat = forth(mat)
    elif b == 5:
        mat = fifth(mat)
    elif b == 6:
        mat = sixth(mat)

for m in mat:
    print(*m)
    
