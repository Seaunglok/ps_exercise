A = input()
B = input()

sol = []
len_a = len(A)
len_b = len(B)
for b in B[len_b::-1]:
    temp = 0
    for i, a in enumerate(A[len_a::-1]):        
        a = 10 ** i * int(a)
        temp += int(a) * int(b)
    sol.append(temp)

last = 0
for i, s in enumerate(sol):
    print(s)
    last += 10 ** i * s
print(last)
        
