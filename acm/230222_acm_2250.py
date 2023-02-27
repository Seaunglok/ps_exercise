N = int(input())
G = [[] for _ in range(N+1)]
parent = [0] * (N+1)

A = [[] for _ in range(N+1)]

cnt = 1
def inorder(node, depth):
    global cnt
    if node == -1: return
    inorder(G[node][0], depth+1)
    A[depth].append(cnt)
    cnt += 1
    inorder(G[node][1], depth+1)    


for _ in range(N):
    a, b, c = map(int, input().split())
    G[a] = [b, c]
    if b != -1:
        parent[b] += 1
    if c != -1:
        parent[c] += 1
        
for i in range(1, N+1):
    if parent[i] == 0:
        root = i    

inorder(root, 1)

# print(A)

width = max(A[1]) - min(A[1]) + 1
idx = 1
for i in range(2, N+1):
    if A[i]:
        min_width = min(A[i])
        max_width = max(A[i])
        cal_width = max_width - min_width
        
        if width < cal_width+1:
            width = cal_width+1
            idx = i

print(idx, width)
        
        
        
    
