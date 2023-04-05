import sys
sys.setrecursionlimit(10**6)
readl = sys.stdin.readline

N, M = map(int, readl().split())
A = [i for i in range(N+1)]

def find(x):
    if x != A[x]:
        A[x] = find(A[x])
    return A[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        a, b = b, a
    A[a] = b        

for _ in range(M):
    c, a, b = map(int, readl().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")


