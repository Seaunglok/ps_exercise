import math

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

def cal(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

MIN = 10**9
SC = cal(Ax, Ay, Az, Cx, Cy, Cz)
EC = cal(Bx, By, Bz, Cx, Cy, Cz)

while True:
    mx = (Ax + Bx) / 2
    my = (Ay + By) / 2
    mz = (Az + Bz) / 2
    
    KC = cal(mx, my, mz, Cx, Cy, Cz)
    
    if abs(MIN - KC) <= 1e-6:
        print(f'{KC:.10f}')
        break
    
    MIN = min(KC, MIN)
    
    if SC < EC:
        Bx, By, Bz = mx, my, mz
        EC = KC
    else:
        Ax, Ay, Az = mx, my, mz
        SC = KC
