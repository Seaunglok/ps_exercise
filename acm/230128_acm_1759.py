from itertools import combinations

L, C = map(int, input().split())
A = list(input().split())
vowel = set(['a', 'e', 'i', 'o', 'u'])
ans = []
A.sort()

def make_pass():
    for aa in list(combinations(A, L)):
        vo_cnt = 0
        co_cnt = 0
        for a in aa:
            if a in vowel:
                vo_cnt += 1
            else:
                co_cnt += 1
                
        if vo_cnt > 0 and co_cnt > 1:
            ans.append("".join(aa))

make_pass()

for an in ans:
    print(an)


