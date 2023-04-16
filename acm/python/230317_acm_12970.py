N, K = map(int, input().split())

A = 0
B = N

while A*B < K and B > 0:
    A += 1
    B -= 1
    
if K == 0:
    print('B'*N)
elif B == 0:
    print(-1)

remain = K - (A-1)*B

# print(A, B, remain)

print('A'*(A-1) + 'B'*(B-remain) + 'A' + 'B'*remain)

    