
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
stack = []
check = [0] * (N+1)
def dfs(node):
    if check[node]: return
    
    check[node] = 1
    stack.append(node)
    
    for g in sorted(graph[node]):
        dfs(g)
    
que = []    
rtn = []
def bfs(node):
    que.append(node)
    check[node] = 1
    rtn.append(node)
    
    while que:
        q = que.pop(0)
        for g in sorted(graph[q]):
            if check[g]: continue
            que.append(g)
            check[g] = 1
            rtn.append(g)

dfs(V)
for s in stack:
    print(s, end=" ")
print()
check = [0] * (N+1)
bfs(V)
for r in rtn:
    print(r, end=" ")