import sys

readl = sys.stdin.readline

V, E = map(int, readl().split())

G = [] * (V+1)
P = [0] * (V+1)
for _ in range(E):
    s, e, c = map(int, readl().split())
    G.append((c, s, e))
    
for i in range(V):
    P[i] = i        
    
def find(x):
    if P[x] != x:
        P[x] = find(P[x])
    return P[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        x, y = y, x
    P[x] = y

sol = 0
    
G.sort()
for g in G:
    cost, start, end = g
    if find(start) != find(end):
        union(start, end)
        sol += cost

print(sol)
        
    
    
    
    