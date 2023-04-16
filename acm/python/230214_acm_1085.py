x, y, w, h = map(int, input().split())

sol = 0
xmin = min(abs(x-0), abs(x-w))
ymin = min(abs(y-0), abs(y-h))
sol = min(xmin, ymin)

print(sol)