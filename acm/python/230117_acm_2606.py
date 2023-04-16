N = int(input())
V = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(V):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    

cnt = 0
check = [0] * (N+1)
def dfs(node):
    global cnt
    if check[node]: return
    check[node] = 1
    cnt += 1
    # print(cnt, node)
    for g in graph[node]:
        if not check[g]:
            dfs(g)   
    
dfs(1)
    
print(cnt-1)