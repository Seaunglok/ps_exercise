K, N = map(int, input().split())
A = [int(input()) for _ in range(K)]

start = 1
end = max(A)

while start <= end:
    mid = (start+end) // 2
    # print(start, end, mid)
    cnt = 0
    
    for a in A:
        cnt += a // mid
        
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
    
        
        
        