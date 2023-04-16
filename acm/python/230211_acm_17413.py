S = list(input().strip())

# print(S)

ans = ""
stack = ""
idx = 0
basket = 0

for s in S:
    if s == '<':
        basket = 1
        ans += stack[::-1]
        stack = ""
        ans += s
        continue
    elif s == '>':
        basket = 0
        ans += s
        continue
    elif s == ' ':
        ans += stack[::-1] + s
        stack = ""
        continue
    
    if basket:
        ans += s
    else:
        # print(stack, s)
        stack += s

print(ans+stack[::-1])        
        
#     elif s == '>':
#         basket = 0
#         stack.append(s)
#     elif ord('a') <= ord(s) <= ord('z') and basket == 1:
#         stack.append(s)
#     elif ord('a') <= ord(s) <= ord('z') and basket == 0:
        
        
            
    
    
    
    