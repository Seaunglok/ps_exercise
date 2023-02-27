from collections import Counter

N = int(input())

A = [int(input()) for _ in range(N)]

AVG = 0
MID = 0
CNT = 0
RNG = 0

SUM = sum(A)
AVG = round(SUM / N)

A.sort()
MID = A[N//2]

a = Counter(A)
cnt = a.most_common(2)
if N > 1:
    if cnt[0][1] == cnt[1][1]:
        CNT = cnt[1][0]
    else:
        CNT = cnt[0][0]

else:    
    CNT = cnt[0][0]

MAX = max(A)
MIN = min(A)
RNG = MAX-MIN

print(AVG)
print(MID)
print(CNT)
print(RNG)

    