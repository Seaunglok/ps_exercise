D, N = input().split()
dc, dr = map(int, input().split())

def find(r, c, idx, size):
    global R, C
    if size == 1:
        R, C = r, c
        return 
    
    if N[idx] == '2':
        find(r, c, idx+1, size//2)
    elif N[idx] == '1':
        find(r, c+size//2, idx+1, size//2)
    elif N[idx] == '3':
        find(r+size//2, c, idx+1, size//2)
    else:
        find(r+size//2, c+size//2, idx+1, size//2)
        
def solve(r, c, size, rr, cc):
    global ans
    if size == 1:
        print(ans)
        return
    
    if rr < r+size//2 and cc < c+size//2:
        ans += '2'
        solve(r, c, size//2, rr, cc)
    elif rr < r+size//2 and cc >= c+size//2:
        ans += '1'
        solve(r, c+size//2, size//2, rr, cc)
    elif rr >= r+size//2 and cc < c+size//2:
        ans += '3'
        solve(r+size//2, c, size//2, rr, cc)
    else:
        ans += '4'
        solve(r+size//2, c+size//2, size//2, rr, cc)
        
size = 2 ** int(D)
R, C = 0, 0
find(0, 0, 0, size)

C += dc
R -= dr

ans = ''
if 0 <= R < size and 0 <= C < size:
    solve(0, 0, size, R, C)
else:
    print(-1)



