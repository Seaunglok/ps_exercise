from collections import deque

N = int(input())
card = deque([i for i in range(1, N+1)])
# print(card)

idx = 1
while len(card) != 1:
    if idx % 2:
        card.popleft()
    else:
        card.append(card.popleft())
    idx += 1
    
print(*card)

    
    