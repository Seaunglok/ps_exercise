S = input()
T = input()

def dfs(t):
    if t == S:
        return 1
    if len(t) <= len(S):
        return 0
    
    ans = 0
    if t[-1] == 'A':
        ans = dfs(t[:-1])
    if ans == 1:
        return 1
    if t[0] == 'B':
        ans = dfs(t[:0:-1])
    return ans   

print(dfs(T))