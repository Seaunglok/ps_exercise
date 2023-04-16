from itertools import combinations

N = 9
A = [int(input()) for _ in range(N)]

A.sort()
# for a in combinations(A, 7):
#     if sum(a) == 100:
#         ans = a
#         break

# for i in ans:
#     print(i)

ans = []
def dfs(start, idx):
    # print(ans, start, idx)
    if idx == 7:
        if sum(ans) == 100:
            for a in ans:
                print(a)
            exit(0)
        else:
            return
    
    for i in range(start, len(A)):
        ans.append(A[i])
        dfs(i+1, idx+1)
        ans.pop()

dfs(0, 0)





