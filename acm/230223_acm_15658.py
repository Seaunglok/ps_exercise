N = int(input())
A = list(map(int, input().split()))
OP = list(map(int, input().split()))

MIN = 10**9
MAX = -10**9

def dfs(idx, sol, plus, minus, mul, div):
    global MIN, MAX
    if idx >= N:
        MIN = min(MIN, sol)
        MAX = max(MAX, sol)
        return
        
    if plus > 0:
        dfs(idx+1, sol+A[idx], plus-1, minus, mul, div)
    if minus > 0:
        dfs(idx+1, sol-A[idx], plus, minus-1, mul, div)
    if mul > 0:
        dfs(idx+1, sol*A[idx], plus, minus, mul-1, div)
    if div > 0:
        dfs(idx+1, int(sol/A[idx]), plus, minus, mul, div-1)

dfs(1, A[0], OP[0], OP[1], OP[2], OP[3])

print(MAX)
print(MIN)
    





