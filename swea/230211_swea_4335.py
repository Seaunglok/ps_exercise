T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    Boxes = [list(map(int, input().split())) for _ in range(N)]
    XY = 0
    YZ = 1
    ZX = 2
    dp = [[[0] * 21 for _ in range(3)] for _ in range(20)]
    visit = [0] * 20
    max_height = 0
 
    def stackable(bx1, by1, bx2, by2):
        return (bx1 >= bx2 and by1 >= by2) or (bx1 >= by2 and by1 >= bx2)
 
    def getHeight(box, ax):
        if ax == XY:
            return box[2]
        elif ax == YZ:
            return box[0]
        else:
            return box[1]
 
    def dfs(boxBottom, boxX, boxY, boxSide, numstack, height):
        global max_height
 
        if height > max_height:
            max_height = height
        if numstack == N:
            return
        if dp[boxBottom][boxSide][numstack] > height:
            return
        dp[boxBottom][boxSide][numstack] = height
 
        for i in range(N):
            if visit[i]:
                continue
            visit[i] = 1
            if stackable(Boxes[i][0], Boxes[i][1], boxX, boxY):
                dfs(i, Boxes[i][0], Boxes[i][1], XY, numstack+1, height+getHeight(Boxes[i], XY))
            if stackable(Boxes[i][1], Boxes[i][2], boxX, boxY):
                dfs(i, Boxes[i][1], Boxes[i][2], YZ, numstack+1, height+getHeight(Boxes[i], YZ))
            if stackable(Boxes[i][2], Boxes[i][0], boxX, boxY):
                dfs(i, Boxes[i][2], Boxes[i][0], ZX, numstack+1, height+getHeight(Boxes[i], ZX))
            visit[i] = 0
 
    dfs(0, 0, 0, XY, 0, 0)
    print(f'#{t} {max_height}')