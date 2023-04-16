N = int(input())
W = list(map(int, input().split()))

MAX = 0

def dfs(total):
    global MAX
    if len(W) == 2:
        if MAX < total:
            MAX = total
        return
    
    for i in range(1, len(W)-1):
        energy = W[i-1] * W[i+1]
        k = W[i]
        del W[i]
        dfs(total+energy)
        W.insert(i, k)

dfs(0)

print(MAX)