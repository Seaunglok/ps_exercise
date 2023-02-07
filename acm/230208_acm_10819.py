N = int(input())
A = list(map(int, input().split()))

ans = []
sol = []
check = [0] * (N)
def dfs(idx):
    if idx == N:
        sol.append(tuple(ans))
        return
    
    for i in range(N):
        if check[i]: continue
        check[i] = 1
        ans.append(A[i])
        dfs(idx+1)
        ans.pop()
        check[i] = 0
dfs(0)

rtn = 0
total = 0
for s in sol:    
    total = 0    
    for i in range(len(s)-1):
        total += abs(s[i]-s[i+1])
        # print("t", total)
    # print(total, rtn, s)
    rtn = max(rtn, total)

print(rtn)
    