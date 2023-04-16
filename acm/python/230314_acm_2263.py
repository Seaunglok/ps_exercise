import sys
sys.setrecursionlimit(10**9)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (N+1)
for i in range(N):
    pos[inorder[i]] = i

def dfs(in_s, in_e, po_s, po_e):
    if in_s > in_e or po_s > po_e:
        return
    
    root = postorder[po_e]
    print(root, end=' ')
    
    idx = pos[root]
    left = idx - in_s
    right = in_e - idx
    
    dfs(in_s, idx-1, po_s, po_s+left-1)
    dfs(idx+1, in_e, po_e-right, po_e-1)

dfs(0, N-1, 0, N-1)