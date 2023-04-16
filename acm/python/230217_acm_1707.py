T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        # G[b].append(a)
        
    
    check = [0] * (V+2)
    cnt = 0 
    def dfs(start):
        for i in G[start]:
            if check[i]: continue
            check[i] = 1
            dfs(i)
    
    for i in range(1, V+1):
        # print(i, check)
        if check[i]: continue
        check[i] = 1
        dfs(i)
        cnt += 1
    
    # print(cnt)
        
    if cnt == 2:
        print("YES")
    else:
        print("NO")
        
    