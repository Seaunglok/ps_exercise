from collections import deque

A, B = map(int, input().split())

que = deque()
cnt = 0
que.append((A, cnt))

while que:
    num, cnt = que.popleft()
    if num > B:
        continue
    if num == B:
        print(cnt+1)
        break 
    
    que.append((int(str(num)+'1'), cnt+1))
    que.append((num*2, cnt+1))
else:
    print(-1)
        
    

