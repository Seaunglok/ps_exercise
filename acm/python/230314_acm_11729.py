N = int(input())

def dfs(n, fr, to, other):
    if n == 0:
        return
    dfs(n-1, fr, other, to)
    print(fr, to)
    dfs(n-1, other, to, fr)

print(2**N-1)
dfs(N, 1, 3, 2)