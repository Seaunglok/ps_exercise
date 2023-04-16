N = int(input())

MOD = 1000000
sol = 0

M = [[1, 1], [1, 0]]
F = [0, 1]

def mul(m1, m2):
    rtn = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                rtn[i][j] += m1[i][k] * m2[k][j] % MOD
    return rtn

def power(a, b):
    if b == 1:
        return a
    else:
        tmp = power(a, b//2)
        if b % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), a)
        
sol = power(M, N)
print(sol[0][1] % MOD)