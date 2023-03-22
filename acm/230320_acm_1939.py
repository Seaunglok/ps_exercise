import sys
sys.setrecursionlimit(10**9)
readl = sys.stdin.readline

N, M = map(int, readl().split())
A = [list(map(int, readl().split())) for _ in range(M)]
I = list(map(int, readl().split()))

G = [[] for _ in range(N+1)]
for a, b, c in A:
    G[a].append((b, c))
    G[b].append((a, c))
    
def check(node, limit):
    if visit[node]:
        return False
    
    visit[node] = True
    
    if node == end:
        return True
    
    for next, cost in G[node]:
        if cost >= limit:
            if check(next, limit):
                return True
    return False
    
left = 1
right = 1000000000

start = I[0]
end = I[1]
ans = 0

while left <= right:
    mid = (left + right) // 2
    
    visit = [0] * (N+1)    
    if check(start, mid):        
        left = mid + 1
    else:
        right = mid - 1

print(right)
        
    