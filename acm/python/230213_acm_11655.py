A = input()
sol = ""

# print(chr(ord('k') + 13))
for a in A:
    if a.isalpha() and a.isupper():
        rtn = ord(a) + 13
        if rtn > ord('Z'):
            rtn = ord(a) - 13
        sol += chr(rtn)
    elif a.isalpha and a.islower():
        rtn = ord(a) + 13
        if rtn > ord('z'):
            rtn = ord(a) - 13
        sol += chr(rtn)
    else:
        sol += a

print(sol)
        
    
