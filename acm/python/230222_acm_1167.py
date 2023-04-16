import sys
sys.setrecursionlimit(10**9)
readl = sys.stdin.readline

N = int(readl())
G = [[] for _ in range(N+1)]
check = [-1] * (N+1)

def make_graph(arr):
    idx = 1
    while True:
        if arr[idx] == -1:
            break
        G[arr[0]].append([arr[idx], arr[idx+1]])
        idx += 2    
        
for i in range(1, N+1):
    A = list(map(int, readl().split()))
    make_graph(A)       
    # for ii in range(1, len(A)-2, 2):
        # G[A[0]].append([A[ii], A[ii+1]])
        
        
def dfs(node, dist):
    for next, next_dist in G[node]:
        if check[next] == -1:      
            check[next] = dist + next_dist
            dfs(next, dist+next_dist)     

check[1] = 0
dfs(1, 0)
idx = check.index(max(check))

check = [-1] * (N+1)
check[idx] = 0
dfs(idx, 0)
print(max(check))
    
        
    