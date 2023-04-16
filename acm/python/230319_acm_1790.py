N, K = map(int, input().split())

digit = 1
num = 9
sol = 0

while K > digit * num:
    K -= digit * num
    sol += num
    digit += 1
    num *= 10

sol += ((K-1) // digit) + 1

if sol > N:
    print(-1)
else:
    print(str(sol)[(K-1) % digit])
    