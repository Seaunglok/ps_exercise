N = int(input())

final_num = 666
cnt = 0

while N:
    if '666' in str(final_num):
        cnt += 1
    
    if N == cnt:
        break
        
    final_num += 1
    
print(final_num)