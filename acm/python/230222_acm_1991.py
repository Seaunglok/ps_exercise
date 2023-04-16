from collections import defaultdict

N = int(input())
T = defaultdict()

for _ in range(N):
    a, b, c = input().split()
    T[a] = [b, c]

def preorder(node):
    if node == '.': return
    print(node, end='')
    preorder(T[node][0])
    preorder(T[node][1])
    
def inorder(node):
    if node == '.': return
    inorder(T[node][0])
    print(node, end='')
    inorder(T[node][1])
    
def postorder(node):
    if node == '.': return
    postorder(T[node][0])
    postorder(T[node][1])
    print(node, end='')
    
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
