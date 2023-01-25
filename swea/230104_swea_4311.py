def calc(q, n, op):
    rtn = 0
    if op == 1:
        rtn = q + n
    elif op == 2:
        rtn = q - n
    elif op == 3:
        rtn = q * n
    elif op == 4:
        if n == 0:
            return -1
        rtn = q // n
    if 0<= rtn < 1000:
        return rtn
    else:
        return -1
    
def recur(cur, x):
    if cur == 3:
        return
    for n in num_list:
        next = x * 10 + n
        # print(n, x, next)
        if visit[next] <= cur + 1:
            continue
        visit[next] = cur + 1
        que.append(next)
        nums.append(next)
        recur(cur+1, next)    

T = int(input())
for t in range(1, T+1):
    N, O, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    #1: 더하기, 2: 빼기, 3: 곱하기, 4: 나누기
    oper = list(map(int, input().split()))
    goal = int(input())
    nums = []    
        
    INF = M+1
    visit = [INF] * 1000
    que = []
    recur(0, 0)
        
    if visit[goal] < INF:
        print(f'#{t} {visit[goal]}')
        continue
    
    while que:
        q = que.pop(0)
        for n in nums:
            click = visit[q] + len(str(n)) + 1
            if click + 1 > M:
                continue
            for op in oper:
                next = calc(q, n, op)
                if next == -1:
                    continue
                if visit[next] <= click:
                    continue
                visit[next] = click
                que.append(next)
            
    if visit[goal] < INF:
        print(f'#{t} {visit[goal] + 1}')
    else:
        print(f'#{t} -1')
                
    
    
    
    