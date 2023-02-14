from collections import Counter

N = int(input())
A = list(map(int, input().split()))


arr = Counter(A)
# print(arr)
# arr = []
# for i in range(N):
#     arr.append(A.count(A[i]))

stack = [0]
sol = [-1] * N
for i in range(1, N):
    while stack and arr[A[stack[-1]]] < arr[A[i]]:
        idx = stack.pop()
        sol[idx] = A[i]
    stack.append(i)
    
print(*sol)
    