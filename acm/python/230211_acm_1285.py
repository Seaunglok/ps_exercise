from copy import deepcopy

N = int(input())
mat = [list(input().strip()) for _ in range(N)]
ans = 10**9
for bit in range(1<<N):
    # tmp = deepcopy(mat)
    tmp = [mat[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1<<i):
            for j in range(N):
                if tmp[i][j] == 'H':
                    tmp[i][j] = 'T'
                else:
                    tmp[i][j] = 'H'
    
    total = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if tmp[j][i] == 'T':
                cnt += 1
        total += min(cnt, N-cnt)
    ans = min(ans, total)

print(ans)

    
        
    