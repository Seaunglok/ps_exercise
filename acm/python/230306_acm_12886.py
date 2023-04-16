from collections import deque

A, B, C = map(int, input().split())


def bfs():
    global total
    visit = [[0] * (total+1) for _ in range(total+1)]
    
    que = deque()
    que.append((A, B))    
    visit[A][B] = 1
    
    while que:
        x, y = que.popleft()
        z = total - (x + y)
        
        if x == y == z:
            print(1)
            return
        
        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a                
            elif a > b:
                a -= b
                b += b 
            else:
                continue
            
            c = total - (a + b)
            
            x = min(a, b, c)
            y = max(a, b, c)
        
            # print(a, b, c, x, y)
            
            if not visit[x][y]:
                visit[x][y] = 1
                que.append((x, y))       
    
    print(0)

total = A + B + C
if total % 3 != 0:
    print(0)
    exit(0)

bfs()