A, B, C, X, Y = map(int, input().split())

sol = 0
if A + B > 2 * C:
    MIN = min(X, Y)
    sol += 2 * C * MIN
    if X > Y:
        sol += (X - Y) * min(A, 2*C)
    elif X < Y:
        sol += (Y - X) * min(B, 2*C)

else:
    sol = A * X + B * Y
    

print(sol)