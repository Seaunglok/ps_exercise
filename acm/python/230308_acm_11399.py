N = int(input())
A = list(map(int, input().split()))

A.sort()

presum = [0]
for a in A:
    presum.append(a+presum[-1])

print(sum(presum))
    