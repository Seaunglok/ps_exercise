while (1):
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        exit(0)
    mat = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    # print(mat)
    
    def solve():
        ans = 0
        for r in range(1, N):
            for c in range(1, M+1):
                if mat[r][c]:
                    mat[r][c] = mat[r-1][c] + 1
        
        for r in range(N):
            stack = [0]
            # print(arr)
            for c in range(1, M+2):
                while stack and mat[r][c] <= mat[r][stack[-1]]:
                    height = mat[r][stack[-1]]
                    stack.pop()
                    if stack:
                        width = c - stack[-1] - 1
                    else:
                        width = c
                    ans = max(ans, height*width)
                stack.append(c)
        return ans    
    
    print(solve())
