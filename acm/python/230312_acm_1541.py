import sys
readl = sys.stdin.readline

A = input().rsplit('-')

sol = []
for a in A:
    temp = list(map(int, a.split('+')))
    sol.append(sum(temp))

ans = sol[0]
for s in sol[1:]:
    ans -= s

print(ans)

    