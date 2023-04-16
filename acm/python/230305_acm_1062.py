from itertools import combinations

N, K = map(int, input().split())
    
words = []
sol = 0

for _ in range(N):
    s = 0
    temp = input().strip()
    for x in temp:
        s |= (1 << (ord(x) - ord('a')))
    words.append(s)
    
if K < 5:
    print(0)
    exit(0)

app = ['a', 'n', 't', 'i', 'c']
candi = [i for i in range(26) if chr(i+97) not in app]


for comb in list(combinations(candi, K-5)):
    mask = 0
    cnt = 0
    for i in app:
        mask |= (1 << (ord(i) - ord('a')))
    for i in comb:
        mask |= 1 << i
    
    for word in words:
        # print(mask, word, mask&word)
        if mask & word == word:
            cnt += 1
            
    if sol < cnt:
        sol = cnt

print(sol)
    
    
            
        
            
